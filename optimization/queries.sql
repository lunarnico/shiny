-- Selecting which of my Shiny Pokemon have an ability that can increase its speed
-- 'speed' will be replaced with user input
EXPLAIN SELECT p.name, a.name, a.game_text
FROM pokemon p
JOIN abilities a ON p.ability = a.name
WHERE a.game_text ILIKE '%speed%'
ORDER BY p.pokedex_number; 

CREATE INDEX IF NOT EXISTS idx_speed
ON pokemon (ability);

CREATE INDEX IF NOT EXISTS idx_ability
ON abilities (name);

CREATE INDEX IF NOT EXISTS idx_gametext
ON abilities (game_text);

CREATE INDEX IF NOT EXISTS idx_dex
ON pokemon (pokedex_number);

CREATE INDEX IF NOT EXISTS idx_name
ON pokemon (name);

-- Selecting how many of my Shiny Pokemon have Attack boosting natures
-- 'Attack' will be replaced with user input
EXPLAIN SELECT p.nature, COUNT(n.increases)
FROM pokemon p 
JOIN natures n ON p.nature = n.name
WHERE n.increases = 'Attack'
GROUP BY p.nature;

CREATE INDEX IF NOT EXISTS idx_natures
ON pokemon (nature)

CREATE INDEX IF NOT EXISTS idx_n
ON natures (name);

-- Selecting the Pokemon name, origin game and shiny boost method 
EXPLAIN SELECT p.name, p.origin_game, s.shiny_method AS boost_method
FROM pokemon p
JOIN shiny_data s ON p.id = s.id
WHERE s.boost = 'True';

CREATE INDEX IF NOT EXISTS idx_id
ON pokemon (id);

-- Selecting the game name and how many pokemon are
-- shiny boosted in those games
EXPLAIN SELECT g.name, COUNT(s.shiny_method)
FROM games g
JOIN pokemon p ON g.name = p.origin_game
JOIN shiny_data s ON p.id = s.id
WHERE s.boost = 'True'
GROUP BY g.name;

CREATE INDEX IF NOT EXISTS idx_games
ON games (name);

CREATE INDEX IF NOT EXISTS idx_og
ON pokemon (origin_game);

CREATE INDEX IF NOT EXISTS idx_boost
ON shiny_data (boost);