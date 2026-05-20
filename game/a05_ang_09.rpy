label a05_ang_09:

    scene white with Dissolve(0.5)
    pause 1.6



    show ang_09:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg02ba_grayscale with Dissolve(0.375)
    pause 1.125

    play music bgm05

    show rin 1 sm school g grayscale:
        xcenter 928
    show fumi 1 sm school e grayscale:
        xcenter 584
    show hina 1 sm school f grayscale:
        xcenter 764
    show sachiko 1 grayscale sm outfit i:
        xcenter 188
    with Dissolve(0.25)

    voice "SYO_0099"
    sachiko "\"Hmm...\""

    show fumi 1 sm school h grayscale with dict_dissolve_25

    voice "FUM_0482"
    fumi "\"...Do you know what it is?\""

    show sachiko 1 grayscale sm outfit g with dict_dissolve_25

    voice "SYO_0100"
    sachiko "\"Nope~ Teehee!\""

    "Sachiko spun the feather around so that I could see it."

    "Did that really come from me?"

    "A picture is one thing, but I can't believe I could leave behind such concrete evidence of myself."

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg01ba_grayscale with Dissolve(0.25)
    pause 1.25

    show rin 1 sm school b grayscale:
        xcenter 928
    show fumi 1 sm school a grayscale:
        xcenter 584
    show hina 1 sm school j grayscale:
        xcenter 764
    show sachiko 1 grayscale sm outfit j:
        xcenter 188
    with Dissolve(0.25)

    voice "SYO_0104"
    sachiko "\"If there are no signs of infiltration from outside, then that means... the culprit is among us! Bam!\""

    "Eep."

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg05ba_grayscale with Dissolve(0.25)
    pause 1.25

    show sachiko 1 grayscale lg outfit cigarette i at pos_l2 with Dissolve(0.25)

    $ side_image = "side/hina_1_side_school_g_grayscale.webp"

    voice "HIN_0657"
    hina "\"We are not! Get lost already!!\""

    play sound se118c

    show sachiko:
        "sachiko 1 grayscale lg outfit cigarette h" with Dissolve(0.25)
        ShakeSide
    pause 0.25

    show sachiko 1 grayscale lg outfit cigarette h:
        xcenter 172 xoffset 0 yoffset 0
        easein 0.25 xcenter 512

    "The girls chased Sachiko out, and I followed her into the hallway."

    show sachiko 1 grayscale lg outfit cigarette h:
        xcenter 512
    with None

    "......"

    show sachiko:
        "sachiko 1 grayscale lg outfit cigarette g" with Dissolve(0.25)
        ShakeYes

    voice "SYO_0207"
    sachiko "\"Ta-dah♪\""

    show sachiko 1 grayscale lg outfit cigarette g:
        xoffset 0 yoffset 0
    with None

    "Oh."

    show sachiko 1 grayscale lg outfit cigarette a with dict_dissolve_25

    voice "SYO_0208"
    sachiko "\"I switched it.\""

    "Sachiko took my feather out of her pocket in the hallway."

    voice "SYO_0209"
    sachiko "\"They've got a goose feather in there now. I snatched one from Hina's down jacket.\""

    voice "2SA_0027"
    sachiko "\"So you lost a feather... Think that means you're getting closer to being human?\""

    show sachiko:
        "sachiko 1 grayscale lg outfit cigarette d" with Dissolve(0.25)
        ShakeTameiki

    voice "SYO_0210"
    sachiko "\"You should be careful from now on... Not that anyone should be able to see you.\""

    show sachiko 1 grayscale lg outfit cigarette d:
        xoffset 0 yoffset 0
    with None

    "Sachiko spun the feather around again."

    show sachiko 1 grayscale lg outfit cigarette a with dict_dissolve_25

    voice "SYO_0211"
    sachiko "\"Those girls are the only ones who can see this feather.\""

    "And you."

    show sachiko 1 grayscale lg outfit cigarette b with dict_dissolve_25

    voice "SYO_0212"
    sachiko "\"They're special.\""

    "Special?"

    voice "SYO_0213"
    sachiko "\"They even remember me...\""

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a05_ang_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
