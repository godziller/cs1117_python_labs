SELECT id, name FROM actors WHERE id
= (SELECT id FROM movies WHERE title LIKE '%Big Sleep, The%')

SELECT title FROM movies WHERE director 
= (SELECT director FROM movies WHERE title LIKE '%Citizen Kane%')

SELECT name FROM actors WHERE id = 
(SELECT actorid FROM castings WHERE movieid  584)

SELECT movieid FROM castings WHERE movieid =
(SELECT id FROM movies WHERE yr < 1950 OR)

SELECT name FROM actors 
WHERE id IN (
    SELECT actorid FROM castings 
    WHERE movieid = (
           SELECT id FROM movies 
           WHERE title LIKE '%Big Sleep, The%'
    )
)

SELECT title FROM movies WHERE id IN (
    SELECT movieid FROM castings 
    WHERE actorid IN (
        SELECT id FROM actors 
        WHERE name LIKE '%Elizabeth Taylor%'
    )
)
UNION 
SELECT title FROM movies WHERE yr < 1950;

        
SELECT title FROM movies 
WHERE score = (
    SELECT MAX(score) FROM movies
);


SELECT actorid, COUNT(actorid) as occurances FROM castings
GROUP BY actorid 
HAVING occurances >= 10;

SELECT name,actorid, COUNT(actorid) as occurances FROM actors JOIN castings 
ON castings.actorid = actors.id
GROUP BY actorid 
HAVING occurances >= 10;

SELECT id, SUM(score)/10*100 AS percentage  FROM movies 
GROUP BY id 
ORDER BY MAX(score) DESC 
RETURN TO QUESTION 8


SELECT name FROM actors 
WHERE id IN (
    SELECT actorid FROM castings 
    WHERE movieid IN (
       SELECT id FROM movies
       WHERE score <= 3.0
    )
)

SELECT title , MAX(score) FROM movies 
UNION
SELECT title, MIN(score) FROM movies


SELECT title, yr FROM movies 
WHERE yr < (
    SELECT yr FROM movies 
    WHERE title LIKE '%Citizen Kane%'
)

SELECT title, yr FROM movies 
WHERE yr <= (
    SELECT MIN(yr) FROM movies 
    WHERE director IN (
        SELECT director FROM movies 
        WHERE title LIKE '%Citizen Kane%'
    )
)

SELECT title, score FROM movies 
WHERE yr >= 1940
INTERSECT
SELECT  score FROM movies 
WHERE score = (
    SELECT MAX(score) FROM movies
    WHERE yr = 1940, score > MAX(SCORE)
)

SELECT title FROM movies 
WHERE score = (
    SELECT SUM(score > MAX(score)) as max_score FROM movies
    WHERE 
)


13
SELECT title FROM movies
WHERE id IN (
    SELECT movieid FROM castings
    WHERE actorid IN (
        SELECT id FROM actors
        WHERE name LIKE '%Clint Eastwood%'
    )
)
INTERSECT 
SELECT title FROM movies
WHERE id IN (
    SELECT movieid FROM castings
    WHERE actorid IN (
        SELECT id FROM actors
        WHERE name LIKE '%Richard Burton%'
    )
)

SELECT name FROM actors
WHERE id IN (
    SELECT actorid FROM castings 
    WHERE movieid IN (
        SELECT movieid FROM castings
        WHERE actorid IN (
            SELECT id FROM actors
            WHERE name LIKE 'Al Pacino'
        )
    )
)

SELECT director, MAX(id) FROM movies
WHERE id = (
SELECT COUNT(id) FROM movies
GROUP BY director
ORDER BY director
)


16

SELECT director FROM (
SELECT MAX(my_count) FROM actors
FROM
( 
    SELECT COUNT(title) AS my_count FROM movies
    GROUP BY director
    ORDER BY director
)
)

SELECT di rector, MAX(my_count) FROM movies
WHERE title IN (
    SELECT COUNT(title) FROM movies 
)