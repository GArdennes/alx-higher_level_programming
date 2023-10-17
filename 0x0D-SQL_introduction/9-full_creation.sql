-- A script that creates a table second_table
CREATE TABLE IF NOT EXISTS second_table (
	id INT NOT NULL,
	name VARCHAR(254) NOT NULL,
	score INT NOT NULL
);

INSERT INTO second_table(id, name, score) VALUES (1, 'John', 10)
INSERT INTO second_table(id, name, score) VALUES (2, 'Alex', 3)
INSERT INTO second_table(id, name, score) VALUES (3, 'Bob', 14)
INSERT INTO second_table(id, name, score) VALUES (4, 'George', 8)
