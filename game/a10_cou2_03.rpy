label a10_cou2_03:

    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    play sound se521
    pause 1.0

    $ side_image = "hina 2 side school_scarf d"

    voice "2HI_1378"
    hina "\"We're back.\"" id a10_cou2_03_e6973efe

    "Hina and Rin returned to the dorm."

    "As they'd discussed earlier, Fumi and Miyako had broken off from them on the way, sending the two of them home on their own."

    $ side_image = "hina 2 side school_scarf f"

    voice "2HI_1379"
    hina "\"I wonder what Asou and Miyako have to talk about.\"" id a10_cou2_03_b0a9ee1c

    "Hina mused, turning on the air conditioner."

    $ side_image = "rin 1 side school_scarf f"

    voice "2RI_1323"
    rin "\"Maybe they have some planning to do for Valentine's Day.\"" id a10_cou2_03_385d0fb5

    $ side_image = "hina 2 side school_scarf e"

    voice "2HI_1380"
    hina "\"Hmm.\"" id a10_cou2_03_a7dfd349

    $ side_image = "rin 1 side school_scarf c"

    voice "2RI_1324"
    rin "\"But because of that, we've got some unexpected time alone, right?\"" id a10_cou2_03_3c5be411

    $ side_image = "hina 1 side school_scarf m"

    voice "2HI_1381"
    hina "\"I suppose so.\"" id a10_cou2_03_d101aeb5

    "Hina said curtly, removing her scarf."

    "In contrast to Rin's excitement, Hina seemed somehow distracted."

    $ side_image = "rin 1 side school_scarf h"

    voice "2RI_1325"
    rin "\"......\"" id a10_cou2_03_c66174d6

    "Rin took the collar out of her pocket and sidled up to Hina."

    show rin 1 lg school_scarf f at pos_r with dict_dissolve_25

    voice "2RI_1326"
    rin "\"Hiiinaaa?\"" id a10_cou2_03_4e9630b9

    "She said coaxingly and brought the collar up to Hina's neck, but..."

    show hina 2 lg school e at pos_l with dict_dissolve_25

    voice "2HI_1382"
    hina "\"......\"" id a10_cou2_03_39ddb896

    "Hina twisted to escape her grasp."

    show rin 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_1327"
    rin "\"Huh?\"" id a10_cou2_03_c557f162

    "Rin was left standing there blankly, collar in hand."

    show rin 1 lg school_scarf g with dict_dissolve_25

    voice "2RI_1328"
    rin "\"Umm, the collar...\"" id a10_cou2_03_aae76d90

    show hina 2 lg school f with dict_dissolve_25

    voice "2HI_1383"
    hina "\"You want to put it on?\"" id a10_cou2_03_70200251

    show rin 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_1329"
    rin "\"Well, I mean, haven't you been in kind of a bad mood lately? Things were kind of awkward on the way home... You didn't say much.\"" id a10_cou2_03_95a34908

    show hina 2 lg school d with dict_dissolve_25

    voice "2HI_1384"
    hina "\"......\"" id a10_cou2_03_00af5aa0

    show rin 2 lg school_scarf b with dict_dissolve_25

    voice "2RI_1330"
    rin "\"So, to make up...\"" id a10_cou2_03_392892cc

    "Rin held the collar out again."

    show hina 2 lg school h with dict_dissolve_25

    voice "2HI_1385"
    hina "\"......\"" id a10_cou2_03_686b5df5

    "Hina shook her head."

    show rin 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_1331"
    rin "\"Huh? You don't want to?\"" id a10_cou2_03_eb6f2a54

    voice "2HI_1386"
    hina "\"Not today.\"" id a10_cou2_03_2879a04a

    show rin 1 lg school_scarf g with dict_dissolve_25

    voice "2RI_1332"
    rin "\"What? Why? I don't get it.\"" id a10_cou2_03_e3f741dc

    "Hina's unexpected reaction threw Rin for a loop."

    show hina 2 lg school e with dict_dissolve_25

    voice "2HI_1387"
    hina "\"I'm going out for a bit.\"" id a10_cou2_03_c46145e9

    hide hina with dict_dissolve_25

    "Hina slipped past the floundering Rin and opened the door."

    show rin 2 lg school_scarf f with dict_dissolve_25

    voice "2RI_1333"
    rin "\"Huh? Wait, going out? But we just got home? You haven't even changed. Where are you going?\"" id a10_cou2_03_654ca48f

    $ side_image = "hina 2 side school e"

    voice "2HI_1388"
    hina "\"I dunno.\"" id a10_cou2_03_b026483d

    play sound se521
    pause 2.0

    stop music fadeout 1.0

    "She left."

    show rin 1 lg school_scarf j with dict_dissolve_25

    voice "2RI_1334"
    rin "\"Huh? Wha? Whaaat?!\"" id a10_cou2_03_79e7f00d

    "Rin wailed at the door, the empty collar clutched in her hand."

    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou2_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
