SELECT name FROM countries WHERE region = "Europe" ORDER BY population;
SELECT * FROM countries;
SELECT DISTINCT region FROM countries ORDER BY region;
SELECT name,region FROM countries ORDER BY region;
SELECT name,gdp FROM countries WHERE gdp IS NULL;
SELECT name,region FROM countries WHERE region LIKE '%Asia%';
SELECT name,region FROM countries WHERE region LIKE '%North%' OR region LIKE '%South%';
SELECT name FROM countries WHERE name LIKE '%stan%';
SELECT name FROM countries WHERE name LIKE '%x%' OR name LIKE '%y%' OR name LIKE '%z%';
SELECT name, gdp/population as PERCAPITA FROM countries WHERE PERCAPITA IS NOT NULL AND PERCAPITA >= 25000;

LAB 3
SELECT * FROM countries;
SELECT MAX(area), name FROM countries;
SELECT MAX(population), name FROM countries WHERE region LIKE '%Africa%';
SELECT SUM(gdp) FROM countries WHERE region LIKE '%Europe%';
SELECT name, population FROM countries WHERE gdp IS NULL;
SELECT gdp, name FROM countries WHERE gdp IS NOT NULL;
SELECT name FROM countries WHERE name LIKE SUBSTRING(region);