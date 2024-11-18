# Define custom styles for the Windows 11-inspired dialog
define gui.text_font = "DejaVuSans.ttf"  # Substitute with the desired font

style win11_frame:
    xpadding 40
    ypadding 20
    xalign 0.5
    yalign 0.5
    xmaximum 600
    ymaximum 400
    background Frame("#ffffff", 10, 10)  # Rounded corners with a white background

style win11_button:
    background "#0078D4"  # Windows 11 blue color for the button
    foreground "#ffffff"
    padding (10, 15)
    xalign 0.5
    font gui.text_font
    hover_background "#005a9e"  # Darker color on hover

# Terms of Service screen
screen tos_screen():
    # Background for the whole screen
    window:
        background "#ffffff"  # Full white background for the screen
    
    # Dialog box with terms and conditions
    frame:
        style "win11_frame"
        vbox:
            spacing 10

            # Title
            text "Условия использования" size 24 color "#333333" xalign 0.5

            # TOS content
            text "StressLove - это неофициальная модификация для Doki Doki Literature Club и никак не связана с Team Salvato."
            text "В этом моде также может использоваться музыка из DDLC+, Minecraft, A Dance of Fire and Ice."
            text "В данном моде могут содержаться сцены умеренного насилия, оскорбления, издевательства и социальное давление."

            # Spoiler warning
            text "И кстати, вы соглашаетесь на спойлеры из DDLC+... Вы можете скачать её с itch.io (https://ddlc.moe)." xalign 0.5
            
            # Button to agree
            textbutton "Я согласен на спойлеры.":
                action [Return(True), SetVariable("persistent.first_run", True)]
                style "win11_button"

