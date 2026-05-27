label a03_comn_04:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg01aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    play sound se620_120 fadein 0.5

    show hina 2 lg pyjama a:
        xcenter 432
    with Dissolve(0.25)

    show hina:
        xoffset 0
        ease 0.5 xoffset -10
        ease 0.5 xoffset 0
        repeat 2

    pause 0.5

    show rin:
        "rin 3 lg light pyjama g flat"
        alpha 0.0 xpos 1018 ypos 174
        easein 1.5 alpha 1.0 xpos 918

    pause 1.0

    voice "RIN_0537"
    rin "\"Ugh... noisy...\"" id a03_comn_04_54d56935

    show rin 3 lg light pyjama g:
        alpha 1.0 xpos 918 ypos 174
    show hina 2 lg pyjama a:
        xcenter 432 xoffset 0
    with None

    stop sound fadeout 1.0

    show hina:
        "hina 1 lg pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0663"
    hina "\"Hey, Rin! Why are you sleeping?!\"" id a03_comn_04_86ceb072

    show hina 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None

    "Hina shouted over her vacuuming."

    show rin 3 lg light pyjama b with dict_dissolve_25

    voice "RIN_0538"
    rin "\"I can sleep in on the weekend, can't I?\"" id a03_comn_04_3af618d4

    "Rin stuck her hand out from the bed and waved Hina away."

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0664"
    hina "\"But we all decided together we were gonna clean Saturday morning.\"" id a03_comn_04_70965851

    show rin 3 lg light pyjama d with dict_dissolve_25

    voice "RIN_0539"
    rin "\"Did we...?\"" id a03_comn_04_4e584482

    show hina 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0665"
    hina "\"We did! And it was your idea!\"" id a03_comn_04_6e29719e

    show rin 3 lg light pyjama a with dict_dissolve_25

    voice "RIN_0540"
    rin "\"...I'll get it together next week.\"" id a03_comn_04_cbb1b6e4

    voice "HIN_0666"
    hina "\"You won't! We all have jobs to do, and yours is the window in the living room!\"" id a03_comn_04_266acaf7

    show rin 3 lg light pyjama g with dict_dissolve_25

    voice "RIN_0541"
    rin "\"Uuugh... I get it already...\"" id a03_comn_04_2ab8842a

    "She rustled around in bed, but showed no signs of actually emerging."

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0667"
    hina "\"What are you doing?\"" id a03_comn_04_2baddabe

    show rin 3 lg light pyjama e with dict_dissolve_25

    voice "RIN_0542"
    rin "\"I can't find my glasses...\"" id a03_comn_04_2feb3426

    show hina 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0668"
    hina "\"What~? Again? Where do you usually put them?\"" id a03_comn_04_b1d2f14c

    show rin 3 lg light pyjama g with dict_dissolve_25

    voice "RIN_0543"
    rin "\"Mmh...\"" id a03_comn_04_7aa347fb

    $ side_image = "fumi 2 side pyjama h"

    voice "FUM_0494"
    fumi "\"Umm...\"" id a03_comn_04_67150534

    "Fumi raised a hand timidly in the kitchen, where she was cleaning."

    $ side_image = "fumi 2 side pyjama g"

    voice "FUM_0495"
    fumi "\"I found these in the microwave...\"" id a03_comn_04_71a9bc5f

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0669"
    hina "\"Wait, you don't mean...\"" id a03_comn_04_f522eb19

    show rin 3 lg light pyjama f with dict_dissolve_25

    voice "RIN_0544"
    rin "\"Oh, my glasses.\"" id a03_comn_04_d2e33d73

    show hina:
        "hina 1 lg pyjama g" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0670"
    hina "\"Why?!\"" id a03_comn_04_8d32c88a

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if (route1 == 1 or route1 == 2) and hina_fumi_score > rin_hina_score:
        jump a03_cou1_03
    else:
        jump a03_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
