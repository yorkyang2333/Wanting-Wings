label a00_op_02:

    $ hina_fumi_score = 2
    $ route1 = 2

    scene white with Dissolve(0.5)
    pause 1.5

    scene bg08cb with Dissolve(0.375)
    pause 1.125

    play music bgm05

    pause 1.5

    voice "FUM_0001"
    fumi "I saw the angel when I was six, on Christmas Eve. It was a white Christmas, which was a rarity in that area." (what_first_indent=24, show_name=False)

    voice "FUM_0002"
    fumi "That evening, I picked up a Christmas cake at the bakery where my father worked and headed home with it." (what_first_indent=24, show_name=False)

    voice "FUM_0003"
    fumi "I enjoyed the crunch of the snow underfoot with each step I took." (what_first_indent=24, show_name=False)

    voice "FUM_0004"
    fumi "But suddenly, I stopped. I was missing one shoe. It must have come off in the snow somewhere." (what_first_indent=24, show_name=False)

    voice "FUM_0005"
    fumi "I'd gotten these shoes for Christmas the year before, and they were my absolute favorite pair." (what_first_indent=24, show_name=False)

    voice "FUM_0006"
    fumi "I probably shouldn't have worn such important shoes out in the snow, but at the time, going to my father's bakery felt like visiting a castle." (what_first_indent=24, show_name=False)

    voice "FUM_0007"
    fumi "As my surroundings began to darken, I grew more and more anxious, tears threatening to spill from my eyes at any moment." (what_first_indent=24, show_name=False)

    window hide
    pause 0.5

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    show op_b01:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene bg08cb with Dissolve(0.5)
    pause 1.5



    window auto
    voice "FUM_0008"
    fumi "I looked up at the voice—and there the angel was." (what_first_indent=24, show_name=False)

    window hide
    pause 0.5

    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    show op_b02:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene bg08cb with Dissolve(0.5)
    pause 1.5



    window auto
    voice "FUM_0009"
    fumi "The angel was pointing down, where the heel of a red shoe was sticking up out of the snow. I ran to her and picked up my shoe." (what_first_indent=24, show_name=False)

    voice "FUM_0010"
    fumi "\"Thank you!\"—but when I looked back up at her, the angel was gone." (what_first_indent=24, show_name=False)

    stop music fadeout 2.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.75)
    pause 2.25

    jump a01_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
