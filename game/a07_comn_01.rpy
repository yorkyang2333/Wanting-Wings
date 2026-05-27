label a07_comn_01:

    pause 0.5

    scene expression "gui/kimikara/mainmenu_ground1.webp"
    with Dissolve(0.5)
    pause 1.5

    show expression "gui/kimikara/title1.webp" as title
    with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    "—Third term. The morning of the first day."

    scene bg02ag with Dissolve(0.5)
    pause 1.5

    play music bgm01

    show hina 1 lg school_scarf f
    with Dissolve(0.25)

    show hina:
        ShakeYes

    voice "2HI_0038"
    hina "\"Get up, Rin!\"" id a07_comn_01_61c78c14

    show hina:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side school k"

    voice "2RI_0034"
    rin "\"Four more hours...\"" id a07_comn_01_9be24a25

    "It's getting longer."

    voice "2HI_0039"
    if persistent.dpatch:
        hina "\"It's the first day of school! I'm not letting you be late on the first day!\"" id a07_comn_01_3fd19e85
    else:
        hina "\"It's the first day of classes! I'm not letting you be late on the first day!\"" id a07_comn_01_e1839a59

    show hina:
        ShakeYes

    "Hina reached under the covers and grabbed the grumbling Rin's wrist."

    show hina 1 lg school_scarf j:
        xoffset 0 yoffset 0
    with dict_dissolve_50

    voice "2HI_0040"
    hina "\"I'll wake you up with a {i}thunk{/i} again.\"" id a07_comn_01_be5c36ff

    $ side_image = "rin 1 side school j"

    voice "2RI_0035"
    rin "\"Wait!\"" id a07_comn_01_755267b6

    hide hina with Dissolve(0.25)

    show rin:
        "rin 2 sm school b flat"
        alpha 0.0 xcenter 612
        easein 1.0 alpha 1.0 xcenter 512

    "Rin reluctantly rose and emerged from the bed."

    show rin 2 sm school b:
        alpha 1.0 xcenter 512
    with None

    $ side_image = "hina 1 side school_scarf e"

    voice "2HI_0041"
    hina "\"Okay!\"" id a07_comn_01_678990f4

    $ side_image = "fumi 2 side school_scarf c"

    if route2 == 3:
        voice "2FU_0021"
        fumi "\"Are you up, Rin?\"" id a07_comn_01_f2f6420d
    else:
        voice "2FU_0022"
        fumi "\"Are you up, Ogata?\"" id a07_comn_01_4082c4a3

    "Fumi came over after placing the mugs on the drying rack."

    $ side_image = "fumi 2 side school_scarf i"

    voice "2FU_0023"
    fumi "\"Okay, are you ready?\"" id a07_comn_01_c80972ea

    show rin 2 sm school c with dict_dissolve_25

    voice "2RI_0036"
    rin "\"Uh hunh...\"" id a07_comn_01_79dfc1c6

    hide rin with Dissolve(0.25)

    pause 0.5

    show rin 2 lg school a with dict_dissolve_25
    show fumi 2 lg school c at pos_l2
    with Dissolve(0.25)

    pause 0.5

    show fumi:
        ShakeYes

    voice "2FU_0024"
    fumi "\"Your lunch.\"" id a07_comn_01_e6067220

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0037"
    rin "\"Yep.\"" id a07_comn_01_bd8e15cb

    show fumi:
        ShakeYes

    voice "2FU_0025"
    fumi "\"Your commuter pass.\"" id a07_comn_01_c476a6f3

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0038"
    rin "\"Yep.\"" id a07_comn_01_30fc18cb

    show fumi:
        ShakeYes
        0.5
        ShakeYes

    voice "2FU_0026"
    fumi "\"Your wallet, your handkerchief.\"" id a07_comn_01_7ed88c19

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0039"
    rin "\"Yep, yep.\"" id a07_comn_01_57481cd5

    $ side_image = "hina 2 side school_scarf a"

    voice "2HI_0042"
    hina "\"Your tie... it's okay for once!\"" id a07_comn_01_0798a474

    show fumi:
        ShakeYes

    voice "2FU_0027"
    fumi "\"Last one. Your scarf.\"" id a07_comn_01_9d01db5a

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school c with dict_dissolve_25

    voice "2RI_0040"
    rin "\"Thanks.\"" id a07_comn_01_a5d2cee1

    hide fumi
    with Dissolve(0.25)

    show rin:
        "rin 1 lg school_scarf c" with Dissolve(0.5)
        ShakeYes

    play sound se116a

    "Rin wrapped her scarf around her neck. At this point, at least, she always looks the part of the cool beauty."

    hide rin
    with Dissolve(0.25)

    show rin 1 sm school_scarf b with dict_dissolve_25

    voice "2RI_0041"
    rin "\"Okay—\"" id a07_comn_01_e63bbdc6

    show hina behind rin:
        "hina 1 sm school_scarf j flat"
        alpha 0.0 xcenter 622
        easein 0.25 alpha 1.0 xcenter 722
    pause 0.25

    "Hina grabbed the end of Rin's scarf. She readied for her usual judo throw."

    show hina 1 sm school_scarf j:
        alpha 1.0 xcenter 722
    with None
    show rin 1 sm school_scarf i with dict_dissolve_25

    voice "2RI_0042"
    rin "\"I was gonna say 'let's go'!\"" id a07_comn_01_cfc13edd

    show hina 1 sm school_scarf m with dict_dissolve_25

    voice "2HI_0043"
    hina "\"Oh, were you? I was just going off of your usual behavior.\"" id a07_comn_01_1a6f97fc

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "2RI_0043"
    if persistent.dpatch:
        rin "\"Isn't that a little harsh on the first day of school?\"" id a07_comn_01_c32faa39
    else:
        rin "\"Isn't that a little harsh on the first day of class?\"" id a07_comn_01_4c7bba7b

    show hina 1 sm school_scarf f with dict_dissolve_25

    voice "2HI_0044"
    if persistent.dpatch:
        hina "\"And who was it who slept in until the last minute on the first day of school?!\"" id a07_comn_01_67305437
    else:
        hina "\"And who was it who slept in until the last minute on the first day?!\"" id a07_comn_01_a4e6b759

    show fumi 2 sm school_scarf c at pos_l with dict_dissolve_25

    voice "2FU_0028"
    fumi "\"Alright, let's get going~\"" id a07_comn_01_ea843706

    show hina 1 sm school_scarf b with dict_dissolve_25

    voice "2HI_0045"
    hina "\"Okay—\"" id a07_comn_01_822bc972

    voice "2MI_0001"
    miyako "\"Hwahh...\"" (show_name="???") id a07_comn_01_9017212a

    show rin 1 sm school_scarf e with dict_dissolve_25

    voice "2RI_0044"
    rin "\"Ah...\"" id a07_comn_01_98cbff3b

    show fumi 2 sm school_scarf g with dict_dissolve_25

    voice "2FU_0029"
    fumi "\"Huh...?\"" id a07_comn_01_8058b0b7

    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "2HI_0046"
    hina "\"Aaah!!\"" id a07_comn_01_c7f66da0

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    pause 0.5

    show miyako 2 lg pyjama_hood j with dict_dissolve_75

    voice "2MI_0002"
    miyako "\"Good morning~\"" id a07_comn_01_b60fa2a8

    $ side_image = "side/hina_fumi_rin_school_scarf_sozai01.webp"

    $ voice3("hina","2HI_0047N","rin","2RI_0045","fumi","2FU_0030")
    hina_rin_fumi "\"We forgot~!!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    scene expression "gui/kimikara/mainmenu_ground1.webp"
    show expression "gui/kimikara/title2.webp"
    with Dissolve(0.5)
    pause 1.5



    show chapter07 with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

label a07_comn_01_g:

    if routes_cleared == 1:
        jump a07_comn_01_a
    else:
        jump a07_comn_01_end


label a07_comn_01_a:
    python:
        _last_say_what = ""
        _last_say_who = None
        renpy.choice_for_skipping()

    scene select_back2 with Dissolve(0.5)
    pause 1.5


    menu:
        "■選択肢１枠"((400,297), "menu/btn_select_0401"):
            jump a07_comn_01_g2

label a07_comn_01_g2:

    scene black with Dissolve(0.25)
    pause 1.25

    scene bg09aa with bg_effect_27_750
    pause 2.0

    show sachiko 2 sm outfit g with Dissolve(0.25)

    voice "2SA_0041"
    sachiko "\"Oh, I forgot...\"" id a07_comn_01_g2_9357881d

label a07_comn_01_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
