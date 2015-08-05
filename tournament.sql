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
    (SELECT COUNT(*)
        FROM matches
        WHERE players.id=matches.winner_id)
    AS wins,
    (SELECT COUNT(matches.*)
        FROM matches
        WHERE players.id=matches.winner_id
        OR players.id=matches.loser_id)
    AS matches
    FROM players
    LEFT JOIN matches
    ON players.id=matches.winner_id
    GROUP BY players.id
    ORDER BY wins DESC
);

CREATE VIEW pairings AS (
    SELECT p1.id AS id1,
    p1.name AS name1,
    p2.id AS id2,
    p2.name AS name2
    FROM standings p1,
    standings p2
    WHERE p1.wins = p2.wins
    AND p1.id < p2.id
);