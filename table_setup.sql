DROP TABLE types, abilities, natures, games;

CREATE TABLE IF NOT EXISTS types (
    id INTEGER PRIMARY KEY,
    name VARCHAR(15) UNIQUE
);

CREATE TABLE IF NOT EXISTS abilities (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) UNIQUE,
    game_text TEXT
);

CREATE TABLE IF NOT EXISTS natures (
    id INTEGER PRIMARY KEY,
    name VARCHAR(25) UNIQUE,
    increases VARCHAR(25),
    decreases VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    original_trainer VARCHAR(15),
    trainer_id INTEGER
);

CREATE TABLE IF NOT EXISTS pokemon (
    pokedex_number INTEGER PRIMARY KEY,
    name VARCHAR(50),
    level INTEGER CHECK(level >= 1 AND level <= 100),
    ability VARCHAR(30) REFERENCES abilities(name),
    nature VARCHAR(25) REFERENCES natures(name),
    gender VARCHAR(15),
    nickname VARCHAR(15),
    type_one VARCHAR(15) REFERENCES types(name) NOT NULL,
    type_two VARCHAR(15) REFERENCES types(name),
    origin_game VARCHAR(50) REFERENCES games(name),
    catch_date VARCHAR(15),
    registered_date VARCHAR(15),
    obtained_by VARCHAR(15),
    original_trainer VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS shiny_data (
    pokedex_number INTEGER PRIMARY KEY REFERENCES pokemon(pokedex_number),
    charm BOOLEAN,
    shiny_method VARCHAR(50)
);

