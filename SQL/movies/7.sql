SELECT title, rating
FROM movies, ratings
WHERE movies.id = ratings.movie_id and movies.year = 2010
ORDER BY rating desc, title;