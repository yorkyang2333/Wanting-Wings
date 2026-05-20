label a10_cou3_04:

    scene bg07bb with Dissolve(0.5)
    pause 1.5

    show rin_1_120_school_j:
        xcenter 512 ycenter 1684
        function LayerShake(20,20,0.3)
    with dict_dissolve_10
    $ persistent.layer_shaken = False

    voice "2RI_1573"
    rin "\"Ngaaaaaaaah!!\""

    show rin_1_120_school_j:
        xcenter 512 ycenter 1684 xoffset 0 yoffset 0
    with None

    "Rin's scream echoed from the rooftop at dusk."

    play music bgm01 fadein 1.0

    $ side_image = "hina 1 side school j"

    voice "2HI_1560"
    hina "\"She's starting to lose it from the lack of Asou.\""

    if persistent.dpatch:
        "Fumi was commuting to school from home for the whole week so that she could help out at their store. For the last few days, they'd been meeting in the classroom and parting at the bus stop." id a10_cou3_04_41138bf4
    else:
        "Fumi was commuting to class from home for the whole week so that she could help out at their store. For the last few days, they'd been meeting in the classroom and parting at the bus stop."

    hide rin_1_120_school_j with Dissolve(0.25)

    show sachiko 1 sm outfit c at pos_ls
    show rin 1 sm school j at pos_rs
    with dict_dissolve_25

    voice "2SA_0866"
    sachiko "\"You've just gotta wait another what, three days?\""

    show rin:
        ShakeJump

    voice "2RI_1574"
    rin "\"She's got classes to go to, too!\""

    show rin:
        xoffset 0 yoffset 0
    with None

    show sachiko 2 sm outfit a with dict_dissolve_25

    voice "2SA_0867"
    sachiko "\"Oh, that. Well, Foomin said she was gonna say no, right?\""

    $ side_image = "hina 2 side school e"

    voice "2HI_1561"
    hina "\"Asou can be a bit of a pushover, though...\""

    show rin:
        function LayerShake(10,10,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1575"
    rin "\"Mmmmmmmh!\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "The fact that she still hasn't managed to turn them down does kind of support that."

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1576"
    rin "\"It's unethical of them to try to scout a student, don't you think?\""

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0868"
    sachiko "\"There's a lot of students in the entertainment industry these days, huh?\""

    show rin 1 sm school h with dict_dissolve_25

    voice "2RI_1577"
    if persistent.dpatch:
        rin "\"It's probably against school rules, right?\"" id a10_cou3_04_d3670dd5
    else:
        rin "\"It's probably against campus rules, right?\""

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "2SA_0869"
    if persistent.dpatch:
        sachiko "\"This school's pretty hands-off about that stuff, actually~\"" id a10_cou3_04_b627e4d3
    else:
        sachiko "\"This academy's pretty hands-off about that stuff, actually~\""

    show rin 1 sm school g with dict_dissolve_25

    voice "2RI_1578"
    rin "\"That's not what I mean!\""

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0870"
    sachiko "\"Well, what do you want me to do about it?\""

    "She just wanted to take out her frustrations on someone."

    $ side_image = "hina 1 side school e"

    voice "2HI_1562"
    hina "\"......\""

    "Hina watched as Rin threw her tantrum."

    hide sachiko with Dissolve(0.25)

    show hina 1 sm school e at pos_ls
    show rin 1 sm school e
    with dict_dissolve_25

    voice "2RI_1579"
    rin "\"Wh-What?\""

    voice "2HI_1563"
    hina "\"Say what you really mean.\""

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1580"
    rin "\"What I really...\""

    show hina 2 sm school d with dict_dissolve_25

    voice "2HI_1564"
    hina "\"What is it that you want Asou to do, Rin?\""

    "Rin winced at the straightforward question. She hesitated for a bit, then..."

    show rin:
        "rin 1 sm school g" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2RI_1581"
    rin "\"I don't want her to go somewhere far away...!\""

    show rin 1 sm school g:
        xoffset 0 yoffset 0
    with None

    "She said her true feelings."

    show hina 1 sm school e with dict_dissolve_25

    voice "2HI_1565"
    hina "\"Why don't you tell her that?\""

    "Rin shook her head."

    show rin 2 sm school d with dict_dissolve_25

    voice "2RI_1582"
    rin "\"Because I don't want her to hate me.\""

    show hina 1 sm school k with dict_dissolve_25

    voice "2HI_1566"
    hina "\"Why would she hate you?\""

    voice "2RI_1583"
    rin "\"I don't want to get in her way...\""

    show hina 1 sm school e with dict_dissolve_25

    voice "2HI_1567"
    hina "\"Then why not just let her go and do as she likes?\""

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1584"
    rin "\"I can't do that! If you take being Fumi's girlfriend away from me, what do I even have left?!\""

    show hina 2 sm school e with dict_dissolve_25

    voice "2HI_1568"
    hina "\"Being her ex, I guess.\""

    show rin:
        "rin 1 sm school j" with Dissolve(0.25)
        function LayerShake(10,10,0.3)
    $ persistent.layer_shaken = False

    voice "2RI_1585"
    rin "\"Waaaaaaaaaaaah!!\""

    show rin 1 sm school j:
        xoffset 0 yoffset 0
    with None
    show hina 2 sm school f with dict_dissolve_25

    voice "2HI_1569"
    hina "\"Why don't you make something else of yourself, then? So you'd be a better match for each other.\""

    show rin 1 sm school i with dict_dissolve_25

    voice "2RI_1586"
    rin "\"But... I don't have anything.\""

    show hina 1 sm school h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "2HI_1570"
    hina "\"Haahh. Why are you always trying to drag people down to your level?\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina sighed."

    show hina 1 sm school j with dict_dissolve_25

    voice "2HI_1571"
    hina "\"There's part of you that thinks she likes you because of your bad parts, right?\""

    show rin:
        "rin 1 sm school g" with Dissolve(0.25)
        ShakeSide

    voice "2RI_1587"
    rin "\"Ugh...\""

    show rin 1 sm school g:
        xoffset 0 yoffset 0
    with None

    "...was all she could come up with."

    $ side_image = "sachiko 1 side outfit d"

    voice "2SA_0871"
    sachiko "\"Try not to dig the knife in too deep, Hinacchi. She won't be able to recover.\""

    show hina 1 sm school e with dict_dissolve_25

    voice "2HI_1572"
    hina "\"By depending on her, you're placing your own limitations on her. Getting in her way, in other words.\""

    $ side_image = "sachiko 2 side outfit i"

    voice "2SA_0872"
    sachiko "\"...Kinda goes both ways in this case, though.\""

    show hina 2 sm school d with dict_dissolve_25

    voice "2HI_1573"
    hina "\"It's because you're so dependent on her that anything that shifts the balance slightly throws you completely out of whack. This could be a good opportunity. Why don't you try relying on her a bit less?\""

    show rin 2 sm school d with dict_dissolve_25

    voice "2RI_1588"
    rin "\"......\""

    "One person being entirely reliant on another is no kind of relationship."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou3_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
