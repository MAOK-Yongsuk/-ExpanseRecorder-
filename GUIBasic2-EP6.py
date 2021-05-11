# GUIBasic2-Expense.py
from tkinter import *
from tkinter import ttk, messagebox # ttk is theme of Tk
import csv
from datetime import datetime
from tkinter.ttk import Notebook

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by MAOK')
GUI.geometry('600x750+500+50')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก

################################## MENU ##########################################

menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')
# Help
def About():
    messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

#################################### TAB 1 #######################################

#-------------------- TAB/PHOTO--------------------------

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH, expand=True)

F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack(pady=40)



bg = PhotoImage(file='wallet.png').subsample(2)
walletpic = ttk.Label(F1,image=bg).pack()

bgTab1 = PhotoImage(file='add.png').subsample(8)
bgTab2 = PhotoImage(file='listt.png').subsample(8)

Tab.add(T1, text=f'{"Add Expanse":^{20}}',image=bgTab1, compound='top')
Tab.add(T2,text=f'{"All List":^{20}}',image=bgTab2,compound='top')


#---------------------------------------------------------

days = {'Mon':'จันทร์','Tue':'อังคาร','Wed':'พุธ','Thu':'พฤหัสบดี','Fri':'ศุกร์','Sat':'เสาร์','Sun':'อาทิตย์'}

def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    quantity = v_quantity.get()

    if expense == '':
        print('No Data')
        messagebox.showinfo('Error','กรุณากรอกข้อมูลค่าใช้จ่าย')
        return
    elif price == '':
            messagebox.showinfo('Error','กรุณากรอกราคา')
            return    
    elif quantity == '':
             quantity = 1       

    total = float(price) * float(quantity)
    try:
        total = float(price) * float(quantity)
        # .get() คือดึงค่ามาจาก v_expense = StringVar()
        print('รายการ: {} ราคา: {}'.format(expense,price))
        print('จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total))
        text = 'รายการ: {} ราคา: {}\n'.format(expense,price)
        text = text + 'จำนวน: {} รวมทั้งหมด: {} บาท'.format(quantity,total)
        v_result.set(text)
        # clear ข้อมูลเก่า
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')


        # บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
        today = datetime.now().strftime('%a')
        print(today)
        dt = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        dt = days[today] + '-' + dt
        with open('savedata.csv','a',encoding='utf-8',newline='') as f:
            # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
            # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
            # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
            data = [dt,expense,price,quantity,total]
            fw.writerow(data)


        # ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
        E1.focus()
        #update_record()
        update_table()
    except:
        print('ERROR')
        messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')
    
      
# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'

#------text1--------
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#-------------------

#------text2--------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-------------------

#------text3--------
L = ttk.Label(F1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_quantity = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable=v_quantity,font=FONT1)
E3.pack()
#-------------------

savepic = PhotoImage(file='savepic.png').subsample(9) #รูปไอคอนsave
B2 = ttk.Button(F1,text='Save',image=savepic,compound='left',command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('------ผลลัพธ์-----')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='green')
result.pack(pady=20)
GUI.bind('<Tab>',lambda x: E2.focus())

############################### TAB 2 #######################################

#------------ text all List ----------------

def read_csv():
    with open('savedata.csv',encoding='utf-8',newline='') as f:
        fr = csv.reader(f)
        data = list(fr)
    return data
'''
def update_record():
    getdata = read_csv()
    v_list.set('')
    text = ''
    for d in getdata:
        txt = '{}---{}---{}---{}---{}\n'.format(d[0],d[1],d[2],d[3],d[4])
        text = text + txt
        
    v_list.set(text)

v_list = StringVar()
v_list.set('----All Record----')
alllist = ttk.Label(T2, textvariable=v_list,font=(None,15),foreground='green')
alllist.pack(pady=20)

update_record()
'''
#----------------- table ----------------------

L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด',font=FONT1).pack(pady=20)
header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=15)
resulttable.pack()

# for i in range(len(header)):
    # resulttable.heading(header[i],text=header[i])

for h in header:
    resulttable.heading(h,text=h)

headerwidth = [200,120,85,85,85]
for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)

def update_table():
    resulttable.delete(*resulttable.get_children())
    data = read_csv()
    for dd in data:
        resulttable.insert('',0,value=dd)

update_table()

GUI.mainloop()
