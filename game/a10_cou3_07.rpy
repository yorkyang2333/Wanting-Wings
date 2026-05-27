label a10_cou3_07:

    "—Valentine's Day."

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play sound se_2s_j018

    "Rin hung up her phone irritatedly."

    play music bgm03 fadein 1.0

    show rin 2 lg school b with dict_dissolve_25

    voice "2RI_1608"
    rin "\"...She's not answering.\"" id a10_cou3_07_e4e1cfea

    "It was Fumi's phone she was calling, naturally."

    show rin 2 lg school d with dict_dissolve_25

    voice "2RI_1609"
    rin "\"What are you doing... Fumi...\"" id a10_cou3_07_c0cfc563

    "She was calling because it was lunch now and Fumi still hadn't shown up."

    "She'd called every break, but Fumi had never picked up. It was the same when she called her home phone."

    voice "2RI_1610"
    rin "\"......\"" id a10_cou3_07_5cfab1e7

    "Rin stared at the screen nervously. On the display was the number for Fumi's family's store, Le Chocolat Chocolat."

    "After all her hesitating, she bit her lip and tapped the \"Dial\" button."

    hide rin with dict_dissolve_50

    play sound se_yobidasi

    pause 1.5

    "......"

    $ side_image = "rin 1 side school b"

    voice "2RI_1611"
    if persistent.dpatch:
        rin "\"Ah, I'm sorry for calling when you're so busy. My name is Rin Ogata. I'm in Fumi's class, but she didn't come to school today—\"" id a10_cou3_07_f87707bb
    else:
        rin "\"Ah, I'm sorry for calling when you're so busy. My name is Rin Ogata. I'm in Fumi's class, but she didn't come to campus today—\"" id a10_cou3_07_65ce3a83

    $ side_image = "rin 1 side school g"

    voice "2RI_1612"
    rin "\"Oh, waiting to hear...? Oh, okay. No, sorry for calling when you're so busy... Thank you.\"" id a10_cou3_07_fbf4b60f

    play sound se_2s_j012

    show hina z4 1 lg school k
    show miyako z4 1 lg school_a a:
        xcenter 172
    with dict_dissolve_25

    voice "2HI_1576"
    hina "\"Did you call Asou again? Did she pick up?\"" id a10_cou3_07_73654920

    "Hina and Miyako came over to Rin's desk."

    show rin z4 1 lg school b:
        xcenter 852
    with dict_dissolve_25

    voice "2RI_1613"
    rin "\"No... I called the store.\"" id a10_cou3_07_445455c7

    show hina:
        "hina z4 1 lg school d" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1577"
    hina "\"What? You're bothering them when they're so busy?\"" id a10_cou3_07_4811cbde

    show hina z4 1 lg school d:
        xoffset 0 yoffset 0
    with None

    "It was easy to guess how busy a pastry shop would be on Valentine's. It was no wonder Hina disapproved."

    show rin z4 2 lg school d with dict_dissolve_25

    voice "2RI_1614"
    rin "\"I know...\"" id a10_cou3_07_0cf4f0cf

    "Of course, this was obvious to Rin as well. Nonetheless."

    show hina:
        "hina z4 1 lg school n" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_1578"
    hina "\"...So? What'd they say?\"" id a10_cou3_07_5fdd5733

    show hina z4 1 lg school n:
        xoffset 0 yoffset 0
    with None

    "Hina asked with a sigh."

    voice "2RI_1615"
    rin "\"They said she was waiting to hear back.\"" id a10_cou3_07_17d9c6c3

    show miyako z4 2 lg school a with dict_dissolve_25

    voice "2MI_1055"
    miyako "\"From who?\"" id a10_cou3_07_abba2d2a

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1616"
    rin "\"From the audition, obviously... Fumi's going far away.\"" id a10_cou3_07_cbab6c84

    hide rin with dict_dissolve_50

    "Rin stood up, her chair clattering behind her. And she stumbled over to the door."

    show hina:
        "hina z4 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_1579"
    hina "\"Rin!\"" id a10_cou3_07_0f46aee2

    show hina z4 1 lg school f:
        xoffset 0 yoffset 0
    with None

    "Rin stopped at Hina's voice."

    $ side_image = "rin 2 side school d"

    voice "2RI_1617"
    rin "\"......\"" id a10_cou3_07_bc9060d7

    pause 0.5

    show rin z4 1 lg school d:
        xcenter 852
    with Dissolve(0.5)

    pause 0.25

    "After hesitating a good while, Rin plopped back down in her seat."

    voice "2RI_1618"
    rin "\"...This is what she chose.\"" id a10_cou3_07_bc5c2a4f

    show hina z4 1 lg school e with dict_dissolve_25

    voice "2HI_1580"
    hina "\"Yeah...\"" id a10_cou3_07_01272cf5

    "Hina laid her hand on Rin's back."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
