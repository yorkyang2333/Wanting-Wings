label a04_cou2_08:

    scene bg05bb with Dissolve(0.5)
    pause 1.5

    play music bgm02

    play sound se001b

    show rin behind fumi:
        "rin 1 sm school_scarf b flat"
        alpha 0.0 xcenter 762
        easein 0.5 alpha 1.0 xcenter 662
    show fumi:
        "fumi 1 sm school_scarf h flat"
        alpha 0.0 xcenter 962
        easein 0.5 alpha 1.0 xcenter 862
    pause 0.5

    show rin 1 sm school_scarf b behind fumi:
        alpha 1.0 xcenter 662
    show fumi 1 sm school_scarf h:
        alpha 1.0 xcenter 862
    with None

    voice "RIN_1191"
    rin "\"If she was gonna go home without us, she could have said something. She's not answering her phone, either.\"" id a04_cou2_08_dd768417

    show fumi 1 sm school_scarf k with dict_dissolve_25

    voice "FUM_1070"
    fumi "\"Maybe she's not feeling well. She seemed a little under the weather this morning.\"" id a04_cou2_08_d56adb40

    "Unlike yesterday, today it was these two who had been left behind. They made their way to their room, perplexed."

    scene black with bg_effect_02
    pause 0.5

    scene bg02ba with bg_effect_02
    pause 0.5

    play sound se521

    show rin 1 sm school i with Dissolve(0.25)

    voice "RIN_1192"
    rin "\"Hey, Hina, why'd you go home without us?\"" id a04_cou2_08_5f0f9ed4

    "Rin called into the living room, pulling off her loafers."

    $ side_image = "fumi 1 side school h"

    voice "FUM_1071"
    fumi "\"Oh, she's not there.\"" id a04_cou2_08_43da0117

    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_1193"
    rin "\"Huh? Really? Then, her bed—nope...\"" id a04_cou2_08_899c03de

    "Rin peered into Hina's bed."

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_1194"
    rin "\"Hmm, wonder where she went.\"" id a04_cou2_08_37cf1689

    stop music fadeout 0.1

    $ side_image = "fumi 1 side school k"

    voice "FUM_1072"
    fumi "\"Ogata!\"" id a04_cou2_08_57dd211e

    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_1195"
    rin "\"Huh? What?\"" id a04_cou2_08_1e657eba

    "Rin hurried to the living room."

    scene black with bg_effect_12
    pause 0.25

    scene bg01ac
    show fumi 2 lg school f at pos_l
    with bg_effect_12
    pause 0.5

    show rin:
        "rin 2 lg school a flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772

    voice "FUM_1073"
    fumi "\"This was on Natsume's desk...\"" id a04_cou2_08_2f216fc4

    show rin 2 lg school a:
        alpha 1.0 xcenter 772
    with None

    "Fumi handed Rin an envelope that said, in Hina's handwriting:"

    show rin 2 lg school f with dict_dissolve_25

    voice "RIN_1196"
    rin "\"'To Rin'...?\"" id a04_cou2_08_10e2e831

    play music bgm05

    play sound se015a

    show rin 1 lg school h with dict_dissolve_25

    "Rin opened the envelope and pulled out the stationery inside. Fumi looked on worriedly."

    voice "RIN_1197"
    rin "\"'I can't live with you anymore. I'm sorry for being so selfish. Thank you for everything. I really loved you.'\"" (show_name=False) id a04_cou2_08_7610903c

    show rin:
        "rin 1 lg school g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_1198"
    rin "\"Huh? Wait, why? What is this?\"" id a04_cou2_08_8ba5f939

    show rin 1 lg school g:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg school a with dict_dissolve_25

    voice "FUM_1074"
    fumi "\"Did she... run away?\"" id a04_cou2_08_bd271f1a

    show rin:
        "rin 1 lg school j" with Dissolve(0.25)
        ShakeJump

    voice "RIN_1199"
    rin "\"But why would she do that?!\"" id a04_cou2_08_7edbb866

    show rin 1 lg school j:
        xoffset 0 yoffset 0
    with None
    show fumi 1 lg school h with dict_dissolve_25

    voice "FUM_1075"
    fumi "\"I don't know...\"" id a04_cou2_08_557e47f5

    show rin 1 lg school g with dict_dissolve_25

    play sound se026c

    voice "RIN_1200"
    rin "\"I'll try calling her agai—\"" id a04_cou2_08_d0ea1d43

    play sound se027a_150

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_1201"
    rin "\"Huh?\"" id a04_cou2_08_ea56bad4

    "Hearing something buzzing, she turned around to see Hina's flip phone vibrating on her desk."

    show rin 1 lg school g with dict_dissolve_25

    voice "RIN_1202"
    rin "\".........\"" id a04_cou2_08_79b2030e

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_1076"
    fumi "\"Umm, her wallet and train pass are here, too...\"" id a04_cou2_08_45c72b76

    show rin 2 lg school c with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "RIN_1203"
    rin "\"...What are you in such a rush for, you idiot...?\"" id a04_cou2_08_0e9caa10

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi 2 lg school f with dict_dissolve_25

    voice "FUM_1077"
    fumi "\"But she couldn't have gone far without them...\"" id a04_cou2_08_adcdfed8

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_1204"
    rin "\"Right. Let's split up and look nearby.\"" id a04_cou2_08_84f43de5

    scene black with bg_effect_01
    pause 0.5

    scene bg05bb with bg_effect_01
    pause 0.5

    play sound se521

    show sachiko 1 sm outfit i at pos_r with dict_dissolve_25
    show rin behind fumi:
        "rin 1 sm school h flat"
        alpha 0.0 xcenter 262
        easein 0.5 alpha 1.0 xcenter 362
    show fumi:
        "fumi 1 sm school h flat"
        alpha 0.0 xcenter 62
        easein 0.5 alpha 1.0 xcenter 162
    pause 0.5

    voice "SYO_0171"
    sachiko "\"You're going out? It started raining, you know.\"" id a04_cou2_08_5b77e3f6

    "Sachiko called out to the two of them on their way out the dorm."

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_1205"
    rin "\"Hina... ran away...\"" id a04_cou2_08_e00991a9

    show sachiko 1 sm outfit h with dict_dissolve_25

    voice "SYO_0172"
    sachiko "\"Huh? Ran away?\"" id a04_cou2_08_b249b23c

    show fumi 1 sm school k with dict_dissolve_25

    voice "FUM_1078"
    fumi "\"Oh, that's right, you didn't see her leave, did you?\"" id a04_cou2_08_3c706d05

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "SYO_0173"
    sachiko "\"Sorry, I didn't. Why would she run away, though?\"" id a04_cou2_08_4e40f6c2

    show rin 1 sm school h with dict_dissolve_25

    voice "RIN_1206"
    rin "\"That's what I want to know!\"" id a04_cou2_08_7ccd332b

    show fumi 1 sm school h with dict_dissolve_25

    voice "FUM_1079"
    fumi "\"You can't think of anything, can you, Sachiko?\"" id a04_cou2_08_fad72517

    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "SYO_0174"
    sachiko "\"Why she'd run away...?\"" id a04_cou2_08_a8d34edb

    "Sachiko folded her arms and pondered."

    show sachiko 1 sm outfit h with dict_dissolve_25

    voice "SYO_0175"
    sachiko "\"......Oh.\"" id a04_cou2_08_339c44bb

    "Sachiko snapped her fingers in realization."

    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_1207"
    rin "\"What?\"" id a04_cou2_08_02b9fc88

    show sachiko:
        "sachiko 1 sm outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "SYO_0176"
    sachiko "\"Shit, it might be my fault.\"" id a04_cou2_08_1438fa04

    show sachiko 1 sm outfit d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_1080"
    fumi "\"What? Why?\"" id a04_cou2_08_d96e156a

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0177"
    sachiko "\"Rin, did you tell Hina about the modeling?\"" id a04_cou2_08_3393762b

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_1208"
    rin "\"No, I've been keeping it a secret.\"" id a04_cou2_08_26e0e073

    show sachiko 1 sm outfit d with dict_dissolve_25

    voice "SYO_0178"
    sachiko "\"That must be it, then. I told her to tell you I'd be seeing you again tonight.\"" id a04_cou2_08_fb77a10b

    show rin 1 sm school h with dict_dissolve_25

    show fumi 1 sm school h with dict_dissolve_25

    voice "RIN_1209"
    rin "\".........\"" id a04_cou2_08_4c0bf628

    show sachiko 1 sm outfit c with dict_dissolve_25

    voice "SYO_0179"
    sachiko "\"Maybe she's got some weird misunderstanding. That we're together or something.\"" id a04_cou2_08_2776b5f6

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_1210"
    rin "\"No way. You're like twice my age.\"" id a04_cou2_08_78ee5cd4

    show sachiko 1 sm outfit h with dict_dissolve_25

    voice "SYO_0180"
    sachiko "\"Right... Hey, I am not!\"" id a04_cou2_08_f1883e1f

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_1211"
    rin "\"That idiot!\"" id a04_cou2_08_67a74acf

    play sound se137b

    show rin:
        "rin 1 sm school g flat"
        alpha 1.0 xcenter 362
        easeout 0.25 alpha 0.0 xcenter 462

    "Rin stomped her foot and ran out of the dorm."

    hide rin with None
    show fumi:
        "fumi 1 sm school k" with Dissolve(0.25)
        xcenter 162
        easein 0.25 xcenter 252


    voice "FUM_1081"
    fumi "\"I-I'm coming too!\"" id a04_cou2_08_4b9193a7

    show sachiko 1 sm outfit j with dict_dissolve_25

    voice "SYO_0181"
    sachiko "\"Ah, wait, Foomin. Here, take this.\"" id a04_cou2_08_830e542b

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_1082"
    fumi "\"What's—\"" id a04_cou2_08_f1c49ff1

    "Fumi looked at the package thrust into her hands in confusion for a moment, but quickly realized what it was."

    show fumi:
        "fumi 1 sm school c" with Dissolve(0.25)
        ShakeYes

    voice "FUM_1083"
    fumi "\"Alright! Got it.\"" id a04_cou2_08_ba61dde3

    show fumi 1 sm school c:
        xoffset 0 yoffset 0
    with None

    "And she made to run out of the dorm after Rin."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "SYO_0182"
    sachiko "\"Oh, Foomin, I think you should give Rin a head start.\"" id a04_cou2_08_2911885f

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_1084"
    fumi "\"Umm... yes, you're right.\"" id a04_cou2_08_7b9cd131

    show sachiko 1 sm outfit g with dict_dissolve_25

    voice "SYO_0183"
    sachiko "\"Here, I'll go get an umbrella.\"" id a04_cou2_08_d275eab1

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_1085"
    fumi "\"Thank you.\"" id a04_cou2_08_ac28603a

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
