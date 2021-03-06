#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def commit_close(database):
    """Commit database changes and close connection

    Args:
      database: the connection to commit & close.
    """
    database.commit()
    database.close()


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    database = connect()
    c = database.cursor()
    c.execute("DELETE FROM matches")
    commit_close(database)


def deletePlayers():
    """Remove all the player records from the database."""
    database = connect()
    c = database.cursor()
    c.execute("DELETE FROM players")
    commit_close(database)


def countPlayers():
    """Returns the number of players currently registered."""

    database = connect()
    c = database.cursor()
    c.execute("SELECT COUNT(*) AS count FROM players")
    player_count = c.fetchone()[0]
    commit_close(database)

    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    name = bleach.clean(name)

    database = connect()
    c = database.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    commit_close(database)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    database = connect()
    c = database.cursor()
    c.execute("SELECT * FROM standings")
    standings = c.fetchall()
    commit_close(database)

    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    database = connect()
    c = database.cursor()
    c.execute("INSERT INTO matches (winner_id, loser_id) \
        VALUES (%s, %s)", (winner, loser,))
    commit_close(database)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    database = connect()
    c = database.cursor()
    c.execute("SELECT * FROM pairings")
    pairings = c.fetchall()
    commit_close(database)

    return pairings
