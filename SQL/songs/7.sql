SELECT AVG(songs.energy)
FROM songs, artists
WHERE songs.artist_id = artists.id and artists.name like "Drake"