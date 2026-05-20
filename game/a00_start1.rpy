label start:

    stop music fadeout 1.0
    scene black
    with Fade(0.5,1.5,0.5)

    $ _game_menu_screen = None
    $ persistent.layer_shaken = False

    if persistent.game == "kimihane":
        scene expression "gui/kimihane/mainmenu_ground1.webp" with Dissolve(0.5)

        $ routes_cleared = sum([bool(persistent.hina_fumi_clear1),bool(persistent.rin_hina_clear1),bool(persistent.fumi_rin_clear1)])

        pause 1.0

        call screen kimihane_chapters with Dissolve(0.5)
        with Dissolve(0.25)

    elif persistent.game == "kimikara":

        $ routes_cleared = sum([bool(persistent.hina_fumi_clear2),bool(persistent.rin_hina_clear2),bool(persistent.fumi_rin_clear2)])

        scene expression "gui/kimikara/mainmenu_ground1.webp" with Dissolve(0.5)

        pause 1.0

        call screen kimikara_chapters with Dissolve(0.5)
        with Dissolve(0.25)

    $ renpy.block_rollback()

    scene black with Dissolve(0.5)

    pause 1.0

    $ _game_menu_screen = "save"

    if _return:
        jump expression _return
    else:

        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
