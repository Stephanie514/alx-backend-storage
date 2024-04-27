-- SQL script that creates a table users following these requirements:
--With these attributes:
--id, integer, never null, auto increment and primary key
--email, string (255 characters), never null and unique

CREATE TABLE IF NOT EXISTS users(
	id int PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
	);
