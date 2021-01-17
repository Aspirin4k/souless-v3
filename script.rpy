# Вы можете расположить сценарий своей игры в этом файле.
default preferences.text_cps = 15

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

define simple = Character(None, what_ypos=0.0, screen="main_text")

screen main_text(what, who):
    fixed:
        xoffset 15
        yoffset 15

        vbox:
            spacing 10

            text what id "what"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    simple "Hi!"

    extend "Hi2!"

    return
