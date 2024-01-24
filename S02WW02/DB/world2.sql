SELECT name, population FROM cities 
LIMIT 20

SELECT COUNT(cities.name), countries.name FROM cities
JOIN countries ON cities.country_code = countries.code
WHERE cities.population>= 1000000   
GROUP BY countries.name
HAVING COUNT(cities.name)>=5

