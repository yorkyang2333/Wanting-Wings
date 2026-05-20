label a10_cou3_05:

    scene bg02cg with Dissolve(0.5)
    pause 1.5

    play sound se_2s_j002
    pause 0.5

    play music bgm02 fadein 1.0

    "How unusual. Rin's doing the dishes."

    "She doesn't do it often, so she's awkward at it. I wonder if she's rinsing them properly."

    "Hina made curry for dinner tonight."

    "Unlike Rin's dish-washing, it's something she's used to. Chop everything up and throw it in the pot. I can see why she'd told Fumi to leave things to her."

    show miyako 1 sm pyjama_a e with dict_dissolve_25

    voice "2MI_1052"
    miyako "\"Can I leave the rest of the dishes here?\""

    "Miyako placed a stack of plates next to the sink."

    $ side_image = "rin 2 side pyjama glasses d"

    voice "2RI_1589"
    rin "\"Mm.\""

    "...came Rin's half-hearted reply."

    show miyako 1 sm pyjama_a g with dict_dissolve_25

    voice "2MI_1053"
    miyako "\"Umm, do you need any help?\""

    $ side_image = "hina 2 side pyjama_pjm d"

    voice "2HI_1574"
    hina "\"Miyako, just let her do it.\""

    "Hina stopped her."

    $ side_image = "hina 1 side pyjama_pjm a"

    voice "2HI_1575"
    hina "\"We should go back to the living room.\""

    show miyako 2 sm pyjama a with dict_dissolve_25

    voice "2MI_1054"
    miyako "\"Oh, okay.\""

    hide miyako with dict_dissolve_50

    "Left alone in the kitchen, Rin silently scrubbed the dishes."

    play sound se_2s_j002

    $ side_image = "rin 2 side pyjama glasses d"

    voice "2RI_1590"
    rin "\"......\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
