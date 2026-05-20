label a04_comn_07:

    scene bg05bb with Dissolve(0.5)
    pause 1.5

    $ side_image = "sachiko 1 side outfit cigarette b"

    voice "SYO_0145"
    sachiko "\"I thought it was cold...\""

    "The manager's room. Sachiko wiped away the condensation on the window and looked up at the sky."

    $ side_image = "sachiko 1 side outfit cigarette a"

    voice "SYO_0146"
    sachiko "\"It's snowing.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a04_cou3_08
    elif rin_hina_score > hina_fumi_score:
        jump a04_cou2_09
    else:
        jump a04_cou1_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
