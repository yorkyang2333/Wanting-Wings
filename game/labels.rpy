label splashscreen:



    if persistent.first_run is None:
        scene select_language with Dissolve(0.5)
        pause 1.5
        call screen language_select with Dissolve(0.5)
        $ persistent.first_run = config.version
        scene black with Dissolve(0.5)
        if _return == True:
            $ renpy.change_language(None)
        else:
            $ renpy.change_language(_return)


        if persistent.fumi_rin_clear1:
            $ persistent.kimihane_menu_status = 1
        if sum([bool(persistent.hina_fumi_clear2),bool(persistent.rin_hina_clear2),bool(persistent.fumi_rin_clear2)]) == 3:
            $ persistent.kimikara_menu_status = 1
        pause 1.5
    else:
        python:
            try:
                
                if float(persistent.first_run) < float(config.version):
                    persistent.first_run = config.version
            except ValueError:
                persistent.first_run = config.version



    $ persistent.game = None

    $ _skipping = False
    $ _rollback = False

    if persistent.dpatch:
        scene back_a
        show warning
        with Dissolve(0.5)
        pause

        hide warning with Dissolve(0.25)
        pause 0.5
        show logo_1 with Dissolve(0.25)
    else:
        scene back_a
        show logo_1
        with Dissolve(0.5)
    pause 3.0

    hide logo_1 with Dissolve(0.25)
    $ renpy.pause(0.1,hard=True)
    show logo_2 with Dissolve(0.25)
    pause 3.0
    hide logo_2 with Dissolve(0.25)
    $ renpy.pause(0.1,hard=True)


    if not persistent.angel_clear:
        pause 1.0
        play music bgm03
        scene back_a
        show expression "gui/title_select_1_ground.webp"
        show expression "gui/title_select_1_idle.webp"
        with Dissolve(0.5)
    elif persistent.angel_clear and not persistent.miyako_sachiko_clear:
        scene black with Dissolve(0.5)
        pause 1.0
        play music bgm03
        scene back_b
        show expression "gui/title_select_2_idle.webp"
        with Dissolve(0.5)
    else:
        scene black with Dissolve(0.5)
        pause 1.0
        play music bgm03
        scene expression "gui/title_select_3_ground.webp"
        show expression "gui/title_select_3_kimihane_idle.webp":
            pos (0,0)
        show expression "gui/title_select_3_kimikara_idle.webp":
            pos (365,0)
        show expression "gui/title_select_3_exit_idle.webp":
            pos (620,708)
        with Dissolve(0.5)

    $ _skipping = True
    $ _rollback = True

label before_main_menu:

    if persistent.kimihane_menu_status == 1 and persistent.game == "kimihane":
        scene expression "gui/kimihane/mainmenu_ground1.webp" with Dissolve(0.25)

        pause 1.0

        scene white with Dissolve(0.5)
        pause 1.5

        scene expression "gui/kimihane/mainmenu_ground2.webp" with Dissolve(0.5)
        pause 2.0

        show expression "gui/kimihane/mainmenu_idle3.webp" with Dissolve(0.5)

        $ persistent.kimihane_menu_status = 2

    elif persistent.kimikara_menu_status == 1 and persistent.game == "kimikara":
        scene expression "gui/kimikara/mainmenu_ground1.webp" with Dissolve(0.25)

        pause 1.0

        scene white with Dissolve(0.5)
        pause 1.5

        scene expression "gui/kimikara/mainmenu_ground2.webp" with Dissolve(0.5)
        pause 2.0

        show expression "gui/kimikara/mainmenu_idle3.webp" with Dissolve(0.5)

        $ persistent.kimikara_menu_status = 2

    elif persistent.main_menu_status == 1 and persistent.game is None:
        scene expression "gui/title_select_3_ground.webp"
        with Dissolve(0.25)

        pause 2.0

        show expression "gui/title_select_3_kimihane_idle.webp":
            pos (0,0)
        show expression "gui/title_select_3_kimikara_idle.webp":
            pos (365,0)
        show expression "gui/title_select_3_exit_idle.webp":
            pos (620,708)
        with Dissolve(0.5)

        $ persistent.main_menu_status = 2

label after_load:




    camera

    python:
        persistent.layer_shaken = False

        if float(_version) < float(config.version):
            _version = config.version
            renpy.block_rollback()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
