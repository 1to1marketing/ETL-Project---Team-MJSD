-- Create Two Tables
CREATE TABLE Kaggle_CSV (
  id INT PRIMARY KEY,
  team_name TEXT,
  year int,
  attendance int
);

CREATE TABLE MLB_API (
  id serial PRIMARY KEY,
  team_name TEXT,
  city TEXT,
  venue TEXT,
  year int
);
