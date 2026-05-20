label a11_cou4_17:

    scene white with Dissolve(0.5)
    pause 2.0

    scene kimikara_10_v with Dissolve(2.0)

    voice "2SA_1201"
    sachiko "\"Miyako, grab the viridian?\""

    scene kimikara_10_w with Dissolve(0.5)

    voice "2MI_1303"
    miyako "\"Here.\""

    scene kimikara_10_x with Dissolve(0.5)

    voice "2MI_1304a"
    miyako "\"......\""

    scene kimikara_10_y with Dissolve(0.5)

    voice "2MI_1304"
    miyako "\"I can't see you, but you're there, aren't you? I've been sensing you all this time.\""

    window hide

    $ persistent.miyako_sachiko_clear = True
    $ renpy.block_rollback()

    pause 1.0
    scene ed2_d00 with Dissolve(0.75)
    pause 2.25
    show ed2_d01 with Dissolve(0.75)
    pause 5.25

    stop music fadeout 3.0

    scene black with Dissolve(0.75)
    pause 2.25



    scene ed2_d02 with Dissolve(0.5)
    pause 4.5

    stop music fadeout 1.0
    stop sound fadeout 1.0
    scene black with Dissolve(0.5)
    pause 2.0


    $ persistent.game = None
    if persistent.main_menu_status == 0:
        $ persistent.main_menu_status = 1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
