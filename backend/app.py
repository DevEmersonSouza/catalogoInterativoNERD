from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Configurações de conexão com o banco de dados
db_config = {
    'host': 'srv642.hstgr.io',
    'user': 'u799757764_teste',
    'password': 'Testeloja123',
    'database': 'u799757764_teste'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/shirts', methods=['GET'])
def get_shirts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM shirts')
    shirts = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(shirts)

@app.route('/colors/<shirt_type>', methods=['GET'])
def get_colors(shirt_type):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = 'SELECT * FROM colors WHERE shirt_type = %s'
    cursor.execute(query, (shirt_type,))
    colors = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(colors)

if __name__ == '__main__':
    app.run(debug=True)