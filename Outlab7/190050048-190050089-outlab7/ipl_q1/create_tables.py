import sqlite3

c = sqlite3.connect('ipl.db')

c.execute('''CREATE TABLE TEAM
         (team_id INT PRIMARY KEY     NOT NULL,
         team_name           TEXT);''')
c.execute('''CREATE TABLE PLAYER
         (player_id INT PRIMARY KEY     NOT NULL,
         player_name           TEXT,
         dob                   TIMESTAMP,
         batting_hand          TEXT,
         bowling_skill         TEXT,
         country_name          TEXT);''')
c.execute('''CREATE TABLE MATCH
         (match_id INT PRIMARY KEY     NOT NULL,
         season_year           INT,
         team1 INT,
         team2 INT,
         battedfirst           TEXT,
         battedsecond          TEXT,
         venue_name            TEXT,
         city_name             TEXT,
         country_name          TEXT,
         toss_winner INT,
         match_winner INT,
         toss_name             TEXT,
         win_type              TEXT,
         man_of_match INT,
         win_margin            INT,
         FOREIGN KEY(team1) REFERENCES TEAM(team_id),
         FOREIGN KEY(team2) REFERENCES TEAM(team_id),
         FOREIGN KEY(man_of_match)        REFERENCES PLAYER(player_id),
         FOREIGN KEY(toss_winner)        REFERENCES TEAM(team_id),
         FOREIGN KEY(match_winner)        REFERENCES TEAM(team_id));''')
c.execute('''CREATE TABLE PLAYER_MATCH
         (playermatch_key INT PRIMARY KEY     NOT NULL,
         match_id INT,
         player_id INT,
         batting_hand          TEXT,
         bowling_skill         TEXT,
         role_desc          TEXT,
         team_id INT,
         FOREIGN KEY(match_id)        REFERENCES MATCH(match_id),
         FOREIGN KEY(player_id)        REFERENCES PLAYER(player_id),
                  FOREIGN KEY(team_id)        REFERENCES TEAM(team_id));''')
c.execute('''CREATE TABLE BALL_BY_BALL
         (match_id INT,
         innings_no INT,
         over_id INT,
         ball_id INT,
         striker_batting_position INT,
         runs_scored INT,
         extra_runs INT,
         out_type TEXT,
         striker INT,
         non_striker INT,
         bowler INT,
         FOREIGN KEY(match_id)        REFERENCES MATCH(match_id),
         FOREIGN KEY(striker)        REFERENCES PLAYER(player_id),
         FOREIGN KEY(non_striker)        REFERENCES PLAYER(player_id),
         FOREIGN KEY(bowler)        REFERENCES PLAYER(player_id),
         PRIMARY KEY(match_id, innings_no, over_id, ball_id));''')
c.commit()
c.close()