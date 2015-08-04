-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS matches (
    id SERIAL PRIMARY KEY,
    winner_id INT NOT NULL REFERENCES players(id),
    loser_id INT NOT NULL REFERENCES players(id)
);

CREATE VIEW standings AS (
    SELECT players.id,
    players.name,
    COUNT(players.name) AS wins
    FROM players, matches
    WHERE players.id = matches.winner_id
    GROUP BY players.id
    ORDER BY wins DESC
);