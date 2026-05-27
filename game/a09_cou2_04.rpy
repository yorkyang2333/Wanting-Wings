label a09_cou2_04:

    scene bg07ca with Dissolve(0.5)
    pause 1.5

    play music bgm02

    play sound se521
    pause 2.0

    show sachiko 1 sm outfit cigarette i at pos_ls with Dissolve(0.25)

    voice "2SA_0731"
    sachiko "\"You come to the roof too often.\"" id a09_cou2_04_3cd60983

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0981"
    rin "\"Well, you're here too often.\"" id a09_cou2_04_9a1bc045

    "The two pointed their fingers at each other."

    show sachiko 1 sm outfit cigarette a with dict_dissolve_25
    show rin 1 sm pyjama glasses b at pos_rs with dict_dissolve_50

    voice "2SA_0732"
    sachiko "\"What's up? Feeling troubled? Need some sage advice?\"" id a09_cou2_04_aff4f4b2

    show rin 1 sm pyjama glasses a with dict_dissolve_25

    voice "2RI_0982"
    rin "\"No, I just needed some disinfectant and a band-aid, but you weren't there.\"" id a09_cou2_04_9d5557bf

    "Rin held up her bandaged finger."

    show sachiko 1 sm outfit cigarette i with dict_dissolve_25

    voice "2SA_0733"
    sachiko "\"Mm, wanna head down, then?\"" id a09_cou2_04_bd7b2de7

    hide sachiko with dict_dissolve_50

    "She got up from the fence she was leaning against, but..."

    show rin 1 sm pyjama glasses b with dict_dissolve_25

    voice "2RI_0983"
    rin "\"Oh, but I could use some advice, too.\"" id a09_cou2_04_a8fa007d

    $ side_image = "sachiko 2 side outfit cigarette e"

    voice "2SA_0734"
    sachiko "\"...Sure thing.\"" id a09_cou2_04_16023419

    play sound se_fence

    "Sachiko finished her cigarette, dropped it in a portable ashtray, and leaned back against the fence again."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg07ca with bg_effect_05
    pause 0.5

    show sachiko z4 1 lg outfit h:
        xcenter 298
    show rin z4 1 lg pyjama glasses a:
        xcenter 726
    with Dissolve(0.25)

    voice "2SA_0735"
    sachiko "\"Wow, that's some wild stuff you're making her do.\"" id a09_cou2_04_0797d387

    "...was Sachiko's reaction when Rin told her about what had happened on their walk that afternoon."

    show rin z4 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0984"
    rin "\"Huh? You think so?\"" id a09_cou2_04_fe31e6b1

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0736"
    sachiko "\"I mean, 'shake, stay, spin'? You're treating your girlfriend like she's a dog. If you're putting a collar on her and taking her for walks, I'd say you're in pervert territory already.\"" id a09_cou2_04_6a4f87e1

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_0985"
    rin "\"We're not! Hina wants me to put it on her! And it's not a collar, it's a choker!\"" id a09_cou2_04_0d5bec61

    show rin z4 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0737"
    sachiko "\"Well, I'm mostly joking. So what are you worried about?\"" id a09_cou2_04_25e8eca7

    show sachiko z4 1 lg outfit d:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0986"
    rin "\"...I'm beginning to fear my own power.\"" id a09_cou2_04_df77ef64

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0738"
    sachiko "\"Power? Like your arm aches or you can see something not of this world?\"" id a09_cou2_04_2852ceac

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0987"
    rin "\"No, nothing like that. It's Hina. She's too obedient. When she's wearing the choker, she'll do anything I tell her to.\"" id a09_cou2_04_574bbf4d

    show sachiko z4 1 lg outfit h with dict_dissolve_25

    voice "2SA_0739"
    sachiko "\"Wait, so this {i}is{/i} some kind of slave training thing? I don't think I'm really qualified to help with that...\"" id a09_cou2_04_9d19ff30

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0988B"
    rin "\"That's not it! It just kind of freaks me out how devoted she is.\"" id a09_cou2_04_197ef21d

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0740"
    sachiko "\"Yeah, she is that, Hinacchi. Unlike you.\"" id a09_cou2_04_a08a5aa6

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0989"
    rin "\"Ugh... It's true.\"" id a09_cou2_04_15fcec9b

    voice "2SA_0741"
    sachiko "\"She's like a blank canvas just waiting to be painted right now, and she'll change her colors to whatever you want.\"" id a09_cou2_04_7aed6535

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0990B"
    rin "\"...I'm already starting to panic about how she's changing.\"" id a09_cou2_04_ae1d7932

    "Rin scrunched up her shoulders. It was clear to anyone, not just Rin, how different Hina was now than before they were dating."

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0742"
    sachiko "\"So. You say you're scared of your power, and I do think you have the power to break Hinacchi.\"" id a09_cou2_04_7b8c72d1

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0991"
    rin "\"Brea... I-I'd never order her to do something that bad!\"" id a09_cou2_04_639154f6

    show rin z4 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    show sachiko z4 1 lg outfit g with dict_dissolve_25

    voice "2SA_0743"
    sachiko "\"Haha, Hinacchi's not so weak that she'd break from something you ordered her to do.\"" id a09_cou2_04_a65e7db4

    show rin z4 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0992"
    rin "\"Huh...?\"" id a09_cou2_04_1cae1cc7

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0744"
    sachiko "\"What you should be scared of isn't the power you have over Hina. It's the negative power inside you.\"" id a09_cou2_04_b3646867

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0993"
    rin "\"What? You mean like the Force?\"" id a09_cou2_04_d910a17c

    "She didn't get it."

    show sachiko z4 2 lg outfit a with dict_dissolve_25

    voice "2SA_0745"
    sachiko "\"Do you love Hinacchi?\"" id a09_cou2_04_272d3ddb

    "Sachiko put on a bit of a serious face."

    show rin z4 2 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0994"
    rin "\"Of course I do.\"" id a09_cou2_04_2821098b

    show sachiko z4 2 lg outfit b with dict_dissolve_25

    voice "2SA_0746"
    sachiko "\"Well, Hinacchi loves you more.\"" id a09_cou2_04_bf4e6ef6

    show rin z4 2 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0995"
    rin "\"Probably...\"" id a09_cou2_04_8e0daa2b

    show sachiko z4 1 lg outfit d with Dissolve(0.25)
    show sachiko:
        ShakeTameiki

    voice "2SA_0747"
    sachiko "\"You know, that 'probably'...\"" id a09_cou2_04_17d68ae4

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show rin z4 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0996"
    rin "\"Yeah?\"" id a09_cou2_04_d99718fe

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0748"
    sachiko "\"...Nah, that's enough for today.\"" id a09_cou2_04_e7575428

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0997"
    rin "\"What? Don't just leave me hanging.\"" id a09_cou2_04_66a85bd1

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0749"
    sachiko "\"I'm not leaving you hanging. I'm watching over you.\"" id a09_cou2_04_e4566517

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0998"
    rin "\"Uh huh...\"" id a09_cou2_04_f2aa7606

    show sachiko z4 1 lg outfit i with dict_dissolve_25

    voice "2SA_0750"
    sachiko "\"Anyway. You gotta hold the leash tight, or you're gonna get bit.\"" id a09_cou2_04_5c378a5e

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0999"
    rin "\"I already got bit.\"" id a09_cou2_04_23f5f028

    "Rin held up her finger with the band-aid falling off of it."

    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        ShakeTameiki

    voice "2SA_0751"
    sachiko "\"...Hahh...\"" id a09_cou2_04_64e826fc

    show sachiko z4 1 lg outfit d:
        xoffset 0 yoffset 0
    with None

    "Sachiko sighed at Rin's lack of understanding."

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0752"
    sachiko "\"I'm going down. Come on, I'll get you a new band-aid.\"" id a09_cou2_04_0a0c0627

    hide sachiko with dict_dissolve_50

    "Sachiko headed over to the door from the fence."

    show rin z4 2 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_1000"
    rin "\"Oh, okay.\"" id a09_cou2_04_a5352b51

    hide rin with dict_dissolve_50

    "Rin followed."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_cou2_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
