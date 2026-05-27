label a09_cou1_02:

    scene bg01ag with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Just before noon on Sunday."

    "Rin was lounging around in the living room."

    show hina:
        "hina z4 2 lg school a flat"
        alpha 0.0 xcenter 612
        easein 0.5 alpha 1.0 xcenter 512

    voice "2HI_0854"
    hina "\"Okay, I'll be back.\"" id a09_cou1_02_a3490575

    show hina z4 2 lg school a:
        alpha 1.0 xcenter 512
    with None

    "Hina came in from the bedroom wearing her uniform."

    $ side_image = "rin 1 side pyjama glasses e"

    voice "2RI_0845"
    rin "\"Huh? Were you subbing today?\"" id a09_cou1_02_a7b1c0a8

    "Rin rolled over and looked up at her."

    voice "2HI_0855"
    hina "\"Yeah, softball and basketball today.\"" id a09_cou1_02_94c10230

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_0846"
    rin "\"Ugh, a doubleheader?! You really do have too much energy.\"" id a09_cou1_02_19dd2675

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_0856"
    hina "\"Well, the softball team asked me first, but there's just enough time before the basketball game that I can make that, too.\"" id a09_cou1_02_6e2ee50d

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_0847"
    rin "\"Where the heck does all the energy come from in that little body of yours...? Huh, are you nuclear-powered, Hina?\"" id a09_cou1_02_d0bf9cb5

    show hina z4 1 lg school e with dict_dissolve_25

    voice "2HI_0857"
    hina "\"I'm food-powered!\"" id a09_cou1_02_c3e0d624

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0848"
    rin "\"Come to think of it, do they pay you for your sub work?\"" id a09_cou1_02_a6d41305

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_0858"
    hina "\"Based on performance.\"" id a09_cou1_02_95d01935

    $ side_image = "rin 1 side pyjama glasses f"

    voice "2RI_0849"
    rin "\"D'you need an agent? I know an Ogata who's good.\"" id a09_cou1_02_84344912

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_0859"
    hina "\"Nope. Anyway, Fumi made you some lunch in the fridge. Go ahead and eat it if you get hungry.\"" id a09_cou1_02_ba004780

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0850"
    rin "\"Uh huh.\"" id a09_cou1_02_10234291

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_0860"
    hina "\"You just have to heat it up in the microwave. You know how?\"" id a09_cou1_02_c6b40b0b

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0851"
    rin "\"Of course I know how. How long d'you think I've been a latchkey kid?\"" id a09_cou1_02_f5f548dc

    show hina z4 1 lg school p with dict_dissolve_25

    voice "2HI_0861"
    hina "\"Right, right. Tell Miyako, too.\"" id a09_cou1_02_e5a944b5

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_0852"
    rin "\"Mhm~\"" id a09_cou1_02_12e00866

    show hina:
        "hina z4 1 lg school a" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0862"
    hina "\"Here we go...\"" id a09_cou1_02_16b54170

    show hina z4 1 lg school a:
        xoffset 0 yoffset 0
    with None

    "Hina hefted up a bag with her uniforms and equipment in it."

    $ side_image = "rin 2 side pyjama glasses a"

    voice "2RI_0853"
    rin "\"You should join a team for real.\"" id a09_cou1_02_049ab585

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_0863"
    hina "\"Yeah, they tell me they want me to join officially, but...\"" id a09_cou1_02_360dbf94

    $ side_image = "rin 2 side pyjama glasses g"

    voice "2RI_0854"
    rin "\"Multiple teams, right? And they're letting you use shoes and equipment and stuff, not just uniforms. You're a regular VIP.\"" id a09_cou1_02_4b72d908

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_0864"
    hina "\"Yeah, but I'm not gonna.\"" id a09_cou1_02_94501206

    $ side_image = "rin 2 side pyjama glasses a"

    voice "2RI_0855"
    rin "\"Why?\"" id a09_cou1_02_7d422f2e

    show hina z4 2 lg school c with dict_dissolve_25

    voice "2HI_0865"
    hina "\"'Cause I'd have less time to be with Fumi♪\"" id a09_cou1_02_de1d481f

    show hina z4 1 lg school b with Dissolve(0.25)

    show hina:
        "hina z4 1 lg school_scarf b" with Dissolve(0.25)
        ShakeYes

    "Hina smiled and wrapped her scarf around her neck."

    show hina z4 1 lg school_scarf b:
        xoffset 0 yoffset 0
    with None
    show hina z4 1 lg school_scarf p with dict_dissolve_25

    voice "2HI_0866"
    hina "\"Okay, see you!\"" id a09_cou1_02_c6569fc9

    hide hina with Dissolve(0.5)

    play sound se521
    pause 2.0

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_0856"
    rin "\"Kh, the confidence of the blessed...\"" id a09_cou1_02_cb80cee1

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou1_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
