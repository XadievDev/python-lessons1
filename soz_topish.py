"""
29.10.22

So'z topish

Author: Xadiev_dev
"""
# import random as r
# from uzwords import words
#
#
# def get_words():
#     word =  r.choice(words)
#     while '-' in word or ' ' in word:
#         word = r.choice(words)
#     return word.upper()
#
#
# def display(user_letters,word):
#     display_letter=""
#     for letter in word:
#         if letter in user_letters:
#             display_letter += letter
#         else:
#             display_letter += "-"
#     return display_letter
#
# def play():
#     word = get_words()
#     word_letters = set(word)
#     user_letters = ''
#     print(f"Men {len(word)} xonali so'z o'yladim. Topa olasizmi?")
#     while len(word_letters) > 0:
#         print(display(user_letters,word))
#         if len(user_letters)>0:
#             print(f"Shu paytgacha kiritgan hatflaringiz: {user_letters}.")
#
#         letter = input("Harf kiriting:").upper()
#         if letter in user_letters:
#             print("Bu harfni avval kiritgansiz.Boshqa harf kiriting.")
#             continue
#         elif letter in word:
#             word_letters.remove(letter)
#             print(f"{letter} harfi to'g'ri.")
#         else:
#             print("Bunday harf yoq.")
#             user_letters += letter
#     print(f"Tabriklayman! {word} ni {len(user_letters)} ta urinishda topdingiz.")
#
# play()


import random
from uzwords import words


def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters, word):
    display_letter = ""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter


def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    # print(word)
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")

        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")

play()