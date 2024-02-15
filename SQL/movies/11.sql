SELECT movies.title
FROM  movies, people , ratings, stars
WHERE movies.id = ratings.movie_id and movies.id = stars.movie_id and stars.person_id = people.id and people.name LIKE "Chadwick Boseman"
ORDER BY ratings.rating
DESC LIMIT 5;