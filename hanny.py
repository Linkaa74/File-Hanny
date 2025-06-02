import tkinter as tk
from tkinter import messagebox
import random

flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Choco", "Cookie & Cream", "Matcha"]
toppings = ["Rainbow Sprinkles", "Classic Sprinkles", "Oreo Crumbs", "Marshmallow", "Wafer Stick"]
base_price, topping_price = 9000, 3000

def roll_dice():
    return random.randint(1, 6)

def calculate_total():
    try:
        dice_roll = roll_dice()
        discount = dice_roll * 500
        
        selected_flavors = [flavor for flavor, var in flavor_vars.items() if var.get()]
        scoops = int(entry_scoops.get())
        selected_toppings = [topping for topping, var in topping_vars.items() if var.get()]
        
        if scoops < len(selected_flavors):
            messagebox.showwarning("Invalid Move!", f"You need {len(selected_flavors)} scoops for {len(selected_flavors)} flavors!")
            return
            
        subtotal = (base_price * scoops) + (topping_price * len(selected_toppings))
        total = subtotal - discount
        
        result_text = f"""
        {cust_name.get()}'s Ice Cream Adventure:
        ┌────────────────────┐
          Flavors:    {len(selected_flavors):>2} x Rp 9,000  
          Scoops:     {scoops:>2} x Rp 9,000  
          Toppings:   {len(selected_toppings):>2} x Rp 3,000  
        ├────────────────────┤
          Subtotal:   Rp {subtotal:>7,}  
          Discount: -Rp {discount:>7,}  
        ├────────────────────┤
         TOTAL PRICE: Rp {total:>7,}  
        └────────────────────┘"""
        label_result.config(text=result_text)
        
    except ValueError:
        messagebox.showerror("Game Rule Violation!", "Please enter valid numbers!")

window = tk.Tk()
window.title("Ice Cream Corner")
window.geometry("500x800")
window.configure(bg='#ffebcd')

tk.Label(window, text=" CONEFECTION Ice Cream ", font=('Comic Sans MS', 16, 'bold'), bg='#ffebcd', fg='#8b0000').grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(window, text="hi i'm:", font=('Arial', 12), bg='#ffebcd', fg='#8b0000').grid(row=1, column=0, sticky='e')
cust_name = tk.StringVar(value="Your Name")
tk.Entry(window, textvariable=cust_name, font=('Arial', 12), bg='white', fg='black').grid(row=1, column=1, sticky='w')

flavor_frame = tk.LabelFrame(window, text=" FLAVORS ", font=('Arial', 12), bg='#fffacd', fg='#8b0000')
flavor_frame.grid(row=2, column=0, padx=10, pady=5, sticky='nsew')

flavor_vars = {}
for i, flavor in enumerate(flavors):
    var = tk.IntVar()
    flavor_vars[flavor] = var
    tk.Checkbutton(flavor_frame, text=flavor, variable=var, font=('Arial', 11), bg='#fffacd', fg='#8b0000', selectcolor='#ffe4e1').pack(anchor='w')

topping_frame = tk.LabelFrame(window, text="TOPPINGS", font=('Arial', 12), bg='#fffacd', fg='#8b0000')
topping_frame.grid(row=2, column=1, padx=10, pady=5, sticky='nsew')

topping_vars = {}
for i, topping in enumerate(toppings):
    var = tk.IntVar()
    topping_vars[topping] = var
    tk.Checkbutton(topping_frame, text=topping, variable=var, 
                  font=('Arial', 11), bg='#fffacd', fg="#5e0000", selectcolor='#ffe4e1').pack(anchor='w')

tk.Label(window, text="Your Scoop Stack:", font=('Arial', 12), bg='#ffebcd', fg="#5f0000").grid(row=3, column=0, sticky='e')
entry_scoops = tk.Entry(window, font=('Arial', 12), bg='white', fg='black')
entry_scoops.grid(row=3, column=1, sticky='w')
entry_scoops.insert(0, "1")

button_frame = tk.Frame(window, bg='white')
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="See My Conefection", command=calculate_total, 
          font=('Arial', 12, 'bold'), bg="#EC8E87", fg='white').pack(side='left', padx=5)

tk.Button(button_frame, text="Exit", command=window.destroy, 
          font=('Arial', 12, 'bold'), bg="#f59d9d", fg='white').pack(side='left', padx=5)

result_frame = tk.LabelFrame(window, text="ORDER SUMMARY", font=('Arial', 12), bg="#d46161")
result_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(result_frame, text="Choose your chill and let the dice do the magic!", 
                       font=('Arial', 11), bg='#ffe4b5', fg='#8b0000', justify='left', width=50, height=12)
label_result.pack()

tk.Label(window, text="How to play: Scoop your flavors, stack your toppings, roll for a sweet surprise!", 
         font=('Arial', 10), bg='#ffe4b5', fg='#8b0000').grid(row=6, column=0, columnspan=2)


window.mainloop()