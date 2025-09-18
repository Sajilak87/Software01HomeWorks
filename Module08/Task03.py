import mysql.connector
from geopy.distance import geodesic


def get_airport_coordinates(icao_code):

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',  # use your actual DB name
        user='root',
        password='password',
        autocommit=True
    )

    cursor = connection.cursor()

    # Query to get coordinates
    query = """
            SELECT latitude_deg, longitude_deg
            FROM airport
            WHERE ident = %s; \
            """
    cursor.execute(query, (icao_code,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return (float(result[0]), float(result[1]))
    else:
        return None


def run_airport_distance():
    icao1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)

    if coords1 and coords2:
        distance_km = geodesic(coords1, coords2).kilometers
        print(f"\nDistance between {icao1} and {icao2}: {distance_km:.2f} kilometers")
    else:
        print("One or both ICAO codes not found in the database.")



run_airport_distance()