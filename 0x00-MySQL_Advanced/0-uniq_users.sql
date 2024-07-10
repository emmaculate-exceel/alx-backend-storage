-- Create a table called users following some requirement

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL ,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  PRIMARY KEY (id)
);
