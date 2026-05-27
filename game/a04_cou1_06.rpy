label a04_cou1_06:

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina 2 lg school f at pos_r
    show fumi 1 lg school a at pos_l
    with Dissolve(0.25)

    voice "HIN_1159"
    hina "\"Oh, I'm gonna jump, so hold it down, okay?\"" id a04_cou1_06_4e894c57

    show fumi 1 school c with dict_dissolve_25

    voice "FUM_0981"
    fumi "\"Okay!\"" id a04_cou1_06_3312ec1f

    show hina 1 school f with Dissolve(0.25)
    show hina:
        ShakeJump2
        ShakeJump2
        ShakeJump2

    voice "HIN_1160"
    hina "\"Hup, up, there!\"" id a04_cou1_06_e7dcbadf

    show hina:
        xoffset 0 yoffset 0
    with None
    play sound se524

    "Hina jumped three times, grabbing at the curtain rail. The hooks came off and the curtain floated to the floor."

    "Fumi let go of the ladder after Hina had climbed down and picked up the curtain, patting the dust from it."

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1161"
    hina "\"That's it, right?\"" id a04_cou1_06_5cb6b433

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0982"
    fumi "\"Yep. Good work.\"" id a04_cou1_06_eb739a80

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0983a"
    fumi "\"If only Ogata were here, too.\"" id a04_cou1_06_2671f60a

    "Since she's tall."

    show hina:
        "hina 2 lg school g" with Dissolve(0.25)
        xcenter 772
        easein 0.5 xcenter 662


    voice "HIN_1162"
    hina "\"Yeah, but then we couldn't be alone.\"" id a04_cou1_06_26441139

    show hina 2 lg school g:
        xcenter 662
    with None
    show fumi:
        "fumi 2 lg school i" with Dissolve(0.25)
        xcenter 252
        easein 0.5 xcenter 362

    voice "FUM_0984"
    fumi "\"Heheh, I suppose that's true.\"" id a04_cou1_06_3cacae8f

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
    hina "\"Wah! You're so cute, Fumi!\"" id rp_scene04_end_f38393a8

    "Hina exclaimed, seeing Fumi wrapped up in the curtain."

    if persistent.dpatch:
        $ side_image = "hina 1 side znd c"

    voice "HIN_1194"
    hina "\"It's like a princess dress!\"" id rp_scene04_end_b85b9406

    "Now that she mentioned it, it did sort of look like a mermaid-style dress."

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain g"

    voice "FUM_1015"
    fumi "\"I just wrapped the curtain around myself.\" " id rp_scene04_end_52bd69f2

    if persistent.dpatch:
        $ side_image = "hina 1 side znd b"

    voice "HIN_1195"
    hina "\"Okay, I'm gonna do it too.\"" id rp_scene04_end_7603d30d

    "Hina wrapped a curtain around herself as well, but..."

    if persistent.dpatch:
        $ side_image = "hina 1 side znd k"

    voice "HIN_1196"
    hina "\"Huh? That's weird... This goes like this...?\"" id rp_scene04_end_85a5946d

    "It wasn't going as well as it had with Fumi."

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain f"

    voice "HIN_1197"
    hina "\"This way?\"" id rp_scene04_end_072e5f86

    "When she turned around to Fumi, it wasn't a dress she was wearing, but—"

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain h"

    voice "HIN_1198"
    hina "\"This... isn't a dress, is it? It's like...\"" id rp_scene04_end_44256b9e

    "She looked like a Halloween ghost."

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain b"

    voice "FUM_1016"
    fumi "\"You must be my prince, Hina.\"" id rp_scene04_end_5b5f9908

    "Hmm, that's another way to look at it, I suppose."

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain f"

    voice "HIN_1199"
    hina "\"Prince?\"" id rp_scene04_end_2ea9abac

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain c"

    voice "FUM_1017"
    fumi "\"Yes. It looks like a cape. It's very cool.\"" id rp_scene04_end_1d4c6e59

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain b"

    voice "HIN_1200"
    hina "\"Even though I'm a girl?\"" id rp_scene04_end_7d6b8738

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain d"

    voice "FUM_1018"
    fumi "\"Ah...\"" id rp_scene04_end_acc4de44

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain g"

    voice "HIN_1201"
    hina "\"That's okay. I'll let you be the princess, Fumi.\"" id rp_scene04_end_6ef42057

    "Hina smiled toothily."

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain c"

    voice "HIN_1202"
    hina "\"If I can be with the princess forever, then I'll be a prince.\"" id rp_scene04_end_9c50cf40

    "She said, reaching a hand out to Fumi."

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain h"

    voice "FUM_1019"
    fumi "\"Hina...\"" id rp_scene04_end_7580f081

    "They gazed at each other for a short while, and Fumi took her hand reverently."

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain c"

    voice "FUM_1020"
    fumi "\"We can keep dreaming for a little longer, can't we?\"" id rp_scene04_end_b94fd230

    "Hina nodded and pulled Fumi upright."

    if persistent.dpatch:
        $ side_image = "hina 2 side curtain c"

    voice "HIN_1203"
    hina "\"Together...\"" id rp_scene04_end_0431d26f

    if persistent.dpatch:
        $ side_image = "fumi 2 side curtain i"

    voice "FUM_1021"
    fumi "\"...Forever.\"" id rp_scene04_end_3d544a7e

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
