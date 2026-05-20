label a04_cou2_01:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg01ca with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show fumi 1 lg pyjama a:
        zoom 0.81 xcenter 234 ycenter 861
    show rin 1 lg pyjama i:
        zoom 0.81 xcenter 724 ycenter 855
    show hina 1 lg pyjama c:
        zoom 0.81 xcenter 724 ycenter 951
    with Dissolve(0.25)

    voice "HIN_1243"
    hina "\"♪Nyaaa, nya nya nyaaa!\""

    "It was their usual post-dinner resting time, and Hina was nya-nya-ing as always."

    "The only thing different from usual was—"

    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "FUM_1057"
    fumi "\"Eheh, you two are so close.\""

    "—that Hina was seated between Rin's knees, leaning her back against her."

    show hina:
        "hina 1 lg pyjama b" with Dissolve(0.25)
        ShakeYes

    voice "HIN_1244"
    hina "\"Yeah♪\""

    show hina 1 lg pyjama b:
        xcenter 724 ycenter 951 xoffset 0 yoffset 0
    with None

    "Hina's smile took up her whole face."

    show rin 1 lg pyjama g with dict_dissolve_25

    voice "RIN_1024"
    rin "\"A-Ahahaha.\""

    "Rin's smile, on the other hand, was somewhat strained."

    show layer master:
        xcenter 0.5 ycenter 0.5 zoom 1.0 transform_anchor True
        easeout 1.0 zoom 1.33

    scene white with Dissolve(0.5)
    pause 1.0

    scene bg01ca_grayscale
    show rin 1 lg pyjama glasses k grayscale:
        xcenter 302 ycenter 1016
    show hina 1 lg pyjama k grayscale:
        xcenter 512 ycenter 981
    with Dissolve(0.25)
    pause 0.75

    play sound se521

    show rin:
        "rin 1 lg pyjama glasses j grayscale" with Dissolve(0.25)
        ShakeJump

    show hina:
        "hina 1 lg pyjama d grayscale" with Dissolve(0.25)
        ShakeJump

    $ side_image = "side/fumi_1_side_pyjama_d_grayscale.webp"

    voice "FUM_0671"
    fumi "\"I forgot my shampoo—\""

    show rin 1 lg pyjama glasses j grayscale:
        xoffset 0 yoffset 0
    show hina 1 lg pyjama d grayscale:
        xoffset 0 yoffset 0
    with None
    $ side_image = "side/fumi_2_side_pyjama_c_grayscale.webp"

    voice "FUM_0672"
    fumi "\"Oh my.\""

    hide rin
    hide hina
    with Dissolve(0.05)
    pause 0.2

    show rin 1 sm pyjama glasses j grayscale at pos_l:
        xcenter 252
    show hina 1 sm pyjama k grayscale:
        xcenter 462
    with dict_dissolve_25

    show fumi 1 sm pyjama b grayscale:
        alpha 0.0 xcenter 952
        easein 0.5 alpha 1.0 xcenter 852
    with Dissolve(0.25)
    pause 0.25

    show fumi 1 sm pyjama b grayscale:
        alpha 1.0 xcenter 852 ycenter 631
    with None

    voice "FUM_1058"
    fumi "\"...Am I interrupting something?\""

    show rin:
        ShakeSide

    voice "RIN_1025"
    rin "\"Umm, this is, uhh, well—\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show hina 1 sm pyjama a grayscale with dict_dissolve_25

    voice "HIN_1245"
    hina "\"Asou!\""

    "Hina's happy voice cut through Rin's mumbling."

    show hina 1 sm pyjama c grayscale with dict_dissolve_25

    voice "HIN_1246"
    hina "\"Rin feels the same way!\""

    show rin:
        ShakeSide

    voice "RIN_1026"
    rin "\"H-Hina?!\""

    show rin:
        xoffset 0 yoffset 0
    with None
    show fumi 1 sm pyjama c grayscale with dict_dissolve_25

    voice "FUM_1059"
    fumi "\"Umm... oh! Congratulations!\""

    show hina 1 sm pyjama a grayscale with dict_dissolve_25

    voice "HIN_1247"
    hina "\"Thank you!\""

    hide fumi
    hide hina
    with Dissolve(0.25)

    show hina 1 lg pyjama c grayscale
    show fumi 1 lg pyjama c grayscale at pos_r
    with Dissolve(0.25)

    show hina:
        ShakeJump2
    show fumi:
        ShakeJump2

    $ voice2("hina","HIN_1248","fumi","FUM_1060")
    hina_fumi "\"Yay! Heheheheh!\"\n\"Wow! Eheheheh!\"" (what_rest_indent=0)

    show hina:
        xoffset 0 yoffset 0
    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses g grayscale with dict_dissolve_25

    voice "RIN_1027"
    rin "\"Huh? What's going on?\""

    "Before Rin knew it, the other two were holding hands and jumping up and down together."

    "Rin was the only one left out of the happy atmosphere."

    show rin 1 sm pyjama glasses i grayscale with dict_dissolve_25

    voice "RIN_1028"
    rin "\"Umm, excuse me? What's with the energy in here?\""

    hide fumi
    hide hina
    with Dissolve(0.25)

    show fumi 1 sm pyjama b grayscale:
        xcenter 772
    show hina 1 sm pyjama c grayscale:
        xcenter 512
    with dict_dissolve_25

    voice "FUM_1061"
    fumi "\"I had a feeling Natsume liked you. Didn't I tell you that?\""

    show rin 1 sm pyjama glasses g grayscale with dict_dissolve_25

    voice "RIN_1029"
    rin "\"Huh? Yeah... You did, but...\""

    show fumi 1 sm pyjama c grayscale with dict_dissolve_25

    voice "FUM_1062"
    fumi "\"So I'm excited that you return her feelings!\""

    show hina 1 sm pyjama c grayscale with dict_dissolve_25

    voice "HIN_1249"
    hina "\"Oh, but we'll still be best friends, Asou!\""

    show fumi:
        ShakeYes

    voice "FUM_1063"
    fumi "\"Yes!\""

    show fumi:
        xoffset 0 yoffset 0
    with None
    show rin 1 sm pyjama glasses i grayscale with dict_dissolve_25

    voice "RIN_1030"
    rin "\"......\""

    show layer master:
        xcenter 0.5 ycenter 0.5 zoom 1.0 transform_anchor True
        easeout 1.0 zoom 1.15
    show white with bg_effect_08

    pause 0.25

    scene bg01ca

    show fumi 1 lg pyjama i:
        zoom 0.81 xcenter 234 ycenter 861
    show rin 1 lg pyjama g:
        zoom 0.81 xcenter 724 ycenter 855
    show hina 1 lg pyjama b:
        zoom 0.81 xcenter 724 ycenter 951
    with Dissolve(0.25)
    pause 0.75

    show hina 2 lg pyjama f with Dissolve(0.25)

    voice "HIN_1250"
    hina "\"Hey, Rin, how do you read this?\""

    "Hina turned her head back and looked up at Rin."

    "She was pointing at a page of the paperback she was reading."

    show rin 1 lg pyjama glasses a with dict_dissolve_25

    voice "RIN_1031"
    rin "\"That's 'head.'\""

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_1251"
    hina "\"Oh, so you can write 'head' this way, too.\""

    show fumi 2 lg pyjama d with dict_dissolve_25

    voice "FUM_1064"
    fumi "\"It's rare to see you reading, Natsume.\""

    show hina 1 lg pyjama a with dict_dissolve_25

    voice "HIN_1252"
    hina "\"Yeah, I'm borrowing one of Rin's favorites.\""

    "Oh, it's the book she was sneaking a peek at before."

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1253"
    hina "\"Rin, Rin. What about this one?\""

    show rin 1 lg pyjama glasses h with dict_dissolve_25

    voice "RIN_1032"
    rin "\"That's 'eyelid.'\""

    "Hina stared up at Rin."

    show rin 1 lg pyjama glasses i with dict_dissolve_25

    voice "RIN_1033"
    rin "\"What is it?\""

    show hina 2 lg pyjama g with dict_dissolve_25

    voice "HIN_1254"
    hina "\"You're so smart.\""

    "Her eyes sparkled with pure adoration."

    show rin 1 lg pyjama glasses g with dict_dissolve_25

    voice "RIN_1034"
    rin "\"Th... Thanks.\""

    show hina 2 lg pyjama f with dict_dissolve_25

    voice "HIN_1255"
    hina "\"?\""

    show rin:
        "rin 1 lg pyjama glasses i" with Dissolve(0.25)
        ShakeYes

    "With a little sigh, Rin slowly stroked Hina's head."

    show rin 1 lg pyjama glasses i:
        xcenter 724 ycenter 855 xoffset 0 yoffset 0
    with None
    show fumi 2 lg pyjama i with dict_dissolve_25

    voice "FUM_1065"
    fumi "\"Eheheheheh.\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_cou2_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
