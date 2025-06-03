import tkinter as tk
from tkinter import messagebox
import random

flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Choco", "Cookie & Cream", "Matcha"]
toppings = ["Rainbow Sprinkles", "Classic Sprinkles", "Oreo Crumbs", "Marshmallow", "Wafer Stick"]
base_price, topping_price = 9000, 3000

orders = []  # To store multiple orders
user_name = None  # To store single user name for all orders

#fungsi panggilan
def roll_dice():
    return random.randint(1, 6)
def calculate_current_order():
    try:
        dice_roll = roll_dice()
        discount = dice_roll * 500
        
        selected_flavors = [flavor for flavor, var in flavor_vars.items() if var.get()]
        scoops = int(entry_scoops.get())
        selected_toppings = [topping for topping, var in topping_vars.items() if var.get()]
        
        if scoops < len(selected_flavors):
            messagebox.showwarning("Invalid Move!", f"You need {len(selected_flavors)} scoops for {len(selected_flavors)} flavors!")
            return None
            
        subtotal = (base_price * scoops) + (topping_price * len(selected_toppings))
        total = subtotal - discount

        return {
            'flavors': selected_flavors,
            'scoops': scoops,
            'toppings': selected_toppings,
            'discount': discount,
            'subtotal': subtotal,
            'total': total,
            'dice_roll': dice_roll
        }
    except ValueError:
        messagebox.showerror("Game Rule Violation!", "Please enter valid numbers!")
        return None
def add_order_to_cart():
    global user_name
    # Validate and store user name once
    name = cust_name.get().strip()
    if not name:
        messagebox.showwarning("Input Needed", "Please enter your name before ordering.")
        return
    if user_name is None:
        user_name = name
        cust_name_entry.config(state='disabled')  # Disable further editing
    elif name != user_name:
        messagebox.showwarning("Name Mismatch", f"You already ordered as {user_name}. Please continue ordering under this name.")
        cust_name.set(user_name)
        return

    order = calculate_current_order()
    if order is not None:
        orders.append(order)
        messagebox.showinfo("Added", f"Order added to cart for {user_name}!\nYou can order more or see your invoice.")
        reset_inputs()
def reset_inputs():
    # Reset all selections for next order except the name
    for var in flavor_vars.values():
        var.set(0)
    for var in topping_vars.values():
        var.set(0)
    entry_scoops.delete(0, tk.END)
    entry_scoops.insert(0, "1")
def show_invoice():
    if user_name is None:
        messagebox.showinfo("No Orders", "Please enter your name and add at least one order before viewing invoice!")
        return
    if not orders:
        messagebox.showinfo("No Orders", "No orders in cart. Please add at least one order!")
        return
    display_orders_summary()
    main_frame.pack_forget()
    invoice_frame.pack(fill='both', expand=True)
def back_to_order():
    invoice_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)
def welcome():
    welcome_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)
def exit_app():
    window.destroy()
def display_orders_summary():
    label_result.config(text="")  # Clear previous
    total_all = 0
    lines = []
    lines.append(f"🍦 INVOICE FOR {user_name.upper()} 🍦")
    lines.append("="*40)
    for idx, order in enumerate(orders, 1):
        lines.append(f"Order {idx}:")
        lines.append("─────────────────────────────")
        lines.append(f"  Flavors   : {', '.join(order['flavors']) if order['flavors'] else 'None'}")
        lines.append(f"  Scoops    : {order['scoops']} x Rp 9,000")
        lines.append(f"  Toppings  : {', '.join(order['toppings']) if order['toppings'] else 'None'}")
        lines.append(f"  Subtotal  : Rp {order['subtotal']:,}")
        lines.append(f"  Discount  : -Rp {order['discount']:,} (dice roll {order['dice_roll']})")
        lines.append(f"  Total     : Rp {order['total']:,}")
        lines.append("-"*29)
        total_all += order['total']
    lines.append(f"GRAND TOTAL PRICE FOR {len(orders)} ORDER{'S' if len(orders)>1 else ''}: Rp {total_all:,}")
    lines.append("="*40)
    label_result.config(text="\n".join(lines))

window = tk.Tk()
window.title("Ice Cream Corner")
window.geometry("450x600")
window.configure(bg='#ffebcd')

cust_name = tk.StringVar()
#frame aplikasi 
welcome_frame = tk.Frame(window, bg='#ffebcd')
main_frame = tk.Frame(window, bg='#ffebcd')
#label aplikasi 
welcome_label= tk.Label(welcome_frame, text="🍦 WELCOME SCOOPTERS 🍦", font=('Comic Sans MS', 20, 'bold'), bg='#ffebcd', fg='#8b0000').grid(row=0, column=0, columnspan=3, pady=5)
main_label = tk.Label(main_frame, text="🍦 CONFECTION ICE CREAM 🍦", font=('Comic Sans MS', 16, 'bold'), bg='#ffebcd', fg='#8b0000').grid(row=0, column=0, columnspan=2, pady=10)
cust_input = tk.Label(main_frame, text="Your Name:", font=('Arial', 12), bg='#ffebcd', fg='#8b0000').grid(row=1, column=0, sticky='e')
#button aplikasi
welcome_button = tk.Button(welcome_frame, text="MENU", font=('Comic Sans MS', 12, 'bold'), fg='#ffebcd', bg='#8b0000', command=welcome)

#entry aplikasi
cust_name_entry = tk.Entry(main_frame, textvariable=cust_name, font=('Arial', 12), bg='white', fg='black')

#edit pack, grid aplikasi
welcome_frame.pack(fill='both', expand=True)
welcome_button.grid(row=1, column=1)
cust_name_entry.grid(row=1, column=1, sticky='w')

#label frame rasa
flavor_frame = tk.LabelFrame(main_frame, text=" FLAVORS ", font=('Arial', 12), bg='#fffacd', fg='#8b0000')
#label frame grid, pack
flavor_frame.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')

#frame looping flavor and toppings
flavor_vars = {}
for flavor in flavors:
    var = tk.IntVar()
    flavor_vars[flavor] = var
    tk.Checkbutton(flavor_frame, text=flavor, variable=var, font=('Arial', 11), bg='#fffacd', fg='#8b0000', selectcolor='#ffe4e1').pack(anchor='w')

topping_frame = tk.LabelFrame(main_frame, text="TOPPINGS", font=('Arial', 12), bg='#fffacd', fg='#8b0000')
topping_frame.grid(row=2, column=1, padx=10, pady=5, sticky='nsew')

topping_vars = {}
for topping in toppings:
    var = tk.IntVar()
    topping_vars[topping] = var
    tk.Checkbutton(topping_frame, text=topping, variable=var, 
                  font=('Arial', 11), bg='#fffacd', fg='#8b0000', selectcolor='#ffe4e1').pack(anchor='w')
    

#label scoops entry
tk.Label(main_frame, text="Your Scoop Stack:", font=('Arial', 12), bg='#ffebcd', fg='#8b0000').grid(row=3, column=0, sticky='e')
entry_scoops = tk.Entry(main_frame, font=('Arial', 12), bg='white', fg='black')
entry_scoops.grid(row=3, column=1, sticky='w')
entry_scoops.insert(0, "1")

button_frame = tk.Frame(main_frame, bg='white')
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Add to Cart", command=add_order_to_cart, 
          font=('Arial', 12, 'bold'), bg="#4CAF50", fg='white').pack(side='left', padx=5)
tk.Button(button_frame, text="See Invoice", command=show_invoice, 
          font=('Arial', 12, 'bold'), bg="#EC8E87", fg='white').pack(side='left', padx=5)
tk.Button(button_frame, text="Exit", command=exit_app, 
          font=('Arial', 12, 'bold'), bg="#f59d9d", fg='white').pack(side='left', padx=5)

invoice_frame = tk.Frame(window, bg='#ffebcd')

result_frame = tk.LabelFrame(invoice_frame, text="INVOICE SUMMARY", font=('Arial', 12), bg="#d46161")
result_frame.pack(padx=10, pady=10, fill='both', expand=True)

label_result = tk.Label(result_frame, text="Your orders will appear here!", 
                       font=('Arial', 11), bg='#ffe4b5', fg='#8b0000', justify='left', anchor='nw')
label_result.pack(fill='both', expand=True)

nav_button_frame = tk.Frame(invoice_frame, bg='#ffebcd')
nav_button_frame.pack(pady=10)

tk.Button(nav_button_frame, text="Order More", command=back_to_order, 
          font=('Arial', 12, 'bold'), bg="#4a90e2", fg='white').pack(side='left', padx=5)
tk.Button(nav_button_frame, text="Quit", command=exit_app, 
          font=('Arial', 12, 'bold'), bg="#d46161", fg='white').pack(side='left', padx=5)

window.mainloop()