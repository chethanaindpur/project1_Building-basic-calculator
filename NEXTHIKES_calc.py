from tkinter import *
import math

# Global variables
calc_operator = ""
text_input = None

# Button click handler
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

# Clear all function
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

# Backspace function
def button_delete():
    global calc_operator
    calc_operator = calc_operator[:-1]
    text_input.set(calc_operator)

# Trigonometric functions
def trig_function(func):
    global calc_operator
    try:
        value = float(calc_operator)
        if func == 'sin':
            result = math.sin(math.radians(value))
        elif func == 'cos':
            result = math.cos(math.radians(value))
        elif func == 'tan':
            result = math.tan(math.radians(value))
        
        calc_operator = str(round(result, 10))
        text_input.set(calc_operator)
    except ValueError:
        calc_operator = "ERROR"
        text_input.set(calc_operator)

# Logarithmic functions
def log_function(func):
    global calc_operator
    try:
        value = float(calc_operator)
        if value <= 0:
            calc_operator = "ERROR"
        else:
            if func == 'log':
                result = math.log10(value)
            elif func == 'ln':
                result = math.log(value)
            
            calc_operator = str(round(result, 10))
        text_input.set(calc_operator)
    except ValueError:
        calc_operator = "ERROR"
        text_input.set(calc_operator)

# Square root function
def square_root():
    global calc_operator
    try:
        value = float(calc_operator)
        if value < 0:
            calc_operator = "ERROR"
        else:
            calc_operator = str(math.sqrt(value))
        text_input.set(calc_operator)
    except ValueError:
        calc_operator = "ERROR"
        text_input.set(calc_operator)

# Percentage function
def percentage():
    global calc_operator
    try:
        value = float(calc_operator)
        calc_operator = str(value / 100)
        text_input.set(calc_operator)
    except ValueError:
        calc_operator = "ERROR"
        text_input.set(calc_operator)

# Exponential function
def exponential():
    global calc_operator
    calc_operator += '**'
    text_input.set(calc_operator)

# Equals button function
def button_equal():
    global calc_operator
    try:
        # Safe evaluation with limited globals
        result = eval(calc_operator, 
                      {"__builtins__": None}, 
                      {
                          'math': math,
                          'sin': math.sin,
                          'cos': math.cos,
                          'tan': math.tan,
                          'log': math.log,
                          'sqrt': math.sqrt,
                          'pi': math.pi
                      })
        calc_operator = str(result)
        text_input.set(calc_operator)
    except Exception:
        calc_operator = "ERROR"
        text_input.set(calc_operator)

# Create main window
def create_calculator():
    global text_input
    
    # Main window setup
    tk_calc = Tk()
    tk_calc.configure(bg="#000000", bd=10)
    tk_calc.title("Nexthikes Scientific Calculator")
    tk_calc.geometry("350x350")
    tk_calc.resizable(False, False)

    # String variable for display
    text_input = StringVar()

    # Display entry
    text_display = Entry(
        tk_calc, 
        font=('Times new roman', 30, 'bold'), 
        textvariable=text_input,
        bd=10, 
        insertwidth=4, 
        bg='#BBB', 
        justify='left'
    )
    text_display.pack(expand=True, fill='x')

    # Button styling
    button_params = {
        'bd': 5, 
        'fg': 'white', 
        'bg': '#34495E', 
        'font': ('Times new roman', 18)
    }

    # Button layout
    button_frame = Frame(tk_calc, bg="#000000")
    button_frame.pack(expand=True, fill='both')

    # Create buttons
    buttons = [
        ['(', ')', 'C', '←', '%'],
        ['7', '8', '9', '/', 'sqrt'],
        ['4', '5', '6', '*', '^'],
        ['1', '2', '3', '-', '10^'],
        ['0', '.', '00', '+', '='],
        ['sin', 'cos', 'tan', 'log', 'ln']
    ]

    # Dynamic button creation
    for r, row in enumerate(buttons):
        for c, text in enumerate(row):
            # Special button mapping
            if text == 'C':
                cmd = button_clear_all
            elif text == '←':
                cmd = button_delete
            elif text == '%':
                cmd = percentage
            elif text == 'sqrt':
                cmd = square_root
            elif text == '^':
                cmd = exponential
            elif text == '10^':
                cmd = lambda: button_click('10**')
            elif text in ['sin', 'cos', 'tan']:
                cmd = lambda x=text: trig_function(x)
            elif text in ['log', 'ln']:
                cmd = lambda x=text: log_function(x)
            elif text == '=':
                cmd = button_equal
            else:
                cmd = lambda x=text: button_click(x)

            # Create button
            btn = Button(
                button_frame, 
                text=text, 
                command=cmd,
                **button_params
            )
            btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

        # Configure grid weights
        button_frame.grid_rowconfigure(r, weight=1)
        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)

    tk_calc.mainloop()

# Run the calculator
if __name__ == "__main__":
    create_calculator()