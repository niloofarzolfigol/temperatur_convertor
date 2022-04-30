import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Written by Niloofar Zolfigol')

fahrenheit_val = tk.StringVar()
lbl_result_f2c = ttk.Label(
    window,
    text='Result will be shown here...'
)


def conv_f2c():
    f_user_input = fahrenheit_val.get()
    try:
        f_value = float(f_user_input)
        result = round((f_value - 32) / 1.8, 1)
    except ValueError:
        if f_user_input == '':
            result = 'The input is empty...'
        else:
            result = 'You should enter a number...'
    lbl_result_f2c['text'] = result


# ============================================

lbl_fahrenheit = ttk.Label(
    window,
    text='Fahrenheit:',
)
ent_input_f2c = ttk.Entry(
    window,
    width=30,
    textvariable=fahrenheit_val
)
btn_calc_f2c = ttk.Button(
    window,
    text='Calculate F to C',
    width=15,
    command=conv_f2c,
)

lbl_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
ent_input_f2c.grid(row=0, column=1,  pady=10)
btn_calc_f2c.grid(row=0, column=2, padx=10, pady=10)

# ============================================

lbl_celsius = ttk.Label(
    window,
    text='Celsius:',
)
lbl_line = ttk.Label(
    window,
    text='_'*70,
)

lbl_celsius.grid(row=1, column=0, pady=10)
lbl_result_f2c.grid(row=1, column=1, pady=10)
lbl_line.grid(row=2, column=0, columnspan=3)

# ==================================================================================

celsius_val = tk.StringVar()
lbl_result_c2f = ttk.Label(
    window,
    text='Result will be shown here...'
)


def conv_c2f():
    c_user_input = celsius_val.get()
    try:
        c_value = float(c_user_input)
        result = round((c_value*1.8) + 32, 1)
    except ValueError:
        if c_user_input == '':
            result = 'The input is empty...'
        else:
            result = 'You should enter a number...'
    lbl_result_c2f['text'] = result


# ============================================

lbl_celsius = ttk.Label(
    window,
    text='Celsius:',
)
ent_input_c2f = ttk.Entry(
    window,
    width=30,
    textvariable=celsius_val
)
btn_calc_c2f = ttk.Button(
    window,
    text='Calculate C to F',
    width=15,
    command=conv_c2f,
)

lbl_celsius.grid(row=3, column=0, padx=10, pady=(20, 10))
ent_input_c2f.grid(row=3, column=1,  pady=(20, 10))
btn_calc_c2f.grid(row=3, column=2, padx=10, pady=(20, 10))

# ============================================

lbl_fahren = ttk.Label(
    window,
    text='Fahrenheit:',
)
lbl_fahren.grid(row=4, column=0, pady=(10, 20))
lbl_result_c2f.grid(row=4, column=1, pady=(10, 20))

# ==================================================================================


def func(*args):
    conv_c2f()
    conv_f2c()


window.bind('<Return>', func)

window.mainloop()
