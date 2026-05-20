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
    hina "\"Get up, Rin!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    $ side_image = "rin 1 side school k"

    voice "2RI_0034"
    rin "\"Four more hours...\""

    "It's getting longer."

    voice "2HI_0039"
    if persistent.dpatch:
        hina "\"It's the first day of school! I'm not letting you be late on the first day!\"" id a07_comn_01_3fd19e85
    else:
        hina "\"It's the first day of classes! I'm not letting you be late on the first day!\""

    show hina:
        ShakeYes

    "Hina reached under the covers and grabbed the grumbling Rin's wrist."

    show hina 1 lg school_scarf j:
        xoffset 0 yoffset 0
    with dict_dissolve_50

    voice "2HI_0040"
    hina "\"I'll wake you up with a {i}thunk{/i} again.\""

    $ side_image = "rin 1 side school j"

    voice "2RI_0035"
    rin "\"Wait!\""

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
    hina "\"Okay!\""

    $ side_image = "fumi 2 side school_scarf c"

    if route2 == 3:
        voice "2FU_0021"
        fumi "\"Are you up, Rin?\""
    else:
        voice "2FU_0022"
        fumi "\"Are you up, Ogata?\""

    "Fumi came over after placing the mugs on the drying rack."

    $ side_image = "fumi 2 side school_scarf i"

    voice "2FU_0023"
    fumi "\"Okay, are you ready?\""

    show rin 2 sm school c with dict_dissolve_25

    voice "2RI_0036"
    rin "\"Uh hunh...\""

    hide rin with Dissolve(0.25)

    pause 0.5

    show rin 2 lg school a with dict_dissolve_25
    show fumi 2 lg school c at pos_l2
    with Dissolve(0.25)

    pause 0.5

    show fumi:
        ShakeYes

    voice "2FU_0024"
    fumi "\"Your lunch.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0037"
    rin "\"Yep.\""

    show fumi:
        ShakeYes

    voice "2FU_0025"
    fumi "\"Your commuter pass.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0038"
    rin "\"Yep.\""

    show fumi:
        ShakeYes
        0.5
        ShakeYes

    voice "2FU_0026"
    fumi "\"Your wallet, your handkerchief.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    voice "2RI_0039"
    rin "\"Yep, yep.\""

    $ side_image = "hina 2 side school_scarf a"

    voice "2HI_0042"
    hina "\"Your tie... it's okay for once!\""

    show fumi:
        ShakeYes

    voice "2FU_0027"
    fumi "\"Last one. Your scarf.\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg school c with dict_dissolve_25

    voice "2RI_0040"
    rin "\"Thanks.\""

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
    rin "\"Okay—\""

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
    rin "\"I was gonna say 'let's go'!\""

    show hina 1 sm school_scarf m with dict_dissolve_25

    voice "2HI_0043"
    hina "\"Oh, were you? I was just going off of your usual behavior.\""

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "2RI_0043"
    if persistent.dpatch:
        rin "\"Isn't that a little harsh on the first day of school?\"" id a07_comn_01_c32faa39
    else:
        rin "\"Isn't that a little harsh on the first day of class?\""

    show hina 1 sm school_scarf f with dict_dissolve_25

    voice "2HI_0044"
    if persistent.dpatch:
        hina "\"And who was it who slept in until the last minute on the first day of school?!\"" id a07_comn_01_67305437
    else:
        hina "\"And who was it who slept in until the last minute on the first day?!\""

    show fumi 2 sm school_scarf c at pos_l with dict_dissolve_25

    voice "2FU_0028"
    fumi "\"Alright, let's get going~\""

    show hina 1 sm school_scarf b with dict_dissolve_25

    voice "2HI_0045"
    hina "\"Okay—\""

    voice "2MI_0001"
    miyako "\"Hwahh...\"" (show_name="???")

    show rin 1 sm school_scarf e with dict_dissolve_25

    voice "2RI_0044"
    rin "\"Ah...\""

    show fumi 2 sm school_scarf g with dict_dissolve_25

    voice "2FU_0029"
    fumi "\"Huh...?\""

    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "2HI_0046"
    hina "\"Aaah!!\""

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    pause 0.5

    show miyako 2 lg pyjama_hood j with dict_dissolve_75

    voice "2MI_0002"
    miyako "\"Good morning~\""

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
    sachiko "\"Oh, I forgot...\""

label a07_comn_01_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
