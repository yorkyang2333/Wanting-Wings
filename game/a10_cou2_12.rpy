label a10_cou2_12:

    scene white with Dissolve(0.5)
    pause 2.0

    play music bgm06 fadein 1.0

    scene kimikara_21_a with Dissolve(2.0)

    voice "2AR_0002"
    arthur "\"Ruff!\"" id a10_cou2_12_f64a2b55

    "Arthur was in a great mood with his two favorite people."

    "Rin walked through the park under the clear winter sky, Arthur's leash in her right hand and Hina's hand in her left."

    "She couldn't deny she was being pulled along by the two powerful animals(?), but a bright, happy smile was on her face regardless."

    voice "2AR_0001"
    arthur "\"Ruff, ruff!\"" id a10_cou2_12_0bd7e8ba_1

    voice "2RI_1536"
    rin "\"Wait, not that way, Arthur.\"" id a10_cou2_12_8b424da2

    "Spotting another dog, Arthur was about to run off, but Rin tugged at his leash, keeping him close."

    voice "2HI_1541"
    hina "\"You were so scared of him before, but you're getting the hang of it now.\"" id a10_cou2_12_cafa9d41

    voice "2RI_1537"
    rin "\"Well, I've had practice taking care of you every day.\"" id a10_cou2_12_97479fba

    "What's important is conveying your affection and acting with confidence. It's the same with Hina, too."

    voice "2HI_1542"
    hina "\"Oh, there's a fountain. I wanna take a picture.\"" id a10_cou2_12_84c28449

    voice "2RI_1538"
    rin "\"Ah, hey, Hina! If you're gonna run off, let go of me first!\"" id a10_cou2_12_156d1d87

    voice "2AR_0001"
    arthur "\"Ruff, ruff!\"" id a10_cou2_12_0bd7e8ba_1

    voice "2RI_1539"
    rin "\"Waaah! Arthur too?!\"" id a10_cou2_12_2c8ff183

    "When Hina sped away, Arthur also took off."

    voice "2RI_1540"
    rin "\"Hey, hey, hey, hey! Not different directions, you two! You're gonna take my arms with you!\"" id a10_cou2_12_cf85284b

    voice "2HI_1543"
    hina "\"Let's race, let's race!\"" id a10_cou2_12_593b7d88

    voice "2RI_1541"
    rin "\"Hina, stay! I mean it, stay!\"" id a10_cou2_12_5224a1b2

    voice "2HI_1544"
    hina "\"Okay♪\"" id a10_cou2_12_2c0c3ace

    voice "2RI_1542"
    rin "\"You're not actually doing it!\"" id a10_cou2_12_0f28468a

    "It seemed the path of the owner was still a long one for Rin."

    window hide

    $ persistent.rin_hina_clear2 = True
    if sum([bool(persistent.hina_fumi_clear2),bool(persistent.rin_hina_clear2),bool(persistent.fumi_rin_clear2)]) == 3 and persistent.kimikara_menu_status == 0:
        $ persistent.kimikara_menu_status = 1
    $ renpy.block_rollback()

    pause 1.0
    scene ed2_b00 with Dissolve(0.75)
    pause 2.25
    show ed2_b01 with Dissolve(0.75)
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
