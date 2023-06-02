import tkinter as tk
import winsound

# Create an empty list to store the calculations
calculations = []

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))
    play_button_sound()

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        calculations.append(entry.get() + ' = ' + str(result))  # Add the calculation to the list of calculations
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def play_button_sound():
    winsound.PlaySound("button_click.wav", winsound.SND_ASYNC)

# Function to display the calculations in a separate area
def display_calculations():
    calculation_window = tk.Toplevel(window)
    calculation_window.title("Calculation History")

    # Create a label for each calculation and pack them vertically
    for i, calculation in enumerate(calculations):
        label = tk.Label(calculation_window, text=f"Calculation {i+1}: {calculation} ", font=('Arial', 16))
        label.pack(padx=10, pady=5)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the entry field
entry = tk.Entry(window, width=20, font=('Arial', 12))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
for i in range(1, 10):
    button = tk.Button(window, text=str(i), width=5, height=2, font=('Arial', 12),
                       command=lambda num=i: button_click(num),bg='blue')
    button.grid(row=(9 - i) // 3 + 1, column=(i - 1) % 3)

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, width=5, height=2, font=('Arial', 12),
                       command=lambda op=operator: button_click(op))
    button.grid(row=i + 1, column=3)

# Create additional buttons
button_zero = tk.Button(window, text='0', width=5, height=2, font=('Arial', 12),
                        command=lambda: button_click(0))
button_zero.grid(row=4, column=0)

button_clear = tk.Button(window, text='C', width=5, height=2, font=('Arial', 12),
                         command=button_clear)
button_clear.grid(row=4, column=1)

button_equal = tk.Button(window, text='=', width=5, height=2, font=('Arial', 12),
                         command=button_equal)
button_equal.grid(row=4, column=2)

# Create a button to display the calculations
button_history = tk.Button(window, text='Show History', width=12, height=2, font=('Arial', 12),
                           command=display_calculations)
button_history.grid(row=5, column=0, columnspan=3, pady=10)

# Start the main event loop
window.mainloop()
   