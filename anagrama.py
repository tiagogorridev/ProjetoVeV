def isAnagram(palavra):
    letras = list(palavra)
    invertida = ''.join(letras[::-1])
    if palavra == invertida:
        return "É um anagrama"
    else:
        return "Não é um anagrama"