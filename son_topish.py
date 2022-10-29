"""
29.10.22

Son topish

Author: Xadiev_dev
"""
import random as r
def son_top(son=10):
    print(f"Men 1dan {son}gacha son o'yladim.Topa olasizmi?")
    taxminiy_son = r.randint(1,son+1)
    sikl = 0
    while True:
        sikl += 1
        son_oyla = int(input("Sonni kiriting:\n>>>"))
        if son_oyla == taxminiy_son:
            break
        elif son_oyla>taxminiy_son:
            print("Men o'ylagan son bundan kichik.")
        else:
            print("Men o'ylagan siznikidan katta.")
    print(f"Topdiz!Men {taxminiy_son}ni o'ylagan edim.{sikl} ta taxmin bilan topdingiz.\n")
    return sikl

#
# def son_top_pc(son=10):
#     input(f"1dan {son}gacha son o'ylang. Men topishga harakat qilaman\n"
#           f"Son o'ylagan bo'lsangiz istalgan tugmani bosing.")
#     quyi = 1
#     yuqori = son
#     sikl = 0
#     while True:
#         sikl += 1
#         if yuqori != quyi:
#             taxmin = r.randint(quyi,yuqori)
#         else:
#             taxmin = yuqori
#         javob = input(f"Siz {taxmin} sonini o'yladingiz:to'g'ri(T),"
#                       f"agar o'ylagan soningiz kichik bo'lsa(-),yoki katta bo'lsa(+):\n>>>").lower()
#         if javob == '-':
#             yuqori = taxmin-1
#         elif javob == '+':
#             quyi = taxmin+1
#         else:
#             break
#         print(f"Men {sikl} ta urunishda topdim.")
#         return sikl



def son_top_pc(son=10):
    input(f"1 dan {son} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = son
    sikl = 0
    while True:
        sikl += 1
        if quyi != yuqori:
            taxmin = r.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
            f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower()
        )
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {sikl} ta taxmin bilan topdim!")
    return sikl

def play(son=10):
    yana = True
    while yana:
        sontop = son_top(son)
        sontop_pc = son_top_pc(son)
        if sontop < sontop_pc:
            print(f"Siz {sontop} ta taxmin bilan yutdingiz.")
        elif sontop > sontop_pc:
            print(f"Men {sontop_pc} ta taxmin bilan yutdim.")
        else:
            print('Durrang')
        yana = int(input("Yana o'ynaysizmi?(1/0)"))
play()


