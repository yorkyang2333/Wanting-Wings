label a02_cou3_02:

    scene bg08ba with Dissolve(0.5)
    pause 1.5

    scene bg01ba with Dissolve(0.25)
    pause 0.75

    play music bgm01

    play sound se118b

    show hina:
        "hina 1 lg pyjama l flat"
        alpha 0.0 xcenter 512 ycenter 1081
        easein 0.5 alpha 1.0 ycenter 981

    voice "HIN_0621"
    hina "\"Hwah?!\""

    show hina 1 lg pyjama l:
        alpha 1.0 xcenter 512 ycenter 981

    "Hina's head flew up from the table."

    "She looked around, but didn't see Rin or Fumi anywhere."

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0622"
    hina "\"Where'd they go...?\""

    "A blanket fell from her shoulders."

    play sound se521

    $ side_image = "rin 1 side casual a"

    voice "RIN_0482"
    rin "\"Heeey.\""

    $ side_image = "fumi 1 side casual b"

    voice "FUM_0433"
    fumi "\"We're back.\""

    "The two of them returned just then, shopping bags in hand."

    show hina 1 lg pyjama d with dict_dissolve_25

    voice "HIN_0623"
    hina "\"H... Hi.\""

    $ side_image = "fumi 1 side casual d"

    voice "FUM_0434"
    fumi "\"I went shopping with Ogata since you were sleeping, Natsume.\""

    "Fumi opened the refrigerator and started putting the food away."

    show hina:
        "hina 1 lg pyjama h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0624"
    hina "\"I dozed off, huh?\""

    show hina 1 lg pyjama h:
        xoffset 0 yoffset 0
    with None

    $ side_image = "fumi 1 side casual a"

    voice "FUM_0435"
    fumi "\"Well, we were up late last night.\""

    hide hina with Dissolve(0.25)

    show hina 1 sm pyjama k with dict_dissolve_25:
        xcenter 252
    show rin:
        "rin 1 sm casual c flat"
        alpha 0.0 xcenter 872
        easein 0.5 alpha 1.0 xcenter 772
    pause 0.5

    show hina 1 sm pyjama k with None
    show rin 1 sm casual c:
        alpha 1.0 xcenter 772
        4.3
        "rin 1 sm casual e" with Dissolve(0.25)

    voice "RIN_0483"
    rin "\"Ahaha, and how'd your sleep-learning go... whoa!\""

    show rin 1 sm casual e:
        alpha 1.0 xcenter 772
    with None

    "Rin did a double-take when she went into the living room and saw Hina's face."

    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0625"
    hina "\"'Whoa!' what?\""

    show hina 1 sm pyjama f:
        xoffset 0 yoffset 0
    with None

    show rin:
        "rin 1 sm casual e" with Dissolve(0.25)
        xcenter 772
        easein 0.25 xcenter 512
    show hina:
        "hina 1 sm pyjama f" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 172
    show fumi:
        "fumi 1 sm casual e flat"
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852
    pause 0.5

    show rin 1 sm casual e:
        xcenter 512
    show hina 1 sm pyjama f:
        xcenter 172
    show fumi 1 sm casual e:
        alpha 1.0 xcenter 852
    with None

    voice "FUM_0436"
    fumi "\"Oh my.\""

    "Fumi followed Rin in and noticed as well."

    show hina:
        "hina 1 sm pyjama d" with Dissolve(0.25)
        ShakeJump
        0.5
        ShakeJump

    voice "HIN_0626"
    hina "\"What? What is it?\""

    show hina 1 sm pyjama d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm casual d with dict_dissolve_25

    voice "FUM_0437"
    fumi "\"Your notes are on your forehead.\""

    show hina:
        "hina 1 sm pyjama l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0627"
    hina "\"What?!\""

    show hina 1 sm pyjama l:
        xoffset 0 yoffset 0
    with None

    "Hina's hands flew to her forehead."

    show rin 1 sm casual f with dict_dissolve_25

    voice "RIN_0484"
    rin "\"You might get in trouble for cheating.\""

    show fumi 1 sm casual c with dict_dissolve_25

    voice "FUM_0438"
    fumi "\"Ahaha, I'll go get a wet towel.\""

    show hina:
        "hina 1 sm pyjama d" with Dissolve(0.25)
        ShakeNo

    voice "HIN_0628"
    hina "\"Urrrgh...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
