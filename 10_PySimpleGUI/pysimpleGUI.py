import PySimpleGUI as sg

layout = [[sg.Text("Hello, PySimpleGUI!")], [sg.Button("OK")]]
window = sg.Window("Hello World", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "OK":
        break

window.close()