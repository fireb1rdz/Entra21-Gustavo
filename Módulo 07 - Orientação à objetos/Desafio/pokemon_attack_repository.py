from typing import Any, List
import sqlite3
from pokemon import Pokemon
from attack import Attack

class PokemonAttackRepository:
    
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def __execute_query(self, query: str, *params: Any) -> None:
        """Executes a query in the database.
        
            Args:
                query (str): Query that will be executed.
                params (Any): Query parameters.
        """
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()
    
    def __execute_select_query(self, query: str, *params: Any) -> List[Attack]:
        """Executes a query in the database and returns a list with Attack objects.
        
            Args:
                query (str): Query that will be executed.
                params (Any): Query parameters.

            Returns:
                List[Attack]: A list with matched attacks
        """
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        connection.close()
        return [Attack(row[0], row[1], row[2], row[3]) for row in rows]
    
    def insert_pokemon_attack_relation(self, id, pokemon_id: int, attack_id: int) -> None:
        """Insert the relation pokemon x attack in the pokemons_attacks table.
        
            Args:
                pokemon_id (int): The pokemons' id.
                attack_id (int): The attack's id.
        """
        query = "INSERT INTO pokemons_attacks (id, pokemon_id, attack_id) VALUES (?, ?, ?)"
        self.__execute_query(query, id, pokemon_id, attack_id)

    def get_attacks_by_pokemon_id(self, pokemon: Pokemon) -> List[Attack]:
        """Gets attack objects from database according to the referred pokemon.
        
            Args:
                pokemon_id (int): The pokemons' id.
                attack_id (int): The attack's id.
            
            Returs:
                List[Attacks]: A list with matched attacks.
        """
        query = "SELECT attacks.id, attacks.name, attacks.damage, attacks.type FROM attacks INNER JOIN pokemons_attacks ON attacks.id = pokemons_attacks.attack_id INNER JOIN pokemons ON pokemons.id = pokemons_attacks.pokemon_id WHERE pokemon_id = ?"
        return self.__execute_select_query(query, pokemon.id)
