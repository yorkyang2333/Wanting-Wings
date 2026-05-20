label a09_comn_08:

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    play music bgm01
    play sound se521
    pause 2.0

    show miyako:
        "miyako 2 sm school_sei c flat"
        alpha 0.0 xcenter 552
        easein 0.75 alpha 1.0 xcenter 452
        0.5
        "miyako 1 sm school_a_sei f" with Dissolve(0.25)
    show hina:
        "hina 2 sm school_scarf a flat"
        alpha 0.0 xcenter 732
        easein 0.75 alpha 1.0 xcenter 632
        0.5
        "hina 1 sm school_scarf l" with Dissolve(0.25)
    show rin behind hina, fumi:
        "rin 2 sm school_scarf a flat"
        alpha 0.0 xcenter 876
        easein 0.75 alpha 1.0 xcenter 776
        0.5
        "rin 1 sm school_scarf e" with Dissolve(0.25)
    show fumi:
        "fumi 1 sm school_scarf c flat"
        alpha 0.0 xcenter 1040
        easein 0.75 alpha 1.0 xcenter 940
        0.5
        "fumi 1 sm school_scarf j" with Dissolve(0.25)
        0.25
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2FU_0636"
    fumi "\"We're ba—aaah!\""

    show miyako 1 sm school_a_sei f:
        alpha 1.0 xcenter 452
    show hina 1 sm school_scarf l:
        alpha 1.0 xcenter 632
    show rin 1 sm school_scarf e:
        alpha 1.0 xcenter 776
    show fumi 1 sm school_scarf j:
        alpha 1.0 xcenter 940 xoffset 0 yoffset 0

    "Fumi shrieked as she returned from her shopping trip."

    hide rin
    hide fumi
    hide hina
    hide miyako
    show namahage lg
    with Dissolve(0.25)

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0589"
    namahage_sachiko "\"Any naughty kids around?!\""

    camera
    with None

    $ side_image = "rin 1 side school_scarf e"

    voice "2RI_0785"
    rin "\"A namahage...?\""

    camera:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0590"
    namahage_sachiko "\"Any naughty girls with naughty bodies around?!\""

    camera
    with None

    play sound se_can

    "Clang!"

    show namahage:
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0591"
    namahage_sachiko "\"Gyaaa! H-Hard! What did you throw at me?!\""

    show namahage:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side school_scarf j"

    voice "2HI_0776"
    hina "\"Canned sardines.\""

    voice "2SA_0592"
    namahage_sachiko "\"Hey, canned stuff is a bit much, no?! At least make it beans!\""

    $ side_image = "hina 1 side school_scarf c"

    voice "2HI_0777"
    hina "\"They were on sale, so I've got plenty more~\""

    "Hina wound up with another can."

    hide namahage with Dissolve(0.25)

    show namahage lg:
        zoom 0.71 xcenter 521 ycenter 777
    with dict_dissolve_25

    voice "2SA_0593"
    sachiko "\"Waaaah!\""

    $ side_image = "rin 1 side school_scarf g"

    voice "2RI_0786"
    rin "\"Thus, the namahage becomes the crybaby.\""

    $ side_image = "hina 1 side school_scarf f"

    voice "2HI_0778"
    hina "\"Everything about this is wrong!\""

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg05ba with bg_effect_05
    pause 0.5

    show miyako 2 sm school_sei a:
        xcenter 452
    show hina 1 sm school_scarf e:
        xcenter 632
    show rin 1 sm school_scarf i behind hina, fumi:
        xcenter 776
    show fumi 1 sm school_scarf k:
        xcenter 940
    with dict_dissolve_25

    voice "2MI_0705"
    miyako "\"This is very well-made. Where did you get it?\""

    "Miyako looked over the namahage costume, impressed."

    show sachiko 1 sm outfit c:
        xcenter 152
    with dict_dissolve_25

    voice "2SA_0594"
    sachiko "\"...Akita.\""

    show rin:
        "rin 1 sm school_scarf j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0787"
    rin "\"That's pretty authentic! Why would you go that far?!\""

    show rin 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 sm outfit b with dict_dissolve_25

    voice "2SA_0595"
    sachiko "\"I thought it'd surprise you...\""

    show fumi:
        "fumi 1 sm school_scarf j" with Dissolve(0.25)
        ShakeJump

    voice "2FU_0637"
    fumi "\"It did surprise me!\""

    show fumi 1 sm school_scarf j:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko 1 sm outfit g" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0596"
    sachiko "\"Yay!\""

    show sachiko 1 sm outfit g:
        xoffset 0 yoffset 0
    with None

    "Sachiko struck a victory pose."

    show hina 1 sm school_scarf j with dict_dissolve_25

    voice "2HI_0779"
    hina "\"But why was there a namahage at home waiting for us in the first place?\""

    "Typically, namahage were supposed to visit homes, not wait inside them."

    show sachiko 1 sm outfit a with dict_dissolve_25

    voice "2SA_0597"
    sachiko "\"'Cause it's setsubun.\""

    show fumi 1 sm school_scarf e with dict_dissolve_25

    voice "2FU_0638"
    fumi "\"Wait, is a namahage a demon?\""

    show hina 1 sm school_scarf d with dict_dissolve_25

    voice "2HI_0780"
    hina "\"Then it's even more wrong! The demon's not supposed to be inside!\""

    "I'm pretty sure namahage are supposed to be visiting gods, not demons, but whatever."

    show miyako 1 sm school_a_sei b with dict_dissolve_25

    voice "2MI_0706"
    miyako "\"Ah, here we go.\""

    "Miyako pulled a cardboard demon mask out of their shopping bag. It was something the store had been giving away for free."

    show rin 1 sm school_scarf a with dict_dissolve_25

    voice "2RI_0788"
    rin "\"This is definitely good enough, isn't it?\""

    show sachiko:
        "sachiko 1 sm outfit e" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0598"
    sachiko "\"Let's celebrate setsubun! Any bean-throwing kids around?! Any makizushi-eating kids around?!\""

    show sachiko 1 sm outfit e:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm school_scarf j with dict_dissolve_25

    voice "2HI_0781"
    hina "\"What is wrong with her...?\""

    show miyako 1 sm school_a_sei d with dict_dissolve_25

    voice "2MI_0707"
    miyako "\"Yay! Setsubun!\""

    show rin 1 sm school_scarf g with dict_dissolve_25

    voice "2RI_0789"
    rin "\"We got another one over here...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
