import PySimpleGUI as sg
import functions
import os

sg.theme('Topanga')

RUNNING = True

if not os.path.exists('series.txt'):
    with open('series.txt', 'w'):
        pass

label1 = sg.Text('Series Randomizer', font=('Helvetica', 12))
input1 = sg.InputText(key='input_series')
add_button = sg.Button('Add', key='Add_button')
list_box = sg.Listbox(values=functions.visualize_series(),
                      key='visualized_series',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button('Edit', key='Edit_button')
random_button = sg.Button('Randomize', key='Random_button')
random_result = sg.Text(key='random_result', font=('Helvetica', 16))

layout = [[label1], [input1, add_button], [
    list_box, edit_button], [random_button, random_result]]

window = sg.Window('Series Randomizer', layout)

while RUNNING:
    event, values = window.read()
    print('-----------')
    print(event)
    print('-----------')
    print(values['visualized_series'])
    match event:
        case 'Add_button':
            series = functions.visualize_series()
            new_series = values['input_series'] + "\n"
            series.append(new_series)
            functions.add_series(series)
            window['visualized_series'].update(values=series)
            window['input_series'].update(value='')
        case 'Edit_button':
            try:
                series_to_edit = values['visualized_series'][0]
                overwriting_series = values['input_series']
                series = functions.visualize_series()
                index = series.index(series_to_edit)
                series[index] = overwriting_series+'\n'
                functions.add_series(series)
                window['visualized_series'].update(values=series)
                window['input_series'].update(value='')
            except IndexError:
                sg.Popup('Please select an item first.',
                         font=("Helvetica", 16))

        case 'Random_button':
            window['random_result'].update(value=functions.random_series())
        case sg.WIN_CLOSED:
            break

window.close()
