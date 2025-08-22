
# aula-01 POO - 22/08/2025

# Rodar o container

    docker compose up -d


# Acessar o container no terminal

    docker exec -it aula-poo bash


# Executar os scripts Python
    python exemplo-1.py

    python exemplo-2.py

    python exemplo-3.py


### Atividades

1. No `exemplo-1.py`, usando a programação estruturada, adicione um produto "Calça Jeans" com o preço de "90.0" e aplique o desconto de 10%. Depois, no `exemplo-2.py`, usando POO, repita a adição do produto. Exiba na saída de ambos os scripts o resultado com o desconto aplicado.

Saída esperada:

    root@4b08a55506d3:/app# python exemplo-1.py
    Camiseta 45.0
    Calça Jeans 81.0

2. No `exemplo-2.py`, adicione um novo atributo chamado `peso` e um novo método chamado `calcular_frete` na Classe `Produto`. Atualize os objetos instanciados para possuirem um peso e calcule o frete baseado. Sugestão do calculo do frete `self.peso * 10.0`

Saída esperada:

    root@4b08a55506d3:/app# python exemplo-2.py
    Camiseta 45.0 2.0
    Calça Jeans 81.0 5.0