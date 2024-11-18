init offset = -1












define -2 text_outline_color = "#000000"




style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/Fonts03X/DelaGothicOne.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#000000", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size







style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True






style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
















screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                if (len(_history_list) == 0) or (len(_history_list) > 0 and not who == _history_list[-1].who):
                    at whoanim
                style "namebox"
                text who id "who"



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

transform whoanim:
    zoom 1.05
    easein 0.5 zoom 1


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Transform("gui/textbox.png", xalign=0.5, yalign=1.0)

style window_monika is window:
    background Transform("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]


style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0 zoom 1.1  
        easein 0.75 alpha 0.5 xoffset -5 zoom 1.0  
        repeat











image input_caret:
    Solid("#ffffff")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

        text prompt style "input_prompt"
        input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5

















screen choice(items):
    style_prefix "choice"

    vbox:

        for i in items:

            if "kwargs=" in i.caption:

                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:

                    $ kwarg = kwarg.replace(", ", ",").split(",")

                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')

                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]

                    textbutton caption:
                        idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)), gui.choice_button_borders)
                        hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, "#fff")), gui.choice_button_borders)
                        action i.action

                else:

                    textbutton caption:
                        style kwarg
                        action i.action

            else:

                textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    idle_background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)







transform hover_up:
    zoom 1.0
    xoffset 0
    yoffset 0

    on hover:
        easeout_cubic 0.3 zoom 1.1 yoffset -12 # Плавный "вход" с увеличением и смещением
        easein_bounce 0.4 zoom 1.0 yoffset 0 # Возвращение с эффектом «отскока»

    on idle:
        easein_quad 0.4 zoom 1.0 yoffset 0 # Плавное возвращение к норме


screen quick_menu():


    zorder 100

    if quick_menu:


        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995


            textbutton _("История") action ShowMenu('history') at hover_up
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True) at hover_up
            textbutton _("Авто") action Preference("auto-forward", "toggle") at hover_up
            textbutton _("Сохранить") action ShowMenu('save') at hover_up
            textbutton _("Загрузить") action ShowMenu('load') at hover_up


            textbutton _("Настройки") action ShowMenu('preferences') at hover_up







default quick_menu = True




style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []



transform hover_side:
    zoom 1.0 xoffset 0 yoffset 0
    on hover:
        easeout_back 0.3 xoffset 15 zoom 1.05
        easein_elastic 0.5 xoffset 0 zoom 1.0

transform menu_move(t=1.0):
    on show:
        subpixel True
        xpos -200 alpha 0.0
        easeout_quad 0.5 xpos 80 alpha 1.0 zoom 1.05
        easein_quad 0.2 zoom 1.0

    on hide:
        subpixel True
        easeout_back 0.5 xpos 400 alpha 0.5 zoom 1.1 
        easein_quad 0.5 xpos 750 alpha 0.0 

    on replace:
        subpixel True
        xpos -390 alpha 0.0
        easeout_quad t xpos 80 alpha 1.0 zoom 1.05
        easein_quad 0.2 zoom 1.0

    on replaced:
        subpixel True
        easeout_back t xpos 400 zoom 1.1 alpha 0.5
        easein_quad 0.5 xpos 750 alpha 0.0


init python:
    def FinishEnterName():
        if not player: return
        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

screen navigation():

    vbox:
        style_prefix "navigation" at menu_move

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        if not persistent.autoload or not main_menu:

            if main_menu:

                if persistent.playthrough == 1:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("Новая игра") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Пожалуйста введите свое имя", ok_action=Function(FinishEnterName))) at hover_side

            else:

                textbutton _("История") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)] at hover_side

                textbutton _("Сохранить игру") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)] at hover_side

            textbutton _("Загрузить игру") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)] at hover_side



            textbutton _("Достижения") action [ShowMenu("achievements"), SensitiveIf(renpy.get_screen("achievements") == None)] at hover_side

            textbutton _("О моде") action [ShowMenu("about"), SensitiveIf(renpy.get_screen("about") == None)] at hover_side


            if _in_replay:

                textbutton _("Закончить реплей") action EndReplay(confirm=True)

            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Главное меню") action MainMenu() at hover_side
                else:
                    textbutton _("Главное меню") action NullAction() at hover_side

            textbutton _("Настройки") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)] at hover_side



            if renpy.variant("pc"):


                textbutton _("Помощь") action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))] at hover_side


                textbutton _("Выход") action Quit(confirm=not main_menu) at hover_side
        else:
            timer 1.75 action Start("autoload_yurikill")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/fonting/Raleway-Bold.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]

    hover_outlines [(4, "#000000", 0, 0), (2, "#000000", 2, 2)]
    insensitive_outlines [(4, "#a0a0a0", 0, 0), (2, "#616161", 2, 2)]








transform menu_move_m(t=1.0):
    on show:
        subpixel True
        ease_quart t alpha 1.0
    on hide:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0
    on replace:
        subpixel True
        ypos -590
        ease_quart t ypos 640 alpha 1.0
    on replaced:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0

transform menu_move_s(t=1.0):
    on show:
        subpixel True
        ease_quart t alpha 1.0
    on hide:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0
    on replace:
        subpixel True
        ypos -590
        ease_quart t ypos 500 alpha 1.0
    on replaced:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0

transform menu_move_n(t=1.0):
    on show:
        subpixel True
        ease_quart t alpha 1.0
    on hide:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0
    on replace:
        subpixel True
        ypos -590
        ease_quart t ypos 385 alpha 1.0
    on replaced:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0

transform menu_move_y(t=1.0):
    on show:
        subpixel True
        ease_quart t alpha 1.0
    on hide:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0
    on replace:
        subpixel True
        ypos -590
        ease_quart t ypos 335 alpha 1.0
    on replaced:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0

transform menu_move_logo(t=1.0):
    on show:
        subpixel True
        ease_quart t alpha 1.0
    on hide:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0
    on replace:
        subpixel True
        ypos -590
        ease_quart t ypos 120 alpha 1.0
    on replaced:
        subpixel True
        ease_quart t ypos -700
        ease_quart 0.3 alpha 0.0

transform rdizzy(m, t):
    subpixel True
    rotate 0
    block:
        ease 0.75 * t rotate 10 * m
        ease 0.75 * t rotate -5 * m
        ease 0.75 * t rotate 5 * m
        ease 0.75 * t rotate -3 * m
        repeat


screen main_menu():




    style_prefix "main_menu" tag menu

    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        add "menu_bg"
        add "menu_nyx_art"
        frame




        use navigation

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo" at menu_move_logo, rdizzy(.7,3)
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_particles"
        if persistent.playthrough != 4:
            add "menu_art_m" at menu_move_m
        add "menu_fade"

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#ffffff"
    size 16
    outlines []



    yfill True



style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size











transform settings_move(t=1.0):
    on show:
        subpixel True
        ypos -200 alpha 0.0  # Начальная позиция и прозрачность
        easeout_back t ypos 1 alpha 1.0 zoom 1.05  # Появление с отскоком и увеличением
        easein_quad 0.2 zoom 1.0  # Возврат к обычному размеру

    on hide:
        subpixel True
        easeout_quad 0.5 zoom 1.1 alpha 0.5 ypos 360  # Легкое увеличение перед уходом
        easein_cubic t ypos -700 alpha 0.0  # Плавное исчезновение вверх

    on replace:
        subpixel True
        ypos -200 alpha 0.0
        easeout_back t ypos 1 alpha 1.0 zoom 1.05
        easein_quad 0.2 zoom 1.0

    on replaced:
        subpixel True
        easeout_quad 0.5 zoom 1.1 alpha 0.5 ypos 360
        easein_cubic t ypos -700 alpha 0.0

screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):


    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame at settings_move:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 1.0

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    textbutton _("Вернуться"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"


style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/fonting/Raleway-Bold.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]

    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30









screen about():
    tag menu





    use game_menu(_("О моде"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "StressLove это всего лишь модификация для DDLC."
            text _("Версия [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Текущая версия {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size












screen save():
    tag menu


    use file_slots(_("Сохранить"))


screen load():
    tag menu


    use file_slots(_("Загрузить"))

init python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:



            order_reverse True



            button:
                style "page_label"


                xalign 0.5


                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing








                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page) at hover_up




style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#ffffff"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")
    idle_background Frame("gui/button/slot_idle_background.png", gui.choice_button_borders)
    hover_background Frame("gui/button/slot_hover_background.png", gui.choice_button_borders)

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []









screen preferences():
    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Параметры мода"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("Отображение экрана")
                        textbutton _("В окне") action Preference("display", "window")
                        textbutton _("Полный экран") action Preference("display", "fullscreen")

                if config.developer:
                    vbox:
                        style_prefix "radio"
                        label _("Сторона прокрутки")
                        textbutton _("Отключено") action Preference("rollback side", "disable")
                        textbutton _("Назад") action Preference("rollback side", "left")
                        textbutton _("Вперед") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Пропуски")
                    textbutton _("Всего текста") action Preference("skip", "toggle")
                    textbutton _("После выборов") action Preference("after choices", "toggle")

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Скорость текста")
                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Время авто-чтения")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("Громкость музыки")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Громкость SFX")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Тест") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Громкость голоса")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Тест") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Заглушить все"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            # Button to delete all saves
            vbox:
                spacing 10
                textbutton _("Удалить все сохранения"):
                    action [Function(delete_all_saves)]
                    style "delete_saves_button"

    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"


# Python function to delete all save files
init python:
    import os

    def delete_all_saves():
        # Delete all files in the save directory
        save_dir = renpy.save_location
        for filename in os.listdir(save_dir):
            if filename.endswith(".save") or filename.endswith(".persistent"):
                file_path = os.path.join(save_dir, filename)
                try:
                    os.remove(file_path)
                    renpy.notify(_("Все сохранения удалены."))
                except Exception as e:
                    renpy.notify(_("Ошибка при удалении сохранений: {}").format(str(e)))


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/fonting/Raleway-Bold.ttf"
    size 24
    color "#fff"
    outlines [(3, "#000000", 0, 0), (1, "#000000", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/Fonts03X/Pips.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/Fonts03X/Pips.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450










screen history():




    predict False tag menu

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("История диалогов пока что пуста на данный момент.")



style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5












































































































































































transform w_move:
    zoom 0.8
    alpha 0

    linear 0.2 zoom 1.05 alpha 1
    linear 0.1 zoom 1.0

image o_confirm:
    "gui/overlay/confirm.png"
    alpha 0  # Начальная прозрачность для анимации
    linear 0.2 alpha 1  # Плавный переход к полному отображению

screen name_input(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"

    # Отображение изображения с анимацией
    add "o_confirm" at w_move

    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:
        at w_move  # Анимация для frame
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5


        input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"






        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action at hover_up

screen dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "o_confirm"

    frame at w_move:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action at hover_up

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "o_confirm"

    frame at w_move:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        if in_sayori_kill and message == layout.QUIT:
            add "confirm_glitch" xalign 0.5

        else:
            label _(message):
                style "confirm_prompt"
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Да") action yes_action at hover_up
            textbutton _("Нет") action no_action at hover_up





style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)

    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#ffffff"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")








screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Пропуск текста...")



style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "gui/Fonts03X/DelaGothicOne.ttf"









screen notify(message):
    zorder 100
    style_prefix "notify"

    # Размещаем уведомление в верхней части экрана
    frame at notify_appear:
        # Устанавливаем положение фрейма
        xalign 0.5
        yalign 0.1  # Отступ сверху

        text message

    # Уведомление будет скрыто через 3.25 секунды
    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size








screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id


define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

