label a05_ang_13:

    scene white with Dissolve(0.5)
    pause 1.6



    show ang_13:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    play music bgm03

    scene ev03e_grayscale with Dissolve(0.375)
    pause 1.625

    voice "SYO_0223"
    sachiko "\"What'd you think of my three girls? Pretty cute, right?\"" id a05_ang_13_cb293f9c

    "Sachiko leaned against the fence and winked at me."

    voice "SYO_0224"
    sachiko "\"Well, you ready to get rid of those wings?\"" id a05_ang_13_ea01f171

    "She was full of confidence as she asked."

    "I am ready."

    "I'll discard eternity in order to make {i}my own{/i} history."

    show ev03e_grayscale as ev03e_grayscale2:
        alpha 1.0 xcenter 0.5 ycenter 0.5 zoom 1.0 transform_anchor True
        easeout 1.0 alpha 0.0 zoom 1.33

    scene white with Dissolve(1.0)
    pause 1.5

    scene ev03d
    show ev03d as ev03d2:
        alpha 1.0 xcenter 0.5 ycenter 0.5 zoom 1.33 transform_anchor True
        linear 2.5 alpha 0.0 zoom 1.0

    show white:
        alpha 1.0
        linear 2.5 alpha 0.0
    pause 2.5

    hide ev03d2
    hide white
    with None

    "I alighted into a world of full color."

    voice "SYO_0225"
    sachiko "\"Table for one, right this way~♪\"" id a05_ang_13_f6f1bcbc

    "Sachiko welcomed me with wide-open arms like she was this world's representative."

    voice "SYO_0226"
    sachiko "\"Oh, but I'm not giving you any of those girls.\"" id a05_ang_13_9bd86e1d

    "That's a little disappointing. But it's not as if they belong to you."

    voice "SYO_0227"
    sachiko "\"Come on down. You're in heaven now.\"" id a05_ang_13_8797cadc

    pause 1.0

    stop music fadeout 3.0
    stop sound fadeout 3.0
    scene white with Dissolve(0.75)
    pause 2.25

    call staff_d from _call_staff_d

    jump a05_ang_14
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
