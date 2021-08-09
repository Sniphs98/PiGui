import PySimpleGUI


def mov_gui():
    file_line_of_column = [
        [
            PySimpleGUI.Button(),
            PySimpleGUI.Button("▲"),
            PySimpleGUI.Button()
        ]
    ]

    second_line_of_column = [
        [
            PySimpleGUI.Button("◄"),
            PySimpleGUI.Button(),
            PySimpleGUI.Button("►")
        ]
    ]

    third_line_of_column = [
        [
            PySimpleGUI.Button(""),
            PySimpleGUI.Button(""),
            PySimpleGUI.Button("▼"),
        ]
    ]

    layout = [
        [
            PySimpleGUI.Column(file_line_of_column),
            PySimpleGUI.Column(second_line_of_column),
            PySimpleGUI.Column(third_line_of_column),
        ]
    ]

    window = PySimpleGUI.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == PySimpleGUI.WIN_CLOSED:
            break


