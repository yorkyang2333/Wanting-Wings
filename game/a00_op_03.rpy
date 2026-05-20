label a00_op_03:

    $ route1 = 3

    scene white with Dissolve(0.5)
    pause 1.5

    scene bg08cb with Dissolve(0.375)
    pause 1.125

    play music bgm05

    pause 1.5

    voice "2RI_0001"
    rin "\"I saw the angel when I was nine, on Christmas Eve. It was a warm winter that year, and I hadn't seen any snow yet.\""

    voice "RIN_0002"
    rin "I was sitting in bed again that day, wrapped up in blankets and reading a book. It didn't matter that it was Christmas." (what_first_indent=24, show_name=False)

    voice "RIN_0003"
    rin "For dinner, I heated up some frozen pilaf in the microwave, and got some fried chicken from a convenience store, too." (what_first_indent=24, show_name=False)

    voice "RIN_0004"
    rin "My parents had been gone for the last three days at some academic conference in Germany. They wouldn't be back until after New Year's." (what_first_indent=24, show_name=False)

    voice "RIN_0005"
    rin "They'd given me money to buy a cake, but I'd spent it on a book instead." (what_first_indent=24, show_name=False)

    voice "RIN_0006"
    rin "I'd gotten cash for both Christmas and New Year's, and I'd spent that on books, too." (what_first_indent=24, show_name=False)

    voice "RIN_0007"
    rin "School was on break starting tomorrow. I could spend the whole time reading books, just like this. Books would stay with me, in exchange for making my eyesight worse." (what_first_indent=24, show_name=False)

    window hide
    pause 0.5

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    show op_c01:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene bg08cb with Dissolve(0.5)
    pause 1.5



    window auto
    voice "RIN_0008"
    rin "I heard a voice out of nowhere and jumped. When I looked up—there was an angel there." (what_first_indent=24, show_name=False)

    voice "RIN_0009"
    rin "I screamed and threw the book I was holding." (what_first_indent=24, show_name=False)

    window hide
    pause 0.5

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    show op_c02:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene bg08cb with Dissolve(0.5)
    pause 1.5



    window auto
    voice "RIN_0010"
    rin "The book went right through the angel and hit the wall behind her." (what_first_indent=24, show_name=False)

    stop music fadeout 2.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.75)
    pause 2.25

    jump a01_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
