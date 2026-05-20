label a02_comn_04:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg04ba with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show fumi 1 sm school_scarf a at pos_l2
    show rin 1 sm school_scarf a
    show hina 1 sm school a at pos_r2
    with Dissolve(0.25)

    voice "HIN_0365"
    hina "\"You should go home without me today.\""

    show rin 1 sm school_scarf e with dict_dissolve_25

    voice "RIN_0319"
    rin "\"Why?\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0366"
    hina "\"Today's the monthly class rep meeting.\""

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "FUM_0278"
    fumi "\"You work so hard every month. And we have exams right around the corner, too.\""

    show rin 1 sm school_scarf b with dict_dissolve_25

    voice "RIN_0320"
    rin "\"Today's what?\""

    show hina 1 sm school j with dict_dissolve_25

    voice "HIN_0367"
    hina "\"A meeting between all the class representatives. How many times have you asked me that, anyway? You really don't bother to remember anything you're not interested in, do you?\""

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "FUM_0279"
    fumi "\"Hahaha...\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0368"
    hina "\"So I'll be busy for two hours or so, but I should be back in time for dinner.\""

    show fumi:
        "fumi 1 sm school_scarf a" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0280"
    fumi "\"Sure thing.\""

    show fumi 1 sm school_scarf a:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0369"
    hina "\"See you later~\""

    play sound se000f

    show hina:
        "hina 1 sm school b flat"
        alpha 1.0 xcenter 852
        easeout 0.5 alpha 0.0 xcenter 952
    pause 0.5

    hide hina with None
    hide rin
    hide fumi
    with Dissolve(0.05)
    pause 0.2

    show rin 2 lg school_scarf g at pos_r
    show fumi 2 lg school_scarf h at pos_l
    with Dissolve(0.25)

    voice "FUM_0281"
    fumi "\".........\""

    voice "RIN_0321"
    rin "\"......\""

    "The two exchanged a glance."

    show fumi:
        "fumi 2 lg school_scarf c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0282"
    fumi "\"Well, should we get going?\""

    show fumi 2 lg school_scarf c:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg school_scarf e with dict_dissolve_25

    voice "RIN_0322"
    rin "\"Yeah. The bus to town is 30 minutes, so we'll have about an hour to shop.\""

    show fumi 2 lg school_scarf d with dict_dissolve_25

    voice "FUM_0283"
    fumi "\"Umm, could we stop by my father's store while we're out?\""

    show rin 1 lg school_scarf e with dict_dissolve_25

    voice "RIN_0323"
    rin "\"Ah, to order the cake?\""

    show fumi 1 lg school_scarf d with dict_dissolve_25

    voice "FUM_0284"
    fumi "\"Yeah. It's not far from the station, so it shouldn't take long.\""

    show rin 1 lg school_scarf c with dict_dissolve_25

    voice "RIN_0324"
    rin "\"Sure. I know what I'm buying, so we should have plenty of time.\""

    show fumi 1 lg school_scarf b with dict_dissolve_25

    voice "FUM_0285"
    fumi "\"We'll talk more details on the bus.\""

    show rin:
        ShakeYes

    voice "RIN_0325"
    rin "\"Okay.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a02_cou3_01
    else:
        jump a02_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
