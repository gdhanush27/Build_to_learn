from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5838320632:AAHPufkl98Di8dR0PsduLhJZkX45aqR0_wk",use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Vanakkam Welcome to the Build to learn Bot.Please write\
		/help to see the commands available.")
 
def Datatypes(update: Update, context: CallbackContext):
	update.message.reply_text("""Example ==>> Data Type
	
x = "Hello World" ==>> str	
x = 20 ==>> int	
x = 20.5 ==>> float	
x = 1j ==>> complex	
x = ["apple", "banana", "cherry"] ==>> list	
x = ("apple", "banana", "cherry") ==>> tuple	
x = range(6) ==>> range	
x = {"name" : "John", "age" : 36 ==>> dict	
x = {"apple", "banana", "cherry"} ==>> set	
x = frozenset({"apple", "banana", "cherry"}) ==>> frozenset	
x = True ==>> bool	
x = b"Hello" ==>> bytes	
x = bytearray(5) ==>> bytearray	
x = memoryview(bytes(5)) ==>> memoryview
x = None ==>> NoneType
  """)

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/Arithmetic_Operators - To Know about python's Arithmetic Operators
	/Loops - To Know about for loop and while loop
	/If_else - To Know about branching(If else statement)
	/functions - To Know about user defined functions
  /Datatypes - To Know about data types in python""")


def Loops(update: Update, context: CallbackContext):
	update.message.reply_text(
		"""  1.While loop:

    Syntax:
    while expression:
      statement(s)

    Example:
    count = 0
    while (count < 3):   
        count = count + 1
        print("Hello Geek")
    
    Output:
    Hello Geek
    Hello Geek
    Hello Geek

    2.For loop:

    Syntax:
    for iterator_var in sequence:
        statements(s)

    Example:
    n = 4
    for i in range(0, n):
        print(i)
    
    Output:
    0
    1
    2
    3
    """)


def If_else(update: Update, context: CallbackContext):
	update.message.reply_text("""Python If ... Else:

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

Short Hand If ... Else:

a = 2
b = 330
print("A") if a > b else print("B")

Nested If:

x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
""")


def Arithmetic_Operators(update: Update, context: CallbackContext):
	update.message.reply_text(
		"""# Examples of Arithmetic Operator
a = 9
b = 4
  
# Addition of numbers
add = a + b
  
# Subtraction of numbers
sub = a - b
  
# Multiplication of number
mul = a * b
  
# Division(float) of number
div1 = a / b
  
# Division(floor) of number
div2 = a // b
  
# Modulo of both number
mod = a % b
  
# Power
p = a ** b
  
# print results
print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)

Output:
13
5
36
2.25
2
1
6561""")


def functions(update: Update, context: CallbackContext):
	update.message.reply_text("syntax of user defined functions\n\ndef function_name(parameters):\n   return expression\n\nExamble:\n\ndef hello_world():\n\t\tprint(\"Hello World\")\n\nhello_world()")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('If_else', If_else))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('Arithmetic_Operators', Arithmetic_Operators))
updater.dispatcher.add_handler(CommandHandler('Loops', Loops))
updater.dispatcher.add_handler(CommandHandler('functions', functions))
updater.dispatcher.add_handler(CommandHandler('Datatypes', Datatypes))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) 

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
