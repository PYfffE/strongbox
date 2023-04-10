CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
	username VARCHAR ( 50 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL
);

CREATE TABLE IF NOT EXISTS stored_passwords (
	id VARCHAR ( 50 ) UNIQUE NOT NULL,
	username_id VARCHAR ( 50 ) NOT NULL,
	site VARCHAR (50) NOT NULL,
	username VARCHAR (50) NOT NULL,
	password VARCHAR ( 50 ) NOT NULL
);

CREATE SEQUENCE useq start 1 increment 1;


INSERT INTO users
  (id, username, password)
  VALUES
    (nextval('useq'),'admin', 'c1489d720e7c2c7ffa1c33eb613a328fd7d08991');

INSERT INTO stored_passwords
	(id, username_id, site, username, password)
	VALUES
	('deadbeef', 'admin', '192.168.1.1', 'admin', 'FLAG{RealFlag}')
