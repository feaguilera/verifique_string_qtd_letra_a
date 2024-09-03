def verificar_letra_a(texto):
    texto = texto.lower()
    
    quantidade = texto.count('a')
    
    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto = input("Informe uma string: ")

verificar_letra_a(texto)
