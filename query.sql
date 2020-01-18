-- Query to check successful load
SELECT * FROM Kaggle_CSV;

SELECT * FROM MLB_API;

-- Join tables on team_name
SELECT Kaggle_CSV.id, Kaggle_CSV.year, Kaggle_CSV.attendance, MLB_API.city, MLB_API.venue
FROM Kaggle_CSV
INNER JOIN team_name
ON Kaggle_CSV.team_name = MLB_API.team_name;
