from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import random
import time
from PIL import Image,ImageTk
import requests
import mysql.connector

#---------------------------------------------Function_for_login---------------------------------------------------------

def login():
    user = e_username.get()
    pss = e_password.get()
    mydb = mysql.connector.connect(
        host= "localhost",
        username = "root",
        password = "sahil2000",
        database='Omni food'
    )
    mycursor = mydb.cursor()

    sql = "SELECT * FROM login WHERE username = %s and password = %s"
    mycursor.execute(sql,[(user),(pss)])
    myresult = mycursor.fetchall()
    if myresult:
        messagebox.showinfo("Login Successfull","Successfully Login")
        top.destroy()
        main()
        return True
    else:
        messagebox.showerror("Error","Wrong Username or Password")
        return False

#----------------------------------------------Login_GUI-----------------------------------------------------------
top = Tk()
top.geometry("400x500")
top.resizable(0,0)
top.config(bg='DarkOrange2')

image = Image.open("user.png")
resize_img = image.resize((120,120))
img = ImageTk.PhotoImage(resize_img)
img_label = Label(top,image = img,bg='DarkOrange2')
img_label.pack(side = TOP,pady=25)

username = Label(top,text='Username',font=('arial',18,'bold'),bg='DarkOrange2')
username.pack(pady=5)
e_username = Entry(top,font=('arial',16,'bold'))
e_username.pack()

password = Label(top,text='Password',font=('arial',18,'bold'),bg='DarkOrange2')
password.pack(pady=5)
e_password = Entry(top,show='*',font=('arial',16,'bold'))
e_password.pack()

login_btn = Button(top,text='Login',font= ('arial',16,'bold'),bd=3,relief=RIDGE,command=login)
login_btn.pack(pady = 30)



#-----------------------------------------main--------------------------------------------------
def main():
    global var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21 \
        , var22,var23,var24,var25,var26,var27,e_vegburger,e_cheeseburger,e_noodles,e_manchurian,e_stmomos,e_frimomos,e_friedrice,e_chillypotato,e_springroll \
        ,e_lassi,e_coffee,e_faluda,e_shikanji,e_roohafza,e_jaljeera,e_masalatea,e_badammilk,e_colddrinks \
        ,e_oreo,e_apple,e_kitkat,e_vanilla,e_banana,e_brownie,e_pineapple,e_chocolate,e_blackforest \
        ,costoffoodvar,costofdrinksvar,costofcakesvar,subtotalvar,servicetaxvar,totalcostvar,operator,insert_text

    root = Tk()
    root.geometry("1337x690+0+0")
    root.resizable(0, 0)
    root.title("Restaurant Management System")
    root.config(bg='black')

    # ---------------------------------------Variables-----------------------------------------------
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var18 = IntVar()
    var19 = IntVar()
    var20 = IntVar()
    var21 = IntVar()
    var22 = IntVar()
    var23 = IntVar()
    var24 = IntVar()
    var25 = IntVar()
    var26 = IntVar()
    var27 = IntVar()

    e_vegburger = StringVar()
    e_cheeseburger = StringVar()
    e_noodles = StringVar()
    e_manchurian = StringVar()
    e_stmomos = StringVar()
    e_frimomos = StringVar()
    e_friedrice = StringVar()
    e_chillypotato = StringVar()
    e_springroll = StringVar()

    e_lassi = StringVar()
    e_coffee = StringVar()
    e_faluda = StringVar()
    e_shikanji = StringVar()
    e_roohafza = StringVar()
    e_jaljeera = StringVar()
    e_masalatea = StringVar()
    e_badammilk = StringVar()
    e_colddrinks = StringVar()

    e_oreo = StringVar()
    e_apple = StringVar()
    e_kitkat = StringVar()
    e_vanilla = StringVar()
    e_banana = StringVar()
    e_brownie = StringVar()
    e_pineapple = StringVar()
    e_chocolate = StringVar()
    e_blackforest = StringVar()

    costoffoodvar = StringVar()
    costofdrinksvar = StringVar()
    costofcakesvar = StringVar()
    subtotalvar = StringVar()
    servicetaxvar = StringVar()
    totalcostvar = StringVar()

    e_vegburger.set('0')
    e_cheeseburger.set('0')
    e_noodles.set('0')
    e_manchurian.set('0')
    e_stmomos.set('0')
    e_frimomos.set('0')
    e_friedrice.set('0')
    e_chillypotato.set('0')
    e_springroll.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_shikanji.set('0')
    e_roohafza.set('0')
    e_jaljeera.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_colddrinks.set('0')

    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    operator = ''  # for_calculator
    insert_text = StringVar()

    # -----------------------------Functions--------------------------------
    def vegburger():
        if var1.get() == 1:
            textvegburger.config(state=NORMAL)
            textvegburger.delete(0, END)
            textvegburger.focus()
        else:
            textvegburger.config(state=DISABLED)
            e_vegburger.set(0)

    def cheeseburger():
        if var2.get() == 1:
            textcheeseburger.config(state=NORMAL)
            textcheeseburger.delete(0, END)
            textcheeseburger.focus()
        else:
            textcheeseburger.config(state=DISABLED)
            e_cheeseburger.set(0)

    def stmomos():
        if var3.get() == 1:
            textstmomos.config(state=NORMAL)
            textstmomos.delete(0, END)
            textstmomos.focus()
        else:
            textstmomos.config(state=DISABLED)
            e_stmomos.set(0)

    def noodles():
        if var4.get() == 1:
            textnoodles.config(state=NORMAL)
            textnoodles.delete(0, END)
            textnoodles.focus()
        else:
            textnoodles.config(state=DISABLED)
            e_noodles.set(0)

    def friedrice():
        if var5.get() == 1:
            textfriedrice.config(state=NORMAL)
            textfriedrice.delete(0, END)
            textfriedrice.focus()
        else:
            textfriedrice.config(state=DISABLED)
            e_friedrice.set(0)

    def manchurian():
        if var6.get() == 1:
            textmanchurian.config(state=NORMAL)
            textmanchurian.delete(0, END)
            textmanchurian.focus()
        else:
            textmanchurian.config(state=DISABLED)
            e_manchurian.set(0)

    def frimomos():
        if var7.get() == 1:
            textfrimomos.config(state=NORMAL)
            textfrimomos.delete(0, END)
            textfrimomos.focus()
        else:
            textfrimomos.config(state=DISABLED)
            e_frimomos.set(0)

    def chillypotato():
        if var8.get() == 1:
            textchillypotato.config(state=NORMAL)
            textchillypotato.delete(0, END)
            textchillypotato.focus()
        else:
            textchillypotato.config(state=DISABLED)
            e_chillypotato.set(0)

    def springroll():
        if var9.get() == 1:
            textspringroll.config(state=NORMAL)
            textspringroll.delete(0, END)
            textspringroll.focus()
        else:
            textspringroll.config(state=DISABLED)
            e_springroll.set(0)

    def lassi():
        if var10.get() == 1:
            textlassi.config(state=NORMAL)
            textlassi.delete(0, END)
            textlassi.focus()
        else:
            textlassi.config(state=DISABLED)
            e_lassi.set(0)

    def coffee():
        if var11.get() == 1:
            textcoffee.config(state=NORMAL)
            textcoffee.delete(0, END)
            textcoffee.focus()
        else:
            textcoffee.config(state=DISABLED)
            e_coffee.set(0)

    def faluda():
        if var12.get() == 1:
            textfaluda.config(state=NORMAL)
            textfaluda.delete(0, END)
            textfaluda.focus()
        else:
            textfaluda.config(state=DISABLED)
            e_faluda.set(0)

    def shikanji():
        if var13.get() == 1:
            textshikanji.config(state=NORMAL)
            textshikanji.delete(0, END)
            textshikanji.focus()
        else:
            textshikanji.config(state=DISABLED)
            e_shikanji.set(0)

    def jaljeera():
        if var14.get() == 1:
            textjaljeera.config(state=NORMAL)
            textjaljeera.delete(0, END)
            textjaljeera.focus()
        else:
            textjaljeera.config(state=DISABLED)
            e_jaljeera.set(0)

    def roohafza():
        if var15.get() == 1:
            textroohafza.config(state=NORMAL)
            textroohafza.delete(0, END)
            textroohafza.focus()
        else:
            textroohafza.config(state=DISABLED)
            e_roohafza.set(0)

    def masalatea():
        if var16.get() == 1:
            textmasalatea.config(state=NORMAL)
            textmasalatea.delete(0, END)
            textmasalatea.focus()
        else:
            textmasalatea.config(state=DISABLED)
            e_masalatea.set(0)

    def badaammilk():
        if var17.get() == 1:
            textbadaammilk.config(state=NORMAL)
            textbadaammilk.delete(0, END)
            textbadaammilk.focus()
        else:
            textbadaammilk.config(state=DISABLED)
            e_badammilk.set(0)

    def colddrinks():
        if var18.get() == 1:
            textcolddrinks.config(state=NORMAL)
            textcolddrinks.delete(0, END)
            textcolddrinks.focus()
        else:
            textcolddrinks.config(state=DISABLED)
            e_colddrinks.set(0)

    def oreo():
        if var19.get() == 1:
            textoreo.config(state=NORMAL)
            textoreo.delete(0, END)
            textoreo.focus()
        else:
            textoreo.config(state=DISABLED)
            e_oreo.set(0)

    def apple():
        if var20.get() == 1:
            textapple.config(state=NORMAL)
            textapple.delete(0, END)
            textapple.focus()
        else:
            textapple.config(state=DISABLED)
            e_apple.set(0)

    def kitkat():
        if var21.get() == 1:
            textkitkat.config(state=NORMAL)
            textkitkat.delete(0, END)
            textkitkat.focus()
        else:
            textkitkat.config(state=DISABLED)
            e_kitkat.set(0)

    def vanilla():
        if var22.get() == 1:
            textvanilla.config(state=NORMAL)
            textvanilla.delete(0, END)
            textvanilla.focus()
        else:
            textvanilla.config(state=DISABLED)
            e_vanilla.set(0)

    def banana():
        if var23.get() == 1:
            textbanana.config(state=NORMAL)
            textbanana.delete(0, END)
            textbanana.focus()
        else:
            textbanana.config(state=DISABLED)
            e_banana.set(0)

    def brownie():
        if var24.get() == 1:
            textbrownie.config(state=NORMAL)
            textbrownie.delete(0, END)
            textbrownie.focus()
        else:
            textbrownie.config(state=DISABLED)
            e_brownie.set(0)

    def pineapple():
        if var25.get() == 1:
            textpineapple.config(state=NORMAL)
            textpineapple.delete(0, END)
            textpineapple.focus()
        else:
            textpineapple.config(state=DISABLED)
            e_pineapple.set(0)

    def chocolate():
        if var26.get() == 1:
            textchocolate.config(state=NORMAL)
            textchocolate.delete(0, END)
            textchocolate.focus()
        else:
            textchocolate.config(state=DISABLED)
            e_chocolate.set(0)

    def blackforest():
        if var27.get() == 1:
            textblackforest.config(state=NORMAL)
            textblackforest.delete(0, END)
            textblackforest.focus()
        else:
            textblackforest.config(state=DISABLED)
            e_blackforest.set(0)

    # ------------------------------function_for_totalcost-----------------------------------------
    def total_cost():
        global priceoffood, priceofdrinks, priceofcakes, subtotalofitems, totalcost

        if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 \
                or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 \
                or var14.get() != 0 or var15.get() != 0 or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 \
                or var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or var26.get() != 0 or var27.get() != 0:

            item1 = int(e_vegburger.get())
            item2 = int(e_cheeseburger.get())
            item3 = int(e_stmomos.get())
            item4 = int(e_noodles.get())
            item5 = int(e_friedrice.get())
            item6 = int(e_manchurian.get())
            item7 = int(e_frimomos.get())
            item8 = int(e_chillypotato.get())
            item9 = int(e_springroll.get())

            item10 = int(e_lassi.get())
            item11 = int(e_coffee.get())
            item12 = int(e_faluda.get())
            item13 = int(e_shikanji.get())
            item14 = int(e_jaljeera.get())
            item15 = int(e_roohafza.get())
            item16 = int(e_masalatea.get())
            item17 = int(e_badammilk.get())
            item18 = int(e_colddrinks.get())

            item19 = int(e_oreo.get())
            item20 = int(e_apple.get())
            item21 = int(e_kitkat.get())
            item22 = int(e_vanilla.get())
            item23 = int(e_banana.get())
            item24 = int(e_brownie.get())
            item25 = int(e_pineapple.get())
            item26 = int(e_chocolate.get())
            item27 = int(e_blackforest.get())

            priceoffood = (item1 * 30) + (item2 * 50) + (item3 * 60) + (item4 * 60) + (item5 * 70) + (item6 * 60) + (
                        item7 * 80) \
                          + (item8 * 70) + (item9 * 60)

            priceofdrinks = (item10 * 50) + (item11 * 40) + (item12 * 80) + (item13 * 30) + (item14 * 40) + (
                        item15 * 60) + (item16 * 20) \
                            + (item17 * 50) + (item18 * 80)

            priceofcakes = (item19 * 400) + (item20 * 300) + (item21 * 500) + (item22 * 550) + (item23 * 450) + (
                        item24 * 800) + (item25 * 620) \
                           + (item26 * 700) + (item27 * 550)

            costoffoodvar.set('Rs.' + str(priceoffood))
            costofdrinksvar.set('Rs.' + str(priceofdrinks))
            costofcakesvar.set('Rs.' + str(priceofcakes))

            subtotalofitems = priceoffood + priceofdrinks + priceofcakes
            subtotalvar.set('Rs.' + str(subtotalofitems))

            servicetaxvar.set('Rs. 50')

            totalcost = subtotalofitems + 50
            totalcostvar.set('Rs.' + str(totalcost))

        else:
            messagebox.showerror('Error', 'No item is selected')

    # ------------------------------fuction_for_reciept-------------------------------------------
    def reciept():
        global billnumber, date

        if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
            textreciept.delete(1.0, END)
            x = random.randint(100, 10000)
            billnumber = 'BILL' + str(x)
            date = time.strftime('%d/%m/%y')
            textreciept.insert(END, 'Reciept Ref:\t\t' + billnumber + '\t\t' + date + '\n')
            textreciept.insert(END, '***************************************************************\n')
            textreciept.insert(END, 'Items:\t\t Cost of Items(Rs.)\n')
            textreciept.insert(END, '***************************************************************\n')
            if e_vegburger.get() != '0':
                textreciept.insert(END, f'Veg Burger\t\t\t{int(e_vegburger.get()) * 30}\n\n')
            if e_cheeseburger.get() != '0':
                textreciept.insert(END, f'Cheese Burger\t\t\t{int(e_cheeseburger.get()) * 50}\n\n')
            if e_stmomos.get() != '0':
                textreciept.insert(END, f'Steam Momos\t\t\t{int(e_stmomos.get()) * 60}\n\n')
            if e_noodles.get() != '0':
                textreciept.insert(END, f'Noodles\t\t\t{int(e_noodles.get()) * 60}\n\n')
            if e_friedrice.get() != '0':
                textreciept.insert(END, f'Fried Rice\t\t\t{int(e_friedrice.get()) * 80}\n\n')
            if e_manchurian.get() != '0':
                textreciept.insert(END, f'Manchurian\t\t\t{int(e_manchurian.get()) * 60}\n\n')
            if e_frimomos.get() != '0':
                textreciept.insert(END, f'Fried Momos\t\t\t{int(e_frimomos.get()) * 80}\n\n')
            if e_chillypotato.get() != '0':
                textreciept.insert(END, f'Chilly Potato\t\t\t{int(e_chillypotato.get()) * 70}\n\n')
            if e_springroll.get() != '0':
                textreciept.insert(END, f'Spring Roll\t\t\t{int(e_springroll.get()) * 60}\n\n')

            if e_lassi.get() != '0':
                textreciept.insert(END, f'Lassi\t\t\t{int(e_lassi.get()) * 50}\n\n')
            if e_coffee.get() != '0':
                textreciept.insert(END, f'Coffee\t\t\t{int(e_coffee.get()) * 40}\n\n')
            if e_faluda.get() != '0':
                textreciept.insert(END, f'Faluda\t\t\t{int(e_faluda.get()) * 80}\n\n')
            if e_shikanji.get() != '0':
                textreciept.insert(END, f'Shikanji\t\t\t{int(e_shikanji.get()) * 30}\n\n')
            if e_jaljeera.get() != '0':
                textreciept.insert(END, f'Jaljeera\t\t\t{int(e_jaljeera.get()) * 40}\n\n')
            if e_roohafza.get() != '0':
                textreciept.insert(END, f'Rooh Afza\t\t\t{int(e_roohafza.get()) * 60}\n\n')
            if e_masalatea.get() != '0':
                textreciept.insert(END, f'Masala Tea\t\t\t{int(e_masalatea.get()) * 20}\n\n')
            if e_badammilk.get() != '0':
                textreciept.insert(END, f'Badaam Milk\t\t\t{int(e_badammilk.get()) * 50}\n\n')
            if e_colddrinks.get() != '0':
                textreciept.insert(END, f'Cold Drinks\t\t\t{int(e_colddrinks.get()) * 80}\n\n')

            if e_oreo.get() != '0':
                textreciept.insert(END, f'Oreo\t\t\t{int(e_oreo.get()) * 400}\n\n')
            if e_apple.get() != '0':
                textreciept.insert(END, f'Apple\t\t\t{int(e_apple.get()) * 300}\n\n')
            if e_kitkat.get() != '0':
                textreciept.insert(END, f'Kitkat\t\t\t{int(e_kitkat.get()) * 500}\n\n')
            if e_vanilla.get() != '0':
                textreciept.insert(END, f'Vanilla\t\t\t{int(e_vanilla.get()) * 550}\n\n')
            if e_banana.get() != '0':
                textreciept.insert(END, f'Banana\t\t\t{int(e_banana.get()) * 450}\n\n')
            if e_brownie.get() != '0':
                textreciept.insert(END, f'Brownie\t\t\t{int(e_brownie.get()) * 800}\n\n')
            if e_pineapple.get() != '0':
                textreciept.insert(END, f'Pineapple\t\t\t{int(e_pineapple.get()) * 620}\n\n')
            if e_chocolate.get() != '0':
                textreciept.insert(END, f'Chocolate\t\t\t{int(e_chocolate.get()) * 700}\n\n')
            if e_blackforest.get() != '0':
                textreciept.insert(END, f'Black Forest\t\t\t{int(e_blackforest.get()) * 550}\n\n')

            textreciept.insert(END, '***************************************************************\n')
            if costoffoodvar.get() != 'Rs.0':
                textreciept.insert(END, f'Cost of Food\t\t\tRs.{priceoffood}\n\n')
            if costofdrinksvar.get() != 'Rs.0':
                textreciept.insert(END, f'Cost of Drinks\t\t\tRs.{priceofdrinks}\n\n')
            if costofcakesvar.get() != 'Rs.0':
                textreciept.insert(END, f'Cost of Cakes\t\t\tRs.{priceofcakes}\n\n')

            textreciept.insert(END, '***************************************************************\n')
            textreciept.insert(END, f'Subtotal of items\t\t\tRs.{subtotalofitems}\n\n')
            textreciept.insert(END, f'Service Tax\t\t\tRs.50\n\n')
            textreciept.insert(END, f'Total Cost\t\t\tRs.{totalcost}\n\n')

        else:
            messagebox.showerror('Error', 'No item is selected')

    # --------------------------------fuction_for_savebtn-----------------------------------------
    def save():
        if textreciept.get(1.0, END) == '\n':
            pass
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
            if url == None:
                pass
            else:
                billdata = textreciept.get(1.0, END)
                url.write(billdata)
                url.close()
                messagebox.showinfo('Information', 'Your Bill is saved Successfully..!!')

    # ----------------------------function_for_send_btn---------------------------------------------------
    def send():
        if textreciept.get(1.0, END) == '\n':
            pass
        else:
            def sendmessage():
                message = f'Bill No. {billnumber}\nDate: {date}\nYour Bill :\nCost of Food : Rs.{priceoffood}\n' \
                          f'Cost of Drinks : Rs.{priceofdrinks}\nCost of Cake : Rs.{priceofcakes}\nTotal Cost : Rs.{totalcost}\n(Including Service Tax)'
                number = numfield.get()
                auth = 'LeDRTxYn3lrMKCkG6AHOBad19N0bo7qFJQ4pfP85ShUciwEWvyjDsXvkCFmJezQaVOpwL02lP6SbgG7i'
                url = 'https://www.fast2sms.com/dev/bulkV2'

                params = {
                    'authorization': auth,
                    'message': message,
                    'numbers': number,
                    'sender_id': 'FSTSMS',
                    'route': 'p',
                    'language': 'english'
                }
                response = requests.get(url=url, params=params)
                dic = response.json()
                result = dic.get('return')
                if result == True:
                    messagebox.showinfo('Send Successfully', 'Message send successfully')
                else:
                    messagebox.showerror('Error', 'Something went wrong')

            root2 = Toplevel()

            root2.title("Send Bill")
            root2.config(bg='DarkOrange2')
            root2.geometry("485x620+50+50")

            image = Image.open("message.png")
            resize_image = image.resize((120, 120))
            logoimage = ImageTk.PhotoImage(resize_image)
            label = Label(root2, image=logoimage, bg='DarkOrange2')
            label.pack(pady=5)

            numlabel = Label(root2, text='Mobile Number', font=('arial', 18, 'underline', 'bold'), bg='DarkOrange2',
                             fg='black')
            numlabel.pack(pady=5)
            numfield = Entry(root2, font=('arial', 22, 'bold'), bd=3, relief=RIDGE, width=24)
            numfield.pack(pady=5)

            billabel = Label(root2, text='Bill Details', font=('arial', 18, 'underline', 'bold'), bg='DarkOrange2',
                             fg='black')
            billabel.pack(pady=5)
            billfield = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
            billfield.pack(pady=5)
            billfield.insert(END, 'Reciept Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

            billfield.insert(END, '***************************************************************\n')
            if costoffoodvar.get() != 'Rs.0':
                billfield.insert(END, f'Cost of Food\t\t\tRs.{priceoffood}\n')
            if costofdrinksvar.get() != 'Rs.0':
                billfield.insert(END, f'Cost of Drinks\t\t\tRs.{priceofdrinks}\n')
            if costofcakesvar.get() != 'Rs.0':
                billfield.insert(END, f'Cost of Cakes\t\t\tRs.{priceofcakes}\n')

            billfield.insert(END, '***************************************************************\n')
            billfield.insert(END, f'Subtotal of items\t\t\tRs.{subtotalofitems}\n')
            billfield.insert(END, f'Service Tax\t\t\tRs.50\n')
            billfield.insert(END, f'Total Cost\t\t\tRs.{totalcost}\n')

            sendbtn = Button(root2, text='Send', font=('arial', 19, 'bold'), bg='white', fg='DarkOrange2', bd=7,
                             relief=GROOVE, command=sendmessage)
            sendbtn.pack(pady=5)

            root2.mainloop()

    # --------------------------------fuction_for_reset------------------------------

    def reset():
        textreciept.delete(1.0, END)
        e_vegburger.set('0')
        e_cheeseburger.set('0')
        e_noodles.set('0')
        e_manchurian.set('0')
        e_stmomos.set('0')
        e_frimomos.set('0')
        e_friedrice.set('0')
        e_chillypotato.set('0')
        e_springroll.set('0')

        e_lassi.set('0')
        e_coffee.set('0')
        e_faluda.set('0')
        e_shikanji.set('0')
        e_roohafza.set('0')
        e_jaljeera.set('0')
        e_masalatea.set('0')
        e_badammilk.set('0')
        e_colddrinks.set('0')

        e_oreo.set('0')
        e_apple.set('0')
        e_kitkat.set('0')
        e_vanilla.set('0')
        e_banana.set('0')
        e_brownie.set('0')
        e_pineapple.set('0')
        e_chocolate.set('0')
        e_blackforest.set('0')

        textvegburger.config(state=DISABLED)
        textcheeseburger.config(state=DISABLED)
        textstmomos.config(state=DISABLED)
        textnoodles.config(state=DISABLED)
        textfriedrice.config(state=DISABLED)
        textmanchurian.config(state=DISABLED)
        textfrimomos.config(state=DISABLED)
        textchillypotato.config(state=DISABLED)
        textspringroll.config(state=DISABLED)

        textlassi.config(state=DISABLED)
        textcoffee.config(state=DISABLED)
        textfaluda.config(state=DISABLED)
        textshikanji.config(state=DISABLED)
        textjaljeera.config(state=DISABLED)
        textroohafza.config(state=DISABLED)
        textmasalatea.config(state=DISABLED)
        textbadaammilk.config(state=DISABLED)
        textcolddrinks.config(state=DISABLED)

        textoreo.config(state=DISABLED)
        textapple.config(state=DISABLED)
        textkitkat.config(state=DISABLED)
        textvanilla.config(state=DISABLED)
        textbanana.config(state=DISABLED)
        textbrownie.config(state=DISABLED)
        textpineapple.config(state=DISABLED)
        textchocolate.config(state=DISABLED)
        textblackforest.config(state=DISABLED)

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set(0)
        var23.set(0)
        var24.set(0)
        var25.set(0)
        var26.set(0)
        var27.set(0)

        costoffoodvar.set('')
        costofdrinksvar.set('')
        costofcakesvar.set('')
        subtotalvar.set('')
        servicetaxvar.set('')
        totalcostvar.set('')

    # --------------------------------FRAME-------------------------------
    top = Frame(root, bd=10, relief=RIDGE, bg='DarkOrange2')
    top.pack(side=TOP)

    label_title = Label(top, text='~~~~~~ Omni Food ~~~~~~', font=('arial', 30, 'bold'), fg='DarkOrange2', bg='black',
                        width=54, bd=9)
    label_title.grid(row=0, column=0)

    menuframe = Frame(root, bd=10, relief=RIDGE, bg='DarkOrange2')
    menuframe.pack(side=LEFT)

    costframe = Frame(menuframe, bd=4, relief=RIDGE, bg='Black', pady=8)
    costframe.pack(side=BOTTOM)

    foodframe = LabelFrame(menuframe, text='Food', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='DarkOrange2')
    foodframe.pack(side=LEFT)

    drinksframe = LabelFrame(menuframe, text='Drinks', font=('arial', 19, 'bold'), bd=10, relief=RIDGE,fg='DarkOrange2')
    drinksframe.pack(side=LEFT)

    cakesframe = LabelFrame(menuframe, text='Cakes', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='DarkOrange2' )
    cakesframe.pack(side=LEFT)

    rightframe = Frame(root, bd=10, relief=RIDGE, bg='DarkOrange2')
    rightframe.pack(side=RIGHT)

    calculatorframe = Frame(rightframe, bd=1, relief=RIDGE, bg='Black')
    calculatorframe.pack()

    recieptframe = Frame(rightframe, bd=4, relief=RIDGE, bg='Black')
    recieptframe.pack()

    buttonframe = Frame(rightframe, bd=3, relief=RIDGE, bg='Black')
    buttonframe.pack()

    # -------------------FOOD---------------------------------
    vegburger = Checkbutton(foodframe, text='Veg Burger', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1,
                       command=vegburger)
    vegburger.grid(row=0, column=0, sticky=W)

    cheeseburger = Checkbutton(foodframe, text='Cheese Burger', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2,
                       command=cheeseburger)
    cheeseburger.grid(row=1, column=0, sticky=W)

    stmomos = Checkbutton(foodframe, text='Steam Momos', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3,
                       command=stmomos)
    stmomos.grid(row=2, column=0, sticky=W)

    noodles = Checkbutton(foodframe, text='Noodles', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4,
                        command=noodles)
    noodles.grid(row=3, column=0, sticky=W)

    friedrice = Checkbutton(foodframe, text='Fried Rice', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5,
                        command=friedrice)
    friedrice.grid(row=4, column=0, sticky=W)

    manchurian = Checkbutton(foodframe, text='Manchurian', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6,
                         command=manchurian)
    manchurian.grid(row=5, column=0, sticky=W)

    frimomos = Checkbutton(foodframe, text='Fried Momos', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7,
                         command=frimomos)
    frimomos.grid(row=6, column=0, sticky=W)

    chillypotato = Checkbutton(foodframe, text='Chilly Potato', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8,
                         command=chillypotato)
    chillypotato.grid(row=7, column=0, sticky=W)

    springroll = Checkbutton(foodframe, text='Spring Roll', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9,
                          command=springroll)
    springroll.grid(row=8, column=0, sticky=W)

    # ---------------------------Emtries_for_food-----------------

    textvegburger = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_vegburger)
    textvegburger.grid(row=0, column=1)

    textcheeseburger = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_cheeseburger)
    textcheeseburger.grid(row=1, column=1)

    textstmomos = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_stmomos)
    textstmomos.grid(row=2, column=1)

    textnoodles = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_noodles)
    textnoodles.grid(row=3, column=1)

    textfriedrice = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_friedrice)
    textfriedrice.grid(row=4, column=1)

    textmanchurian = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_manchurian)
    textmanchurian.grid(row=5, column=1)

    textfrimomos = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_frimomos)
    textfrimomos.grid(row=6, column=1)

    textchillypotato = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_chillypotato)
    textchillypotato.grid(row=7, column=1)

    textspringroll = Entry(foodframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_springroll)
    textspringroll.grid(row=8, column=1)

    # -----------------------------------Drinks------------------------------
    lassi = Checkbutton(drinksframe, text='Lassi', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var10,
                        command=lassi)
    lassi.grid(row=0, column=0, sticky=W)

    coffee = Checkbutton(drinksframe, text='Coffee', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var11,
                         command=coffee)
    coffee.grid(row=1, column=0, sticky=W)

    faluda = Checkbutton(drinksframe, text='Faluda', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var12,
                         command=faluda)
    faluda.grid(row=2, column=0, sticky=W)

    shikanji = Checkbutton(drinksframe, text='Shikanji', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                           variable=var13, command=shikanji)
    shikanji.grid(row=3, column=0, sticky=W)

    jaljeera = Checkbutton(drinksframe, text='Jaljeera', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                           variable=var14, command=jaljeera)
    jaljeera.grid(row=4, column=0, sticky=W)

    roohafza = Checkbutton(drinksframe, text='Roohafza', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                           variable=var15, command=roohafza)
    roohafza.grid(row=5, column=0, sticky=W)

    masalatea = Checkbutton(drinksframe, text='Masala Tea', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var16, command=masalatea)
    masalatea.grid(row=6, column=0, sticky=W)

    badaammilk = Checkbutton(drinksframe, text='Badaam Milk', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                             variable=var17, command=badaammilk)
    badaammilk.grid(row=7, column=0, sticky=W)

    colddrinks = Checkbutton(drinksframe, text='Cold Drinks', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                             variable=var18, command=colddrinks)
    colddrinks.grid(row=8, column=0, sticky=W)

    # ---------------------------Emtries_for_drinks-----------------

    textlassi = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_lassi)
    textlassi.grid(row=0, column=1)

    textcoffee = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_coffee)
    textcoffee.grid(row=1, column=1)

    textfaluda = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_faluda)
    textfaluda.grid(row=2, column=1)

    textshikanji = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_shikanji)
    textshikanji.grid(row=3, column=1)

    textjaljeera = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_jaljeera)
    textjaljeera.grid(row=4, column=1)

    textroohafza = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_roohafza)
    textroohafza.grid(row=5, column=1)

    textmasalatea = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                          textvariabl=e_masalatea)
    textmasalatea.grid(row=6, column=1)

    textbadaammilk = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                           textvariabl=e_badammilk)
    textbadaammilk.grid(row=7, column=1)

    textcolddrinks = Entry(drinksframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                           textvariabl=e_colddrinks)
    textcolddrinks.grid(row=8, column=1)

    # -------------------Cakes---------------------------------
    oreo = Checkbutton(cakesframe, text='Oreo', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var19,
                       command=oreo)
    oreo.grid(row=0, column=0, sticky=W)

    apple = Checkbutton(cakesframe, text='Apple', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var20,
                        command=apple)
    apple.grid(row=1, column=0, sticky=W)

    kitkat = Checkbutton(cakesframe, text='Kitkat', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var21,
                         command=kitkat)
    kitkat.grid(row=2, column=0, sticky=W)

    vanilla = Checkbutton(cakesframe, text='Vanilla', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var22,
                          command=vanilla)
    vanilla.grid(row=3, column=0, sticky=W)

    banana = Checkbutton(cakesframe, text='Banana', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var23,
                         command=banana)
    banana.grid(row=4, column=0, sticky=W)

    brownie = Checkbutton(cakesframe, text='Brownie', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var24,
                          command=brownie)
    brownie.grid(row=5, column=0, sticky=W)

    pineapple = Checkbutton(cakesframe, text='Pineapple', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var25, command=pineapple)
    pineapple.grid(row=6, column=0, sticky=W)

    chocolate = Checkbutton(cakesframe, text='Chocolate', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                            variable=var26, command=chocolate)
    chocolate.grid(row=7, column=0, sticky=W)

    blackforest = Checkbutton(cakesframe, text='Black Forest', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                              variable=var27, command=blackforest)
    blackforest.grid(row=8, column=0, sticky=W)

    # ---------------------------Emtries_for_food-----------------

    textoreo = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_oreo)
    textoreo.grid(row=0, column=1)

    textapple = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_apple)
    textapple.grid(row=1, column=1)

    textkitkat = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_kitkat)
    textkitkat.grid(row=2, column=1)

    textvanilla = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_vanilla)
    textvanilla.grid(row=3, column=1)

    textbanana = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_banana)
    textbanana.grid(row=4, column=1)

    textbrownie = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariabl=e_brownie)
    textbrownie.grid(row=5, column=1)

    textpineapple = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                          textvariabl=e_pineapple)
    textpineapple.grid(row=6, column=1)

    textchocolate = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                          textvariabl=e_chocolate)
    textchocolate.grid(row=7, column=1)

    textblackforest = Entry(cakesframe, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                            textvariabl=e_blackforest)
    textblackforest.grid(row=8, column=1)

    # ---------------------------------Costlabels________________________
    labelcostoffood = Label(costframe, text=' Cost of Food', font=('arial', 16, 'bold'), bg='black', fg='DarkOrange2')
    labelcostoffood.grid(row=0, column=0)

    textcostoffood = Entry(costframe, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                           textvariable=costoffoodvar)
    textcostoffood.grid(row=0, column=1, padx=62)

    labelcostofdrinks = Label(costframe, text=' Cost of Drinks', font=('arial', 16, 'bold'), bg='black',
                              fg='DarkOrange2')
    labelcostofdrinks.grid(row=1, column=0)

    textcostofdrinks = Entry(costframe, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                             textvariable=costofdrinksvar)
    textcostofdrinks.grid(row=1, column=1, padx=62)

    labelcostofcakes = Label(costframe, text=' Cost of Cakes', font=('arial', 16, 'bold'), bg='black', fg='DarkOrange2')
    labelcostofcakes.grid(row=2, column=0)

    textcostofcakes = Entry(costframe, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                            textvariable=costofcakesvar)
    textcostofcakes.grid(row=2, column=1, padx=62)

    labelsubtotal = Label(costframe, text='Sub Total', font=('arial', 16, 'bold'), bg='black', fg='DarkOrange2')
    labelsubtotal.grid(row=0, column=2)

    textsubtotal = Entry(costframe, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                         textvariable=subtotalvar)
    textsubtotal.grid(row=0, column=3, padx=62)

    labelservicetax = Label(costframe, text='Service Tax', font=('arial', 16, 'bold'), bg='black', fg='DarkOrange2')
    labelservicetax.grid(row=1, column=2)

    textservicetax = Entry(costframe, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                           textvariable=servicetaxvar)
    textservicetax.grid(row=1, column=3, padx=62)

    labeltotalcost = Label(costframe, text='Total Cost', font=('arial', 16, 'bold'), bg='black', fg='DarkOrange2')
    labeltotalcost.grid(row=2, column=2)

    texttotalcost = Entry(costframe, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                          textvariable=totalcostvar)
    texttotalcost.grid(row=2, column=3, padx=62)

    # ----------------------Buttons------------------
    buttontotal = Button(buttonframe, text='Total', font=('arial', 14, 'bold'), fg='DarkOrange2', bg='black', bd=3,
                         padx=4, command=total_cost)
    buttontotal.grid(row=0, column=0)

    buttonreciept = Button(buttonframe, text='Reciept', font=('arial', 14, 'bold'), fg='DarkOrange2', bg='black', bd=3,
                           padx=4, command=reciept)
    buttonreciept.grid(row=0, column=1)

    buttonsave = Button(buttonframe, text='Save', font=('arial', 14, 'bold'), fg='DarkOrange2', bg='black', bd=3,
                        padx=4, command=save)
    buttonsave.grid(row=0, column=2)

    buttonsend = Button(buttonframe, text='Send', font=('arial', 14, 'bold'), fg='DarkOrange2', bg='black', bd=3,
                        padx=4, command=send)
    buttonsend.grid(row=0, column=3)

    buttonreset = Button(buttonframe, text='Reset', font=('arial', 14, 'bold'), fg='DarkOrange2', bg='black', bd=3,
                         padx=4, command=reset)
    buttonreset.grid(row=0, column=4)

    # ----------------------------TextArea-----------------
    textreciept = Text(recieptframe, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
    textreciept.grid(row=0, column=0)

    # -----------------------Calculator---------------------

    def btn_click(number):
        global operator
        operator = operator + number
        insert_text.set(operator)

    def btn_ans():
        global operator
        result = str(eval(operator))
        insert_text.set(result)

    def btn_clear():
        global operator
        operator = ''
        insert_text.set('')


    calculatorfield = Entry(calculatorframe, font=('arial', 27, 'bold'), width=19, bd=4, textvariable=insert_text,
                            justify=LEFT)
    calculatorfield.grid(row=0, column=0, columnspan=4)

    btn7 = Button(calculatorframe, text='7', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("7"))
    btn7.grid(row=1, column=0)

    btn8 = Button(calculatorframe, text='8', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("8"))
    btn8.grid(row=1, column=1)

    btn9 = Button(calculatorframe, text='9', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("9"))
    btn9.grid(row=1, column=2)

    btnplus = Button(calculatorframe, text='+', font=('arial', 16, 'bold'), fg='White', bg='DarkOrange2', bd=6, width=6,
                     command=lambda: btn_click("+"))
    btnplus.grid(row=1, column=3)

    btn4 = Button(calculatorframe, text='4', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("4"))
    btn4.grid(row=2, column=0)

    btn5 = Button(calculatorframe, text='5', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("5"))
    btn5.grid(row=2, column=1)

    btn6 = Button(calculatorframe, text='6', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("6"))
    btn6.grid(row=2, column=2)

    btnminus = Button(calculatorframe, text='-', font=('arial', 16, 'bold'), fg='White', bg='DarkOrange2', bd=6,
                      width=6, command=lambda: btn_click("-"))
    btnminus.grid(row=2, column=3)

    btn1 = Button(calculatorframe, text='1', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("1"))
    btn1.grid(row=3, column=0)

    btn2 = Button(calculatorframe, text='2', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("2"))
    btn2.grid(row=3, column=1)

    btn3 = Button(calculatorframe, text='3', font=('arial', 16, 'bold'), bg='#DCDCDC', fg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("3"))
    btn3.grid(row=3, column=2)

    btnmultiply = Button(calculatorframe, text='*', font=('arial', 16, 'bold'), fg='White', bg='DarkOrange2', bd=6,
                         width=6, command=lambda: btn_click("*"))
    btnmultiply.grid(row=3, column=3)

    btnans = Button(calculatorframe, text='Ans', font=('arial', 16, 'bold'), fg='White', bg='DarkOrange2', bd=6,
                    width=6, command=lambda: btn_ans())
    btnans.grid(row=4, column=0)

    btnclear = Button(calculatorframe, text='Clear', font=('arial', 16, 'bold'), fg='White', bg='DarkOrange2', bd=6,
                      width=6, command=lambda: btn_clear())
    btnclear.grid(row=4, column=1)

    btn0 = Button(calculatorframe, text='0', font=('arial', 16, 'bold'), fg='White', bg='DarkOrange2', bd=6, width=6,
                  command=lambda: btn_click("0"))
    btn0.grid(row=4, column=2)

    btndivide = Button(calculatorframe, text='/', font=('arial', 16, 'bold'), fg='White', bg='DarkOrange2', bd=6,
                       width=6, command=lambda: btn_click("/"))
    btndivide.grid(row=4, column=3)

    root.mainloop()

top.mainloop()