import PySimpleGUI as sg

def make_window1():
    layout = [[sg.Text('Window 1')],
              [sg.Button('Next >'), sg.Button('Exit')]]

    return sg.Window('Window 1', layout, finalize=True).Finalize()


def make_window2():
    layout = [[sg.Text('Window 2')],
               [sg.Button('Next >'), sg.Button('Exit')]]

    return sg.Window('Window 2', layout, finalize=True).Finalize()


window1, window2 = make_window1(), None

while True:
    window, event, values = sg.read_all_windows()
    window.Maximize()
    if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
        break

    if window == window1:
        if event == 'Next >':
            window1.hide()
            window2 = make_window2()

    if window == window2 and event in (sg.WIN_CLOSED, 'Exit'):
        break


window.close()