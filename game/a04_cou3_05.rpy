label a04_cou3_05:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    scene bg02ca with Dissolve(0.25)
    pause 0.75

    play music bgm01

    show hina 3 lg light pyjama b:
        xcenter 646 ycenter 541
    with Dissolve(0.25)

    voice "HIN_1500"
    hina "\"Hey, Rin?\""

    show rin 3 lg light pyjama b with dict_dissolve_25

    voice "RIN_1342"
    rin "\"Hm~?\""

    show hina 3 lg pyjama f with dict_dissolve_25

    voice "HIN_1501"
    hina "\"I'm guessing I'm wrong about this, but Asou's not bullying you, is she?\""

    play sound se530

    show rin 3 lg light pyjama f with dict_dissolve_25

    voice "RIN_1343"
    rin "\"Wha?!\""

    "Rin dropped the book she was reading."

    voice "RIN_1344"
    rin "\"Wh-Where'd you come up with something like that?\""

    show hina 3 lg pyjama b with dict_dissolve_25

    voice "HIN_1502"
    hina "\"Well, you ran out of the classroom crying today.\""

    voice "RIN_1345"
    rin "\"Th-That's because...\""

    show hina 3 lg pyjama d with dict_dissolve_25

    voice "HIN_1503"
    hina "\"You seem kinda timid around her lately, but Asou isn't really acting any different.\""

    show rin 3 lg light pyjama d with dict_dissolve_25

    voice "RIN_1346"
    rin "\"O-Oh... Is that what you mean?\""

    show hina 3 lg pyjama b with dict_dissolve_25

    voice "HIN_1504"
    hina "\"What did you think I meant?\""

    show rin 3 lg light pyjama f with dict_dissolve_25

    voice "RIN_1347"
    rin "\"Nothing, there's nothing going on!\""

    show hina 3 lg pyjama d with dict_dissolve_25

    voice "HIN_1505"
    hina "\"...Well, alright. But you can talk to me about anything, okay?\""

    show hina 3 lg pyjama f with dict_dissolve_25

    voice "HIN_1506"
    hina "\"We all get to live together in the same room, so we should get along. I consider both of you to be important friends to me.\""

    show rin 3 lg light pyjama d with dict_dissolve_25

    voice "RIN_1348"
    rin "\"Yeah...\""

    "Rin seemed to be debating something."

    voice "RIN_1349"
    rin "\"L-Listen, Hina. Fumi and I are—\""

    show hina 3 lg pyjama i with dict_dissolve_25

    voice "HIN_1507"
    hina "\"It's a good thing we're all girls, though.\""

    show rin 3 lg light pyjama b with dict_dissolve_25

    voice "RIN_1350"
    rin "\"Huh?\""

    show hina 3 lg pyjama e with dict_dissolve_25

    voice "HIN_1508"
    hina "\"Well, it'd make things pretty complicated if romance got involved.\""

    show rin 3 lg light pyjama f with dict_dissolve_25

    voice "RIN_1351"
    rin "\"Y-Yeah, I guess.\""

    show hina 3 lg pyjama b with dict_dissolve_25

    voice "HIN_1509"
    hina "\"Oh, were you about to say something?\""

    show rin 3 lg light pyjama e with dict_dissolve_25

    voice "RIN_1352"
    rin "\"No, it was nothing.\""

    "...The truth remains concealed."

    play sound se521

    $ side_image = "fumi 1 side pyjama c"

    voice "FUM_1180"
    fumi "\"Okay, Sachiko's going to pick up our Christmas cake.\""

    scene black with Dissolve(0.5)
    pause 2.0

    "........."

    "......"

    scene bg02dd with bg_effect_05
    pause 0.5

    show rin 3 sm nightlight pyjama d with Dissolve(0.25)

    voice "RIN_1353"
    rin "\"Whoops, can't find my glasses.\""

    show hina 3 sm dark pyjama b with dict_dissolve_25

    voice "HIN_1510"
    hina "\"Are they on your head?\""

    show rin 3 sm nightlight pyjama b with dict_dissolve_25

    voice "RIN_1354"
    rin "\"I looked there first.\""

    "It was Rin's usual reading routine."

    show fumi 3 sm nightlight pyjama c with dict_dissolve_25

    voice "FUM_1181"
    fumi "\"Oh, your glasses are right here.\""

    "Fumi found them on her pillow."

    show rin 3 sm nightlight pyjama f with dict_dissolve_25

    voice "RIN_1355"
    rin "\"...Oh.\""

    "Rin's face said, \"crap.\" And a moment later..."

    show fumi 3 sm nightlight pyjama e with dict_dissolve_25

    voice "FUM_1182"
    fumi "\"...Oh!\""

    "Fumi's said the same."

    show hina 3 sm dark pyjama g with dict_dissolve_25

    voice "HIN_1511"
    hina "\"Why?!\""

    show fumi 3 sm nightlight pyjama g with dict_dissolve_25

    voice "FUM_1183"
    fumi "\"U-Umm... err...\""

    show rin 3 sm nightlight pyjama b with dict_dissolve_25

    voice "RIN_1356"
    rin "\"Uhh...\""

    show hina 3 lg dark pyjama g with dict_dissolve_25

    voice "HIN_1512"
    hina "\"A magic trick?!\""

    "Oh... she hadn't noticed."

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    jump a04_comn_05
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
