city = str(input("Ingresa tu ciudad de nacimiento: "))
age= int (input("Ingresa tu edad:  "))

if(age >= 18):
    #msg= "Esta persona tiene la edad de: " str(age) + " puede votar en la ciudad de " + city
    print(f'Esta persona tiene la edad de {age} puede votar en la ciudad de {city}')
else:
    print("Esta persona no tiene edad suficiente para votar")
