label a10_comn_01:

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    if persistent.dpatch:
        "Valentine's was finally a day away, and a light and airy mood had settled over the school." id a10_comn_01_8432f745
    else:
        "Valentine's was finally a day away, and a light and airy mood had settled over the campus."

    "But first, there's something that must be dealt with."

    "The results of the proficiency tests."

    show hina_1_150_school_g as hina with Dissolve(0.1):
        xcenter 512 ycenter 1235
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "2HI_1186"
    hina "\"Gwaaah!\"" id a10_comn_01_75dd3c9f

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route2 == 1:
        jump a10_cou1_04
    elif route2 == 3:
        jump a10_cou3_06
    elif routes_cleared >= 2:
        jump a10_cou4_01
    elif route2 == 2:
        jump a10_cou2_06
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
