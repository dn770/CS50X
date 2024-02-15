SELECT people.name
FROM movies, stars, people
WHERE movies.id = stars.movie_id and stars.person_id = people.id and movies.title like "Toy Story";