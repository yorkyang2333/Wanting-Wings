label a04_cou3_09:

    scene white with Dissolve(0.5)
    pause 1.5

    scene bg08cb with Dissolve(0.375)
    pause 1.125

    play music bgm03

    $ voice3("hina","HIN_1538","rin","RIN_1478","fumi","FUM_1300")
    hina_rin_fumi "\"Merry Christmas!\""

    play sound [se585,se585]
    pause 0.5
    play sound2 se585

    "Laughter filled their room."

    "They exchanged presents, ate cake, and enjoyed their time together, all three of them."

    "However—"

    scene white with Dissolve(0.375)
    pause 1.125

    scene ev15a with Dissolve(0.375)
    pause 1.125

    voice "HIN_1539"
    hina "\"I have one more present for both of you.\""

    voice "FUM_1301"
    fumi "\"Huh? What is it?\""

    voice "RIN_1479"
    rin "\"For us?\""

    voice "HIN_1540"
    hina "\"I'll close my eyes for a little while.\""

    "Rin and Fumi exchanged a blank look."

    voice "HIN_1541"
    hina "\"Ugh, god! I'm telling you I won't look!\""

    $ voice2("rin","RIN_1480","fumi","FUM_1302")
    rin_fumi "\"Oh...\""

    voice "HIN_1542"
    hina "\"I noticed you two holding hands under the table, you know.\""

    voice "FUM_1303"
    fumi "\"...Natsume...\""

    voice "RIN_1481"
    rin "\"...Hina...\""

    voice "HIN_1543"
    hina "\"Ah, but a kiss is all you get, okay?!\""

    voice "RIN_1482"
    rin "\"Fumi...\""

    voice "FUM_1304"
    fumi "\"Rin...\""

    voice "HIN_1544"
    hina "\"Okay, Merry Christmas! Merry Christmas!\""

    "So Rin and Fumi exchanged a blissful kiss."

    window hide

    $ persistent.fumi_rin_clear1 = True
    if persistent.kimihane_menu_status == 0:
        $ persistent.kimihane_menu_status = 1
    $ renpy.block_rollback()

    pause 1.0
    scene ed_c00 with Dissolve(0.75)
    pause 2.25
    show ed_c01 with Dissolve(0.75)
    pause 5.25

    stop music fadeout 3.0

    scene white with Dissolve(0.75)
    pause 2.25

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 1.5

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
