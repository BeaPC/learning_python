# Problema "retangulo"
# Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
# da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.
# Exemplo 1:
# Base do retangulo: 4.0
# Altura do retangulo: 5.0
# AREA = 20.0000
# PERIMETRO = 18.0000
# DIAGONAL = 6.4031

base= float; 
altura= float; area = float; perimetro= float; 

base = float(input(" Base do retangulo:"))
altura= float(input("Altura do retangulo:"))

area = base * altura
perimetro = 2 * (base + altura)

print(f"AREA ={area}")
print(f"PERIMETRO ={perimetro}")
