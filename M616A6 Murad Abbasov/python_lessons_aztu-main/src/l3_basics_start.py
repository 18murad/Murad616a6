# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

ad = input()
print("Salam, " + ad + "!")   # Proqram — əmrlər ardıcıllığı
# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)
age = int(input())
print("Menim yasim, ", age + 1 , "!")

print(age)
age = 25
print(age < 25)
print(age < 25)
print(age == 25)





print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# TODO: cell, rsrp, drops

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# TODO: type(...) və «mətn ≠ ədəd»

print("=== Kərpic 4 ===")   # Müqayisə → True / False
# TODO: rsrp < -105, ==

print("=== Kərpic 5 ===")   # Siyahı (list)
# TODO: rsrp_list, indeks, len, orta

name_list = ["Emin", "Murad", "Əli", "Veli", "Sirveli"]
print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[3])
print(name_list[4])

print("=== Kərpic 6 ===")   # Lüğət (dict)
# TODO: row = {...}, row["region"]

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# TODO: zəif ölçmələri saymaq

age = int(input("yasini daxil et: "))

if age > 18:
     print ("yeke")

elif age == 18:
     print("18 yas")
        
else:
     print("Balaca")




rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
weak = 0
for v in rsrp_list:
 if v < -105:
     print(v,"zeif")
     weak = weak + 1
 else:
      print(v, "normal")
print("Zeif olcme sayi", weak) 

    
 
print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd
