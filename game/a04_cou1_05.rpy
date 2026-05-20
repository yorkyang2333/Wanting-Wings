label a04_cou1_05:

    scene bg08aa with Dissolve(0.5)
    pause 1.5

    scene bg06aa with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show fumi z3 2 lg school g at pos_l2_z3
    show rin z3 1 lg school b at pos_r2_z3
    show hina z3 1 lg school m
    with Dissolve(0.25)

    voice "RIN_0957"
    rin "\"Hina, you dropped some.\""

    show hina z3 1 lg school k with dict_dissolve_25

    voice "HIN_1086"
    hina "\"Huh? Oh... you're right.\""

    show hina:
        ShakeTameiki

    "Hina picked up the clump of rice on the pew and put it on the lid of her lunch box."

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0958"
    rin "\"You keep dropping stuff. Actually, haven't you been a little out of it since last night?\""

    voice "HIN_1087"
    hina "\"Huh? Have I...?\""

    show rin z3 1 lg school h with dict_dissolve_25

    voice "RIN_0959"
    rin "\"Oh, it's not your cold coming back, is it?\""

    "Rin reached out and touched Hina's forehead."

    show rin z3 1 lg school b with dict_dissolve_25

    voice "RIN_0960"
    rin "\"Hmm... Doesn't feel like you've got a fever.\""

    show hina:
        "hina z3 1 lg school d" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1088"
    hina "\"I-I'm full of vigor.\""

    show hina z3 1 lg school d:
        xoffset 0 yoffset 0
    with None

    "She flexed awkwardly."

    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0961"
    rin "\"Hina's acting weird, right, Asou?\""

    voice "FUM_0910"
    fumi "\"......\""

    "But Fumi was also acting strange; robotically moving her chopsticks between her food and her mouth and not looking at either of them."

    show rin z3 1 lg school b with dict_dissolve_25

    voice "RIN_0962"
    rin "\"Umm, Asou?\""

    show fumi:
        1.0
        "fumi 2 lg school g" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0911"
    fumi "\"...Huh?! Y-Yes, what is it?\""

    show fumi 2 lg school g:
        xoffset 0 yoffset 0
    with None

    "Fumi finally looked up when Rin waved a hand in front of her face."

    show rin z3 1 lg school h with dict_dissolve_25

    voice "RIN_0963"
    rin "\"...You're being weird, too.\""

    "Rin cocked her head, looking between the two girls."

    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0964"
    rin "\"You weren't like this before you went to your organ practice yesterday—\""

    stop music fadeout 1.0

    show rin z3 1 lg school e with dict_dissolve_25

    voice "RIN_0965"
    rin "\"Oh...\""

    pause 0.5

    scene black with bg_effect_09
    pause 0.5

    show bg06ba with bg_effect_10
    pause 0.5

    play music bgm02

    show fumi 2 lg school d with Dissolve(0.25)
    show fumi:
        ShakeJump

    voice "FUM_0912"
    fumi "\"Oh.\""

    show fumi:
        xoffset 0 yoffset 0
    with None

    "Fumi twisted, attempting to take the pose Hina had told her to, then stopped."

    show fumi:
        "fumi 2 lg school d" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 252
    show hina 1 lg school k at pos_r with dict_dissolve_25

    voice "HIN_1089"
    hina "\"What's wrong, Fumi?\""

    show fumi 2 lg school d:
        xcenter 252
    with None

    "Hina lowered her camera and ran over to Fumi worriedly."

    show fumi 1 lg school d with dict_dissolve_25

    voice "FUM_0913"
    fumi "\"...Umm, my bra seems to have become unhooked.\""

    show hina 1 lg school h with dict_dissolve_25

    voice "HIN_1090"
    hina "\"Oh, I thought you might have pulled a muscle.\""

    voice "FUM_0914"
    fumi "\"Aha, no, I'm fine. But this keeps happening lately...\""

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1091"
    hina "\"Maybe they don't fit anymore.\""

    show fumi 2 lg school f with Dissolve(0.25)
    show fumi:
        ShakeNo

    voice "FUM_0915"
    fumi "\"Ugh, maybe... I don't want them to get any bigger, though...\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina 1 lg school j with dict_dissolve_25

    voice "HIN_1092"
    hina "\"Pretty extravagant complaint if you ask me.\""

    show fumi 1 lg school g with dict_dissolve_25

    voice "FUM_0916"
    fumi "\"But the bigger the bra, the fewer cute ones there are, you know? The band in the back gets bigger and all that...\""

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1093"
    hina "\"Hmm?\""

    "She didn't seem to understand."

    show fumi 1 lg school h with Dissolve(0.25)
    show fumi:
        ShakeTameiki

    voice "FUM_0917"
    fumi "\"Mmph... Yeah, I have to take this off...\""


    show fumi:
        "fumi 1 lg school h" with Dissolve(0.25)
        ycenter 1021 xoffset 0 yoffset 0
        easein 0.5 ycenter 1145
    pause 0.5

    play sound se116a

    show fumi 1 lg school h:
        ycenter 1145 xoffset 0 yoffset 0
        ShakeYes

    "Fumi removed her jacket and hiked up the back of her shirt."

    show fumi 2 lg school d:
        ycenter 1145 xoffset 0 yoffset 0
    with dict_dissolve_25

    voice "FUM_0918"
    fumi "\"Oh, no pictures, please.\""

    show hina 2 lg school f with dict_dissolve_25

    voice "HIN_1094"
    hina "\"Okay, but can I watch?\""

    show fumi 1 lg school h with dict_dissolve_25

    voice "FUM_0919"
    fumi "\"Umm...\""

    "She couldn't resist Hina's eyes, sparkling with curiosity."

    show hina 1 lg school k with dict_dissolve_25

    voice "HIN_1095"
    hina "\"I see. So it takes all the stuff under your arms and brings it to the front, too.\""

    show fumi 1 lg school j with Dissolve(0.25)
    show fumi:
        ycenter 1145
        ShakeSide

    voice "FUM_0920"
    fumi "\"...Ugh.\""

    show fumi:
        ycenter 1145 xoffset 0 yoffset 0
    with None

    "Hina's innocent words pierced Fumi's weak point once more."

    if persistent.dpatch:
        jump a04_cou1_05_d
    else:
        stop music fadeout 1.0
        stop sound fadeout 1.0
        scene black with Dissolve(0.5)
        pause 3.5
        "........."
        "......"
        window hide

label rp_scene01_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 2.0
    window auto

    $ renpy.end_replay()

    scene bg06aa with bg_effect_10
    pause 0.5

    play music bgm01

    show fumi z3 2 lg school g at pos_l2_z3
    show rin z3 1 lg school h at pos_r2_z3
    show hina z3 1 lg school d
    with Dissolve(0.25)

    voice "RIN_0966"
    rin "\"......\""

    show hina z3 1 lg school l with dict_dissolve_25

    voice "HIN_1152"
    hina "\"Wh-What?\""

    show rin z3 1 lg school h with dict_dissolve_25

    voice "RIN_0967"
    rin "\"Nothing~\""

    show fumi z3 1 lg school d with Dissolve(0.25)
    show fumi:
        ShakeJump

    voice "FUM_0976"
    fumi "\"Ch-Christmas is coming up soon, isn't it?\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show hina:
        "hina z3 1 lg school d" with Dissolve(0.25)
        ShakeJump

    voice "HIN_1153"
    hina "\"S-Sure is~ And you know what Christmas means: Jingle Bells!\""

    show hina z3 1 lg school d:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school a with dict_dissolve_25

    voice "RIN_0968"
    rin "\"You know what I've heard is that lately young people get up to all sorts of debauchery around Christmas time~\""

    show hina:
        "hina z3 1 lg school l" with Dissolve(0.25)
        ShakeSide

    voice "HIN_1154"
    hina "\"Erk.\""

    show hina z3 1 lg school l:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school f with dict_dissolve_25

    voice "RIN_0969"
    rin "\"Hm? Something wrong?\""

    show hina z3 1 lg school g with dict_dissolve_25

    voice "HIN_1155"
    hina "\"Th-That's right, debauchery is no good!\""

    "Her heart's not in it."

    voice "RIN_0970"
    rin "\"And any scoundrels engaging in such activities in a holy place such as the chapel...\""

    show fumi:
        "fumi z3 1 lg school h" with Dissolve(0.25)
        ShakeSide

    voice "FUM_0977"
    fumi "\"Erk.\""

    show fumi z3 1 lg school h:
        xoffset 0 yoffset 0
    with None

    voice "RIN_0971"
    rin "\"...will probably receive harsh punishment from any angels watching. Wouldn't you say, Hina?\""

    show hina:
        "hina z3 1 lg school d" with Dissolve(0.25)
        ShakeJump

    voice "HIN_1156"
    hina "\"I-It's exactly as you say, Rin!\""

    show hina z3 1 lg school d:
        xoffset 0 yoffset 0
    with None

    "Yet again, there was no sincerity."

    show rin z3 1 lg school b with dict_dissolve_25

    voice "RIN_0972"
    rin "\"Say, Asou—\""

    show fumi z3 1 lg school k with Dissolve(0.25)

    show fumi:
        xoffset 0
        ease 0.05 xoffset 3
        ease 0.05 xoffset 0
        repeat 20

    voice "FUM_0978"
    fumi "\"I'm sorry, I'm sorry, I'm sorry...\""

    show fumi:
        xoffset 0
    with None

    show rin z3 1 lg school i with dict_dissolve_25

    voice "RIN_0973"
    rin "\"Crap... what are these adorable creatures?\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
