SELECT * FROM students;
UPDATE students SET points = 550 WHERE id_number = 112345678;
UPDATE students SET date_of_birth = '2001-06-13', hometown = 'Tahiti' WHERE id_number = 112836467;
INSERT INTO students VALUES ('112713281', 'Grainne', 'Goggin', '2001-11-21', 'Kenmare', 'ck401', '590' );
INSERT INTO students VALUES ('112938299', 'Hugh', 'Hegarty', NULL, NULL, NULL, NULL);
UPDATE students SET date_of_birth = '2002-01-04', hometown = 'Fermoy', course = 'ck402', points = '465' WHERE id_number = 11293829;

INSERT INTO students
VALUES 
('112382931', 'Michael','Myers', '2002-04-13', 'Boston', 'ck401', '295'), 
('112183923', 'Bruce','Wayne', '2002-11-28', 'Dublin', 'ck405', '155'),
('112392914', 'Steven','Hawkings', '2003-02-01', 'London', 'ck401', '235'), 
('112192391', 'Sarah','Haras', '2004-10-18', 'Belfast', 'ck402', '200');

DELETE FROM students WHERE points <= '300';

INSERT INTO students VALUES ('112713281', 'Grainne', 'Dummy', '2001-11-21', 'Kenmare', 'ck401', '590' );

INSERT INTO students VALUES ('112932099', 'Hugh', 'Hegarty', NULL, NULL, NULL, NULL);

DELETE FROM students WHERE id_number = 112932099;

