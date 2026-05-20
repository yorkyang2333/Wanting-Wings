label a04_cou1_09:

    scene bg08ca with Dissolve(0.5)
    pause 1.5

    play music bgm03

    scene ev13a with Dissolve(0.375)
    pause 1.125

    voice "HIN_1238"
    hina "\"Wait, your present is the same as mine, Fumi!\""

    voice "FUM_1052"
    fumi "\"Wow! What a wonderful coincidence! We have matching shoes now!\""

    voice "RIN_1018"
    rin "\"Wow, a padded kimono.\""

    voice "HIN_1239"
    hina "\"I wanted to get you red shoes no matter what, since you're my angel, Fumi.\""

    "A triumphant smile."

    voice "FUM_1053"
    fumi "\"I wanted red shoes for you to wear too, Hina.\""

    voice "RIN_1019"
    rin "\"Well, don't you two get along swell? And I've got my padded kimono.\""

    voice "FUM_1054"
    fumi "\"Oh, did you want matching shoes too, Ogata?\""

    voice "RIN_1020"
    rin "\"No way, that cute stuff wouldn't look good on me~\""

    voice "HIN_1240"
    hina "\"Don't pout~ I picked it out with Fumi. It's perfect for you, isn't it?\""

    voice "RIN_1021"
    rin "\"Weeell, geeeee, thaaanks.\""

    voice "FUM_1055"
    fumi "\"Heheh, okay, get ready...\""

    voice "HIN_1241"
    hina "\"Everyone got your party poppers?\""

    voice "RIN_1022"
    rin "\"Yeah, yeah.\""

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
