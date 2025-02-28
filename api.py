from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect("KOHVIKUD.db")
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/kohvikud', methods=['GET'])
def get_all_kohvikud():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SOOKLA")
    kohvikud = cursor.fetchall()
    conn.close()
    return jsonify([dict(k) for k in kohvikud])

@app.route('/kohvikud/avamisaeg', methods=['GET'])
def get_kohvikud_by_time_range():
    start_time = request.args.get('start', '00:00')
    end_time = request.args.get('end', '23:59')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM SOOKLA 
        WHERE TIME(time_open) <= TIME(?) 
        AND TIME(time_closed) >= TIME(?)""",
        (start_time, end_time))
    kohvikud = cursor.fetchall()
    conn.close()
    return jsonify([dict(k) for k in kohvikud])

@app.route('/kohvikud', methods=['POST'])
def add_kohvik():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO SOOKLA (NAME, LOCATION, PROVIDER, time_open, time_closed) VALUES (?, ?, ?, ?, ?)",
                   (data['name'], data['location'], data['provider'], data['time_open'], data['time_closed']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Kohvik lisatud!"}), 201

@app.route('/kohvikud/<int:kohvik_id>', methods=['PUT'])
def update_kohvik(kohvik_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE SOOKLA SET NAME=?, LOCATION=?, PROVIDER=?, time_open=?, time_closed=? WHERE ID=?",
                   (data['name'], data['location'], data['provider'], data['time_open'], data['time_closed'], kohvik_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Kohvik uuendatud!"})

@app.route('/kohvikud/<int:kohvik_id>', methods=['DELETE'])
def delete_kohvik(kohvik_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM SOOKLA WHERE ID=?", (kohvik_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Kohvik kustutatud!"})

if __name__ == '__main__':
    app.run(debug=True)
