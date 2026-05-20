label a08_cou2_01:

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina 2 lg school a at pos_l
    show rin 1 lg school a at pos_r
    with dict_dissolve_25

    voice "2RI_0633"
    rin "\"That's economics right there. Girls all over Japan are buying chocolate, right? Aren't the economic implications just fascinating?\""

    "Rin looked on at the early Valentine's atmosphere blossoming around Fumi's desk with a mix of wonder and scorn on her face."

    show rin 1 lg school h with dict_dissolve_25

    voice "2RI_0634"
    rin "\"I want to put a Valentine's tax on it and make a sweet profit.\""

    "Would that be in chocolate coins?"

    show hina 1 lg school e with dict_dissolve_25

    voice "2HI_0624"
    hina "\"On what authority?\""

    show rin 1 lg school a with dict_dissolve_25

    voice "2RI_0635"
    rin "\"I'm sure you were the type to receive chocolates, right, Hina?\""

    show hina 1 lg school j with dict_dissolve_25

    voice "2HI_0625"
    hina "\"I don't like the way you asked that.\""

    show rin 2 lg school a with dict_dissolve_25

    voice "2RI_0636"
    rin "\"You're being paranoid. So? Am I right?\""

    show hina 2 lg school e with dict_dissolve_25

    voice "2HI_0626"
    hina "\"Well... yeah.\""

    show rin 1 lg school c with dict_dissolve_25

    voice "2RI_0637"
    rin "\"Knew it.\""

    $ side_image = "miyako 1 side school_a b"

    voice "2MI_0528"
    miyako "\"You were popular, huh~?\""

    show hina 1 lg school n with dict_dissolve_25

    voice "2HI_0627"
    hina "\"I think it's more like I just wasn't considered a girl.\""

    show rin 1 lg school f with dict_dissolve_25

    voice "2RI_0638"
    rin "\"Have you always shaved your head?\""

    show hina:
        "hina 1 lg school g" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0628"
    hina "\"I had long hair in grade school!\""

    show hina 1 lg school g:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school c with dict_dissolve_25

    voice "2RI_0639"
    rin "\"Then you only shaved it in middle school?\""

    show hina:
        ShakeJump
        ShakeJump

    voice "2HI_0629"
    hina "\"I've never shaved my head!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 lg school k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0640"
    rin "\"Well, you don't have your secondary sex characteristics yet. Your voice hasn't changed yet, either.\""

    show rin 1 lg school k:
        xoffset 0 yoffset 0
    with None
    show hina:
        ShakeJump

    voice "2HI_0630"
    hina "\"My voice is never going to change!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school d with dict_dissolve_25

    voice "2RI_0641"
    rin "\"Hahahaha!\""

    show hina 1 lg school f with dict_dissolve_25

    voice "2HI_0631"
    hina "\"Shut up already! I got a lot of chocolate from girls, okay?! What, are you jealous?!\""

    "Hina snapped."

    show rin 1 lg school c with dict_dissolve_25

    voice "2RI_0642B"
    rin "\"I actually happen to have received quite a bit myself~ Oh, my hair's always been long, though~\""

    "Rin brushed a hand through her hair like she was in a shampoo commercial. It's irritating to admit it, but she does look good."

    show hina 2 lg school f with dict_dissolve_25

    voice "2HI_0632"
    hina "\"...How much?\""

    show rin 1 lg school f with dict_dissolve_25

    voice "2RI_0643"
    rin "\"I would say 40 to 50 was the average per year. I mean, it wasn't enough to have to carry it in a truck or anything.\""

    $ side_image = "miyako 1 side school_a e"

    voice "2MI_0529"
    miyako "\"Wow~\""

    show rin 1 lg school c with dict_dissolve_25

    voice "2RI_0644"
    rin "\"I guess I was pretty popular~\""

    "Well, she is attractive. She's got that much going for her at least."

    show hina:
        "hina 2 lg school i" with Dissolve(0.25)
        ShakeNo

    voice "2HI_0633"
    hina "\"Uuuuuuugh.\""

    show hina 2 lg school i:
        xoffset 0 yoffset 0
    with None

    "Hina's mood was only worsening."

    show rin 1 lg school d with dict_dissolve_25

    voice "2RI_0645"
    rin "\"Don't be jealous~\""

    show hina 2 lg school h with dict_dissolve_25

    voice "2HI_0634"
    hina "\"I'm... not jealous.\""

    show rin 1 lg school f with dict_dissolve_25

    voice "2RI_0646"
    rin "\"It's better to have a popular girlfriend than an unpopular one, right?\""

    voice "2HI_0635"
    hina "\".........\""

    $ side_image = "miyako 1 side school_a d"

    voice "2MI_0530"
    miyako "\"You must have gotten really full eating all that chocolate!\""

    "And this one's impressed about something weird."

    show hina 2 lg school d with dict_dissolve_25

    voice "2HI_0636"
    hina "\"Th-This year, I'll give you—\""

    show rin:
        "rin 1 lg school k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0647"
    rin "\"Sick of it, more like. I'm not even all that into sweets in the first place~\""

    show rin 1 lg school k:
        xoffset 0 yoffset 0
    with None

    "Hina's words petered out before even reaching Rin's ears."

    hide rin
    hide hina
    with Dissolve(0.5)
    pause 0.5

    $ side_image = "fumi 1 side school d"

    voice "2FU_0529"
    fumi "\"Sorry I'm late.\""

    $ side_image = "rin 1 side school c"

    voice "2RI_0648"
    rin "\"Hey, good work.\""

    "Rin welcomed Fumi to them when she returned, looking apologetic."

    show hina 2 lg school h at pos_l with dict_dissolve_25

    voice "2HI_0637"
    hina "\"......\""

    "Meanwhile, Hina was stewing in her feelings now that they had nowhere to go."

    show miyako 2 lg school c at pos_r with dict_dissolve_25

    voice "2MI_0531"
    miyako "\"It's alright.\""

    "Miyako put a gentle hand on her back."

    show hina 2 lg school c with dict_dissolve_25

    voice "2HI_0638"
    hina "\"Thanks.\""

    "Hina turned to her and smiled."

    $ side_image = "rin 1 side school c"

    voice "2RI_0649"
    rin "\"Okay, now that we're all done here, let's get going.\""

    show hina 1 lg school b with dict_dissolve_25

    voice "2HI_0639"
    hina "\"Yeah!\""

    "Hina grabbed her bag and ran off."

    hide hina
    hide miyako
    with dict_dissolve_50

    "......"

    "She definitely is a girl."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if routes_cleared != 0:
        jump a08_comn_03
    else:
        jump a08_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
