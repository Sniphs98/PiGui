import PySimpleGUI


def mov_gui():

    x = 0
    y = 0

    file_line_of_column = [
        [
            PySimpleGUI.Button("▲"),
        ]
    ]

    second_line_of_column = [
        [
            PySimpleGUI.Button("◄"),
            PySimpleGUI.Button("   "),
            PySimpleGUI.Button("►")
        ]
    ]

    third_line_of_column = [
        [
            PySimpleGUI.Button("▼"),
        ]
    ]

    option_line = [
        [
            PySimpleGUI.Button("Exit"),
        ]
    ]

    layout = [
        [PySimpleGUI.Column(file_line_of_column, justification='center')],
        [PySimpleGUI.Column(second_line_of_column, justification='center')],
        [PySimpleGUI.Column(third_line_of_column, justification='center')],
        [PySimpleGUI.Column(option_line, justification='center')]
    ]

    window = PySimpleGUI.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == PySimpleGUI.WIN_CLOSED:
            break
        if event == "▲":
            y = y + 1
            print(y)
        if event == "▼":
            y = y - 1
            print(y)
        if event == "►":
            x = x + 1
            print(x)
        if event == "◄":
            x = x - 1
            print(x)



