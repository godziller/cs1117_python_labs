SELECT name, population FROM cities 
ORDER by population DESC
LIMIT 20

SELECT name AS occ FROM countries
    WHERE code IN (
        SELECT country_code FROM cities
            WHERE population > 1000000
            GROUP BY country_code
    )


SELECT COUNT(cities.name), countries.name
FROM countries JOIN cities 
ON cities.country_code=countries.code
WHERE cities.population >= 1000000
GROUP BY countries.name
HAVING COUNT(cities.name)>=5

SELECT name FROM countries 
WHERE indep_year >(
    SELECT indep_year FROM countries

SELECT countries.name, cities.name FROM countries 
JOIN cities ON countries.code = cities.country_code
WHERE COUNT(cities.population)>=1000000)

SELECT language FROM country_languages
HAVING COUNT(country_code) >= 5
WHERE country_code


SELECT  name,surface_area FROM countries
    WHERE surface_area IN (
        SELECT SUM(surface_area) AS sum FROM countries
        WHERE continent LIKE 'South America'
)

SELECT COUNT(cities.name) FROM cities
    JOIN cities ON countries.country_code = cities.country_code


--------------------------------------------- attempt2

SELECT name, population FROM cities 
ORDER BY population DESC
LIMIT(10)

SELECT COUNT(cities.name), countries.name FROM cities
JOIN countries ON cities.country_code = countries.code
WHERE cities.population>= 1000000   
GROUP BY countries.name
HAVING COUNT(cities.name)>=5

SELECT name, surface_area  FROM countries  
    WHERE continent LIKE 'South America'  AND surface_area >= (
        SELECT SUM(surface_area) * 0.10  FROM countries
            WHERE continent LIKE 'South America'    
)

