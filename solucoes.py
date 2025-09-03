import re

def encontrar_maior_palavra(frase: str) -> str:
    """
    Retorna a maior palavra de uma frase.
    - Ignora pontuação anexada às palavras.
    - Em caso de empate, retorna a primeira que aparece.
    - Se não houver palavras, retorna string vazia.
    """
    if not frase or not isinstance(frase, str):
        return ""

    tokens = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+", frase)

    if not tokens:
        return ""

    return max(tokens, key=len)
