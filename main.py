# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.

import re

def normalize(s):
    replacements = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u'
    }
    for a, b in replacements.items():
        s = s.replace(a, b)
    return s

def is_palindrome(text):
    formatted_text = re.sub("[^\w]", "", text).lower()
    normalized_text = normalize(formatted_text)

    i = 0
    j = len(normalized_text) - 1
    while i < j:
        if normalized_text[i] != normalized_text[j]:
            return False
        i += 1
        j -= 1

    return True

print(is_palindrome("Ana lleva al oso la avellana")) # True
print(is_palindrome("Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida")) # True
print(is_palindrome("¿Qué tal todo?")) # False
print(is_palindrome("I did, did I?")) # True
print(is_palindrome("solod")) # False