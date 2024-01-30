How the tables or relations were built and data imported in Postgres:

STEPS:

1. We created a new database on PostgreSQL named 'CSE560_Project_Football'
2. The we executed the create.sql file to create the football related tables/relations, also this file contains commands to
alter the table's foreign key, primary keys and etc.
3. Added all the cleaned csv files on a new folder on Mac.
4. Opened the PSQL tool by right clicking on the newly created database.
5. Used these PSQL commands in the PSQL tool/terminal to copy the data from the CSV files to the corresponding tables/relations in the database.

Commands:

a) Games Table - \copy games FROM '/Users/pranavbellamprasad/Downloads/Football/games_cleaned.csv' WITH CSV HEADER;
b) Leagues Table - \copy leagues FROM '/Users/pranavbellamprasad/Downloads/Football/leagues_cleaned.csv' WITH CSV HEADER;
c) Players Table - \copy players FROM '/Users/pranavbellamprasad/Downloads/Football/players_cleaned.csv' WITH CSV HEADER
d) Teams Table - \copy teams FROM '/Users/pranavbellamprasad/Downloads/Football/teams_cleaned.csv' WITH CSV HEADER
e) Shots Table - \copy shots FROM '/Users/pranavbellamprasad/Downloads/Football/shots_cleaned.csv' WITH CSV HEADER
f) Team Stats Table - \copy teamStats FROM '/Users/pranavbellamprasad/Downloads/Football/team_stats_cleaned.csv' WITH CSV HEADER
g) Apperances Table - \copy appearences FROM '/Users/pranavbellamprasad/Downloads/Football/appearences_cleaned.csv' WITH CSV HEADER


STEPS TO RUN THE WEBSITE:

1) Create a Python Virtual Env in terminal.
2) Navigate to the folder "DMQL-PHASE-2".
2) Perform "pip3 install -r requirements.txt" - This will install flask, psycopg2, etc.
3) Once all the dependencies are installed successfully.
4) Make sure in the app.py, the database parameters are set correctly, i.e the port, domain, password and Users.
5) Then in the terminal execure the command "python3 app.py".
6) Visit http://127.0.0.1:5000/ on the browser to see the index page of the website.





