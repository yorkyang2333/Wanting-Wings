label a03_cou2_02:

    scene bg05ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin 2 lg pyjama glasses g:
        xcenter 462
    with Dissolve(0.25)

    play sound se013b

    voice "RIN_0660"
    rin "\"......\""

    play sound se013b

    "........."

    play sound se013b

    "......"

    show hina behind rin:
        "hina 2 lg pyjama g flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772
    pause 0.5

    play sound se118b

    show hina 2 lg pyjama g:
        ShakeJump

    voice "HIN_0846"
    hina "\"Yah!\""

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0661"
    rin "\"Wah?! What?!\""

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "Rin spun around, surprised, when the back of her shirt was suddenly rolled up."

    show hina 2 lg pyjama d with dict_dissolve_25

    voice "HIN_0847"
    hina "\"...Yeah, I thought not.\""

    "The culprit was Hina."

    show rin:
        "rin 1 lg pyjama glasses j behind hina" with Dissolve(0.25)
        easein 0.25 xcenter 259

    voice "RIN_0662"
    rin "\"Wh-What are you doing?!\""

    show rin 1 lg pyjama glasses j behind hina:
        xcenter 259
    with None
    show hina 1 lg pyjama a with dict_dissolve_25

    voice "HIN_0848"
    hina "\"Checking for wings.\""

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0663"
    rin "\"This is stupid. Of course I don't have them.\""

    show hina 1 lg pyjama n with dict_dissolve_25

    voice "HIN_0849"
    hina "\"...I just wanted to make sure.\""

    "Hina looked disappointed somehow."

    show rin 1 lg pyjama glasses d with dict_dissolve_25

    voice "RIN_0664"
    rin "\"Fine, then... I'll check you, too!!\""

    play sound se118a

    show rin 1 lg pyjama glasses d:
        xcenter 259
        easein 0.25 xcenter 512

    show hina:
        "hina 1 lg pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0850"
    hina "\"Waaah?!\""

    show hina 1 lg pyjama l:
        xoffset 0 yoffset 0
    with None

    "Rin leapt on Hina and held her down."

    show hina:
        "hina 1 lg pyjama c" with Dissolve(0.25)
        function LayerShake(20,20,1.0)
    $ persistent.layer_shaken = False

    voice "HIN_0851"
    hina "\"Aha, ahahahahaha! Hey, what do you think you're—You know I'm tickli...hahah!\""

    show hina 1 lg pyjama c:
        xoffset 0 yoffset 0
    with None

    show rin 1 lg pyjama glasses f with dict_dissolve_25

    voice "RIN_0665"
    rin "\"Where are your wings~?\""

    show hina:
        "hina 1 lg pyjama g" with Dissolve(0.25)
        ShakeJump
        ShakeJump

    voice "HIN_0852"
    hina "\"Yaaah, stop it! Ahahaha! Stop, stooop!\""

    show hina 1 lg pyjama g:
        xoffset 0 yoffset 0
    with None

    play sound se521

    pause 0.5

    $ side_image = "fumi 1 side pyjama c"
    voice "FUM_0648"
    fumi "\"You two get along so well~\""

    "It always ends like that, huh?"

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a03_comn_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
