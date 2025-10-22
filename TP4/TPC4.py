import json
from datetime import date

STOCK="stock.json"

MOEDAS=[
    (200, "2e"),
    (100, "1e"),
    (50, "50c"),
    (20, "20c"),
    (10, "10c"),
    (5, "5c"),
    (2, "2c"),
    (1, "1c"),
]

def load_stock():
    with open(STOCK, "r", encoding="utf-8") as f:
        return json.load(f)

def save_stock(stock):
    with open(STOCK, "w", encoding="utf-8") as f:
        json.dump(stock, f, ensure_ascii=False, indent=2)

def list_stock(stock):
    if not stock:
        print("maq: Stock vazio.")
        return
    print("maq:\ncod | nome | quant | preco")
    print("---------------------------")
    for p in stock:
        print(f"{p['cod']} {p['nome']} {p['quant']} {p['preco']}")

def listar_saldo(saldo):
    saldoe=saldo//100
    saldoc=saldo%100
    print(f"maq: Saldo = {f'{saldoe}e' if saldoe > 0 else ''}{saldoc:02d}c.")

def main():
    stock=load_stock()
    print(f"maq: {date.today().isoformat()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    saldo=0
    while True:
        resposta=input().strip()
        linhas=resposta.split(None, 1)
        comando=linhas[0].upper()
        args=" ".join(linhas[1:])
        if comando=="LISTAR":
            load_stock()
            list_stock(stock)
        elif comando=="MOEDA":
            for n in args.split(','):
                tok = n.strip().strip(".,")
                enc=0
                for m, i in MOEDAS:
                    if tok==i:
                        saldo+=m
                        enc=1
                if enc==0:
                    print(f"maq: Moeda {n} inválida.")
            listar_saldo(saldo)
        elif comando=="SELECIONAR":
            codigo=args.strip()
            produto=None
            for p in stock:
                if p['cod']==codigo:
                    produto=p
                    preco=int(p['preco']*100)
                    if saldo>=preco:
                        saldo-=preco
                        produto['quant']-=1
                        save_stock(stock)
                        print(f"maq: Pode retirar o produto dispensado {produto['nome']}")
                        listar_saldo(saldo)
                    else:
                        print(f"maq: Saldo insufuciente para satisfazer o seu pedido")
                        listar_saldo(saldo)
                        print(f"maq: Pedido = {preco//100}e{preco%100}c.")
            if produto is None:
                print(f"maq: Produto {produto} inexistente.")
        elif comando=="SAIR":
            if saldo>0:
                print(f"maq: Pode retirar o troco: {saldo//100}e{saldo%100}c.")
                print("maq: Até à próxima")
            break

if __name__=="__main__":
    main()
    
