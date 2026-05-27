label a02_comn_05:

    scene bg05ba with Dissolve(0.5)
    pause 1.5

    play music bgm01

    play sound se001b

    show sachiko 1 lg outfit f at pos_l with dict_dissolve_25
    show hina at pos_r:
        "hina 1 lg school_scarf d flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772
    pause 0.5

    show hina 1 lg school_scarf d:
        alpha 1.0 xcenter 772
    with None

    voice "SYO_0048"
    sachiko "\"Welcome hooome!\"" id a02_comn_05_3960cacb

    show hina 1 lg school_scarf h with dict_dissolve_25

    voice "HIN_0370"
    hina "\"...Hi.\"" id a02_comn_05_7dee0952

    "What a contrast these two make."

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "SYO_0049"
    sachiko "\"Rin and Foomin got home a little bit ago. Did you have your class rep stuff again?\"" id a02_comn_05_0da3f7f1

    show hina 2 lg school_scarf d with dict_dissolve_25

    voice "HIN_0371"
    hina "\"Mhm.\"" id a02_comn_05_b9e0fd61

    show sachiko 1 lg outfit c with dict_dissolve_25

    voice "SYO_0050"
    sachiko "\"Huh? You seem kinda down, Hinacchi.\"" id a02_comn_05_33ed308f

    show hina 2 lg school_scarf h with dict_dissolve_25

    voice "HIN_0372"
    hina "\"{size=15}...Exams.{/size}\"" id a02_comn_05_624bd356

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "SYO_0051"
    sachiko "\"Huh? What was that?\"" id a02_comn_05_50ae5180

    show hina:
        "hina 2 lg school_scarf j" with Dissolve(0.25)
        ShakeJump
        ShakeJump
        ShakeJump

    voice "HIN_0373"
    hina "\"Exams!\"" id a02_comn_05_2a1fcdad

    show hina 2 lg school_scarf j:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "SYO_0052"
    if persistent.dpatch:
        sachiko "\"Ahh, I getcha. No wonder the whole school's so tense lately.\"" id a02_comn_05_373d5f13
    else:
        sachiko "\"Ahh, I getcha. No wonder the whole academy's so tense lately.\"" id a02_comn_05_ae7fadf6

    show hina 2 lg school_scarf h with dict_dissolve_25

    voice "HIN_0374"
    hina "\"We just had midterms, why is this happening again...\"" id a02_comn_05_2778c11b

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "SYO_0053"
    sachiko "\"Well, when you're a student, tests are basically your job.\"" id a02_comn_05_7f314b8d

    show hina 1 lg school_scarf h with Dissolve(0.25)
    show hina:
        ShakeTameiki

    voice "HIN_0375"
    hina "\"I'm starting to feel like life is only what happens in between tests.\"" id a02_comn_05_c71a7bb5

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 lg outfit d with dict_dissolve_25

    voice "SYO_0054"
    sachiko "\"Hey now, I think you're a bit young to be talking about life already, Hinacchi.\"" id a02_comn_05_5b09c4e6

    show hina 1 lg school_scarf j with dict_dissolve_25

    voice "HIN_0376"
    hina "\"Life... is suffering.\"" id a02_comn_05_8ddaf8d1

    show sachiko 1 lg outfit e with dict_dissolve_25

    voice "SYO_0055"
    sachiko "\"Oh, you poor thing! I'll help you forget about it all!\"" id a02_comn_05_853cc124

    play sound se118b

    show sachiko behind hina:
        "sachiko 1 lg outfit e" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 512

    show hina:
        "hina 1 lg school_scarf l" with Dissolve(0.25)
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "HIN_0377"
    hina "\"Gyaa! Get off me!\"" id a02_comn_05_899c3e67

    show sachiko 1 lg outfit e:
        xcenter 512
    show hina 1 lg school_scarf l:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko 1 lg outfit g" with Dissolve(0.25)
        ShakeNo

    voice "SYO_0056"
    sachiko "\"Hey, repeat the year if you have to. I wouldn't mind having you around forever, Hinacchi.\"" id a02_comn_05_2dcfff1c

    show sachiko 1 lg outfit g:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg school_scarf d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0378"
    hina "\"L-Lemme go! I'm graduating right now!\"" id a02_comn_05_b208359b

    scene black with bg_effect_05
    pause 0.5

    show bg05ba with bg_effect_05
    pause 0.5

    show sachiko 1 lg outfit g at pos_l
    show hina 1 lg school_scarf d at pos_r
    with Dissolve(0.25)

    show hina:
        ShakeTameiki
        ShakeTameiki
        ShakeTameiki

    voice "HIN_0379"
    hina "\"Haah, haah, haah...\"" id a02_comn_05_df396f96

    show hina:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "SYO_0057"
    sachiko "\"Oh, that's right. Your birthday's coming up, isn't it?\"" id a02_comn_05_744b2f78

    show hina 2 lg school_scarf e with dict_dissolve_25

    voice "HIN_0380"
    hina "\"...Y-Yeah?\"" id a02_comn_05_7d4bd5ba

    show sachiko 1 lg outfit g with dict_dissolve_25

    voice "SYO_0058"
    sachiko "\"Let me give you a present, too.\"" id a02_comn_05_d11304dd

    show hina 2 lg school_scarf f with dict_dissolve_25

    voice "HIN_0381"
    hina "\"Like what?\"" id a02_comn_05_c87da3a1

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "SYO_0059"
    sachiko "\"I'd love for it to be something you'll carry in your heart forever...\"" id a02_comn_05_d7c12f16

    show hina 1 lg school_scarf d with dict_dissolve_25

    voice "HIN_0382"
    hina "\"Trauma...?\"" id a02_comn_05_ad634ecf

    show sachiko 1 lg outfit c with dict_dissolve_25

    voice "SYO_0060"
    sachiko "\"Why's that?\"" id a02_comn_05_8e054452

    show sachiko 1 lg outfit e with dict_dissolve_25

    voice "SYO_0061"
    sachiko "\"I'll paint you a portr—\"" id a02_comn_05_794afb5c

    show hina:
        "hina 1 lg school_scarf f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0383"
    hina "\"No thanks!\"" id a02_comn_05_9ee4c2f7

    show hina 1 lg school_scarf f:
        xoffset 0 yoffset 0
    with None
    show sachiko 1 lg outfit j with dict_dissolve_25

    voice "SYO_0062"
    sachiko "\"You don't have to be so vehement about it. What's wrong with posing for a painting?\"" id a02_comn_05_5ac0b35b

    show hina 1 lg school_scarf j with dict_dissolve_25

    voice "HIN_0384"
    hina "\"In the nude, right?\"" id a02_comn_05_6b02cc6f

    show sachiko:
        "sachiko 1 lg outfit e" with Dissolve(0.25)
        ShakeYes

    voice "SYO_0063"
    sachiko "\"Well, of course! You gotta capture the sight of a girl when she's at her most beautiful for the canvas!\"" id a02_comn_05_67ae4b31

    show sachiko 1 lg outfit e:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg school_scarf d with dict_dissolve_25

    voice "HIN_0385"
    hina "\"......\"" id a02_comn_05_59c0132d

    show hina:
        "hina 2 lg school_scarf d flat"
        alpha 1.0 xcenter 772
        easeout 0.5 alpha 0.0 xcenter 672
    pause 0.5

    hide hina with None
    show sachiko:
        "sachiko 1 lg outfit h" with Dissolve(0.25)
        ShakeSide

    voice "SYO_0064"
    sachiko "\"Wah, wait, Hinacchi!\"" id a02_comn_05_19c89652

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
