"""
22.10.22

16-lesson: Nesting

Author: Xadiev_dev
"""
#
# shaxs0 = {
#     'ism':'Abdulla Qodiriy',
#     't_yil':810,
#     't_joy':'Buxoro',
#     'umr':60
#     }
#
# shaxs1 = {
#     'ism':'Erkin Vohidov',
#     't_yil':1894,
#     't_joy':'Farg\'ona',
#     'umr':80
#     }
#
# shaxs2 = {
#     'ism':'Alisher Navoiy',
#     't_yil':1441,
#     't_joy':'Xirot',
#     'umr':60
#     }
#
# shaxslar = [shaxs0,shaxs1,shaxs2]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     t_yil = shaxs['t_yil']
#     t_joy = shaxs['t_joy']
#     umr = shaxs['umr']
#     print(f"{ism} {t_yil}-yilda {t_joy}da tavallud topgan. "
#           f"{umr} yil umr ko'rgan.")
#
# movies ={
#         'ali':['teminator','rambo','titanic'],
#         'vali':['tenet','inception','intersteller'],
#         'hasan':['abdullajon','bomba','shaytanat'],
#         'husan':['mahallada duv-duv gap','john wick','spider-man']
#          }
# for h,m in movies.items():
#     print(f"\n{h.title()} sevimli kinolari:")
#     for i in m:
#         print(i.title())

# davlatlar =  {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower() == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")

