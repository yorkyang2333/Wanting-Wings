label a04_cou2_06:

    play sound se030a

    scene bg04ba with Dissolve(0.5)
    pause 1.5

    play music bgm05

    play sound2 se071a_120 fadein 0.5

    pause 0.5

    show rin 2 lg school_scarf a at pos_l2 with Dissolve(0.25)

    $ side_image = "hina 2 side school f"

    voice "HIN_1423"
    hina "\"Hey, Rin, where'd you go last—\"" id a04_cou2_06_fb6bbcc9

    stop sound2 fadeout 1.0

    show fumi:
        "fumi 1 lg school_scarf b flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    voice "FUM_1067"
    fumi "\"Ogata.\"" id a04_cou2_06_6e97152d

    show fumi 1 lg school_scarf b:
        alpha 1.0 xcenter 512
    with None

    "Fumi had been just a moment quicker in addressing Rin."

    show rin 1 lg school_scarf c with dict_dissolve_25

    voice "RIN_1184"
    rin "\"Ah, you ready?\"" id a04_cou2_06_393ca98a

    show fumi 1 lg school_scarf c with dict_dissolve_25

    voice "FUM_1068"
    fumi "\"Yep, all good.\"" id a04_cou2_06_2c85ed51

    $ side_image = "hina 2 side school h"

    voice "HIN_1424"
    hina "\"Rin?\"" id a04_cou2_06_b3795a28

    show rin 1 lg school_scarf a with dict_dissolve_25

    voice "RIN_1185"
    rin "\"Sorry Hina, Asou and I have somewhere to go today, so could you go home without us?\"" id a04_cou2_06_05fd692a

    $ side_image = "hina 1 side school d"

    voice "HIN_1425"
    hina "\"I-I'll come with you!\"" id a04_cou2_06_addfe04d

    show rin 1 lg school_scarf h with dict_dissolve_25

    voice "RIN_1186"
    rin "\"You will not. You're not done with that English assignment yet, are you?\"" id a04_cou2_06_dae9f097

    $ side_image = "hina 2 side school h"

    voice "HIN_1426"
    hina "\"But...\"" id a04_cou2_06_f41bbeda

    show fumi 1 lg school_scarf a with dict_dissolve_25

    voice "FUM_1069"
    fumi "\"I'm sorry, Natsume. We can help you when we get back if you need it.\"" id a04_cou2_06_e7ed5a14

    show rin 1 lg school_scarf c with dict_dissolve_25

    voice "RIN_1187"
    rin "\"See you.\"" id a04_cou2_06_46a7732c

    show rin:
        "rin 1 lg school_scarf c flat"
        alpha 1.0 xcenter 172
        easeout 0.5 alpha 0.0 xcenter 272
    show fumi:
        "fumi 1 lg school_scarf a flat"
        alpha 1.0 xcenter 512
        easeout 0.5 alpha 0.0 xcenter 612

    $ side_image = "hina 1 side school d"

    voice "HIN_1427"
    hina "\"Ah... Rin...\"" id a04_cou2_06_1b2e74a7

    hide rin
    hide fumi
    with None

    play sound se000f

    "........."

    show hina 2 lg school h with dict_dissolve_25

    voice "HIN_1428"
    hina "\"...What's with her?\"" id a04_cou2_06_6c1acd69

    scene black with Dissolve(0.5)
    pause 2.0

    scene bg05ba with Dissolve(0.25)
    pause 0.75

    play sound se001b

    show hina:
        "hina 2 lg school_scarf h flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512
    pause 0.5

    show hina 2 lg school_scarf h:
        alpha 1.0 xcenter 512
    with None

    voice "HIN_1429"
    hina "\"Haahh...\"" id a04_cou2_06_3efdcc74


    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0167"
    sachiko "\"Huh? All alone today?\"" id a04_cou2_06_565d5008

    "Sachiko looked up from a bundle of old newspapers by the front door."

    show hina 1 lg school_scarf h with dict_dissolve_25

    voice "HIN_1430"
    hina "\"They said they were going somewhere together so I should go home by myself...\"" id a04_cou2_06_a5185583

    $ side_image = "sachiko 1 side outfit a"

    voice "SYO_0168"
    sachiko "\"Huh... Oh yeah?\"" id a04_cou2_06_5747213e

    "Sachiko nodded knowingly and returned to her work."

    show hina 2 lg school_scarf h with Dissolve(0.25)
    show hina:
        xcenter 512
        easein 1.0 xcenter 252

    voice "HIN_1431"
    hina "\"See you...\"" id a04_cou2_06_4925a3b8

    "Hina trudged off to her room."

    $ side_image = "sachiko 1 side outfit i"

    voice "SYO_0169"
    sachiko "\"Oh yeah, Hinacchi. When Rin gets back, tell her I'll see her again tonight, will you?\"" id a04_cou2_06_d9b1a471

    "Sachiko said, head still down."

    show hina 1 lg school_scarf k with dict_dissolve_25

    voice "HIN_1432"
    hina "\"Huh?\"" id a04_cou2_06_53317c2c

    "Hina froze."

    show hina:
        "hina 2 lg school_scarf h flat" with Dissolve(0.25)
        alpha 1.0 xcenter 252
        2.0
        easeout 0.5 alpha 0.0 xcenter 152

    $ side_image = "sachiko 1 side outfit f"

    voice "SYO_0170"
    sachiko "\"Man, Rin's beautiful, ain't she? She's got a great figure... huh?\"" id a04_cou2_06_35d39692

    hide hina with None

    "When she looked up, Hina was already gone."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
