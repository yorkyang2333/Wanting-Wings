label a04_comn_04:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg04aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 1 sm school d
    show rin 1 sm school a at pos_r2
    show fumi 1 sm school a at pos_l2
    with Dissolve(0.25)

    show hina:
        ShakeUji

    voice "HIN_0994"
    hina "\"B-By the skin of my teeth...\""

    show hina:
        xoffset 0 yoffset 0
    with None

    "Hina's voice trembled, exam in hand."

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0938"
    rin "\"You were seriously one question away here.\""

    show hina 1 sm school c with dict_dissolve_25

    voice "HIN_0995"
    hina "\"But I've managed to avoid remedial English lessons!\""

    show fumi 1 sm school c with dict_dissolve_25

    voice "FUM_0835"
    fumi "\"Congratulations.\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0939"
    rin "\"Pretty unique for the class rep to fail and take remedial classes.\""

    show hina 1 sm school h with dict_dissolve_25

    voice "HIN_0996"
    hina "\"Really... I just barely managed to protect my standing as class rep.\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0940"
    rin "\"I dunno if it really counts if you only just barely passed...\""

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0836"
    fumi "\"Oh, but don't forget you have assignments to do instead of remedial classes.\""

    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0997"
    hina "\"Ugh... that's right.\""

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school d with dict_dissolve_25

    voice "RIN_0941"
    rin "\"You can do it! Protect that standing!\""

    show hina:
        "hina 1 sm school h" with Dissolve(0.25)
        ShakeUji

    voice "HIN_0998"
    hina "\"Auuugh...\""

    show hina 1 sm school h:
        xoffset 0 yoffset 0
    with None

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a04_cou3_04
    elif rin_hina_score > hina_fumi_score:
        jump a04_cou2_05
    else:
        jump a04_cou1_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
