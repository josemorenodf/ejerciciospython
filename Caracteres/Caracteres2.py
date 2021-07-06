# 3 veces 'un', seguido de 'ium'
word = 3 * 'un' + 'ium'
print(f"1. {word}")

prefix = 'Py'
python = prefix + 'thon'
print(f"2. {python}")

# Dos o más cadenas literales una al lado de la otra o una debajo de la otra, se concatenan automáticamente.

text=('Put several strings within parentheses '
'to have them joined together.')
print(f"3. {text}")

extrange_word = 'helloworld'
print("4." , extrange_word[0:5]) # Caracteres de la posición 0 a la 5

another_word = len(str('otorrinolaringología'))
print(f"5. La cantidad de caracteres de 'otorrinolaringología' es: {another_word}")