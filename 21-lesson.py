"""
27.10.22

21-lesson: Functions and Dictionary

Author: Xadiev_dev
"""

talabalar = ['ali', 'vali', 'hasan', 'husan']


def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar)
print(baholar)
print(talabalar)