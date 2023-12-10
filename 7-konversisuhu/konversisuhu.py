print("\n","===PROGRAM KONVERSI SUHU CELCIUS===")

celcius = float(input("Masukan suhu celcius "))
print("Suhu celcius nya adalah",celcius,"celcius")

reamur = 4 / 5 * celcius
print("Suhu reamur nya adalah",reamur)

fahrenheit = ( 9 / 5 * celcius) + 32
print("Suhu fahrenheit nya adalah",fahrenheit)

kelvin = celcius + 273.15
print("Suhu kelvin nya adalah",kelvin)


print("\n","===PROGRAM KONVERSI SUHU REAMUR===")

reamur = float(input("Masukan suhu reamur "))
print("Suhu reamur nya adalah",reamur)

celcius = 5 /4 * reamur
print("Suhu celcius nya adalah",celcius)

fahrenheit = (9 / 4 * reamur) + 32
print("Suhu fahrenheit nya adalah",fahrenheit)

kelvin = (5 / 4 * reamur) + 273.15
print("Suhu kelvin nya adalah",kelvin)

print("\n","===PROGRAM KONVERSI FAHRENHEIT===")

fahrenheit = float(input("Masukkan suhu fahrenheit: "))
print("Suhu fahrenheit nya adalah",fahrenheit)

celcius = (5 /9) * (fahrenheit - 32)
print("Suhu celcius nya adalah",celcius)

reamur = (4 /9) * (fahrenheit - 32)
print("Suhu reamur nya adalah",reamur)

kelvin = celcius + 273.15
print("Suhu kelvin nya adalah",kelvin)


print("\n","===PROGRAM KONVERSI KELVIN===")

kelvin = float(input("Masukan suhu kelvin: "))
print("Suhu kelvin nya adalah",kelvin)

celcius = kelvin - 273.15
print("Suhu celcius nya adalah",celcius)

reamur = (4 / 5) * (kelvin-273.15)
print("Suhu reamur nya adalah",reamur)

fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu fahrenheit nya adalah",fahrenheit)
