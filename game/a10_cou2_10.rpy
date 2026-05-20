label a10_cou2_10:

    if persistent.dpatch:
        jump a10_cou2_10_d
    else:
        pause 2.0
        "........."
        "......"
        window hide
        pause 0.5
        window auto

label rp_c_scene04_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    $ renpy.end_replay()


    if routes_cleared < 2:
        jump a10_comn_03
    else:
        jump a10_cou2_11
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
