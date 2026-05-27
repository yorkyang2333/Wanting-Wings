label a04_cou1_01:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show fumi z3 2 lg pyjama b behind hina at pos_l2_z3
    show rin z3 1 lg pyjama a behind hina at pos_r2_z3
    show hina z3 2 lg pyjama b
    with Dissolve(0.25)

    voice "HIN_1000"
    hina "\"This pork stew is so thick!\"" id a04_cou1_01_d63c8af1

    show fumi z3 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0838"
    fumi "\"I let it sit overnight. You can really taste the flavor in the radish, right?\"" id a04_cou1_01_7443755a

    show rin z3 1 lg pyjama b with dict_dissolve_25

    voice "RIN_0943"
    rin "\"......\"" id a04_cou1_01_f10d32ee

    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1001"
    hina "\"The salad's good, too! Did you make this dressing?\"" id a04_cou1_01_1c663756

    show fumi z3 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0839"
    fumi "\"Yes, it's my special onion dressing. I mince the onions with a food processor instead of grating them.\"" id a04_cou1_01_8ceb3e30

    show hina z3 2 lg pyjama g with dict_dissolve_25

    voice "HIN_1002"
    hina "\"So that's why they're so crisp!\"" id a04_cou1_01_29154dc1

    show rin z3 1 lg pyjama h with dict_dissolve_25

    voice "RIN_0944"
    rin "\"......\"" id a04_cou1_01_3e77d2bc

    show hina z3 1 lg pyjama f with dict_dissolve_25

    voice "HIN_1003"
    hina "\"Hey, you're avoiding the peppers again! Fumi's dressing is really good, you know?\"" id a04_cou1_01_b7b7f12d

    show rin z3 1 lg pyjama b with dict_dissolve_25

    voice "RIN_0945"
    rin "\"...Listen.\"" id a04_cou1_01_e40aa0a3

    show fumi z3 1 lg pyjama e
    show hina z3 1 lg pyjama k
    with dict_dissolve_25

    $ voice2("hina","HIN_1004","fumi","FUM_0840")
    hina_fumi "\"Hm?\"\n\"Yes?\"" (what_rest_indent=0)

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0946"
    rin "\"Is there anything you two want to tell me?\"" id a04_cou1_01_72e2e453

    "Hina and Fumi shared a look."

    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1005"
    hina "\"Did something happen?\"" id a04_cou1_01_a157f75a

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0841"
    fumi "\"Oh, now that I think about it, I switched to a different brand of tea recently. It's very sharp of you to notice, Ogata.\"" id a04_cou1_01_be7de2d3

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0947"
    rin "\"Huh? No...\"" id a04_cou1_01_69e3f5cd

    show hina z3 1 lg pyjama a with dict_dissolve_25

    voice "HIN_1006"
    hina "\"Oh yeah, I cut my bangs this morning. It was just a little trim; you noticed?\"" id a04_cou1_01_0692321e

    show rin z3 1 lg pyjama i with dict_dissolve_25

    voice "RIN_0948"
    rin "\"No, I mean...\"" id a04_cou1_01_66c3a40e

    show fumi z3 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0842"
    fumi "\"Gabe's wings were a little dirty, so I cleaned them.\"" id a04_cou1_01_320d233b

    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_1007"
    hina "\"Fumi fixed the hole in my down jacket.\"" id a04_cou1_01_6c6a6071

    "Hina and Fumi listed off their innocuous updates."

    show hina z3 1 lg pyjama b with dict_dissolve_25

    voice "HIN_1008"
    hina "\"Oh, and Fumi and I are making pudding after dinner!\"" id a04_cou1_01_978df1d8

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0949"
    rin "\"I-I see.\"" id a04_cou1_01_d90fc6ab

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0950"
    rin "\"When did you two start using each other's names, anyway?\"" id a04_cou1_01_02737ab1

    show hina z3 2 lg pyjama b with dict_dissolve_25

    voice "HIN_1009"
    hina "\"Well, we thought it was too formal to keep using our last names.\"" id a04_cou1_01_d654c804

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0843"
    fumi "\"Should I call you by your name too, Ogata? Rin?\"" id a04_cou1_01_eff8115f

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0951"
    rin "\"I don't really care either way...\"" id a04_cou1_01_1b390347

    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_1010"
    hina "\"Well, you {i}are{/i} the younger one, Rin.\"" id a04_cou1_01_c0a18210

    "Rin put a hand to her temple."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_cou1_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
