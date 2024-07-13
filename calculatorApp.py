"""
Notes-> eval is a built-in- function used in python, eval function parses the expression argument and evaluates it as a python expression. In simple words, the eval function evaluates the “String” like a python expression and returns the result as an integer
usually grid used in frame not window
in window usually .pack

Values can be assigned to string variables defined using StringVar() using 2 ways:

Passing the value in constructor: You can pass the value of the string variable in value parameter of the constructor while defining the Tkinter variable.
string_variable = tk.StringVar(master=master_window, value="Initial value of string variable")

Using the set() method: You can use set() method to change the value of the string. For example:
string_variable = tk.StringVar(master_window)
string_variable.set("Some Text")
equation_text = ..
equatipon_label.set("..")

"""
import tkinter

def buttor_press(num):
    global equation_text
    
    equation_text += str(num) 
    equation_label.set(equation_text)
def equals():
    global equation_text
    
    try: 
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("arthemetic error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Synatax error")
        equation_text = ""
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""



window = tkinter.Tk()
window.title("Kumar Calculator Program")
window.geometry("500x500")

equation_text = ""

equation_label = tkinter.StringVar(window)

label = tkinter.Label(window , textvariable= equation_label , font = ('consolas' ,20), bg = "white" , width=24 , height = 2)
label.pack()

frame = tkinter.Frame(window)
frame.pack()

"""
List_buttons = [1,2,3,'+',4,5,6,'-',7,8,9,'*',0, '.']
for i in range(14):

    list_buttonh = tkinter.Button(frame , text = list_buttons[i]  , height= 4, width = 9, font = 35, command = lambda: buttor_press(list_buttons[i] ))
    list_buttonh.grid(row = i//4 , column=i%4)
"""
    
button1 = tkinter.Button(frame , text = 1 , height= 4, width = 9, font = 35, command = lambda: buttor_press(1))
button1.grid(row = 0 , column=0)

button2 = tkinter.Button(frame , text = 2 , height= 4, width = 9, font = 35, command = lambda: buttor_press(2))
button2.grid(row = 0 , column=1)

button3 = tkinter.Button(frame , text = 3 , height= 4, width = 9, font = 35, command = lambda: buttor_press(3))
button3.grid(row = 0 , column=2)

button4 = tkinter.Button(frame , text = 4 , height= 4, width = 9, font = 35, command = lambda: buttor_press(4))
button4.grid(row = 1 , column=0)

button5 = tkinter.Button(frame , text = 5 , height= 4, width = 9, font = 35, command = lambda: buttor_press(5))
button5.grid(row = 1 , column=1)

button6 = tkinter.Button(frame , text = 6 , height= 4, width = 9, font = 35, command = lambda: buttor_press(6))
button6.grid(row = 1 , column=2)

button7 = tkinter.Button(frame , text = 7 , height= 4, width = 9, font = 35, command = lambda: buttor_press(7))
button7.grid(row = 2 , column=0)

button8 = tkinter.Button(frame , text = 8 , height= 4, width = 9, font = 35, command = lambda: buttor_press(8))
button8.grid(row = 2 , column=1)

button9 = tkinter.Button(frame , text = 9 , height= 4, width = 9, font = 35, command = lambda: buttor_press(9))
button9.grid(row = 2 , column=2)

button0 = tkinter.Button(frame , text = 0 , height= 4, width = 9, font = 35, command = lambda: buttor_press(0))
button0.grid(row = 3 , column=0)



button_plus = tkinter.Button(frame , text = '+' , height= 4, width = 9, font = 35, command = lambda: buttor_press('+'))
button_plus.grid(row = 0 , column=3)

button_subtract = tkinter.Button(frame , text = '-' , height= 4, width = 9, font = 35, command = lambda: buttor_press('-'))
button_subtract.grid(row = 1 , column=3)

button_multiply = tkinter.Button(frame , text = '*' , height= 4, width = 9, font = 35, command = lambda: buttor_press('*'))
button_multiply.grid(row = 2 , column=3)

button_decimal = tkinter.Button(frame , text = '.' , height= 4, width = 9, font = 35, command = lambda: buttor_press('.'))
button_decimal.grid(row = 3 , column=1)

button_devide = tkinter.Button(frame , text = '/' , height= 4, width = 9, font = 35, command = lambda: buttor_press('/'))
button_devide.grid(row = 3 , column=3)


button_equal = tkinter.Button(frame , text = '=' , height= 4, width = 9, font = 35, command = equals)
button_equal.grid(row = 3 , column=2)

button_clear = tkinter.Button(window , text = 'Clear' , height= 4, width = 18, font = 35, command = clear)
button_clear.pack()



window.mainloop()
