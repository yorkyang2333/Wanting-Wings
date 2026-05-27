label a10_cou3_04:

    scene bg07bb with Dissolve(0.5)
    pause 1.5

    show rin_1_120_school_j:
        xcenter 512 ycenter 1684
        function LayerShake(20,20,0.3)
    with dict_dissolve_10
    $ persistent.layer_shaken = False

    voice "2RI_1573"
    rin "\"Ngaaaaaaaah!!\"" id a10_cou3_04_f830ef36

    show rin_1_120_school_j:
        xcenter 512 ycenter 1684 xoffset 0 yoffset 0
    with None

    "Rin's scream echoed from the rooftop at dusk."

    play music bgm01 fadein 1.0

    $ side_image = "hina 1 side school j"

    voice "2HI_1560"
    hina "\"She's starting to lose it from the lack of Asou.\"" id a10_cou3_04_c966a521

    if persistent.dpatch:
        "Fumi was commuting to school from home for the whole week so that she could help out at their store. For the last few days, they'd been meeting in the classroom and parting at the bus stop." id a10_cou3_04_41138bf4
    else:
        "Fumi was commuting to class from home for the whole week so that she could help out at their store. For the last few days, they'd been meeting in the classroom and parting at the bus stop."

    hide rin_1_120_school_j with Dissolve(0.25)

    show sachiko 1 sm outfit c at pos_ls
    show rin 1 sm school j at pos_rs
    with dict_dissolve_25

    voice "2SA_0866"
    sachiko "\"You've just gotta wait another what, three days?\"" id a10_cou3_04_d4ed1052

    show rin:
        ShakeJump

    voice "2RI_1574"
    rin "\"She's got classes to go to, too!\"" id a10_cou3_04_5e972c5b

    show rin:
        xoffset 0 yoffset 0
    with None

    show sachiko 2 sm outfit a with dict_dissolve_25

    voice "2SA_0867"
    sachiko "\"Oh, that. Well, Foomin said she was gonna say no, right?\"" id a10_cou3_04_6b9128aa

    $ side_image = "hina 2 side school e"

    voice "2HI_1561"
    hina "\"Asou can be a bit of a pushover, though...\"" id a10_cou3_04_b5bfa0fb

    show rin:
        function LayerShake(10,10,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1575"
    rin "\"Mmmmmmmh!\"" id a10_cou3_04_27e96a22

    show rin:
        xoffset 0 yoffset 0
    with None

    "The fact that she still hasn't managed to turn them down does kind of support that."

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1576"
    rin "\"It's unethical of them to try to scout a student, don't you think?\"" id a10_cou3_04_ddcab418

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0868"
    sachiko "\"There's a lot of students in the entertainment industry these days, huh?\"" id a10_cou3_04_8140b2e6

    show rin 1 sm school h with dict_dissolve_25

    voice "2RI_1577"
    if persistent.dpatch:
        rin "\"It's probably against school rules, right?\"" id a10_cou3_04_d3670dd5
    else:
        rin "\"It's probably against campus rules, right?\"" id a10_cou3_04_8309578f

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0869"
    if persistent.dpatch:
        sachiko "\"This school's pretty hands-off about that stuff, actually~\"" id a10_cou3_04_b627e4d3
    else:
        sachiko "\"This academy's pretty hands-off about that stuff, actually~\"" id a10_cou3_04_93f95130

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_1578"
    rin "\"That's not what I mean!\"" id a10_cou3_04_44ae2c18

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0870"
    sachiko "\"Well, what do you want me to do about it?\"" id a10_cou3_04_0c7ef3ed

    "She just wanted to take out her frustrations on someone."

    $ side_image = "hina 1 side school e"

    voice "2HI_1562"
    hina "\"......\"" id a10_cou3_04_47c4450e

    "Hina watched as Rin threw her tantrum."

    hide sachiko with Dissolve(0.25)

    show hina 1 sm school e at pos_ls
    show rin 1 sm school e
    with dict_dissolve_25

    voice "2RI_1579"
    rin "\"Wh-What?\"" id a10_cou3_04_b99c0c94

    voice "2HI_1563"
    hina "\"Say what you really mean.\"" id a10_cou3_04_7920e00c

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1580"
    rin "\"What I really...\"" id a10_cou3_04_23bf528e

    show hina 2 sm school d with dict_dissolve_25

    voice "2HI_1564"
    hina "\"What is it that you want Asou to do, Rin?\"" id a10_cou3_04_fdd34334

    "Rin winced at the straightforward question. She hesitated for a bit, then..."

    show rin:
        "rin 1 sm school g" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2RI_1581"
    rin "\"I don't want her to go somewhere far away...!\"" id a10_cou3_04_9e1c88d4

    show rin 1 sm school g:
        xoffset 0 yoffset 0
    with None

    "She said her true feelings."

    show hina 1 sm school e with dict_dissolve_25

    voice "2HI_1565"
    hina "\"Why don't you tell her that?\"" id a10_cou3_04_31928dd2

    "Rin shook her head."

    show rin 2 sm school d with dict_dissolve_25

    voice "2RI_1582"
    rin "\"Because I don't want her to hate me.\"" id a10_cou3_04_a9dd3c9a

    show hina 1 sm school k with dict_dissolve_25

    voice "2HI_1566"
    hina "\"Why would she hate you?\"" id a10_cou3_04_1eefd3f5

    voice "2RI_1583"
    rin "\"I don't want to get in her way...\"" id a10_cou3_04_12c14857

    show hina 1 sm school e with dict_dissolve_25

    voice "2HI_1567"
    hina "\"Then why not just let her go and do as she likes?\"" id a10_cou3_04_32e5f433

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1584"
    rin "\"I can't do that! If you take being Fumi's girlfriend away from me, what do I even have left?!\"" id a10_cou3_04_17f70aec

    show hina 2 sm school e with dict_dissolve_25

    voice "2HI_1568"
    hina "\"Being her ex, I guess.\"" id a10_cou3_04_c40c7da6

    show rin:
        "rin 1 sm school j" with Dissolve(0.25)
        function LayerShake(10,10,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1585"
    rin "\"Waaaaaaaaaaaah!!\"" id a10_cou3_04_c42b883e

    show rin 1 sm school j:
        xoffset 0 yoffset 0
    with None
    show hina 2 sm school f with dict_dissolve_25

    voice "2HI_1569"
    hina "\"Why don't you make something else of yourself, then? So you'd be a better match for each other.\"" id a10_cou3_04_96382334

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1586"
    rin "\"But... I don't have anything.\"" id a10_cou3_04_4f3829fe

    show hina 1 sm school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "2HI_1570"
    hina "\"Haahh. Why are you always trying to drag people down to your level?\"" id a10_cou3_04_cb94182c

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina sighed."

    show hina 1 sm school j with dict_dissolve_25

    voice "2HI_1571"
    hina "\"There's part of you that thinks she likes you because of your bad parts, right?\"" id a10_cou3_04_d85d3de5

    show rin:
        "rin 1 sm school g" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1587"
    rin "\"Ugh...\"" id a10_cou3_04_fa5b7583

    show rin 1 sm school g:
        xoffset 0 yoffset 0
    with None

    "...was all she could come up with."

    $ side_image = "sachiko 1 side outfit d"

    voice "2SA_0871"
    sachiko "\"Try not to dig the knife in too deep, Hinacchi. She won't be able to recover.\"" id a10_cou3_04_ad3bc2c0

    show hina 1 sm school e with dict_dissolve_25

    voice "2HI_1572"
    hina "\"By depending on her, you're placing your own limitations on her. Getting in her way, in other words.\"" id a10_cou3_04_09ff8e9a

    $ side_image = "sachiko 2 side outfit i"

    voice "2SA_0872"
    sachiko "\"...Kinda goes both ways in this case, though.\"" id a10_cou3_04_e1f9522c

    show hina 2 sm school d with dict_dissolve_25

    voice "2HI_1573"
    hina "\"It's because you're so dependent on her that anything that shifts the balance slightly throws you completely out of whack. This could be a good opportunity. Why don't you try relying on her a bit less?\"" id a10_cou3_04_49ecc75a

    show rin 2 sm school d with dict_dissolve_25

    voice "2RI_1588"
    rin "\"......\"" id a10_cou3_04_bd7c18a1

    "One person being entirely reliant on another is no kind of relationship."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou3_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
