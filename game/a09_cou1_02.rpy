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
    hina "\"Okay, I'll be back.\""

    show hina z4 2 lg school a:
        alpha 1.0 xcenter 512
    with None

    "Hina came in from the bedroom wearing her uniform."

    $ side_image = "rin 1 side pyjama glasses e"

    voice "2RI_0845"
    rin "\"Huh? Were you subbing today?\""

    "Rin rolled over and looked up at her."

    voice "2HI_0855"
    hina "\"Yeah, softball and basketball today.\""

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_0846"
    rin "\"Ugh, a doubleheader?! You really do have too much energy.\""

    show hina z4 1 lg school a with dict_dissolve_25

    voice "2HI_0856"
    hina "\"Well, the softball team asked me first, but there's just enough time before the basketball game that I can make that, too.\""

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_0847"
    rin "\"Where the heck does all the energy come from in that little body of yours...? Huh, are you nuclear-powered, Hina?\""

    show hina z4 1 lg school e with dict_dissolve_25

    voice "2HI_0857"
    hina "\"I'm food-powered!\""

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0848"
    rin "\"Come to think of it, do they pay you for your sub work?\""

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_0858"
    hina "\"Based on performance.\""

    $ side_image = "rin 1 side pyjama glasses f"

    voice "2RI_0849"
    rin "\"D'you need an agent? I know an Ogata who's good.\""

    show hina z4 2 lg school a with dict_dissolve_25

    voice "2HI_0859"
    hina "\"Nope. Anyway, Fumi made you some lunch in the fridge. Go ahead and eat it if you get hungry.\""

    $ side_image = "rin 1 side pyjama glasses k"

    voice "2RI_0850"
    rin "\"Uh huh.\""

    show hina z4 2 lg school f with dict_dissolve_25

    voice "2HI_0860"
    hina "\"You just have to heat it up in the microwave. You know how?\""

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0851"
    rin "\"Of course I know how. How long d'you think I've been a latchkey kid?\""

    show hina z4 1 lg school p with dict_dissolve_25

    voice "2HI_0861"
    hina "\"Right, right. Tell Miyako, too.\""

    $ side_image = "rin 1 side pyjama glasses b"

    voice "2RI_0852"
    rin "\"Mhm~\""

    show hina:
        "hina z4 1 lg school a" with Dissolve(0.25)
        ShakeYes

    voice "2HI_0862"
    hina "\"Here we go...\""

    show hina z4 1 lg school a:
        xoffset 0 yoffset 0
    with None

    "Hina hefted up a bag with her uniforms and equipment in it."

    $ side_image = "rin 2 side pyjama glasses a"

    voice "2RI_0853"
    rin "\"You should join a team for real.\""

    show hina z4 2 lg school e with dict_dissolve_25

    voice "2HI_0863"
    hina "\"Yeah, they tell me they want me to join officially, but...\""

    $ side_image = "rin 2 side pyjama glasses g"

    voice "2RI_0854"
    rin "\"Multiple teams, right? And they're letting you use shoes and equipment and stuff, not just uniforms. You're a regular VIP.\""

    show hina z4 2 lg school d with dict_dissolve_25

    voice "2HI_0864"
    hina "\"Yeah, but I'm not gonna.\""

    $ side_image = "rin 2 side pyjama glasses a"

    voice "2RI_0855"
    rin "\"Why?\""

    show hina z4 2 lg school c with dict_dissolve_25

    voice "2HI_0865"
    hina "\"'Cause I'd have less time to be with Fumi♪\""

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
    hina "\"Okay, see you!\""

    hide hina with Dissolve(0.5)

    play sound se521
    pause 2.0

    $ side_image = "rin 1 side pyjama glasses g"

    voice "2RI_0856"
    rin "\"Kh, the confidence of the blessed...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou1_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
