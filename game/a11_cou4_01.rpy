label a11_cou4_01:

    scene black with Dissolve(1.0)

    play sound se_bati

    show bati at truecenter
    pause 0.5

    "—There was a flash of lightning."

    pause 0.5

    scene kimikara_11_c with bg_effect_24_750

    pause 0.5

    voice "2SA_0947"
    sachiko "\"N-Noe—?!\"" id a11_cou4_01_ef56cd9f

    pause 0.5

    window hide
    show white:
        alpha 1.0 additive 1.0
        linear 0.3 alpha 0.0
        repeat 2
    pause 0.6
    window auto

    scene white with Dissolve(0.125)
    pause 0.375

    play sound se_2s_h004

    pause 0.5

    scene bg08cb with Dissolve(0.375)
    pause 1.125

    $ side_image = "miyako 1 side school_a d"

    voice "2MI_1117"
    miyako "\"Nice to meet you!\"" id a11_cou4_01_72c0fd8a

    pause 0.5

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
