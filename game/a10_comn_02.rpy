label a10_comn_02:

    scene bg05bb with Dissolve(0.5)
    pause 1.5

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0813"
    sachiko "\"Here we go, happy Valentine's, happy Valentine's.\""

    "Sachiko put chocolates in all the dorm students' shoe cubbies."

    "...She's so quick at this, it's like she's delivering mail."

    if routes_cleared >= 2:
        jump a10_comn_02_a
    else:
        jump a10_comn_02_end

label a10_comn_02_a:

    $ side_image = "sachiko 1 side outfit i"

    voice "2SA_0814"
    sachiko "\"...Hm?\""

    "Sachiko stopped. She was at Miyako's cubby."

    show sachiko 1 sm outfit i with dict_dissolve_25

    voice "2SA_0815"
    sachiko "\"School shoes...\""

    "She stood and looked upward."

label a10_comn_02_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a10_cou1_07
    elif route2 == 2:
        jump a10_cou2_08
    elif route2 == 3:
        jump a10_cou3_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
