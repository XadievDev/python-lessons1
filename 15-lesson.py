"""
22.10.22

15-lesson: Dictionary

Author: Xadiev_dev
"""
#
# py_dictionary = {
#     'boolean':'mantiqiy qiymat',
#     'float':"o'nlik son",
#     'for':'uchun',
#     'if':'agar',
#     'integer':'butun son',
#     'else':'als holda',
#     'elif':'aks holda agar'
#     }
#
# for k, v in sorted(py_dictionary.items()):
#     print(f"{k.title()} - {v.title()}")


# country_capital =  {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# print('Dunyo davlatlari:')
# for q in sorted(country_capital.keys()):
#     print(q)
# print('Davlatlarning poytaxtlari:')
# for k in sorted(country_capital.values()):
#     print(k)

# request  = input('Qaysi davlatni poytaxtini bilishni istaysiz?\n>>>').lower()
# capital = country_capital.get(request)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
# else:
#     print(f"{request.upper()}ning poytaxti {capital.title()} shahri")

menu = {
        'osh':30000,
        'non':3000,
        'manti':25000,
        'kabob':30000,
        "lag'mon":20000,
        'somsa':7000,
        'shashlik':45000
        }
print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")