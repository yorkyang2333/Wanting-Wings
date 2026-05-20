label a00_op_01:

    $ rin_hina_score = 2
    $ route1 = 1

    scene white with Dissolve(0.5)
    pause 1.5

    scene bg08cb with Dissolve(0.375)
    pause 1.125

    play music bgm05

    pause 1.5

    voice "HIN_0001"
    hina "I saw the angel when I was six, on Christmas Eve. It was a white Christmas, which was a rarity in that area." (what_first_indent=24, show_name=False)

    voice "HIN_0002"
    hina "In that warm living room, I cared not for turkey or cake, but was focused entirely on the toy camera I'd gotten as a present." (what_first_indent=24, show_name=False)

    voice "HIN_0003"
    hina "Due to an unfortunate encounter at my bedside the year before, I no longer believed in Santa and was handed the present directly from my dad." (what_first_indent=24, show_name=False)

    voice "HIN_0004"
    hina "Waving away the help my dad was trying to give me, I struggled for some time, but eventually managed to get the film inserted." (what_first_indent=24, show_name=False)

    voice "HIN_0005"
    hina "And when I raised my head in search of a subject to photograph—an angel met my eye." (what_first_indent=24, show_name=False)

    voice "HIN_0006"
    hina "I tugged on my sister's sleeve! But she didn't seem to be able to see the angel. And not just her, but my mom and dad couldn't, either." (what_first_indent=24, show_name=False)

    voice "HIN_0007"
    hina "The angel picked up the strawberry from my half-eaten Christmas cake and asked," (what_first_indent=24, show_name=False)

    window hide
    pause 0.5

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    show op_a02:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene bg08cb with Dissolve(0.5)
    pause 1.5



    window auto
    voice "HIN_0008"
    hina "\"Red,\" I answered, and snapped a picture for the first time in my life." (what_first_indent=24, show_name=False)

    stop music fadeout 2.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.75)
    pause 2.25

    jump a01_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
