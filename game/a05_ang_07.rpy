label a05_ang_07:

    scene white with Dissolve(0.5)
    pause 1.6



    show ang_07:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg06aa_grayscale with Dissolve(0.375)
    pause 1.125

    play sound se102c

    show rin z3 1 lg school a grayscale
    show hina z3 1 lg school h grayscale at pos_r2_z3
    show fumi z3 1 lg school a grayscale at pos_l2_z3
    with Dissolve(0.25)

    show hina:
        ShakeYes

    voice "HIN_0331"
    hina "\"O Lord! I'll give you the best part of my lunch, so please give me a miracle!\"" id a05_ang_07_0f26f398

    show hina:
        xoffset 0 yoffset 0
    with None
    show rin z3 1 lg school g grayscale with dict_dissolve_25

    voice "RIN_0289"
    rin "\"You resorted to that real quick.\"" id a05_ang_07_0d802525

    show fumi z3 1 lg school d grayscale with dict_dissolve_25

    voice "FUM_0259"
    fumi "\"I don't think you're supposed to clap like that at a church...\"" id a05_ang_07_30cc27f5

    hide rin
    hide fumi
    hide hina
    with Dissolve(0.25)

    play music bgm05

    "I listened to Hina's plea from the pulpit, my chin in my hands."

    "I was just listening, of course. There was nothing I could do for her."

    "On the plate in front of the cross was a selection of delicacies hand-picked from Hina's lunch."

    "This is quite an offering."

    "...But what am I supposed to do with it?"

    "I turned around and looked up at whoever it was depicted in the stained glass."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a05_ang_08
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
