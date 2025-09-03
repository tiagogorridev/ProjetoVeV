"""
Atividade Prática: Code Review e Colaboração com Git & GitHub
"""

def sao_anagramas(string1, string2):
    return sorted(string1.replace(" ", "").lower()) == sorted(string2.replace(" ", "").lower())


def cifra_de_cesar(texto, deslocamento):
    """
    Aplica a Cifra de César a uma string.
    """
    pass


def encontrar_maior_palavra(frase):
    """
    Encontra a maior palavra em uma frase.
    """
    pass


def main():
    """
    Função principal para testar as implementações.
    """
    print("=== Testes das Funções ===\n")
    
    # Testes para anagramas
    print("1. Verificador de Anagramas:")
    print(f"   sao_anagramas('amor', 'roma'): {sao_anagramas('amor', 'roma')}")
    print(f"   sao_anagramas('A gentleman', 'Elegant man'): {sao_anagramas('A gentleman', 'Elegant man')}")
    print(f"   sao_anagramas('gato', 'cabra'): {sao_anagramas('gato', 'cabra')}")
    
    # Testes para cifra de César
    print("\n2. Cifra de César:")
    print(f"   cifra_de_cesar('abc', 2): {cifra_de_cesar('abc', 2)}")
    print(f"   cifra_de_cesar('xyz', 3): {cifra_de_cesar('xyz', 3)}")
    print(f"   cifra_de_cesar('Ataque ao Amanhecer!', 5): {cifra_de_cesar('Ataque ao Amanhecer!', 5)}")
    
    # Testes para maior palavra
    print("\n3. Encontrar Maior Palavra:")
    print(f"   encontrar_maior_palavra('O rato roeu a roupa do rei de Roma'): {encontrar_maior_palavra('O rato roeu a roupa do rei de Roma')}")
    print(f"   encontrar_maior_palavra('A jornada de mil milhas começa com um único passo.'): {encontrar_maior_palavra('A jornada de mil milhas começa com um único passo.')}")
    print(f"   encontrar_maior_palavra('Seja forte e corajoso'): {encontrar_maior_palavra('Seja forte e corajoso')}")


if __name__ == "__main__":
    main()