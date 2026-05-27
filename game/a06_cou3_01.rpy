label a06_cou3_01:

    $ route2 = 3

    scene black with Dissolve(0.5)
    pause 1.5

    play music bgm03

    voice "2RI_0031"
    rin "\"...Merry Christmas, Fumi.\"" id a06_cou3_01_b916ab38

    voice "2FU_0018"
    fumi "\"...Merry Christmas, Rin.\"" id a06_cou3_01_d3a86dad

    $ voice2("rin","2RI_0032","fumi","2FU_0019")
    rin_fumi "\"Mh...\""

    show hina 1 lg pyjama q with Dissolve(0.5)

    voice "2HI_0026"
    hina "\"Mhm, mhm, good, good. A friend's happiness might be even nicer than your own happiness.\"" id a06_cou3_01_58a00766

    show hina 1 lg pyjama m with dict_dissolve_25

    voice "2HI_0027"
    hina "\"......\"" id a06_cou3_01_5ffedd32

    show hina:
        "hina 1 lg pyjama n flat" with Dissolve(0.25)
        alpha 1.0
        5.0
        linear 0.25 alpha 0.0

    show ev15_sozai01:
        alpha 0.0
        5.25
        "ev15_sozai01.webp" with bg_effect_18_2000
        linear 2.0 alpha 1.0

    voice "2HI_0028"
    hina "\"Kisses make more noise than I thought they would. I don't think peeping would be very polite, but... waaah?!\"" id a06_cou3_01_ffa16d97

    hide hina with None
    show ev15_sozai01 with None
    hide ev15_sozai01 with bg_effect_17_300

    pause 1.0

    show hina 2 lg pyjama b
    with Dissolve(0.25)

    voice "2HI_0029"
    hina "\"Y-You know, even I'm not gonna completely reject anything sexual. I know it's a natural thing for two people who love each other to do.\"" id a06_cou3_01_f3f727e9

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "2HI_0030"
    hina "\"I'm surprised you can hold your breath that long, though... You've got to be running out soon...\"" id a06_cou3_01_817e0bc3

    $ voice2("rin","2RI_0033","fumi","2FU_0020")
    rin_fumi "\"Whew...\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "2HI_0031"
    hina "\"Oh, are you done...?\"" id a06_cou3_01_45fec52e

    hide hina
    with Dissolve(0.25)

    show ev15_sozai01
    with bg_effect_18_1000

    pause 1.0

    hide ev15_sozai01
    with bg_effect_17_300

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "2HI_0032"
    hina "\"What, it was just a break?!\"" id a06_cou3_01_f85b9866

    show hina:
        "hina 1 lg pyjama h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0033"
    hina "\"Haah... Fine, just go until you're satisfied...\"" id a06_cou3_01_c0e57cbc

    show hina 1 lg pyjama h:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg pyjama m" with Dissolve(0.25)
        ShakeNo_2_250

    voice "2HI_0034"
    hina "\"......\"" id a06_cou3_01_d3886a76

    show hina 1 lg pyjama m:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg pyjama n" with Dissolve(0.25)
        ShakeNo_3_500

    voice "2HI_0035"
    hina "\"............\"" id a06_cou3_01_7b92dfa1

    show hina 1 lg pyjama n:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina 1 lg pyjama o" with Dissolve(0.25)
        ShakeUji

    voice "2HI_0036"
    hina "\"..................\"" id a06_cou3_01_46a41e9a

    play sound se_2s_g007

    scene black
    with Dissolve(0.125)

    pause 0.675

    scene bg01ch with bg_effect_18

    $ side_image = "hina 1 side pyjama g"

    voice "2HI_0037"
    hina "\"Ah! Hey! You're taking your clothes off, aren't you?! Stop, stop! Cut it out! That's enough! That's all for tonight, folks!!\"" id a06_cou3_01_695df10b

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a07_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
