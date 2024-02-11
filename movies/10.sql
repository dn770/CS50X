SELECT  distinct people.name
FROM  directors, people , ratings
WHERE directors.movie_id = ratings.movie_id and directors.person_id = people.id and ratings.rating >= 9.0;