label a11_cou4_13:

    if persistent.dpatch:
        jump rp_c_scene07
    else:
        stop sound fadeout 1.0
        pause 2.0
        "........."
        "......"
        window hide
        pause 1.0
        window auto

label rp_c_scene07_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
