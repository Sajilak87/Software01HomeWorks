import mysql.connector


def get_airports_by_country(country_code):

    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',  # use your actual DB name
        user='root',
        password='password',
        autocommit=True
    )

    cursor = connection.cursor()

    query = """
            SELECT type, COUNT(*)
            FROM airport
            WHERE iso_country = %s
            GROUP BY type
            ORDER BY type; \
            """
    cursor.execute(query, (country_code,))

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()
    airports = get_airports_by_country(country_code)

    print(f"\nAirports in {country_code}:")
    for airport_type, count in airports:
        print(f"{count} {airport_type} airports")


# Run the program
run_country_program()