-- Create a table called users following some requirement

CREATE TABLE IF NOT EXISTS users (
  id INT PRIMARY KEY AUTOINCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  PRIMARY KEY (id)
);
