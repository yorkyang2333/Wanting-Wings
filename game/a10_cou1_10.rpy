label a10_cou1_10:

    scene white with Dissolve(0.5)
    pause 2.0

    play music bgm06 fadein 1.0

    scene kimikara_20_a with Dissolve(2.0)

    voice "2HI_1364"
    hina "\"Taaah!\""

    voice "2FU_1106"
    fumi "\"To, to, tah♪\""

    if persistent.dpatch:
        "Hina and Fumi ran up the stone steps that led to the school gate." id a10_cou1_10_9a2df169
    else:
        "Hina and Fumi ran up the stone steps that led to the academy gate."

    $ side_image = "rin 1 side school_scarf j"

    voice "2RI_1303"
    rin "\"Heeh... haah...\""

    $ side_image = "miyako 2 side school_sei a"

    voice "2MI_1030"
    miyako "\"Are you okay?\""

    "Then there was Rin, whose life had drained to zero after having to run full-speed first thing in the morning."

    $ side_image = "rin 1 side school_scarf j"

    voice "2RI_1304"
    rin "\"We're not even gonna be late. Why are those two in such a hurry?\""

    $ side_image = "miyako 2 side school_sei c"

    voice "2MI_1031"
    miyako "\"Eheheh. I wonder if they just can't keep their hearts or their feet still.\""

    "Miyako peered up at them as if they were too bright to look at."

    voice "2HI_1365"
    hina "\"It's 'cause we've got wings on our shoes♪\""

    voice "2FU_1107"
    fumi "\"Yep♪\""

    voice "2HI_1366"
    hina "These are our precious Christmas present shoes. But we don't mind anymore if they get dirty or worn down." (what_first_indent=24, show_name=False)

    voice "2FU_1108"
    fumi "Now we know that we'll be able to make as many memories as we want from now on." (what_first_indent=24, show_name=False)

    $ voice2("hina","2HI_1367","fumi","2FU_1109")
    if persistent.dpatch:
        hina_fumi "Puddles, mud, school rules... We'll run through them all in these shoes!" id a10_cou1_10_aaaf4a27 (what_first_indent=24, show_name=False)
    else:
        hina_fumi "Puddles, mud, campus rules... We'll run through them all in these shoes!" (what_first_indent=24, show_name=False)

    "Before their youth, ten years and eternity were the same \"forever\" to them."

    "The future they looked toward now stretched on infinitely before them, no matter how far they reached their arms toward it."

    "You don't have to just believe in the future you can see."

    "And you don't have to only look far off, either. Yesterday, today, tomorrow, forever. Isn't that good enough?"

    "Carpe diem!"

    window hide

    $ persistent.hina_fumi_clear2 = True
    if sum([bool(persistent.hina_fumi_clear2),bool(persistent.rin_hina_clear2),bool(persistent.fumi_rin_clear2)]) == 3 and persistent.kimikara_menu_status == 0:
        $ persistent.kimikara_menu_status = 1
    $ renpy.block_rollback()

    pause 1.0
    scene ed2_a00 with Dissolve(0.75)
    pause 2.25
    show ed2_a01 with Dissolve(0.75)
    pause 5.25

    stop music fadeout 3.0

    scene white with Dissolve(0.75)
    pause 2.25

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 2.5

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
