label a11_cou4_04:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_04:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg09aa with Dissolve(0.25)
    pause 0.75

    play music bgm01 fadein 1.0

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0984"
    sachiko "\"Mhm, yeah. I forgot to give it to her. I'll bring it. I can stop by your office when I come do my cleaning.\"" id a11_cou4_04_3a9e8b95

    "Sachiko was on the phone. Miyako's transfer forms were in her hand."

    $ side_image = "sachiko 1 side outfit d"

    voice "2SA_0985"
    sachiko "\"Hm? It's been almost two weeks since she came down. Yes, I know, you don't need to worry. I had her get a physical.\"" id a11_cou4_04_87dfdbf4

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_0986"
    sachiko "\"Yep, this one's perfectly healthy...\"" id a11_cou4_04_037ac226

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0987"
    sachiko "\"Ahaha, all former angels are, aren't they? Including you.\"" id a11_cou4_04_989e0478

    $ side_image = "sachiko 1 side outfit b"

    voice "2SA_0988"
    sachiko "\"What? You want to see her? Hmm, well she's probably arriving right about now. They were running around this morning, so they might be late.\"" id a11_cou4_04_56219699

    "Sachiko looked up at the clock."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0989"
    sachiko "\"Yeah, give 'em a pass just this once, would you?\"" id a11_cou4_04_7ef88af8

    $ side_image = "sachiko 1 side outfit g"

    voice "2SA_0990"
    sachiko "\"...I think you'll be surprised when you see her face. You always liked her, didn't you? Mhm, just like a granddaughter.\"" id a11_cou4_04_da2f20a6

    $ side_image = "sachiko 2 side outfit f"

    voice "2SA_0991"
    sachiko "\"Yeah, thanks. That was a real help. Uh huh... mhm.\"" id a11_cou4_04_3b78dd3b

    $ side_image = "sachiko 2 side outfit g"

    voice "2SA_0992"
    sachiko "\"What? No, it's not like that. I'm just looking after her until she gets used to things.\"" id a11_cou4_04_889b87e2

    $ side_image = "sachiko 1 side outfit c"

    voice "2SA_0993"
    sachiko "\"If you're gonna be that way, I'll just mail in the forms.\"" id a11_cou4_04_ec88b052

    $ side_image = "sachiko 1 side outfit d"

    voice "2SA_0994"
    sachiko "\"...Yes, yes. I understand. Okay, I'll see you. Look out for Miyako, would you?\"" id a11_cou4_04_00baeab6

    play sound se_2s_j012

    "Not liking where the conversation was going, Sachiko entrusted Miyako to the principal and ended her phone call."

    "Well, I can imagine what the topic was."

    show sachiko 1 lg outfit d with Dissolve(0.25)
    show sachiko:
        ShakeTameiki

    voice "2SA_0995"
    sachiko "\"Haahh... what is she, my grandma?\"" id a11_cou4_04_a2d9d682

    show sachiko 2 lg outfit i:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2SA_0996"
    sachiko "\"I'm not lonely or anything. Unlike you, I'm still young!\"" id a11_cou4_04_11445ffe

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
