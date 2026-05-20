label a01_cou3_02:

    scene bg02dd with Dissolve(0.5)
    pause 1.5

    play music bgm02

    show hina 3 sm dark pyjama a with Dissolve(0.25)

    voice "HIN_0292"
    hina "\"Hnnh... mmh...\""

    "Hina mumbled quietly in her sleep."

    play sound se013b

    show rin 3 sm nightlight pyjama glasses_e with dict_dissolve_25

    voice "RIN_0248"
    rin "\".........\""

    show fumi 3 sm nightlight pyjama b with dict_dissolve_25

    voice "FUM_0220"
    fumi "\"......\""

    "Rin was reading with her bedside light on, and Fumi was writing in her diary."

    show fumi 3 sm nightlight pyjama c with dict_dissolve_25

    voice "FUM_0221"
    fumi "\"...Okay.\""

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    pause 0.5

    play sound se024a

    scene bg02db with Dissolve(0.25)
    pause 0.75

    show fumi 3 lg dark pyjama c
    show rin 3 sm nightlight pyjama glasses_d
    with Dissolve(0.25)

    voice "RIN_0249"
    rin "\"Oh, going to sleep? I can turn my light off if it's too bright.\""

    voice "FUM_0222"
    fumi "\"No, that's fine.\""

    show rin 3 sm nightlight pyjama glasses_b with dict_dissolve_25

    voice "RIN_0250"
    rin "\"Is Hina sleeping?\""

    show fumi 3 lg dark pyjama c with dict_dissolve_25

    voice "FUM_0223"
    fumi "\"Yep. She looks comfortable.\""

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "RIN_0251"
    rin "\"She falls asleep so fast.\""

    show fumi 3 lg dark pyjama b with dict_dissolve_25

    voice "FUM_0224"
    fumi "\"...Did you contact your family?\""

    show rin 3 sm nightlight pyjama glasses_e with dict_dissolve_25

    voice "RIN_0252"
    rin "\"Ah... mhm. I called earlier.\""

    show fumi 3 lg dark pyjama h with dict_dissolve_25

    voice "FUM_0225"
    fumi "\"Good job.\""

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "RIN_0253"
    rin "\"...Hahh.\""

    show fumi 3 lg dark pyjama b with dict_dissolve_25

    voice "FUM_0226"
    fumi "\"Not going to sleep yet?\""

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "RIN_0254"
    rin "\"Mm, I will in a little bit.\""

    show fumi 3 lg dark pyjama c with dict_dissolve_25

    voice "FUM_0227"
    fumi "\"Okay. Good night.\""

    show rin 3 sm nightlight pyjama glasses_c with dict_dissolve_25

    voice "RIN_0255"
    rin "\"Night.\""

    show fumi 3 lg dark pyjama b with dict_dissolve_25

    voice "FUM_0228"
    fumi "\"...It'll be hard to get up in the morning if you stay up too late.\""

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    voice "RIN_0256"
    rin "\"Ah... uh huh.\""

    hide fumi
    with Dissolve(0.25)

    "Fumi rolled over, and Rin continued reading."

    show rin 3 sm nightlight pyjama glasses_b with dict_dissolve_25

    voice "RIN_0257"
    rin "\"......\""

    play sound se530

    show rin 3 sm nightlight pyjama glasses_d with dict_dissolve_25

    "But she glanced at Fumi's bed and then closed her book."

    scene bg02da with Dissolve(0.25)
    pause 0.75

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
