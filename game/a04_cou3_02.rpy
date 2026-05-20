label a04_cou3_02:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg04ba with Dissolve(0.25)
    pause 0.75

    play music bgm04

    "Two shadows became one in the light of the setting sun, coming together tentatively."

    show rin 1 lg school k
    show fumi 2 lg school j:
        xcenter 302
    with Dissolve(0.25)

    voice "RIN_1271"
    rin "\"Chp... mmh... ah...\""

    voice "FUM_1096"
    fumi "\"Mmh... anh... nah... chp...\""

    "Their saliva mixed noisily."

    "The sound was even more pronounced due to the emptiness of the classroom."

    voice "RIN_1272"
    rin "\"Mhh... mm... hwah... ahh...\""

    voice "FUM_1097"
    fumi "\"Haah... mmh...\""

    "Their lips finally separated when they ran out of breath."

    "Their tongues pulled apart last, as if reluctant to do so."

    show fumi:
        "fumi 2 lg school h" with Dissolve(0.25)
        xcenter 302
        easein 0.25 xcenter 252
    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 772

    voice "RIN_1273"
    rin "\"Amh... that was close.\""

    show fumi 2 lg school h:
        xcenter 252
    show rin 1 lg school g:
        xcenter 772
    with None

    "Rin caught her breath, wiping her chin."

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_1098"
    fumi "\"Haahh... what was?\""

    "Fumi asked, also catching her breath."

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_1274"
    rin "\"...Any more and I wouldn't be able to stop.\""

    show fumi 2 lg school g with dict_dissolve_25

    voice "FUM_1099"
    fumi "\"I suppose you're right, then. There isn't a meeting or anything today.\""

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1275"
    rin "\"Yeah. If Hina saw this...\""

    "Rin shrugged anxiously."

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_1100"
    fumi "\"She surprised me last night.\""

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_1276"
    rin "\"Yeah. She can be sharp sometimes... Call it animal instinct, I guess.\""

    show fumi 1 lg school h with dict_dissolve_25

    voice "FUM_1101"
    fumi "\"I feel kind of bad, though.\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_1277"
    rin "\"I do feel a little guilty about keeping it to ourselves, but I don't really have the courage to say anything right now...\""

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_1102"
    fumi "\"She is a little strait-laced about these things...\""

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_1278"
    rin "\"Yeah. Well, if it comes to it, we'll just have to elope.\""

    show fumi 1 lg school k with dict_dissolve_25

    voice "FUM_1103"
    fumi "\"Elope...\""

    "Fumi's face was sorrowful."

    show rin:
        "rin 1 lg school e" with Dissolve(0.25)
        ShakeJump

    voice "RIN_1279"
    rin "\"Oh, that was a joke. I was just joking.\""

    show rin 1 lg school e:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg school h with dict_dissolve_25

    voice "FUM_1104"
    fumi "\"Our relationship is important to me, but so is the relationship between the three of us.\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1280"
    rin "\"Hey, I agree.\""

    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_1281"
    rin "\"We'll just have to keep our trysts secret for now.\""

    show fumi 1 lg school i with dict_dissolve_25

    voice "FUM_1105"
    fumi "\"Right...\""

    "The two both sighed and smiled."

    show rin 1 lg school k
    show fumi 2 lg school j
    with dict_dissolve_25

    voice "RIN_1282a"
    rin "\"Asou...\""

    "Rin cupped Fumi's face and was about to kiss her again when—"

    stop music fadeout 0.1

    play sound se000c

    hide rin
    hide fumi
    with Dissolve(0.05)
    pause 0.2

    show hina:
        "hina 1 lg school c flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    voice "HIN_1492"
    hina "\"I'm back!\""

    show hina 1 lg school c:
        alpha 1.0 xcenter 512
        easein 0.25 xcenter 852
    with None
    show rin 1 lg school e behind fumi, hina
    show fumi 1 lg school j at pos_l2
    with Dissolve(0.25)

    show fumi:
        ShakeSide

    voice "FUM_1106"
    fumi "\"Awawa.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeTameiki

    voice "RIN_1283"
    rin "\"Seriously... speak of the devil.\""

    show rin 1 lg school g:
        xoffset 0 yoffset 0
    with None

    play music bgm01

    show hina 1 lg school e with dict_dissolve_25

    voice "HIN_1493"
    hina "\"What, were you badmouthing me again?!\""

    show fumi 1 lg school d
    show rin 1 lg school i
    with dict_dissolve_25

    $ voice2("rin","RIN_1284","fumi","FUM_1107")
    rin_fumi "\"No, no.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
