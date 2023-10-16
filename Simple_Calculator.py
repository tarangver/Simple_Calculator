from tkinter import *

root = Tk()
root.geometry('320x320')
root.title('Calculator')

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb
root.config(bg=_from_rgb((85,85,85)))

def ce_fun():
    text.delete('0','end')
    return
def c_fun():
    en_field = val.get()
    length = len(en_field)
    l = en_field[0:length-1]
    text.delete('0','end')
    text.insert(END,l)

def b0_fun():
    text.insert(END,'0')
def b1_fun():
    text.insert(END,'1')
def b2_fun():
    text.insert(END,'2')
def b3_fun():
    text.insert(END,'3')
def b4_fun():
    text.insert(END,'4')
def b5_fun():
    text.insert(END,'5')
def b6_fun():
    text.insert(END,'6')
def b7_fun():
    text.insert(END,'7')
def b8_fun():
    text.insert(END,'8')
def b9_fun():
    text.insert(END,'9')
def dot_fun():
    text.insert(END,'.')
def plus_fun():
    text.insert(END,'+')
def minus_fun():
    text.insert(END,'-')
def mul_fun():
    text.insert(END,'*')
def div_fun():
    text.insert(END,'/')


def sign_fun():
    en_field = val.get()
    if en_field[0] in '0123456789':
        text.insert('0','-')
    elif en_field[0] in '-':
        text.delete('0','1')

def eq_fun():
    en_field = val.get()
    ans = eval(en_field)
    text.delete('0','end')
    text.insert(END,ans)

#Taking variable:-
val = StringVar()

#Adding fiel to enter numbers:-
text = Entry(root, textvariable=val ,width=10,border=0 ,font=('Arial',40),bg=_from_rgb((85,85,85)),fg='white')
text.grid(row=0 , column=0, padx=10, pady=4, columnspan=4 )

# Now Adding some buttons:-
ce = Button(root, text='CE', width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white', bg=_from_rgb((85,85,85)),command=ce_fun).grid(row=1 , column=0)
c = Button(root, text='C', width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white', bg=_from_rgb((85,85,85)),command=c_fun).grid(row=1 , column=1)
cross = Button(root, text='[x]', width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white', bg=_from_rgb((85,85,85))).grid(row=1 , column=2)
divide = Button(root, text='/', width=10, relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white', bg=_from_rgb((85,85,85)),command=div_fun).grid(row=1 , column=3)
b7 = Button(root, text='7',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14, fg='white',bg='grey',command=b7_fun ).grid(row=2 , column=0)
b8= Button(root, text='8',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b8_fun).grid(row=2 , column=1 )
b9 = Button(root, text='9',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b9_fun).grid(row=2 , column=2 )
mul = Button(root, text='*',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white', bg=_from_rgb((85,85,85)),command=mul_fun).grid(row=2 , column=3 )
b4 = Button(root, text='4',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b4_fun).grid(row=3, column=0 )
b5 = Button(root, text='5',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b5_fun).grid(row=3 , column=1 )
b6 = Button(root, text='6',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b6_fun).grid(row=3 , column=2 )
minus = Button(root, text='-',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white', bg=_from_rgb((85,85,85)),command=minus_fun).grid(row=3 , column=3 )
b1 = Button(root, text='1',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b1_fun).grid(row= 4, column=0 )
b2 = Button(root, text='2',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b2_fun).grid(row= 4, column=1 )
b3 = Button(root, text='3',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b3_fun).grid(row= 4, column=2 )
plus = Button(root, text='+',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white', bg=_from_rgb((85,85,85)),command=plus_fun).grid(row= 4,column=3 )
sign = Button(root, text='+/-',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=sign_fun).grid(row=5 , column=0 )
b0 = Button(root, text='0',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=b0_fun).grid(row=5 , column=1 )
dot = Button(root, text='.',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14,fg='white',bg='grey',command=dot_fun).grid(row=5 , column=2 )
eq = Button(root, text='=',width=10,relief=RIDGE,borderwidth=1, padx=2, pady=14, fg='black',  bg=_from_rgb((0,171,240)),command=eq_fun).grid(row=5 , column=3 )

root.mainloop()
