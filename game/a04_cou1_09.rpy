label a04_cou1_09:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    play music bgm03

    scene ev13a with Dissolve(0.375)
    pause 1.125

    voice "HIN_1238"
    hina "\"Wait, your present is the same as mine, Fumi!\"" id a04_cou1_09_3aa0a0c4

    voice "FUM_1052"
    fumi "\"Wow! What a wonderful coincidence! We have matching shoes now!\"" id a04_cou1_09_757cce87

    voice "RIN_1018"
    rin "\"Wow, a padded kimono.\"" id a04_cou1_09_88d5637a

    voice "HIN_1239"
    hina "\"I wanted to get you red shoes no matter what, since you're my angel, Fumi.\"" id a04_cou1_09_eebf2c90

    "A triumphant smile."

    voice "FUM_1053"
    fumi "\"I wanted red shoes for you to wear too, Hina.\"" id a04_cou1_09_564cbd27

    voice "RIN_1019"
    rin "\"Well, don't you two get along swell? And I've got my padded kimono.\"" id a04_cou1_09_e8e0d77c

    voice "FUM_1054"
    fumi "\"Oh, did you want matching shoes too, Ogata?\"" id a04_cou1_09_1ea9146f

    voice "RIN_1020"
    rin "\"No way, that cute stuff wouldn't look good on me~\"" id a04_cou1_09_b5d70df5

    voice "HIN_1240"
    hina "\"Don't pout~ I picked it out with Fumi. It's perfect for you, isn't it?\"" id a04_cou1_09_77694b06

    voice "RIN_1021"
    rin "\"Weeell, geeeee, thaaanks.\"" id a04_cou1_09_99144a2d

    voice "FUM_1055"
    fumi "\"Heheh, okay, get ready...\"" id a04_cou1_09_b370f419

    voice "HIN_1241"
    hina "\"Everyone got your party poppers?\"" id a04_cou1_09_8ad31abd

    voice "RIN_1022"
    rin "\"Yeah, yeah.\"" id a04_cou1_09_19ffdada

    play sound [se585,se585]
    pause 0.5
    play sound2 se585
    pause 1.0

    $ voice3("hina","HIN_1242","rin","RIN_1023","fumi","FUM_1056")
    hina_rin_fumi "\"Merry Christmas!\""
    window hide


    $ persistent.hina_fumi_clear1 = True
    $ renpy.block_rollback()

    pause 1.0
    scene ed_a00 with Dissolve(0.75)
    pause 2.25
    show ed_a01 with Dissolve(0.75)
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
