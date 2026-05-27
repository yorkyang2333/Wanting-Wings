label a01_comn_01:

    pause 0.5

    scene expression "gui/kimihane/mainmenu_ground1.webp"
    with Dissolve(0.5)
    pause 1.5

    show expression "gui/kimihane/title1.webp" as title:
        yoffset 50
    with Dissolve(1.5)
    pause 2.0

    hide title with Dissolve(1.5)

    pause 0.5



    show chapter01 with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    scene bg02aa with Dissolve(1.0)
    pause 2.0

    play music bgm01

    show hina 1 lg school_scarf f with Dissolve(0.25)
    show hina at ShakeYes

    voice "HIN_0009"
    hina "\"Get up, Rin!\"" (show_name="Short-haired Girl") id a01_comn_01_acfbf8bf

    "The girl was small, but her voice carried."

    "Her obvious displeasure was directed at another girl who was dozing off on a bed, her back against the wall."

    show hina at ShakeJump

    voice "HIN_0010"
    hina "\"Who goes back to sleep after putting on her uniform?! And that's my bed!\"" (show_name="Short-haired Girl") id a01_comn_01_be6c6ea6

    $ side_image = "rin 1 side school k"

    voice "RIN_0011"
    rin "\"Nnuhh?\"" id a01_comn_01_f82e1c7e

    play sound se120a

    "The girl on the bed—Rin—turned against the wall with no regard for the wrinkling of her skirt."

    $ side_image = "rin 1 side school k"

    voice "RIN_0012"
    rin "\"Just three more hours.\"" id a01_comn_01_19b2dbee

    show hina 1 lg school_scarf j with dict_dissolve_25

    voice "HIN_0011"
    hina "\"It'll be lunch by then! This is 'cause you stay up so late reading books! Come on, just get out of bed already!\"" (show_name="Short-haired Girl") id a01_comn_01_e6aed296

    "The short-haired girl reached into the bed and grabbed the wrists of the grumbling Rin."


    show hina:
        "hina 1 lg school_scarf e" with Dissolve(0.25)
        ShakeYes
        ShakeJump

    voice "HIN_0012"
    hina "\"Come on!\"" (show_name="Short-haired Girl") id a01_comn_01_0e93da58


    show hina 1 lg school_scarf e:
        xoffset 0 yoffset 0
    with None

    "She pulled hard, trying to drag Rin from the bed—however..."

    play sound se104a

    camera:
        function LayerShake(20,20,0.25)



    $ persistent.layer_shaken = False

    $ side_image = "rin 1 side school j"

    voice "RIN_0013"
    rin "\"Ugh?!\"" id a01_comn_01_87f97ef0


    camera
    with None

    "With both of her hands captive, Rin ended up hitting her forehead against the bed's frame."

    show hina 1 lg school_scarf l with dict_dissolve_25

    voice "HIN_0013"
    hina "\"Ah, sorr—\"" (show_name="Short-haired Girl") id a01_comn_01_adf7e816

    hide hina with Dissolve(0.05)
    pause 0.2

    show hina 1 lg school_scarf l at pos_r with dict_dissolve_25



    show fumi:
        "fumi 1 lg school e flat"
        alpha 0.0 xcenter 152
        easein 0.5 alpha 1.0 xcenter 252

    voice "FUM_0011"
    fumi "\"A-Are you okay? That was kind of a loud noise.\"" (show_name="Pigtailed Girl") id a01_comn_01_b739debe


    show fumi 1 lg school e:
        alpha 1.0 xcenter 252
    with None

    "Another girl who'd been placing mugs in the draining basket next to the sink hurried over."

    $ side_image = "rin 1 side school h"

    voice "RIN_0014"
    rin "\"Uhh... who are you? I think the impact jumbled my memories...\"" id a01_comn_01_721a39ac

    show fumi 1 lg school j with Dissolve(0.25)
    show fumi:
        ShakeYes2

    voice "FUM_0012"
    fumi "\"Fumi! I'm Fumi! Your roommate, Fumi Asou!\"" id a01_comn_01_78cbea05

    show fumi 1 lg school j:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side school k"

    voice "RIN_0015"
    rin "\"Unh... my head hurts... I'm... taking the day off...\"" id a01_comn_01_b6e1f372

    show hina 1 lg school_scarf f with Dissolve(0.25)
    show hina at ShakeJump

    voice "HIN_0014"
    hina "\"You are not!\"" (show_name="Short-haired Girl") id a01_comn_01_771cb1cd

    show hina 1 lg school_scarf f:
        xoffset 0 yoffset 0
    with None

    play sound se207a

    show hina at ShakeYes

    camera:
        function LayerShake(25,25,0.3)
    $ persistent.layer_shaken = False

    $ side_image = "rin 1 side school j"

    voice "RIN_0016"
    rin "\"Aaah!\"" id a01_comn_01_999c9547

    camera
    with None

    show hina:
        xoffset 0 yoffset 0
    with None

    "Rin tried to lie down again, but this time, the short-haired girl's forehead collided with hers."

    $ side_image = "rin 1 side school i"

    voice "RIN_0017"
    rin "\"That hurt, Hina! What are you doing?!\"" id a01_comn_01_3ce2e9e3

    show hina 2 lg school_scarf d with dict_dissolve_25

    voice "HIN_0015"
    hina "\"Are you awake now?\"" id a01_comn_01_879503ba

    $ side_image = "rin 1 side school i"

    voice "RIN_0018"
    rin "\"I don't want such a violent wake-up call. I request a sweet wake-up kiss on the forehead from Asou.\"" id a01_comn_01_b3be3a7f

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0013"
    fumi "\"Uhh...\"" id a01_comn_01_88ad1713

    show hina 1 lg school_scarf f with dict_dissolve_25

    voice "HIN_0016"
    hina "\"Enough outta you! Get up!\"" id a01_comn_01_5248fdce

    $ side_image = "rin 1 side school i"

    voice "RIN_0019"
    rin "\"U-Ungh...\"" id a01_comn_01_aec37dc4

    play sound se116a

    hide hina
    hide fumi
    with Dissolve(0.25)

    show fumi 1 sm school d at pos_l
    show hina 1 sm school_scarf e at pos_r
    with dict_dissolve_25

    show rin:
        "rin 1 sm school i flat"
        alpha 0.0 xcenter 612
        easein 1.0 alpha 1.0 xcenter 512

    "Rin reluctantly stood from the bed. Upright, she was clearly tall and slim."

    show rin 1 sm school i:
        alpha 1.0 xcenter 512
    with None

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0014"
    fumi "\"Umm, we're really about to be late here.\"" id a01_comn_01_efe1aa67

    "Fumi pointed at the clock, and the other two focused on it."

    show hina 1 sm school_scarf l with Dissolve(0.25)
    show hina:
        ShakeJump
        ShakeJump

    voice "HIN_0017"
    hina "\"Aaah! The bus is gonna be here any minute!\"" id a01_comn_01_b4b9387b

    show hina:
        xoffset 0 yoffset 0
    with None

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0015"
    fumi "\"Okay, Ogata, are you ready?\"" id a01_comn_01_18754ef9

    "Fumi handed Rin her bag and stood prepared."

    hide hina
    hide fumi
    hide rin
    with Dissolve(0.25)

    show rin 2 lg school a
    show fumi 2 lg school c at pos_l2
    with Dissolve(0.25)

    voice "RIN_0020"
    rin "\"Ah, yeah.\"" id a01_comn_01_34e3f738

    show fumi at ShakeYes

    voice "FUM_0016"
    fumi "\"Here's your lunch.\"" id a01_comn_01_6172261e

    voice "RIN_0021"
    rin "\"Yep.\"" id a01_comn_01_7fa2c13d

    show fumi at ShakeYes

    voice "FUM_0017"
    fumi "\"And your commuter pass.\"" id a01_comn_01_d1002389

    voice "RIN_0022"
    rin "\"Yep.\"" id a01_comn_01_084f40f8

    show fumi:
        ShakeYes
        0.5
        ShakeYes

    voice "FUM_0018"
    fumi "\"Your wallet and your handkerchief.\"" id a01_comn_01_deb60940

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "RIN_0023"
    rin "\"Yep. Yep.\"" id a01_comn_01_5609cb6f

    "Fumi rapidly handed over the items she had ready."

    hide fumi with Dissolve(0.05)
    pause 0.25

    show rin 1 lg school a
    show hina 2 lg school_scarf f at pos_r2
    with Dissolve(0.25)

    voice "HIN_0018"
    hina "\"Here, your tie's crooked.\"" id a01_comn_01_96391116

    show rin at ShakeUji

    voice "RIN_0024"
    rin "\"Nnh~\"" id a01_comn_01_6d5051cf

    show hina 2 lg school_scarf d with Dissolve(0.25)
    show hina:
        ShakeJump
        0.5
        ShakeJump

    voice "HIN_0019"
    hina "\"Hup... hup!\"" id a01_comn_01_4df047b7

    show hina:
        xoffset 0 yoffset 0
    with None

    "Their height difference was so brutal that Hina had to jump to try to fix Rin's tie."

    show hina 1 lg school_scarf f with Dissolve(0.25)

    voice "HIN_0020"
    hina "\"Bend down!\"" id a01_comn_01_8c433c56

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0025"
    rin "\"Fine...\"" id a01_comn_01_43c85328

    show rin:
        yoffset 0
        easeout 1.0 yoffset 100

    "Rin bent down like it was a terrible inconvenience."

    show hina 1 lg school_scarf j with dict_dissolve_25

    voice "HIN_0021"
    hina "\"Tch, what a pain.\"" id a01_comn_01_7a6602d9

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show rin 2 lg school a
    show fumi 2 lg school c at pos_l2:
        0.25
        ShakeYes
    with Dissolve(0.25)

    voice "FUM_0019"
    fumi "\"Last one! Your scarf.\"" id a01_comn_01_e934f51c

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school c with dict_dissolve_25

    voice "RIN_0026"
    rin "\"Yep. Thanks as always.\"" id a01_comn_01_25cff908

    hide fumi with Dissolve(0.25)

    show rin at ShakeYes

    play sound se116a

    show rin 1 lg school_scarf c with Dissolve(0.5)

    "She took the scarf and wrapped it around her neck."

    show rin 1 sm school_scarf b with Dissolve(0.25)

    show rin:
        "rin 1 sm school_scarf b flat"
        alpha 1.0 xcenter 512
        1.0
        easeout 1.0 alpha 0.0 xcenter 612

    voice "RIN_0027"
    rin "\"Well—\"" id a01_comn_01_c2d1a1f2


    hide rin with None

    show hina 1 sm school_scarf j at pos_r2:
        "hina 1 sm school_scarf j flat"
        alpha 0.0 xcenter 752
        easeout 0.25 alpha 1.0 xcenter 852
        ShakeJump

    voice "HIN_0022"
    hina "\"Oh no you don't!\"" id a01_comn_01_572f5756

    show hina 1 sm school_scarf j at pos_r2:
        alpha 1.0 xcenter 852 xoffset 0 yoffset 0
    with None

    play sound se118b

    "Rin was headed back to bed, but Hina grabbed the end of her scarf and pulled it over her own shoulder like she was about to do a judo throw."

    show hina 1 sm school_scarf j at pos_r2:
        xcenter 852
        easeout 0.25 xcenter 652



    show rin 1 sm school_scarf j behind hina:
        "rin 1 sm school_scarf j flat"
        alpha 0.0 xcenter 1012
        0.25
        parallel:
            linear 0.25 alpha 1.0
        parallel:
            easeout 0.25 xcenter 912

    voice "RIN_0028"
    rin "\"Gh—\"" id a01_comn_01_d1355203


    show hina:
        xcenter 652
    show rin:
        alpha 1.0 xcenter 912
    with None

    show hina:
        "hina 1 sm school_scarf f" with Dissolve(0.25)
        easeout 0.25 xcenter 552

    show rin:
        xcenter 912
        0.25
        easeout 0.25 xcenter 812

    voice "HIN_0023"
    hina "\"We don't have time to mess around anymore!\"" id a01_comn_01_d5c6d448

    show rin 1 sm school_scarf j:
        alpha 1.0 xcenter 812
    show hina 1 sm school_scarf f:
        alpha 1.0 xcenter 552
    with None

    show fumi 1 sm school b at pos_l with Dissolve(0.25)

    voice "FUM_0020"
    fumi "\"Alright, let's go~\"" id a01_comn_01_c211ded2

    show hina 1 sm school_scarf c with dict_dissolve_25

    voice "HIN_0024"
    hina "\"Out the door!\"" id a01_comn_01_b39e4449

    show rin at ShakeSide:
        0.25
        0.3
        function LayerShake(20,20,0.25)
    $ persistent.layer_shaken = False

    voice "RIN_0029"
    rin "\"Y-You're... strangling... me~\"" id a01_comn_01_e816c55d

    stop music fadeout 1.0
    stop sound fadeout 1.0

    scene black
    with Dissolve(0.5)

    pause 1.5

    jump a01_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
