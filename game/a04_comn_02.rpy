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
    rin "\"Pianos and organs aren't the same?\""

    "Rin asked Fumi, closing the lid of her lunch box."

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0814"
    fumi "\"Ah, they're similar but there are a lot of differences, too. A piano is a string instrument, and an organ is a wind instrument.\""

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0919"
    rin "\"Hm...\""

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0815"
    fumi "\"A hammer hits strings in a piano, but in an organ, it's air passing through pipes.\""

    "Fumi went on as Rin gave her an uncomprehending look."

    show fumi 2 lg school b with dict_dissolve_25

    voice "FUM_0816"
    fumi "\"The organ here is a reed organ, so it makes sound by vibrating air created with the pedals against brass reeds.\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_0920"
    rin "\"I see. So really the only thing they share is the keys.\""

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0817"
    fumi "\"You could say that. They all have different ways of adjusting their volume.\""

    show rin 1 lg school a with dict_dissolve_25

    voice "RIN_0921"
    rin "\"So why'd they ask you to play accompaniment to the Christmas recital? You play the piano, don't you?\""

    show fumi 1 lg school a with dict_dissolve_25

    voice "FUM_0818"
    fumi "\"Yes, but we also played the organ in class a lot, ever since elementary school.\""

    show rin 1 lg school h with dict_dissolve_25

    voice "RIN_0922"
    rin "\"So you'll be good?\""

    show fumi 1 lg school b with dict_dissolve_25

    voice "FUM_0819"
    fumi "\"I am a little worried since it's my first time playing a non-electric organ, so I got permission to practice after class.\""

    show rin 1 lg school i with dict_dissolve_25

    voice "RIN_0923"
    rin "\"Yuck, that sounds like a lot of work...\""

    show fumi 2 lg school c with dict_dissolve_25

    voice "FUM_0820"
    fumi "\"But it's a rare opportunity, so—\""

    play sound organ01

    show fumi 2 lg school d with dict_dissolve_25

    "The discordant sound of the organ interrupted their conversation."

    show rin 1 lg school e with dict_dissolve_25

    voice "RIN_0924"
    rin "\"That was you, Hina? That scared me...\""

    show fumi 2 lg school b with dict_dissolve_25

    stop sound fadeout 1.0

    $ side_image = "hina 1 side school a"

    voice "HIN_0973"
    hina "\"I wanted to know what it sounded like.\""

    show rin 1 lg school b with dict_dissolve_25

    voice "RIN_0925"
    rin "\"You've heard it at the entrance ceremony and church services before, haven't you?\""

    $ side_image = "hina 1 side school h"

    voice "HIN_0974"
    hina "\"Well, yeah, but you just want to try it yourself, don't you? It didn't make much noise, though.\""

    show fumi 2 lg school d with dict_dissolve_25

    voice "FUM_0821"
    fumi "\"Oh, you have to step on the pedals.\""

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
    hina "\"Ohh~!\""

    voice "RIN_0926"
    rin "\"Sounds great. I get why the chaplain asked you to do it.\""

    stop sound fadeout 1.0

    show fumi 1 sm school d
    show hina 1 sm school a
    with Dissolve(0.25)

    voice "FUM_0822"
    fumi "\"Oh, those were just some random notes.\""

    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0976"
    hina "\"I'm kind of looking forward to the hymn recital now.\""

    show rin 1 sm school f with dict_dissolve_25

    voice "RIN_0927"
    rin "\"It should sound nice as long as you don't do any singing, Hina.\""

    show hina:
        "hina 1 sm school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0977"
    hina "\"What?!\""

    show hina 1 sm school f:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm school e with dict_dissolve_25

    voice "RIN_0928"
    rin "\"I know. Why don't you get Asou to do some voice training with you?\""

    show fumi 1 sm school e with dict_dissolve_25

    voice "FUM_0823"
    fumi "\"Voice training?\""

    show rin 1 sm school a with dict_dissolve_25

    voice "RIN_0929"
    rin "\"You know, ah, ah, ah, ah, ah. I doubt Hina'll be any good at it, though.\""

    show hina:
        "hina 1 sm school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_0978"
    hina "\"I-I will, too!\""

    show hina 1 sm school d:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0824"
    fumi "\"Want to try?\""

    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0979"
    hina "\"Yeah!\""

    show fumi 1 sm school a with dict_dissolve_25

    voice "FUM_0825"
    fumi "\"Okay, sing the same notes as the organ, then.\""

    show hina 1 sm school f with dict_dissolve_25

    voice "HIN_0980"
    hina "\"Bring it on!\""

    "Hina took a fighting pose."

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0826"
    fumi "\"Umm, you should probably relax more.\""

    show hina 1 sm school a with dict_dissolve_25

    voice "HIN_0981"
    hina "\"Oh, right.\""

    play sound organ03

    show fumi 1 sm school a
    show hina 1 sm school h
    with dict_dissolve_25

    voice "HIN_0982"
    hina "\"Ah, ah, ah, ah, ah.\""

    stop sound fadeout 1.0

    show rin:
        "rin 1 sm school f" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0930"
    rin "\"Pfft.\""

    show rin 1 sm school f:
        xoffset 0 yoffset 0
    with None

    "Rin snorted as Hina sang off-key, just as she expected."

    show fumi 1 sm school b with dict_dissolve_25

    voice "FUM_0827"
    fumi "\"Listen carefully.\""

    play sound organ03

    show hina 1 sm school g with dict_dissolve_25

    voice "HIN_0983"
    hina "\"Ah, ah, ah, ah, ah.\""

    stop sound fadeout 1.0

    "It was even worse that time."

    show hina 1 sm school b with dict_dissolve_25

    voice "HIN_0984"
    hina "\"How's that!\""

    show rin 1 sm school i with dict_dissolve_25

    voice "RIN_0931"
    rin "\"Why do you look so proud?\""

    show hina 1 sm school k with dict_dissolve_25

    voice "HIN_0985"
    hina "\"Huh? Didn't I do it?\""

    show rin 1 sm school g with dict_dissolve_25

    voice "RIN_0932"
    rin "\"She doesn't even realize she's off-key, huh... That's pretty bad.\""

    show hina:
        "hina 1 sm school l" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0986"
    hina "\"Huh?\""

    show hina 1 sm school l:
        xoffset 0 yoffset 0
    with None

    "Hina turned around to Fumi, shocked."

    show fumi 1 sm school d with dict_dissolve_25

    voice "FUM_0828"
    fumi "\"Umm... your voice is very cute... If you practice, it'll be fine!\""

    "A pained smile and a pumped arm."

    show hina:
        "hina 1 sm school h" with Dissolve(0.25)
        ShakeUji

    voice "HIN_0987"
    hina "\"Auuugh...\""

    show hina 1 sm school h:
        xoffset 0 yoffset 0
    with None

    "Hina couldn't hide her shock at the truth thrust in front of her."

    show fumi 1 sm school b with dict_dissolve_25

    if hina_fumi_score != 999:

        voice "FUM_0829"
        fumi "\"We can do your voice training at the same time as my organ practice, Natsume.\""
    else:


        voice "FUM_0830"
        fumi "\"We can do your voice training at the same time as my organ practice, Hina.\""

    voice "HIN_0988"
    hina "\"Ugh... thank you.\""

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
