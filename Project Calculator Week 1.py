name = str(input("PLZ Enter Your First Name: "))
family = str(input("Plz Enter Your Last Name: "))
print(f"Welcome To This App , {name} {family} ")
#namayeshe menu
print(" 1-Addition\n 2-Subtraction\n 3-Multiplication\n 4-Division\n 5-Exponentiation\n 6-Modulus\n 7-Exit\n ")
#Entekhab Menu
number1 = int(input(f"Plz Enter Your First Number {name} {family} : "))
number2 = int(input(f"Plz Enter Your Second Number {name} {family} : "))
choosemenu = input(f"Plz Enter One of Menu Numbers Or Type Operator Name , {name} {family}: ")

#jam
sum = number1 + number2
#tafrigh
subtraction = number1 - number2
#Zarb
multiplication = number1 * number2
#Taghsim
division = number1 / number2
#Tavan
exponentiation = number1 ** number2
#Baghimandeh
modulus = number1 % number2

#jam
if choosemenu == "1" or choosemenu =="Addition" or choosemenu =="addition":
 print(f"Jame Adade {number1} va Adade {number2} barabar ast ba = {sum}, Dear {name} {family}")

#tafrigh
elif choosemenu == "2" or choosemenu =="Subtraction" or choosemenu =="subtraction":
    print(f"Tafrighe Adade {number1} bar Adade {number2} barabar ast ba = {subtraction}, Dear {name} {family}")

#Zarb
elif choosemenu == "3" or choosemenu =="Multiplication" or choosemenu =="multiplication":
     print(f"Zarbe Adade {number1} Dar Adade {number2} barabar ast ba = {multiplication}, Dear {name} {family}")

#Taghsim
elif choosemenu == "4" or choosemenu =="Division" or choosemenu =="division":
     print(f"Taghsime Adade {number1} Bar Adade {number2} barabar ast ba = {division}, Dear {name} {family}")

#Tavan
elif choosemenu == "5" or choosemenu =="Exponentiation" or choosemenu =="exponentiation":
    print(f"Adade {number1} Be Tavane Adade {number2} barabar ast ba = {exponentiation}, Dear {name} {family}")

#Baghimandeh
elif choosemenu == "6" or choosemenu =="Modulus" or choosemenu =="modulus":
     print(f"Baghimande Adade {number1} Bar Adade {number2} barabar ast ba = {modulus}, Dear {name} {family}")

#Exit
elif choosemenu == "7" or choosemenu =="Exit" or choosemenu =="exit":
    print(f"Goodbye , Dear {name} {family}")

#Dar Soorati Ke Adadha Ya Text Eshtebah Bashad
else:
    print(f"{name} {family} Shoma Adade Eshtebah Dar Menu Vared Kardid Ya In ke Gozine Morde Nazar Ra Eshtebah Type Kardid")
    
    
