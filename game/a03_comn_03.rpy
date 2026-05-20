label a03_comn_03:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    show hina z3 1 lg pyjama d
    show rin z3 1 lg pyjama i behind hina at pos_r2_z3
    show fumi z3 2 lg pyjama a behind hina at pos_l2_z3
    with Dissolve(0.25)

    voice "FUM_0487"
    fumi "\".........\""

    voice "HIN_0658"
    hina "\"......\""

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "FUM_0488"
    fumi "\".........\""

    voice "RIN_0532"
    rin "\"......\""

    show fumi z3 2 lg pyjama g with dict_dissolve_25

    voice "FUM_0489"
    fumi "\"Umm...\""

    show hina z3 1 lg pyjama l
    show rin z3 2 lg pyjama c
    with Dissolve(0.25)

    $ voice2("hina","HIN_0659","rin","RIN_0533")
    hina_rin "\"We're not angels!\""

    show fumi z3 1 lg pyjama h with Dissolve(0.25)
    show fumi:
        ShakeUji

    voice "FUM_0490"
    fumi "\"Augh...\""

    play music bgm01

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina z3 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0660"
    hina "\"We've seen each other's backs plenty of times changing clothes, right?\""

    show fumi z3 1 lg pyjama d with dict_dissolve_25

    voice "FUM_0491"
    fumi "\"I guess that's true.\""

    "She still seemed unconvinced."

    show rin z3 1 lg pyjama e with dict_dissolve_25

    voice "RIN_0534"
    rin "\"I know how we can find out.\""

    show fumi z3 1 lg pyjama e with dict_dissolve_25

    voice "FUM_0492"
    fumi "\"Really?!\""

    show hina z3 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0661"
    hina "\"What...?\""

    "Fumi's eyes were sparkling, but Hina looked incredulous."

    show rin z3 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0535"
    rin "\"We'll just cut our fingers with a knife, put the blood on a Petri dish, and heat it up with a wire...\""

    show hina z3 1 lg pyjama k with dict_dissolve_25

    show fumi z3 2 lg pyjama d with dict_dissolve_25


    $ voice2("hina","HIN_0662","fumi","FUM_0493")
    hina_fumi "\"???\""

    show rin z3 1 lg pyjama g with dict_dissolve_25

    voice "RIN_0536"
    rin "\"Sorry, never mind...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a03_cou3_02
    elif rin_hina_score > hina_fumi_score:
        jump a03_cou2_02
    else:
        jump a03_cou1_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
