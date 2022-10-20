"""
19.10.22

9-lesson: LIST(continue)

Author: Xadiev_dev
"""

# mehmonlar = ['Ali','Vali','Hasan','Husan']
# n = 0
# for mehmon in mehmonlar:
#     print(f"Assalomu aleykum {mehmon}.")
#     n += 1
# print(f"Kod {n} marta takrorlandi.")
#

# for n in range(11,100,2):
#     print(f"{n} ning kubi {n**3} ga teng.")
#
#
# kinolar = []
# for n in range(5):
#     kino = input(f"Sevimli {n+1}-kinongizni kiriting.\n>>>")
#     kinolar.append(kino)
# print(kinolar)

suhbatdoshlar = []
n = int(input('Bugun necha kishi bilan suhbatlashdingiz?\n>>>'))
for i in range(n):
    suhbatdosh = input(f"{i+1}-suhbatdoshingiz kim?\n>>>")
    suhbatdoshlar.append(suhbatdosh)
print(suhbatdoshlar)

