label a03_cou2_07:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm02

    $ side_image = "fumi 2 side pyjama b"

    voice "FUM_0670"
    fumi "\"Okay, I'm going to go take my bath.\""

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0725"
    rin "\"Oh, okay.\""

    "Rin looked up from her book when Fumi called out from the entrance, bath set in hand."

    play sound se522

    "With Fumi gone, Rin and Hina were left alone in the room."

    show rin 2 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0726"
    rin "\"Hina, wanna go—\""

    "Hina had her head down at her desk, her headphones on. She didn't seem to have noticed Fumi leaving."

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0727"
    rin "\"...Oh.\""

    "Rin pouted, sensing that Hina wasn't listening."

    "........."

    stop music fadeout 3.0

    show rin:
        "rin 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeSide

    voice "RIN_0728"
    rin "\"Ahh, geez!\""

    show rin 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None

    "Rin scratched her head, letting out a frustrated exclamation."

    show rin 2 lg pyjama glasses d with dict_dissolve_25

    voice "RIN_0729"
    rin "\"...I hate this.\""

    "And she stood up."

    play music bgm05

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0730"
    rin "\"...I'm sorry. Maybe I've been taking it too far lately.\""

    "Rin spoke to the unlistening Hina."

    show rin 2 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0731"
    rin "\"I'm all twisted, so your purity is unusual to me. So... I don't know, I can't help wanting to tease you.\""

    voice "RIN_0732"
    rin "\"It's not like I'm making fun of you... I do it because... it's like, I admire you.\""

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0733"
    rin "\"You're so fiery, you know? At first, I didn't really like that...\""

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0734"
    rin "\"But at some point, it got kind of comfortable. Ah... I guess I kind of joke around too much for that to be obvious, though.\""

    show rin 2 lg pyjama glasses d with dict_dissolve_25

    voice "RIN_0735"
    rin "\"It's the first time I've ever been so close to someone.\""

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0736"
    rin "\"Messing around with you is really important to me. It's fun, and it makes me happy, and I don't ever want to ruin our relationship.\""

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0737"
    rin "\"So... I'm sorry. Can't we just fight like we usually do again?\""

    show rin 2 lg pyjama glasses e with dict_dissolve_25

    voice "RIN_0738"
    rin "\"—Yeah, right. I know you're not listening.\""

    "Hina still had her head down on her desk and her headphones on."

    show rin 1 lg pyjama glasses g with Dissolve(0.25)
    show rin:
        ShakeTameiki

    voice "RIN_0739"
    rin "\"Haah... why can't I just say it to your face? If I could just be a hundredth as honest as you...\""

    show rin:
        xoffset 0 yoffset 0
    with None

    "Rin squirmed."

    show rin 2 lg pyjama glasses c with dict_dissolve_25

    voice "RIN_0740"
    rin "\"It's only natural you'd hate a twisted person like—\""

    stop music fadeout 3.0

    "Her words stopped."

    show layer master:
        xcenter 0.5 ycenter 0.5 zoom 1.0 transform_anchor True
        easeout 1.0 zoom 1.33

    scene white with Dissolve(0.5)
    pause 1.0





    scene a03_cou2_07_grayscale01

    with Dissolve(0.25)
    pause 0.75

    voice "FUM_0669"
    fumi "\"Natsume likes you, Ogata.\""

    window hide

    show layer master:
        xcenter 0.5 ycenter 0.5 zoom 1.0 transform_anchor True
        easeout 1.0 zoom 1.15
    show white with bg_effect_08

    pause 0.25

    scene bg01ca
    show rin 2 lg pyjama glasses c
    with Dissolve(0.5)

    pause 2.0

    show rin 2 lg pyjama glasses a with dict_dissolve_25

    play sound se220c_100

    window auto

    voice "RIN_0741"
    rin "\"...Hina, do you...\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0742"
    rin "\"Like me?\""

    play sound se115a

    $ side_image = "hina 2 side pyjama headphones j"

    voice "HIN_0920"
    hina "\"I do!!\""

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        function LayerShake(20,20,0.5)
    $ persistent.layer_shaken = False

    voice "RIN_0743"
    rin "\"Wah?!\""

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    play sound se555

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        xcenter 512
        easein 0.25 xcenter 252
    show hina:
        "hina 2 lg pyjama h flat"
        alpha 0.0 xcenter 772 ycenter 1081
        easein 0.5 alpha 1.0 ycenter 981

    "Hina suddenly stood, ripping off her headphones and turning to Rin."

    show rin 1 lg pyjama glasses j:
        xcenter 252
    show hina 2 lg pyjama h:
        alpha 1.0 xcenter 772 ycenter 981
    with None

    play music bgm03

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0744"
    rin "\"Y-You were listening?\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0921"
    hina "\"The batteries ran out a minute ago.\""

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "RIN_0745"
    rin "\"...H-How much did you hear?\""

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0922"
    hina "\"From how you're all twisted...\""

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0746"
    rin "\"So... pretty much all of it.\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0923"
    hina "\".........\""

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "RIN_0747"
    rin "\"......\""

    "They both stood stock-still, eyes on the floor."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0748"
    rin "\"Hey...\""

    show hina 2 lg pyjama d with dict_dissolve_25

    "Rin spoke first, and Hina lifted her head."

    show rin 1 lg pyjama glasses b with dict_dissolve_25

    voice "RIN_0749"
    rin "\"Let me just ask one more time, you...?\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0924"
    hina "\"...Like you.\""

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "RIN_0750"
    rin "\"As a friend—\""

    show hina:
        "hina 2 lg pyjama i" with Dissolve(0.25)
        ShakeNo

    "Hina shook her head."

    show hina 2 lg pyjama i:
        xoffset 0 yoffset 0
    with None
    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0751"
    rin "\"As, like, someone you'd want to kiss...?\""

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0925"
    hina "\"...Yeah.\""

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_0752"
    rin "\"...Since when?\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0926"
    hina "\"When I saw you doing ballet, I realized you were really pretty, and my heart wouldn't stop pounding, and it hurt when I looked at you...\""

    "Choosing her words carefully, Hina went on hesitantly but earnestly."

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0927"
    hina "\"I thought it was weird to feel that way about another girl, but then I read your book and started to think maybe it wasn't...\""

    voice "HIN_0928"
    hina "\"Then, the other night, you almost kissed me, but you didn't, and you laughed so much about it...\""

    voice "HIN_0929"
    hina "\"When I thought about how I like you so much and you don't seem to think anything at all of me, I really wanted to cry...\""

    "Hina's eyes filled with tears, but she didn't look away."

    show rin 1 lg pyjama glasses j with dict_dissolve_25

    play sound se_bati

    show bati2:
        xcenter 292 ycenter 534

    pause 0.3

    show rin:
        ShakeSide

    voice "RIN_0753"
    rin "\"Waah, waah...\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0930"
    hina "\"?\""

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_0754"
    rin "\"Are you stupid? Are you stupid?\""

    show hina 2 lg pyjama e with dict_dissolve_25

    voice "HIN_0931"
    hina "\"...I'm not stupid.\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_0755"
    rin "\"C'mere!\""

    show hina:
        "hina 2 lg pyjama f" with Dissolve(0.25)
        xcenter 772
        easein 1.0 xcenter 512

    "Rin held her arms out and Hina walked forward obediently, despite the dumbfounded look on her face."

    show hina 2 lg pyjama f:
        xcenter 512
    with None

    show rin:
        "rin 1 lg pyjama glasses c" with Dissolve(0.25)
        xcenter 252
        easein 0.25 xcenter 302

    play sound se118a

    show hina 2 lg pyjama h with dict_dissolve_25

    voice "HIN_0932"
    hina "\"...Huh?!\""

    "Rin put her arms around Hina and squeezed."

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_0933"
    hina "\"...Do you like me too, Rin?\""

    show rin:
        "rin 1 lg pyjama glasses g" with Dissolve(0.25)
        ShakeUji

    voice "RIN_0756"
    rin "\"Umm, umm...\""

    show rin 1 lg pyjama glasses g:
        xoffset 0 yoffset 0
    with None

    "Instead of answering, Rin kissed her."

    show rin 1 lg pyjama glasses k with dict_dissolve_25

    voice "RIN_0757"
    rin "\"Mmh...\""

    show hina 1 lg pyjama k with dict_dissolve_25

    voice "HIN_0934"
    hina "\"...!\""

    stop music fadeout 1.0

    play sound se521

    show rin:
        "rin 1 lg pyjama glasses j" with Dissolve(0.25)
        ShakeJump
    show hina:
        "hina 1 lg pyjama d" with Dissolve(0.25)
        ShakeJump

    $ side_image = "fumi 2 side pyjama d"

    voice "FUM_0671"
    fumi "\"I forgot my shampoo—\""

    show rin 1 lg pyjama glasses j:
        xoffset 0 yoffset 0
    with None

    $ side_image = "fumi 2 side pyjama c"

    voice "FUM_0672"
    fumi "\"Oh my.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    scene chapter04
    with Dissolve(0.5)
    pause 1.5

    show chapter04b with Dissolve(1.5)
    pause 3.0

    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
