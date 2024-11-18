









define config.log_gl_shaders = True



define config.name = "StressLove"





define gui.show_name = True




define config.version = "1.0"





define gui.about = _("Текущая версия Ren'Py {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].")






define build.name = "StressLove"






define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = audio.t1










define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)




define config.after_load_transition = None




define config.end_game_transition = Dissolve(.5)
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75
















define config.save_directory = "StressLove"







define config.window_icon = "gui/window_icon.png"



define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 60
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)






init python:




















    build.archive("recipe", "all")
    build.archive("IMG", "all")
    build.archive("msc", "all")
    build.archive("fonts", "all")
    build.archive("quota", "all")
    build.archive("patched", "all")
    build.archive("clips", "all")
    build.archive("GIFAnim", "all")

    build.classify("game/**.mp4", "clips")
    build.classify("game/**.webm", "clips")
    build.classify("game/**.ogv", "clips") 
    build.classify("game/**.mkv", "clips")
    build.classify("game/**.avi", "clips")
    build.classify("game/**.mov", "clips")

    build.classify("game/**.gif", "GIFAnim")

    build.classify("game/**.jpg", "IMG")
    build.classify("game/**.png", "IMG")
    build.classify("game/**.webp", "IMG")
    build.classify("game/**.jpeg", "IMG")
    build.classify("game/**.tiff", "IMG")

    build.classify("/game/quota/**.jpg", "quota")
    build.classify("/game/quota/**.png", "quota")

    build.classify("/game/gui/quotaFonts/**.ttf", "quota")
    build.classify("/game/gui/quotaFonts/**.otf", "quota")

    build.classify("game/**.rpyc", "recipe")
    build.classify("game/**.txt", "recipe")
    build.classify("game/**.chr", "recipe")
    build.classify("game/**.wav", "msc")
    build.classify("game/**.mp3", "msc")
    build.classify("game/**.ogg", "msc")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "fonts")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)









    build.documentation('*.html')
    build.documentation('*.txt')

    build.include_old_themes = False











define build.itch_project = "teamsalvato/ddlc"
