init python:
    gui.init(1024, 768)




screen say(who, what, name=True):
    style_prefix "say"

    window:
        id "window"


        if (persistent.game == "kimihane" and not persistent.fumi_rin_clear1) or (persistent.game == "kimikara"
            and not (persistent.hina_fumi_clear2 or persistent.rin_hina_clear2 or persistent.fumi_rin_clear2)):
            background Transform("gui/[persistent.game]/textbox1.webp",alpha=persistent.window_opacity)

        else:
            background Transform("gui/[persistent.game]/textbox2.webp",alpha=persistent.window_opacity)


        if who and name:

            window:
                id "namebox"
                style "namebox"
                if (persistent.game == "kimihane" and not persistent.fumi_rin_clear1) or (persistent.game == "kimikara"
                    and not (persistent.hina_fumi_clear2 or persistent.rin_hina_clear2 or persistent.fumi_rin_clear2)):
                    background Transform("gui/[persistent.game]/namebox1.webp",alpha=persistent.window_opacity,xoffset=-20)
                else:
                    background Transform("gui/[persistent.game]/namebox2.webp",alpha=persistent.window_opacity,xoffset=-20)

                if not isinstance(name,basestring):
                    text who id "who" style "say_label"

                else:
                    text name id "who" style "say_label"

        if renpy.is_seen(ever=True):
            text what:
                id "what"
                slow_cps (0 if persistent.read_text_instant else preferences.text_cps)
                color ("#d7d7d7" if persistent.read_text_recolor else "#ffffff")
        else:
            text what id "what"

    add side_image
    use quick_menu

style window is default
style say_label is default
style say_dialogue is default
style namebox is default

style window:
    xpos 0
    ypos 617
    left_padding 20

style namebox:
    yoffset -29
    left_padding 20

style say_label:
    font "Homizio-bold.ttf"
    size 22
    outlines [(1,"#102d09",0,0),(0, "#102d09", 2, 2)]
    yoffset -1
    xoffset 10
    color "#ffffff"

style say_dialogue:
    font "Tuffy-Regular.ttf"
    size 24
    xsize 710
    xoffset 5
    yoffset 2
    rest_indent 8
    outlines [(1,"#102d09",0,0),(0, "#102d09", 2, 2)]
    color "#ffffff"

style say_thought is say_dialogue:
    first_indent 24

translate simplified_chinese style say_dialogue:
    font "2@SourceHanSans-Medium.ttc"
    size 26
    outlines [(1,"#102d09",0,0),(0, "#102d09", 2, 2)]
    yoffset 0
    xoffset 10
    rest_indent 24
    color "#ffffff"

translate simplified_chinese style say_thought is say_dialogue:
    first_indent 24
    xoffset 12

translate simplified_chinese style say_label:
    font "2@SourceHanSans-Medium.ttc"
    size 20
    outlines [(1,"#102d09",0,0),(0, "#102d09", 2, 2)]
    yoffset -4
    xoffset 40
    color "#ffffff"

define config.font_replacement_map = {("Tuffy-Regular.ttf",False,True):("Tuffy-Italic.ttf",False,False),
                                        ("Tuffy-Regular.ttf",True,False):("Tuffy-Bold.ttf",False,False)}







screen choice(items, no_chosen=False):

    for i in items:
        imagebutton:
            action i.action
            pos i.args[0]

            if not i.chosen or no_chosen or not persistent.read_choices_recolor:
                idle i.args[1] + "_idle.webp"
            else:
                idle i.args[1] + "_idle.webp" at read_choice
            hover i.args[1] + "_hover.webp"
            at menu_dissolve

    use quick_menu

transform menu_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0

transform read_choice:
    matrixcolor ContrastMatrix(0.7) * SaturationMatrix(0.5)


screen skip_indicator():
    pass




screen notify(message):

    zorder 100

    frame at notify_appear:
        ypos 45
        yminimum 34
        right_padding 50

        background Frame("gui/[persistent.game]/notify.webp",right=50)
        text "[message!tq]":
            style "notify_text"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_text:
    font "Tuffy-Regular.ttf"
    size 18
    xoffset 8
    yoffset 5
    outlines [(1,"#102d09",0,0),(0, "#102d09", 2, 2)]
    color "#ffffff"

translate simplified_chinese style notify_text:
    font "2@SourceHanSans-Medium.ttc"
    xoffset 18
    yoffset 2




screen history():
    tag menu

    predict False

    imagemap:
        ground "gui/[persistent.game]/history_ground.webp"
        idle "gui/[persistent.game]/history_idle.webp"
        hover "gui/[persistent.game]/history_hover.webp"
        hotspot (919,61,19,18) action Scroll("history_window","vertical decrease",10000)
        hotspot (919,80,19,18) action Scroll("history_window","vertical decrease","step")
        hotspot (919,639,19,18) action Scroll("history_window","vertical increase","step")
        hotspot (919,658,19,18) action Scroll("history_window","vertical increase",10000)
        hotspot (835,727,100,29) action Return()


    if _history_list == []:
        text _("The dialogue history is empty.") style "say_dialogue" xcenter 480 ypos 370 text_align 0.5

    viewport:
        id "history_window"
        xpos 90
        ypos 60
        xmaximum 800
        ymaximum 620
        mousewheel True
        yinitial 1.0
        has vbox
        for i in _history_list:
            hbox:
                if i.voice.filename:
                    imagebutton:
                        idle "gui/[persistent.game]/history_voice_idle.webp"
                        hover "gui/[persistent.game]/history_voice_hover.webp"
                        action PlayCharacterVoice(i.who,i.voice.filename)
                else:

                    null width 41 height 41

                vbox:

                    if i.show_args.get("name",i.who):
                        text i.show_args.get("name",i.who):
                            style "say_label"
                            xoffset 30
                        text i.what:
                            style "say_dialogue"
                            xoffset 10
                            first_indent i.what_args.get("first_indent",style.say_dialogue.first_indent)
                            rest_indent i.what_args.get("rest_indent",style.say_dialogue.rest_indent)
                            substitute False
                    else:
                        text i.what:
                            style "say_thought"
                            xoffset 10
                            substitute False


                    null height 50

    add "gui/[persistent.game]/history_bar.webp" xpos 919 ypos 99

    vbar:
        value YScrollValue("history_window")
        style "history_scrollbar"

    key "game_menu" action Return()
    key "hide_windows" action Return()

style history_scrollbar:
    bar_vertical True
    thumb "gui/[persistent.game]/thumb.webp"
    bar_invert True
    xpos 913
    ypos 99
    ymaximum 539
    xmaximum 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
