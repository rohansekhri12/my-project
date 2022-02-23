

from tkinter import *
class call_bill:

    def __init__(self,root):
        self.root=root
       # self.root.geometry("1920x1080+0+0")
        self.root.title("SUPER MARKET SOFTWARE")
        pad = 3
        self._geom = '200x200+0+0'
        root.geometry("{0}x{1}+0+0".format(
        root.winfo_screenwidth() - pad, root.winfo_screenheight() - pad))
        root.bind('<Escape>', self.toggle_geom)
        bg_color="#633507"
        h1=Label(self.root,text=("     JACKPOT SUPER MARKET(JSM)     "),fg='yellow',bd=12,relief=GROOVE,bg=bg_color,font=("family of roman",30,"bold"),pady=2).pack(fill=X)
        h2=Label(self.root,text=("     {BILLING CORNER}     "),fg='yellow',bd=12,relief=GROOVE,bg=bg_color,font=("family of roman",25,"bold"),pady=2).pack(fill=X)
        h3=LabelFrame(self.root,text=("Customer Detail Corner"),font=("family of roman ",14,"bold"),bg=bg_color,fg="grey")
        h3.place(x=0,y=120,relwidth=1)

        cu_nam=Label(h3,text=("CustomerName"),font=("family of roman",15,"bold"),fg='yellow',bg=bg_color).grid(row=0,column=0,padx=10,pady=6)
        cu_en=Entry(h3,width=20,font=("arial 15"),bd=12,relief=GROOVE,fg="orange").grid(row=0,column=1,padx=20,pady=6)

        ph_nam = Label(h3, text=("ContactNo."), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=0, column=3, padx=20, pady=6)
        ph_en = Entry(h3, width=20, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=0, column=4, padx=40,pady=6)
        bn_nam = Label(h3, text=("BillNo."), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=0, column=5, padx=10, pady=6)
        bn_en = Entry(h3, width=20, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=0, column=6, padx=60,pady=6)

        s_en =Button(h3,width=10,text="Search",font="arial 15",fg="black").grid(row=0,column=7,padx=10,pady=6)

#------------------------------------------CONFECTIONARY ITEMS--------------------------------------------------------------------------------------
        h4=LabelFrame(self.root,text=("CONFECTIONARY"),bd=12,relief=GROOVE,font=('family of roman',15,"bold"),fg="grey",bg=bg_color)
        h4.place(x=0,y=200,width=370,height=600)
        co_nam1 = Label(h4, text=("BREAD"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=0, column=0, padx=10, pady=6)
        co_en1 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=0, column=1, padx=20,pady=6)
        co_nam2 = Label(h4, text=("BUTTER"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=1,column=0,padx=10,pady=6)
        co_en2 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=1, column=1, padx=20,pady=6)

        co_nam3 = Label(h4, text=("MAYONISE"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=2,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=6)
        co_en3 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=2, column=1, padx=20,
                                                                                               pady=6)
        co_nam4 = Label(h4, text=("EGGS"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=3,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=6)
        co_en4 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=3, column=1, padx=20,
                                                                                               pady=6)
        co_nam5 = Label(h4, text=("CHEESE"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=4,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=6)
        co_en5 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=4, column=1, padx=20,
                                                                                               pady=6)

        co_nam6 = Label(h4, text=("JAM"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=5,
                                                                                                                column=0,
                                                                                                                padx=10,
                                                                                                                pady=6)
        co_en6 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=5, column=1, padx=20,
                                                                                               pady=6)

        co_nam7 = Label(h4, text=("BURGER BUNS"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=6,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=6)
        co_en7 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=6, column=1,
                                                                                                padx=20,
                                                                                                pady=6)
        co_nam8 = Label(h4, text=("PIZZA BASE"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=7,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=6)
        co_en8 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=7, column=1,
                                                                                                padx=20,
                                                                                                pady=6)
        co_nam9 = Label(h4, text=("MILK"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=8,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=6)
        co_en9 = Entry(h4, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=8, column=1,
                                                                                                padx=20,
                                                                                                pady=6)

        #-------------------------------------------------COSMETICS PRODUCTS---------------------------------------------------------------------------------
        h5=LabelFrame(self.root,text=('COSMETICS'),bd=12,relief=GROOVE,font=("family of roman",15,"bold"),bg=bg_color,fg="grey")
        h5.place(x=370,y=200,width=430,height=600)
        cos_nam1 = Label(h5, text=("LIPSTICK"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(row=0,
                                                                                                                 column=0,
                                                                                                                 padx=10,
                                                                                                                 pady=6)
        cos_en1 = Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=0, column=1,
                                                                                                padx=20, pady=6)

        cos_nam2 = Label(h5, text=("FOUNDATION"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=1,
            column=0,
            padx=10,
            pady=6)
        cos_en2 = Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=1, column=1,
                                                                                                 padx=20, pady=6)

        cos_nam3 = Label(h5, text=("FACE WASH"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=2,
            column=0,
            padx=10,
            pady=6)
        cos_en3 = Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=2, column=1,
                                                                                                 padx=20, pady=6)

        cos_nam4 = Label(h5, text=("DEODRANTS"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=3,
            column=0,
            padx=10,
            pady=6)
        cos_en4 = Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=3, column=1,
                                                                                                 padx=20, pady=6)

        cos_nam5 = Label(h5, text=("EYEBROW PENCIL"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=4,
            column=0,
            padx=10,
            pady=6)
        cos_en5 = Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=4, column=1,
                                                                                                 padx=20, pady=6)

        cos_nam6 = Label(h5, text=("LIP BAM"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=5,
            column=0,
            padx=10,
            pady=6)
        cos_en6 = Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=5, column=1,
                                                                                                 padx=20, pady=6)

        cos_nam7 = Label(h5, text=("FACE PACK"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=6,
            column=0,
            padx=10,
            pady=6)
        cos_en7 = Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=6, column=1,
                                                                                                 padx=20, pady=6)

        cos_nam8 = Label(h5, text=("ANTI WRINKLE CREAM"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=7,
            column=0,
            padx=10,
            pady=6)
        cos_en8= Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=7, column=1,
                                                                                                 padx=20, pady=6)

        cos_nam9 = Label(h5, text=("TALCUM POWDER"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=8,
            column=0,
            padx=10,
            pady=6)
        cos_en1 = Entry(h5, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=8, column=1,
                                                                                                 padx=20, pady=6)




#----------------------------------------------------GROCERIES--------------------------------------------------------------------------

        h6=LabelFrame(self.root,text=("GROCERY"),font=("family of roman",15,"bold"),bg=bg_color,fg="grey",bd=12,relief=GROOVE)
        h6.place(x=800,y=200,width=375,height=380)

        gos_nam1 = Label(h6, text=("PULSES"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=0,
            column=0,
            padx=10,
            pady=6)
        gos_en1 = Entry(h6, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=0, column=1,
                                                                                                 padx=20, pady=6)

        gos_nam2 = Label(h6, text=("FLOUR"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=1,
            column=0,
            padx=10,
            pady=6)
        gos_en2 = Entry(h6, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=1, column=1,
                                                                                                 padx=20, pady=6)

        gos_nam3 = Label(h6, text=("OILS"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=2,
            column=0,
            padx=10,
            pady=6)
        gos_en3 = Entry(h6, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=2, column=1,
                                                                                                 padx=20, pady=6)
        gos_nam4 = Label(h6, text=("SPICES"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=3,
            column=0,
            padx=10,
            pady=6)
        gos_en4 = Entry(h6, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange").grid(row=3, column=1,
                                                                                                 padx=20, pady=6)

        gos_nam5 = Label(h6, text=("GRAM FLOUR"), font=("family of roman", 15, "bold"), fg='yellow', bg=bg_color).grid(
            row=4,
            column=0,
            padx=10,
            pady=6)
        gos_en5 = Entry(h6, width=10, font=("arial 15"), bd=12, relief=GROOVE, fg="orange" )

        gos_en5.insert(0,"RAJDHANI ")
        gos_en5.grid(row=4,column=1,padx=20,pady=6)
#-------------------------------------------BILLING AREA------------------------------------------------------------------------------

        h7=LabelFrame(self.root,text=('BILLING AREA'),font=("family of roman",15,"bold"),fg="grey",bd=12,relief=GROOVE)
        h7.place(x=1170,y=200,width=365,height=380)

#------------------------------------------SWITCH CONTROLS-------------------------------------------------------------------------------



        h8=LabelFrame(self.root,text='',bd=12,bg=bg_color,relief=GROOVE)
        h8.place(x=800,y=580,width=730,height=220)

        to_btn1=Button(h8,width=14,height=5,text=("TOTAL"),bg='yellow',font=("arial 15")).grid(row=0,column=0,padx=10,pady=6)

        to_btn2 = Button(h8, width=12,height=5,text=("BILL"),bg='yellow', font=("arial 15")).grid(row=0, column=1, padx=10, pady=6)

        to_btn3 = Button(h8, width=14,height=5,text=("CLEAR"),bg='yellow', font=("arial 15")).grid(row=0, column=2, padx=10, pady=6)

        to_btn4 = Button(h8, width=12,height=5,text=("EXIT"),bg='yellow', font=("arial 15")).grid(row=0, column=3, padx=10, pady=6)








#->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->


    def toggle_geom(self, event):
        geom = self.root.winfo_geometry()
        print(geom, self._geom)
        self.root.geometry(self._geom)
        self._geom = geom


root=Tk()
x=call_bill(root)
root.mainloop()


#--------------------------------------------------------------------------------------------------------------------------------------------------------





