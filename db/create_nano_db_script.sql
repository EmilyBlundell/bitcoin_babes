CREATE DATABASE nano;

USE nano;

-- Creation of investor info table
--
CREATE TABLE investors_info (
investor_id INTEGER NOT NULL,
investor_first_name VARCHAR(45) NOT NULL,
investor_last_name VARCHAR(45) NOT NULL,
current_score INTEGER NOT NULL,
crypto_balance DECIMAL NOT NULL,
CONSTRAINT PK_trader_info PRIMARY KEY (investor_ID));

-- inserting dummy data
INSERT INTO investors_info
VALUES
(1,'John','Smith', 6, 600),
(2, 'Kate', 'Booker', 9, 900),
(3, 'Shannon', 'Burton', 7, 700),
(4, 'Joshua', 'Medley', 4, 400),
(5, 'Tracey', 'James', 3, 300),
(6, 'Chris', 'Bailey', 2, 200);

-- stored procedure to fill data on investors

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `fillinvestor`(IN id INTEGER, IN first_name VARCHAR(45), last_name VARCHAR(45), score integer, IN crypto decimal )
BEGIN
    INSERT INTO investors_info (investor_id, investor_first_name, investor_last_name, current_score, crypto_balance)
    VALUES (id, first_name, last_name, score, crypto);
END$$
DELIMITER ;

-- adding a new investor using stored procedure
CALL fillinvestor(7, 'Laura', 'Green', 9, 900);
Footer
