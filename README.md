game_tournament - v1.0 08-05-2015
===================================

A database to hold participants in a Swiss-style tournament, record and store their matches, and pair them into fair matches according to their win/loss standings.

Pre-requisites
--------------

- [Git]()
- [VirtualBox](https://www.virtualbox.org/)
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrant virtual machine](https://www.udacity.com/wiki/ud088/vagrant)

Getting Started
---------------

1. Follow the [guide](https://www.udacity.com/wiki/ud088/vagrant) to get the udacity VM cloned to your computer

2. Clone [this repo](https://github.com/Drkeenbean/game_tournament) into your vagrant directory

3. Navigate to your vagrant folder from the terminal/command prompt and run `vagrant up` to boot your Vagrant VM.

4. Connect to your Vagrant VM with `vagrant ssh`. If you are on Windows you can use [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/) to connect and login with username `vagrant` and password `vagrant`

Setting up the database
---------------

1. Once connected to your Vagrant VM, enter `psql` to enter the PostgreSQL command line

2. Run `CREATE DATABASE tournament;` to create the tournament database

3. Run `\c tournament` to connect to your newly-created tournament database

4. Run `\i tournament.sql` to create the necessary tables and views for the application to work

5. Exit out of psql with `\q`

Running the application
---------------

1. Navigate to the cloned tournament directory created from cloning this repo and run `python tournament_test.py`

2. Make note: HUGE SUCCESS

Download
-------
- [Version 1.0](https://github.com/Drkeenbean/game_tournament/master.zip)
