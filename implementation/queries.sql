-- Count how many of my Pokemon are male, female and unknown
SELECT gender, COUNT(gender)
FROM pokemon
GROUP BY gender;

-- Selecting which of my Shiny Pokemon have an ability that can increase its speed
SELECT p.name, a.name, a.game_text
FROM pokemon p
JOIN abilities a ON p.ability = a.name
WHERE a.game_text ILIKE '%speed%'
ORDER BY p.pokedex_number; 

-- Selecting how many of my Shiny Pokemon have Attack boosting natures
SELECT p.nature, COUNT(n.increases)
FROM pokemon p 
JOIN natures n ON p.nature = n.name
WHERE n.increases = 'Attack'
GROUP BY p.nature;

-- Selecting the Pokemon name, origin game and shiny boost method 
SELECT p.name, p.origin_game, s.shiny_method AS boost_method
FROM pokemon p
JOIN shiny_data s ON p.id = s.id
WHERE s.boost = 'True';

