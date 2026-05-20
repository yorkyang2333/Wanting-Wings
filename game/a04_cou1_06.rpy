label a04_cou1_06:

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina 2 lg school f at pos_r
    show fumi 1 lg school a at pos_l
    with Dissolve(0.25)

    voice "HIN_1159"
    hina "\"Oh, I'm gonna jump, so hold it down, okay?\""

    show fumi 1 school c with dict_dissolve_25

    voice "FUM_0981"
    fumi "\"Okay!\""

    show hina 1 school f with Dissolve(0.25)
    show hina:
        ShakeJump2
        ShakeJump2
        ShakeJump2

    voice "HIN_1160"
    hina "\"Hup, up, there!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    play sound se524

    "Hina jumped three times, grabbing at the curtain rail. The hooks came off and the curtain floated to the floor."

    "Fumi let go of the ladder after Hina had climbed down and picked up the curtain, patting the dust from it."

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1161"
    hina "\"That's it, right?\""

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0982"
    fumi "\"Yep. Good work.\""

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0983a"
    fumi "\"If only Ogata were here, too.\""

    "Since she's tall."

    show hina:
        "hina 2 lg school g" with Dissolve(0.25)
        xcenter 772
        easein 0.5 xcenter 662


    voice "HIN_1162"
    hina "\"Yeah, but then we couldn't be alone.\""

    show hina 2 lg school g:
        xcenter 662
    with None
    show fumi:
        "fumi 2 lg school i" with Dissolve(0.25)
        xcenter 252
        easein 0.5 xcenter 362

    voice "FUM_0984"
    fumi "\"Heheh, I suppose that's true.\""

    show fumi 2 lg school i:
        xcenter 362
    with None

    show fumi 2 lg school j
    show hina 2 lg school c
    with dict_dissolve_25

    "The two exchanged a brief kiss."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 2.5

    if persistent.dpatch:
        jump rp_scene04
    else:
        pause 1.0
        "........."
        "......"
        window hide
        pause 1.25
        window auto

label rp_scene04_end:

    scene black with Dissolve(0.25)
    pause 1.25

    scene bg04aa with bg_effect_05
    pause 0.5

    if persistent.dpatch:
        $ side_image = "hina 1 side znd l"

    voice "HIN_1193"
    hina "\"Wah! You're so cute, Fumi!\""

    "Hina exclaimed, seeing Fumi wrapped up in the curtain."

    if persistent.dpatch:
        $ side_image = "hina 1 side znd c"

    voice "HIN_1194"
    hina "\"It's like a princess dress!\""

    "Now that she mentioned it, it did sort of look like a mermaid-style dress."

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain g"

    voice "FUM_1015"
    fumi "\"I just wrapped the curtain around myself.\" "

    if persistent.dpatch:
        $ side_image = "hina 1 side znd b"

    voice "HIN_1195"
    hina "\"Okay, I'm gonna do it too.\""

    "Hina wrapped a curtain around herself as well, but..."

    if persistent.dpatch:
        $ side_image = "hina 1 side znd k"

    voice "HIN_1196"
    hina "\"Huh? That's weird... This goes like this...?\""

    "It wasn't going as well as it had with Fumi."

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain f"

    voice "HIN_1197"
    hina "\"This way?\""

    "When she turned around to Fumi, it wasn't a dress she was wearing, but—"

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain h"

    voice "HIN_1198"
    hina "\"This... isn't a dress, is it? It's like...\""

    "She looked like a Halloween ghost."

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain b"

    voice "FUM_1016"
    fumi "\"You must be my prince, Hina.\""

    "Hmm, that's another way to look at it, I suppose."

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain f"

    voice "HIN_1199"
    hina "\"Prince?\""

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain c"

    voice "FUM_1017"
    fumi "\"Yes. It looks like a cape. It's very cool.\""

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain b"

    voice "HIN_1200"
    hina "\"Even though I'm a girl?\""

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain d"

    voice "FUM_1018"
    fumi "\"Ah...\""

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain g"

    voice "HIN_1201"
    hina "\"That's okay. I'll let you be the princess, Fumi.\""

    "Hina smiled toothily."

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain c"

    voice "HIN_1202"
    hina "\"If I can be with the princess forever, then I'll be a prince.\""

    "She said, reaching a hand out to Fumi."

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain h"

    voice "FUM_1019"
    fumi "\"Hina...\""

    "They gazed at each other for a short while, and Fumi took her hand reverently."

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain c"

    voice "FUM_1020"
    fumi "\"We can keep dreaming for a little longer, can't we?\""

    "Hina nodded and pulled Fumi upright."

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain c"

    voice "HIN_1203"
    hina "\"Together...\""

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain i"

    voice "FUM_1021"
    fumi "\"...Forever.\""

    "They smiled in the glittering light of the afternoon. In this moment, they were a picture-perfect prince and princess."

    play sound se030a

    "The sound of a new dream starting..."

    "Growing up doesn't mean not dreaming anymore."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
