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
    hina "\"I have one more present for both of you.\"" id a04_cou3_09_ee10e9da

    voice "FUM_1301"
    fumi "\"Huh? What is it?\"" id a04_cou3_09_639b26d2

    voice "RIN_1479"
    rin "\"For us?\"" id a04_cou3_09_9c397be1

    voice "HIN_1540"
    hina "\"I'll close my eyes for a little while.\"" id a04_cou3_09_1b8c6e44

    "Rin and Fumi exchanged a blank look."

    voice "HIN_1541"
    hina "\"Ugh, god! I'm telling you I won't look!\"" id a04_cou3_09_72d6be2e

    $ voice2("rin","RIN_1480","fumi","FUM_1302")
    rin_fumi "\"Oh...\""

    voice "HIN_1542"
    hina "\"I noticed you two holding hands under the table, you know.\"" id a04_cou3_09_fd5663d1

    voice "FUM_1303"
    fumi "\"...Natsume...\"" id a04_cou3_09_7442ae22

    voice "RIN_1481"
    rin "\"...Hina...\"" id a04_cou3_09_901ced5d

    voice "HIN_1543"
    hina "\"Ah, but a kiss is all you get, okay?!\"" id a04_cou3_09_6125e6bf

    voice "RIN_1482"
    rin "\"Fumi...\"" id a04_cou3_09_aa2c7f90

    voice "FUM_1304"
    fumi "\"Rin...\"" id a04_cou3_09_2db07c47

    voice "HIN_1544"
    hina "\"Okay, Merry Christmas! Merry Christmas!\"" id a04_cou3_09_6ccacff5

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
