from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from math import *

root = Tk()
root.title("cryptocurrency")
root.geometry("1000x650")
root.resizable(0,0)

#IMG = ImageTk.PhotoImage(Image.open("cryptocurrency.jpeg"))

CRYPTYPE = ["BTC", "BCH", "LIT", "ETH"]

CURRENCY_TYPE = ["DOLLARS", "INR", "EUROS"]

clicked = StringVar()
clicked.set(CRYPTYPE[0])
clicked1 = StringVar()
clicked1.set(CURRENCY_TYPE[0])

CURRENT_INR_BTC = 807283.25
CURRENT_DOLLAR_BTC = 10967.01
CURRENT_EURO_BTC = 9262.91

CURRENT_INR_BCH = 16930.33
CURRENT_DOLLAR_BCH = 230.38
CURRENT_EURO_BCH = 194.26

CURRENT_INR_LIT = 3562.73
CURRENT_DOLLAR_LIT = 48.40
CURRENT_EURO_LIT = 40.88

CURRENT_INR_ETH = 28116.13
CURRENT_DOLLAR_ETH = 381.96
CURRENT_EURO_ETH = 322.61

##MIN_INR_BTC=1613.18
##MIN_DOLLAR_BTC=21.93
##MIN_EURO_BTC=18.77

##MIN_INR_BCH=847.44
##MIN_DOLLAR_BCH=11.52
##MIN_EURO_BCH=9.86

##MIN_INR_ETH=2810.87
##MIN_DOLLAR_ETH=38.2
##MIN_EURO_ETH=32.71

##MIN_INR_LIT=712.08
##MIN_DOLLAR_LIT=9.68
##MIN_EURO_LIT=8.29

# mainwindow of the application
def frame1():
    global cryptype_menu
    global currencytype_menu
    global amount_entry
    global value_entry

    global amount
    amount = DoubleVar()

    global value
    value = DoubleVar()
    # frame
    frame1 = Frame(root).place(x=0, y=0, width=1000, height=650)
    # labels
    title_label = Label(frame1, text="CRYPTOCURRENCY", font=("TimesNewRoman 40")).place(x=200, y=5, width=600, height=52)
    #image_label = Label(frame1, image=IMG).place(x=0, y=91)
    cryptype_label = Label(frame1, text="CRYPTYPE", font=("TimesNewRoman 15 bold")).place(x=100, y=480, width=137, height=31)
    cryptype_label = Label(frame1,text="CURRENCY TYPE",font=("TimesNewRoman 15 bold")).place(x=319, y=480, width=223, height=31)
    cryptype_label = Label(frame1, text="AMOUNT", font=("TimesNewRoman 15 bold")).place(x=618, y=480, width=112, height=31)
    cryptype_label = Label(frame1, text="VALUE", font=("TimesNewRoman 15 bold")).place(x=813, y=480, width=87, height=31)

    # dropdown menu
    cryptype_menu = ttk.Combobox(frame1, values=CRYPTYPE)
    cryptype_menu.place(x=115, y=515, width=108)
    cryptype_menu.current(0)

    currencytype_menu = ttk.Combobox(frame1, values=CURRENCY_TYPE)
    currencytype_menu.place(x=345, y=515, width=172)
    currencytype_menu.current(0)
    # entry menu
    amount_entry = Entry(frame1, width=13, borderwidth=2, textvariable = amount).place(x=631, y=515)
    value_entry = Entry(frame1, width=13, borderwidth=2, textvariable = value).place(x=823, y=515)

    # Buttons
    signup_button = Button(frame1, text="SIGN UP", command=lambda: show_frame(frame2)).place(x=804, y=9, width=82, height=30)
    signin_button = Button(frame1, text="SIGN IN", command=lambda:show_frame(frame3)).place(x=895, y=9, width=82, height=30)
    value_button = Button(frame1, text="GET", command=calculation).place(x=823, y=535, width=83)

def min_value_error():
    error_window=Toplevel()
    error_window.geometry("500x400+385+200")
    error_window_label=Label(error_window, text="THE AMOUNT YOU HAVE ENTERED IS LOWER THAN THE MINIMUM ENTRY.").place(x=50, y=50)
    error_window_label2=Label(error_window, text="PLEASE CHECK THE MINIMUM VALUES GIVEN BELOW:").place(x=50, y=70)
    error_window_label3=Label(error_window, text='''MINIMUM BTC(INR)=1613.18
MINIMUM BTC(DOLLAR)=21.93
MINIMUM BTC(EURO)=18.77

MINIMUM BCH(INR)=847.44
MINIMUM BCH(DOLLAR)=11.52
MINIMUM BCH(EURO)=9.86

MINIMUM ETH(INR)=2810.87
MINIMUM ETH(DOLLAR)=38.2
MINIMUM ETH(EURO)=32.71

MINIMUM LIT(INR)=712.08
MINIMUM LIT(DOLLAR)=9.68
MINIMUM LIT(EURO)=8.29''', font="TimesNewRoman 9").place(x=155, y=100) 

def calculation():
    cryptype = cryptype_menu.get()
    currency_type = currencytype_menu.get()

    Amount = amount.get()
    Value=0
    
    if cryptype == "BTC":
        if currency_type == "INR":
            if Amount<MIN_INR_BTC:
                min_value_error()
            elif Amount>=MIN_INR_BTC:
                Value = Amount *float(CURRENT_INR_BTC)
        elif currency_type == "DOLLARS":
            if Amount<MIN_DOLLAR_BTC:
                min_value_error()
            elif Amount>=MIN_DOLLAR_BTC:
                Value = Amount * float(CURRENT_DOLLAR_BTC)
        elif currency_type == "EUROS":
            if Amount<MIN_EURO_BTC:
                min_value_error()
            elif Amount>=MIN_EURO_BTC:
                Value = Amount * float(CURRENT_EURO_BTC)

    elif cryptype == "BCH":
        if currency_type == "INR":
            if Amount<MIN_INR_BCH:
                min_value_error()
            elif Amount>=MIN_INR_BCH:
                Value = Amount *float(CURRENT_INR_BCH)
        elif currency_type == "DOLLARS":
            if Amount<MIN_DOLLAR_BCH:
                min_value_error()
            elif Amount>=MIN_DOLLAR_BCH:
                Value = Amount * float(CURRENT_DOLLAR_BCH)
        elif currency_type == "EUROS":
            if Amount<MIN_EURO_BCH:
                min_value_error()
            elif Amount>=MIN_EURO_BCH:
                Value = Amount * float(CURRENT_EURO_BCH)

    elif cryptype == "ETH":
        if currency_type == "INR":
            if Amount < MIN_INR_ETH:
                min_value_error()
            elif Amount >= MIN_INR_ETH:
                Value = Amount * float(CURRENT_INR_ETH)
        elif currency_type == "DOLLARS":
            if Amount < MIN_DOLLAR_ETH:
                min_value_error()
            elif Amount >= MIN_DOLLAR_ETH:
                Value = Amount * float(CURRENT_DOLLAR_ETH)
        elif currency_type == "EUROS":
            if Amount < MIN_EURO_ETH:
                min_value_error()
            elif Amount >= MIN_EURO_ETH:
                Value = Amount * float(CURRENT_EURO_ETH)

    elif cryptype == "LIT":
        if currency_type == "INR":
            if Amount < MIN_INR_LIT:
                min_value_error()
            elif Amount >= MIN_INR_LIT:
                Value = Amount * float(CURRENT_INR_LIT)
        elif currency_type == "DOLLARS":
            if Amount < MIN_DOLLAR_LIT:
                min_value_error()
            elif Amount >= MIN_DOLLAR_LIT:
                Value = Amount * float(CURRENT_DOLLAR_LIT)
        elif currency_type == "EUROS":
            if Amount < MIN_EURO_LIT:
                min_value_error()
            elif Amount >= MIN_EURO_LIT:
                Value = Amount * float(CURRENT_EURO_LIT)
    
    value.set(round(Value, 2))



def frame2():
    frame2 = Frame(root).place(x=0, y=0, width=1000, height=650)
    # labels
    username_label = Label(frame2, text="USERNAME", font=("TimesNewRoman 10 bold")).place(x=236, y=224, width=245, height=37)
    email_label = Label(frame2, text="EMAIL", font=("TimesNewRoman 10 bold")).place(x=220, y=267, width=245, height=37)
    password_label = Label(frame2, text="PASSWORD", font=("TimesNewRoman 10 bold")).place(x=238, y=310, width=245, height=37)
    confirm_password_label = Label(frame2, text="CONFIRM PASSWORD", font=("TimesNewRoman 10 bold")).place(x=269, y=353, width=245, height=37)

    # entrys

    username_entry = Entry(frame2).place(x=550, y=230, width=170, height=20)
    email_entry = Entry(frame2).place(x=550, y=270, width=170, height=20)
    password_entry = Entry(frame2).place(x=550, y=315, width=170, height=20)
    confirm_password_entry = Entry(frame2).place(x=550, y=361, width=170, height=20)

    # buttons

    create_account_button = Button(frame2, text="CREATE ACCOUNT", command=CA_popup).place(x=450, y=422, width=150, height=35)
    back_button = Button(frame2, text="<--", command=lambda: show_frame(frame1)).place(x=10, y=10, width=40, height=30)

def frame3():
    global frame3
    frame3 = Frame(root).place(x=0, y=0, width=1000, height=650)
    #labels

    username_label = Label(frame3, text="USERNAME", font=("TimesNewRoman 12 bold")).place(x=300, y=285, width=245, height=37)
    password_label = Label(frame3, text="PASSWORD", font=("TimesNewRoman 12 bold")).place(x=300, y=325, width=245, height=37)

    #entrys

    username_entry = Entry(frame3).place(x=499, y=293, width=170, height=20)
    password_entry = Entry(frame3).place(x=500, y=332, width=170, height=20)

    #buttons

    signin_button = Button(frame3, text="SIGN IN", command=lambda: show_frame(frame4)).place(x=540, y= 380, width=120, height=30)
    forget_password_button = Button(frame3, text="FORGOT PASSWORD").place(x=380, y= 382, width=140, height=28)

    back_button = Button(frame3, text="<--", command=lambda: show_frame(frame1)).place(x=10, y=10, width=40, height=30)

def CA_popup():
    global CA_popup
    CA_popup =Toplevel()
    CA_popup.geometry("350x200+450+250")
    CA_popup.title("Creation success!")

    CA_popup_label1 = Label(CA_popup, text="Your account has been successfully created!").place(x=60,y=60)
    CA_popup_label2 = Label(CA_popup, text="Please sign in again to continue.").place(x=90,y=80)

    CA_popup_button = Button(CA_popup, text="OK", command=signup_destroy).place(x= 130,y=130, height=25, width=100)

def signup_destroy():
    CA_popup.destroy()
    show_frame(frame1)

def show_frame(frame):
    return frame()

def data_table():


    My_tree = ttk.Treeview(frame4)

    My_tree['columns'] = ("BTC", "BCH", "LIT", "ETH")

    #formating the column
    My_tree.column("#0", width = 120)
    My_tree.column("BTC", width = 120)
    My_tree.column("BCH", width = 120)
    My_tree.column("LIT", width = 120)
    My_tree.column("ETH", width = 120)

    #HEADING
    My_tree.heading("#0", text="CURRENCY", anchor=W)
    My_tree.heading("BTC", text="BTC", anchor=W)
    My_tree.heading("BCH", text="BCH", anchor=W)
    My_tree.heading("LIT", text="LIT", anchor=W)
    My_tree.heading("ETH", text="ETH", anchor=W)

    #INSERTING DATA
    My_tree.insert(parent="", index='end', iid=0, text="", values=())
    My_tree.insert(parent="", index='end', iid=1, text="INR", values=(CURRENT_INR_BTC, CURRENT_INR_BCH, CURRENT_INR_LIT, CURRENT_INR_ETH))
    My_tree.insert(parent="", index='end', iid=2, text="", values=())
    My_tree.insert(parent="", index='end', iid=3, text="EUROS", values=(CURRENT_EURO_BTC, CURRENT_EURO_BCH, CURRENT_EURO_LIT, CURRENT_EURO_ETH))
    My_tree.insert(parent="", index='end', iid=4, text="", values=())
    My_tree.insert(parent="", index='end', iid=5, text="DOLLARS", values=(CURRENT_DOLLAR_BTC, CURRENT_DOLLAR_BCH, CURRENT_DOLLAR_LIT, CURRENT_DOLLAR_ETH))
    My_tree.insert(parent="", index='end', iid=6, text="", values=())


    My_tree.place(x= 190, y= 400)

def frame4():
    global btc_value
    global bch_value
    global lit_value
    global eth_value

    btc_value=0.00
    bch_value=0.00
    lit_value=0.00
    eth_value=0.00

    global frame4
    frame4 = Frame(root).place(x=0, y=0, width=1000, height=650)

    username_label= Label(frame4, text="PROJECT", font=("TimesNewRoman 30 bold")).place(x=15, y=15, height=40, width=200)
    btc_label =Label(frame4, text="BTC", font=("TimesNewRoman 15 bold")).place(x=20, y=120, height=40, width=50)
    bch_label =Label(frame4, text="BCH", font=("TimesNewRoman 15 bold")).place(x=140, y=120, height=40, width=50)
    lit_label =Label(frame4, text="LIT", font=("TimesNewRoman 15 bold")).place(x=260, y=120, height=40, width=50)
    eth_label =Label(frame4, text="ETH", font=("TimesNewRoman 15 bold")).place(x=380, y=120, height=40, width=50)

    btc_value_label=Label(frame4, text=btc_value, font=("TimesNewRoman 15 bold")).place(x=20, y=160, height=40, width=50)
    bch_value_label=Label(frame4, text=bch_value, font=("TimesNewRoman 15 bold")).place(x=140, y=160, height=40, width=50)
    lit_value_label=Label(frame4, text=lit_value, font=("TimesNewRoman 15 bold")).place(x=260, y=160, height=40, width=50)
    eth_value_label=Label(frame4, text=eth_value, font=("TimesNewRoman 15 bold")).place(x=380, y=160, height=40, width=50)

    send_button = Button(frame4, text="SEND").place(x=20, y=250, width=100, height=35)
    recieve_button = Button(frame4, text="RECIEVE").place(x=150, y=250, width=100, height=35)

    data_table()
    

frame1()

root.mainloop()

