SELECT  distinct people.name
FROM movies, stars, people
WHERE movies.id = stars.movie_id and stars.person_id = people.id and movies.year = 2004
ORDER BY people.birth;