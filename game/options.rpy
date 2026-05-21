define config.name = _("Wanting Wings")
define gui.show_name = True
define config.version = "2.0"
define build.name = "WantingWings"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.main_menu_music = audio.bgm03

define config.after_load_transition = Fade(0.5,1.0,0.5)
define config.end_game_transition = Fade(0.5,1.0,0.5)
define config.enter_transition = Dissolve(0.5)
define config.exit_transition = Dissolve(0.5)
define config.intra_transition = Dissolve(0.25)
define config.enter_yesno_transition = Dissolve(0.25)
define config.exit_yesno_transition = Dissolve(0.25)
define config.main_game_transition = Fade(0.5,1.0,0.5)
define config.game_main_transition = Fade(0.5,1.0,0.5)
define config.enter_replay_transition = Fade(0.5,1.0,0.5)
define config.exit_replay_transition = Fade(0.5,1.0,0.5)

define config.voice_filename_format = "voice/{filename}.opus"

define config.default_music_volume = 0.75
define config.default_sfx_volume = 0.65
define config.default_voice_volume = 1.0

define config.thumbnail_width = 120
define config.thumbnail_height = 90

init python:
    renpy.music.register_channel("bgv","bgv",loop=True,tight=True)
    renpy.music.register_channel("sound2","sfx",loop=False,tight=True)

define config.window = "auto"
define config.history_length = 250

define config.save_token_keys = ['MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEpXxVwOQ2iXG4+jZfAl/HKiS+iqJYrYu3ib2FO9Cg49xAiCME00mJwVPbhUshDnwg0E2A20wJwTqk6vcbB2on9Q==']

default preferences.text_cps = 0
default preferences.afm_time = 15
default persistent.read_text_instant = True
default persistent.read_text_recolor = True
default persistent.read_choices_recolor = True
default persistent.auto_after_choices = True
default preferences.skip_after_choices = True

default preferences.emphasize_audio = True
default persistent.emphasize_audio_volume = 0.68
default persistent.window_opacity = 0.5

default persistent.game = None
default persistent.hina_fumi_clear1 = False
default persistent.rin_hina_clear1 = False
default persistent.fumi_rin_clear1 = False
default persistent.angel_clear = False
default persistent.hina_fumi_clear2 = False
default persistent.rin_hina_clear2 = False
default persistent.fumi_rin_clear2 = False
default persistent.miyako_sachiko_clear = False
default route1 = 0
default route2 = 0
default routes_cleared = 0
default hina_fumi_score = 0
default rin_hina_score = 0
default side_image = Null()
default persistent.kimihane_menu_status = 0
default persistent.kimikara_menu_status = 0
default persistent.main_menu_status = 0


default persistent.first_run = None
default persistent.layer_shaken = False
default persistent.dpatch = None



default rin_pyjama = "pyjama_a"
default hina_choker = ""
default miyako_scarf = ""

define config.save_directory = "Wanting Wings"
define config.window_icon = "gui/window_icon.png"


init python:
    if renpy.loadable('define_dpatch.rpyc') and renpy.loadable('images/warning.webp'):
        persistent.dpatch = True
    else:
        persistent.dpatch = False

    build.package('dpatch','zip',file_lists=['dpatch'])
    build.package('pc-patched','zip',file_lists=['dpatch','all','renpy','windows','linux'])
    build.package('mac-patched','app-zip',file_lists=['dpatch','all','renpy','mac'])
    build.package('linux-patched','tar.bz2',file_lists=['dpatch','all','renpy','linux'])
    build.package('android-patched','directory',file_lists=['dpatch','android','all'])





    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/sync.*', None)
    build.classify('**/desktop.ini',None)
    build.classify('**/*.rpy',None)
    build.classify('**/*.log',None)
    build.classify('dist/**', None)
    build.classify('__pycache__/**', None)
    build.classify('.vscode/**', None)
    build.classify('_engine_runtimes_backup/**', None)
    build.classify('_temp_assets_backup/**', None)
    build.classify('_temp_dpatch_backup/**', None)
    build.classify('game/cache/**', None)
    build.classify('game/saves/**', None)
    build.classify('*.keystore', None)
    build.classify('android.json', None)
    build.classify('android-**.png', None)
    build.classify('log.txt', None)
    build.classify('traceback.txt', None)
    build.classify('upload_log.txt', None)

    build.archive('images')
    build.archive('gui')
    build.archive('audio')
    build.archive('script')
    build.archive('assets_dpatch','dpatch')
    build.archive('script_dpatch','dpatch')


    build.classify('game/images/rin/rin_3**znd**.webp','images')

    build.classify('game/*_dpatch.rpyc','script_dpatch')
    build.classify('game/*_d.rpyc','script_dpatch')
    build.classify('**/images/warning.webp','assets_dpatch')
    build.classify('game/images/**znd**.webp','assets_dpatch')
    build.classify('game/images/**curtain**.webp','assets_dpatch')
    build.classify('**/ev07**.webp','assets_dpatch')
    build.classify('**/ev08**.webp','assets_dpatch')
    build.classify('**/ev09**.webp','assets_dpatch')
    build.classify('**/ev10**.webp','assets_dpatch')
    build.classify('**/ev11**.webp','assets_dpatch')
    build.classify('**/ev12**.webp','assets_dpatch')
    build.classify('**/kimihane_16**.webp','assets_dpatch')
    build.classify('game/images/kimikara_02d**.webp','assets_dpatch')
    build.classify('game/gui/thumbs/kimikara_02t_alt.webp','assets_dpatch')
    build.classify('**/kimikara_12**.webp','assets_dpatch')
    build.classify('**/kimikara_13**.webp','assets_dpatch')
    build.classify('**/kimikara_14**.webp','assets_dpatch')
    build.classify('**/kimikara_15**.webp','assets_dpatch')
    build.classify('**/kimikara_16**.webp','assets_dpatch')
    build.classify('**/kimikara_17**.webp','assets_dpatch')
    build.classify('**/kimikara_18**.webp','assets_dpatch')
    build.classify('game/voice/d/*.opus','assets_dpatch')

    build.classify('game/gui/**','gui')
    build.classify('**/*.ttc','images')
    build.classify('**/*.ttf','images')
    build.classify('**/*.webp','images')
    build.classify('**/*.opus','audio')
    build.classify('**/*_ren.py','script')
    build.classify('**/*.py',None) 
    build.classify('**/*.rpyc','script')
    build.classify('**/*.rpym','script')

    build.documentation('*.html')
    build.documentation('*.rtf')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
