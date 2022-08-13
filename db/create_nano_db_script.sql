CREATE DATABASE IF NOT EXISTS nano;
USE nano;
-- Creation of investor info table
CREATE TABLE IF NOT EXISTS
    investors_info (
        investor_id INTEGER NOT NULL,
        investor_first_name VARCHAR(45) NOT NULL,
        investor_last_name VARCHAR(45) NOT NULL,
        current_score FLOAT NOT NULL,
        crypto_balance FLOAT NOT NULL,
        currency VARCHAR(15) NOT NULL,
        CONSTRAINT PK_trader_info PRIMARY KEY (investor_ID)
    );
-- inserting dummy data
INSERT INTO investors_info
VALUES
(1, 'John', 'Smith', 5.94, 35.28, 'BTC'),
(2, 'Kate', 'Booker', 9.9, 98.01, 'ETH'),
(3, 'Shannon', 'Burton', 13.54, 183.33, 'BNB'),
(4, 'Joshua', 'Medley', 22.3, 497.29, 'XRP'),
(5, 'Tracey', 'James', 9.23, 85.19, 'ETH'),
(6, 'Chris', 'Bailey', 12.93, 167.18, 'ETH');


-- stored procedure to fill data on investors
USE nano;
DELIMITER $$
CREATE DEFINER =`root`@`localhost` PROCEDURE `fillinvestor`
(IN id INTEGER, IN first_name VARCHAR(45), last_name VARCHAR(45), score integer, IN crypto decimal, currency VARCHAR(15))
BEGIN
	INSERT INTO
	    investors_info (
	        investor_id,
	        investor_first_name,
	        investor_last_name,
	        current_score,
	        crypto_balance,
            currency
	    )
	VALUES (
	        id,
	        first_name,
	        last_name,
	        score,
	        crypto,
            currency
	    );

END$$
DELIMITER ;
-- adding a new investor using stored procedure
CALL fillinvestor(7, 'Laura', 'Green', 9, 80.02, 'ETH');