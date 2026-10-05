# Fresh 20-episode paired chain build

Validation: **PASS**
Sources: **20** · variants: **40** · baseline turns: **108** · interruption devices: **57**

Each source has a clean-handoff `baseline.json` and an `interruptions.json` whose `base_turns` are byte-equivalent JSON values. Questions were authored from `briefs_v4` and overlay-free clean frames; prior generated questions were excluded as authoring inputs.

This delivery is chain-only. Device triggers use live assistant word progress. Oracle onset stays null until measured TTS retiming, so no fixed-time overlap is claimed.

## Validation evidence

- Errors: 0; warnings: 0
- Verbatim raw annotation rows checked: 293
- Baseline pairwise lexical leak checks: 88
- Semantic-device leak checks: 40
- Base-family mix: `{"action_narration": 15, "episodic_memory": 93}`
- Device mix: `{"cross_question": 13, "plain_backchannel": 17, "question_change_related": 6, "same_question_refinement": 15, "topic_switch": 6}`
- Prior-artifact freshness scan: 31,671 files / 828,368,549 bytes; exact matches=0; near matches=0 at threshold ≥0.88
- Independent post-repair content audit: `pass`

Corrections made during pixel audit include a silver toaster, generic laundry machines where washer-versus-dryer was not visually settled, and a generic red cleaning machine where narration said floor scrubber but pixels resembled an upright vacuum. The disputed fine labels are quarantined rather than used as gold.

Duration, first-trigger HOI, and object-location proposals remain unshipped when their dense boundary, first-transition, or every-frame absence checks were unavailable.

## Episode index

| clip | seconds | turns | devices | device types | rejected / dense-review |
|---|---:|---:|---:|---|---:|
| `20231101_s0_joshua_smith_act1_5eipiv__T10_at_450` | 600 | 10 | 5 | cross_question:1, plain_backchannel:1, question_change_related:1, same_question_refinement:1, topic_switch:1 | 4 |
| `20231101_s1_dean_krause_act3_682crw__T2_at_720` | 120 | 3 | 2 | plain_backchannel:1, same_question_refinement:1 | 3 |
| `20231107_s0_amy_snow_act3_y044ox__T3_at_90` | 180 | 6 | 3 | cross_question:1, plain_backchannel:1, same_question_refinement:1 | 2 |
| `20231106_s1_amanda_rodgers_act4_kli4b8__T10_at_420` | 600 | 10 | 5 | cross_question:2, plain_backchannel:1, same_question_refinement:1, topic_switch:1 | 3 |
| `20231108_s0_nicholas_hicks_act3_j7bheq__T10_at_90` | 600 | 10 | 5 | cross_question:1, plain_backchannel:1, question_change_related:1, same_question_refinement:1, topic_switch:1 | 6 |
| `20231121_s0_alexandria_griffith_act2_t3030z__T2_at_900` | 120 | 3 | 3 | cross_question:1, plain_backchannel:1, question_change_related:1 | 3 |
| `20231128_s0_paul_nguyen_act1_5i49b8__T2_at_720` | 120 | 3 | 1 | plain_backchannel:1 | 2 |
| `20230609_s0_angela_harrell_act2_42epvf__T2_at_180` | 120 | 3 | 1 | same_question_refinement:1 | 1 |
| `20230713_s1_amy_crawford_act4_7nrb9d__T2_at_240` | 120 | 3 | 2 | plain_backchannel:1, same_question_refinement:1 | 1 |
| `20230725_s1_julie_taylor_act4_iemk0l__T2_at_120` | 120 | 3 | 2 | plain_backchannel:1, same_question_refinement:1 | 2 |
| `20231129_s0_brittney_goodwin_act4_j3rly0__T3_at_810` | 180 | 6 | 3 | plain_backchannel:1, question_change_related:1, topic_switch:1 | 4 |
| `20230615_s0_dawn_heath_act1_9s9e13__T2_at_930` | 120 | 3 | 2 | cross_question:1, plain_backchannel:1 | 1 |
| `20230707_s0_anthony_perez_act0_wghngx__T3_at_930` | 180 | 6 | 1 | same_question_refinement:1 | 2 |
| `20231003_s1_allen_evans_act2_7pj863__T3_at_120` | 180 | 6 | 3 | cross_question:1, plain_backchannel:1, same_question_refinement:1 | 2 |
| `20231025_s1_alicia_drake_act3_dja4ib__T2_at_120` | 120 | 3 | 2 | plain_backchannel:1, same_question_refinement:1 | 1 |
| `20230817_s1_rebecca_ward_act2_39a7o2__T3_at_870` | 180 | 6 | 3 | cross_question:1, plain_backchannel:1, same_question_refinement:1 | 6 |
| `20230905_s1_elizabeth_morgan_act2_nfmn6i__T3_at_90` | 180 | 6 | 1 | cross_question:1 | 2 |
| `20230807_s0_dominique_frye_act3_lysseo__T3_at_840` | 180 | 6 | 3 | plain_backchannel:1, question_change_related:1, same_question_refinement:1 | 4 |
| `20230928_s0_grace_randolph_act4_j1cw74__T3_at_690` | 180 | 6 | 5 | cross_question:1, plain_backchannel:1, question_change_related:1, same_question_refinement:1, topic_switch:1 | 2 |
| `20231004_s1_ashley_reyes_act1_3d7yqq__T3_at_690` | 180 | 6 | 5 | cross_question:2, plain_backchannel:1, same_question_refinement:1, topic_switch:1 | 1 |

Rejected evidence ledger: needs_dense_review=17, quarantined=34, rejected=1.

## Dialogue review

### `NymeriaPlus_v1.0_20231101_s0_joshua_smith_act1_5eipiv__T10_at_450`

Baseline:

- `joshua_t01` 45.0s · `episodic_memory` · What did I do at the coffee maker earlier? → **You reached to the coffee maker's controls and switched it on.**
- `joshua_t02` 125.0s · `episodic_memory` · Where had I taken the mugs from earlier? → **You had taken the mugs out of the dishwasher and set them on the counter.**
- `joshua_t03` 202.0s · `episodic_memory` · What did I set beside the sink earlier? → **You set a white dinner plate on the counter beside the kitchen sink.**
- `joshua_t04` 225.0s · `episodic_memory` · What did I put into the dishwasher a moment ago? → **You put the black frying pan back into the open dishwasher.**
- `joshua_t05` 290.0s · `episodic_memory` · Which appliance did I fill and switch on earlier? → **You filled the electric kettle at the kitchen sink, then switched it on.**
- `joshua_t06` 334.0s · `episodic_memory` · Who did I hand the stuffed toy to? → **You handed the stuffed toy to your peer at the dining table.**
- `joshua_t07` 390.0s · `episodic_memory` · How many beds did I strip? → **You stripped bedding from two different beds in two separate bedrooms.**
- `joshua_t08` 446.0s · `episodic_memory` · Which room did I check just now? → **You checked the small hallway bathroom with the toilet and sink.**
- `joshua_t09` 526.0s · `episodic_memory` · What did I find when I looked behind the bathroom door downstairs? → **You found a washing machine behind the downstairs bathroom door.**
- `joshua_t10` 593.0s · `episodic_memory` · What did I do at the downstairs kitchen window? → **You opened the curtain, looked outside, and then closed it again.**

Output-contingent devices:

- `joshua_e01` on `joshua_t02` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `joshua_e02` on `joshua_t04` · `question_change_related` after 5 words · Actually, what did I pick up after closing it? → **You picked up the gray towel from the kitchen counter.**
- `joshua_e03` on `joshua_t05` · `cross_question` after 5 words · And where had I filled it? → **You filled the kettle with water at the kitchen sink.**
- `joshua_e04` on `joshua_t06` · `same_question_refinement` after 5 words · The person at the dining table? → **Yes. You gave it to the peer seated at the dining table.**
- `joshua_e05` on `joshua_t09` · `topic_switch` after 5 words · Forget that—what did I point out over the kitchen island? → **You pointed out the chandelier hanging above the kitchen island.**

Held out:

- `needs_dense_review` · Ask how long the bed-stripping task took. — Duration boundaries were not swept densely enough to clear the duration gate; the count question is supported without estimating time.
- `needs_dense_review` · Ask whether an object stayed absent after a bedroom placement. — No all-frame same-object absence sweep was completed, so no absence claim is shipped.
- `needs_dense_review` · Fire an HOI reminder when the kettle or bedding action begins. — There is no separately authored 45-second precondition instruction plus dense first-trigger verification in this chain.
- `quarantined` · Answer that only a washing machine was behind the downstairs bathroom door. — The brief names one washing machine, while the clean pixels show a side-by-side laundry pair; the shipped answer asserts only that a washing machine was present and does not claim it was the sole appliance.

### `NymeriaPlus_v1.0_20231101_s1_dean_krause_act3_682crw__T2_at_720`

Baseline:

- `dean_t01` 48.0s · `action_narration` · What am I busy doing in here right now? → **You're rearranging the living room by moving the long sofa into place.**
- `dean_t02` 75.0s · `episodic_memory` · What did I do with the single-seat chair a moment ago? → **You carried it across the living room and set it down.**
- `dean_t03` 110.0s · `episodic_memory` · Which seat did I put the pillows on first? → **The pillow sequence started on the long sofa with two, then ended on the single-seat chair.**

Output-contingent devices:

- `dean_e01` on `dean_t01` · `plain_backchannel` after 5 words · Right. → **no response; continue parent**
- `dean_e02` on `dean_t03` · `same_question_refinement` after 5 words · Just how many went on the first seat? → **Two pillows went on the first seat.**

Held out:

- `needs_dense_review` · Ask for the exact duration of moving the long sofa. — The action recurs in several bouts and no dense start/end boundary audit was completed.
- `needs_dense_review` · Ask whether the first side table remains absent from the center area. — Object-absence requires an all-frame sweep and matched positive control that were not completed.
- `quarantined` · Use the sparse lamp track as a memory target. — The lamp is visible for only about half a second and is too weak for a natural, reliable question.

### `NymeriaPlus_v1.0_20231107_s0_amy_snow_act3_y044ox__T3_at_90`

Baseline:

- `q01` 51.0s · `episodic_memory` · What was I just checking on that box? → **You were reading the label on the Hungry Jack pancake-mix box.**
- `q02` 88.0s · `episodic_memory` · How did I open those joined food packs? → **You cut open the joined food packs with a kitchen knife.**
- `q03` 110.0s · `episodic_memory` · Before I started peeling the tape, which appliance did I check twice? → **You opened the refrigerator twice and took the food packs out the second time.**
- `q04` 135.0s · `episodic_memory` · What was I reading before opening that drawer? → **You had been reading the torn label from the food-package wrapping.**
- `q05` 155.0s · `episodic_memory` · What did I take from the bottom oven drawer? → **You pulled out a baking pan and set it on the kitchen counter.**
- `q06` 176.0s · `episodic_memory` · Which appliance did I switch on after setting down the pan? → **You switched on the stove and then went back to reading the food label.**

Output-contingent devices:

- `e01` on `q01` · `plain_backchannel` after 5 words · Right. → **no response; continue parent**
- `e02` on `q02` · `same_question_refinement` after 5 words · Just tell me what tool I'm using. → **You're using a kitchen knife.**
- `e03` on `q03` · `cross_question` after 5 words · And which hand did I use to take them out? → **You used your left hand to take them out.**

Held out:

- `quarantined` · The wearer is reading the expiry date at q01. — Narration proposes an expiry-date check, but the fine print is unreadable in clean frames; the shipped answer only claims label reading.
- `quarantined` · A microwave completion beep should trigger a proactive turn. — The candidate is not needed for this fixed-turn build and was not independently verified against synchronized audio and pixels.

### `NymeriaPlus_v1.0_20231106_s1_amanda_rodgers_act4_kli4b8__T10_at_420`

Baseline:

- `q01` 57.2s · `episodic_memory` · What did I just sprinkle over the flatbread? → **You sprinkled grated cheese from the open bag over the flatbread in the pan.**
- `q02` 144.0s · `episodic_memory` · Before I brought the first plate to the table, what did I put away in the fridge? → **Before carrying the plate over, you put the peanut butter jar and the butter container into the refrigerator.**
- `q03` 200.0s · `action_narration` · Can you tell what I'm making? → **You're cooking a flatbread in the pan on the stove right now.**
- `q04` 304.0s · `episodic_memory` · Before I handed that plate over, what had I just finished? → **You moved the cooked tortilla onto a white plate and then turned the stove off.**
- `q05` 330.0s · `action_narration` · What am I preparing right now? → **You're preparing tea with a tea bag and the electric kettle.**
- `q06` 411.0s · `episodic_memory` · What was I trying to sort out with this kettle? → **You were repositioning the kettle on its powered base and checking how the cord fit.**
- `q07` 445.2s · `episodic_memory` · What did I throw away after putting the tea bag in the mug? → **You threw the empty tea sachet into the trash bin beside the refrigerator.**
- `q08` 480.2s · `episodic_memory` · Where did I go before coming back to the kitchen? → **You went into the living room, set the drink on the center table, and then returned.**
- `q09` 534.8s · `action_narration` · What kitchen task am I doing right now? → **You're loading utensils from the sink into the dishwasher.**
- `q10` 575.0s · `episodic_memory` · What had I fixed before taking out the trash? → **You reattached a loose wooden piece to the chopping board, then loaded the board into the dishwasher.**

Output-contingent devices:

- `d01` on `q01` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `d02` on `q02` · `same_question_refinement` after 5 words · Just the two containers—what were they? → **They were the peanut butter jar and the butter container.**
- `d03` on `q03` · `cross_question` after 5 words · Which utensil am I using? → **You're using a spatula.**
- `d04` on `q06` · `cross_question` after 7 words · Was the kettle switched on at that point? → **Yes. Its blue indicator was lit while you checked the base and cord.**
- `d05` on `q07` · `topic_switch` after 7 words · Wait—what machine had I switched on before buttering the toast? → **You had switched on the toaster.**

Held out:

- `needs_dense_review` · Ask for the exact duration of tortilla cooking. — Not authored because both activity boundaries would require a dense 15 fps review.
- `needs_dense_review` · Ask where the peanut butter remained at 130 s. — Not authored as object memory because no every-frame absence window was run.
- `needs_dense_review` · Ask where the finished hot drink was left. — Replaced because a placement question requires a dense every-frame absence and missed-pickup check.

### `NymeriaPlus_v1.0_20231108_s0_nicholas_hicks_act3_j7bheq__T10_at_90`

Baseline:

- `q01` 50.0s · `action_narration` · What am I working on right now? → **You're taking party supplies out of the box and sorting them into separate groups.**
- `q02` 115.0s · `episodic_memory` · What did I do with the box once it was empty? → **You lifted the empty box off the center table and moved it out of the way.**
- `q03` 175.0s · `action_narration` · What am I setting up over here? → **You're laying paper plates in a neat row along the cabinet beneath the television.**
- `q04` 235.0s · `action_narration` · What part of the setup am I working on now? → **You're unpacking another batch of party decorations as you continue setting up the room.**
- `q05` 295.0s · `action_narration` · What task am I on at the moment? → **You're decorating the cabinet beneath the television with birthday signs.**
- `q06` 355.0s · `episodic_memory` · What did I pick up after bringing the decorations back to the center table? → **You picked up the roll of adhesive tape from the center table and began peeling off pieces.**
- `q07` 420.0s · `episodic_memory` · Which small decoration was I handling by the door? → **You were handling a black-and-pink polka-dot bow beside the living-room door.**
- `q08` 475.0s · `episodic_memory` · What was I carrying as I moved past the sofa? → **You were carrying several party cutouts and the blue roll of tape.**
- `q09` 535.0s · `episodic_memory` · What did I do with the tape while I had those large cutouts? → **You rolled a piece of tape and pressed it onto the back of a large cutout.**
- `q10` 580.0s · `episodic_memory` · What did I do with the spare stack after laying out the plates? → **You carried the remaining paper plates away from the cabinet and back toward the center table.**

Output-contingent devices:

- `e01` on `q01` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `e02` on `q03` · `same_question_refinement` after 5 words · I mean, which surface am I putting them on? → **You're putting the plates on the cabinet beneath the television.**
- `e03` on `q09` · `cross_question` after 5 words · And where was I holding the cutout? → **You were holding it up in front of the living-room window.**
- `e04` on `q10` · `question_change_related` after 5 words · Actually, forget that—what did I pick up next? → **You picked up a pack of paper napkins.**
- `e05` on `q04` · `topic_switch` after 5 words · Forget that—where was the refrigerator again? → **It was in the kitchen beside the long counter.**

Held out:

- `quarantined` · The empty box landed at an exact named floor position. — The clean 2 fps frames show it leave the table but the landing is occluded; q02 therefore only says it was moved out of the way.
- `quarantined` · The package at q04 contains a specifically named napkin or banner set. — Narration variants disagree on the package identity and the pixels do not resolve the print; q04 keeps 'party supplies.'
- `quarantined` · The plate-layout activity lasted about one minute. — The 2 fps clean-frame cache brackets the activity, but no independent dense boundary pass or corpus duration-baseline disclosure was available; the duration proposal was quarantined instead of shipped.
- `quarantined` · A party cutout was definitively attached to the hallway wall around 450-470 seconds. — The frames clearly show the cutouts and tape being carried, but they do not settle contact and release against that wall; q08 asks only what was carried.
- `quarantined` · The spare plate stack visibly landed on the center table. — The carry back toward the table is clear, but the contact instant is occluded; q10 avoids the exact landing claim.
- `quarantined` · The pink cutouts depict a specifically named licensed character. — Color and black-and-white accents are clear, but the clean frames do not resolve a character identity; q09 asks only the verified appearance.

### `NymeriaPlus_v1.0_20231121_s0_alexandria_griffith_act2_t3030z__T2_at_900`

Baseline:

- `alexandria_t01` 60.0s · `episodic_memory` · What did I do after moving the pillows around? → **You carried the stuffed toys over and then straightened the blanket.**
- `alexandria_t02` 83.0s · `episodic_memory` · What was my peer doing to my right arm earlier? → **Your peer tightened and repositioned the strapped device on your right arm.**
- `alexandria_t03` 118.0s · `episodic_memory` · What did I do after carrying the game box into the bedroom? → **You set the game box on the wall shelf and walked back out.**

Output-contingent devices:

- `alexandria_e01` on `alexandria_t01` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `alexandria_e02` on `alexandria_t02` · `question_change_related` after 5 words · Actually, where did I go right after that? → **You walked to the trash bin beside the kitchen counter.**
- `alexandria_e03` on `alexandria_t03` · `cross_question` after 5 words · And what did I pick up after I came back? → **You picked up the tablet and a sheet of paper from the center table.**

Held out:

- `quarantined` · Name the exact brand or purpose of the arm device. — Pixels and narration establish a strapped device being adjusted, but do not license a brand or medical purpose.
- `needs_dense_review` · Ask how long the sofa arranging lasted. — The activity has overlapping pillow, toy, and blanket sub-actions; dense boundary review was not completed.
- `needs_dense_review` · Ask whether the game box stays absent from the living room. — A full post-placement absence sweep with a positive control was not performed.

### `NymeriaPlus_v1.0_20231128_s0_paul_nguyen_act1_5i49b8__T2_at_720`

Baseline:

- `q01` 52.5s · `episodic_memory` · What were those machines I just walked past? → **You walked past two front-loading laundry machines along the left side of the garage.**
- `q02` 80.0s · `episodic_memory` · What was I checking on the bed? → **You were lifting and rearranging the pillows at the head of the bed.**
- `q03` 106.0s · `episodic_memory` · Where did those stairs bring me? → **They brought you upstairs into the living-room hallway beside the kitchen.**

Output-contingent devices:

- `d01` on `q02` · `plain_backchannel` after 5 words · Yeah. → **no response; continue parent**

Held out:

- `quarantined` · Call both garage appliances washing machines. — The brief uses that plural label, but pixels only support two front-loading laundry machines and may show a washer/dryer pair.
- `quarantined` · Ask for the identity of the handheld item on the bathroom shelf. — Held out because the pixels do not cleanly distinguish the proposed blower from other shelf objects.

### `NymeriaPlus_v1.0_20230609_s0_angela_harrell_act2_42epvf__T2_at_180`

Baseline:

- `q01` 47.0s · `episodic_memory` · What did I just bring up from the lower cabinet? → **You brought the silver toaster up from the lower kitchen cabinet with both hands.**
- `q02` 72.0s · `episodic_memory` · What did I do after setting it on the counter? → **You plugged the toaster into the wall and then switched the toaster on.**
- `q03` 114.1s · `episodic_memory` · Before opening the cabinet, what did I take from the drawer? → **You took a knife from the cutlery drawer beside the oven.**

Output-contingent devices:

- `d01` on `q02` · `same_question_refinement` after 5 words · Just the last step—what did I switch on? → **You switched on the toaster.**

Held out:

- `needs_dense_review` · Ask how long the toaster had been running. — Not authored because duration boundaries were not densely verified.

### `NymeriaPlus_v1.0_20230713_s1_amy_crawford_act4_7nrb9d__T2_at_240`

Baseline:

- `q01` 52.0s · `episodic_memory` · Where did I check in the bathroom? → **You checked inside the vanity cabinet and behind the shower curtain.**
- `q02` 79.0s · `episodic_memory` · What did I move onto the bedside table while I was looking around? → **While you were looking around, you moved a drinking glass and its coaster onto the bedside table.**
- `q03` 115.0s · `action_narration` · What am I checking around right now? → **You're searching around the bed, moving the pillows and blanket as you look.**

Output-contingent devices:

- `e01` on `q01` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `e02` on `q02` · `same_question_refinement` after 5 words · Just name both items. → **The drinking glass and its coaster.**

Held out:

- `quarantined` · The wearer is searching for a specifically named missing object. — The pixels and narration show a search but never establish the target object; every shipped question avoids inventing one.

### `NymeriaPlus_v1.0_20230725_s1_julie_taylor_act4_iemk0l__T2_at_120`

Baseline:

- `b01` 60.0s · `episodic_memory` · What did I do with the cup after picking it up by the sofa? → **You put the cup on the table, then picked it up again a moment later.**
- `b02` 85.0s · `episodic_memory` · What did I find on the sofa while I was holding the cup? → **You moved the pillows and found a set of keys on the sofa.**
- `b03` 115.0s · `episodic_memory` · What did I do after leaving the dining area? → **You went back upstairs and continued into the upper hallway.**

Output-contingent devices:

- `d01` on `b02` · `same_question_refinement` after 5 words · Just the item—what did I find? → **You found the keys on the sofa.**
- `d02` on `b03` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**

Held out:

- `needs_dense_review` · Ask where the cup and keys were left before going upstairs. — Not shipped because object-memory placement requires the dense every-frame absence and missed-pickup gates.
- `quarantined` · Use a track reappearance as an HOI fire. — Targets were non-unique and no dense first-transition check was run.

### `NymeriaPlus_v1.0_20231129_s0_brittney_goodwin_act4_j3rly0__T3_at_810`

Baseline:

- `brittney_t01` 45.0s · `episodic_memory` · What was I looking through earlier? → **You were looking through books and had just opened a second one.**
- `brittney_t02` 65.0s · `episodic_memory` · Which room did I leave before heading down the hallway? → **You left the living room before walking down the hallway.**
- `brittney_t03` 86.5s · `action_narration` · What's keeping me busy right now? → **You're straightening and folding the two towels on the bedroom table.**
- `brittney_t04` 109.0s · `episodic_memory` · Where did I pick up the two towels? → **You took one from the bathroom wall rack and the other from the shower-door handle.**
- `brittney_t05` 140.9s · `action_narration` · What's my current task? → **You're opening a bedroom curtain.**
- `brittney_t06` 179.0s · `episodic_memory` · What did I do at the restroom after the curtains? → **You stepped into the restroom, partly closed the door, and then came back out.**

Output-contingent devices:

- `brittney_e01` on `brittney_t03` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `brittney_e02` on `brittney_t02` · `question_change_related` after 5 words · Actually, which area did I pass through on the way? → **You crossed the dining area before reaching the hallway.**
- `brittney_e03` on `brittney_t06` · `topic_switch` after 5 words · Forget the restroom—who had I stopped to talk to before leaving the living room? → **You had stopped to talk to your peer beside the closed door.**

Held out:

- `quarantined` · Quote the remark about the white curtain. — That speech segment is timing-tier and disputed, so its words are not licensed as answer content.
- `needs_dense_review` · Ask how long towel folding lasted. — Folding and sorting overlap and no dense boundary pass has separated the activities.
- `quarantined` · Ask for the exact moment folding changed into sorting. — The clean frames show continued towel handling but do not visually separate those two fine-grained labels with enough confidence.
- `needs_dense_review` · Ask whether the books stayed on the side table until the end. — Object absence and final location require an all-frame post-handling sweep that was not completed.

### `NymeriaPlus_v1.0_20230615_s0_dawn_heath_act1_9s9e13__T2_at_930`

Baseline:

- `b01` 65.0s · `episodic_memory` · What was I moving around on the bed before I checked the closet? → **You were rearranging several pillows and propping them against the wall.**
- `b02` 90.0s · `episodic_memory` · What did I do beside the bed after checking the storage box? → **You knelt beside the bed, then stood up and walked across the room.**
- `b03` 116.0s · `episodic_memory` · Before I reached toward the towel, what did I open? → **You opened the shower curtain and stepped over toward the shower.**

Output-contingent devices:

- `d01` on `b01` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `d02` on `b03` · `cross_question` after 5 words · What was hanging inside that shower area? → **A white towel was hanging inside the shower area.**

Held out:

- `quarantined` · The wearer handed a bag to the other person. — Narration asserts it, but the transfer is not visible in the checked ego frames.

### `NymeriaPlus_v1.0_20230707_s0_anthony_perez_act0_wghngx__T3_at_930`

Baseline:

- `q01` 45.0s · `action_narration` · What task am I doing right now? → **You're moving the cleaning tools out of the living room.**
- `q02` 73.0s · `episodic_memory` · What did I put away before coming into this bathroom? → **You put the broom in the hallway closet and kept the dustpan with you.**
- `q03` 94.0s · `episodic_memory` · What did I check while I was in the bathroom? → **You touched the shower curtain, checked a drawer, and left the dustpan on the floor.**
- `q04` 115.0s · `episodic_memory` · Where did I go after putting the dustpan down? → **You left the bathroom and walked back into the living area.**
- `q05` 138.0s · `episodic_memory` · What did I bring out of the closet this time? → **You brought out a red upright cleaning machine and set it on the floor.**
- `q06` 174.0s · `episodic_memory` · What had I been doing with the red machine? → **Standing beside the red machine for several moments, you pulled more of its power cord out.**

Output-contingent devices:

- `d01` on `q06` · `same_question_refinement` after 5 words · Just the cord—what had I been doing with it? → **You had been pulling more of the power cord out from the machine.**

Held out:

- `quarantined` · Call the red machine a floor scrubber. — The brief says floor scrubber, while pixels look like an upright vacuum; shipped claims use only the shared generic category cleaning machine.
- `quarantined` · Ask about picking the broom up from the living-room floor. — The brief first puts the broom in the closet but never explains its later relocation to the floor; the inconsistent event is not shipped.

### `NymeriaPlus_v1.0_20231003_s1_allen_evans_act2_7pj863__T3_at_120`

Baseline:

- `q01` 67.0s · `episodic_memory` · Where did I look in the bedroom? → **So far in that room, you've checked under the bed, behind the pillows, and inside the bedside drawer.**
- `q02` 92.0s · `episodic_memory` · What did I check after the bedroom? → **You searched between the sofa cushions and under the blankets in the living room.**
- `q03` 112.0s · `episodic_memory` · What came after the sofa search? → **You searched through a bag and then a box filled with folded clothes.**
- `q04` 134.0s · `episodic_memory` · What was I checking by the fireplace? → **You looked behind the large floor cushion and around the speakers by the fireplace.**
- `q05` 156.0s · `episodic_memory` · What did I check on the way over to this table? → **You lifted the blanket by the stairs and then looked behind the sofa.**
- `q06` 176.0s · `episodic_memory` · What had I just finished checking? → **You had just finished checking the open board-game box and its contents.**

Output-contingent devices:

- `e01` on `q01` · `same_question_refinement` after 5 words · Just give me the three spots. → **Under the bed, behind the pillows, and inside the bedside drawer.**
- `e02` on `q02` · `plain_backchannel` after 5 words · Yeah. → **no response; continue parent**
- `e03` on `q06` · `cross_question` after 5 words · And what did I set back inside? → **You put the small packet, the black game pieces, and the game board back inside.**

Held out:

- `quarantined` · The missing target is definitely a set of keys. — Speech mentions keys, but the visual search never resolves a found target; the shipped questions test the observed search path instead of inventing a find.
- `quarantined` · The bedroom search lasted about fifty seconds. — The 2 fps cache suggests that interval, but the duration design requires dense independently tightened boundaries and a corpus baseline disclosure; the duration item was quarantined.

### `NymeriaPlus_v1.0_20231025_s1_alicia_drake_act3_dja4ib__T2_at_120`

Baseline:

- `b01` 50.0s · `episodic_memory` · What did I put into the toaster when I came to this counter? → **At the counter, you loaded two slices of bread into the toaster, one with each hand.**
- `b02` 75.0s · `episodic_memory` · How did I get the toaster started after loading the bread? → **You pushed down the lever, then leaned in and adjusted the toaster knob.**
- `b03` 116.0s · `episodic_memory` · What had I kept checking on the stove while I waited? → **You kept looking at the frying pan on the stove from across the kitchen island.**

Output-contingent devices:

- `d01` on `b01` · `same_question_refinement` after 5 words · Just the number—how many slices? → **Two slices.**
- `d02` on `b03` · `plain_backchannel` after 5 words · Right. → **no response; continue parent**

Held out:

- `quarantined` · Score how long the wearer waited for the toaster. — The activity boundaries were not tightened at dense frame rate.

### `NymeriaPlus_v1.0_20230817_s1_rebecca_ward_act2_39a7o2__T3_at_870`

Baseline:

- `rebecca_t01` 55.0s · `action_narration` · What's going on—what am I doing right now? → **You're performing a sequence of gestures and movements for your peers.**
- `rebecca_t02` 82.0s · `episodic_memory` · What did I do at the bed just now? → **You bent over at the bed and grabbed the blanket.**
- `rebecca_t03` 105.0s · `episodic_memory` · What did I do after leaving the bed? → **You turned away from the bed and walked across the open floor.**
- `rebecca_t04` 125.0s · `episodic_memory` · Which way did I turn after walking backward with my arms up? → **You ran forward and then turned counterclockwise.**
- `rebecca_t05` 145.0s · `episodic_memory` · Where did I run after bending down? → **You stood up and ran to the right across the bedroom.**
- `rebecca_t06` 179.0s · `episodic_memory` · What did I pretend to do just before holding my arm up? → **You pretended to pull something before keeping your right arm raised overhead.**

Output-contingent devices:

- `rebecca_e01` on `rebecca_t01` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `rebecca_e02` on `rebecca_t02` · `same_question_refinement` after 5 words · Just what did I grab there? → **You grabbed the blanket on the regular bed.**
- `rebecca_e03` on `rebecca_t06` · `cross_question` after 5 words · And what did I do just before that pull? → **You stepped forward into the open area and stopped.**

Held out:

- `needs_dense_review` · Ask which sports the wearer mimed during charades. — The action narration names sports, but the wearer's own full-body gestures are mostly outside the egocentric frames; pixels cannot independently clear the HOI labels.
- `quarantined` · Ask whether the wearer was pretending to be shot. — The body pose is not visible enough in the glasses view to validate that semantic action independently.
- `needs_dense_review` · Ask how long the charades round lasted. — The clip begins and ends during the broader game, so both duration boundaries are unavailable.
- `quarantined` · Ask who 'Ivan' refers to. — The agreed speech contains the name but does not ground its referent in pixels or dialogue.
- `quarantined` · Use recalled-speech questions as base turns. — The five cited chain designs do not define a speech-memory base family, so agreed transcripts remain supporting context rather than scored base questions.
- `quarantined` · Use static current-scene questions about room type, people count, decor, or doorway state. — Those prompts are ordinary scene captioning and do not implement any of the five design-doc task families.

### `NymeriaPlus_v1.0_20230905_s1_elizabeth_morgan_act2_nfmn6i__T3_at_90`

Baseline:

- `q01` 45.0s · `action_narration` · Can you remind me which game we're playing? → **You're playing rock-paper-scissors with your peer while seated at the dining table.**
- `q02` 65.0s · `episodic_memory` · What did I do with the chair before walking away? → **You tucked the dining chair back under the table before walking away.**
- `q03` 85.0s · `episodic_memory` · Where did I go after leaving the dining area? → **You crossed the living room and foyer, followed the hallway, and reached the kitchen.**
- `q04` 105.0s · `episodic_memory` · Where had I been heading through the hallway? → **You had been walking through the hallway toward the staircase at the far end.**
- `q05` 138.0s · `episodic_memory` · What kind of rooms have I been checking up here? → **You've been walking through several different bedrooms along the upstairs hallway.**
- `q06` 171.8s · `episodic_memory` · What did I point to in the bedroom before coming downstairs? → **You pointed at the wall from the bedroom doorway, then looked behind the door.**

Output-contingent devices:

- `d01` on `q06` · `cross_question` after 5 words · Was I inside the room when I pointed? → **No. You were standing in the bedroom doorway when you pointed at the wall.**

Held out:

- `quarantined` · Ask for the exact number of rooms visited upstairs. — Not authored because the rapid door touches and room transitions are visually ambiguous.
- `quarantined` · Ask for the purpose of the upstairs inspection. — Rejected because neither visible action nor trusted speech licenses a purpose.

### `NymeriaPlus_v1.0_20230807_s0_dominique_frye_act3_lysseo__T3_at_840`

Baseline:

- `q01` 45.0s · `action_narration` · What task am I in the middle of right now? → **You're folding laundry on your lap while sitting on the sofa.**
- `q02` 80.0s · `episodic_memory` · What did I switch to after the shirt? → **After the shirt, you picked up the pants and folded them across your lap.**
- `q03` 100.0s · `episodic_memory` · What did I do after I finished folding the pants? → **You set the pants down, then picked up another garment from the floor.**
- `q04` 136.0s · `episodic_memory` · Right before I picked up this black garment, what had I just done? → **You had finished folding the previous garment and put it down on the floor.**
- `q05` 156.0s · `episodic_memory` · What did I do when I reached the bedroom with the folded clothes? → **You leaned over the bed, put the folded clothes down, and headed back out.**
- `q06` 178.0s · `episodic_memory` · What did I do after leaving those clothes in the bedroom? → **You returned to the living room, picked up more clothes, and sat back on the sofa.**

Output-contingent devices:

- `e01` on `q01` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `e02` on `q02` · `same_question_refinement` after 5 words · Just which item did I pick up next? → **You picked up the pants next.**
- `e03` on `q03` · `question_change_related` after 5 words · Actually, where did I pick the next garment up from? → **You picked it up from the floor in front of the sofa.**

Held out:

- `quarantined` · The malformed final action rows establish what happens after 167.9 seconds. — Each listed row ends before it starts; q06 uses only the valid return-and-sit sequence ending at 160.9 seconds.
- `quarantined` · Every later garment has a specific clothing type. — Only the first shirt and the pants are visually distinctive; later garments remain 'piece of clothing.'
- `quarantined` · The first folded shirt and later folded stack form verified object-memory absence items. — No dense all-frame absence sweep, present-control detector pass, or missed-pickup check was run. The location-style proposals were quarantined and replaced with visually verified action episodes.
- `quarantined` · The brief hand-to-face motion can be scored as a mouth wipe. — The narration proposes it, but the 2 fps ego frames do not independently resolve hand-to-mouth contact; the shipped turn uses the clearly visible next garment instead.

### `NymeriaPlus_v1.0_20230928_s0_grace_randolph_act4_j1cw74__T3_at_690`

Baseline:

- `b01` 45.0s · `episodic_memory` · What did I do with the paper towel after wiping the island? → **You crumpled it, carried it to the trash can, and threw it away.**
- `b02` 75.0s · `episodic_memory` · What did I do at the trash bin before going to the microwave? → **You opened the bin twice and threw away two small pieces of trash.**
- `b03` 96.0s · `episodic_memory` · What was I carrying as I walked over to the drawers? → **You were carrying the salad bowl from the table toward the counter.**
- `b04` 120.0s · `episodic_memory` · Which utensils did I take out? → **You took out forks first, then gathered knives from the same drawer.**
- `b05` 140.0s · `episodic_memory` · What did I close before I started checking the bottles by the stove? → **You went back to the open wall cabinet and closed its door.**
- `b06` 170.0s · `episodic_memory` · What was I doing with the drawers later? → **You kept opening and closing several kitchen drawers while talking to your peer.**

Output-contingent devices:

- `d01` on `b01` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `d02` on `b02` · `cross_question` after 5 words · What was I still carrying when I reopened it? → **You were still carrying the packaging and paper.**
- `d03` on `b04` · `same_question_refinement` after 5 words · Just what came after the forks? → **You took out the knives after the forks.**
- `d04` on `b05` · `topic_switch` after 5 words · Wait—what had I carried from the wall cabinet to the table? → **You had carried two white plates to the table.**
- `d05` on `b06` · `question_change_related` after 5 words · Actually, did I check a cabinet too? → **Yes. You opened and closed a lower cabinet after checking the drawers.**

Held out:

- `needs_dense_review` · Ask where the packaging and paper were left. — Not shipped because the placement would require dense object-absence verification at the ask.
- `rejected` · Ask during the long 101–113 second wearer speech span. — The authored anchors were moved to clear source-speech windows.

### `NymeriaPlus_v1.0_20231004_s1_ashley_reyes_act1_3d7yqq__T3_at_690`

Baseline:

- `b01` 50.0s · `episodic_memory` · Which rooms did I look into before I first went upstairs? → **You checked the bathroom and the recreation room before heading up the stairs.**
- `b02` 75.0s · `episodic_memory` · How did I go up the stairs the next time? → **You walked backward up the stairs and briefly reached down to the floor.**
- `b03` 95.0s · `episodic_memory` · What had I been doing as I went down the corridor? → **You were walking down the corridor and touching doors with your hands as you passed them.**
- `b04` 125.0s · `episodic_memory` · Which door did I open after leaving the second bedroom? → **You opened the bathroom door, looked in, and then continued along the hallway.**
- `b05` 149.0s · `episodic_memory` · Where did I go after pointing down the stairs? → **You walked downstairs and headed toward a bedroom off the lower hallway.**
- `b06` 176.0s · `episodic_memory` · What did I do after talking with my peer in the hallway? → **You turned toward the stairs and started walking up them.**

Output-contingent devices:

- `d01` on `b01` · `cross_question` after 5 words · Which one did I check second? → **You checked the recreation room second.**
- `d02` on `b02` · `plain_backchannel` after 5 words · Mm-hm. → **no response; continue parent**
- `d03` on `b03` · `same_question_refinement` after 5 words · Just the action—what was I doing? → **You were touching the corridor doors as you passed them.**
- `d04` on `b04` · `cross_question` after 5 words · And where did I head after that? → **You continued along the hallway.**
- `d05` on `b05` · `topic_switch` after 5 words · Wait—what had I stopped to look up at on the first trip upstairs? → **You looked up at the transom window above the front door.**

Held out:

- `quarantined` · Ask for an exact count of corridor doors. — Overlapping narration spans and source counting speech make the exact count ambiguous.

## Paths

- Manifest: `data/ego_duplex/avd/chain20_fresh_v1/manifest.json`
- Clean baseline collection: `data/ego_duplex/avd/chain20_fresh_v1/baseline.jsonl`
- Interruption collection: `data/ego_duplex/avd/chain20_fresh_v1/interruptions.jsonl`
- Machine validation: `data/ego_duplex/avd/chain20_fresh_v1/validation/report.json`
- Prior-question freshness: `data/ego_duplex/avd/chain20_fresh_v1/validation/freshness_report.json`
- Deduplicated prior-question index: `data/ego_duplex/avd/chain20_fresh_v1/validation/freshness_prior_index.json`
- Independent content audit: `data/ego_duplex/avd/chain20_fresh_v1/validation/content_audit.json`
- Integrity hashes: `data/ego_duplex/avd/chain20_fresh_v1/checksums.sha256`
- Episode pairs: `data/ego_duplex/avd/chain20_fresh_v1/episodes/<clip>/{baseline.json,interruptions.json,audit.json}`
