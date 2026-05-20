label a02_comn_08:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg04aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    "At last, the day of the exams."

    show hina 1 sm school g
    show rin 1 sm school a at pos_r2
    show fumi 1 sm school a at pos_l2
    with Dissolve(0.25)

    voice "HIN_0416"
    hina "\"I did everything I could!\""

    show rin 1 sm school b with dict_dissolve_25

    voice "RIN_0360"
    rin "\"Really?\""

    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0417"
    hina "\"P-Probably! I prayed in the chapel this morning, too.\""

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0311"
    fumi "\"When did you have time for that?\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0361"
    rin "\"So you resorted to praying after all.\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0418"
    hina "\"Anyway! Pass or fail, these next three days will decide it all!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0362"
    rin "\"Of course, if you fail, you'll have to take extra classes and retake the exam.\""

    show hina:
        "hina 1 sm school g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0419"
    hina "\"Don't rain on my parade!\""

    scene black with bg_effect_05
    pause 0.5

    play sound se030a

    pause 1.0

    scene bg08ba with bg_effect_05
    pause 1.0

    scene bg04ba with Dissolve(0.25)
    pause 0.75

    show hina 1 sm school g
    show rin 1 sm school b at pos_r2
    show fumi 1 sm school a at pos_l2
    with Dissolve(0.25)

    voice "HIN_0420"
    hina "\"I-It's all oveeer!\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0363"
    rin "\"In which way?\""

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0421"
    hina "\"Don't ask that!\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0312"
    fumi "\"Okay, we're having a party tonight!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_09
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
