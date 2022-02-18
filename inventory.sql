CREATE DATABASE fablab;
USE fablab;

CREATE TABLE tool
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nom VARCHAR(100),
    quantity INT,
    space VARCHAR(100),
    price FLOAT
);

INSERT INTO plant (id,nom, brightness,humidity,temperature) VALUES (1,'hammer', 3, 'shelf-3', 19);
INSERT INTO plant (nom, brightness,humidity,temperature) VALUES ('scissors', 2, 'box-1', 5);