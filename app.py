from flask import Flask, jsonify
import dotenv
import os
import psycopg2


app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')  

def get_db_conn():
    conn = psycopg2.connect(DATABASE_URL) 
    return conn

@app.route('/api/economic-data/<country>/<year>')
def get_economic_data(country, year):
    conn = get_db_conn()
    cur = conn.cursor()

    sql = """
    SELECT c.name, e.year, p.fertility_rate, e.unemployment_rate
    FROM countries c
    INNER JOIN populations p
    ON c.code = p.country_code
    INNER JOIN economies e
    ON p.year = e.year AND e.code = p.country_code
    WHERE c.code ILIKE %s AND p.year = %s
    """

    cur.execute(sql, (country, year))
    result = cur.fetchone()

    if result is None:
        return jsonify({'error': 'No data found'}), 404

    data = {
        "year": result[1],
        "fertility_rate": result[2],
        "unemployment_rate": result[3]
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
