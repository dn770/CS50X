SELECT  people.name
FROM  movies, people, stars
WHERE movies.id = stars.movie_id and stars.person_id = people.id and people.name not like "Kevin Bacon" and  movies.id in (

    SELECT  movies.id
    FROM  movies, people, stars
    WHERE movies.id = stars.movie_id and stars.person_id = people.id and people.name LIKE "Kevin Bacon" and people.birth = 1958
);