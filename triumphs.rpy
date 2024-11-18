








init python:
    import math

    achievementList = []
    selectedAchievement = None











    class Achievements:
        
        def __init__(self, name, description, image, persistent, count=False, maxCount=100):
            
            self.name = name
            
            
            self.description = description
            
            
            self.image = image
            
            
            
            self.locked = im.MatrixColor(image, im.matrix.desaturate())
            
            
            self.count = count
            
            
            self.persistent = persistent
            
            
            self.maxCount = maxCount



    startup = Achievements("Добро пожаловать в StressLove!", "Спасибо что заинтересовались модом.",
            "gui/logo.png", "persistent.first_run")
    achievementList.append(startup)

    secretdesires = Achievements("Тайные желания", "Вы возбудили её и смогла разговорить то, о чём она давно молчала. \nТеперь тени стали ещё ближе... Это пиздец?",
            "mod_assets/ach/x.png", "persistent.secretdesires")
    achievementList.append(secretdesires)

    destroycorruptedworld = Achievements("Сломал игру чутка.", "Вы окончательно добили разрушение до предела, погрузив мир в непонятную хрень.",
            "mod_assets/ach/thumb.png", "persistent.destroycorruptedworld")
    achievementList.append(destroycorruptedworld)

    obt = Achievements("OutterBox Technologies", "What are they doing here?",
            "mod_assets/ach/obt.png", "persistent.obt")
    achievementList.append(obt)

    # FSL - Final StressLove, если понятнее это достижение дается до тех пор, пока не пройдешь мод.
    FSL = Achievements("То что ты должен был...", "{color=#FFFFFF}Ты прислушался к приказам неизвестной тебе личности. \nИ теперь с Моникой пара.{/color}",
            "triumphs/triumoni.png", "persistent.FSL")
    achievementList.append(FSL)

    E2R = Achievements("Двойной удар", "{color=#FFFFFF}Ваше обаяние сработало дважды! \nДва сердца покорены, и вы уверенно движетесь к вершинам любви.{/color}",
            "triumphs/e2rtriu.png", "persistent.E2R")
    achievementList.append(E2R)

    E3R = Achievements("Покоритель сердец", "{color=#FFFFFF}Ваша харизма не знает границ! Три сердца отданы вам без остатка. \nПоздравляем, вы настоящий мастер любви.{/color}",
            "triumphs/e3rtriu.png", "persistent.E3R")
    achievementList.append(E3R)














screen achievements():
    tag menu


    use game_menu(_("Достижения")):

        style_prefix "achievements"



        vbox:
            xpos 0.26
            ypos -0.1

            hbox:

                if selectedAchievement:

                    python:
                        currentVal = eval(selectedAchievement.persistent)

                        if not currentVal:
                            currentVal = False

                    if selectedAchievement.count:
                        add ConditionSwitch(
                                currentVal >= selectedAchievement.maxCount, selectedAchievement.image, "True",
                                selectedAchievement.locked) at achievement_scaler(128)
                    else:
                        add ConditionSwitch(
                                currentVal, selectedAchievement.image, "True",
                                selectedAchievement.locked) at achievement_scaler(128)
                else:
                    null height 128

                spacing 20

                vbox:
                    xsize 400
                    ypos 0.2

                    if selectedAchievement:

                        text selectedAchievement.name:
                            font gui.name_font
                            color "#fff"
                            outlines [(2, "#3d3d3d", 0, 0)]

                        if selectedAchievement.count:
                            text "[selectedAchievement.description] ([currentVal] / [selectedAchievement.maxCount])"
                        else:
                            text selectedAchievement.description
                    else:
                        null height 128


        vpgrid:
            id "avp"
            rows math.ceil(len(achievementList) / 6.0)
            cols 6

            spacing 25
            mousewheel True

            xalign 0.5
            ypos 0.2
            ysize 410

            for al in achievementList:

                python:
                    currentVal = eval(al.persistent)

                    if not currentVal:
                        currentVal = False

                if al.count:

                    imagebutton:
                        idle Transform(ConditionSwitch(
                                currentVal >= al.maxCount, al.image, "True",
                                al.locked), size=(96,96))
                        action SetVariable("selectedAchievement", al)
                else:
                    imagebutton:
                        idle Transform(ConditionSwitch(
                                currentVal, al.image, "True",
                                al.locked), size=(96,96))
                        action SetVariable("selectedAchievement", al)

        vbar value YScrollValue("avp") xalign 1.01 ypos 0.2 ysize 400

        textbutton "Подробнее":
            style "return_button"
            xpos 0.85 ypos 1.1
            action ShowMenu("dialog", "Серые иконки обозначают что достижения еще не разблокированы. А цветные - разблокированы.\nОбычно достижения разблокировать можно во время чтения сюжета.", ok_action=Hide("dialog"))

        if config.developer:
            textbutton "тест":
                style "return_button"
                xpos 0.8 ypos 1.1
                action ShowMenu("achievement_notify", startup)











screen achievement_notify(reward):

    style_prefix "achievements"

    frame at achievement_notif_transition:
        xsize 300
        ysize 100
        xpos 0.4

        has hbox:
            xalign 0.27
            yalign 0.5
            add reward.image at achievement_scaler(50)
            spacing 20
        vbox:
            spacing 5
            text "Достижение успешно выполнено!" size 16
            text reward.name size 14

    timer 5.0 action [Hide("achievement_notify"), With(Dissolve(1.0))]

style achievements_text is gui_text
style achievements_text:
    color "#000"
    outlines []
    size 20

transform achievement_scaler(x):
    size (x, x)

transform achievement_notif_transition:
    alpha 0.0
    linear 0.5 alpha 1.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
