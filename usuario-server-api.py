from flask import Flask, jsonify

app = Flask(__name__)

# Dados dos usuários
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
    }
]

# Endpoint para obter a lista de usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)
