**Autor:** Gustavo da Silva Faria, a108575

<img width="344" height="269" alt="pfp" src="https://github.com/user-attachments/assets/bf9861a2-9d1d-425b-a42d-b3e486f22931" />


# Pergunta
Pediram-te para construir um programa que simule uma máquina de vending.

# Resposta
```
maq: 2025-10-22, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
LISTAR
maq:
cod | nome | quant | preco
---------------------------
A22 água 0.33L 9 0.5
A23 água 0.5L 6 0.7
A24 água 1.5L 5 1.0
B11 coca cola 6 1.0
B12 fanta 4 1
B13 ice tea 2 0.9
C16 kit-kat 3 0.3
C17 snickers 0 0.4
D3 cookies 2 1.2
D4 batatas fritas 3 1.0
D5 doritos 7 1.2
MOEDA 1e, 10c, 5c
maq: Saldo = 1e15c.
SELECIONAR D3
maq: Saldo insufuciente para satisfazer o seu pedido
maq: Saldo = 1e15c.
maq: Pedido = 1e20c.
SELECIONAR A23
maq: Pode retirar o produto dispensado água 0.5L
maq: Saldo = 45c.
LISTAR
maq:
cod | nome | quant | preco
---------------------------
A22 água 0.33L 9 0.5
A23 água 0.5L 5 0.7
A24 água 1.5L 5 1.0
B11 coca cola 6 1.0
B12 fanta 4 1
B13 ice tea 2 0.9
C16 kit-kat 3 0.3
C17 snickers 0 0.4
D3 cookies 2 1.2
D4 batatas fritas 3 1.0
D5 doritos 7 1.2
SAIR
maq: Pode retirar o troco: 0e45c.
maq: Até à próxima
```

<img width="560" height="797" alt="image" src="https://github.com/user-attachments/assets/6d5ba1ba-c045-4cf1-ab41-ef4f3212489c" />





[codigo](TPC4.py)

[stock](stock.json)
