temperature = int(input("ENTER TEMPERATURE:"))

if temperature < 50:
     print(temperature, ": is Normal")
elif temperature >=50 and temperature <70:
    print( temperature," : is WARNING")
elif temperature >=70 and temperature <85:
    print( temperature, ": is High Temperature")
elif temperature >=85:
    print("Critical Temperature - Shutdoen Required")
else:
 print ("PLEASE ENTER THE CORRECT TEMPERATURE")
 