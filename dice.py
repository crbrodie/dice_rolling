from random import randint as r

dice_size = int(input('pick a dice size: '))
random_num = r(1, dice_size)

print(random_num)