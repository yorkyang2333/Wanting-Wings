label a01_comn_12:

    scene bg02ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina 1 lg pyjama a at pos_r
    show fumi 1 lg pyjama a at pos_l
    with Dissolve(0.25)

    voice "FUM_0185"
    fumi "\"Okay, do you want to handle this?\"" id a01_comn_12_9cf604ba

    show hina:
        "hina 1 lg pyjama c" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0258"
    hina "\"Bring it on!\"" id a01_comn_12_62cd7d63

    show hina 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None

    "Fumi handed Hina a bowl of eggs and seasoning, and Hina began to stir it vigorously."

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0259"
    hina "\"I'd like to eat in the chapel again.\"" id a01_comn_12_d6745822

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0186"
    fumi "\"Heheh. I said it was just for today when I prayed, though.\"" id a01_comn_12_da6219f5

    show hina 2 lg pyjama a with dict_dissolve_25

    voice "HIN_0260"
    hina "\"Next time, we can share a bit of our lunch with God. Then I bet He'll let us.\"" id a01_comn_12_d80a3d0c

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0187"
    fumi "\"You mean, like... an offering?\"" id a01_comn_12_3270407b

    voice "HIN_0261"
    if persistent.dpatch:
        hina "\"The chapel here's pretty impressive for the size of the school, don't you think?\"" id a01_comn_12_93fc4dca
    else:
        hina "\"The chapel here's pretty impressive for the size of the campus, don't you think?\"" id a01_comn_12_7f524392

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0188"
    if persistent.dpatch:
        fumi "\"Oh, it's the other way around, actually. They didn't build the chapel on school grounds; they built the school around the chapel.\"" id a01_comn_12_3c8d2971
    else:
        fumi "\"Oh, it's the other way around, actually. They didn't build the chapel on campus grounds; they built the campus around the chapel.\"" id a01_comn_12_948858cc

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0262"
    hina "\"So the chapel was here first?\"" id a01_comn_12_821140a2

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0189"
    fumi "\"Yes. The story goes that a woman awakened to her faith after hearing a prophecy from an angel, and she built a small chapel here.\"" id a01_comn_12_81e7ba36

    voice "HIN_0263"
    if persistent.dpatch:
        hina "\"I guess it makes sense there'd be rumors of angels at a school with a history like that.\"" id a01_comn_12_0d0988eb
    else:
        hina "\"I guess it makes sense there'd be rumors of angels at a campus with a history like that.\"" id a01_comn_12_a3141d39

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0190"
    if persistent.dpatch:
        fumi "\"I think so, too. Maybe that angel is still here, watching over the school from the chapel.\"" id a01_comn_12_0aa9bea3
    else:
        fumi "\"I think so, too. Maybe that angel is still here, watching over the campus from the chapel.\"" id a01_comn_12_4b9d9031

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0264"
    hina "\"......\"" id a01_comn_12_81776d45

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0191"
    fumi "\"Natsume?\"" id a01_comn_12_dcbbcc14

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0265"
    hina "\"Umm, actually, I—\"" id a01_comn_12_aeb5f526

    play sound se521

    $ side_image = "rin 1 side school a"

    voice "RIN_0209"
    rin "\"I'm back.\"" id a01_comn_12_0763b904

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0266"
    hina "\"H-Hey, Rin.\"" id a01_comn_12_61e39943

    "Hina swallowed the words she was about to say."

    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0192"
    fumi "\"Welcome back.\"" id a01_comn_12_3f9c2993

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show hina 1 sm pyjama k at pos_r2
    show rin 1 sm school c at pos_l2
    show fumi 1 sm pyjama a
    with Dissolve(0.25)

    voice "RIN_0210"
    rin "\"Would you like dinner? Or a bath? Or perhaps... me?\"" id a01_comn_12_444dae03

    show hina 1 sm pyjama h with dict_dissolve_25

    voice "HIN_0267"
    hina "\"Never heard that from the person coming home before.\"" id a01_comn_12_9486d927

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0193"
    fumi "\"Dinner's almost ready, so we should probably have our bath afterward.\"" id a01_comn_12_de669e52

    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_0211"
    rin "\"And the third option?\"" id a01_comn_12_c96d41b6

    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0268"
    hina "\"Quit getting in the way of the cooking! And stop lounging around in your uniform! Change!\"" id a01_comn_12_9c62da25

    show hina 1 sm pyjama f:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0212"
    rin "\"Yeah, yeah.\"" id a01_comn_12_1c61fd3d

    scene black with bg_effect_05
    pause 0.5

    scene bg02ca with bg_effect_05
    pause 0.5

    show rin 1 lg pyjama b with Dissolve(0.25)

    voice "RIN_0213"
    rin "\"......\"" id a01_comn_12_19ef068e

    "Rin peered at the two in the kitchen as she shrugged her tracksuit on."

    $ side_image = "fumi 2 side pyjama c"

    voice "FUM_0194"
    fumi "\"It'll be just a few more minutes.\"" id a01_comn_12_629eb05a

    show rin 1 lg pyjama a with Dissolve(0.25)
    show rin:
        ShakeYes2

    voice "RIN_0214"
    rin "\"Mhm, mhm.\"" id a01_comn_12_24908032

    show rin:
        xoffset 0 yoffset 0
    with None

    "She nodded as if coming to some understanding."

    $ side_image = "fumi 2 side pyjama d"

    voice "FUM_0195"
    fumi "\"C-Can I help you?\"" id a01_comn_12_bd537494

    show rin 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0215"
    rin "\"Oh, just thinking that your young wife vibes are through the roof as always.\"" id a01_comn_12_d2b5190a

    $ side_image = "hina 1 side pyjama f"

    voice "HIN_0269"
    hina "\"What is that supposed to mean?\"" id a01_comn_12_4ec7387c

    show rin 1 lg pyjama f with dict_dissolve_25

    voice "RIN_0216"
    rin "\"—And the kid helping out.\"" id a01_comn_12_9e27570b

    $ side_image = "hina 1 side pyjama f"

    voice "HIN_0270"
    hina "\"What was that?!\"" id a01_comn_12_232e8071

    $ side_image = "fumi 1 side pyjama d"

    voice "FUM_0196"
    fumi "\"I'm not sure how to take that.\"" id a01_comn_12_e9a38402

    show rin 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0217"
    rin "\"Oh, it's a compliment. There's no other girl in the world who looks so fantastic standing in a kitchen as you do.\"" id a01_comn_12_09e12234

    $ side_image = "fumi 1 side pyjama d"

    voice "FUM_0197"
    fumi "\"Th-Thank you?\"" id a01_comn_12_e9de6d92

    show rin 1 lg pyjama h with dict_dissolve_25

    voice "RIN_0218"
    rin "\"Kinda turns me on, too.\"" id a01_comn_12_857fd45a

    $ side_image = "fumi 2 side pyjama g"

    voice "FUM_0198"
    fumi "\"Umm, I...\"" id a01_comn_12_c889d1fd

    show rin:
        "rin 1 lg pyjama f" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 412
    pause 0.25

    voice "RIN_0219"
    rin "\"Fumi, you look so alluring again today. It's making me feel all sorts of ways.\"" id a01_comn_12_98f0124d

    show rin:

        "rin 1 lg pyjama f"
        "rin 2 lg pyjama e" with Dissolve(0.25)
        xcenter 412
        easein 0.25 xcenter 632
    pause 0.25

    show rin 2 lg pyjama e:
        ShakeNo

    voice "RIN_0220"
    rin "\"Save it for later, sweetie. The food's almost done.\"" id a01_comn_12_a5c5069d

    show rin:
        "rin 2 lg pyjama e"
        "rin 1 lg pyjama f" with Dissolve(0.25)
        xcenter 632 xoffset 0 yoffset 0
        easein 0.25 xcenter 412
    pause 0.25

    voice "RIN_0221"
    rin "\"No, I can't wait. I want you right now!\"" id a01_comn_12_5075003c

    show rin:
        "rin 1 lg pyjama f"
        "rin 2 lg pyjama e" with Dissolve(0.25)
        xcenter 412
        easein 0.25 xcenter 632
    pause 0.25

    show rin 2 lg pyjama e:
        xcenter 632
        ShakeJump
        4.0
        "rin 2 lg pyjama c"
        ShakeSide

    voice "RIN_0222"
    rin "\"Ah, no... when you're aggressive like that, I... No, the miso soup's going to get cold!\"" id a01_comn_12_5803fa84

    show rin 2 lg pyjama c:
        xoffset 0 yoffset 0
    with None

    $ side_image = "fumi 1 side pyjama d"

    voice "FUM_0199"
    fumi "\"Umm, Natsume, what do you suppose I should do...?\"" id a01_comn_12_f2fa1a27

    $ side_image = "hina 1 side pyjama h"

    voice "HIN_0271"
    hina "\"Just ignore her! You can't give her attention!\"" id a01_comn_12_a4dc00e4

    $ side_image = "fumi 1 side pyjama d"

    voice "FUM_0200"
    fumi "\"O-Okay.\"" id a01_comn_12_026f510b

    show rin 2 lg pyjama e with Dissolve(0.25)
    show rin:
        ShakeNo

    voice "RIN_0223"
    rin "\"No, our child's watching!\"" id a01_comn_12_ce29f0e1

    show rin:
        xoffset 0 yoffset 0
    with None

    show rin:
        "rin 1 lg pyjama f" with Dissolve(0.25)
        xcenter 632
        easein 0.25 xcenter 412
    pause 0.25

    voice "RIN_0224"
    rin "\"It's alright. Hina's just a baby. She's got no idea what's going on.\"" id a01_comn_12_06862666

    show rin 1 lg pyjama f:
        xcenter 412
    with None

    $ side_image = "hina 1 side pyjama j"

    voice "HIN_0272"
    hina "\"...That's it.\"" id a01_comn_12_032b60f1

    $ side_image = "fumi 2 side pyjama g"

    voice "FUM_0201"
    fumi "\"Ah...\"" id a01_comn_12_93e71132

    show hina:
        "hina 1 lg pyjama f flat"
        alpha 0.0 xcenter 612
        easein 0.25 alpha 1.0 xcenter 512

    show rin:
        "rin 1 lg pyjama e" with Dissolve(0.25)
        easein 0.25 xcenter 252

    voice "HIN_0273"
    hina "\"Kyeeeeh!\"" id a01_comn_12_b0e97e16

    show rin 1 lg pyjama e:
        xcenter 252
    show hina 1 lg pyjama f:
        alpha 1.0 xcenter 512
    with None

    show rin:
        "rin 1 lg pyjama j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0225"
    rin "\"Hey! Whoa! Put the knife down...\"" id a01_comn_12_9e7d18c6

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a01_comn_13
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
