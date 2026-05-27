label a09_cou1_04:

    scene bg09ca with Dissolve(0.5)
    pause 1.5

    play music bgm01

    "Hina and Miyako had come to the manager's room."

    "Hina started up the laptop on Sachiko's desk and placed a CD in the disc tray, plugging in her MP3 player."

    "There wasn't a computer in their room, so when she wanted to put new music on her player, she had to come here."

    show bg_obi
    show sachiko 1 lg outfit a at pos_l
    show hina 2 lg pyjama_pjm f at pos_r
    with dict_dissolve_50

    voice "2HI_0888"
    hina "\"What program do I use, Sachiko?\"" id a09_cou1_04_c5d71dbc

    voice "2SA_0696"
    sachiko "\"Rin installed something... Oh, here it is.\"" id a09_cou1_04_675bcfdb

    "She clicked on a musical note icon, and the software started up, reading the data from the CD."

    voice "2SA_0697"
    sachiko "\"Now you just follow the prompts and go through your CDs.\"" id a09_cou1_04_622a96d6

    show hina 2 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0889"
    hina "\"Okay. Thanks.\"" id a09_cou1_04_860a8806

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_0698"
    sachiko "\"You really listen to some oldies, don't you?\"" id a09_cou1_04_1eeb62e7

    "Sachiko picked up a CD from the stack, which was all western music from the 80s and 90s."

    show hina 1 lg pyjama_pjm p with dict_dissolve_25

    voice "2HI_0890"
    hina "\"Yeah, it's all stuff my dad recommended me. I've got space on my player, so I borrowed a bunch of them over New Year's.\"" id a09_cou1_04_4388e6a8

    $ side_image = "miyako 2 side pyjama a"

    voice "2MI_0834"
    miyako "\"They've got dollar prices on them. Are they imported?\"" id a09_cou1_04_251b6c6d

    show hina 1 lg pyjama_pjm a with dict_dissolve_25

    voice "2HI_0891"
    hina "\"Nah, he bought them over there. Dad was overseas most of the time when he was younger. He's fluent in English!\"" id a09_cou1_04_5d9cb034

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0835"
    miyako "\"Wow~ That's amazing.\"" id a09_cou1_04_29727794

    "It's amazing how bad Hina is at English with a dad like that, too."

    show sachiko 1 lg outfit c with dict_dissolve_25

    voice "2SA_0699"
    sachiko "\"How do you fit in listening to just stuff like this? What do you sing at karaoke?\"" id a09_cou1_04_e39a5622

    show hina 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0892"
    hina "\"What do you mean? I sing stuff like this. Here, I'll show y—\"" id a09_cou1_04_8510797c

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0700"
    sachiko "\"That's okay.\"" id a09_cou1_04_8bc0200c

    "A hasty \"no thank you.\""

    show hina 1 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0893"
    hina "\"Rude.\"" id a09_cou1_04_0790096c

    $ side_image = "miyako 1 side pyjama_a b"

    voice "2MI_0836"
    miyako "\"I like your singing. It's untamed.\"" id a09_cou1_04_b6d08be0

    "Like an animal?"

    show hina 1 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0894"
    hina "\"You've got a rocker's soul, Miyako.\"" id a09_cou1_04_531f2bfe

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0701"
    sachiko "\"Oh yeah. Don't open this folder or this folder or this folder or this folder.\"" id a09_cou1_04_7ff873ea

    show hina:
        "hina 1 lg pyjama_pjm f" with Dissolve(0.25)
        ShakeJump

    voice "2HI_0895"
    hina "\"That's a lot! That's everything on the desktop!\"" id a09_cou1_04_986c3eea

    show hina 1 lg pyjama_pjm f:
        xoffset 0 yoffset 0
    with None
    hide sachiko with Dissolve(0.25)

    show miyako 2 lg pyjama a at pos_l with dict_dissolve_25

    voice "2MI_0837"
    miyako "\"What's in them? The names sound pretty impressive... 'Amazing!' and 'Spectacle!' and 'Fantastic!'\"" id a09_cou1_04_10290bc4

    $ side_image = "sachiko 1 side outfit f"

    voice "2SA_0702"
    sachiko "\"Well, I'd show you, but Hinacchi would get mad.\"" id a09_cou1_04_aea95483

    show hina 1 lg pyjama_pjm j with dict_dissolve_25

    voice "2HI_0896"
    hina "\"You will show nothing. The only thing that's not dirty on here is the wallpaper!\"" id a09_cou1_04_255c90d3

    "Somewhat unexpectedly, her desktop wallpaper was still the default image."

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0703"
    sachiko "\"Well, of course it isn't. I use this computer for work and bring it to meetings and stuff.\"" id a09_cou1_04_6cdce17c

    show hina 1 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0897"
    hina "\"It's for work, and you've got this stuff on it?!\"" id a09_cou1_04_99adcb43

    "Click."

    show miyako 1 lg pyjama_a g with dict_dissolve_25

    voice "2MI_0838"
    miyako "\"Wow, there's so many naked ladies~\"" id a09_cou1_04_a0450d2a

    show hina:
        "hina 1 lg pyjama_pjm h" with Dissolve(0.25)
        ShakeTameiki

    voice "2HI_0898"
    hina "\"She opened one...\"" id a09_cou1_04_13332fc7

    show hina 1 lg pyjama_pjm h with None
    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg09ca with bg_effect_05
    pause 0.5

    "........."

    "Hina's music transfer finished, and Miyako began opening all the folders on Sachiko's desktop, beginning with \"Amazing!\" and \"Spectacle!\""

    show bg_obi
    show miyako 1 lg pyjama_a i
    with dict_dissolve_25

    $ side_image = "sachiko 1 side outfit a"

    voice "2SA_0704"
    sachiko "\"Having fun?\"" id a09_cou1_04_12c77d57

    show miyako 1 lg pyjama_a k with dict_dissolve_25

    voice "2MI_0839"
    miyako "\"I don't know, but I just feel like I have to open them all and see what's inside!\"" id a09_cou1_04_ecec2735

    "She's lost in the sheer number of files."

    $ side_image = "sachiko 2 side outfit e"

    voice "2SA_0705"
    sachiko "\"You'll be here 'til morning.\"" id a09_cou1_04_af63cb29

    hide bg_obi
    hide miyako
    with dict_dissolve_50

    $ side_image = "hina 1 side pyjama_pjm n"

    voice "2HI_0899"
    hina "\"......\"" id a09_cou1_04_fdd330a7

    "Hina raised her head from where she was leaning against the bed, gathering all her CDs together."

    $ side_image = "hina 2 side pyjama_pjm h"

    voice "2HI_0900"
    hina "\"...Hey, Sachiko?\"" id a09_cou1_04_26c28f3b

    show sachiko z4 1 lg outfit h with dict_dissolve_25

    voice "2SA_0706"
    sachiko "\"Y-Yes?\"" id a09_cou1_04_fdfc80d0

    "Sachiko turned around timidly."

    $ side_image = "hina 2 side pyjama_pjm d"

    voice "2HI_0901"
    hina "\"I want to ask you something.\"" id a09_cou1_04_e7558150

    show sachiko z4 1 lg outfit b with dict_dissolve_25

    voice "2SA_0707"
    sachiko "\"You're not mad about the porn?\"" id a09_cou1_04_60a0d8a1

    $ side_image = "hina 2 side pyjama_pjm h"

    voice "2HI_0902"
    hina "\"No, just...\"" id a09_cou1_04_369eb15f

    "She hesitated for a moment, then..."

    $ side_image = "hina 2 side pyjama_pjm f"

    voice "2HI_0903"
    hina "\"Sachiko, have you had sex?\"" id a09_cou1_04_219a1f57

    show sachiko:
        "sachiko z4 1 lg outfit h" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0708"
    sachiko "\"Gbfh?!\"" id a09_cou1_04_2953ed0d

    show sachiko z4 1 lg outfit h:
        xoffset 0 yoffset 0
    with None

    "Sachiko spluttered at the sudden question."

    show sachiko z4 1 lg outfit f with dict_dissolve_25

    voice "2SA_0709"
    sachiko "\"...Am I being propositioned?\"" id a09_cou1_04_eb989b68

    $ side_image = "hina 1 side pyjama_pjm g"

    voice "2HI_0904"
    hina "\"I'm not propositioning you!\"" id a09_cou1_04_8f223600

    play sound se_2s_g002

    show sachiko:
        "sachiko z4 1 lg outfit d" with Dissolve(0.25)
        function LayerShake(20,20,0.3)
    $ persistent.layer_shaken = False

    voice "2SA_0710"
    sachiko "\"Gufh!\"" id a09_cou1_04_019c16b0

    show sachiko z4 1 lg outfit d with None
    hide sachiko with dict_dissolve_25

    "Hina threw a pillow that landed a direct hit on Sachiko's face."

    show hina z4 2 lg pyjama_pjm d:
        xcenter 726
    with dict_dissolve_25

    voice "2HI_0905"
    hina "\"Have you, Miyako?\"" id a09_cou1_04_afa04607

    show miyako z4 1 lg pyjama_a g:
        xcenter 298
    with dict_dissolve_25

    voice "2MI_0840"
    miyako "\"Not yet, no~\"" id a09_cou1_04_804acc15

    "The blunt question was met with a blithe answer."

    show miyako z4 2 lg pyjama a with dict_dissolve_25

    voice "2MI_0841"
    miyako "\"Why do you ask, though?\"" id a09_cou1_04_0f401127

    "She did understand that it wasn't like Hina to ask something like that."

    show hina z4 2 lg pyjama_pjm h with dict_dissolve_25

    voice "2HI_0906"
    hina "\"I don't know what I should do with Fumi.\"" id a09_cou1_04_c962059f

    show miyako z4 1 lg pyjama_a e with dict_dissolve_25

    voice "2MI_0842"
    miyako "\"Haven't you done it a few times already, though?\"" id a09_cou1_04_64916bfc

    show hina z4 2 lg pyjama_pjm d with dict_dissolve_25

    voice "2HI_0907"
    hina "\"Yeah, but... I want to get better at it. I want to make Fumi feel good.\"" id a09_cou1_04_18da7dc2

    show miyako z4 1 lg pyjama_a a with dict_dissolve_25

    voice "2MI_0843"
    miyako "\"I see~\"" id a09_cou1_04_42e35673

    "Sachiko looked somewhat befuddled at the extremely frank conversation the girls were having."

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0908"
    hina "\"But you know all about that stuff, right, Sachiko?\"" id a09_cou1_04_ffccd901

    "Naturally, the conversation turned to her."

    $ side_image = "sachiko 1 side outfit h"

    voice "2SA_0711"
    sachiko "\"O-Of course! Ask me anything!\"" id a09_cou1_04_35f8a4d2

    show hina z4 2 lg pyjama_pjm c with dict_dissolve_25

    voice "2HI_0909"
    hina "\"Thanks. I've got a ton of stuff I want to know.\"" id a09_cou1_04_106ff35d

    show miyako z4 1 lg pyjama_a b with dict_dissolve_25

    voice "2MI_0844"
    miyako "\"I'm interested, too.\"" id a09_cou1_04_62f175d5

    $ side_image = "sachiko 2 side outfit i"

    voice "2SA_0712"
    sachiko "\"Uhh, err...\"" id a09_cou1_04_d4f074c8

    pause 0.5
    scene white with bg_effect_27_750
    pause 1.0

    "—At the same time."

    window hide

    pause 0.5

    scene bg01cg with bg_effect_27_750
    pause 0.5

    play music bgm01

    show fumi z4 2 lg pyjama a:
        xcenter 298
    with dict_dissolve_25

    window auto

    voice "2FU_0741"
    fumi "\"Do you have a minute, Ogata?\"" id a09_cou1_04_0ea0b913

    "Fumi set some tea on the table and sat down."

    $ side_image = "rin 2 side pyjama g"

    voice "2RI_0874"
    rin "\"Hm? What's with the formality?\"" id a09_cou1_04_d695e790

    show rin:
        "rin z4 2 lg pyjama glasses a flat"
        alpha 0.0 xcenter 726 ycenter 859
        easein 1.0 alpha 1.0 ycenter 759

    "Rin was lying under the table, but she sat up when she saw the serious look on Fumi's face."

    show rin z4 2 lg pyjama glasses a:
        alpha 1.0 xcenter 726 ycenter 759
    with None
    show fumi z4 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0742"
    fumi "\"I have something I'd like to know, and you're the only one I trust to ask about it.\"" id a09_cou1_04_ff7613a1

    show rin z4 1 lg pyjama glasses a with dict_dissolve_25

    voice "2RI_0875"
    rin "\"Well, I'm not sure what I've done to earn this trust, but ask away.\"" id a09_cou1_04_bb7a6df9

    show fumi z4 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0743"
    fumi "\"Thank you. So, the thing is, umm...\"" id a09_cou1_04_7da6e39c

    show rin:
        "rin z4 1 lg pyjama glasses k" with Dissolve(0.25)
        ShakeTameiki

    voice "2RI_0876"
    rin "\"Uh huh...?\"" id a09_cou1_04_48afdcc7

    show rin z4 1 lg pyjama glasses k:
        xoffset 0 yoffset 0
    with None

    "Rin sipped her tea, waiting for Fumi to continue."

    show fumi z4 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0744"
    fumi "\"Please teach me about sex!\"" id a09_cou1_04_26fc3371

    hide rin
    show rin 1 lg pyjama glasses j as rin_1:
        xcenter 772 ycenter 1016
        function LayerShake(20,20,0.3)
    with dict_dissolve_10
    $ persistent.layer_shaken = False

    voice "2RI_0877"
    rin "\"Bhwh?!\"" id a09_cou1_04_f378132c

    show rin 1 lg pyjama glasses j as rin_1 with None
    hide fumi
    hide rin_1
    with dict_dissolve_50

    "She spit out the tea in her mouth, and spilled the rest from her mug."

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg01cg with bg_effect_05
    pause 0.5

    show fumi 2 lg pyjama b at pos_l
    show rin 1 lg pyjama glasses g at pos_r
    with dict_dissolve_25

    voice "2FU_0745"
    fumi "\"You should probably change everything under your jacket. Please take it off; I'll wash it.\"" id a09_cou1_04_d8429649

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0878"
    rin "\"Uh, okay.\"" id a09_cou1_04_1698cbf0

    hide rin with dict_dissolve_25

    "Rin stood and took her pants off."

    $ side_image = "rin 1 side pyjama glasses i"

    voice "2RI_0879"
    rin "\"Good thing nothing got on my kimono.\"" id a09_cou1_04_bb15f42b

    show fumi 1 lg pyjama a with dict_dissolve_25

    voice "2FU_0746"
    fumi "\"...Yes.\"" id a09_cou1_04_f4ee291d

    show fumi:
        ShakeYes

    "Fumi smiled, taking Rin's track pants from her."

    show fumi 1 lg pyjama b:
        xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "2FU_0747"
    fumi "\"Do you have a spare pair?\"" id a09_cou1_04_e7f315e8

    $ side_image = "rin 2 side pyjama glasses e"

    voice "2RI_0880"
    rin "\"Yeah, I'm good. Anyway, that surprised me. I didn't think you'd ask me that all of a sudden.\"" id a09_cou1_04_b2603636

    show fumi 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0748"
    fumi "\"I'm sorry.\"" id a09_cou1_04_e2593c1a

    $ side_image = "rin 1 side pyjama glasses a"

    voice "2RI_0881"
    rin "\"It's okay. Just gotta get over the shock of hearing the word 'sex' come out of your mouth.\"" id a09_cou1_04_64603734

    show fumi 1 lg pyjama j with dict_dissolve_25

    voice "2FU_0749"
    fumi "\"I'm sorry, I'm sorry, I'm sorry!\"" id a09_cou1_04_fd9da2ec

    show rin 2 lg pyjama glasses f at pos_r with dict_dissolve_25

    voice "2RI_0882"
    rin "\"Really though, where is this coming from? Oh, you're not propositioning me, are you?\"" id a09_cou1_04_7d8911f3

    show fumi 2 lg pyjama d with Dissolve(0.25)
    show fumi:
        ShakeNo

    voice "2FU_0750"
    fumi "\"I'm not, I'm not!\"" id a09_cou1_04_af5ac3dd

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0883"
    rin "\"Ahaha, I'm kidding. You're asking because of Hina, right?\"" id a09_cou1_04_063b905a

    show fumi:
        "fumi 2 lg pyjama h" with Dissolve(0.25)
        ShakeYes

    voice "2FU_0751"
    fumi "\"...Yes. I don't know what to do.\"" id a09_cou1_04_dcc75297

    show fumi 2 lg pyjama h:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses e with dict_dissolve_25

    voice "2RI_0884"
    rin "\"What, you don't want to do it with her?\"" id a09_cou1_04_7c491c28

    show fumi 1 lg pyjama g with dict_dissolve_25

    voice "2FU_0752"
    fumi "\"No, that's not it! I want to do it a lot more!\"" id a09_cou1_04_316ab120

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0885"
    rin "\"A-Ah.\"" id a09_cou1_04_33695798

    show fumi 1 lg pyjama k with dict_dissolve_25

    voice "2FU_0753"
    fumi "\"But neither of us know the first thing about it...\"" id a09_cou1_04_256f7a43

    show fumi 1 lg pyjama h with dict_dissolve_25

    voice "2FU_0754"
    fumi "\"Of course, Hina's trying her hardest, but there must be something I can do, too.\"" id a09_cou1_04_229f51d2

    show fumi 2 lg pyjama f with dict_dissolve_25

    voice "2FU_0755"
    fumi "\"So, I came to you because I figured you know a lot about it.\"" id a09_cou1_04_b8f2da3e

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0886"
    rin "\"......\"" id a09_cou1_04_66921fc0

    "Her face was blank. Well, of course it was. This was basically her punishment."

    show rin 2 lg pyjama glasses b with dict_dissolve_25

    voice "2RI_0887"
    rin "\"Er, y'see... I don't know that I'd say I know a lot about it... since I've never... done it...\"" id a09_cou1_04_ed29c954

    play sound se521
    pause 1.0

    $ side_image = "hina 1 side pyjama_pjm l"

    voice "2HI_0910"
    hina "\"We're back, Fumi, and we brought Sachi—aaah!\"" id a09_cou1_04_7647c447

    show rin 2 lg pyjama glasses a with Dissolve(0.25)
    show rin:
        4.0
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0888"
    rin "\"Oh, hey—wait, what? Ah, N-No, th-this isn't...!!\"" id a09_cou1_04_f2bcdf64

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None
    $ side_image = "hina 1 side pyjama_pjm f"

    voice "2HI_0911"
    hina "\"CHWAAAAH!!\"" id a09_cou1_04_c616cc8d

    play sound se_2s_k007

    show fumi 2 lg pyjama d with dict_dissolve_25
    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False
    pause 0.5

    camera
    with None

    scene white with bg_effect_05
    pause 1.5

    scene bg02dg with bg_effect_25_750
    pause 0.5

    play music bgm01

    show sachiko z4 1 lg outfit a:
        xcenter 298
    show rin z4 1 lg pyjama glasses g:
        xcenter 726
    with Dissolve(0.25)

    show rin:
        ShakeTameiki

    voice "2RI_0889"
    rin "\"Ouch... Those guys are really putting me through the wringer today.\"" id a09_cou1_04_55703cf5

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin massaged her cheek."

    voice "2SA_0713"
    sachiko "\"I mean, she sees a pantsless girl about to pounce on her girlfriend... Can't blame her for bringing out the knee, really.\"" id a09_cou1_04_a7ac7b91

    show rin:
        "rin z4 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeJump

    voice "2RI_0890B"
    rin "\"I just spilled some tea and was changing! Don't say 'pantsless'!\"" id a09_cou1_04_9deae30d

    show rin z4 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    "She was no longer pantsless."

    show sachiko z4 1 lg outfit a with dict_dissolve_25

    voice "2SA_0714"
    sachiko "\"Well, what do we do about this?\"" id a09_cou1_04_5e7f535f

    "Rin and Sachiko had left the others in the living room and were now, of course, discussing..."

    show rin z4 1 lg pyjama glasses i with dict_dissolve_25

    voice "2RI_0891B"
    rin "\"You can't just ask me about sex in real life. It's purely in the realm of fiction for me right now.\"" id a09_cou1_04_0f1a6239

    show sachiko z4 2 lg outfit f with dict_dissolve_25

    voice "2SA_0715"
    sachiko "\"Hinacchi came at me with the real naked truth about everything. And it's like the more innocent she is, the more guilty I feel.\"" id a09_cou1_04_f9ea6b36

    show rin z4 1 lg pyjama glasses g with dict_dissolve_25

    voice "2RI_0892"
    rin "\"Ugh, I get that.\"" id a09_cou1_04_013fb77f

    show sachiko z4 2 lg outfit b with dict_dissolve_25

    voice "2SA_0716"
    sachiko "\"Anyway, can you really talk specifics with them?\"" id a09_cou1_04_0754490e

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0893"
    rin "\"Not me. I'm pure as an angel.\"" id a09_cou1_04_5fb8eb54

    show sachiko z4 1 lg outfit d with Dissolve(0.25)
    show sachiko:
        ShakeTameiki

    voice "2SA_0717"
    sachiko "\"Physically, maybe. I guess it's like a rookie racer asking for advice from an unlicensed gaming addict.\"" id a09_cou1_04_6734c5f7

    show sachiko:
        xoffset 0 yoffset 0
    with None
    show rin:
        "rin z4 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeSide

    voice "2RI_0894"
    rin "\"Ugh. I'm not really sure, but I get the feeling you just hit the nail on the head, and I don't like it...\"" id a09_cou1_04_4e595920

    show rin z4 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None

    "One real experience, even if less than perfect, is better than one hundred magnificent descriptions."

    show rin z4 1 lg pyjama glasses h with dict_dissolve_25

    voice "2RI_0895"
    rin "\"Then I guess it's up to the experienced Miss Sachiko.\"" id a09_cou1_04_a7e732aa

    show sachiko z4 1 lg outfit h with dict_dissolve_25

    voice "2SA_0718"
    sachiko "\"Hey, that's not fair.\"" id a09_cou1_04_1ea822ed

    show rin z4 1 lg pyjama glasses c with dict_dissolve_25

    voice "2RI_0896"
    rin "\"What, you're not going to tell me you're inexperienced? You talk like you're the authority on eros!\"" id a09_cou1_04_d5e91298

    show sachiko z4 2 lg outfit h with dict_dissolve_25

    voice "2SA_0719"
    sachiko "\"O-Of course I'm experienced! Super experienced! I'm practically a pro!\"" id a09_cou1_04_44a6ff22

    "Heheheh."

    show sachiko z4 2 lg outfit j with dict_dissolve_25

    voice "2SA_0720"
    sachiko "\"But what am I supposed to tell them to do? Foreplay?\"" id a09_cou1_04_057897af

    show rin z4 1 lg pyjama glasses f with dict_dissolve_25

    voice "2RI_0897"
    rin "\"When I parted her firmly shut thighs, I found her slit already hot and dripping with honey, twitching...\"" id a09_cou1_04_10c4daaa

    show sachiko z4 1 lg outfit e
    show rin z4 1 lg pyjama glasses d
    with dict_dissolve_25

    $ voice2("rin","2RI_0898","sachiko","2SA_0721N")
    rin_sachiko "\"Aaaaah!\""

    "They both covered their faces with their hands."

    $ side_image = "miyako 1 side pyjama_a c"

    voice "2MI_0845"
    miyako "\"If they both love each other and speak honestly to each other, won't they find the way that works for them naturally?\"" id a09_cou1_04_87dffe9d

    show sachiko z4 1 lg outfit h
    show rin z4 1 lg pyjama glasses j
    with dict_dissolve_25
    camera:
        function LayerShake(5,5,0.3)
    $ persistent.layer_shaken = False

    $ voice2("rin","2RI_0899","sachiko","2SA_0722")
    rin_sachiko "\"Waaah?!\""

    camera
    with None

    "Miyako made her way into the farce the two of them were putting on."

    $ side_image = "miyako 1 side pyjama_b b"

    voice "2MI_0846"
    miyako "\"I was just wondering when you were coming back.\"" id a09_cou1_04_d1bd283a

    show sachiko z4 1 lg outfit c with dict_dissolve_25

    voice "2SA_0723"
    sachiko "\"Ah, umm... we're coming.\"" id a09_cou1_04_5eebdb7d

    pause 0.5

    scene white with bg_effect_05
    pause 1.5

    scene bg01cg with bg_effect_26_750
    pause 0.5

    play music bgm01

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0724"
    sachiko "\"If you both love each other and speak honestly to each other—\"" id a09_cou1_04_ef5d2e3d

    $ side_image = "rin 1 side pyjama g"

    voice "2RI_0900"
    rin "\"Whoa, she copied her!\"" id a09_cou1_04_37e4dc47

    show sachiko 2 lg outfit i with Dissolve(0.25)
    show sachiko:
        2.0
        "sachiko 1 lg outfit i" with Dissolve(0.25)

    voice "2SA_0725"
    sachiko "\"Hey, shut it.\n —Won't you find the way that works for you naturally?\"" id a09_cou1_04_f830b1ae

    show sachiko 1 lg outfit i:
        pass
    with None
    $ side_image = "fumi 2 side pyjama h"

    voice "2FU_0756"
    fumi "\"I see...\"" id a09_cou1_04_26a0d0ae

    "She said, though her face didn't seem to entirely agree."

    $ side_image = "hina 1 side pyjama_pjm k"

    voice "2HI_0912"
    hina "\"What? What do you mean?\"" id a09_cou1_04_54fbcd22

    "This one wants details."

    hide sachiko with Dissolve(0.25)

    show fumi z4 2 lg pyjama h:
        xcenter 118
    show hina z4 1 lg pyjama_pjm k behind fumi, sachiko:
        xcenter 383
    show sachiko z4 2 lg outfit i:
        xcenter 852
    with dict_dissolve_25

    voice "2SA_0726"
    sachiko "\"Umm, basically, just talk to each other about it.\"" id a09_cou1_04_cd73c6cc

    show hina z4 2 lg pyjama_pjm f with dict_dissolve_25

    voice "2HI_0913"
    hina "\"We are talking... aren't we?\"" id a09_cou1_04_e18fbef4

    show fumi z4 2 lg pyjama a with dict_dissolve_25

    voice "2FU_0757"
    fumi "\"...We are.\"" id a09_cou1_04_50d647a3

    "They weren't the type to keep secrets from each other. They were just going in circles because of their lack of information on the subject."

    show hina z4 1 lg pyjama_pjm n with dict_dissolve_25

    voice "2HI_0914"
    hina "\"Is there like a textbook on sex?\"" id a09_cou1_04_44f1d1ef

    show sachiko z4 2 lg outfit c with dict_dissolve_25

    voice "2SA_0727"
    sachiko "\"A textbook, eh...?\"" id a09_cou1_04_095e2ec9

    $ side_image = "rin 1 side pyjama b"

    voice "2RI_0901"
    rin "\"True, there's plenty of that kind of thing for a man and a woman, but for two women... I don't think I've ever seen one.\"" id a09_cou1_04_8e840756

    show fumi z4 2 lg pyjama g with dict_dissolve_25

    voice "2FU_0758"
    fumi "\"Really?\"" id a09_cou1_04_77934cbc

    $ side_image = "rin 1 side pyjama a"

    voice "2RI_0902"
    rin "\"Well, if you're talking numbers—\"" id a09_cou1_04_10daf2c0

    show sachiko:
        "sachiko z4 2 lg outfit d" with Dissolve(0.25)
        ShakeYes

    voice "2SA_0728"
    sachiko "\"......\"" id a09_cou1_04_19723e8e

    show sachiko z4 2 lg outfit d:
        xoffset 0 yoffset 0
    with None

    "Sachiko cleared her throat and elbowed Rin."

    $ side_image = "rin 2 side pyjama d"

    voice "2RI_0903"
    rin "\"Oh...\"" id a09_cou1_04_49d976e4

    show hina z4 1 lg pyjama_pjm k with dict_dissolve_25

    voice "2HI_0915"
    hina "\"Isn't that what the books you two read are like?\"" id a09_cou1_04_284d66ab

    show sachiko z4 1 lg outfit d with dict_dissolve_25

    voice "2SA_0729r2"
    sachiko "\"No, no, no! You can't learn anything from those! They're useless!\"" id a09_cou1_04_274395a8

    $ side_image = "rin 1 side pyjama g"

    voice "2RI_0904"
    rin "\"That's right! In fact, all those will do is give you weird fetishes.\"" id a09_cou1_04_46a30ce6

    show sachiko z4 1 lg outfit j with dict_dissolve_25
    $ side_image = "rin 1 side pyjama i"

    $ voice2("rin","2RI_0905","sachiko","2SA_0730")
    rin_sachiko "\"Hey, don't point at me!\""

    $ side_image = "miyako 1 side pyjama_a d"

    voice "2MI_0847"
    miyako "\"Ahahaha.\"" id a09_cou1_04_896178a4

    "Miyako laughed while Hina and Fumi merely stared blankly."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a09_comn_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
