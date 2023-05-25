from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Rota GET para buscar dados do banco de dados
@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TAB_REGISTRO')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

# Rota POST para inserir dados no banco de dados
@app.route('/data', methods=['POST'])
def insert_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute('INSERT INTO tabela (NOME, TELEFONE) VALUES (?, ?)', (data['NOME'], data['TELEFONE']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Obrigado pelo registro! '})

if __name__ == '__main__':
    app.run()