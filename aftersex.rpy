transform paperappearance:
    alpha 0.0
    zoom 0.5
    easein 1.5 alpha 1.0 zoom 1.0
    on idle:
        linear 1.0 rotate -2
        linear 1.0 rotate 2


image papernyx01 = "/images/papers/papernyxaggesive.png"
image poem_special2 = "poem_special/poem_special2.png"
image poem_special3 = "poem_special/poem_special3.png"
image poem_special4 = "poem_special/poem_special4.png"
image poem_end = ConditionSwitch(
    "persistent.clearall == True", "poem_special/poem_end_clearall.png",
    "True", "poem_special/poem_end.png")

label nyxexterasex:
    $ quick_menu = False
    play sound page_turn
    show papernyx01 at paperappearance
    $ pause()
    $ quick_menu = True
    return
label poem_special_2:
    $ quick_menu = False
    play sound page_turn
    show poem_special2 with Dissolve(1.0)
    $ pause()
    play sound "sfx/giggle.ogg"
    $ quick_menu = True
    return
label poem_special_3:
    $ quick_menu = False
    play sound page_turn
    show poem_special3 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
label poem_special_4:
    $ quick_menu = False
    play sound page_turn
    show poem_special4 with Dissolve(1.0)
    $ pause()
    $ quick_menu = True
    return
