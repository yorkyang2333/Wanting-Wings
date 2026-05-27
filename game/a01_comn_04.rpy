label a01_comn_04:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg05ba with Dissolve(0.25)
    pause 0.75

    play music bgm01
    play sound se001b

    show hina:
        "hina 1 sm school_scarf a flat"
        alpha 0.0 xcenter 822
        easein 0.5 alpha 1.0 xcenter 722
    show sachiko 1 sm outfit a at pos_l with Dissolve(0.25)

    voice "SYO_0001"
    sachiko "\"Welcome back!\"" id a01_comn_04_ba8847f1

    show hina 1 sm school_scarf a:
        alpha 1.0 xcenter 722
    with None

    show hina 1 sm school_scarf h with dict_dissolve_25

    voice "HIN_0064"
    hina "\"I'm...! Home...\"" id a01_comn_04_ce838261

    "Hina froze with her hand on the doorknob as she was ambushed from inside."

    show sachiko:
        "sachiko 1 sm outfit f" with Dissolve(0.25)
        xcenter 252
        easein 1.0 xcenter 302

    voice "SYO_0002"
    sachiko "\"Another cold day today~\"" id a01_comn_04_46c174bd

    show sachiko 1 sm outfit f:
        xcenter 302
    with None

    show hina:
        "hina 1 sm school_scarf e" with Dissolve(0.25)
        xcenter 722
        easein 1.0 xcenter 772

    voice "HIN_0065"
    hina "\"I-It wasn't that bad.\"" id a01_comn_04_2e2cae6e

    show hina 1 sm school_scarf e:
        xcenter 772
    with None

    "Her ambusher drew closer. Hina moved in an arc around the lobby, trying to maintain distance between them."

    show sachiko:
        xcenter 302
        easein 1.0 xcenter 352

    voice "SYO_0003"
    sachiko "\"Don't be so wary, Hinacchi.\"" id a01_comn_04_ea99d477

    show sachiko:
        xcenter 352
    with None

    play sound se133b

    show hina:
        "hina 1 sm school_scarf e flat"
        alpha 1.0 xcenter 772
        easeout 0.25 alpha 0.0 xcenter 822

    "Backed up against the wall, Hina ducked to make it past the woman's side."

    hide hina
    with None

    $ side_image = "hina 1 side school_scarf f"

    voice "HIN_0066"
    hina "\"Feint!\"" id a01_comn_04_15bb95b6

    "She made as if to go right but then sped in the other direction. And she was quick, but—"

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0004"
    sachiko "\"It doesn't work if you say it out loud! But your dopiness is why I love you!\"" id a01_comn_04_f5640098

    hide hina
    hide sachiko
    with Dissolve(0.05)
    pause 0.2

    play sound se118b

    show hina 1 lg school_scarf f at pos_r

    show sachiko 1 lg outfit e behind hina:
        xcenter 527
    with Dissolve(0.25)

    "Her right arm snaked out unerringly and wrapped itself around Hina like a chameleon's tongue."

    show hina 1 lg school_scarf d with Dissolve(0.25)
    show hina:
        function LayerShake(40,40,0.8)
    $ persistent.layer_shaken = False

    voice "HIN_0067"
    hina "\"Nyaaa!!\"" id a01_comn_04_51f06141

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko 1 lg outfit f" with Dissolve(0.25)
        ShakeUji

    voice "SYO_0005"
    sachiko "\"So warm~ Nymphets like you run hot, don't they?\"" id a01_comn_04_f2132e84

    show sachiko 1 lg outfit f:
        xoffset 0 yoffset 0
    with None

    "The hunter savored her prey's warmth with her whole body."

    show hina 2 lg school_scarf j with Dissolve(0.25)
    show hina:
        ShakeYes2

    voice "HIN_0068"
    hina "\"Don't call me that!\"" id a01_comn_04_d609510f

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 lg outfit e with dict_dissolve_25

    voice "SYO_0006"
    sachiko "\"Your cheeks are so soft, too~\"" id a01_comn_04_72c4522d

    show hina 1 lg school_scarf l with Dissolve(0.25)
    show hina:
        ShakeSide

    voice "HIN_0069"
    hina "\"You smell like cigarettes! Get off me, you sexual harasser!\"" id a01_comn_04_1bb265c0

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "SYO_0007"
    sachiko "\"Harassment? I'm just giving you a hug, Hinacchi.\"" id a01_comn_04_c4785684

    show hina 1 lg school_scarf f with dict_dissolve_25

    voice "HIN_0070"
    hina "\"If the victim sees it as harassment, it's harassment, you pervert!\"" id a01_comn_04_c796d8e9

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "SYO_0008"
    sachiko "\"If you're gonna be mean, then... I'll do this! Tickle tickle tickle~!\"" id a01_comn_04_44033b3b

    show hina 2 lg school_scarf j with Dissolve(0.25)
    show hina:
        function LayerShake(20,5,1.0)
    $ persistent.layer_shaken = False

    voice "HIN_0071"
    hina "\"Ahaha! Ahahahahaha!! No, anything but that!\"" id a01_comn_04_fa70f4c0

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko 1 lg outfit e" with Dissolve(0.25)
        ShakeTameiki

    voice "SYO_0009"
    sachiko "\"Heheheh, is this your weak point?!\"" id a01_comn_04_ce681a33

    show sachiko 1 lg outfit e:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg school_scarf l with Dissolve(0.25)
    show hina:
        ShakeJump

    voice "HIN_0072"
    hina "\"S-Stooop!\"" id a01_comn_04_d0a39f80

    play bgv "voice/HIN_BGV.opus" fadein 0.5

    hide hina
    hide sachiko
    with Dissolve(0.25)

    play sound se001b

    show rin:
        "rin 1 sm school_scarf a flat"
        alpha 0.0 xcenter 612
        easein 1.0 alpha 1.0 xcenter 512


    show fumi at pos_r:
        "fumi 1 sm school_scarf e flat"
        alpha 0.0 xcenter 872
        1.0
        easein 1.0 alpha 1.0 xcenter 772

    voice "RIN_0067"
    rin "\"Hello... Yeesh, not this again.\"" id a01_comn_04_fa2af927

    show rin 1 sm school_scarf a:
        alpha 1.0 xcenter 512
    show fumi 1 sm school_scarf e:
        alpha 1.0 xcenter 772
    with None

    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0009a"
    sachiko "\"Oh, Rin and Foomin. Welcome back~\"" id a01_comn_04_9d9adb2d

    show fumi 1 sm school_scarf a with dict_dissolve_25

    voice "FUM_0050"
    fumi "\"We're home.\"" id a01_comn_04_ffeeabbd

    $ side_image = "hina 2 side school_scarf j"

    voice "HIN_0074"
    hina "\"R-Rin! Asou! H-Help me!!\"" id a01_comn_04_8558082d

    show fumi 1 sm school_scarf d with dict_dissolve_25

    voice "FUM_0051"
    fumi "\"You're really fond of Natsume, aren't you, Sachiko?\"" id a01_comn_04_95d66647

    $ side_image = "sachiko 1 side outfit g"

    voice "SYO_0010"
    sachiko "\"Oh, it's not just Hinacchi. I'm head-over-heels for you too, Foomin.\"" id a01_comn_04_7bc9d1a4

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "RIN_0068"
    rin "\"What about me?\"" id a01_comn_04_3f3a9f19

    $ side_image = "sachiko 1 side outfit d"

    voice "SYO_0011"
    sachiko "\"There's nothing that cute about you, Rin.\"" id a01_comn_04_f8292ee0

    show rin 1 sm school_scarf b with dict_dissolve_25

    voice "RIN_0069"
    rin "\"I suppose you won't be needing these, then.\"" id a01_comn_04_2836284b

    "Rin dug a pack of cigarettes out of her pocket."

    $ side_image = "sachiko 1 side outfit j"

    voice "SYO_0012"
    sachiko "\"I do. I super do. I love you, Rin!\"" id a01_comn_04_1ebfff7e

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "RIN_0070"
    rin "\"Haah...\"" id a01_comn_04_8c41ee0a

    stop bgv

    play sound se118c

    "Rin tossed the cigarettes in a high arc and Sachiko reached up to catch them. Freed from her restraint, Hina sunk to the floor."

    $ side_image = "sachiko 1 side outfit g"

    voice "SYO_0013"
    sachiko "\"Thanks, hon♪\"" id a01_comn_04_d125318c

    show hina 1 sm school_scarf h at pos_l
    show rin 1 sm school_scarf a
    with Dissolve(0.25)

    show hina:
        ShakeTameiki
        0.4
        ShakeYes
        0.3
        ShakeYes

    voice "HIN_0075"
    hina "\"Huff... huff... huff...\"" id a01_comn_04_e2b04073

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school_scarf b with dict_dissolve_25

    voice "RIN_0071"
    rin "\"I really don't think you should be sending students out to buy cigarettes for you.\"" id a01_comn_04_ed735e83

    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0014"
    sachiko "\"Well, there's no vending machines anywhere close to the dorm. What's for dinner tonight, by the way?\"" id a01_comn_04_971681cc

    "Dismissing Rin's comment, Sachiko eyed the reusable shopping bag Fumi was carrying."

    hide fumi
    hide rin
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show fumi 1 lg school_scarf b with Dissolve(0.25)

    voice "FUM_0052"
    fumi "\"I'll be making—\"" id a01_comn_04_312a76ed

    $ side_image = "sachiko 1 side outfit i"

    voice "SYO_0015"
    sachiko "\"Wait, let me guess. Chicken thighs, tomatoes, potatoes, onions, mushrooms...\"" id a01_comn_04_fd003d9f

    $ side_image = "sachiko 1 side outfit f"

    voice "SYO_0016"
    sachiko "\"I got it! Meat and potato stew!\"" id a01_comn_04_bdc9bbdf

    show fumi 1 lg school_scarf d with dict_dissolve_25

    voice "FUM_0053"
    fumi "\"What about the tomatoes?\"" id a01_comn_04_e5302cce

    $ side_image = "sachiko 1 side outfit h"

    voice "SYO_0017"
    sachiko "\"What?! You put tomatoes in meat and potato stew at your house, Foomin?!\"" id a01_comn_04_9169d5f8

    show fumi:
        "fumi 1 lg school_scarf e" with Dissolve(0.25)
        ShakeJump

    voice "FUM_0054"
    fumi "\"Huh? Huh?\"" id a01_comn_04_f785417d

    show fumi 1 lg school_scarf e:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0018"
    sachiko "\"I'm just kidding. It's a potato and tomato stew, right?\"" id a01_comn_04_86fa8d6c

    show fumi:
        "fumi 1 lg school_scarf d" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0055"
    fumi "\"C-Correct.\"" id a01_comn_04_39cd55ac

    show fumi 1 lg school_scarf d:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit b"

    voice "SYO_0019a"
    sachiko "\"Stew, because it's cold today, and western-style, because you want to get rid of the rest of the white wine...\"" id a01_comn_04_8418fede

    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0019b"
    sachiko "\"It's tomato-based because the chicken was on sale today, and you're probably putting potatoes in instead of celery because Rin complained. Am I on the mark?\"" id a01_comn_04_7111e559

    show fumi 1 lg school_scarf e with dict_dissolve_25

    voice "FUM_0056"
    fumi "\"Where were you watching from?!\"" id a01_comn_04_a32489d2

    $ side_image = "sachiko 1 side outfit g"

    voice "SYO_0020"
    sachiko "\"Oh, it's simple deduction. Isn't that right, Rin?\"" id a01_comn_04_8f2fe7d6

    hide fumi
    hide rin
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show rin 1 lg school_scarf a at pos_l
    show fumi 1 lg school_scarf e at pos_r
    with Dissolve(0.25)

    voice "RIN_0072"
    rin "\"Well, I think I'll grab Hina and get back to our room.\"" id a01_comn_04_523eb181

    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0021"
    sachiko "\"Oh, you got mail today, Rin. From home.\"" id a01_comn_04_5092e780

    show rin 1 lg school_scarf b with dict_dissolve_25

    voice "RIN_0073"
    rin "\"Oh. Thanks.\"" id a01_comn_04_9f070993

    play sound se015a

    "Sachiko took an envelope out of her pocket and handed it to Rin. Rin stuffed it into her own pocket without even looking at it."

    show fumi 2 lg school_scarf b with dict_dissolve_25

    voice "FUM_0057"
    fumi "\"Is it your handout?\"" id a01_comn_04_07da2080

    voice "RIN_0074"
    rin "\"Probably.\"" id a01_comn_04_3c19a497

    show fumi 2 lg school_scarf a with dict_dissolve_25

    voice "FUM_0058"
    fumi "\"......\"" id a01_comn_04_620751b4

    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0022"
    sachiko "\"Say, Foomin, if you've got some of that tomato stew left over—\"" id a01_comn_04_756913ab

    show fumi:
        "fumi 1 lg school_scarf a" with Dissolve(0.25)
        ShakeYes

    voice "FUM_0059"
    fumi "\"Yes, I'll bring some to your room.\"" id a01_comn_04_d58550cd

    show fumi 1 lg school_scarf a:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit g"

    voice "SYO_0023a"
    sachiko "\"Yay! I knew there was a reason I married you, Foomin!\"" id a01_comn_04_2fa0c69f

    voice "RIN_0075"
    rin "\"Okay—hm?\"" id a01_comn_04_90d3d5bf

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2

    play sound se116a

    "Rin made to leave, but Sachiko grabbed the hem of her uniform to stop her."

    show rin 2 lg school_scarf g at pos_r
    show sachiko 1 lg outfit i at pos_l
    with Dissolve(0.25)

    voice "SYO_0024"
    sachiko "\"Money for the cigarettes, and... the goods.\"" id a01_comn_04_b171e112

    "Sachiko quickly handed Rin a few coins and a package the size of a couple of paperbacks."

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "SYO_0025"
    sachiko "\"Highly recommended.\"" id a01_comn_04_4f74583e

    show rin 2 lg school_scarf e with dict_dissolve_25

    voice "RIN_0076"
    rin "\"Oho.\"" id a01_comn_04_9f995074

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "SYO_0026"
    sachiko "\"Thanks in advance for next time, Rin!\"" id a01_comn_04_0484d367

    show rin 1 lg school_scarf f with dict_dissolve_25

    voice "RIN_0077"
    rin "\"Roger that.\"" id a01_comn_04_88063adc

    $ side_image = "fumi 2 side school_scarf h"

    voice "FUM_0060"
    fumi "\"??\"" id a01_comn_04_14220511

    stop music fadeout 1.0
    stop sound fadeout 1.0

    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
