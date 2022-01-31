import tkinter as tk
from tkinter import ttk

data = {
    'latte': {'cost': 2.50},
    'espresso': {'cost': 1.50},
    'cappuccino': {'cost': 3.00}
}

bank_balance = 0


# bank_balance = float(bank_balance)

def latte_entry():
    print('latte ($2.50) button was clicked')
    order_item.set('Latte ($2.50)')


def espresso_entry():
    print('expresso ($1.50) button was clicked')
    order_item.set("Expresso ($1.50)")


def cappuccino_entry():
    print('cappuccino ($3.00) button was clicked')
    order_item.set("Cappuccino ($3.00)")


# price button

def two_doller():
    print('2$ clicked')
    global bank_balance
    bank_balance += 2
    bank.set(bank_balance)


def one_doller():
    print('$1 is clicked')
    global bank_balance
    bank_balance += 1
    bank.set(bank_balance)


def quarter():
    print('$0.25 is clicked')
    global bank_balance
    bank_balance += 0.25
    bank.set(bank_balance)


# payment done

def make_drink():
    make_drink = order_item.get()
    print(make_drink)
    while True:
        while True:
            global bank_balance
            if make_drink == 'Latte ($2.50)' and bank_balance >= 2.5:
                bank_balance -= 2.5
                bank.set(bank_balance)
                payment_done.set('Enjoy your Latte')
                break
            elif make_drink == 'Expresso ($1.50)' and bank_balance >= 1.50:
                bank_balance -= 1.50
                bank.set(bank_balance)
                payment_done.set('Enjoy your Expresso')
                break
            elif make_drink == 'Cappuccino ($3.00)' and bank_balance >= 3:
                bank_balance -= 3
                bank.set(bank_balance)
                payment_done.set('Enjoy your Cappuccino')
                break
            else:
                payment_done.set('Insufficient Money')
                break
        break


# 1. Make a root window
root = tk.Tk()
root.title("Coffee Machine")
root.iconbitmap(r'coffee_root_icon.ico')
root.geometry('416x340')

# 2. Make the main frame
window_frame = tk.Frame(root, background='#817bbd')
window_frame.pack(fill=tk.BOTH, expand=True)

# 3. Make labels
tk.Label(window_frame, text='Welcome to the Coffee Machine!', font=15, background='#817bbd', justify='center').grid(columnspan=5, row=1, pady=(10, 10))

# 4. Make the Menu Buttons
latte = (tk.Button(window_frame, text='Latte ($2.50)', command=latte_entry, justify='center').grid(column=1, row=3, pady=(10, 10), padx=15))
espresso = (tk.Button(window_frame, text='Espresso ($1.50)', command=espresso_entry, justify='center').grid(column=2, row=3, pady=(10, 10)))
cappuccino = (tk.Button(window_frame, text='Cappuccino ($3.00)', command=cappuccino_entry, justify='center').grid(column=3, row=3, pady=(10, 10)))

# 4.1 Make the Price Buttons
price_1 = (tk.Button(window_frame, text='$2.00', command=two_doller, justify='center').grid(column=1, row=4, ipadx=15, pady=(10, 10)))
price_2 = (tk.Button(window_frame, text='$1.00', command=one_doller, justify='center').grid(column=2, row=4, ipadx=15, pady=(10, 10)))
price_3 = (tk.Button(window_frame, text='$0.25', command=quarter, justify='center').grid(column=3, row=4, ipadx=15, pady=(10, 10)))

# 4.2 Make the Order Button
order_button = (tk.Button(window_frame, text='Make Drink', command=make_drink, justify='center').grid(column=2, row=7, ipadx=15, pady=(10, 10)))

# 5. Make Entry box
bank = tk.StringVar()
bank.set('$0.00')
tk.Entry(window_frame, width=30, textvariable=bank, justify='center').grid(column=2, row=5, pady=(10, 10))

order_item = tk.StringVar()
tk.Entry(window_frame, width=30, textvariable=order_item, justify='center').grid(column=2, row=6, pady=(10, 10))

payment_done = tk.StringVar()
tk.Entry(window_frame, width=30, textvariable=payment_done, justify='center').grid(column=2, row=8, pady=(10, 10))

root.mainloop()

