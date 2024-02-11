SELECT  movies.title
FROM  movies, people, stars
WHERE movies.id = stars.movie_id and stars.person_id = people.id and people.name LIKE "Johnny Depp"
INTERSECT
    SELECT  movies.title
    FROM  movies, people, stars
    WHERE movies.id = stars.movie_id and stars.person_id = people.id and people.name LIKE "Helena Bonham Carter"
;

