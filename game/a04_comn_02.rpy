label a04_comn_02:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg06aa with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin 1 lg school e at pos_r
    show fumi 1 lg school a at pos_l
    with Dissolve(0.25)

    voice "RIN_0918"
    rin "\"Pianos and organs aren't the same?\"" id a04_comn_02_9bf4f261

    "Rin asked Fumi, closing the lid of her lunch box."

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0814"
    fumi "\"Ah, they're similar but there are a lot of differences, too. A piano is a string instrument, and an organ is a wind instrument.\"" id a04_comn_02_4dd73f1c

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0919"
    rin "\"Hm...\"" id a04_comn_02_44b8b833

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0815"
    fumi "\"A hammer hits strings in a piano, but in an organ, it's air passing through pipes.\"" id a04_comn_02_159863c9

    "Fumi went on as Rin gave her an uncomprehending look."

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0816"
    fumi "\"The organ here is a reed organ, so it makes sound by vibrating air created with the pedals against brass reeds.\"" id a04_comn_02_1908917c

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_0920"
    rin "\"I see. So really the only thing they share is the keys.\"" id a04_comn_02_723bb954

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0817"
    fumi "\"You could say that. They all have different ways of adjusting their volume.\"" id a04_comn_02_15fee643

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0921"
    rin "\"So why'd they ask you to play accompaniment to the Christmas recital? You play the piano, don't you?\"" id a04_comn_02_c914db14

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_0818"
    fumi "\"Yes, but we also played the organ in class a lot, ever since elementary school.\"" id a04_comn_02_8eac4d99

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_0922"
    rin "\"So you'll be good?\"" id a04_comn_02_bd50e4ab

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0819"
    fumi "\"I am a little worried since it's my first time playing a non-electric organ, so I got permission to practice after class.\"" id a04_comn_02_1db672b7

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0923"
    rin "\"Yuck, that sounds like a lot of work...\"" id a04_comn_02_507cbd05

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0820"
    fumi "\"But it's a rare opportunity, so—\"" id a04_comn_02_5cfbebeb

    play sound organ01

    show fumi 2 lg school d with dict_dissolve_25

    "The discordant sound of the organ interrupted their conversation."

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0924"
    rin "\"That was you, Hina? That scared me...\"" id a04_comn_02_7f80698f

    show fumi 2 lg school b with dict_dissolve_25

    stop sound fadeout 1.0

    $ side_image = "hina 1 side school a"

    voice "HIN_0973"
    hina "\"I wanted to know what it sounded like.\"" id a04_comn_02_9bf96485

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0925"
    rin "\"You've heard it at the entrance ceremony and church services before, haven't you?\"" id a04_comn_02_9f91f738

    $ side_image = "hina 1 side school h"

    voice "HIN_0974"
    hina "\"Well, yeah, but you just want to try it yourself, don't you? It didn't make much noise, though.\"" id a04_comn_02_8d6d3f10

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0821"
    fumi "\"Oh, you have to step on the pedals.\"" id a04_comn_02_36b48841

    "Fumi slid onto the bench next to Hina and began playing."

    hide rin
    hide fumi
    with Dissolve(0.25)

    play sound organ02

    show rin 1 sm school e at pos_r2
    show hina 1 lg school k
    show fumi 1 lg school a at pos_l2
    with Dissolve(0.25)

    pause 7.0

    show hina 1 sm school l with dict_dissolve_25

    voice "HIN_0975"
    hina "\"Ohh~!\"" id a04_comn_02_01343b2d

    voice "RIN_0926"
    rin "\"Sounds great. I get why the chaplain asked you to do it.\"" id a04_comn_02_331b24e2

    stop sound fadeout 1.0

    show fumi 1 sm school d
    show hina 1 sm school a
    with Dissolve(0.25)

    voice "FUM_0822"
    fumi "\"Oh, those were just some random notes.\"" id a04_comn_02_b6a8f620

    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0976"
    hina "\"I'm kind of looking forward to the hymn recital now.\"" id a04_comn_02_77210f40

    show rin 1 sm school f with dict_dissolve_25

    voice "RIN_0927"
    rin "\"It should sound nice as long as you don't do any singing, Hina.\"" id a04_comn_02_2988179f

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0977"
    hina "\"What?!\"" id a04_comn_02_97330efa

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_0928"
    rin "\"I know. Why don't you get Asou to do some voice training with you?\"" id a04_comn_02_6f928382

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0823"
    fumi "\"Voice training?\"" id a04_comn_02_9fcd58ed

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0929"
    rin "\"You know, ah, ah, ah, ah, ah. I doubt Hina'll be any good at it, though.\"" id a04_comn_02_2f7fa450

    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0978"
    hina "\"I-I will, too!\"" id a04_comn_02_9aef927a

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0824"
    fumi "\"Want to try?\"" id a04_comn_02_d2408740

    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0979"
    hina "\"Yeah!\"" id a04_comn_02_5a092779

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0825"
    fumi "\"Okay, sing the same notes as the organ, then.\"" id a04_comn_02_d96da6bc

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0980"
    hina "\"Bring it on!\"" id a04_comn_02_ccc2e08b

    "Hina took a fighting pose."

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0826"
    fumi "\"Umm, you should probably relax more.\"" id a04_comn_02_e240e0a8

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0981"
    hina "\"Oh, right.\"" id a04_comn_02_ccd3920a

    play sound organ03

    show fumi 1 sm school a
    show hina 1 sm school h
    with dict_dissolve_25

    voice "HIN_0982"
    hina "\"Ah, ah, ah, ah, ah.\"" id a04_comn_02_a5d658b3

    stop sound fadeout 1.0

    show rin:
        "rin 1 sm school f" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0930"
    rin "\"Pfft.\"" id a04_comn_02_2d10aa0e

    show rin 1 sm school f:
        xoffset 0 yoffset 0
    with None

    "Rin snorted as Hina sang off-key, just as she expected."

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0827"
    fumi "\"Listen carefully.\"" id a04_comn_02_6144bf7c

    play sound organ03

    show hina 1 sm school g with dict_dissolve_25

    voice "HIN_0983"
    hina "\"Ah, ah, ah, ah, ah.\"" id a04_comn_02_de6d1716

    stop sound fadeout 1.0

    "It was even worse that time."

    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0984"
    hina "\"How's that!\"" id a04_comn_02_92e0e8db

    show rin 1 sm school i with dict_dissolve_25

    voice "RIN_0931"
    rin "\"Why do you look so proud?\"" id a04_comn_02_1d823586

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0985"
    hina "\"Huh? Didn't I do it?\"" id a04_comn_02_70121a5c

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0932"
    rin "\"She doesn't even realize she's off-key, huh... That's pretty bad.\"" id a04_comn_02_db93bd4e

    show hina:
        "hina 1 sm school l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0986"
    hina "\"Huh?\"" id a04_comn_02_fb7e1559

    show hina 1 sm school l:
        xoffset 0 yoffset 0
    with None

    "Hina turned around to Fumi, shocked."

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0828"
    fumi "\"Umm... your voice is very cute... If you practice, it'll be fine!\"" id a04_comn_02_7f741c06

    "A pained smile and a pumped arm."

    show hina:
        "hina 1 sm school h" with Dissolve(0.25)
        ShakeUji

    voice "HIN_0987"
    hina "\"Auuugh...\"" id a04_comn_02_57ea32e9

    show hina 1 sm school h:
        xoffset 0 yoffset 0
    with None

    "Hina couldn't hide her shock at the truth thrust in front of her."

    show fumi 1 sm school b with dict_dissolve_25

    if hina_fumi_score != 999:

        voice "FUM_0829"
        fumi "\"We can do your voice training at the same time as my organ practice, Natsume.\"" id a04_comn_02_b56e39d1
    else:


        voice "FUM_0830"
        fumi "\"We can do your voice training at the same time as my organ practice, Hina.\"" id a04_comn_02_8324b88e

    voice "HIN_0988"
    hina "\"Ugh... thank you.\"" id a04_comn_02_5fc89727

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5


    if route1 == 3:
        jump a04_cou3_02
    elif rin_hina_score > hina_fumi_score:
        jump a04_cou2_03
    else:
        jump a04_cou1_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
