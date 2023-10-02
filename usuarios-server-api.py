from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados dos usuários.
usuarios = [
    {
        "UserID": 1,
        "Nome": "João",
        "Perfil": "Administrador",
        "Mensagem": "Acredite em você e em suas habilidades!",
        "ID": "ID001"
    },
    {
        "UserID": 2,
        "Nome": "Maria",
        "Perfil": "Usuário",
        "Mensagem": "O sucesso começa com a determinação.",
        "ID": "ID002"
    },
    {
        "UserID": 3,
        "Nome": "Carlos",
        "Perfil": "Moderador",
        "Mensagem": "Você é capaz de superar qualquer desafio.",
        "ID": "ID003"
    },
    {
        "UserID": 4,
        "Nome": "Ana",
        "Perfil": "Usuário",
        "Mensagem": "Lembre-se de que cada dia é uma nova oportunidade.",
        "ID": "ID004"
    },
    {
        "UserID": 5,
        "Nome": "Pedro",
        "Perfil": "Convidado",
        "Mensagem": "Nunca subestime seu próprio potencial.",
        "ID": "ID005"
    },
    {
        "UserID": 6,
        "Nome": "tecnicoZ",
        "Perfil": "formatador de PC",
        "Mensagem": "Seja seu melhor.",
        "ID": "ID006"
    },
    {
        "UserID": 7,
        "Nome": "t",
        "Perfil": "formatador de PC",
        "Mensagem": "Seja seu melhor.",
        "ID": "ID007"
    }
]


# Endpoint para obter a lista de usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)


# Endpoint para atualizar um usuário por UserID
@app.route('/usuarios/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    # Procurar o usuário pelo UserID
    usuario_para_atualizar = None
    for usuario in usuarios:
        if usuario["UserID"] == user_id:
            usuario_para_atualizar = usuario
            break

    if usuario_para_atualizar is None:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404

    # Obter dados da solicitação PUT
    dados_atualizados = request.json
    if "Nome" in dados_atualizados:
        usuario_para_atualizar["Nome"] = dados_atualizados["Nome"]
    if "Perfil" in dados_atualizados:
        usuario_para_atualizar["Perfil"] = dados_atualizados["Perfil"]
    if "Mensagem" in dados_atualizados:
        usuario_para_atualizar["Mensagem"] = dados_atualizados["Mensagem"]

    return jsonify({"mensagem": "Usuário atualizado com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
