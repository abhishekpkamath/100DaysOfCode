print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

T_value = name1.count("t") + name2.count("t")
R_value = name1.count("r") + name2.count("r")
U_value = name1.count("u") + name2.count("u")
E_value = name1.count("e") + name2.count("e")
L_value = name1.count("l") + name2.count("l")
O_value = name1.count("o") + name2.count("o")
V_value = name1.count("v") + name2.count("v")
E_value = name1.count("e") + name2.count("e")

digit1 = T_value + R_value + U_value + E_value
digit2 = L_value + O_value + V_value + E_value
number = int(f"{digit1}{digit2}")

if number < 10 or number > 90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif number >= 40 and number <= 50:
    print(f"Your score is {number}, you are alright together.")
else:
    print(f"Your score is {number}.")    