# This program creates a database called 'population_JPS' and a table named 'population' with the
# following fields: city, year, and population. Population uses the 2023 population of ten cities in Florida.
# This program further simulates population growth for the next twenty years at 2% growth / year,
# which is then added to the table. The program queries the user for one of the ten cities, and then
# displays the population growth visually using matplotlib.

import sqlite3
import matplotlib.pyplot as plt


# Population data taken from census.gov website (using 2023 estimates).
population_data = {
    'Miami': 455924,
    'Orlando': 320742,
    'Tampa': 403364,
    'Jacksonville': 985843,
    'Tallahassee': 202221,
    'Naples': 19704,
    'Daytona Beach': 82485,
    'St. Petersburg': 263553,
    'Sarasota': 57602,
    'Pensacola': 53724
}


def create_database():
    conn = sqlite3.connect('population_JPS.db')
    cursor = conn.cursor()

    # Drop 'population' table if it exists to prevent math errors & data duplication.
    cursor.execute('DROP TABLE IF EXISTS population')

    # Create 'population' table.
    cursor.execute('''
        CREATE TABLE population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')

    # Insert 2023 population data.
    for city, pop in population_data.items():
        cursor.execute('''
            INSERT INTO population (city, year, population) VALUES (?, ?, ?)
        ''', (city, 2023, pop))

    # Simulate growth for the next 20 years at 2% growth per year
    for city, initial_pop in population_data.items():
        current_pop = initial_pop
        for year in range(2024, 2044):
            current_pop = int(current_pop * 1.02)
            cursor.execute('''
                INSERT INTO population (city, year, population) VALUES (?, ?, ?)
            ''', (city, year, current_pop))

    conn.commit()
    conn.close()


def query_city(city):
    # Query the database for the population data of the city selected by the user.
    conn = sqlite3.connect('population_JPS.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT year, population FROM population WHERE city = ?
    ''', (city,))
    results = cursor.fetchall()
    conn.close()
    return results


# Plot the population growth of the city selected by the user.
def plot_population_growth(city, data):
    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker='o', linestyle='-', color='b')
    plt.title(f'Population Growth for {city}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.grid(True)
    plt.xticks(years, rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    create_database()
    # Loop for valid city input. If city is not in the list, the user is prompted to try again.
    while True:
        selected_city = input(
            f"Enter the name of one of the following ten cities:\n{', '.join(population_data.keys())}\n")
        if selected_city in population_data:
            break
        else:
            print("City not available. Please try again.\n")

    data = query_city(selected_city)
    plot_population_growth(selected_city, data)

    print("Final estimated population for 2043:", query_city(selected_city)[-1][1])


if __name__ == '__main__':
    main()
