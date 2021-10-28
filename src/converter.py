def conv_celcius():
    c = float(input("masukkan suhu °C : "))
    r = (4/5)*c
    f = ((9/5)*c)+32
    k = c+273

    print("suhu Reamur     : ", r, "°R")
    print("suhu Fahrenheit : ", f, "°F")
    print("suhu Kelvin     : ", k, "K")

def conv_reamur():
    r = float(input("masukkan suhu °R : "))
    c = (5/4)*r
    f = ((9/4)*r)+32
    k = ((5/4)*r)+273

    print("suhu Celcius    : ", c, "°C")
    print("suhu Fahrenheit : ", f, "°F")
    print("suhu Kelvin     : ", k, "K")
    
def conv_fahrenheit():
    f = float(input("masukkan suhu °F : "))
    c = (5/9)*(f-32)
    k = c+273
    r = (4/9)*(f-32)

    print("suhu Kelvin     : ", k, "K")
    print("suhu Celcius    : ", c, "°C")
    print("suhu Reamur     : ", r, "°R")


def conv_kelvin():
    k = float(input("masukkan suhu K : "))
    c = k-273
    f = ((9/5)*c)+32
    r = (4/5)*(k-273)
    
    print("suhu Celcius    : ", c, "°C")
    print("suhu Fahrenheit : ", f, "°F")
    print("suhu Reamur     : ", r, "°R")
