# Conservative narration-level event census (20 clips)

This census audits the 1,662 original Nymeria narration rows extracted for the 20 selected clips (4,380 seconds total). It is a candidate census, not visually verified event ground truth.

## Primary counts

| Family | Conservative count | Alternate scope | Notes |
|---|---:|---:|---|
| Drawer-opening transitions | 19 | 21 including two flagged candidates | 14 furniture/kitchen/bathroom drawers and 5 appliance drawers. The flags are one clip-boundary event and one drawer-versus-organizer label conflict. |
| Phone pickup/use episodes | 0 | 1 incidental phone mention | The single phone row says a hand rests *by* the phone; it does not describe pickup or use. |
| Cabinet/cupboard access episodes | 12 | 14 individual door-leaf transitions | Two accesses explicitly open two leaves of the same cabinet. |
| Structural/room door-opening episodes | 10 | 9 if a closet door is excluded | Wearer actions only. |
| Appliance-door opening episodes | 8 | 9 individual door-leaf transitions | Kept separate from structural doors: 6 refrigerator visits and 2 dishwasher openings. |

For a natural question such as “How many times did I open a cabinet?”, use access episodes (12). For “How many cabinet doors did I open?”, use leaf transitions (14). This distinction prevents double counting a single visit to a two-door cabinet or refrigerator.

If `door` is defined broadly to include room/closet doors and appliance doors, the conservative total is 18 opening episodes (19 individual leaves). Cabinet doors remain in the cabinet family rather than being counted again as generic doors.

## Per-clip conservative counts

`Cabinet` is `access episodes / door-leaf transitions`. `Door` is structural openings. Appliance doors are listed separately. Counts do not include flagged candidates.

| Clip (short name) | Drawer | Phone pickup/use | Cabinet | Door | Appliance door | Flags |
|---|---:|---:|---:|---:|---:|---|
| Angela Harrell | 2 | 0 | 2 / 2 | 0 | 0 | — |
| Dawn Heath | 0 | 0 | 0 / 0 | 1 | 0 | One failed cabinet-opening attempt excluded |
| Anthony Perez | 1 | 0 | 0 / 0 | 0 | 0 | — |
| Amy Crawford | 0 | 0 | 1 / 2 | 1 | 0 | One failed cabinet-opening attempt excluded |
| Julie Taylor | 0 | 0 | 0 / 0 | 0 | 0 | — |
| Dominique Frye | 0 | 0 | 0 / 0 | 0 | 0 | — |
| Rebecca Ward | 0 | 0 | 0 / 0 | 0 | 0 | — |
| Elizabeth Morgan | 0 | 0 | 0 / 0 | 1 | 0 | — |
| Grace Randolph | 7 | 0 | 2 / 2 | 0 | 0 | — |
| Allen Evans | 1 | 0 | 0 / 0 | 0 | 0 | One incidental phone mention, no interaction |
| Ashley Reyes | 0 | 0 | 0 / 0 | 5 | 0 | A colleague’s cabinet action excluded |
| Alicia Drake | 0 | 0 | 0 / 0 | 0 | 0 | — |
| Joshua Smith | 1 | 0 | 3 / 4 | 2 | 1 | One drawer opening crosses the clip start and is excluded |
| Dean Krause | 0 | 0 | 0 / 0 | 0 | 0 | — |
| Amanda Rodgers | 5 | 0 | 3 / 3 | 0 | 5 | Four refrigerator visits and one dishwasher opening; one drawer/organizer label conflict; one cabinet event mostly before clip start |
| Amy Snow | 2 | 0 | 1 / 1 | 0 | 2 | First refrigerator visit opens two leaves (3 appliance leaves across 2 visits) |
| Nicholas Hicks | 0 | 0 | 0 / 0 | 0 | 0 | — |
| Alexandria Griffith | 0 | 0 | 0 / 0 | 0 | 0 | — |
| Paul Nguyen | 0 | 0 | 0 / 0 | 0 | 0 | — |
| Brittney Goodwin | 0 | 0 | 0 / 0 | 0 | 0 | Partial door closing only; no opening counted |
| **Total** | **19** | **0** | **12 / 14** | **10** | **8** | Two flagged drawer candidates |

## Duplicate-row clustering rule

1. Generate a proposal only from an explicit transition phrase: `opens`, `opening`, `pulls ... open`, or an unambiguous pull-then-push drawer cycle. `About to`, `reaches for`, `holds`, `touches`, `walks toward`, and `tries but does not open` do not qualify.
2. Require the wearer (`C`) to perform the action. Actions performed by a colleague are excluded.
3. Cluster proposals within the same clip and family when their narration intervals overlap, identify the same target, and describe the same continuous hand action. Exact-time multi-annotator paraphrases collapse to one event.
4. Merge an adjacent progressive continuation such as “opens the drawer” followed by “is opening the drawer” when there is no intervening close.
5. Do not merge when the text says `another`/`other`, names a different target, or describes a close followed by a new reopen cycle.
6. For two leaves opened during one continuous access, retain one access episode plus two leaf transitions. This supports both natural QA scopes without changing the underlying evidence.

## Audited examples

- Angela drawer rows at 99.089–104.088 and 104.088–109.087 describe two events: the first drawer is closed before a second drawer is opened.
- Anthony rows at 72.339–77.339 and 77.339–81.238 describe one bathroom-drawer event; the second row is a progressive continuation and close.
- Grace row 80.377–85.376 explicitly opens one drawer, closes it, then opens and closes another, so it contributes two events. The rows at 152.398–157.398 and 157.398–162.397 are one continued event and contribute one.
- Joshua has three paraphrases at -4.238–0.761 for one drawer event. It is flagged rather than counted because the opening may occur before clip time zero.
- Amanda rows at 317.149–323.148 describe one physical pullout but disagree on `kitchen drawer` versus `organizer`; it remains a flagged candidate.
- Joshua’s upper cabinet narration explicitly opens the left door and then the right door. It contributes one cabinet access and two leaf transitions.
- Amy Snow’s three same-time refrigerator paraphrases at 24.815–29.814 collapse to one refrigerator visit, while preserving two opened leaves.
- Amanda’s repeated rows at 5.199–15.197, 30.195–35.694, 57.157–62.156, and 112.148–117.147 collapse to four separate refrigerator-opening visits; the later dishwasher rows collapse to one appliance-door opening.

## Confidence and limitations

Confidence is high that the table correctly represents the extracted narration rows after duplicate removal. Confidence is only medium that it equals the physical video truth: narration may omit a short interaction, use the wrong object label, or span a clip boundary. Phone behavior is especially vulnerable to omission because glancing, tapping, and brief handling may not be narrated.

The object-track taxonomy does not supply a phone class in these extracted files. Its generic `Screen` class explicitly excludes mobile-phone screens, so it cannot be used to raise the phone count.

Before release as counting QA, every candidate should pass a visual gate showing the pre-state, the actual transition, and the post-state. Low-confidence or boundary candidates should be rejected unless dense-frame review resolves them. The original source paths recorded in the extraction files are not mounted in this workspace; the extracted rows retain source episode IDs and annotation SHA-256 values for provenance.
