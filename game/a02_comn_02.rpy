label a02_comn_02:


    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg06aa with Dissolve(0.25)
    pause 0.75

    play music bgm02

    show rin z3 1 lg school a
    show hina z3 1 lg school b at pos_r2_z3
    show fumi z3 1 lg school a at pos_l2_z3
    with Dissolve(0.25)

    "A small plate with a rice ball and some side dishes on it sat in front of the cross."

    "And the three girls were eating lunch again, lesson not learned."

    show rin z3 1 lg school b with dict_dissolve_25

    voice "RIN_0279"
    rin "\"Who knows what's on the English exam~?\"" id a02_comn_02_e589332f

    show fumi z3 1 lg school e with dict_dissolve_25

    voice "FUM_0249"
    fumi "\"Huh? It was all on the board in class just now, wasn't it?\"" id a02_comn_02_ab7460fd

    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0280"
    rin "\"Yeah, I was sleeping.\"" id a02_comn_02_2541d030

    show hina z3 1 lg school j with dict_dissolve_25

    voice "HIN_0323"
    hina "\"I can't stand the fact that your grades are good when you don't put any effort in.\"" id a02_comn_02_f86e9f25

    show fumi z3 1 lg school b with dict_dissolve_25

    voice "FUM_0250"
    fumi "\"There's nothing you're good at or bad at?\"" id a02_comn_02_87547c9a

    show rin z3 1 lg school b with dict_dissolve_25

    voice "RIN_0281"
    rin "\"Not really. I guess I like English, though.\"" id a02_comn_02_490bd2c4

    "Yet she sleeps in class."

    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0282"
    rin "\"What about you, Asou?\"" id a02_comn_02_3c59d7e5

    show fumi z3 1 lg school d with dict_dissolve_25

    voice "FUM_0251"
    fumi "\"I guess I'm better at the humanities? I'm pretty good at classic and modern Japanese, but I'm not great at math and physics.\"" id a02_comn_02_37bf8b5b

    show rin z3 1 lg school c with dict_dissolve_25

    voice "RIN_0283"
    rin "\"And you're good at arithmetic, right, Hina?\"" id a02_comn_02_373bdaae

    show hina:
        "hina z3 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0324"
    hina "\"Don't call it arithmetic.\"" id a02_comn_02_3fa4cf9a

    show hina z3 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg school a with dict_dissolve_25

    voice "FUM_0252"
    fumi "\"Natsume's the science type.\"" id a02_comn_02_66d8e3f7

    show hina:
        "hina z3 1 lg school h" with Dissolve(0.25)
        ShakeTameiki

    voice "HIN_0325"
    if persistent.dpatch:
        hina "\"Well, only a little bit. Honestly, I'm just not very good at school.\"" id a02_comn_02_dc73d14c
    else:
        hina "\"Well, only a little bit. Honestly, I'm just not very good at academia.\"" id a02_comn_02_4455cfe8

    show hina z3 1 lg school h:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0284"
    rin "\"'Cause you're an idiot?\"" id a02_comn_02_245ba198

    show hina z3 1 lg school f with dict_dissolve_25

    voice "HIN_0326"
    hina "\"Choose your words more carefully!\"" id a02_comn_02_b8f02058

    show rin z3 1 lg school e with dict_dissolve_25

    voice "RIN_0285"
    rin "\"Oh, Asou, can I copy the exam schedule off you in addition to what they cover?\"" id a02_comn_02_4ae52a50

    show fumi z3 1 lg school c with dict_dissolve_25

    voice "FUM_0253"
    fumi "\"I can give you the schedule right now.\"" id a02_comn_02_93068944

    play sound se013a

    "Fumi took a journal out of her pocket and flipped open a page to show to Rin."

    show rin z3 1 lg school b with Dissolve(0.25)
    show rin:
        ShakeYes

    voice "RIN_0286"
    rin "\"Hmm. Starting with math and ending on English, eh?\"" id a02_comn_02_38ff2656

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina z3 1 lg school d" with Dissolve(0.25)
        ShakeUji

    voice "HIN_0327"
    hina "\"The one I'm worst at is on the last day. The whole three days is going to be miserable.\"" id a02_comn_02_e437a656

    show hina z3 1 lg school d:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg school d with dict_dissolve_25

    voice "FUM_0254"
    fumi "\"Look at it this way: you have the most time to study for that one.\"" id a02_comn_02_960fb0a9

    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0287"
    rin "\"And you've gotta take the math exam first thing, Asou.\"" id a02_comn_02_7724b154

    show hina z3 1 lg school h
    show fumi z3 1 lg school h
    with Dissolve(0.25)

    show fumi:
        yoffset 0
        ease 0.4 yoffset 30
        ease 0.4 yoffset 0
    show hina:
        yoffset 0
        ease 0.4 yoffset 50
        ease 0.4 yoffset 0

    $ voice2("hina","HIN_0328","fumi","FUM_0255")
    hina_fumi "\"Haahh...\""

    show rin z3 1 lg school c with dict_dissolve_25

    voice "RIN_0288"
    rin "\"Umm, let me know if there's something I can help with.\"" id a02_comn_02_2adb3b97

    show fumi z3 1 lg school i with dict_dissolve_25

    voice "FUM_0256"
    fumi "\"Oh, that's reassuring.\"" id a02_comn_02_4c7b61b8

    show hina:
        "hina z3 1 lg school f" with Dissolve(0.25)
        ShakeJump

    voice "HIN_0329"
    hina "\"You've got the basics down, so you'll be fine, Asou!\"" id a02_comn_02_8e03787c

    show hina z3 1 lg school f:
        xoffset 0 yoffset 0
    with None
    show fumi z3 1 lg school e with dict_dissolve_25

    voice "FUM_0257"
    fumi "\"Wawah?\"" id a02_comn_02_164a7e4d

    show hina z3 1 lg school d with dict_dissolve_25

    voice "HIN_0330"
    hina "\"I don't even have that, so what am I supposed to do?!\"" id a02_comn_02_4718120b

    show fumi z3 1 lg school d with dict_dissolve_25

    voice "FUM_0258"
    fumi "\"Umm, hope that you guess right?\"" id a02_comn_02_26a6d891

    play sound se102c

    show hina:
        "hina z3 1 lg school h" with Dissolve(0.25)
        ShakeYes

    voice "HIN_0331"
    hina "\"O Lord! I'll give you the best part of my lunch, so please give me a miracle!\"" id a02_comn_02_0f26f398

    show hina z3 1 lg school h:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school g with dict_dissolve_25

    voice "RIN_0289"
    rin "\"You resorted to that real quick.\"" id a02_comn_02_0d802525

    show fumi z3 1 lg school d with dict_dissolve_25

    voice "FUM_0259"
    fumi "\"I don't think you're supposed to clap like that in a church...\"" id a02_comn_02_93306398

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a02_comn_03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
