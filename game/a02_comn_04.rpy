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
    hina "\"You should go home without me today.\"" id a02_comn_04_4c13a6fb

    show rin 1 sm school_scarf e with dict_dissolve_25

    voice "RIN_0319"
    rin "\"Why?\"" id a02_comn_04_5c69ea6b

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0366"
    hina "\"Today's the monthly class rep meeting.\"" id a02_comn_04_b642f340

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "FUM_0278"
    fumi "\"You work so hard every month. And we have exams right around the corner, too.\"" id a02_comn_04_674d5a4c

    show rin 1 sm school_scarf b with dict_dissolve_25

    voice "RIN_0320"
    rin "\"Today's what?\"" id a02_comn_04_a7e8d18f

    show hina 1 sm school j with dict_dissolve_25

    voice "HIN_0367"
    hina "\"A meeting between all the class representatives. How many times have you asked me that, anyway? You really don't bother to remember anything you're not interested in, do you?\"" id a02_comn_04_df28400b

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "FUM_0279"
    fumi "\"Hahaha...\"" id a02_comn_04_fcfb5065

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0368"
    hina "\"So I'll be busy for two hours or so, but I should be back in time for dinner.\"" id a02_comn_04_95406328

    show fumi:
        "fumi 1 sm school_scarf a" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0280"
    fumi "\"Sure thing.\"" id a02_comn_04_1177377d

    show fumi 1 sm school_scarf a:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0369"
    hina "\"See you later~\"" id a02_comn_04_f9d33cd2

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
    fumi "\".........\"" id a02_comn_04_3a9d94d0

    voice "RIN_0321"
    rin "\"......\"" id a02_comn_04_8eb8dcea

    "The two exchanged a glance."

    show fumi:
        "fumi 2 lg school_scarf c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0282"
    fumi "\"Well, should we get going?\"" id a02_comn_04_9c1353af

    show fumi 2 lg school_scarf c:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg school_scarf e with dict_dissolve_25

    voice "RIN_0322"
    rin "\"Yeah. The bus to town is 30 minutes, so we'll have about an hour to shop.\"" id a02_comn_04_4821290c

    show fumi 2 lg school_scarf d with dict_dissolve_25

    voice "FUM_0283"
    fumi "\"Umm, could we stop by my father's store while we're out?\"" id a02_comn_04_4aed3c33

    show rin 1 lg school_scarf e with dict_dissolve_25

    voice "RIN_0323"
    rin "\"Ah, to order the cake?\"" id a02_comn_04_115becbb

    show fumi 1 lg school_scarf d with dict_dissolve_25

    voice "FUM_0284"
    fumi "\"Yeah. It's not far from the station, so it shouldn't take long.\"" id a02_comn_04_f1651864

    show rin 1 lg school_scarf c with dict_dissolve_25

    voice "RIN_0324"
    rin "\"Sure. I know what I'm buying, so we should have plenty of time.\"" id a02_comn_04_3a84beff

    show fumi 1 lg school_scarf b with dict_dissolve_25

    voice "FUM_0285"
    fumi "\"We'll talk more details on the bus.\"" id a02_comn_04_8d4106a2

    show rin:
        ShakeYes

    voice "RIN_0325"
    rin "\"Okay.\"" id a02_comn_04_56ac4312

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a02_cou3_01
    else:
        jump a02_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
