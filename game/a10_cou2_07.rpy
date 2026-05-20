label a10_cou2_07:

    scene bg04aa with Dissolve(0.5)
    pause 1.5

    play sound se030a
    pause 1.0

    show rin:
        "rin 1 lg school i flat"
        alpha 0.0 ycenter 1116
        easein 0.25 alpha 1.0 ycenter 1016

    voice "2RI_1364"
    rin "\"We promised!\""

    show rin 1 lg school i:
        alpha 1.0 ycenter 1016
    with None

    "Rin shot up from her seat as soon as the bell for the end of fifth period rang."

    hide rin with dict_dissolve_25

    "She strode over to Miyako's desk."

    play music bgm08 fadein 1.0

    show miyako z4 2 lg school a:
        xcenter 298
    show rin z4 1 lg school h:
        xcenter 726
    with dict_dissolve_25

    voice "2RI_1365"
    rin "\"But she's not here!\""

    show miyako z4 1 lg school_b e with dict_dissolve_25

    voice "2MI_1038"
    miyako "\"That's true, I haven't seen her since lunch.\""

    show rin z4 2 lg school d with dict_dissolve_25

    voice "2RI_1366"
    rin "\"She ran away again...\""

    show miyako z4 1 lg school_b g with dict_dissolve_25

    voice "2MI_1039"
    miyako "\"Huh? But why—\""

    show rin z4 2 lg school a with dict_dissolve_25

    voice "2RI_1367"
    rin "\"Mikoyan, can you tell the teacher I left early? I'm gonna go look for her.\""

    show miyako z4 1 lg school_a e with dict_dissolve_25

    voice "2MI_1040"
    miyako "\"Umm, sure, I don't mind, but...\""

    show rin z4 1 lg school i with dict_dissolve_25

    voice "2RI_1368"
    rin "\"...That dumb lost dog!\""

    hide rin with Dissolve(0.25)
    pause 1.0

    "She spun around and this time strode toward the classroom door."

    if routes_cleared >= 2:
        jump a10_cou2_07_a
    else:
        jump a10_cou2_07_end

label a10_cou2_07_a:

    show miyako:
        "miyako z4 1 lg school_a a" with Dissolve(0.25)
        ShakeYes

    voice "2MI_1041"
    miyako "\"...Right.\""

    show miyako z4 1 lg school_a a:
        xoffset 0 yoffset 0
    with None

    "Miyako stared blankly after Rin for a moment, then nodded to herself and started quickly packing her things away in her bag."

    hide miyako with Dissolve(0.25)

    pause 1.0

    "She stood up and said to the girl in the seat next to her,"

    $ side_image = "miyako 1 side school_a j"

    voice "2MI_1042"
    miyako "\"I'm sorry, but could you tell the teacher that Natsume, Ogata, and Takaoka all left early?\""

label a10_cou2_07_end:

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_comn_02
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
