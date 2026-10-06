# Counting QA feasibility on the 20-episode pilot

This is a conservative proposal census over the original Nymeria evidence. It does not alter the released chains and it does not label any counting item strict.

## What can be counted

Two different tasks must stay separate:

- **Event count:** count verified state transitions, such as a drawer leaf changing from closed to open. Reopening the same leaf after a close counts again.
- **Unique physical object count:** count distinct identities, such as how many different drawers exist. Repeatedly opening one drawer still counts as one object.

The narration is useful for proposing event counts. It cannot establish exact unique-object counts from the extracted tracks: `Storage` merges drawers, cabinets, shelves, and dressers; `Door` also includes door casings and window frames; and there is no phone class.

## Conservative narration census

| Family | Count | Meaning |
|---|---:|---|
| Drawer opens | **19** + 2 flagged | 14 furniture/kitchen/bathroom and 5 appliance drawers |
| Phone pickup/use | **0** | One incidental phone mention, with no interaction |
| Cabinet opens | **12 accesses / 14 leaves** | Two accesses open two cabinet leaves |
| Structural/room doors | **10** | 9 if a closet door is excluded |
| Appliance doors | **8 accesses / 9 leaves** | 6 refrigerator visits and 2 dishwasher visits |

The full row-by-row clustering audit is in [narration_count_census.md](../counting/narration_count_census.md). Duplicate Nymeria paraphrases count once. Failed attempts, `about to` actions, another person's actions, boundary-censored transitions, and conflicting target labels do not enter the conservative total.

## Frame spot checks

Three representative reviews show the main cases:

1. **Clean duplicate cluster:** Amy Snow's lower oven drawer visibly changes from closed to open around 132.3 s. Three overlapping narration rows describe that one event.
2. **Insufficient bracket:** Grace's utensil drawer is already open throughout the available review window. Those frames verify identity and open state, but cannot prove the earlier transition.
3. **Lexical false positive:** Amanda's narration mentions an organizer under a wall cabinet. The frames show a small box/organizer action while the cabinet remains closed.

These checks support the pipeline design; they do not estimate an audited pass rate. Planning ranges before a complete dense review are 14–18 drawer items, 8–11 cabinet items, 8–10 structural-door items, and 6–8 appliance-door items. Treat those ranges as workload estimates.

## Confidence

- **High** that the candidate totals represent the 1,662 extracted narration rows after duplicate clustering.
- **Medium** that a narrated event is the exact physical event shown in the video before dense review.
- **Low** for unique drawer, cabinet, or door counts from raw tracks alone.
- **Low** for claiming there was no phone use. The narration has no phone event and the track taxonomy cannot see phones.

For release, each positive needs dense frames showing the pre-state, the transition, and the post-state. Each count question also needs a full-window negative sweep so an omitted or unnarrated event cannot make the answer key too small.
