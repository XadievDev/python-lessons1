"""
19.10.22

7-lesson: List

Author: Xadiev_dev
"""

# countries = ['Japan','USA','Uzbekistan','Russia','Mexico','German','China']
# print(f"Ro'yxatdagi davlatlar: {countries}.")
# print(f"Ro'yxatdagi davlatlar: {sorted(countries)}.")
# print(f"Ro'yxatdagi davlatlar: {sorted(countries, reverse=True)}.")
# countries.reverse()
# print(f"Ro'yxatdagi davlatlar: {countries}.")
# countries.sort()
# print(f"Ro'yxatdagi davlatlar: {countries}.")
# countries.sort(reverse=True)
# print(f"Ro'yxatdagi davlatlar: {countries}.")

# numbers = list(range(120,1200,2))
# print(numbers)
# print(f"Jami:{max(numbers)}")
# print(f"max-min: {max(numbers)-min(numbers)}")
# print(f"Ro'yxatdagi elementlar soni: {len(numbers)}")
# print(numbers[:20])
# print(numbers[-20:])
taomlar = ['osh','norin','somsa','manti','xonim']
nonushta = taomlar[:]
nonushta.append('tuxum')
nonushta.append('choy')
nonushta.remove('osh')
nonushta.remove('norin')
print(taomlar)
print(nonushta)
