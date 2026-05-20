label a04_cou2_05:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show hina:
        "hina 2 lg pyjama g flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    voice "HIN_1414"
    hina "\"Hey, Rin—\""

    show hina 2 lg pyjama g:
        alpha 1.0 xcenter 512
    with None

    "Hina chirped and went to sit in her lap, but..."

    show rin:
        "rin 2 lg pyjama a flat"
        alpha 0.0 xcenter 252 ycenter 1116
        easein 0.5 alpha 1.0 ycenter 1016
    pause 0.5

    show rin 2 lg pyjama a:
        alpha 1.0 xcenter 252 ycenter 1016
    with None

    play sound se118a

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1415"
    hina "\"Ngyah!\""

    show hina:
        "hina 1 lg pyjama l flat"
        alpha 1.0 ycenter 981 xoffset 0 yoffset 0
        easeout 0.5 alpha 0.0 ycenter 1081
    pause 0.5

    hide hina with None

    play sound se203b

    "She fell backwards with a yelp."

    show rin 1 lg pyjama e with dict_dissolve_25

    voice "RIN_1179"
    rin "\"Oh, sorry. You okay?\""

    "It was because Rin had suddenly stood up."

    show hina:
        "hina 1 lg pyjama h flat"
        alpha 0.0 xcenter 772 ycenter 1081
        easein 0.5 alpha 1.0 ycenter 981

    voice "HIN_1416"
    hina "\"Ngh, I'm good.\""

    show hina 1 lg pyjama h:
        alpha 1.0 xcenter 772 ycenter 981
    with None

    "Hina popped back up."

    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_1180"
    rin "\"Uh, I'm going out.\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_1417"
    hina "\"Huh? Now? Where?\""

    show rin 1 lg pyjama b with dict_dissolve_25

    voice "RIN_1181"
    rin "\"Just, out...\""

    show hina 2 lg pyjama b with dict_dissolve_25

    voice "HIN_1418"
    hina "\"I have a question about the English homework—\""

    show rin 1 lg pyjama a with dict_dissolve_25

    voice "RIN_1182"
    rin "\"Sorry, not today. I'll look at it later.\""

    show hina 1 lg pyjama h with dict_dissolve_25

    voice "HIN_1419"
    hina "\"Whaaat?\""

    show rin:
        "rin 1 lg pyjama a flat"
        alpha 1.0 xcenter 252 ycenter 1016
        easeout 0.5 alpha 0.0 xcenter 352
    pause 0.5

    hide rin with None

    "Rin fixed her bangs in the mirror, ignoring Hina's sulking."

    show hina:
        "hina 2 lg pyjama f" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 512

    voice "HIN_1420"
    hina "\"......\""

    show hina 2 lg pyjama f:
        xcenter 512
    with None

    "This was rare for Rin... and Hina noticed it, too."

    $ side_image = "rin 2 side pyjama a"

    voice "RIN_1183"
    rin "\"See you.\""

    play sound se522

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_1421"
    hina "\"Rin... My homework...\""

    $ side_image = "fumi 1 side pyjama i"

    voice "FUM_1066"
    fumi "\"Oh, I can help you with the homework after I'm done with the dishes.\""

    "Fumi said from the kitchen."

    show hina 1 lg pyjama n with dict_dissolve_25

    voice "HIN_1422"
    hina "\"...Okay. Thanks.\""

    "Hina was left staring at the door Rin had gone out through."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_cou2_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
