# app.py
# 1. Importamos as bibliotecas necessárias
from flask import Flask, request, jsonify

# 2. Criamos a aplicação Flask
app = Flask(__name__)

# --- Dados iniciais (simulando um banco de dados) ---
usuarios = [
    {"id": 1, "nome": "Maria Silva", "email": "maria@email.com"},
    {"id": 2, "nome": "João Souza", "email": "joao@email.com"}
]

produtos = [
    {"id": 1, "nome": "Camiseta", "preco": 29.90, "categoria": "vestuario"},
    {"id": 2, "nome": "Calça Jeans", "preco": 99.90, "categoria": "vestuario"},
    {"id": 3, "nome": "Smartphone", "preco": 1500.00, "categoria": "eletronicos"}
]

# ==================================================
# PARTE 1 – FUNCIONALIDADE: CALCULADORA
# ==================================================

# Rota para a divisão
@app.route('/dividir', methods=['GET'])
def dividir():
    # Pegamos os parâmetros 'a' e 'b' da URL (ex: /dividir?a=10&b=2)
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    # Validação: se não forem números, retornamos um erro.
    if a is None or b is None:
        return jsonify({"erro": "Parâmetros 'a' e 'b' devem ser números."}), 400

    # Tratamento da divisão por zero
    if b == 0:
        return jsonify({"erro": "Divisão por zero não é permitida."}), 400

    # Cálculo e resposta de sucesso
    resultado = a / b
    return jsonify({"resultado": resultado}), 200

# Rota para a multiplicação
@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)

    if a is None or b is None:
        return jsonify({"erro": "Parâmetros 'a' e 'b' devem ser números."}), 400

    resultado = a * b
    return jsonify({"resultado": resultado}), 200

# ==================================================
# PARTE 2 – EXPLORATÓRIO: USUÁRIOS (POST e DELETE)
# ==================================================

# Rota para adicionar um novo usuário (POST)
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    # 1. Verificar se o corpo da requisição é um JSON válido
    if not request.is_json:
        return jsonify({"erro": "Requisição deve ter Content-Type application/json e corpo JSON válido."}), 400

    # 2. Pegar os dados do JSON
    dados = request.get_json()

    # 3. Validar se os campos 'nome' e 'email' existem
    if 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Campos obrigatórios: 'nome' e 'email'."}), 400

    # 4. Criar um novo ID para o usuário
    novo_id = len(usuarios) + 1

    # 5. Montar o novo usuário
    novo_usuario = {
        "id": novo_id,
        "nome": dados['nome'],
        "email": dados['email']
    }

    # 6. Adicionar à lista e retornar sucesso
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201  # 201 = Created

# Rota para deletar um usuário existente (DELETE)
@app.route('/usuarios/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    global usuarios
    # Procurar o usuário pelo ID
    usuario_encontrado = None
    for u in usuarios:
        if u['id'] == user_id:
            usuario_encontrado = u
            break

    # Se não encontrar, retornar erro 404
    if not usuario_encontrado:
        return jsonify({"erro": f"Usuário com ID {user_id} não encontrado."}), 404

    # Remover o usuário da lista
    usuarios = [u for u in usuarios if u['id'] != user_id]
    return jsonify({"mensagem": f"Usuário {user_id} removido com sucesso."}), 200

# ==================================================
# PARTE 3 – REGRESSÃO: PRODUTOS (GET e filtro)
# ==================================================

@app.route('/produtos', methods=['POST'])
def criar_produto():
    if not request.is_json:
        return jsonify({"erro": "Requisição deve ser JSON"}), 400
    dados = request.get_json()
    if 'nome' not in dados or 'preco' not in dados or 'categoria' not in dados:
        return jsonify({"erro": "Campos obrigatórios: nome, preco, categoria"}), 400
    novo_id = len(produtos) + 1
    novo_produto = {
        "id": novo_id,
        "nome": dados['nome'],
        "preco": dados['preco'],
        "categoria": dados['categoria']
    }
    produtos.append(novo_produto)
    return jsonify(novo_produto), 201

# Rota para listar produtos (com filtro opcional por categoria)
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    # Pegar o parâmetro 'categoria' da URL (se existir)
    categoria_filtro = request.args.get('categoria')

    if categoria_filtro:
        # Filtrar a lista de produtos
        produtos_filtrados = []
        for p in produtos:
            if p['categoria'].lower() == categoria_filtro.lower():
                produtos_filtrados.append(p)
        return jsonify(produtos_filtrados), 200

    # Se não tiver filtro, retornar a lista completa
    return jsonify(produtos), 200

# ==================================================
# PARTE 4 – NÃO FUNCIONAL: STATUS
# ==================================================

# Rota simples apenas para verificar se a API está no ar
@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "API operacional"}), 200

# ==================================================
# COMANDO PARA RODAR O SERVIDOR
# ==================================================
if __name__ == '__main__':
    # O servidor vai rodar no seu próprio computador, na porta 5000.
    # debug=True permite que o servidor reinicie automaticamente quando você salvar o arquivo.
    app.run(host='0.0.0.0', port=5000, debug=True)