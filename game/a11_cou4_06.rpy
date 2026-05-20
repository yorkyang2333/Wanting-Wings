label a11_cou4_06:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_06:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg09aa with Dissolve(0.25)
    pause 0.75

    "Sachiko had Miyako wait in the hall while she got ready for snow shoveling in her room."

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_0239"
    sachiko "\"Is it done snowing?\""

    $ side_image = "miyako 1 side school_a b"

    voice "2MI_0389"
    miyako "\"Yes, it was finished by the time I got back. It's clear out now.\""

    show sachiko 1 lg outfit i with dict_dissolve_25

    voice "2SA_0240"
    sachiko "\"We won't need slickers, then. Let's see...\""

    show sachiko 2 lg outfit c with Dissolve(0.25)

    play sound se_2s_j044
    pause 1.0

    show sachiko 2 lg outfit d with dict_dissolve_25

    voice "2SA_1019"
    sachiko "\"......\""

    "She opened up a drawer and picked up a scarf that she found inside."

    pause 0.5

    window hide
    scene white with Dissolve(0.3)
    pause 0.1

    show a11_cou4_06_grayscale01 at truecenter:
        alpha 0.0 zoom 1.12
        parallel:
            linear 0.3 alpha 1.0
        parallel:
            easein 0.3 zoom 1.0
        2.0
        parallel:
            linear 0.3 alpha 0.0
        parallel:
            easein 0.3 zoom 1.12

    pause 3.6

    scene bg09aa
    show sachiko 2 lg outfit c
    with Dissolve(1.0)

    pause 1.0

    voice "2SA_1020"
    sachiko "\"......\""

    $ side_image = "miyako 1 side school_a e"

    voice "2MI_0390"
    miyako "\"Does the snow get deeper than this in this area?\""

    show sachiko 2 lg outfit d with Dissolve(0.5)

    voice "2SA_0127"
    sachiko "\".........\""

    show sachiko 2 lg outfit a with Dissolve(0.25)

    pause 0.5

    hide sachiko with dict_dissolve_50

    "Looking down at the scarf, she seemed to go back and forth on something for a moment before taking it and leaving the room."

    $ miyako_scarf = "_scarf"

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_07
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
