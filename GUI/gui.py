import PySimpleGUI as sg

app = sg.Window("Sorting Algorithm Visualizer", [[sg.Text("Content")], [sg.Button("Exit")]])

while True:
    event, value = app.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
app.close()





if __name__ == "__main__":
    app