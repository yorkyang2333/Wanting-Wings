label a10_cou2_03:

    scene bg02bg with Dissolve(0.5)
    pause 1.5

    play music bgm02 fadein 1.0

    play sound se521
    pause 1.0

    $ side_image = "hina 2 side school_scarf d"

    voice "2HI_1378"
    hina "\"We're back.\""

    "Hina and Rin returned to the dorm."

    "As they'd discussed earlier, Fumi and Miyako had broken off from them on the way, sending the two of them home on their own."

    $ side_image = "hina 2 side school_scarf f"

    voice "2HI_1379"
    hina "\"I wonder what Asou and Miyako have to talk about.\""

    "Hina mused, turning on the air conditioner."

    $ side_image = "rin 1 side school_scarf f"

    voice "2RI_1323"
    rin "\"Maybe they have some planning to do for Valentine's Day.\""

    $ side_image = "hina 2 side school_scarf e"

    voice "2HI_1380"
    hina "\"Hmm.\""

    $ side_image = "rin 1 side school_scarf c"

    voice "2RI_1324"
    rin "\"But because of that, we've got some unexpected time alone, right?\""

    $ side_image = "hina 1 side school_scarf m"

    voice "2HI_1381"
    hina "\"I suppose so.\""

    "Hina said curtly, removing her scarf."

    "In contrast to Rin's excitement, Hina seemed somehow distracted."

    $ side_image = "rin 1 side school_scarf h"

    voice "2RI_1325"
    rin "\"......\""

    "Rin took the collar out of her pocket and sidled up to Hina."

    show rin 1 lg school_scarf f at pos_r with dict_dissolve_25

    voice "2RI_1326"
    rin "\"Hiiinaaa?\""

    "She said coaxingly and brought the collar up to Hina's neck, but..."

    show hina 2 lg school e at pos_l with dict_dissolve_25

    voice "2HI_1382"
    hina "\"......\""

    "Hina twisted to escape her grasp."

    show rin 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_1327"
    rin "\"Huh?\""

    "Rin was left standing there blankly, collar in hand."

    show rin 1 lg school_scarf g with dict_dissolve_25

    voice "2RI_1328"
    rin "\"Umm, the collar...\""

    show hina 2 lg school f with dict_dissolve_25

    voice "2HI_1383"
    hina "\"You want to put it on?\""

    show rin 2 lg school_scarf e with dict_dissolve_25

    voice "2RI_1329"
    rin "\"Well, I mean, haven't you been in kind of a bad mood lately? Things were kind of awkward on the way home... You didn't say much.\""

    show hina 2 lg school d with dict_dissolve_25

    voice "2HI_1384"
    hina "\"......\""

    show rin 2 lg school_scarf b with dict_dissolve_25

    voice "2RI_1330"
    rin "\"So, to make up...\""

    "Rin held the collar out again."

    show hina 2 lg school h with dict_dissolve_25

    voice "2HI_1385"
    hina "\"......\""

    "Hina shook her head."

    show rin 1 lg school_scarf e with dict_dissolve_25

    voice "2RI_1331"
    rin "\"Huh? You don't want to?\""

    voice "2HI_1386"
    hina "\"Not today.\""

    show rin 1 lg school_scarf g with dict_dissolve_25

    voice "2RI_1332"
    rin "\"What? Why? I don't get it.\""

    "Hina's unexpected reaction threw Rin for a loop."

    show hina 2 lg school e with dict_dissolve_25

    voice "2HI_1387"
    hina "\"I'm going out for a bit.\""

    hide hina with dict_dissolve_25

    "Hina slipped past the floundering Rin and opened the door."

    show rin 2 lg school_scarf f with dict_dissolve_25

    voice "2RI_1333"
    rin "\"Huh? Wait, going out? But we just got home? You haven't even changed. Where are you going?\""

    $ side_image = "hina 2 side school e"

    voice "2HI_1388"
    hina "\"I dunno.\""

    play sound se521
    pause 2.0

    stop music fadeout 1.0

    "She left."

    show rin 1 lg school_scarf j with dict_dissolve_25

    voice "2RI_1334"
    rin "\"Huh? Wha? Whaaat?!\""

    "Rin wailed at the door, the empty collar clutched in her hand."

    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a10_cou2_04
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
