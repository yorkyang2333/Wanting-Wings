label a04_comn_06:

    play sound se044_120 fadein 0.5

    scene bg08ab with Dissolve(0.5)
    pause 2.5

    stop sound fadeout 3.0

    scene bg06ab with Dissolve(0.25)
    pause 0.75

    play sound2 organ04

    "The Christmas hymn recital had just ended."

    "Fumi's accompaniment was without issues, and Hina's singing didn't go so far as to disrupt the harmony of the chorus."

    "A sermon from one of the nuns, and the year's classes were over."

    show rin z3 1 lg school k
    show hina z3 1 lg school m at pos_r2_z3
    show fumi z3 2 lg school j at pos_l2_z3
    with Dissolve(0.25)

    $ voice3("hina","HIN_0999","rin","RIN_0942","fumi","FUM_0837")
    hina_rin_fumi "\"Amen.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a04_cou3_07
    elif rin_hina_score > hina_fumi_score:
        jump a04_cou2_08
    else:
        jump a04_cou1_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
