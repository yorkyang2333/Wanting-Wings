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
    hina "\"This pork stew is so thick!\""

    show fumi z3 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0838"
    fumi "\"I let it sit overnight. You can really taste the flavor in the radish, right?\""

    show rin z3 1 lg pyjama b with dict_dissolve_25

    voice "RIN_0943"
    rin "\"......\""

    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1001"
    hina "\"The salad's good, too! Did you make this dressing?\""

    show fumi z3 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0839"
    fumi "\"Yes, it's my special onion dressing. I mince the onions with a food processor instead of grating them.\""

    show hina z3 2 lg pyjama g with dict_dissolve_25

    voice "HIN_1002"
    hina "\"So that's why they're so crisp!\""

    show rin z3 1 lg pyjama h with dict_dissolve_25

    voice "RIN_0944"
    rin "\"......\""

    show hina z3 1 lg pyjama f with dict_dissolve_25

    voice "HIN_1003"
    hina "\"Hey, you're avoiding the peppers again! Fumi's dressing is really good, you know?\""

    show rin z3 1 lg pyjama b with dict_dissolve_25

    voice "RIN_0945"
    rin "\"...Listen.\""

    show fumi z3 1 lg pyjama e
    show hina z3 1 lg pyjama k
    with dict_dissolve_25

    $ voice2("hina","HIN_1004","fumi","FUM_0840")
    hina_fumi "\"Hm?\"\n\"Yes?\"" (what_rest_indent=0)

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0946"
    rin "\"Is there anything you two want to tell me?\""

    "Hina and Fumi shared a look."

    show hina z3 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1005"
    hina "\"Did something happen?\""

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0841"
    fumi "\"Oh, now that I think about it, I switched to a different brand of tea recently. It's very sharp of you to notice, Ogata.\""

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0947"
    rin "\"Huh? No...\""

    show hina z3 1 lg pyjama a with dict_dissolve_25

    voice "HIN_1006"
    hina "\"Oh yeah, I cut my bangs this morning. It was just a little trim; you noticed?\""

    show rin z3 1 lg pyjama i with dict_dissolve_25

    voice "RIN_0948"
    rin "\"No, I mean...\""

    show fumi z3 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0842"
    fumi "\"Gabe's wings were a little dirty, so I cleaned them.\""

    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_1007"
    hina "\"Fumi fixed the hole in my down jacket.\""

    "Hina and Fumi listed off their innocuous updates."

    show hina z3 1 lg pyjama b with dict_dissolve_25

    voice "HIN_1008"
    hina "\"Oh, and Fumi and I are making pudding after dinner!\""

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0949"
    rin "\"I-I see.\""

    show rin z3 1 lg pyjama a with dict_dissolve_25

    voice "RIN_0950"
    rin "\"When did you two start using each other's names, anyway?\""

    show hina z3 2 lg pyjama b with dict_dissolve_25

    voice "HIN_1009"
    hina "\"Well, we thought it was too formal to keep using our last names.\""

    show fumi z3 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0843"
    fumi "\"Should I call you by your name too, Ogata? Rin?\""

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0951"
    rin "\"I don't really care either way...\""

    show hina z3 1 lg pyjama c with dict_dissolve_25

    voice "HIN_1010"
    hina "\"Well, you {i}are{/i} the younger one, Rin.\""

    "Rin put a hand to her temple."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_cou1_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
