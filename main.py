## FastAPI - Construção de API
## Uvicorn - Hospedagem da API local
    # uvicorn main:app --reload

# Fast
# Documentação automática (/docs)
# Gerenciamento de processos assíncronos

from fastapi import FastAPI

app = FastAPI()

saidas = {
    1: {"item": "Coca-Cola Lata", "preco_unitario": 3.50, "quantidade": 12},
    2: {"item": "Coca-Cola Litro", "preco_unitario": 5.60, "quantidade": 2},
    3: {"item": "Chocolate", "preco_unitario": 5, "quantidade": 1},
    4: {"item": "Leite", "preco_unitario": 2.70, "quantidade": 3},
    5: {"item": "Miojo", "preco_unitario": 0.50, "quantidade": 10},
}

@app.get("/")
def home():
    return "HOME"

@app.get("/vendas")
def vendas():
    return {"Vendas:": len(saidas)}

@app.get("/vendas/{id_venda}")
def venda_por_id(id_venda: int):
    return saidas[id_venda]

