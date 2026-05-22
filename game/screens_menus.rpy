

screen language_select():
    tag menu


    imagemap:
        ground "images/select_language.webp"
        idle "gui/language_idle.webp"
        hover "gui/language_hover.webp"
        alpha False
        hotspot (390,336,244,53) action Return(None)
        hotspot (390,459,244,53) action Return("simplified_chinese")





screen main_menu():
    tag menu





    if persistent.game == None:
        if not persistent.angel_clear:
            add "images/back_a.webp"
            imagemap:
                ground "gui/title_select_1_ground.webp"
                idle "gui/title_select_1_idle.webp"
                hover "gui/title_select_1_hover.webp"
                alpha False

                hotspot (276,431,54,23) action Quit(confirm=False)
                hotspot (522,184,411,393) action [SetVariable("persistent.game","kimihane"),FilePageCheck(),With(Fade(0.25,1.0,0.25))]
        elif not persistent.miyako_sachiko_clear:
            imagemap:
                ground "images/back_b.webp"
                idle "gui/title_select_2_idle.webp"
                hover "gui/title_select_2_hover.webp"
                alpha False

                hotspot (950,672,52,22) action Quit(confirm=False)
                hotspot (55,145,411,393) action [SetVariable("persistent.game","kimihane"),FilePageCheck(),With(Fade(0.25,1.0,0.25))]
                hotspot (595,145,411,393) action [SetVariable("persistent.game","kimikara"),FilePageCheck(),With(Fade(0.25,1.0,0.25))]
        else:
            add "gui/title_select_3_ground.webp"

            imagebutton:
                idle "gui/title_select_3_kimihane_idle.webp"
                hover "gui/title_select_3_kimihane_hover.webp"
                pos (0,0)
                action [SetVariable("persistent.game","kimihane"),FilePageCheck(),With(Fade(0.25,1.0,0.25))]
                focus_mask True

            imagebutton:
                idle "gui/title_select_3_kimikara_idle.webp"
                hover "gui/title_select_3_kimikara_hover.webp"
                pos (365,0)
                action [SetVariable("persistent.game","kimikara"),FilePageCheck(),With(Fade(0.25,1.0,0.25))]
                focus_mask True

            imagebutton:
                idle "gui/title_select_3_exit_idle.webp"
                hover "gui/title_select_3_exit_hover.webp"
                pos (620,708)
                action Quit(confirm=False)
                focus_mask True

    elif persistent.game == "kimihane":
        if persistent.kimihane_menu_status == 0:
            add "gui/kimihane/mainmenu_ground1.webp"
            add "gui/kimihane/title1.webp"

            if not (persistent.hina_fumi_clear1 or persistent.rin_hina_clear1 or persistent.fumi_rin_clear1):
                imagemap:
                    ground Null()
                    idle "gui/kimihane/mainmenu_idle1.webp"
                    hover "gui/kimihane/mainmenu_hover1.webp"

                    hotspot (312,320,90,90) action Start()

                    hotspot (416,320,90,90) action ShowMenu("load")
                    hotspot (520,320,90,90) action ShowMenu("preferences")
                    hotspot (624,320,90,90) action [SetVariable("persistent.game",None),With(Fade(0.25,1.0,0.25))]
            else:
                imagemap:
                    ground Null()
                    idle "gui/kimihane/mainmenu_idle2.webp"
                    hover "gui/kimihane/mainmenu_hover2.webp"

                    hotspot (260,320,90,90) action Start()
                    hotspot (364,320,90,90) action ShowMenu("load")
                    hotspot (468,320,90,90) action ShowMenu("kimihane_extra")
                    hotspot (572,320,90,90) action ShowMenu("preferences")
                    hotspot (676,320,90,90) action [SetVariable("persistent.game",None),With(Fade(0.25,1.0,0.25))]

        else:
            imagemap:
                ground "gui/kimihane/mainmenu_ground2.webp"
                idle "gui/kimihane/mainmenu_idle3.webp"
                hover "gui/kimihane/mainmenu_hover3.webp"

                hotspot (508,320,90,90) action Start()
                hotspot (612,320,90,90) action ShowMenu("load")
                hotspot (716,320,90,90) action ShowMenu("kimihane_extra")
                hotspot (820,320,90,90) action ShowMenu("preferences")
                hotspot (924,320,90,90) action [SetVariable("persistent.game",None),With(Fade(0.25,1.0,0.25))]

    elif persistent.game == "kimikara":
        if not (persistent.hina_fumi_clear2 and persistent.rin_hina_clear2 and persistent.fumi_rin_clear2):
            add "gui/kimikara/mainmenu_ground1.webp"
            add "gui/kimikara/title2.webp"

            if not (persistent.hina_fumi_clear2 or persistent.rin_hina_clear2 or persistent.fumi_rin_clear2):
                imagemap:
                    ground Null()
                    idle "gui/kimikara/mainmenu_idle1.webp"
                    hover "gui/kimikara/mainmenu_hover1.webp"

                    hotspot (312,320,90,90) action Start()
                    hotspot (416,320,90,90) action ShowMenu("load")
                    hotspot (520,320,90,90) action ShowMenu("preferences")
                    hotspot (624,320,90,90) action [SetVariable("persistent.game",None),With(Fade(0.25,1.0,0.25))]
            else:
                imagemap:
                    ground Null()
                    idle "gui/kimikara/mainmenu_idle2.webp"
                    hover "gui/kimikara/mainmenu_hover2.webp"

                    hotspot (260,320,90,90) action Start()
                    hotspot (364,320,90,90) action ShowMenu("load")
                    hotspot (468,320,90,90) action ShowMenu("kimikara_extra")
                    hotspot (572,320,90,90) action ShowMenu("preferences")
                    hotspot (676,320,90,90) action [SetVariable("persistent.game",None),With(Fade(0.25,1.0,0.25))]

        else:
            imagemap:
                ground "gui/kimikara/mainmenu_ground2.webp"
                idle "gui/kimikara/mainmenu_idle3.webp"
                hover "gui/kimikara/mainmenu_hover3.webp"

                hotspot (508,320,90,90) action Start()
                hotspot (612,320,90,90) action ShowMenu("load")
                hotspot (716,320,90,90) action ShowMenu("kimikara_extra")
                hotspot (820,320,90,90) action ShowMenu("preferences")
                hotspot (924,320,90,90) action [SetVariable("persistent.game",None),With(Fade(0.25,1.0,0.25))]


    on "replace" action Play("music",audio.bgm03,if_changed=True)

screen kimihane_chapters():

    add "gui/kimihane/chapters1.webp"

    if persistent.fumi_rin_clear1:
        add "gui/kimihane/chapters2.webp"

    imagemap:
        ground Null()
        idle "gui/kimihane/chapters_idle.webp"
        hover "gui/kimihane/chapters_hover.webp"
        insensitive "gui/kimihane/chapters_insensitive.webp"
        alpha False

        hotspot (65,233,197,228) action [Return("a00_op_01"),With(Dissolve(0.25))]
        hotspot (297,233,197,228) action [Return("a00_op_02"),With(Dissolve(0.25))] sensitive routes_cleared >= 1
        hotspot (530,233,197,228) action [Return("a00_op_03"),With(Dissolve(0.25))] sensitive routes_cleared >= 2
        hotspot (763,233,197,228) action [Return("a05_ang_01"),With(Dissolve(0.25))] sensitive routes_cleared == 3
        hotspot (108,70,112,107) action [Return(False),With(Dissolve(0.25))]

screen kimikara_chapters():

    add "gui/kimikara/chapters.webp"
    add "gui/kimikara/title3.webp"

    imagemap:
        ground Null()
        idle "gui/kimikara/chapters_idle.webp"
        hover "gui/kimikara/chapters_hover.webp"
        insensitive "gui/kimikara/chapters_insensitive.webp"
        alpha False

        hotspot (64,288,197,228) action [Return("a06_cou1_01"),With(Dissolve(0.25))]
        hotspot (295,288,197,228) action [Return("a06_cou2_01"),With(Dissolve(0.25))]
        hotspot (528,288,197,228) action [Return("a06_cou3_01"),With(Dissolve(0.25))]
        hotspot (761,288,197,228) action [Return("a11_cou4_01"),With(Dissolve(0.25))] sensitive routes_cleared == 3
        hotspot (888,627,81,93) action [Return(False),With(Dissolve(0.25))]





screen quick_menu():


    zorder 100

    imagemap:
        ground Fixed()
        idle "gui/[persistent.game]/quickmenu_idle.webp"
        insensitive "gui/[persistent.game]/quickmenu_idle.webp"
        hover "gui/[persistent.game]/quickmenu_hover.webp"
        selected_idle "gui/[persistent.game]/quickmenu_hover.webp"
        selected_hover "gui/[persistent.game]/quickmenu_hover.webp"
        hotspot (4,738,31,30) action HideInterface()
        if not _in_replay:
            if persistent.game == "kimihane":

                hotspot (38,738,78,30) action [ShowMenu("save"),FilePageCheck(),SelectedIf(False)]
                hotspot (119,738,78,30) action [ShowMenu("load"),FilePageCheck(),SelectedIf(False)]
                hotspot (200,738,78,30) action QuickSave("quick-1")
                hotspot (281,738,78,30) action QuickLoad("quick-1")
            elif persistent.game == "kimikara":
                hotspot (38,738,78,30) action [ShowMenu("save"),FilePageCheck(),SelectedIf(False)]
                hotspot (119,738,78,30) action [ShowMenu("load"),FilePageCheck(),SelectedIf(False)]
                hotspot (200,738,78,30) action QuickSave("quick-2")
                hotspot (281,738,78,30) action QuickLoad("quick-2")
        hotspot (362,738,78,30) action VoiceReplay()
        hotspot (443,738,78,30) action Preference("auto-forward", "toggle")
        hotspot (524,738,78,30) action Skip() selected renpy.is_skipping()
        hotspot (605,738,78,30) action ShowMenu("history")
        hotspot (686,738,78,30) action [FileTakeScreenshot(),ShowMenu("preferences")]
        if _in_replay:
            hotspot (767,738,78,30) action EndReplay()





screen save():
    tag menu

    use file_slots("save")

screen load():
    tag menu

    use file_slots("load")

screen file_slots(title):

    imagemap:
        ground "gui/[persistent.game]/file_ground.webp"
        idle "gui/[persistent.game]/file_idle.webp"
        hover "gui/[persistent.game]/file_hover.webp"
        insensitive "gui/[persistent.game]/file_idle.webp"

        hotspot (902,720,101,30) action Return()

        for i in range(1,11):
            if persistent.game == "kimihane":
                $ file_name = FileSlotName(i,10)
                $ file_time = FileTime(i, format='%b %d %Y, %H:%M', empty="")
                $ file_lang = FileJson(i,key="language")
                $ auto_page = "auto-1"

            elif persistent.game == "kimikara":

                $ file_name = FileSlotName(i,10)
                $ file_time = FileTime(i, format='%b %d %Y, %H:%M', empty="")
                $ file_lang = FileJson(i,key="language")
                $ auto_page = "auto-2"




            hotspot ((0 if i < 6 else 516),133 + (((i if i < 6 else i - 5)-1) * 114),508,110):
                action FileAction(i,newest=False)
                alternate FileDelete(i)
                sensitive not (renpy.get_screen("save") and FileCurrentPage() == auto_page)
                focus_mask None

                if FileNewest(i):
                    add "gui/[persistent.game]/file_new.webp" xpos 403 ypos 12
                add FileScreenshot(i) xpos 4 ypos 11
                text "[file_name]. [file_time!t]" style "file_info" xpos 128 ypos 10




                if FileJson(i,key="last_who"):

                    text renpy.translate_string(FileJson(i,key="last_who"),language=file_lang) + " ":
                        if file_lang is None:
                            style "file_info_name" xpos 142 ypos 35
                        elif file_lang == "simplified_chinese":
                            style "file_info_name_sc" xpos 142 ypos 35
                    text FileJson(i,key="last_what"):
                        if file_lang is None:
                            style "file_info_dialogue"
                        elif file_lang == "simplified_chinese":
                            style "file_info_dialogue_sc"
                        if FileJson(i,key="last_what_size") is not None:
                            size FileJson(i,key="last_what_size")
                        xpos 128
                        ypos 52

                        rest_indent renpy.slot_json(FileCurrentPage() + "-" + str(i)).get("last_kwargs").get("what_rest_indent",4)
                else:
                    if FileJson(i,key="last_what"):
                        text FileJson(i,key="last_what"):
                            if file_lang is None:
                                style "file_info_thought"
                            elif file_lang == "simplified_chinese":
                                style "file_info_thought_sc"
                            if FileJson(i,key="last_what_size") is not None:
                                size FileJson(i,key="last_what_size")
                            xpos 128
                            ypos 52
                key "save_delete" action FileDelete(i)

    imagebutton:
        idle "gui/[persistent.game]/file_1_idle.webp"
        hover "gui/[persistent.game]/file_1_hover.webp"
        selected_idle "gui/[persistent.game]/file_1_selected.webp"
        selected_hover "gui/[persistent.game]/file_1_selected.webp"
        focus_mask True
        pos (0,72)
        if persistent.game == "kimihane":
            action FilePage(1)
        elif persistent.game == "kimikara":
            action FilePage(6)
    imagebutton:
        idle "gui/[persistent.game]/file_2_idle.webp"
        hover "gui/[persistent.game]/file_2_hover.webp"
        selected_idle "gui/[persistent.game]/file_2_selected.webp"
        selected_hover "gui/[persistent.game]/file_2_selected.webp"
        focus_mask True
        pos (40,72)
        if persistent.game == "kimihane":
            action FilePage(2)
        elif persistent.game == "kimikara":
            action FilePage(7)
    imagebutton:
        idle "gui/[persistent.game]/file_3_idle.webp"
        hover "gui/[persistent.game]/file_3_hover.webp"
        selected_idle "gui/[persistent.game]/file_3_selected.webp"
        selected_hover "gui/[persistent.game]/file_3_selected.webp"
        focus_mask True
        pos (115,72)
        if persistent.game == "kimihane":
            action FilePage(3)
        elif persistent.game == "kimikara":
            action FilePage(8)
    imagebutton:
        idle "gui/[persistent.game]/file_4_idle.webp"
        hover "gui/[persistent.game]/file_4_hover.webp"
        selected_idle "gui/[persistent.game]/file_4_selected.webp"
        selected_hover "gui/[persistent.game]/file_4_selected.webp"
        focus_mask True
        pos (190,72)
        if persistent.game == "kimihane":
            action FilePage(4)
        elif persistent.game == "kimikara":
            action FilePage(9)
    imagebutton:
        idle "gui/[persistent.game]/file_5_idle.webp"
        hover "gui/[persistent.game]/file_5_hover.webp"
        selected_idle "gui/[persistent.game]/file_5_selected.webp"
        selected_hover "gui/[persistent.game]/file_5_selected.webp"
        focus_mask True
        pos (265,72)
        if persistent.game == "kimihane":
            action FilePage(5)
        elif persistent.game == "kimikara":
            action FilePage(10)
    imagebutton:
        idle "gui/[persistent.game]/file_auto_idle.webp"
        hover "gui/[persistent.game]/file_auto_hover.webp"
        selected_idle "gui/[persistent.game]/file_auto_selected.webp"
        selected_hover "gui/[persistent.game]/file_auto_selected.webp"
        focus_mask True
        pos (340,72)
        if persistent.game == "kimihane":
            action FilePage("auto-1")
        elif persistent.game == "kimikara":
            action FilePage("auto-2")
    imagebutton:
        idle "gui/[persistent.game]/file_quick_idle.webp"
        hover "gui/[persistent.game]/file_quick_hover.webp"
        selected_idle "gui/[persistent.game]/file_quick_selected.webp"
        selected_hover "gui/[persistent.game]/file_quick_selected.webp"
        focus_mask True
        pos (464,72)
        if persistent.game == "kimihane":
            action FilePage("quick-1")
        elif persistent.game == "kimikara":
            action FilePage("quick-2")

    if title == "save":
        add "gui/[persistent.game]/file_save.webp"
    elif title == "load":
        add "gui/[persistent.game]/file_load.webp"

style file_info:
    font "Tuffy-Regular.ttf"
    size 18
    outlines [(1,"#102d09",0,0)]
    color "#ffffff"

style file_info_name:
    font "Homizio-bold.ttf"
    size 13
    outlines [(1,"#102d09",0,0)]
    color "#ffffff"

style file_info_dialogue:
    rest_indent 4
    font "Tuffy-Regular.ttf"
    size 12
    outlines [(1,"#102d09",0,0)]
    xsize 370
    color "#ffffff"

style file_info_thought is file_info_dialogue:
    first_indent 12





style file_info_name_sc:
    font "2@SourceHanSans-Medium.ttc"
    size 13
    xoffset 10
    yoffset -4
    outlines [(1,"#102d09",0,0)]
    color "#ffffff"

style file_info_dialogue_sc:
    font "2@SourceHanSans-Medium.ttc"
    size 13
    first_indent -4
    outlines [(1,"#102d09",0,0)]
    line_spacing -2
    xoffset 5
    xsize 360
    color "#ffffff"

style file_info_thought_sc is file_info_dialogue_sc:
    xoffset 0
    rest_indent 12




screen preferences():
    tag menu

    modal True

    imagemap:
        ground "gui/[persistent.game]/config1_ground.webp"
        idle "gui/[persistent.game]/config1_idle.webp"
        hover "gui/[persistent.game]/config1_hover.webp"
        selected_idle "gui/[persistent.game]/config1_hover.webp"
        selected_hover "gui/[persistent.game]/config1_hover.webp"
        insensitive "gui/[persistent.game]/config1_idle.webp"
        alpha False

        hotspot (199,177,128,30) action [Preference("display", "window"),SelectedIf(not _preferences.fullscreen)]
        hotspot (346,177,128,30) action Preference("display", "fullscreen")
        hotspot (263,278,96,30) action Preference("skip", "all")
        hotspot (378,278,96,30) action Preference("skip", "seen")
        hotspot (263,379,96,30) action SetVariable("persistent.read_text_instant",True)
        hotspot (378,379,96,30) action SetVariable("persistent.read_text_instant",False)
        hotspot (263,480,96,30) action SetVariable("persistent.read_text_recolor",True)
        hotspot (378,480,96,30) action SetVariable("persistent.read_text_recolor",False)
        hotspot (263,581,96,30) action SetVariable("persistent.read_choices_recolor",True)
        hotspot (378,581,96,30) action SetVariable("persistent.read_choices_recolor",False)
        hotspot (779,480,96,30) action SetVariable("persistent.auto_after_choices",True)
        hotspot (894,480,96,30) action SetVariable("persistent.auto_after_choices",False)
        hotspot (779,581,96,30) action Preference("after choices", "skip")
        hotspot (894,581,96,30) action Preference("after choices", "stop")
        hotspot (334,682,140,30) action OpenURL("https://www.renpy.org/doc/html/license.html")

        hotspot (670,682,150,30) action Language(None)
        hotspot (840,682,150,30) action Language('simplified_chinese')

        hotspot (533,723,101,30):
            action [Preference("skip", "seen"),
                    SetVariable("persistent.fast_text",False),
                    SetVariable("persistent.read_text_instant",True),
                    SetVariable("persistent.read_text_recolor",True),
                    SetVariable("persistent.auto_after_choices",True),
                    Preference("after choices", "skip"),
                    Preference("text speed",51),
                    Preference("auto-forward time", 9),
                    SetVariable("persistent.window_opacity",0.5)]
            selected False

        if not main_menu:
            hotspot (656,723,101,30) action MainMenu(confirm=True)
        hotspot (779,723,101,30) action Quit(confirm=True)
        hotspot (902,723,101,30) action Return()

    imagebutton:
        idle "gui/[persistent.game]/config1_sound_idle.webp"
        hover "gui/[persistent.game]/config1_sound_hover.webp"
        focus_mask True
        pos (194,71)
        action [Show("preferences2",transition=None),Hide("preferences")]

    bar:

        pos (690,181)
        style "bar"
        value Preference("text speed")
    bar:
        pos (690,282)
        style "bar"
        value FieldValue(preferences,"afm_time",12.0,offset=3)
        bar_invert True
    bar:
        pos (690,383)
        style "bar"
        value FieldValue(persistent,"window_opacity",1.0)

    add "gui/[persistent.game]/version.webp"

screen preferences2():
    tag menu

    modal True

    imagemap:
        ground "gui/[persistent.game]/config2_ground.webp"
        idle "gui/[persistent.game]/config2_idle.webp"
        hover "gui/[persistent.game]/config2_hover.webp"
        selected_idle "gui/[persistent.game]/config2_hover.webp"
        selected_hover "gui/[persistent.game]/config2_hover.webp"
        insensitive "gui/[persistent.game]/config2_idle.webp"
        alpha False


        hotspot (263,169,96,30):
            action [Preference("all mute", "enable"),SetVoiceMute("hina",True),
                    SetVoiceMute("fumi",True),SetVoiceMute("rin",True),
                    SetVoiceMute("sachiko",True),SetVoiceMute("miyako",True),
                    SetVoiceMute("etc",True),SetMute("bgv",True)]
            selected (_preferences.mute.get("music",False)
                        and _preferences.mute.get("sfx",False)
                        and _preferences.mute.get("bgv",False)
                        and len(persistent._voice_mute) >= 5)

        hotspot (378,169,96,30):
            action [Preference("all mute", "disable"),SetVoiceMute("hina",False),
                    SetVoiceMute("fumi",False),SetVoiceMute("rin",False),
                    SetVoiceMute("sachiko",False),SetVoiceMute("miyako",False),
                    SetVoiceMute("etc",False),SetMute("bgv",False)]
            selected (not _preferences.mute.get("music",False)
                        or not _preferences.mute.get("sfx",False)
                        or not _preferences.mute.get("bgv",False)
                        or len(persistent._voice_mute) < 5)
        hotspot (468,248,30,30) action Preference("voice mute", "toggle")
        hotspot (179,409,138,30) action Preference("voice sustain", "enable")
        hotspot (336,409,138,30) action Preference("voice sustain", "disable")
        hotspot (984,170,30,30) action Preference("music mute", "toggle")
        hotspot (984,248,30,30) action Preference("sound mute", "toggle")
        hotspot (984,326,30,30) action ToggleMute("bgv")
        hotspot (779,409,96,30) action Preference("wait for voice", "enable")
        hotspot (894,409,96,30) action Preference("wait for voice", "disable")
        hotspot (468,520,30,30) action ToggleVoiceMute("hina")
        hotspot (468,599,30,30) action ToggleVoiceMute("fumi")
        hotspot (984,520,30,30) action ToggleVoiceMute("rin")
        hotspot (984,599,30,30) action ToggleVoiceMute("sachiko")
        if persistent.game == "kimihane":
            hotspot (468,677,30,30) action ToggleVoiceMute("etc")
        elif persistent.game == "kimikara":
            hotspot (468,677,30,30) action ToggleVoiceMute("miyako")
            hotspot (984,677,30,30) action ToggleVoiceMute("etc")

        hotspot (533,723,101,30):
            action [Preference("all mute", "disable"),
                    Preference("voice mute", "disable"),
                    Preference("music mute", "disable"),
                    Preference("sound mute", "disable"),
                    SetMixer("music", volume=0.75),
                    SetMixer("sfx", volume=0.65),
                    SetMixer("voice", volume=1.0),
                    SetField(persistent,"emphasize_audio_volume",0.68),
                    Preference("voice sustain", "disable"),
                    Preference("wait for voice", "enable"),
                    SetCharacterVolume("hina",1.0),
                    SetCharacterVolume("fumi",1.0),
                    SetCharacterVolume("rin",1.0),
                    SetCharacterVolume("sachiko",1.0),
                    SetCharacterVolume("miyako",1.0),
                    SetCharacterVolume("etc",1.0),
                    SetVoiceMute("hina",False),
                    SetVoiceMute("fumi",False),
                    SetVoiceMute("rin",False),
                    SetVoiceMute("sachiko",False),
                    SetVoiceMute("miyako",False),
                    SetVoiceMute("etc",False),
                    SetMute("bgv",False)]
            selected False

        if not main_menu:
            hotspot (656,723,101,30) action MainMenu(confirm=True)
        hotspot (779,723,101,30) action Quit(confirm=True)
        hotspot (902,723,101,30) action Return()

    imagebutton:
        idle "gui/[persistent.game]/config2_system_idle.webp"
        hover "gui/[persistent.game]/config2_system_hover.webp"
        focus_mask True
        pos (0,71)
        action [Show("preferences",transition=None),Hide("preferences2")]

    bar:

        pos (141,248)
        style "bar"
        value Preference("voice volume")

    bar:
        pos (141,327)
        style "bar"
        value FieldValue(persistent,"emphasize_audio_volume",1.0)

    bar:
        pos (657,170)
        style "bar"
        value Preference("music volume")

    bar:
        pos (657,248)
        style "bar"
        value Preference("sound volume")

    bar:
        pos (657,327)
        style "bar"
        value MixerValue("bgv")

    bar:
        pos (141,520)
        style "bar"
        value SetCharacterVolume("hina")

    bar:
        pos (141,599)
        style "bar"
        value SetCharacterVolume("fumi")

    bar:
        pos (657,520)
        style "bar"
        value SetCharacterVolume("rin")

    bar:
        pos (657,599)
        style "bar"
        value SetCharacterVolume("sachiko")

    if persistent.game == "kimihane":
        bar:
            pos (141,677)
            style "bar"
            value SetCharacterVolume("etc")
    elif persistent.game == "kimikara":
        bar:
            pos (141,677)
            style "bar"
            value SetCharacterVolume("miyako")
        bar:
            pos (657,677)
            style "bar"
            value SetCharacterVolume("etc")

style bar:
    xmaximum 275
    ymaximum 30
    thumb "gui/[persistent.game]/thumb.webp"
    thumb_offset 15
    thumb_shadow None

init python:

    def update_emphasize_audio_volume():
        """Update value of config.emphasize_audio_volume when the
        Reduce BGM During Voice Playback setting is changed.
        This is necessary as config variables cannot be changed
        directly during runtime.
        """
        
        config.emphasize_audio_volume = persistent.emphasize_audio_volume

    config.interact_callbacks.append(update_emphasize_audio_volume)





screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    imagemap:
        ground "gui/[persistent.game]/confirm_ground.webp"
        idle "gui/[persistent.game]/confirm_idle.webp"
        hover "gui/[persistent.game]/confirm_hover.webp"
        insensitive "gui/[persistent.game]/confirm_hover.webp"

        hotspot (287,380,224,37) action yes_action
        hotspot (513,380,224,37) action no_action


    key "game_menu" action no_action

    if message == gui.LOADING:
        add "gui/confirm_load.webp"
    elif message == gui.OVERWRITE_SAVE:
        add "gui/confirm_save.webp"
    elif message == gui.DELETE_SAVE:
        add "gui/confirm_delete.webp"
    elif message == gui.MAIN_MENU:
        add "gui/confirm_title.webp"
    elif message == gui.QUIT:
        add "gui/confirm_quit.webp"
    elif message == gui.END_REPLAY:
        add "gui/confirm_extra.webp"
    elif message == gui.UNKNOWN_TOKEN:
        add "gui/[persistent.game]/confirm2.webp"
        add "gui/confirm_unknown_token.webp"
    elif message == gui.TRUST_TOKEN:
        add "gui/[persistent.game]/confirm2.webp"
        add "gui/confirm_trust_token.webp"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
