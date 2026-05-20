



init python:


    def auto_after_choices_check(mode,old_modes):
        """If persistent.auto_after_choices is False, disable auto mode
        after a choice.
        """
        if persistent.auto_after_choices == False:
            if mode == "say" and old_modes[0] == "menu":
                _preferences.afm_enable = False

    config.mode_callbacks.append(auto_after_choices_check)


    def voice2(tag1,voice1,tag2,voice2):
        """Play two voice files simultaneously with respect to voice mute
        settings.
        """
        
        if set([tag1,tag2]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2)
        elif not tag1 in persistent._voice_mute:
            voice(voice1,tag1)
        elif not tag2 in persistent._voice_mute:
            voice(voice2,tag2)


    def voice3(tag1,voice1,tag2,voice2,tag3,voice3):
        """Play three voice files simultaneously with respect to voice mute
        settings.
        """
        if set([tag1,tag2,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice3)
        elif set([tag1,tag2]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2)
        elif set([tag1,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice3)
        elif set([tag2,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice3)
        elif not tag1 in persistent._voice_mute:
            voice(voice1,tag1)
        elif not tag2 in persistent._voice_mute:
            voice(voice2,tag2)
        elif not tag3 in persistent._voice_mute:
            voice(voice3,tag3)


    def voice4(tag1,voice1,tag2,voice2,tag3,voice3,tag4,voice4):
        """Play four voice files simultaneously with respect to voice mute
        settings.
        """
        if set([tag1,tag2,tag3,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice3 + "+" + voice4)
        elif set([tag1,tag2,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice3)
        elif set([tag1,tag2,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice4)
        elif set([tag1,tag3,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice3 + "+" + voice4)
        elif set([tag2,tag3,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice3 + "+" + voice4)
        elif set([tag1,tag2]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2)
        elif set([tag1,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice3)
        elif set([tag1,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice4)
        elif set([tag2,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice3)
        elif set([tag2,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice4)
        elif set([tag3,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice3 + "+" + voice4)
        elif not tag1 in persistent._voice_mute:
            voice(voice1,tag1)
        elif not tag2 in persistent._voice_mute:
            voice(voice2,tag2)
        elif not tag3 in persistent._voice_mute:
            voice(voice3,tag3)
        elif not tag4 in persistent._voice_mute:
            voice(voice4,tag4)


    def voice5(tag1,voice1,tag2,voice2,tag3,voice3,tag4,voice4,tag5,voice5):
        """Play five voice files simultaneously with respect to voice mute
        settings.
        """
        if set([tag1,tag2,tag3,tag4,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice3 + "+" + voice4 + "+" + voice5)
        elif set([tag1,tag2,tag3,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice3 + "+" + voice4)
        elif set([tag1,tag2,tag3,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice3 + "+" + voice5)
        elif set([tag1,tag2,tag4,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice4 + "+" + voice5)
        elif set([tag1,tag3,tag4,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice3 + "+" + voice4 + "+" + voice5)
        elif set([tag2,tag3,tag4,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice3 + "+" + voice4 + "+" + voice5)
        elif set([tag1,tag2,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice3)
        elif set([tag1,tag2,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice4)
        elif set([tag1,tag2,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2 + "+" + voice5)
        elif set([tag1,tag3,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice3 + "+" + voice4)
        elif set([tag1,tag3,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice3 + "+" + voice5)
        elif set([tag1,tag4,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice4 + "+" + voice5)
        elif set([tag2,tag3,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice3 + "+" + voice4)
        elif set([tag2,tag3,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice3 + "+" + voice5)
        elif set([tag2,tag4,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice4 + "+" + voice5)
        elif set([tag3,tag4,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice3 + "+" + voice4 + "+" + voice5)
        elif set([tag1,tag2]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice2)
        elif set([tag1,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice3)
        elif set([tag1,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice4)
        elif set([tag1,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice1 + "+" + voice5)
        elif set([tag2,tag3]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice3)
        elif set([tag2,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice4)
        elif set([tag2,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice2 + "+" + voice5)
        elif set([tag3,tag4]).isdisjoint(persistent._voice_mute):
            voice(voice3 + "+" + voice4)
        elif set([tag3,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice3 + "+" + voice5)
        elif set([tag4,tag5]).isdisjoint(persistent._voice_mute):
            voice(voice4 + "+" + voice5)
        elif not tag1 in persistent._voice_mute:
            voice(voice1,tag1)
        elif not tag2 in persistent._voice_mute:
            voice(voice2,tag2)
        elif not tag3 in persistent._voice_mute:
            voice(voice3,tag3)
        elif not tag4 in persistent._voice_mute:
            voice(voice4,tag4)
        elif not tag5 in persistent._voice_mute:
            voice(voice5,tag5)


    def autosave_prefix_callback():
        """Callback that overrides the autosave file prefix."""
        if persistent.game == "kimihane":
            return "auto-1-"
        elif persistent.game == "kimikara":
            return "auto-2-"
        else:
            return "auto-"

    config.autosave_prefix_callback = autosave_prefix_callback


    def file_slotname_callback(page,name):
        """[dmc] Don't use numbered pages like version 1.x anymore,
        use new and different quick pages instead
        """
        if page == "quick":
            if persistent.game == "kimihane":
                return "quick-1-" + name
            elif persistent.game == "kimikara":
                return "quick-2-" + name
        
        return page + "-" + name

    config.file_slotname_callback = file_slotname_callback


    def file_last_line(dict):
        """Add keys that contain info of the most recent line of dialogue.
        This info will be displayed in the file screen at one-half the text
        size.
        """
        
        
        dict["game"] = persistent.game
        
        
        
        dict["language"] = _preferences.language
        
        
        
        dict["last_what"] = renpy.filter_text_tags(_last_say_what,deny=["size"])
        
        
        
        if _last_say_kwargs.get("last_what_size") is not None:
            dict["last_what_size"] = _last_say_kwargs.get("last_what_size")
        
        
        if _last_say_who:
            if _last_say_kwargs.get("show_name") is None: 
                
                
                last_who_char = globals().get(_last_say_who)
                if isinstance(last_who_char,ADVCharacter):
                    dict["last_who"] = last_who_char.name
                else:
                    dict["last_who"] = None
            elif isinstance(_last_say_kwargs.get("show_name"),str):
                dict["last_who"] = _last_say_kwargs.get("show_name")
        else: 
            dict["last_who"] = None
        
        dict["last_kwargs"] = _last_say_kwargs

    config.save_json_callbacks = [file_last_line]


    def image_reset(event,interact=True,**kwargs):
        """Callback to unset side_image after each interaction.
    
        Due to issues with side image zorder with respect to the quick menu,
        override the entire side image system and draw the side image in the
        say screen. Set side_image to a displayable in the script, which will
        be drawn in the say screen. It is reset to Null() after every
        interaction.
        """
        
        global side_image
        
        if not interact:
            return
        
        if event == "end":
            side_image = Null()

    config.all_character_callbacks.append(image_reset)



    @renpy.pure
    def QuickSave(page_num,message=_("Quick save complete."), newest=False, screenshot=True):
        
        rv = [FileSave(1, page=str(page_num), confirm=False, cycle=True, newest=newest)]
        if message:
            rv.append(Notify(message))
        
        rv[0].alt = _("Quick save.")
        
        
        if screenshot and not getattr(renpy.context(), "_menu", False):
            rv.insert(0, FileTakeScreenshot())
        
        return rv


    @renpy.pure
    def QuickLoad(page_num,confirm=True):
        
        rv = FileLoad(1, page=str(page_num), confirm=confirm, newest=False)
        rv.alt = _("Quick load.")
        
        return rv


    def FileSlotName(slot, slots_per_page, auto="a", quick="q", format="%s%d"):
        """Override the FileSlotName action.
        Kimihane uses pages 1-5, Kimikara uses pages 6-10.
        """
        
        page = persistent._file_page
        prefix = ""
        
        try:
            
            if int(page) > 5:
                page = int(page) - 6
            else:
                page = int(page) - 1
        except ValueError:
            if page.startswith("auto-"):
                prefix = auto
                page = 0
            elif page.startswith("quick-"):
                prefix = quick
                page = 0
        
        return format % (prefix, page * slots_per_page + slot)


    @renpy.pure
    class FilePageCheck(Action):
        """[dmc] A custom action to fix the file page if the current page
        is not within the range of the current game.
        """
        
        def __init__(self):
            self.page = persistent._file_page
        
        def __call__(self):
            if persistent.game == "kimihane":
                try:
                    if int(self.page) > 5:
                        persistent._file_page = '1'
                except ValueError:
                    if self.page not in ["auto-1","quick-1"]:
                        persistent._file_page = '1'
            
            elif persistent.game == "kimikara":
                try:
                    if int(self.page) < 6:
                        persistent._file_page = '6'
                except ValueError:
                    if self.page not in ["auto-2","quick-2"]:
                        persistent._file_page = '6'






















init -10 python hide:


    if persistent.first_run is None:
        old_saves = renpy.list_slots("^11-")
        for i in old_saves:
            renpy.rename_save(i,"auto-1-" + i[3:])
        
        old_saves = renpy.list_slots("^12-")
        for i in old_saves:
            renpy.rename_save(i,"auto-2-" + i[3:])
        
        old_saves = renpy.list_slots("^13-")
        for i in old_saves:
            renpy.rename_save(i,"quick-1-" + i[3:])
        
        old_saves = renpy.list_slots("^14-")
        for i in old_saves:
            renpy.rename_save(i,"quick-2-" + i[3:])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
