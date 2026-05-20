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
    rin "\"Ugh... noisy...\""

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
    hina "\"Hey, Rin! Why are you sleeping?!\""

    show hina 1 lg pyjama f:
        xoffset 0 yoffset 0
    with None

    "Hina shouted over her vacuuming."

    show rin 3 lg light pyjama b with dict_dissolve_25

    voice "RIN_0538"
    rin "\"I can sleep in on the weekend, can't I?\""

    "Rin stuck her hand out from the bed and waved Hina away."

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0664"
    hina "\"But we all decided together we were gonna clean Saturday morning.\""

    show rin 3 lg light pyjama d with dict_dissolve_25

    voice "RIN_0539"
    rin "\"Did we...?\""

    show hina 1 lg pyjama f with dict_dissolve_25

    voice "HIN_0665"
    hina "\"We did! And it was your idea!\""

    show rin 3 lg light pyjama a with dict_dissolve_25

    voice "RIN_0540"
    rin "\"...I'll get it together next week.\""

    voice "HIN_0666"
    hina "\"You won't! We all have jobs to do, and yours is the window in the living room!\""

    show rin 3 lg light pyjama g with dict_dissolve_25

    voice "RIN_0541"
    rin "\"Uuugh... I get it already...\""

    "She rustled around in bed, but showed no signs of actually emerging."

    show hina 1 lg pyjama j with dict_dissolve_25

    voice "HIN_0667"
    hina "\"What are you doing?\""

    show rin 3 lg light pyjama e with dict_dissolve_25

    voice "RIN_0542"
    rin "\"I can't find my glasses...\""

    show hina 1 lg pyjama l with dict_dissolve_25

    voice "HIN_0668"
    hina "\"What~? Again? Where do you usually put them?\""

    show rin 3 lg light pyjama g with dict_dissolve_25

    voice "RIN_0543"
    rin "\"Mmh...\""

    $ side_image = "fumi 2 side pyjama h"

    voice "FUM_0494"
    fumi "\"Umm...\""

    "Fumi raised a hand timidly in the kitchen, where she was cleaning."

    $ side_image = "fumi 2 side pyjama g"

    voice "FUM_0495"
    fumi "\"I found these in the microwave...\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0669"
    hina "\"Wait, you don't mean...\""

    show rin 3 lg light pyjama f with dict_dissolve_25

    voice "RIN_0544"
    rin "\"Oh, my glasses.\""

    show hina:
        "hina 1 lg pyjama g" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0670"
    hina "\"Why?!\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if (route1 == 1 or route1 == 2) and hina_fumi_score > rin_hina_score:
        jump a03_cou1_03
    else:
        jump a03_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
