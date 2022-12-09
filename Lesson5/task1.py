# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

my_text = 'Ехал Грека через абвреку реку, видит Грека вабв в реке рак. абв.'

def del_symbols(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_symbols(my_text)
print(my_text)
