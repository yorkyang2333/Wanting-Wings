label a03_cou3_05:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show hina 1 lg pyjama c at pos_r2
    show rin 1 lg pyjama glasses a at pos_l2
    show fumi 1 lg pyjama a
    with Dissolve(0.25)

    voice "HIN_0953"
    hina "\"That was great!\"" id a03_cou3_05_3e0a1d0f

    "Hina exclaimed as she polished off her meal."

    show hina 2 lg pyjama c with dict_dissolve_25

    voice "HIN_0954"
    hina "\"It was tasty as always. Thanks for cooking all the time.\"" id a03_cou3_05_fd9166ba

    show fumi 1 lg pyjama b with dict_dissolve_25

    voice "FUM_0737"
    fumi "\"Don't mention it. I'm just happy you enjoy it so much.\"" id a03_cou3_05_5da65d4d

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0825"
    rin "\"...Thanks.\"" id a03_cou3_05_ac927055

    "Rin belatedly repeated the sentiment."

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0955"
    hina "\"What's wrong? Not hungry?\"" id a03_cou3_05_833db998

    "Rin's bowl still had a third of its rice left."

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0826"
    rin "\"Mm, it's like my chest is full or something...\"" id a03_cou3_05_7bad688f

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0956"
    hina "\"Does your stomach hurt? Did you catch a cold going out on the roof last night?\"" id a03_cou3_05_0b4c75d8

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0827"
    rin "\"No, nothing like that.\"" id a03_cou3_05_06a217eb

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0957"
    hina "\"You sure?\"" id a03_cou3_05_92e344b7

    "Hina peered worriedly at Rin's face."

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "FUM_0738"
    fumi "\"Let me clean up, then.\"" id a03_cou3_05_96b264ef

    show fumi:
        "fumi 1 lg pyjama a flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 612
    pause 0.5

    hide fumi with None

    "Fumi stood up and headed into the kitchen."

    show rin:
        "rin 1 lg pyjama glasses e" with Dissolve(0.25)
        xcenter 172
        easein 0.25 xcenter 252
    show hina:
        "hina 2 lg pyjama f" with Dissolve(0.25)
        xcenter 852
        easein 0.25 xcenter 772
    pause 0.25

    voice "RIN_0828"
    rin "\"Oh, I'll help.\"" id a03_cou3_05_e2ac9fe0

    show rin 1 lg pyjama glasses e:
        xcenter 252
    show hina 2 lg pyjama f:
        xcenter 772
    with None

    play sound se009d

    show rin:
        ShakeYes

    "Rin said, stacking up the dishes on the table."

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0958"
    hina "\".........\"" id a03_cou3_05_311e2675

    "Hina watched her curiously, and..."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0829"
    rin "\"...What?\"" id a03_cou3_05_8996e530

    "...Rin said when she noticed."

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0959"
    hina "\"I was just thinking it's rare for you to help with the dishes.\"" id a03_cou3_05_043336f2

    show rin:
        "rin 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0830"
    rin "\"Y-You think so?\"" id a03_cou3_05_2d5ef5ef

    show rin 1 lg pyjama glasses i:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg pyjama h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0960"
    hina "\"I mean, you always just lie around after you eat.\"" id a03_cou3_05_4045b55a

    show hina 1 lg pyjama h:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0831"
    rin "\"Well, I've had a change of heart, and I'll be helping from now on.\"" id a03_cou3_05_63a4c242

    show rin:
        "rin 1 lg pyjama glasses h flat"
        alpha 1.0 xcenter 252
        easeout 0.5 alpha 0.0 xcenter 352
    pause 0.5

    hide rin with None

    "Rin stood up and brought the dishes to the kitchen."

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0961"
    hina "\"...Well, there's nothing wrong with that.\"" id a03_cou3_05_07277cf2

    scene black with bg_effect_01_1000
    pause 0.5

    scene bg02ca with bg_effect_01_1000
    pause 0.5

    play sound se056b_100

    show rin 1 lg pyjama glasses h at pos_r
    show fumi 1 lg pyjama b at pos_l
    with Dissolve(0.25)

    stop sound fadeout 15.0

    voice "FUM_0739"
    fumi "\"Can you rinse them, then?\"" id a03_cou3_05_c275594d

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0832"
    rin "\"Sure.\"" id a03_cou3_05_75f2e401

    "They worked in tandem, standing together at the sink."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0833"
    rin "\"Sorry for last night. You didn't catch a cold, did you?\"" id a03_cou3_05_a705388c

    show fumi 2 lg pyjama c with dict_dissolve_25

    voice "FUM_0740"
    fumi "\"I'm just fine, thank you.\"" id a03_cou3_05_bd7884ca

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0834"
    rin "\"Good. If you got sick, I wouldn't be able to tempt you again for a while.\"" id a03_cou3_05_9ad91093

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_0741"
    fumi "\"Oh? You're going to tempt me again?\"" id a03_cou3_05_198b5611

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0835"
    rin "\"Of course I am. We can't just leave things there, can we?\"" id a03_cou3_05_b08dddb7

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "FUM_0742"
    fumi "\"Ahaha. You're kind of making me nervous.\"" id a03_cou3_05_cbf744d8

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0836"
    rin "\"...You're just as unruffled as always.\"" id a03_cou3_05_3bdd5dcc

    show fumi 2 lg pyjama f with dict_dissolve_25

    voice "FUM_0743"
    fumi "\"I told you that's not true.\"" id a03_cou3_05_d72988d8

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0837"
    rin "\"Do you actually want to keep going from where we stopped yesterday?\"" id a03_cou3_05_198f7a70

    show fumi 2 lg pyjama h with dict_dissolve_25

    voice "FUM_0744"
    fumi "\"......\"" id a03_cou3_05_03fea6db

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0838"
    rin "\"I-If you don't... you can tell me. I know I can get carried away...\"" id a03_cou3_05_28076461

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    voice "FUM_0745"
    fumi "\"I do... want to keep going.\"" id a03_cou3_05_3606504d

    show rin 1 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0839"
    rin "\"...Okay.\"" id a03_cou3_05_4f5ebf50

    show fumi 2 lg pyjama b with dict_dissolve_25

    voice "FUM_0746"
    fumi "\"If we get the chance...\"" id a03_cou3_05_4c34a538

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0840"
    rin "\"Right... if we get the chance.\"" id a03_cou3_05_8e747eab

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_cou3_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
