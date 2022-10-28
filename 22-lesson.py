"""
27.10.22

22-lesson: *args, **kwargs

Author: Xadiev_dev
"""


def kopaytir(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


kopayma = kopaytir(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(kopayma)

def malumot_qaytar(ism,familiya,**malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
avto1 = malumot_qaytar('amirbek','xadiev',yosh=16,yil=2006)
print(avto1)