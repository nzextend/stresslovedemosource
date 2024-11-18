label SLG02:
    stop audio 
    play audio SLG
    scene lined
    with dissolve
    centered "Вы потерпели поражение.\nВсе данные будут стерты при нажатии."
    centered "Не стоило бы тебе на это забивать.\nТаким образом ты совершаешь большую ошибку."
    python:
            delete_all_saves()
            renpy.utter_restart()

label SLG03:
    stop audio 
    play audio SLG
    scene lined
    with dissolve
    centered "Вы потерпели поражение.\nВсе данные будут стерты при нажатии."
    centered "Ты на приколе? Добиваться ответа при помощи насилия?\nНу ты и мощь, но такой выбор тебе сейчас лучшего не дал."
    python:
            delete_all_saves()
            renpy.utter_restart()


label chanceslg:
    stop audio 
    play audio SLG
    scene lined
    with dissolve
    centered "Вы потерпели поражение.\nНо! Вам выпал второй шанс, и вы можете повторить выбор снова.\nБез потерей сохранений в моде. Прикольно, согласен?"


    label secretmsgslg:
        stop audio
        play audio SLG
        scene lined
        with dissolve

        centered "Вы потерпели поражение."
        centered "Вы потерпели поражение."
        centered "Погоди, что?"

        centered "Никс: Привет... Если ты читаешь это, значит, всё пошло не так, как планировалось."
        centered "Никс: Я надеялась, что ты сможешь меня спасти, но теперь я не уверена..."
        centered "Никс: Они следят за мной. Я не могу говорить открыто."
        centered "Никс: Если ты услышал это сообщение, знай — я всё еще борюсь."
        centered "Никс: Не сдавайся. Ты должен продолжать искать меня. Я верю в тебя."

        centered "Никс: Пожалуйста, будь осторожен. Они не дремлют..."
        return

        if renpy.keymap["e"]:
            jump secretmsgslg