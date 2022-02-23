# FINAL PROJECT COMPUTER SCIENCE CLASS XII

import sys,random,datetime,os
from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk
import time

class call_bill:

    def __init__(self, root):
        f1=open('entry_file.txt',mode='r')

        self.root = root
        mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='supermarket')
        self.cursor = mydb.cursor()
        self.cursor.execute('select item,price from stock_confec')
        self.r1=self.cursor.fetchall()
        self.cursor.execute('select * from stock_cosmec')
        self.r2=self.cursor.fetchall()
        self.cursor.execute('select * from stock_groc')
        self.r3=self.cursor.fetchall()

        self. now = datetime.datetime.now()
        self.tn = self.now.strftime("%d%b%Y_%H_%M_%S")
        self.kn = self.now.strftime("%d%b%y%X")
        self.adm_user = StringVar()
        self.adm_pass = StringVar()
        self.cj_bread = StringVar()

        # self.root.geometry("1920x1080+0+0")
        self.root.title("SUPER MARKET SOFTWARE")
        pad = 3
        self._geom = '200x200+0+0'
        root.geometry("{0}x{1}+0+0".format(
            root.winfo_screenwidth() - pad, root.winfo_screenheight() - pad))
        root.bind('<Escape>', self.toggle_geom)
        self.bg_color = "#6A5ACD"
        #"#633507,6A5ACD"
        # ------------------------CUSTOMER VARIABLES--------------------:

        self.c_name = StringVar()
        self.c_contact = StringVar()
       
        self.c_billno = StringVar()
        x = random.randint(1000, 9999)


        self.c_billno.set(str(self.tn))
        # -------------------CONFECTIONARY VARIABLES-----------------------------------------
        self.c_bread =IntVar()
        self.c_butter = IntVar()
        self.c_mayo = IntVar()
        self.c_eggs = IntVar()
        self.c_cheese = IntVar()
        self.c_jam = IntVar()
        self.c_burger = IntVar()
        self.c_pizza = IntVar()
        self.c_milk = IntVar()
        # ------------------COSMETICS VARIABLES---------------------------------
        self.c_lipstick = IntVar()
        self.c_found = IntVar()
        self.c_facewash = IntVar()
        self.c_deo = IntVar()
        self.c_eyebrow = IntVar()
        self.c_lipbam = IntVar()
        self.c_facepack = IntVar()
        self.c_antiwrinkle = IntVar()
        self.c_talcum = IntVar()
        # --------------------GROCERY VARIABLES----------------------------------
        self.c_pulses = IntVar()
        self.c_flour = IntVar()
        self.c_oils = IntVar()
        self.c_spices = IntVar()
        self.c_gram = IntVar()

        # -------------------LOGIC VARIABLES-----------------------------------------
        self.confec_total = StringVar()
        self.cosmec_total = StringVar()
        self.groc_total = StringVar()

        #--------------------COST VARIABLES------------------------------------------
        self.costbread  = self.r1[0][1]
        self.costbutter = self.r1[1][1]
        self.costmayo =   self.r1[2][1]
        self.costeggs   = self.r1[3][1]
        self.costcheese = self.r1[4][1]
        self.costjam   =  self.r1[5][1]
        self.costburger = self.r1[6][1]
        self.costpizza  = self.r1[7][1]
        self.costmilk   = self.r1[8][1]

        self.costlipst   =self.r2[0][1]
        self.costfound  = self.r2[1][1]
        self.costfacewa = self.r2[2][1]
        self.costdeo = self.r2[3][1]
        self.costeye  = self.r2[4][1]
        self.costlipba    = self.r2[5][1]
        self.costfacepa   = self.r2[6][1]
        self.costantiwr = self.r2[7][1]
        self.costtalcum = self.r2[8][1]

        self.costpulses = self.r3[0][1]
        self.costflour    = self.r3[1][1]
        self.costoil  = self.r3[2][1]
        self.costspices   = self.r3[3][1]
        self.costgram = self.r3[4][1]
       # ---------------------------------------------------------------------------

        self.bg = ImageTk.PhotoImage(
            file="C://Users//Rohan Sekhri//Pictures//customer21.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ===========login frame====================================================================================================================================================
        Frame_call_adlogin = Frame(self.root, bg="white")
        Frame_call_adlogin.place(x=500, y=250, height=340, width=500)

        title = Label(Frame_call_adlogin, text="Admin Login Here ", font=("impact", 30, "bold"), fg="#633507",
                      bg='white').place(x=90, y=30)
        desc = Label(Frame_call_adlogin, text="Admin Login Area", font=("Goudy old style", 15, "bold"), fg="#633507",
                     bg='white').place(x=90, y=100)
        lbl_user = Label(Frame_call_adlogin, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg='white').place(x=90, y=140)
        self.txt_user = Entry(Frame_call_adlogin,textvariable=self.adm_user, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(Frame_call_adlogin, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg='white').place(x=90, y=210)
        self.txt_pass = Entry(Frame_call_adlogin,show='*',textvariable=self.adm_pass, font=("times new roman", 15), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        # forget_btn=Button(Frame_call_login,text="Forget Password ?",bg="white",fg="#d77337",bd=0,font=("time new roman",12)).place(x=90,y=280)
        login_btn = Button(self.root, command=self.login, text="Login", fg="white", bg="#633507",
                           font=("time new roman", 20)).place(x=800, y=535, width=180, height=40)
        cancel_btn = Button(command=self.exit3,text="cancel", fg="#633507", bd=0, bg="white",
                            font=("time new roman", 20)).place(x=560, y=535, width=180, height=40)



    def login(self):
        gn = 0
        datadb =mysql.connector.connect(host='localhost',user='root',password='root',database='supermarket')
        cursor=datadb.cursor()
        sql=('select * from admin')
        cursor.execute(sql)
        ma=cursor.fetchall()

        if  self.adm_user.get() != '' and  str(self.adm_pass.get()) !='':
            for i in ma:
                if i[0]==str(self.adm_user.get()) and i[1]==int(self.adm_pass.get()):
                    gn+=1
                    self.display()
                else:
                    gn+=0
            if gn==0:
                print('YOU ARE NOT AN ADMIN!!!')
                sys.exit()

        else:
            messagebox.showerror('Invalid', '!!MANDATORY TO FILL ALL BLANKS FOR ACCESS!!')






    def exit3(self):
        sys.exit()



    def display(self):
            h1 = Label(self.root, text=("     JACKPOT SUPER MARKET(JSM)     "), fg='yellow', bd=12,
                       relief=GROOVE, bg=self.bg_color, font=("family of roman", 30, "bold"), pady=2).pack(
                fill=X)
            h2 = Label(self.root, text=("     {OFFLINE STORE}     "), fg='yellow', bd=12, relief=GROOVE,
                       bg=self.bg_color, font=("family of roman", 25, "bold"), pady=2).pack(fill=X)
            h3 = LabelFrame(self.root, text=("Customer Detail Corner"),
                            font=("family of roman ", 14, "bold"), bg=self.bg_color, fg="grey")
            h3.place(x=0, y=120, relwidth=1)

            cu_nam = Label(h3, text=("CustomerName"), font=("family of roman", 15, "bold"), fg='yellow',
                           bg=self.bg_color).grid(row=0, column=0, padx=10, pady=6)
            cu_en = Entry(h3, width=20, textvariable=self.c_name, font=("arial 15"), bd=12,
                          relief=GROOVE, fg="orange").grid(row=0, column=1, padx=20, pady=6)

            ph_nam = Label(h3, text=("ContactNo."), font=("family of roman", 15, "bold"), fg='yellow',
                           bg=self.bg_color).grid(row=0, column=3, padx=20, pady=6)
            ph_en = Entry(h3, width=20, textvariable=self.c_contact, font=("arial 15"), bd=12,
                          relief=GROOVE, fg="orange").grid(row=0, column=4, padx=40, pady=6)
            bn_nam = Label(h3, text=("BillNo."), font=("family of roman", 15, "bold"), fg='yellow',
                           bg=self.bg_color).grid(row=0, column=5, padx=10, pady=6)
            bn_en = Entry(h3, width=20, textvariable=self.c_billno,font="aerial 15", bd=12,
                          relief=GROOVE, fg="orange").grid(row=0, column=6, padx=60, pady=6)

            sett_bn=Button(h3,width=5,command=self.set,text="SET",font="aerial 15", fg="black",bg="yellow").grid(row=0,column=8,padx=10,pady=6)
            s_en = Button(h3, width=5, command=self.search, text="?",
                          fg="black",bg='yellow').grid(row=0, column=7, padx=10, pady=6)

            # ------------------------------------------CONFECTIONARY ITEMS--------------------------------------------------------------------------------------
            h4 = LabelFrame(self.root, text=("CONFECTIONARY"), bd=12, relief=GROOVE,
                            font=('family of roman', 15, "bold"), fg="grey", bg=self.bg_color)
            h4.place(x=0, y=200, width=370, height=600)
            co_nam1 = Label(h4, text=("BREAD--₹"+str(self.costbread)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=0, column=0, padx=20, pady=6)
            co_en1 = Entry(h4, width=10, textvariable=self.c_bread, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=0, column=1, padx=10, pady=6)
            co_nam2 = Label(h4, text=("BUTTER--₹"+str(self.costbutter)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=1, column=0, padx=10, pady=6)
            co_en2 = Entry(h4, width=10, textvariable=self.c_butter, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=1, column=1, padx=20, pady=6)

            co_nam3 = Label(h4, text=("MAYONISE--₹"+str(self.costmayo)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=2,
                                              column=0,
                                              padx=10,
                                              pady=6)
            co_en3 = Entry(h4, width=10, textvariable=self.c_mayo, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=2, column=1, padx=20,
                                                            pady=6)
            co_nam4 = Label(h4, text=("EGGS--₹"+str(self.costeggs)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=3,
                                              column=0,
                                              padx=10,
                                              pady=6)
            co_en4 = Entry(h4, width=10, textvariable=self.c_eggs, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=3, column=1, padx=20,
                                                            pady=6)
            co_nam5 = Label(h4, text=("CHEESE--₹"+str(self.costcheese)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=4,
                                              column=0,
                                              padx=10,
                                              pady=6)
            co_en5 = Entry(h4, width=10, textvariable=self.c_cheese, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=4, column=1, padx=20,
                                                            pady=6)

            co_nam6 = Label(h4, text=("JAM--₹"+str(self.costjam)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=5,
                                              column=0,
                                              padx=10,
                                              pady=6)
            co_en6 = Entry(h4, width=10, textvariable=self.c_jam, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=5, column=1, padx=20,
                                                            pady=6)

            co_nam7 = Label(h4, text=("BURGER BUNS--₹"+str(self.costburger)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=6,
                                              column=0,
                                              padx=10,
                                              pady=6)
            co_en7 = Entry(h4, width=10, textvariable=self.c_burger, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=6, column=1,
                                                            padx=20,
                                                            pady=6)
            co_nam8 = Label(h4, text=("PIZZA BASE--₹"+str(self.costpizza)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=7,
                                              column=0,
                                              padx=10,
                                              pady=6)
            co_en8 = Entry(h4, width=10, textvariable=self.c_pizza, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=7, column=1,
                                                            padx=20,
                                                            pady=6)
            co_nam9 = Label(h4, text=("MILK--₹"+str(self.costmilk)), font=("family of roman", 15, "bold"), fg='yellow',
                            bg=self.bg_color).grid(row=8,
                                              column=0,
                                              padx=10,
                                              pady=6)
            co_en9 = Entry(h4, width=10, textvariable=self.c_milk, font=("arial 15"), bd=12,
                           relief=GROOVE, fg="orange").grid(row=8, column=1,
                                                            padx=20,
                                                            pady=6)

            # -------------------------------------------------COSMETICS PRODUCTS---------------------------------------------------------------------------------
            h5 = LabelFrame(self.root, text=('COSMETICS'), bd=12, relief=GROOVE,
                            font=("family of roman", 15, "bold"), bg=self.bg_color, fg="grey")
            h5.place(x=370, y=200, width=430, height=600)
            cos_nam1 = Label(h5, text=("LIPSTICK--₹"+str(self.costlipst)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(row=0,
                                               column=0,
                                               padx=10,
                                               pady=6)
            cos_en1 = Entry(h5, width=10, textvariable=self.c_lipstick, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=0, column=1,
                                                             padx=20, pady=6)

            cos_nam2 = Label(h5, text=("FOUNDATION--₹"+str(self.costfound)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=1,
                column=0,
                padx=10,
                pady=6)
            cos_en2 = Entry(h5, width=10, textvariable=self.c_found, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=1, column=1,
                                                             padx=20, pady=6)

            cos_nam3 = Label(h5, text=("FACE WASH--₹"+str(self.costfacewa)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=2,
                column=0,
                padx=10,
                pady=6)
            cos_en3 = Entry(h5, width=10, textvariable=self.c_facewash, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=2, column=1,
                                                             padx=20, pady=6)

            cos_nam4 = Label(h5, text=("DEODRANTS--₹"+str(self.costdeo)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=3,
                column=0,
                padx=10,
                pady=6)
            cos_en4 = Entry(h5, width=10, textvariable=self.c_deo, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=3, column=1,
                                                             padx=20, pady=6)

            cos_nam5 = Label(h5, text=("EYEBROW PENCIL--₹"+str(self.costeye)), font=("family of roman", 15, "bold"),
                             fg='yellow', bg=self.bg_color).grid(
                row=4,
                column=0,
                padx=10,
                pady=6)
            cos_en5 = Entry(h5, width=10, textvariable=self.c_eyebrow, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=4, column=1,
                                                             padx=20, pady=6)

            cos_nam6 = Label(h5, text=("LIP BAM--₹"+str(self.costlipba)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=5,
                column=0,
                padx=10,
                pady=6)
            cos_en6 = Entry(h5, width=10, textvariable=self.c_lipbam, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=5, column=1,
                                                             padx=20, pady=6)

            cos_nam7 = Label(h5, text=("FACE PACK--₹"+str(self.costfacepa)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=6,
                column=0,
                padx=10,
                pady=6)
            cos_en7 = Entry(h5, width=10, textvariable=self.c_facepack, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=6, column=1,
                                                             padx=20, pady=6)

            cos_nam8 = Label(h5, text=("ANTI WRINKLE CREAM--₹"+str(self.costantiwr)), font=("family of roman", 15, "bold"),
                             fg='yellow', bg=self.bg_color).grid(
                row=7,
                column=0,
                padx=10,
                pady=6)
            cos_en8 = Entry(h5, width=10, textvariable=self.c_antiwrinkle, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=7, column=1,
                                                             padx=20, pady=6)

            cos_nam9 = Label(h5, text=("TALCUM POWDER--₹"+str(self.costtalcum)), font=("family of roman", 15, "bold"),
                             fg='yellow', bg=self.bg_color).grid(
                row=8,
                column=0,
                padx=10,
                pady=6)
            cos_en1 = Entry(h5, width=10, textvariable=self.c_talcum, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=8, column=1,
                                                             padx=20, pady=6)

            # ----------------------------------------------------GROCERIES--------------------------------------------------------------------------

            h6 = LabelFrame(self.root, text=("GROCERY"), font=("family of roman", 15, "bold"),
                            bg=self.bg_color, fg="grey", bd=12, relief=GROOVE)
            h6.place(x=800, y=200, width=375, height=380)

            gos_nam1 = Label(h6, text=("PULSES--₹"+str(self.costpulses)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=0,
                column=0,
                padx=10,
                pady=6)
            gos_en1 = Entry(h6, width=10, textvariable=self.c_pulses, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=0, column=1,
                                                             padx=20, pady=6)

            gos_nam2 = Label(h6, text=("FLOUR--₹"+str(self.costflour)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=1,
                column=0,
                padx=10,
                pady=6)
            gos_en2 = Entry(h6, width=10, textvariable=self.c_flour, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=1, column=1,
                                                             padx=20, pady=6)

            gos_nam3 = Label(h6, text=("OILS--₹"+str(self.costoil)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=2,
                column=0,
                padx=10,
                pady=6)
            gos_en3 = Entry(h6, width=10, textvariable=self.c_oils, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=2, column=1,
                                                             padx=20, pady=6)
            gos_nam4 = Label(h6, text=("SPICES--₹"+str(self.costspices)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=3,
                column=0,
                padx=10,
                pady=6)
            gos_en4 = Entry(h6, width=10, textvariable=self.c_spices, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange").grid(row=3, column=1,
                                                             padx=20, pady=6)

            gos_nam5 = Label(h6, text=("GRAM FLOUR--₹"+str(self.costgram)), font=("family of roman", 15, "bold"), fg='yellow',
                             bg=self.bg_color).grid(
                row=4,
                column=0,
                padx=10,
                pady=6)
            gos_en5 = Entry(h6, width=10, textvariable=self.c_gram, font=("arial 15"), bd=12,
                            relief=GROOVE, fg="orange")

            # gos_en5.insert(0,"RAJDHANI ")
            gos_en5.grid(row=4, column=1, padx=20, pady=6)
            # -------------------------------------------BILLING AREA------------------------------------------------------------------------------

            h7 = Frame(self.root, relief=GROOVE)
            h7.place(x=1170, y=200, width=365, height=380)
            bil_title = Label(h7, text='BILL AREA', font='arial 15', bd=7, relief=GROOVE).pack(fill=X)
            scroll_y = Scrollbar(h7, orient=VERTICAL)
            self.text_area = Text(h7, yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_y.config(command=self.text_area.yview)
            self.text_area.pack()

            # ------------------------------------------SWITCH CONTROLS-------------------------------------------------------------------------------
            h8 = LabelFrame(self.root, text='', bd=12, bg=self.bg_color, relief=GROOVE)
            h8.place(x=800, y=580, width=730, height=220)

            to_btn1 = Button(h8, width=14, command=self.bill_area, height=5, text=("BILL"), bg='yellow',
                             font=("arial 15")).grid(row=0, column=0,
                                                     padx=10, pady=6)

            to_btn2 = Button(h8, width=12, command=self.save_bill, height=5, text=("SAVE"), bg='yellow',
                             font=("arial 15")).grid(row=0, column=1,
                                                     padx=10, pady=6)

            to_btn3 = Button(h8, width=14, height=5, command=self.mainpro, text=("TRAS_HIS"),
                             bg='yellow', font=("arial 15")).grid(row=0, column=2,
                                                                  padx=10, pady=6)

            to_btn4 = Button(h8, width=5, command=self.refresh, height=5, text=("CLEAR"), bg='yellow',
                             font=("arial 15")).grid(row=0, column=3,
                                                     padx=10, pady=6)


            to_btn5 = Button(h8, width=5, command=self.exit, height=5, text=("EXIT"), bg='yellow',
                             font=("arial 15")).grid(row=0, column=5,
                                                     padx=10, pady=6)

    def bill_area(self):

        if self.c_name.get() == '' or self.c_contact.get() == '':
            messagebox.showerror('ERROR', 'CUSTOMER DETAILS NECCESSARY!!!')
        else:
            self.confec_total = str(
                (self.c_bread.get() * int(self.costbread)) +
                (self.c_butter.get() * int(self.costbutter)) +
                (self.c_cheese.get() * int(self.costcheese)) +
                (self.c_jam.get() * int(self.costjam)) +
                (self.c_mayo.get() * int(self.costmayo)) +
                (self.c_burger.get() * int(self.costburger)) +
                (self.c_pizza.get() * int(self.costpizza)) +
                (self.c_milk.get() * int(self.costmilk)) +
                (self.c_eggs.get() * int(self.costeggs)))
            # print('TOTAL CONFECTIONARY ITEMS:', self.confec_total)
            self.cosmec_total = str(
                (self.c_lipstick.get() * int(self.costlipst)) +
                (self.c_lipbam.get() * int(self.costlipba)) +
                (self.c_talcum.get() * int(self.costtalcum)) +
                (self.c_deo.get() * int(self.costdeo)) +
                (self.c_antiwrinkle.get() * int(self.costantiwr)) +
                (self.c_facepack.get() * int(self.costfacepa)) +
                (self.c_facewash.get() * int(self.costfacewa))+
                (self.c_eyebrow.get() * int(self.costeye))+
                (self.c_found.get()  * int(self.costfound)))
            # print('TOTAL COSMETIC ITEMS:', self.cosmec_total)
            self.groc_total = str(
                (self.c_pulses.get() * int(self.costpulses)) +
                (self.c_flour.get() * int(self.costflour)) +
                (self.c_gram.get() * int(self.costgram)) +
                (self.c_oils.get() * int(self.costoil)) +
                (self.c_spices.get() * int(self.costspices)))
            # print('TOTAL GROCERY ITEMS:', self.groc_total)
            self.text_area.insert(END, "\n")
            self.text_area.insert(END, "\n     WELCOME TO  JACKPOT SUPER MARKET     ")
            self.text_area.insert(END, "\n-----------------------------------------")
            self.text_area.insert(END, f"\nBNO.:{self.c_billno.get()} ")
            self.text_area.insert(END, f"\tTIME:{self.kn}")
            self.text_area.insert(END, f"\nCUSTOMER NAME:{self.c_name.get()} ")
            self.text_area.insert(END, f"\nCUSTOMER MOB:{self.c_contact.get()} ")
            self.text_area.insert(END, "\n------------------------------------------")
            self.text_area.insert(END, "\n------------------------------------------")
            self.text_area.insert(END, f"\nCONFECT_ITEM TOTAL:Rs.{self.confec_total}")
            self.text_area.insert(END, f"\nCOSMETIC _ITEM TOTAL:Rs.{self.cosmec_total}")
            self.text_area.insert(END, f"\nGROCERY _ITEM TOTAL:Rs.{self.groc_total}")
            self.text_area.insert(END,
                                  f"\nTOTAL(WITHOUT TAX):Rs.{int(self.confec_total) + int(self.cosmec_total) + int(self.groc_total)}")
            z = int((int(self.groc_total) + int(self.cosmec_total) + int(self.confec_total)) * 0.05)
            self.text_area.insert(END, f"\nTAX ON ITEMS(5%):Rs.{z}")
            self.text_area.insert(END, '\n--------------------------------')
            self.text_area.insert(END,
                                  f"\nGRAND TOTAL:Rs.{int(self.confec_total) + int(self.cosmec_total) + int(self.groc_total) + z}")

    def exit(self):
        print('!!!THANKYOU FOR YOUR VISIT!!!')
        sys.exit()

    def refresh(self):
        self.text_area.delete('1.0', END)
        messagebox.showinfo('REFRESHED', 'BILL AREA REFRESHED!!!')

    def save_bill(self):
        op = messagebox.askyesno('SAVE BILL', 'DO YOU WANT TO SAVE BILL')
        if op > 0:
            self.bill_data = (self.text_area.get('1.0', END))
            f1 = open("BILLS/" + str(self.c_billno.get()) + '.txt', 'w')
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo('SAVED', f'BILL NO:{self.c_billno.get()} IS SUCCESSFULLY SAVED!!!')
        else:
            return
    def set(self):
        print('-'*30)
        print('JACKPOT SUPER MARKET ')
        print('-'*4,'SETTINGS','-'*4)
        print('-'*30)
        print()
        print('OPTIONS')
        print('1.FOR PRICE CHANGE:')
        print('2.FOR ADMIN CHANGE:')

        cho=int(input('ENTER YOUR CHOICE 1/2: '))

        if cho==1:
            print('REQUEST FOR PRICE CHANGE...')
            print('PERMISSION GRANTED!!')
            print('-'*45)
            print('connecting to database...')
            conn=mysql.connector.connect(host='localhost',user='root',password='root',database='supermarket')
            mycur=conn.cursor()

            if conn.is_connected() ==True:
                x='connected'
                print('STATUS:' + str(x))
                print()
                print('-'*45)
                print('1.FOR CONFECTIONERY ITEM PRICE CHANGE:')
                print('2.FOR COSMETIC ITEM PRICE CHANGE:')
                print('3.FOR GROCERY ITEM PRICE CHANGE:')
                print('-'*45)
                print()
                cho2=int(input('ENTER YOUR CHOICE 1/2/3: '))
                print('-'*30)
                if cho2==1:
                    en=int(input('ENTER NO. OF ITEMS WANT TO CHANGE OUT OF 9: '))
                    for i in range(en):
                        print('')
                        print('-'*30)
                        print('REQUEST FOR CONFEC ITEM PRICE CHANGE...')
                        print('PERMISSION GRANTED!!')
                        print('')
                        print('1.FOR BREAD ITEM PRICE CHANGE:')
                        print('2.FOR BUTTER ITEM PRICE CHANGE:')
                        print('3.FOR MAYO ITEM PRICE CHANGE:')
                        print('4.FOR EGGS ITEM PRICE CHANGE:')
                        print('5.FOR CHEESE ITEM PRICE CHANGE:')
                        print('6.FOR JAM ITEM PRICE CHANGE:')
                        print('7.FOR BURGER_BUN ITEM PRICE CHANGE:')
                        print('8.FOR PIZZA_BASE ITEM PRICE CHANGE:')
                        print('9.FOR MILK ITEM PRICE CHANGE:')
                        print('-'*30)
                        cho3=int(input('ENTER YOUR CHOICE 1/2/3/4/5/6/7/8/9:'))

                        if cho3==1:
                            itm='bread'
                            prc=int(input('ENTER NEW PRICE: '))
                            l=str(prc)
                            sql=("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql,(l,itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 2:
                            itm = 'butter'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 3:
                            itm = 'mayonise'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                            #conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 4:
                            itm = 'eggs'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 5:
                            itm = 'cheese'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 6:
                            itm = 'jam'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 7:
                            itm = 'burger_buns'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 8:
                            itm = 'pizza_base'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 9:
                            itm = 'milk'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_confec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        else:
                            print('GOING OUT FROM CONFECTIONERY UPDATE COLUMN')
                            print('BYE', '!', 'BYE')
                            conn.close()

                elif cho2==2:
                    en = int(input('ENTER NO. OF ITEMS WANT TO CHANGE OUT OF 9: '))
                    for i in range(en):
                        print('')
                        print('-' * 30)
                        print('REQUEST FOR COSMECTIC ITEM PRICE CHANGE...')
                        print('PERMISSION GRANTED!!')
                        print('')
                        print('1.FOR LIPSTICK ITEM PRICE CHANGE:')
                        print('2.FOR FOUNDATION ITEM PRICE CHANGE:')
                        print('3.FOR FACE_WASH ITEM PRICE CHANGE:')
                        print('4.FOR DEO ITEM PRICE CHANGE:')
                        print('5.FOR EYEBROW_PEN ITEM PRICE CHANGE:')
                        print('6.FOR LIPBAM ITEM PRICE CHANGE:')
                        print('7.FOR FACE_PACK ITEM PRICE CHANGE:')
                        print('8.FOR ANTI_CREAM ITEM PRICE CHANGE:')
                        print('9.FOR TALCUM_POWDER ITEM PRICE CHANGE:')
                        print('-'*30)
                        cho3=int(input('ENTER YOUR CHOICE 1/2/3/4/5/6/7/8/9:'))

                        if cho3==1:
                            itm='lipstick'
                            prc=int(input('ENTER NEW PRICE: '))
                            l=str(prc)
                            sql=("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql,(l,itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 2:
                            itm = 'foundation'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 3:
                            itm = 'face_wash'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                            #conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 4:
                            itm = 'deo'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                            #conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 5:
                            itm = 'eyebrow_pencil'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                            #conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 6:
                            itm = 'lipbam'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                            #conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 7:
                            itm = 'face_pack'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                            #conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 8:
                            itm = 'anti_cream'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                            #conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 9:
                            itm = 'talcum_powder'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_cosmec set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                            #conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        else:
                            print('GOING OUT FROM COSMETIC UPDATE COLUMN')
                            print('BYE', '!', 'BYE')
                            conn.close()

                elif cho2==3:
                    en = int(input('ENTER NO. OF ITEMS WANT TO CHANGE OUT OF 5: '))
                    for i in range(en):
                        print('')
                        print('-' * 30)
                        print('REQUEST FOR GROCERY ITEM PRICE CHANGE...')
                        print('PERMISSION GRANTED!!')
                        print('')
                        print('1.FOR PULSES ITEM PRICE CHANGE:')
                        print('2.FOR FLOUR ITEM PRICE CHANGE:')
                        print('3.FOR OILS ITEM PRICE CHANGE:')
                        print('4.FOR SPICES ITEM PRICE CHANGE:')
                        print('5.FOR GRAM_FLOUR ITEM PRICE CHANGE:')
                        print('-'*30)
                        cho3=int(input('ENTER YOUR CHOICE 1/2/3/4/5:'))

                        if cho3 == 1:
                            itm = 'pulses'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_groc set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 2:
                            itm = 'flour'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_groc set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 3:
                            itm = 'oils'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_groc set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 4:
                            itm = 'spices'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_groc set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        elif cho3 == 5:
                            itm = 'gram_flour'
                            prc = int(input('ENTER NEW PRICE: '))
                            l = str(prc)
                            sql = ("update stock_groc set price=%s where item=%s")
                            mycur.execute(sql, (l, itm))
                            conn.commit()
                           # conn.close()

                            print('CHANGES APPLIED ..')
                            print('PLZ CHECK!!')

                        else:
                            print('GOING OUT FROM GROCERY UPDATE COLUMN')
                            print('BYE','!','BYE')
                            conn.close()



            else:
                x='failed'
                print('STATUS:'+str(x))




        elif cho==2:
            print('REQUEST FOR ADMIN CHANGE...')
            print('PERMISSION GRANTED!!')
            print('-' * 45)
            print('connecting to database...')
            conn = mysql.connector.connect(host='localhost', user='root', password='root', database='supermarket')
            mycur = conn.cursor()

            if conn.is_connected() == True:
                x = 'connected'
                print('STATUS:' + str(x))
                print()
                print('-' * 45)
                print('1.FOR NEW ADMIN:')
                print('2.FOR DELETING EXISTING ADMIN :')
                print('3.FOR UPDATING ADMIN PASSWORD: ')
                print('-' * 45)
                print()
                cho3=int(input("ENTER YOUR CHOICE 1/2/3: "))
                print('-'*45)
                print('')

                if cho3==1:
                    print('')
                    print('-'*30)
                    print('REQUEST FOR NEW ADMIN...')
                    print('PERMISSION GRANTED!!')
                    print('')
                    user=input('ENTER NEW ADMIN USERNAME: ')
                    pas=int(input('SET 4 DIGIT NUMERIC PASSWORD: '))
                    print('')
                    print('...................')
                    sql=('insert into admin values(%s,%s)')
                    mycur.execute(sql,(user,pas))
                    conn.commit()
                    print('ADMIN ADDED SUCCESSFULLY!!')
                    print('PLZ CHECK!')
                    sql1=('select * from admin')
                    mycur.execute(sql1)
                    dt=mycur.fetchall()
                    for i in dt:
                        print('user:',i[0])
                        print('pass:',i[1])
                    print('-'*30)
                elif cho3==2:
                    print('')
                    print('-' * 30)
                    print('REQUEST FOR DELETING  ADMIN...')
                    print('PERMISSION GRANTED!!')
                    print('')
                    user = input('ENTER USERNAME TO DELETE ADMIN: ')
                    pas = int(input('ENTER 4 DIGIT NUMERIC PASSWORD: '))
                    print('')
                    print('...................')
                    sql = ('delete from admin where user=%s and password=%s')
                    mycur.execute(sql, (user, pas))
                    conn.commit()
                    print('ADMIN DELETED SUCCESSFULLY!!')
                    print('PLZ CHECK!')
                    sql1 = ('select * from admin')
                    mycur.execute(sql1)
                    dt = mycur.fetchall()
                    for i in dt:
                        print('user:', i[0])
                        print('pass:', i[1])
                    print('-' * 30)

                elif cho3==3:
                    print('')
                    print('-' * 30)
                    print('REQUEST FOR UPDATING ADMIN...')
                    print('PERMISSION GRANTED!!')
                    print('')
                    user = input('ENTER ADMIN USERNAME: ')
                    pas = int(input('SET NEW 4 DIGIT NUMERIC PASSWORD: '))
                    sql2 = ('select * from admin')
                    mycur.execute(sql2)
                    at = mycur.fetchall()
                    for i in at:
                        if user==[i][0]:
                            print('')
                            print('...................')
                            sql = ('update table admin set password=%s where user=%s)')
                            mycur.execute(sql, ( pas,user))
                            conn.commit()
                            print('ADMIN UPDATED SUCCESSFULLY!!')
                            print('PLZ CHECK!')
                            sql1 = ('select * from admin')
                            mycur.execute(sql1)
                            dt = mycur.fetchall()
                            for i in dt:
                                print('user:', i[0])
                                print('pass:', i[1])
                            print('-' * 30)
                        else:
                            print('INVALID USERNAME!!')
                            print('TRY AGAIN')
                            self.set()

                else:
                    print('RESTART....')
                    self.set()
            else:
                x='failed'
                print('STATUS:'+str(x))

        else:
            print('WRONG CHOICE!!!')
            print('TRY AGAIN ')










    def search(self):
        print()
        cn = 0
        for i in os.listdir("BILLS"):

            if i.split('.')[0] == self.c_billno.get():
                f1 = open(f"BILLS/{i}", 'r')
                r1 = f1.read()
                self.text_area.delete('1.0', END)
                self.text_area.insert(END, r1)
                messagebox.showinfo('DATA FETCHED', 'DATA FOUND AND PASTED ON BILL AREA')
                cn = 1
        if cn == 0:
            messagebox.showerror('ERROR', 'PLZ ENTER A VALID BILL NO.')

    def mainpro(self):
        class call_transac:

            def __init__(self, foot):
                self.foot = foot
                # self.root.geometry("1920x1080+0+0")
                self.foot.title("JSM WINDOW")
                pad = 3
                self._geom = '200x200+0+0'
                foot.geometry("{0}x{1}+0+0".format(
                    foot.winfo_screenwidth() - pad, foot.winfo_screenheight() - pad))
                foot.bind('<Escape>', self.toggle_geom)
                bg_color = "#633507"

                h9 = Frame(self.foot, relief=GROOVE, bg=bg_color)
                h9.place(x=0, y=0, width=1500, height=780)
                bil_title = Label(h9, text='TRANSACTION HISTORY', font='arial 15', bd=10,
                                  relief=GROOVE, fg='orange').pack(fill=X)
                btn1 = Button(h9, command=self.trasac, text='SEARCH', bd=6, fg='red',
                              bg='yellow').pack(fill=X)
                btn2 = Button(h9, command=lambda: call_bill(root), text='BACK', bd=6, fg='red',
                              bg='yellow').pack(fill=X)
                btn3 = Button(h9, command=self.exit2, text='EXIT', bd=6, fg='red',
                              bg='yellow').pack(fill=X)
                scroll_y = Scrollbar(h9, orient=VERTICAL)
                self.text_area = Text(h9, yscrollcommand=scroll_y.set, width=100, height=100,
                                      fg='orange')
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.text_area.yview)
                self.text_area.pack()

            def trasac(self):
                for i in os.listdir("BILLS"):
                    x = i.split('.')[0]

                    f1 = open('BILLS\\' + str(x) + '.txt', 'r')
                    r1 = f1.read()
                    self.text_area.insert(END,
                                          "\n------------------(OFFLINE MODE TRANSACTION)------------------")
                    self.text_area.insert(END,
                                          '\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
                    self.text_area.insert(END, f':{r1}')
                    self.text_area.insert(END,
                                          '\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
                    self.text_area.insert(END, '')

            def exit2(self):
                print('!!!THANKYOU FOR YOUR VISIT!!!')
                sys.exit()


            def toggle_geom(self, event):
                geom = self.foot.winfo_geometry()
                print(geom, self._geom)
                self.foot.geometry(self._geom)
                self._geom = geom

        foot = Tk()
        x = call_transac(foot)
        foot.mainloop()

    def toggle_geom(self, event):
        geom = self.root.winfo_geometry()
        print(geom, self._geom)
        self.root.geometry(self._geom)
        self._geom = geom


root = Tk()
x = call_bill(root)
root.mainloop()
