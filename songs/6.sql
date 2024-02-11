SELECT songs.name
FROM songs, artists
WHERE songs.artist_id = artists.id and artists.name like "Post Malone"