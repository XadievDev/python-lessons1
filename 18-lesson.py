"""
25.10.22

18-lesson: While(continue)

Author: Xadiev_dev
"""

# buyurtmalar = []
# while True:
#     mahsulot = input(f"Buyurtma bermoqchi bo'lgan mahsulotni yozing:\n>>>")
#     buyurtmalar.append(mahsulot)
#     yana = input("Yana buyurtma berasizmi(ha/yo'q):\n>>>")
#     if yana.lower() == 'ha':
#         continue
#     else:
#         break
# # print('Buyurtma bergan mahsulotlariz.')
# # for buyurtma in buyurtmalar:
# #     print(buyurtma)
#
# # e-bozor
# e_bozor = {}
# sikl = True
# while sikl:
#     mahsulot = input("Mahsulot nomini kiriting:\n>>>")
#     narx = int(input(f"{mahsulot.title()}ning narxini kiriting:\n>>>"))
#     e_bozor[mahsulot] = narx
#     javob = input('Yana mahsulot qo\'shasizmi?(1/0)')
#     if javob != '1':
#         sikl = False
# print(e_bozor)

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

for mahsulot, narx in mahsulotlar.items():
    for buyurtma in buyurtmalar:
        if mahsulot == buyurtma:
            print(f"{buyurtma.title()}ning narxi {narx} so'm")