label a01_comn_09:


    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg05ba with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show sachiko 1 lg outfit e with Dissolve(0.25)

    voice "SYO_0027"
    sachiko "\"Hinacchi! Hinacchi! I heard you got a picture of a ghost?!\"" id a01_comn_09_e3c1e856

    "She greeted them with her usual high energy."

    hide sachiko with Dissolve(0.05)
    pause 0.2

    show sachiko 1 sm outfit g:
        xcenter 184
    show hina 1 sm school_scarf j:
        xcenter 632
    show rin 1 sm school_scarf a behind hina, fumi:
        xcenter 776
    show fumi 1 sm school_scarf a:
        xcenter 940
    with Dissolve(0.25)

    voice "HIN_0194"
    hina "\"I-I did not.\"" id a01_comn_09_0ca30aa9

    voice "SYO_0028"
    sachiko "\"Lemme see! Lemme see!\"" id a01_comn_09_8f382ac7

    show hina 1 sm school_scarf k with dict_dissolve_25

    voice "HIN_0195"
    hina "\"I don't have it right now.\"" id a01_comn_09_7e23bbd0

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0029"
    sachiko "\"Whaaat? I wanna see it! I wanna see the ghost!\"" id a01_comn_09_6a9da71c

    show hina 1 sm school_scarf f with dict_dissolve_25

    voice "HIN_0196"
    hina "\"It's not a ghost!\"" id a01_comn_09_d375299a

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "FUM_0133"
    fumi "\"Should I go get it from our room?\"" id a01_comn_09_b5cfbb5c

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "SYO_0030"
    sachiko "\"You're always so nice, Foomin. I love you.\"" id a01_comn_09_19782686

    show fumi 1 sm school_scarf c with dict_dissolve_25

    voice "FUM_0134"
    fumi "\"I'll be right back.\"" id a01_comn_09_6dc540d4

    show fumi:
        "fumi 1 sm school_scarf c flat"
        alpha 1.0 xcenter 940
        easeout 0.5 alpha 0.0 xcenter 840
    pause 0.5

    hide fumi with None
    show hina 1 sm school_scarf j with dict_dissolve_25

    voice "HIN_0197"
    hina "\"You don't need to humor her.\"" id a01_comn_09_47bad93c

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0031"
    sachiko "\"I have a lot to say about the paranormal, you know~\"" id a01_comn_09_7ea88c33

    show hina 1 sm school_scarf h with dict_dissolve_25

    voice "HIN_0198"
    hina "\"You've already said too much.\"" id a01_comn_09_0e1f75ed

    show rin 1 sm school_scarf b with dict_dissolve_25

    voice "RIN_0179"
    rin "\"I'd like to know how to shut you up, personally.\"" id a01_comn_09_dcc663d7

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "SYO_0032"
    sachiko "\"That's easy. Just seal my lips with a kiss!\"" id a01_comn_09_91856a84

    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "HIN_0199"
    hina "\"I don't like talking to this lady~\"" id a01_comn_09_2c44cc6e

    show fumi behind hina, rin:
        "fumi 1 sm school_scarf c flat"
        alpha 0.0 xcenter 468
        linear 0.25 alpha 1.0
    show hina:
        "hina 1 sm school_scarf h" with Dissolve(0.25)
        easein 0.25 xcenter 700
    show rin:
        "rin 1 sm school_scarf b" with Dissolve(0.25)
        easein 0.25 xcenter 840

    voice "FUM_0135"
    fumi "\"Here it is~\"" id a01_comn_09_a9718df4

    show fumi 1 sm school_scarf c:
        alpha 1.0 xcenter 468
    show hina 1 sm school_scarf h:
        xcenter 700
    show rin 1 sm school_scarf b:
        xcenter 840
    with None

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0033"
    sachiko "\"Oh, that was fast. Thanks, Foomin♪\"" id a01_comn_09_b7094a4c

    "Sachiko took the picture, patting Fumi on the head."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0034"
    sachiko "\"Let's see here...\"" id a01_comn_09_81baf0e9

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "RIN_0180"
    rin "\"Can you tell what it is?\"" id a01_comn_09_b7425035

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0035"
    sachiko "\"A skyfish?!\"" id a01_comn_09_171bb47b

    show hina 1 sm school_scarf f with dict_dissolve_25

    voice "HIN_0200"
    hina "\"No!\"" id a01_comn_09_d45c0a27

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "SYO_0036"
    sachiko "\"Then, Mothman.\"" id a01_comn_09_4edd27e7

    show hina 1 sm school_scarf j with dict_dissolve_25

    voice "HIN_0201"
    hina "\"What's that?!\"" id a01_comn_09_974f145b

    show rin 1 sm school_scarf b with dict_dissolve_25

    voice "RIN_0181"
    rin "\"You don't have to give us a random list of cryptids. If you don't know, just say you don't know.\"" id a01_comn_09_79a8bbe0

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0037"
    sachiko "\"Mhm. Wonder what this is?\"" id a01_comn_09_d6dd7865

    show fumi:
        "fumi 1 sm school_scarf b" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0136"
    fumi "\"I think it's an angel~\"" id a01_comn_09_870bd329

    show fumi 1 sm school_scarf b:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "SYO_0038"
    sachiko "\"An angel...?\"" id a01_comn_09_b59fc0a6

    "Fumi nodded."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0039"
    sachiko "\"Well, we do have those rumors, don't we?\"" id a01_comn_09_dbecfa6c

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "RIN_0182"
    if persistent.dpatch:
        rin "\"Every school has stupid rumors like that. There's no such thing as angels.\"" id a01_comn_09_b2caa84c
    else:
        rin "\"Every campus has stupid rumors like that. There's no such thing as angels.\"" id a01_comn_09_be105e6f

    "She was being harsher than usual. And in front of Fumi, too."

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "SYO_0040"
    sachiko "\"No such thing... huh? I'd like to see you say that in front of the chaplain.\"" id a01_comn_09_c95f2af2

    show fumi 1 sm school_scarf h with dict_dissolve_25

    voice "FUM_0137"
    fumi "\"Hmm... You think so...?\"" id a01_comn_09_126dde90

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0041"
    sachiko "\"You know, I believe in angels.\"" id a01_comn_09_2d51b822

    show fumi 1 sm school_scarf b with dict_dissolve_25

    voice "FUM_0138"
    fumi "\"Sachiko!\"" id a01_comn_09_a517d756

    "Fumi took Sachiko's hand, her eyes sparkling."

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0042"
    sachiko "\"I mean—\"" id a01_comn_09_3e5b6474

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "FUM_0139"
    fumi "\"??\"" id a01_comn_09_2676249e

    hide fumi
    hide sachiko
    with Dissolve(0.05)
    pause 0.2

    play sound se118a

    show sachiko 1 lg outfit e:
        xcenter 220
    show fumi 1 lg school_scarf e:
        xcenter 500
    with Dissolve(0.25)

    voice "SYO_0043"
    sachiko "\"There's one right here in front of me!\"" id a01_comn_09_12b0b2fd

    show fumi:
        "fumi 1 lg school_scarf j" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0140"
    fumi "\"Aaaah?!\"" id a01_comn_09_cff1719d

    show fumi 1 lg school_scarf j:
        xoffset 0 yoffset 0
    with None
    show layer master:
        xcenter 0.5 ycenter 0.5 zoom 1.0 transform_anchor True
        easeout 0.5 zoom 1.33

    scene white with Dissolve(0.25)
    pause 0.5

    play sound se209a

    pause 1.0

    scene bg05ba with bg_effect_13
    pause 0.25

    show hina 1 sm school_scarf h at pos_l
    show rin 1 sm school_scarf e
    show fumi 1 sm school_scarf k at pos_r
    with Dissolve(0.25)

    voice "HIN_0202"
    hina "\"You can't let your guard down for a second with her!\"" id a01_comn_09_bdb2b7cf

    voice "RIN_0183"
    rin "\"Are you okay, Asou?\"" id a01_comn_09_bcfe8493

    show fumi:
        ShakeTameiki
        0.2
        ShakeYes
        0.5
        ShakeTameiki

    voice "FUM_0141"
    fumi "\"Haah, haah, haahh...\"" id a01_comn_09_de785867

    show fumi:
        xoffset 0 yoffset 0
    with None

    if persistent.dpatch:
        "...It's hard to believe this is an all-girls school with all the stuff these poor girls go through. Are they okay?" id a01_comn_09_0e67f6b3
    else:
        "...It's hard to believe this is an all-girls academy with all the stuff these poor girls go through. Are they okay?"

    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0044"
    sachiko "\"Oh, right. Remember what I asked about the other day?\"" id a01_comn_09_0cd8128a

    show hina 1 sm school_scarf j with dict_dissolve_25

    voice "HIN_0203"
    hina "\"No brakes, seriously.\"" id a01_comn_09_16743bbe

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "RIN_0184"
    rin "\"Modeling for a painting, was it?\"" id a01_comn_09_09483305

    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0045"
    sachiko "\"Yeah. I'll pay.\"" id a01_comn_09_b764ee5d

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "RIN_0185"
    rin "\"Not interested.\"" id a01_comn_09_2d5a973e

    $ side_image = "sachiko 1 side outfit e"

    voice "SYO_0046"
    sachiko "\"And I'll throw in an extra ten thousand if you do it nude!\"" id a01_comn_09_4815df34

    show hina:
        "hina 1 sm school_scarf f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0204"
    hina "\"Like hell!!\"" id a01_comn_09_93da0631

    show hina 1 sm school_scarf f:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "RIN_0186"
    rin "\"Okay, let's get out of here. Come on, Asou.\"" id a01_comn_09_ebcdf9c4

    $ side_image = "sachiko 1 side outfit j"

    voice "SYO_0047"
    sachiko "\"T-Twelve thousand!\"" id a01_comn_09_9edf3112

    show hina 1 sm school_scarf j with dict_dissolve_25

    voice "HIN_0205"
    hina "\"Shoo, shoo! Back to hell with you, demon!\"" id a01_comn_09_d689d423

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
