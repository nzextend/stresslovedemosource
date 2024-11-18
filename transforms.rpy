# StressLove Transforms

image main_menu_title:
    contains:
        "mod_assets/gui/title/" + "S-.png"
        main_menu_title_effect(100, .75)
    contains:
        "mod_assets/gui/title/" + "e-.png"
        main_menu_title_effect(110, .825)
    contains:
        "mod_assets/gui/title/" + "c.png"
        main_menu_title_effect(120, .9)
    contains:
        "mod_assets/gui/title/" + "r.png"
        main_menu_title_effect(130, .975)
    contains:
        "mod_assets/gui/title/" + "e.png"
        main_menu_title_effect(140, 1.05)
    contains:
        "mod_assets/gui/title/" + "t.png"
        main_menu_title_effect(150, 1.125)
    contains:
        "mod_assets/gui/title/" + "F.png"
        main_menu_title_effect(155, 1.2)
    contains:
         "mod_assets/gui/title/" + "i.png"
         main_menu_title_effect(160, 1.275)
    contains:
        "mod_assets/gui/title/" + "l.png"
        main_menu_title_effect(165, 1.35)
    contains:
        "mod_assets/gui/title/" + "-e.png"
        main_menu_title_effect(170, 1.425)
    contains:
        "mod_assets/gui/title/" + "s.png"
        main_menu_title_effect(185, 1.5)
    contains:
        "mod_assets/gui/title/" + "overlay.png"
        xalign .00
        yalign 1.05


transform textbox_show_transform:
    alpha .00 yoffset 50 subpixel True
    easein_quint .65 alpha 1.00 yoffset 0
transform textbox_normal_transform:
    alpha 1.00 yoffset 0
transform textbox_hide_transform:
    alpha 1.00 yoffset 0 subpixel True
    easein_quint .65 alpha .00 yoffset 50

transform main_menu_transform:
    truecenter
    subpixel True
    zoom .8
    pause .05
    ease_circ 1.25 zoom 1.00
transform main_menu_noise_zoom:
    truecenter
    subpixel True
    zoom 1.4
    pause .05
    ease_circ 1.25 zoom 1.00
transform main_menu_nav_overlay:
    truecenter
    subpixel True
    xoffset -2900
    ease_circ 1.45 xoffset 0
transform main_menu_title_effect(YPOS, T):
    subpixel True
    yoffset YPOS
    pause .4
    easein_quart T yoffset 0
transform main_menu_version_effect:
    alpha .00
    pause 1.25
    easein_quint 1.1 alpha 1.00
transform main_menu_nav_effect(N):
    alpha .00
    pause N
    easein .25 alpha .58
transform main_menu_nav_transform:
    alpha .58
    on hover:
        easein .2 alpha 1.00
    on idle:
        easein .2 alpha .58

transform confirm_window_transform:
    subpixel True
    alpha .00
    zoom .85
    easein_quint .45 alpha 1.00 zoom 1.00
    on hide:
        easein .15 alpha .00 zoom .95
transform confirm_window_overlay_fade:
    alpha .00
    easein .15 alpha .4
    on hide:
        easein .15 alpha .00

transform game_menu_transform:
    subpixel True
    xoffset -50
    alpha .00
    easein_circ .3 alpha 1.00 xoffset 0
    on hide:
        easein_quint .35 alpha .00 xoffset -50

transform pref_menu_label_transform:
    subpixel True
    xoffset -50
    alpha .00
    easein_circ .3 alpha .58 xoffset 0
    on hide:
        easein_quint .35 alpha .00 xoffset -50

transform black_fadeout(t):
    truecenter
    alpha .00
    zoom 3
    easein t alpha 1.00

transform episode_img_transform:
    subpixel True
    xoffset 50
    alpha .00
    pause .5
    easein_circ .3 alpha 1.00 xoffset 0
    on hide:
        easein_quint .35 alpha .00 xoffset 50

transform main_menu_profile_effect:
    pos(1794, 63) subpixel True
    alpha .00
    pause .6
    xoffset 125
    easein_quint 1.1 xoffset 0 alpha 1.00

transform saves_menu_transform:
    truecenter
    subpixel True
    zoom 1.00
    alpha .8
    on hover:
        easein_quint .4 alpha 1.00 zoom .95
    on idle:
        easein_quint .4 alpha .8 zoom 1.00

transform profile_transform:
    subpixel True
    alpha .00
    parallel:
        ease .3 alpha 1.00
    parallel:
        yoffset -54
        easein_quint .6 yoffset -25
    on hide:
        parallel:
            easein .175 alpha .00
        parallel:
            yoffset -25
            easein_quint .6 yoffset -37

transform choice_button_transform:
    subpixel True
    alpha .00
    yoffset 30
    easein_circ .5 alpha .95 yoffset 0
    on hide:
        easein .3 alpha .00

transform shatter(duration=1.0):
    parallel:
        linear duration xzoom 0.1
    parallel:
        linear duration yzoom 0.1
    parallel:
        linear duration xpos 0.2
    parallel:
        linear duration ypos 0.8
    parallel:
        linear duration alpha 0.0

transform perfectxd(duration=1.0):
    alpha 0.0  
    linear duration alpha 1.0  

transform glitchxd:
    parallel:
        easein .1 xalign 0.8
        easeout .1 xalign 0.5
        easein .1 xalign 0.2
        pause 0.1
        easeout .1 xalign 0.5
        
    parallel:
        easein .05 yalign 0.52
        easeout .05 yalign 0.48
        pause 0.05
        easeout .05 yalign 0.5
    
    parallel:
        linear 0.1 alpha 0.8
        linear 0.05 alpha 0.6
        linear 0.05 alpha 0.9
        linear 0.05 alpha 0.5
        pause 0.1
        linear 0.1 alpha 1.0
    repeat


transform text3069:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0

transform shake:
    xpos 0.5
    ypos 0.5
    linear 0.05 xpos 0.48
    linear 0.05 xpos 0.52
    linear 0.05 xpos 0.48
    linear 0.05 xpos 0.52
    linear 0.05 xpos 0.48
    linear 0.05 xpos 0.52
    linear 0.05 xpos 0.5

transform distort:
    xzoom 1.0
    yzoom 1.0
    rotate 0
    parallel:
        # Искажение по x и y
        linear 0.1 xzoom 1.2 yzoom 0.8 rotate -10
        linear 0.1 xzoom 0.8 yzoom 1.2 rotate 10
        linear 0.1 xzoom 1.1 yzoom 0.9 rotate -5
        linear 0.1 xzoom 0.9 yzoom 1.1 rotate 5
        linear 0.1 xzoom 1.0 yzoom 1.0 rotate 0
    repeat

transform faded:
    on show:
        alpha 0.0
        linear 1.0 alpha 1.0



transform VHSEffect:
    xpos 0.5
    ypos 0.5
    alpha 1.0
    parallel:
            linear 0.05 xpos 0.51
            linear 0.05 xpos 0.49
    parallel:
            linear 0.1 xoffset 5
            linear 0.1 xoffset -5
    parallel:
            linear 0.1 ypos 0.52
            linear 0.1 ypos 0.48

transform camsway:
    xoffset 0
    yoffset 0
    parallel:
        linear 1.0 xoffset 10
        linear 1.0 xoffset -10
        linear 1.0 xoffset 10
        linear 1.0 xoffset -10
    parallel:
        linear 1.0 yoffset 10
        linear 1.0 yoffset -10
        linear 1.0 yoffset 10
        linear 1.0 yoffset -10
    repeat

transform fast_sway:
    xalign 0.5
    yalign 0.5
    parallel:
            linear 0.1 xalign 0.55
            linear 0.1 xalign 0.45
            linear 0.1 xalign 0.55
            linear 0.1 xalign 0.45
    parallel:
            linear 0.1 yalign 0.55
            linear 0.1 yalign 0.45
            linear 0.1 yalign 0.55
            linear 0.1 yalign 0.45
    repeat

transform full_screen_sway:
    xzoom 1.0
    yzoom 1.0
    xoffset 0.0
    yoffset 0.0
    parallel:
            linear 0.1 xoffset 0.1
            linear 0.1 xoffset -0.1
            linear 0.1 xoffset 0.1
            linear 0.1 xoffset -0.1
    parallel:
            linear 0.1 yoffset 0.1
            linear 0.1 yoffset -0.1
            linear 0.1 yoffset 0.1
            linear 0.1 yoffset -0.1
    repeat

transform spin:
    xalign 0.5
    yalign 0.5
    rotate 0
    parallel:
            linear 1.0 rotate 360
    repeat

transform LEffectFULL:
    xalign 0.5
    yalign 0.5
    xzoom 1.0
    yzoom 1.0
    rotate 0
    alpha 1.0
    parallel:
            linear 0.1 xzoom 1.2
            linear 0.1 xzoom 0.8
            linear 0.1 xzoom 1.1
            linear 0.1 xzoom 0.9
            linear 0.1 xzoom 1.0
    parallel:
            linear 0.1 yzoom 1.2
            linear 0.1 yzoom 0.8
            linear 0.1 yzoom 1.1
            linear 0.1 yzoom 0.9
            linear 0.1 yzoom 1.0
    parallel:
            linear 0.1 rotate 10
            linear 0.1 rotate -10
            linear 0.1 rotate 5
            linear 0.1 rotate -5
            linear 0.1 rotate 0
    repeat

transform CDWEffectTransition:
    xalign 0.5
    yalign 0.5
    xzoom 1.0
    yzoom 1.0
    rotate 0
    alpha 1.0
    parallel:
            linear 0.1 xalign 0.55
            linear 0.1 xalign 0.45
            linear 0.1 xalign 0.55
            linear 0.1 xalign 0.45
    parallel:
            linear 0.1 yalign 0.55
            linear 0.1 yalign 0.45
            linear 0.1 yalign 0.55
            linear 0.1 yalign 0.45
    parallel:
            linear 0.05 xzoom 1.1 yzoom 0.9
            linear 0.05 xzoom 0.9 yzoom 1.1
            linear 0.05 xzoom 1.0 yzoom 1.0
    repeat

transform resize960:
    zoom 960.0 / 1920.0 

transform bezierTF:
    xpos 0.0 ypos 0.0
    linear 0.5 xpos 0.25 ypos 0.5
    linear 0.5 xpos 0.5 ypos 0.0
    linear 0.5 xpos 0.75 ypos 0.5
    linear 0.5 xpos 1.0 ypos 1.0
    
# DDLC Transforms
transform zoom_in_transform():
    size (0.5, 0.5)
    linear 1.0 size (1.0, 1.0)

transform tcommon(x=640, z=0.80):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03

transform tinstant(x=640, z=0.80):
    xcenter x yoffset 0 zoom z*1.00 alpha 1.00 yanchor 1.0 ypos 1.03


transform focus(x=640, z=0.80):
    yanchor 1.0 ypos 1.03 subpixel True
    on show:

        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.05 alpha 1.00
        yanchor 1.0 ypos 1.03
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.05
        parallel:
            easein .15 yoffset 0


transform sink(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .5 ypos 1.06


transform hop(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .1 yoffset -20
    easeout .1 yoffset 0


transform hopfocus(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.05 alpha 1.00 subpixel True
    easein .1 yoffset -21
    easeout .1 yoffset 0


transform dip(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 yoffset 25
    easeout .25 yoffset 0



transform panic(x=640, z=0.80):
    xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    parallel:
        ease 1.2 yoffset 25
        ease 1.2 yoffset 0
        repeat
    parallel:
        easein .3 xoffset 20
        ease .6 xoffset -20
        easeout .3 xoffset 0
        repeat


transform leftin(x=640, z=0.80):
    xcenter -300 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x


transform rightin(x=640, z=0.80):
    xcenter 2000 yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
    easein .25 xcenter x


transform thide(z=0.80):
    subpixel True
    transform_anchor True
    on hide:

        easein .25 zoom z*0.95 alpha 0.00 yoffset -20


transform lhide:
    subpixel True
    on hide:
        easeout .25 xcenter -300


transform rhide:
    subpixel True
    on hide:
        easeout .25 xcenter 2000




transform t41:
    tcommon(200)
transform t42:
    tcommon(493)
transform t43:
    tcommon(786)
transform t44:
    tcommon(1080)
transform t31:
    tcommon(240)
transform t32:
    tcommon(640)
transform t33:
    tcommon(1040)
transform t21:
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(640)


transform i41:
    tinstant(200)
transform i42:
    tinstant(493)
transform i43:
    tinstant(786)
transform i44:
    tinstant(1080)
transform i31:
    tinstant(240)
transform i32:
    tinstant(640)
transform i33:
    tinstant(1040)
transform i21:
    tinstant(400)
transform i22:
    tinstant(880)
transform i11:
    tinstant(640)


transform f41:
    focus(200)
transform f42:
    focus(493)
transform f43:
    focus(786)
transform f44:
    focus(1080)
transform f31:
    focus(240)
transform f32:
    focus(640)
transform f33:
    focus(1040)
transform f21:
    focus(400)
transform f22:
    focus(880)
transform f11:
    focus(640)


transform s41:
    sink(200)
transform s42:
    sink(493)
transform s43:
    sink(786)
transform s44:
    sink(1080)
transform s31:
    sink(240)
transform s32:
    sink(640)
transform s33:
    sink(1040)
transform s21:
    sink(400)
transform s22:
    sink(880)
transform s11:
    sink(640)


transform h41:
    hop(200)
transform h42:
    hop(493)
transform h43:
    hop(786)
transform h44:
    hop(1080)
transform h31:
    hop(240)
transform h32:
    hop(640)
transform h33:
    hop(1040)
transform h21:
    hop(400)
transform h22:
    hop(880)
transform h11:
    hop(640)


transform hf41:
    hopfocus(200)
transform hf42:
    hopfocus(493)
transform hf43:
    hopfocus(786)
transform hf44:
    hopfocus(1080)
transform hf31:
    hopfocus(240)
transform hf32:
    hopfocus(640)
transform hf33:
    hopfocus(1040)
transform hf21:
    hopfocus(400)
transform hf22:
    hopfocus(880)
transform hf11:
    hopfocus(640)


transform d41:
    dip(200)
transform d42:
    dip(493)
transform d43:
    dip(786)
transform d44:
    dip(1080)
transform d31:
    dip(240)
transform d32:
    dip(640)
transform d33:
    dip(1040)
transform d21:
    dip(400)
transform d22:
    dip(880)
transform d11:
    dip(640)


transform l41:
    leftin(200)
transform l42:
    leftin(493)
transform l43:
    leftin(786)
transform l44:
    leftin(1080)
transform l31:
    leftin(240)
transform l32:
    leftin(640)
transform l33:
    leftin(1040)
transform l21:
    leftin(400)
transform l22:
    leftin(880)
transform l11:
    leftin(640)


transform r41:
    rightin(200)
transform r42:
    rightin(493)
transform r43:
    rightin(786)
transform r44:
    rightin(1080)
transform r31:
    rightin(240)
transform r32:
    rightin(640)
transform r33:
    rightin(1040)
transform r21:
    rightin(400)
transform r22:
    rightin(880)
transform r11:
    rightin(640)


transform face(z=0.80, y=500):
    subpixel True
    xcenter 640
    yanchor 1.0 ypos 1.03
    yoffset y
    zoom z*2.00


transform cgfade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0


transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0


transform n_cg2_wiggle_loop:
    n_cg2_wiggle
    1.0
    repeat



transform n_cg2_zoom:
    subpixel True
    truecenter
    xoffset 0
    easeout 0.20 zoom 2.5 xoffset 200


define dissolve = Dissolve(0.25)


define dissolve_cg = Dissolve(0.75)
define dissolve_scene = Dissolve(1.0)


define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])


define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])


define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])


define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])


define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])


define wipeleft = ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64)


define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/menu/wipeleft.png", 0.5, ramplen=64),
    True])



define tpause = Pause(0.25)


image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat


transform noise_alpha:
    alpha 0.25


transform noisefade(t=0):
    alpha 0.0
    t
    linear 5.0 alpha 0.40


image vignette:
    truecenter
    "images/bg/vignette.png"


transform vignettefade(t=0):
    alpha 0.0
    t
    linear 25.0 alpha 1.00


transform vignetteflicker(t=0):
    alpha 0.0
    t + 2.030
    parallel:
        alpha 1.00
        linear 0.2 alpha 0.8
        0.1
        alpha 0.7
        linear 0.1 alpha 1.00
        alpha 0.0
        1.19
        repeat
    parallel:
        easeout 20 zoom 3.0


transform layerflicker(t=0):
    truecenter
    t + 2.030
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat


transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat
