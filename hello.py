import imp
from random import randint, random
from requests import get
'''
a = 2
b = 3
c = a + b
d = True
print(c);

if d == True :
    print(c);


print("Hello",c);

print("Hello",str(c))

print("μλ?")


def say_hello() :
    print("Hello")

say_hello()

def who_are_u(name="user"):
    print("who are u?")
    print("my name is", name )

who_are_u("mario")
who_are_u()


def calc_plus(a,b = 0):
    print("answer =",a+b)

def calc_minus(a, b = 0):
    print("answer =", a-b)

calc_plus(100,100)
calc_plus(200)

calc_minus(100,100)
calc_minus(300)


def calc_tax(money):
    return_tax = money * 0.05
    return return_tax

def bank_program(tax):
    print("Thank you for your money",tax)

tax = calc_tax(2500000)
bank_program(tax)

format_test = f"a,b,c,d,{tax}"
print(format_test)


age = int(input("how old are you?"))

if age  <= 10 :
    print("So young")
elif age > 10 and age <= 20:
    print("not so young")
elif age == 30 or age == 40 or age == 50:
    print("happy birthday~π")
else :
    print("Go ahead!")


pc_choice = randint(1,500)

print(pc_choice)

print("λ€μ―κ³ κ°κ²μμ ν΄λ³΄λλ‘ νμ~")

pc_choice = randint(1,100)

print("μ»΄ν¨ν°λ μ«μλ₯Ό κ³¨λμ΄μ~")

end_value = 5
ing_value = 0

playing = True

def fail_game():
    global ing_value
    global end_value
    global playing
    ing_value = ing_value + 1
    
    if end_value == ing_value:
        playing = False
        print("5λ² λͺ¨λ μ€ν¨λ‘ κ²μμμ μ‘μ΅λλ€.")
    else :
        return end_value - ing_value

while playing:

    set_value = int(input("μ«μλ₯Ό κ³ λ₯΄μμ€!"))

    if(pc_choice > set_value):
        print("μ!")
        print(f"{fail_game()} λ² λ¨μμ΅λλ€.")
    elif(pc_choice < set_value):
        print("λ€μ΄!")
        print(f"{fail_game()} λ² λ¨μμ΅λλ€.")
    else:
        print("λ§μ·μ΅λλ€! κ²μμμ μΉλ¦¬νμ¨μ΅λλ€")
        playing = False
'''

websites = (
    "google.com",
    "naver.com",
    "facebook.com"
)

results = {}

for website in websites :
    if not website.startswith("https://") :
        website = f"https://{website}"
    respose = get(website)
    
    if respose.status_code == 200:
        results[website] = "OK"
        #print(f"{website} is ok")
    else :
        results[website] = "FAILED"
        #print(f"{website} not ok")
print(results)
