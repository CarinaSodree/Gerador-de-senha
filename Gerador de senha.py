import random
import string

def gerar_senha(comprimento=12, maiusculas=True, minusculas=True, numeros=True, simbolos=True):
    
    """Gera uma senha aleatoria com base nos critérios escolhidos pelo usuário
       Parâmetros:
       - comprimento (int): tamanho da senha desejada (padrão: 12 caracteres)
       - maiusculas (bool): incluir letras maiúsculas na senha
       - minusculas (bool): incluir letras minusculas na senha
       - numeros (bool): incluir números na senha
       - simbolos (bool): incluir símbolos na senha
       
       Retorna:
       - senha(str): a senha gerada
       """ 
    caracteres = ""

    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

        if not caracteres:
            raise ValueError("É necessário selecionar pelo menos um tipo de caractere para gerar a senha")
        senha = "".join(random.choice(caracteres) for _ in range(comprimento))
        return senha
    
# Exemplo de uso
if __name__ == "__main__":
    print("gerador de senhas aleatórias")
    tamanho = int(input("digite o tamanho da senha desejada: "))
    incluir_maiusculas = (input("Incluir letras maiusculas? (s/n): "))
    incluir_minusculas = (input("Incluir letras minusculas? (s/n): "))
    incluir_numeros = input("incluir números? (s/n)) ").strip().lower == "s"
    incluir_simbolos = input("incluir simbolos? (s/n): ").strip().lower() =="s"

    try:
        senha_gerada = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
        print(f"Senha gerada: {senha_gerada}")
    except ValueError as e:
        print(f"Erro: {e}")
        