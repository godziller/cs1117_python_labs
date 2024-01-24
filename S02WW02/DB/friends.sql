SELECT first_name FROM persons WHERE first_name LIKE 'A%'
SELECT first_name FROM persons WHERE first_name LIKE '%A'
SELECT first_name FROM persons WHERE first_name LIKE '%A%'
SELECT first_name FROM persons WHERE length(first_name) = 5;
SELECT street FROM persons WHERE street LIKE '%street%'
SELECT food FROM likes WHERE food LIKE '% %'
SELECT food FROM likes WHERE food LIKE '%te%'

joins
SELECT * FROM persons NATURAL JOIN likes 
SELECT first_name, food FROM persons NATURAL JOIN likes WHERE person_id = 345678;
SELECT first_name, food FROM persons NATURAL JOIN likes WHERE county LIKE '%Cork%'
SELECT food FROM likes NATURAL JOIN persons WHERE gender LIKE 'F'
SELECT first_name FROM likes NATURAL JOIN persons WHERE food LIKE '%Pizza%'
SELECT town FROM persons NATURAL JOIN likes WHERE food LIKE '%Beer%'
SELECT * FROM likes AS L1 JOIN likes AS L2;

SELECT first_name, last_name FROM persons
WHERE first_name OR last_name LIKE '%r%'

SELECT DISTINCT county, COUNT(*)
FROM persons 
GROUP BY county
ORDER BY county
3
SELECT DISTINCT first_name FROM persons NATURAL JOIN likes 
WHERE food LIKE '%e%'

4
SELECT first_name FROM persons
WHERE person_id IN (
    SELECT friend_id FROM knows
    WHERE person_id IN (
        SELECT person_id FROM persons
        WHERE first_name LIKE '%Aoife%'
    )
)

SELECT first_name FROM persons
EXCEPT
SELECT first_name FROM persons
WHERE person_id IN (
    SELECT person_id FROM knows
    WHERE friend_id IN (
        SELECT person_id FROM persons
        WHERE first_name LIKE '%Aoife%'
    )
)


SELECT first_name FROM persons
WHERE person_id IN (
    SELECT friend_id FROM knows
    WHERE person_id IN (
        SELECT person_id FROM persons
        WHERE first_name LIKE '%Aoife%' 
    )
)
INTERSECT
SELECT first_name FROM persons
WHERE person_id IN (
    SELECT friend_id FROM knows
    WHERE person_id IN (
        SELECT person_id FROM persons
        WHERE first_name LIKE '%Declan%' 
    )
)


SELECT food AS most_popular_food FROM likes
GROUP BY food 

SELECT food, COUNT(*)
FROM persons JOIN Likes ON persons.person_id = likes.person_id
WHERE county = 'Cork'
GROUP BY food
ORDER BY COUNT(*) DESC;

SELECT county, COUNT(*)
FROM persons JOIN likes ON persons.person_id = likes.person_id
GROUP BY persons.county, likes.food
HAVING COUNT (*) >= 3

SELECT DISTINCT first_name, last_name FROM persons
WHERE person_id IN (
    SELECT person_id FROM likes 
    WHERE food LIKE '%e%'
)

SELECT first_name FROM persons
WHERE person_id IN (
    SELECT person_id FROM knows 
    WHERE friend_id IN (
        SELECT person_id FROM persons
        WHERE first_name LIKE '%Aoife%'
    )
)

SELECT first_name FROM persons
EXCEPT
SELECT first_name FROM persons
WHERE person_id IN (
    SELECT person_id FROM knows 
    WHERE friend_id IN (
        SELECT person_id FROM persons
        WHERE first_name LIKE '%Aoife%'
    )
)


SELECT first_name FROM persons
WHERE person_id IN (
    SELECT person_id FROM knows 
    WHERE friend_id IN (
        SELECT person_id FROM persons
        WHERE first_name LIKE '%Aoife%'
    )
)
INTERSECT
SELECT first_name FROM persons
WHERE person_id IN (
    SELECT person_id FROM knows 
    WHERE friend_id IN (
        SELECT person_id FROM persons
        WHERE first_name LIKE '%Declan%'
    )
)

SELECT first_name, MAX(birth_date) AS AGE FROM persons
UNION
SELECT first_name, MIN(birth_date) FROM persons