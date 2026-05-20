label a11_cou4_09:

    scene black with Dissolve(0.5)
    pause 1.5

    show white:
        alpha 0.0
        linear 2.0 alpha 1.0



    show chapter05_09:
        alpha 0.0 yoffset -40
        1.0
        linear 2.0 alpha 1.0 yoffset 0
    pause 6.1

    scene white with Dissolve(0.25)
    pause 0.75

    scene bg10bb with Dissolve(0.25)
    pause 0.75

    $ side_image = "sachiko 2 side outfit c"

    voice "2SA_1048"
    sachiko "\"......\""

    "The broadcasting room at dusk. Sachiko ran her finger over the desk after wiping it down."

    $ side_image = "sachiko 2 side outfit d"

    voice "2SA_1049"
    sachiko "\"Phew...\""

    play sound se_2s_h012

    "She folded up the cloth and sat down, satisfied."

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_1050"
    sachiko "\"I haven't missed a week in five years. That's pretty devoted of me, wouldn't you say?\""

    show sachiko 1 lg outfit b with dict_dissolve_25

    voice "2SA_1051"
    sachiko "\"...No, I guess I'm just doing it for myself.\""

    "Sachiko put her hand on the junk transceiver and spoke to it."

    show sachiko 2 lg outfit c with dict_dissolve_25

    voice "2SA_1052"
    sachiko "\"But this'll be the last time I come take care of this room.\""

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_1053"
    sachiko "\"I'm leaving. I'm not managing the dorm anymore, either. Not that I really know where I'm going, but...\""

    "It was like giving an update at a grave."

    show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_1054"
    sachiko "\"I'll make sure the principal has someone clean this room every so often.\""

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_1055"
    if persistent.dpatch:
        sachiko "\"It probably won't be weekly, but I'm sure they'll take care of it until they rebuild the school building. It won't end up like an abandoned grave.\"" id a11_cou4_09_acd7f8ce
    else:
        sachiko "\"It probably won't be weekly, but I'm sure they'll take care of it until they rebuild the campus building. It won't end up like an abandoned grave.\""

    show sachiko 2 lg outfit c with dict_dissolve_25

    voice "2SA_1056"
    sachiko "\"Sorry to tell you this so suddenly.\""

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_1057"
    sachiko "\"...I have to leave before she finishes her scarf.\""

    show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_1058"
    sachiko "\"I gave your scarf to her. Maybe it's supposed to be in exchange for that...\""

    show sachiko 2 lg outfit e with dict_dissolve_25

    voice "2SA_1059"
    sachiko "\"I found her knitting in the dark on the stairs at night. She said she didn't want to wake the other girls up in her room.\""

    show sachiko 2 lg outfit f with dict_dissolve_25

    voice "2SA_1060"
    sachiko "\"But the one who sleeps more than anyone else is staying up late doing something she's not used to. And who was it for? Yep, it was for me.\""

    show sachiko 2 lg outfit a with dict_dissolve_25

    voice "2SA_1061"
    sachiko "\"That's just not fair. It's so cunning. You think I'm going to fall for that bait—\""

    show sachiko 2 lg outfit d with dict_dissolve_25

    "........."

    "......"

    show sachiko 2 lg outfit j with dict_dissolve_25

    voice "2SA_1062"
    sachiko "\"...Being loved is scary.\""

    "She hung her head."

    play sound se_2s_f001
    pause 1.0

    show sachiko 2 lg outfit b with dict_dissolve_25

    voice "2SA_1063"
    sachiko "\"Who's there?\""

    $ side_image = "miyako 1 side school_a a"

    voice "2MI_1161"
    miyako "\"Miyako Takaoka. I'm here to return some equipment.\""

    show sachiko 1 lg outfit a with dict_dissolve_25

    voice "2SA_1064"
    sachiko "\"...Come in.\""

    "Sachiko raised her head and put on her usual face."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a11_cou4_10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
