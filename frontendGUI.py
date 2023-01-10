import PySimpleGUI as sg
import backend as b

feet_text = sg.Text("Enter feet:")
feet_input = sg.Input("Enter number", key="feets")

inches_text = sg.Text("Enter inches")
inches_input = sg.Input("Enter number", key="inches")

result = 0
result_button = sg.Button("Convert", key="converter")
result_print = sg.Text(result, key="result")
layout = [[feet_text, feet_input],
          [inches_text, inches_input],
          [result_button, result_print]]

window = sg.Window("Convertor", layout=layout)

while True:
    event, values = window.read()
    print(event, values)
    try:
        result = b.convertor(values["feets"], values["inches"])

        if event == "converter":
            values["result"] = result
            result_print.update(result)
    except:
        result_print.update("You should enter ONLY numbers")

    if event == sg.WIN_CLOSED:
        break

window.close()
