label a03_comn_05:

    scene bg05aa with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina 1 lg pyjama f with Dissolve(0.25)
    show hina:
        ShakeJump

    voice "HIN_0671"
    hina "\"HEY!\"" id a03_comn_05_8c907877

    show hina:
        xoffset 0 yoffset 0
    with None
    $ side_image = "sachiko 1 side outfit h"

    voice "SYO_0113"
    sachiko "\"Wah?!\"" id a03_comn_05_bb22a8ac

    hide hina with Dissolve(0.05)
    pause 0.2

    show rin 1 sm pyjama b:
        xcenter 96
    show fumi 1 sm pyjama e:
        xcenter 440
    show hina 1 sm pyjama j:
        xcenter 260
    show sachiko 1 sm outfit h:
        xcenter 836
    with Dissolve(0.25)

    voice "HIN_0672"
    hina "\"Stop giving weird books to Rin!\"" id a03_comn_05_5fff63dd

    "Hina thrust a stack of paperbacks out to Sachiko."

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "SYO_0114"
    sachiko "\"Oh, they found 'em?\"" id a03_comn_05_34fcb29c

    "Sachiko was looking over Hina's shoulder at Rin."

    show rin 1 sm pyjama g with dict_dissolve_25

    voice "RIN_0545"
    rin "\"While she was cleaning.\"" id a03_comn_05_3c294820

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "SYO_0115"
    sachiko "\"Whoopsie.\"" id a03_comn_05_2a2c61f5

    "They both raised their hands in a defeated shrug."

    show hina 1 sm pyjama f with dict_dissolve_25

    voice "HIN_0673"
    hina "\"What kind of dorm manager gives a student lewd books?\"" id a03_comn_05_182f6b51

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0116"
    sachiko "\"Lewd? Did you read them, Hinacchi?\"" id a03_comn_05_7b70dd24

    show hina:
        "hina 1 sm pyjama d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0674"
    hina "\"N-No, but you can tell from the titles!\"" id a03_comn_05_ba57ba59

    show hina 1 sm pyjama d:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0117"
    sachiko "\"Like what?\"" id a03_comn_05_b9bee292

    show hina 1 sm pyjama j with dict_dissolve_25

    voice "HIN_0675"
    if persistent.dpatch:
        hina "\"Umm... After-School Art Lessons with a Naughty Nude Model, My Girls' Dorm Tutor Harem, My Roommate's Dirty Secret Expo—Wait, don't make me read them!\"" id a03_comn_05_89f4ed67
    else:
        hina "\"Umm... After-Class Art Lessons with a Naughty Nude Model, My Girls' Dorm Tutor Harem, My Roommate's Dirty Secret Expo—Wait, don't make me read them!\"" id a03_comn_05_5b588c8b

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0118"
    sachiko "\"Didja like 'em, Rin?\"" id a03_comn_05_d1886905

    show rin 1 sm pyjama f with dict_dissolve_25

    voice "RIN_0546"
    rin "\"Yeah.\"" id a03_comn_05_9a3f266b

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0119"
    sachiko "\"Good, good.\"" id a03_comn_05_259c2039

    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0676"
    hina "\"Not good! I'm burning these!\"" id a03_comn_05_19ce92f2

    show hina 1 sm pyjama f:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0120"
    sachiko "\"Didn't think you'd advocate censorship, Hinacchi.\"" id a03_comn_05_5ab418e8

    show fumi 1 sm pyjama b with dict_dissolve_25

    voice "FUM_0496"
    fumi "\"Oh, we just did that in world history recently.\"" id a03_comn_05_9fdfe188

    show rin 1 sm pyjama a with dict_dissolve_25

    voice "RIN_0547"
    rin "\"Mm, 'Fahrenheit 451.'\"" id a03_comn_05_95d24ade

    show sachiko 1 sm outfit f with dict_dissolve_25

    voice "SYO_0121"
    sachiko "\"Hinacchi, eros is a part of human culture that we must be proud of. It's about what people feel for each other, and sharing those feelings so that you become one, which is when you achieve true pleasure—\"" id a03_comn_05_788f4e7a

    show rin 1 sm pyjama b with dict_dissolve_25

    voice "RIN_0548"
    rin "\"Do you even know what you're saying, Sachiko?\"" id a03_comn_05_325a40c4

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "SYO_0122"
    sachiko "\"Umm~...\"" id a03_comn_05_e7823ac3

    show rin 1 sm pyjama a with dict_dissolve_25

    voice "RIN_0549"
    rin "\"In other words...?\"" id a03_comn_05_9a8dc369

    show sachiko 1 sm outfit e with dict_dissolve_25

    voice "SYO_0123"
    sachiko "\"I want to watch and touch cute girls!\"" id a03_comn_05_93f717dc

    show hina 1 sm pyjama d with dict_dissolve_25

    voice "HIN_0677"
    hina "\"How can you say something like that in a girls' dorm?!\"" id a03_comn_05_c7277ed6

    show fumi 1 sm pyjama e with dict_dissolve_25

    voice "FUM_0497"
    fumi "\"Wow, your face is bright red.\"" id a03_comn_05_b51456cd

    show hina 1 sm pyjama i with dict_dissolve_25

    voice "HIN_0678"
    hina "\"I'm going back to our room!\"" id a03_comn_05_175006e2

    show hina:
        "hina 1 sm pyjama i flat"
        alpha 1.0 xcenter 260
        easeout 0.5 alpha 0.0 xcenter 160

    "Hina stomped off."

    hide hina with None

    if hina_fumi_score != 999:

        voice "FUM_0498"
        fumi "\"Ah, Natsume...\"" id a03_comn_05_a79e820e
    else:



        voice "FUM_0499"
        fumi "\"Ah, Hina...\"" id a03_comn_05_3585ba93

    show fumi:
        "fumi 1 sm pyjama e flat"
        alpha 1.0 xcenter 440
        easeout 0.5 alpha 0.0 xcenter 340

    "Fumi chased after her."

    hide fumi with None

    show rin:
        "rin 1 sm pyjama b" with Dissolve(0.25)
        xcenter 96
        easein 0.25 xcenter 252

    voice "RIN_0550"
    rin "\"Yeesh, you made her mad.\"" id a03_comn_05_c99a517d

    show sachiko:
        "sachiko 1 sm outfit d"
        xcenter 836
        easein 0.25 xcenter 772

    voice "SYO_0124"
    sachiko "\"Hinacchi's a pure maiden. I could really teach her a lot.\"" id a03_comn_05_e762e96e

    show rin 1 sm pyjama a with dict_dissolve_25

    voice "RIN_0551"
    rin "\"You could scar her for life, you mean.\"" id a03_comn_05_13eae812

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0125"
    sachiko "\"I'd be gentle!\"" id a03_comn_05_a38fa4be

    show rin 1 sm pyjama g with dict_dissolve_25

    voice "RIN_0552"
    rin "\"Haah...\"" id a03_comn_05_3762457a

    show rin 1 lg pyjama g
    show sachiko 1 lg outfit a
    with dict_dissolve_25

    voice "SYO_0126"
    sachiko "\"...Anyway, here's my new recommendation.\"" id a03_comn_05_1d717c3d

    show rin 1 lg pyjama c with dict_dissolve_25

    voice "RIN_0553"
    rin "\"Thanks.\"" id a03_comn_05_1db4d784

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a03_cou3_03
    else:
        jump a03_cou2_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
