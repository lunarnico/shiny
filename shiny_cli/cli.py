import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="shinies",
        user="postgres",
        host="localhost",
        port="5432"
    )

def list_types():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT name FROM types ORDER BY id"

    try:
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            print(f"{row[0]}")

    except psycopg2.Error as e:
        print(f"Database error: {e}")

def main_menu():

    while True:
        print("Nico's Shiny Pokemon Database")
        print("-----------------------------")
        print("1. View Shiny Boosted Pokemon")
        print("2. Increased Nature Count")
        print("3. Ability Word Finder")
        print("4. Add A New Shiny Pokemon")
        print("5. Exit")

        choice = input("Select Your Option: ")

        if choice == '1':
            shiny_boosted()
        elif choice == '2':
           nature_boosted()
        elif choice == '3':
            ability_finder()
        elif choice == '4':
            add_pokemon()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please try again.")

def shiny_boosted():
    print("Shiny Boosted Pokemon")
    print(" ")

    try: 
        conn = get_connection()
        cursor = conn.cursor()

        query = """
                SELECT p.name, p.origin_game, s.shiny_method AS boost_method
                FROM pokemon p
                JOIN shiny_data s ON p.id = s.id
                WHERE s.boost = 'True'
                ORDER BY p.pokedex_number;
                """
        cursor.execute(query)
        results = cursor.fetchall()

        print(f"{'Name':<20} | {'Origin Game':<20} | {'Boost Method':<20}")
        print("-"*60)

        if not results:
            print("No results found.")
        else:
            for row in results:
                print(f"{row[0]:<20} | {row[1]:<20} | {row[2]:<20}")

        print("-"*60)

    except psycopg2.Error as e:
        print(f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

def nature_boosted():
    print("Attack  | Sp. Atk | Speed")
    print("Defense | Sp. Def | ")
    print(" ")
    stat_name = input("Enter A Status: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
                SELECT p.nature, COUNT(n.increases)
                FROM pokemon p 
                JOIN natures n ON p.nature = n.name
                WHERE n.increases ILIKE %s
                GROUP BY p.nature;
                """
        
        cursor.execute(query, ('%' + stat_name + '%',))
        results = cursor.fetchall()

        print(f"\n{'Nature':<10} | {'Count':<10}")
        print("-"*20)

        if not results:
            print("No Natures match")
        else:
            for row in results:
                print(f"{row[0]:<10} | {row[1]:<10}")
        print("-"*60)

    except psycopg2.Error as e:
        conn.rollback()
        print(f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

def ability_finder():
    key_word = input("Enter a Key-Word: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
                SELECT p.name, a.name, a.game_text
                FROM pokemon p
                JOIN abilities a ON p.ability = a.name
                WHERE a.game_text ILIKE %s
                ORDER BY p.pokedex_number;
                """
        
        cursor.execute(query, ('%' + key_word + '%',))
        results = cursor.fetchall()

        print(f"\n{'Name':<20} | {'Ability':<15} | {'Game_Text'}")
        print("-"*100)

        if not results:
            print("Word Not Found in Game Text")
        else:
            for row in results:
                print(f"{row[0]:<20} | {row[1]:<15} | {row[2]:<15}")
        print('-'*100)

    except psycopg2.Error as e:
        conn.rollback()
        print(f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

def add_pokemon():
    print("Add A New Shiny Pokemon!")
    p_dex = input("Enter Pokedex Number: ")
    p_name = input("Enter Pokemon Name: ")
    p_level = input("Enter Level: ")
    p_ability = input("Enter Ability: ")
    p_nature = input("Enter Nature: ")
    p_gender = input("Enter Gender: ")
    p_nickname = input("Enter Nickname: ")
    #print("Types: ")
    #list_types()

    p_t1 = input("Enter Type One: ")
    p_t2 = input("Enter Type Two (or leave blank): ")

    p_og = input("Enter Origin Game: ")
    p_date = input("Enter Catch Date: ")
    p_obtained = input("Enter Obtained By: ")
    p_ot = input("Enter Original Trainer: ")
    p_tid = input("Enter Trainer ID: ")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO pokemon (pokedex_number, name, level, ability, nature, gender, nickname, origin_game, catch_date, obtained_by, original_trainer, trainer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (p_dex, p_name, p_level, p_ability, p_nature, p_gender, p_nickname, p_t1, p_t2, p_og, p_date, p_obtained, p_ot, p_tid)
        )

        conn.commit()
        print("Shiny Pokemon Added Successfully!")

    except psycopg2.Error as e:
        conn.rollback()
        print(f"Database error: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close() 

if __name__ == '__main__':
    main_menu()