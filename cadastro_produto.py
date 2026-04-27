"""Cadastro de Produto"""
__version__ = "0.1.0"



produto = {
     "nome": "Canetas",
    "cores": ["azul","branco"],
    "preco":3.23, 
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None
}

cliente = {
    "nome": "Victor"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3,
    
}

total_compra = compra["quantidade"] * produto["preco"]

print(f"O cliente {cliente["nome"]} comprou {compra["quantidade"]} {produto["nome"]}"
        f" e pagou {total_compra}")
