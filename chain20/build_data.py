#!/usr/bin/env python3
"""Build the deterministic, static chain20 data bundle for GitHub Pages."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOWNLOADS = {
    "baseline.jsonl": "baseline.jsonl",
    "interruptions.jsonl": "interruptions.jsonl",
    "manifest.json": "manifest.json",
    "validation-report.json": "validation/report.json",
    "freshness-report.json": "validation/freshness_report.json",
    "content-audit.json": "validation/content_audit.json",
    "review.md": "review.md",
    "canonical-checksums.sha256": "checksums.sha256",
}


def read_json(path: Path) -> object:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_public_freshness(source: Path, freshness: dict) -> None:
    """Publish the audit evidence without workstation-specific absolute paths."""
    public = json.loads(json.dumps(freshness))
    public["corpus"] = "chain20_fresh_v1"
    public["scope"]["prior_sources"] = {
        "avd": "data/ego_duplex/avd (excluding chain20_fresh_v1)",
        "claude_job": "supplied Claude job artifacts",
        "claude_transcript": "supplied Claude session transcript",
        "file_filter": freshness["scope"]["prior_sources"]["file_filter"],
    }
    public["prior_index"]["path"] = "validation/freshness_prior_index.json"
    for item in public["snapshot"]["source_file_hashes"]:
        item["path"] = str(Path(item["path"]).relative_to(source))
    for item in public["snapshot"]["utterances"]:
        item["source"] = str(Path(item["source"]).relative_to(source))
    with (HERE / "freshness-report.json").open(
        "w", encoding="utf-8", newline="\n"
    ) as handle:
        json.dump(public, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source",
        type=Path,
        help="Path to the canonical chain20_fresh_v1 directory",
    )
    args = parser.parse_args()
    source = args.source.resolve()

    report_path = source / "validation/report.json"
    report = read_json(report_path)
    freshness = read_json(source / "validation/freshness_report.json")
    content_audit = read_json(source / "validation/content_audit.json")
    episodes = []

    for entry in report["episodes"]:
        clip = entry["clip"]
        episode_dir = source / "episodes" / clip
        episodes.append(
            {
                "baseline": read_json(episode_dir / "baseline.json"),
                "interruptions": read_json(episode_dir / "interruptions.json"),
                "audit": read_json(episode_dir / "audit.json"),
            }
        )

    summary = {key: value for key, value in report.items() if key != "episodes"}
    summary["source_duration_s"] = sum(
        float(item["baseline"]["duration_s"]) for item in episodes
    )
    summary["freshness_audit"] = {
        "status": freshness["status"],
        "files": freshness["scan"]["files"],
        "bytes": freshness["scan"]["bytes"],
        "exact_matches": freshness["result"]["exact_current_utterance_count"],
        "near_matches": freshness["result"]["near_current_utterance_count"],
        "near_threshold": freshness["method"]["near_threshold_inclusive"],
        "utterances": freshness["snapshot"]["utterance_count"],
    }
    summary["content_audit_status"] = content_audit["status"]
    payload = {"summary": summary, "episodes": episodes}
    with (HERE / "data.json").open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(payload, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write("\n")

    for destination_name, source_relative in DOWNLOADS.items():
        shutil.copyfile(source / source_relative, HERE / destination_name)
    write_public_freshness(source, freshness)
    review_path = HERE / "review.md"
    review_path.write_text(
        "\n".join(line.rstrip() for line in review_path.read_text().splitlines())
        + "\n",
        encoding="utf-8",
        newline="\n",
    )

    integrity_files = sorted(["data.json", *DOWNLOADS])
    with (HERE / "checksums.sha256").open(
        "w", encoding="utf-8", newline="\n"
    ) as handle:
        for filename in integrity_files:
            handle.write(f"{sha256(HERE / filename)}  {filename}\n")


if __name__ == "__main__":
    main()
