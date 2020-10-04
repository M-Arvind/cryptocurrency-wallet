from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from math import *
from tkinter import messagebox
import mysql.connector as mc
from tkinter import font


root = Tk()
root.title("cryptocurrency")
root.geometry("1000x650+250+120")

IMG = ImageTk.PhotoImage(Image.open("Cryptocurrency_logos.jpg"))
FRAME_IMG = ImageTk.PhotoImage(Image.open("frame_img2.jpg"))


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

MIN_BTC_ENTRY=0.002
MIN_BCH_ENTRY=0.05
MIN_LIT_ENTRY=0.2
MIN_ETH_ENTRY=0.1

btc_value=0.00
bch_value=0.00
lit_value=0.00
eth_value=0.00

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
    # sign_up_img = ImageTk.PhotoImage(Image.open("signup png.png"))
    global cryptype_menu
    global currencytype_menu
    global amount_entry
    global value_entry

    global coins
    coins = DoubleVar()

    global value
    value = DoubleVar()
    # frame
    frame1 = Frame(root, bg="#FFFFFF").place(x=0, y=0, width=1000, height=650)
    # labels
    title_label = Label(frame1, text="CRYPTOCURRENCY", font=("TimesNewRoman 40"), bg="#FFFFFF").place(x=200, y=5, width=600, height=52)
    image_label = Label(frame1, image=IMG, bg="#FFFFFF").place(x=0, y=91)
    cryptype_label = Label(frame1, text="CRYPTYPE", font=("TimesNewRoman 15 bold"), bg="#FFFFFF").place(x=100, y=480, width=137, height=31)
    currency_type_label = Label(frame1,text="CURRENCY TYPE",font=("TimesNewRoman 15 bold"), bg="#FFFFFF").place(x=319, y=480, width=223, height=31)
    coins_label = Label(frame1, text="COINS", font=("TimesNewRoman 15 bold"), bg="#FFFFFF").place(x=612, y=480, width=112, height=31)
    amount_label = Label(frame1, text="AMOUNT", font=("TimesNewRoman 15 bold"), bg="#FFFFFF").place(x=823, y=480, width=87, height=31)
    # dropdown menu
    cryptype_menu = ttk.Combobox(frame1, values=CRYPTYPE)
    cryptype_menu.place(x=115, y=515, width=108)
    cryptype_menu.current(0)

    currencytype_menu = ttk.Combobox(frame1, values=CURRENCY_TYPE)
    currencytype_menu.place(x=345, y=515, width=172)
    currencytype_menu.current(0)
    # entry menu
    coins_entry = Entry(frame1, width=13, borderwidth=2, textvariable = coins).place(x=631, y=515)
    value_entry = Entry(frame1, width=13, borderwidth=2, textvariable = value).place(x=823, y=515)

    # Buttons

    signup_button = Button(frame1, text="SIGN UP", command=lambda: show_frame(frame2)).place(x=804, y=9, width=82, height=30)
    signin_button = Button(frame1, text="SIGN IN", command=lambda:show_frame(Frame3)).place(x=884, y=9, width=82, height=30)
    value_button = Button(frame1, text="GET", command=calculation).place(x=823, y=535, width=83)


def min_value_error():
    error_window=Toplevel()
    error_window.geometry("500x250+385+200")
    error_window_label=Label(error_window, text="THE AMOUNT YOU HAVE ENTERED IS LOWER THAN THE MINIMUM ENTRY.").place(x=50, y=50)
    error_window_label2=Label(error_window, text="PLEASE CHECK THE MINIMUM VALUES GIVEN BELOW:").place(x=50, y=70)
    error_window_label3=Label(error_window, text='''MINIMUM BTC- 0.002
MINIMUM BCH- 0.05
MINIMUM LIT- 0.2
MINIMUM ETH- 0.1''', font="TimesNewRoman 11").place(x=175, y=100)

def logout():
    message = messagebox.askyesno("logout", "Are you sure?")
    if message == True:
        show_frame(frame1)

def calculation():
    cryptype = cryptype_menu.get()
    currency_type = currencytype_menu.get()

    Amount = coins.get()
    Value=0

    if cryptype == "BTC":
        if Amount<MIN_BTC_ENTRY:
            min_value_error()
        elif Amount>=MIN_BTC_ENTRY:
            if currency_type == "INR":
                Value = Amount *float(CURRENT_INR_BTC)
            elif currency_type == "DOLLARS":
                Value = Amount * float(CURRENT_DOLLAR_BTC)
            elif currency_type == "EUROS":
                Value = Amount * float(CURRENT_EURO_BTC)

    elif cryptype == "BCH":
        if Amount<MIN_BCH_ENTRY:
            min_value_error()
        elif Amount>=MIN_BCH_ENTRY:
            if currency_type == "INR":
                Value = Amount *float(CURRENT_INR_BCH)
            elif currency_type == "DOLLARS":
                Value = Amount * float(CURRENT_DOLLAR_BCH)
            elif currency_type == "EUROS":
                Value = Amount * float(CURRENT_EURO_BCH)

    elif cryptype == "ETH":
        if Amount<MIN_ETH_ENTRY:
            min_value_error()
        elif Amount>=MIN_ETH_ENTRY:
            if currency_type == "INR":
                Value = Amount *float(CURRENT_INR_ETH)
            elif currency_type == "DOLLARS":
                Value = Amount * float(CURRENT_DOLLAR_ETH)
            elif currency_type == "EUROS":
                Value = Amount * float(CURRENT_EURO_ETH)

    elif cryptype == "LIT":
        if Amount<MIN_LIT_ENTRY:
            min_value_error()
        elif Amount>=MIN_LIT_ENTRY:
            if currency_type == "INR":
                Value = Amount *float(CURRENT_INR_LIT)
            elif currency_type == "DOLLARS":
                Value = Amount * float(CURRENT_DOLLAR_LIT)
            elif currency_type == "EUROS":
                Value = Amount * float(CURRENT_EURO_LIT)

    value.set(round(Value, 2))

def signup_destroy():
    #CA_popup.()
    show_frame(frame1)
    CA_popup.destroy()

# def CA_popup():
#     global CA_popup
#     CA_popup =Toplevel()
#     CA_popup.geometry("350x200+450+250")
#     CA_popup.title("Creation success!")

#     CA_popup_label1 = Label(CA_popup, text="Your account has been successfully created!").place(x=60,y=60)
#     CA_popup_label2 = Label(CA_popup, text="Please sign in again to continue.").place(x=90,y=80)

#     CA_popup_button = Button(CA_popup, text="OK", command=signup_destroy).place(x= 130,y=130, height=25, width=100)



def create_wallet():
    username = name.get()
    password = passwd.get()
    email = mail.get()
    c_password = cpasswd.get()
    db = mc.connect(
            host="localhost",
            user="root",
            passwd="arvind",
            database="crypto_wallet"
            )
    cursor = db.cursor()

    query = """SELECT * FROM crypto WHERE username = %s"""

    cursor.execute(query, (username, ))

    record = cursor.fetchall()

    if record == []:


        if len(password) < 8 or password.isalpha() or password.isdigit():
            messagebox.showerror("ERROR", "Min. length should be 8 characters and must be alphanumeric.")
        else:
            if password != c_password:
                messagebox.showerror("ERROR", "passwords do not match")
            else:
                # random_string = username + password + email

                public_key  = None
                private_key = None

                query = """INSERT INTO crypto (username , password, Email, Publickey, privatekey, BTC, BCH, LIT, ETH) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                values_tuple = (username , password, email, public_key, private_key, 0.0, 0.0, 0.0, 0.0)

                cursor.execute(query, values_tuple)

                db.commit()

                messagebox.showinfo("success", "account created successfully....")
                show_frame(frame1)

    else:
        messagebox.showerror("ERROR", "Username already exists!")



def frame2():
    global name
    global mail
    global passwd
    global cpasswd
    global username_entry
    name = StringVar()
    mail = StringVar()
    passwd = StringVar()
    cpasswd = StringVar()
    frame2 = Frame(root, bg="#FFFFFF").place(x=0, y=0, width=1000, height=650)
    # labels
    bg_label = Label(frame2, image=FRAME_IMG).place(x=0, y=0)
    username_label = Label(frame2, text="USERNAME", font=("TimesNewRoman 10 bold"), bg="#FFFFFF").place(x=236, y=224, width=245, height=37)
    email_label = Label(frame2, text="EMAIL", font=("TimesNewRoman 10 bold"), bg="#FFFFFF").place(x=220, y=267, width=245, height=37)
    password_label = Label(frame2, text="PASSWORD", font=("TimesNewRoman 10 bold"), bg="#FFFFFF").place(x=238, y=310, width=245, height=37)
    confirm_password_label = Label(frame2, text="CONFIRM PASSWORD", font=("TimesNewRoman 10 bold"), bg="#FFFFFF").place(x=269, y=353, width=245, height=37)
    # entrys

    username_entry = Entry(frame2, textvariable=name, bg="#FFFFFF").place(x=550, y=230, width=170, height=20)
    email_entry = Entry(frame2, textvariable=mail, bg="#FFFFFF").place(x=550, y=270, width=170, height=20)
    password_entry = Entry(frame2, textvariable=passwd, bg="#FFFFFF").place(x=550, y=315, width=170, height=20)
    confirm_password_entry = Entry(frame2, textvariable=cpasswd, bg="#FFFFFF").place(x=550, y=361, width=170, height=20)

    # buttons

    create_account_button = Button(frame2, text="CREATE ACCOUNT", command=create_wallet).place(x=450, y=422, width=150, height=35)
    back_button = Button(frame2, text="<--", command=lambda: show_frame(frame1)).place(x=10, y=10, width=40, height=30)

def signing_in():
    global table_username
    username = name2.get()
    password = passwd2.get()
    db = mc.connect(
        host="localhost",
        user="root",
        passwd="arvind",
        database="crypto_wallet"
        )

    cursor = db.cursor()

    query = """SELECT * FROM crypto WHERE username = %s"""
    cursor.execute(query, (username, ))

    record = cursor.fetchall()

    if record == []:
        messagebox.showerror("ERROR", "Username not found!")
    else:
        table_username = record[0][0]
        if record[0][1] == password:
            show_frame(Frame4)
        else:
            messagebox.showerror("ERROR", "Incorrect password.")





def Frame3():
    global name2
    global passwd2
    global frame3

    name2 = StringVar()
    passwd2 = StringVar()

    frame3 = Frame(root, bg="#FFFFFF").place(x=0, y=0, width=1000, height=650)
    #labels

    bg_label = Label(frame3, image=FRAME_IMG).place(x=0, y=0)
    username_label = Label(frame3, text="USERNAME", font=("TimesNewRoman 12 bold"), bg="#FFFFFF").place(x=300, y=285, width=245, height=37)
    password_label = Label(frame3, text="PASSWORD", font=("TimesNewRoman 12 bold"), bg="#FFFFFF").place(x=300, y=325, width=245, height=37)

    #entrys

    username_entry = Entry(frame3, bg="#FFFFFF", textvariable=name2).place(x=499, y=293, width=170, height=20)
    password_entry = Entry(frame3, bg="#FFFFFF", textvariable=passwd2).place(x=500, y=332, width=170, height=20)

    #buttons

    signin_button = Button(frame3, text="SIGN IN", command=signing_in).place(x=540, y= 380, width=120, height=30)
    forget_password_button = Button(frame3, text="FORGOT PASSWORD").place(x=380, y= 382, width=140, height=28)

    back_button = Button(frame3, text="<--", command=lambda: show_frame(frame1)).place(x=10, y=10, width=40, height=30)


def show_frame(frame):
    return frame()

def data_table():


    style= ttk.Style()
    style.theme_use("alt")
    style.configure("Treeview", rowheight=29, fieldbackground="white")
    style.configure("Treeview", font=("ComicSansMS",9,"bold"))
    style.configure("Treeview.Heading", font =("ComicSansMS",10,"bold"))

    style.map("Treeview", background=[("selected", 'lightblue')])




    My_tree = ttk.Treeview(frame4)
    My_tree2 = ttk.Treeview(frame4)

    My_tree['columns'] = ("BTC", "BCH", "LIT", "ETH")
    My_tree2['columns'] = ("From", "To", "Amount")


    #formating the column
    My_tree.column("#0", width = 92)
    My_tree.column("BTC", width = 92)
    My_tree.column("BCH", width = 92)
    My_tree.column("LIT", width = 92)
    My_tree.column("ETH", width = 92)

    My_tree2.column("#0", width = 115)
    My_tree2.column("From", width = 115)
    My_tree2.column("To", width = 115)
    My_tree2.column("Amount", width = 116)

    #HEADING
    My_tree.heading("#0", text="CURRENCY", anchor=W)
    My_tree.heading("BTC", text="BTC", anchor=W)
    My_tree.heading("BCH", text="BCH", anchor=W)
    My_tree.heading("LIT", text="LIT", anchor=W)
    My_tree.heading("ETH", text="ETH", anchor=W)

    My_tree2.heading("#0", text="ID", anchor=W)
    My_tree2.heading("From", text="From", anchor=W)
    My_tree2.heading("To", text="To", anchor=W)
    My_tree2.heading("Amount", text="Amount", anchor=W)

    #INSERTING DATA
    My_tree.insert(parent="", index='end', iid=0, text="", values=(), tags=("odd",))
    My_tree.insert(parent="", index='end', iid=1, text="INR", values=(CURRENT_INR_BTC, CURRENT_INR_BCH, CURRENT_INR_LIT, CURRENT_INR_ETH), tags=("even",))
    My_tree.insert(parent="", index='end', iid=2, text="", values=(), tags=("odd",))
    My_tree.insert(parent="", index='end', iid=3, text="EUROS", values=(CURRENT_EURO_BTC, CURRENT_EURO_BCH, CURRENT_EURO_LIT, CURRENT_EURO_ETH), tags=("even",))
    My_tree.insert(parent="", index='end', iid=4, text="", values=(), tags=("odd",))
    My_tree.insert(parent="", index='end', iid=5, text="DOLLARS", values=(CURRENT_DOLLAR_BTC, CURRENT_DOLLAR_BCH, CURRENT_DOLLAR_LIT, CURRENT_DOLLAR_ETH), tags=("even",))

    My_tree.tag_configure('odd', background="white")
    My_tree.tag_configure('even', background="#8FA2A3")

    My_tree.place(x= 6, y= 435)
    My_tree2.place(x= 5, y=115)

def send():
    value = option.get()
    reciever_address = to.get()
    amount = coins_amount.get()
    sender = name2.get()

    db = mc.connect(
        host="localhost",
        user="root",
        passwd="arvind",
        database="crypto_wallet"
        )

    cursor = db.cursor()

    query = """SELECT * FROM crypto WHERE address = %s"""
    cursor.execute(query, (reciever_address, ))

    record = cursor.fetchall()

def Frame4():

    global frame4
    global to
    global coins_amount
    global option
    frame4 = Frame(root, bg="#FFFFFF").place(x=0, y=0, width=1000, height=650)

    to = StringVar()
    coins_amount = StringVar()
    option = StringVar()

    btc_balance = btc_value * CURRENT_INR_BTC
    bch_balance = bch_value * CURRENT_INR_BCH
    lit_balance = lit_value * CURRENT_INR_LIT
    eth_balance = eth_value * CURRENT_INR_ETH

    btc_image = ImageTk.PhotoImage(Image.open("btc_icon.png"))
    bch_image = ImageTk.PhotoImage(Image.open("bch_icon.png"))
    lit_image = ImageTk.PhotoImage(Image.open("lit_icon.png"))
    eth_image = ImageTk.PhotoImage(Image.open("eth_icon.png"))


    my_font = font.Font(family="Comic Sans MS", size=30)
    my_font2 = font.Font(family="Comic Sans MS", size=20)
    my_font3 = font.Font(family="Comic Sans MS", size=10)

    coins_frame = LabelFrame(frame4, text= "Mycoins",bg="#FFFFFF", font=("ComicSansMS 15"), labelanchor="n").place(x=480, y=80, width=500, height= 350)
    mytree_frame = LabelFrame(frame4, text="My Transfer", bg="#FFFFFF", font=("ComicSansMS 15"), labelanchor="n").place(x=5, y=80, width=465, height= 349)
    transfer_frame = LabelFrame(frame4, text="Transaction", bg="#FFFFFF", font=("ComicSansMS 15"), labelanchor="n").place(x=480, y=440, width=500, height= 160)

    header_label = Label(frame4, bg="#8FA2A3").place(x=0, y=0, width= 1000, height = 70)

    username_label= Label(frame4, text=table_username, font=my_font, bg="#8FA2A3", fg="white").place(x=800, y=15, height=40, width=200)
    To_label = Label(frame4, text = "TO", font=("ComicSansMS 12 bold"), bg="#FFFFFF").place(x=490, y=470, width= 30, height= 30)
    amount = Label(frame4, text = "AMOUNT", font=("ComicSansMS 12 bold"), bg="#FFFFFF").place(x=495, y=520, width= 70, height= 30)
    btc_label =Label(frame4, text="BTC", font=my_font3, bg="#FFFFFF").place(x=585, y=138, height=40, width=50)
    bch_label =Label(frame4, text="BCH", font=my_font3, bg="#FFFFFF").place(x=585, y=220, height=40, width=50)
    lit_label =Label(frame4, text="LIT", font=my_font3, bg="#FFFFFF").place(x=585, y=300, height=40, width=50)
    eth_label =Label(frame4, text="ETH", font=my_font3, bg="#FFFFFF").place(x=586, y=380, height=40, width=50)

    btc_value_label=Label(frame4, text=btc_value, font=my_font3, bg="#FFFFFF").place(x=553, y=138, height=40, width=40)
    lit_value_label=Label(frame4, text=lit_value, font=my_font3, bg="#FFFFFF").place(x=548, y=300, height=40, width=50)
    eth_value_label=Label(frame4, text=eth_value, font=my_font3, bg="#FFFFFF").place(x=548, y=380, height=40, width=50)
    bch_value_label=Label(frame4, text=bch_value, font=my_font3, bg="#FFFFFF").place(x=548, y=220, height=40, width=50)

    btc_label2 =Label(frame4, text="My BTC wallet", font=my_font2, bg="#FFFFFF").place(x=550, y=105, height=40, width=200)
    bch_label2 =Label(frame4, text="My BCH wallet", font=my_font2, bg="#FFFFFF").place(x=550, y=180, height=50, width=200)
    lit_label2 =Label(frame4, text="My LIT wallet", font=my_font2, bg="#FFFFFF").place(x=547, y=260, height=50, width=200)
    eth_label2 =Label(frame4, text="My ETH wallet", font=my_font2, bg="#FFFFFF").place(x=550, y=340, height=50, width=200)

    btc_amount_label = Label(frame4, text="Rs " + str(btc_balance), bg="#FFFFFF", font=my_font2).place(x=800, y=105, width=160, height=40)
    bch_amount_label = Label(frame4, text="Rs " + str(bch_balance), bg="#FFFFFF", font=my_font2).place(x=800, y=185, width=160, height=40)
    lit_amount_label = Label(frame4, text="Rs " + str(lit_balance), bg="#FFFFFF", font=my_font2).place(x=800, y=265, width=160, height=40)
    eth_amount_label = Label(frame4, text="Rs " + str(eth_balance), bg="#FFFFFF", font=my_font2).place(x=800, y=345, width=160, height=40)

    btc_image_label = Label(frame4, image=btc_image)
    btc_image_label.image = btc_image
    btc_image_label.place(x=500, y=110)
    bch_image_label = Label(frame4, image = bch_image)
    bch_image_label.image = bch_image
    bch_image_label.place(x=500, y=190)
    lit_image_label = Label(frame4, image = lit_image)
    lit_image_label.image = lit_image
    lit_image_label.place(x=500, y=270)
    eth_image_label = Label(frame4, image = eth_image)
    eth_image_label.image = eth_image
    eth_image_label.place(x=500, y=350)

    to_entry = Entry(frame4, textvariable=to, bg= "#FFFFFF").place(x=600, y=470, width=350, height=25)
    amount_entry = Entry(frame4, textvariable=coins_amount, bg= "#FFFFFF").place(x=600, y=520, width=350, height=25)

    send_button = Button(frame4, text="SEND", command=send).place(x=770, y=610, width=100, height=30)
    # recieve_button = Button(frame4, text="RECIEVE").place(x=585, y=440, width=100, height=30)
    logout_button = Button(frame4, text= "LOG OUT", command= logout).place(x=887, y=610, width=90, height=30)

    btc_radio_button = Radiobutton(frame4, text="BTC", font=my_font3, variable=option, value= "BTC", bg="#FFFFFF").place(x=490, y=560)
    btc_radio_button = Radiobutton(frame4, text="BCH", font=my_font3, variable=option, value= "BCH", bg="#FFFFFF").place(x=550, y=560)
    btc_radio_button = Radiobutton(frame4, text="LIT", font=my_font3, variable=option, value= "LIT", bg="#FFFFFF").place(x=610, y=560)
    btc_radio_button = Radiobutton(frame4, text="ETH", font=my_font3, variable=option, value= "ETH", bg="#FFFFFF").place(x=670, y=560)





    data_table()

def database():
    db = mc.connect(
        host="localhost",
        user="root",
        passwd="arvind",

        )
    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS crypto_wallet ")

    cursor.execute("use crypto_wallet")

    cursor.execute("""CREATE TABLE  IF NOT EXISTS crypto
            (username varchar(50),
             password varchar(50),
             Email varchar(50),
             Publickey varchar(100),
             privatekey varchar(100),
             BTC float(10),
             BCH float(10),
             LIT float(10),
             ETH float(10)
             )
            """)
    cursor.close()


frame1()
database()


root.mainloop()

