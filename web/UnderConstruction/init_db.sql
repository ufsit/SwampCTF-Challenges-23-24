ALTER USER 'root'@'localhost' IDENTIFIED BY 'PasswordMomento!!!';

CREATE DATABASE ctf_challenge;
USE ctf_challenge;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'admin');
