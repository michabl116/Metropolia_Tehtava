
from flask import Flask,jsonify, abort
import  mysql.connector
app =Flask(__name__)
@app.route('/kenttä/<kodi>', methods=['GET'])
def lentokenta(kodi):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='',
        password='1Peru20243#',
        autocommit=True
    )
    cursor = connection.cursor()
    vastaus = "SELECT  ident, name, municipality  FROM airport where ident = %s"
    cursor.execute(vastaus, (kodi.upper(),))
    result = cursor.fetchone()

    connection.close()
    if result:
        return ({
            "ICAO": result[0],
            "Name": result[1],
            "Municipality": result[2]
        })

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)


