# OPERASI KONVERSI SUHU
'''
Jenis suhu
    1. Celcius
    2. Reamur
    3. Fahrenheit
    4. Kelvin
'''
import converter as cv

def convert_temp():
    print("\n OPERASI KONVERSI SUHU \n")
    print("1.Celcius\n2.Reamur\n3.Fahrenheit\n4.Kelvin")
    conv = input("masukkan suhu yang ingin di convert ? ").lower()


    # Celcius to other
    if conv == "1" or conv == "c" or conv == "celcius":
        cv.conv_celcius()
        

    # Reamur to other
    elif conv == conv == "2" or conv == "r" or conv == "reamur":
        cv.conv_reamur()
        

    # Fahreinheit to other
    elif conv == conv == "3" or conv == "f" or conv == "fahrenheit":
        cv.conv_fahrenheit()
        
    # Kelvin to other
    elif conv == conv == "4" or conv == "k" or conv == "kelvin":
       cv.conv_kelvin()
       
    else:
        err = input("jenis suhu tidak ada coba lagi ? \n (y/n) ").lower()
        if err == 'y':
            convert_temp()
        else:
            print("bye")
            exit()



if __name__ == '__main__':
    convert_temp()

ans = input("coba lagi ? \n (y/n)").lower()
if ans == 'y':
    convert_temp()
else:
    print("bye")
    exit

       
      