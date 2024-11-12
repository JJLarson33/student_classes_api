import sqlite3 as sql

conn = sql.connect('school.db')
cur = conn.cursor()
create_students_table = "CREATE TABLE STUDENTS (STUDENTID INTEGER not null primary key, ENROLLED VARCHAR(5), AGE INTEGER, FIRSTNAME VARCHAR(35), LASTNAME VARCHAR(35), GENDER VARCHAR(15), EMAIL VARCHAR(50), PHONE VARCHAR(20), ADDRESS VARCHAR(100), JOINDATE VARCHAR(30), CLASSLIST VARCHAR(30))"

cur.execute(create_students_table)

cur.execute('INSERT INTO STUDENTS VALUES (0, "FALSE", 21, "Veronica", "Potter", "female", "veronicapotter@furnigeer.com", "+1 (849) 512-2231", "771 Downing Street, Tyro, Nebraska, 6696", "Wed Feb 19 2020 07:25:47", "0,2,14,19")')
cur.execute('INSERT INTO STUDENTS VALUES (1, "TRUE", 25, "Bray", "Summers", "male", "braysummers@furnigeer.com", "+1 (833) 417-2236", "184 Dekoven Court, Driftwood, Marshall Islands, 6520","Mon Aug 06 2018 04:13:31", "1,9,4,14")')
cur.execute('INSERT INTO STUDENTS VALUES (2, "FALSE", 38, "Isabelle", "Robles", "female", "isabellerobles@furnigeer.com", "+1 (830) 458-3893", "250 Jamaica Avenue, Elrama, District Of Columbia, 1166","Tue Nov 28 2017 19:13:59", "11,12,13")')
cur.execute('INSERT INTO STUDENTS VALUES (3, "FALSE", 25, "Cynthia", "Campbell", "female", "cynthiacampbell@furnigeer.com", "+1 (900) 441-2849", "816 Preston Court, Coinjock, Wisconsin, 9858","Wed Sep 27 2017 12:42:10", "1")')
cur.execute('INSERT INTO STUDENTS VALUES (4, "FALSE", 21, "Holder", "Livingston", "male", "holderlivingston@furnigeer.com", "+1 (943) 407-3952", "380 Prospect Street, Adelino, New Hampshire, 4695","Sat Sep 21 2019 19:58:47", "5,7,14,2,1")')
cur.execute('INSERT INTO STUDENTS VALUES (5, "FALSE", 29, "Bentley", "Burke", "male", "bentlyburke@furnigeer.com", "+1 (804) 565-2529", "950 Kingston Avenue, Ribera, American Samoa, 2016","Tue Feb 09 2021 04:07:36", "15,12,13")')
cur.execute('INSERT INTO STUDENTS VALUES (6, "TRUE", 34, "Velazquez", "Lucas", "male", "velazquezlucas@furnigeer.com", "+1 (919) 519-3148", "148 Beacon Court, Bradenville, Connecticut, 4771","Fri Aug 27 2021 04:49:06", "6,8,13")')
cur.execute('INSERT INTO STUDENTS VALUES (7, "TRUE", 26, "Blevins", "Farmer", "male", "blevinsfarmer@furnigeer.com", "+1 (962) 490-2957", "425 Ridge Court, Dotsero, South Carolina, 3021", "Mon Oct 12 2015 15:41:49", "1,2,3")')
cur.execute('INSERT INTO STUDENTS VALUES (8, "TRUE", 37, "Doyle", "Camacho", "male", "doylecamacho@furnigeer.com", "+1 (909) 436-2106", "812 Christopher Avenue, Kiskimere, Palau, 175", "Thu Jan 10 2019 16:19:30", "2,4,7,10,15")')
cur.execute('INSERT INTO STUDENTS VALUES (9, "FALSE", 18, "Donovan", "Rowe", "male", "donovanrowe@furnigeer.com", "+1 (812) 464-3111", "490 Alice Court, Bangor, Maine, 979", "Sat Nov 28 2020 13:59:50", "0,1,3,5,15")')
cur.execute('INSERT INTO STUDENTS VALUES (10, "TRUE", 25, "Estelle", "Casey", "female", "estellecasey@furnigeer.com", "+1 (846) 424-3549", "470 Senator Street, Lindcove, Northern Mariana Islands, 927", "Tue Dec 12 2017 01:00:47", "10,4,13")')
cur.execute('INSERT INTO STUDENTS VALUES (11, "TRUE", 26, "Sherman", "Gay", "male", "shermangay@furnigeer.com", "+1 (849) 447-2805", "145 Lamont Court, Spelter, New Mexico, 7050", "Wed Jan 20 2016 00:48:42", "9,4,3,5,1")')
cur.execute('INSERT INTO STUDENTS VALUES (12, "FALSE", 26, "Cummings", "Hester", "male", "cummingshester@furnigeer.com", "+1 (935) 590-2194", "323 Division Avenue, Hobucken, Federated States Of Micronesia, 6081", "Wed Mar 16 2022 09:44:27", "3,4,9,6,14")')
cur.execute('INSERT INTO STUDENTS VALUES (13, "TRUE", 28, "Allyson", "Wiggins", "female", "allysonwiggins@furnigeer.com", "+1 (934) 514-3729", "759 Bergen Street, Fairforest, Alabama, 7393", "Fri Apr 23 2021 09:42:15", "11,12,2")')
cur.execute('INSERT INTO STUDENTS VALUES (14, "TRUE", 20, "Powell", "Walsh", "male", "powellwalsh@furnigeer.com", "+1 (922) 572-3476", "138 Glendale Court, Gratton, California, 2403", "Thu Dec 10 2015 19:44:09", "0,10,5")')

print(cur.execute('SELECT * from STUDENTS').fetchall())

create_classes_table = 'CREATE TABLE CLASSES (CLASSID INTEGER not null primary key, CODE VARCHAR(15), TITLE VARCHAR(30), DESCRIPTION VARCHAR(75))'

cur.execute(create_classes_table)

cur.execute('INSERT INTO CLASSES VALUES (0, "INFO 1003", "Basic Programming", "Basic programing class using Python.")')
cur.execute('INSERT INTO CLASSES VALUES (1, "INFO 1001", "Intro to Programming", "Visual programming class.")')
cur.execute('INSERT INTO CLASSES VALUES (2, "INFO 1002", "Intro to Web Development", "Basics of HTML and CSS.")')
cur.execute('INSERT INTO CLASSES VALUES (3, "INFO 1004", "Programming I", "Advanced topics of programming.")')
cur.execute('INSERT INTO CLASSES VALUES (4, "INFO 1005", "Intro to Database", "Basics of database design and development class.")')
cur.execute('INSERT INTO CLASSES VALUES (5, "INFO 1011", "Intro to C#", "Programming class using C# language.")')
cur.execute('INSERT INTO CLASSES VALUES (6, "INFO 1010", "Intro to Java", "Programming class using Java language")')
cur.execute('INSERT INTO CLASSES VALUES (7, "INFO 1021", "Advanced C#", "Advanced programming class using C# language.")')
cur.execute('INSERT INTO CLASSES VALUES (8, "INFO 1020", "Advanced Java", "Advanced programming class using Java language.")')
cur.execute('INSERT INTO CLASSES VALUES (9, "INFO 1015", "Intro to AWS", "Basics of cloud services using AWS.")')
cur.execute('INSERT INTO CLASSES VALUES (10, "INFO 1014", "Intro to Azure", "Basics of cloud services using Azure.")')
cur.execute('INSERT INTO CLASSES VALUES (11, "INFO 1012", "Intro to Game Development", "Basics of game development using Unity3d Engine.")')
cur.execute('INSERT INTO CLASSES VALUES (12, "INFO 1022", "Advanced Game Development", "Advanced game development using Unity3d Engine.")')
cur.execute('INSERT INTO CLASSES VALUES (13, "INFO 1032", "Intro to .NET", "Basics of .NET Framework")')
cur.execute('INSERT INTO CLASSES VALUES (14, "INFO 1101", "Intro to Spring Boot", "Basics of Spring Boot using Java")')
cur.execute('INSERT INTO CLASSES VALUES (15, "INFO 1102", "Advanced Spring Boot", "Advanced topics of Spring Boot with Java")')

print(cur.execute('SELECT * from CLASSES').fetchall())

create_token_table = 'CREATE TABLE TOKENS (TOKEN VARCHAR(30))'
cur.execute(create_token_table)

cur.execute('INSERT INTO TOKENS VALUES ("C3j3h5KL5g")')
cur.execute('INSERT INTO TOKENS VALUES ("gUT67D3vjh")')
cur.execute('INSERT INTO TOKENS VALUES ("hY523bx7qE")')
cur.execute('INSERT INTO TOKENS VALUES ("Ei5OP4Le77")')
cur.execute('INSERT INTO TOKENS VALUES ("7dTy4IO3Md")')

print(cur.execute('SELECT * from TOKENS').fetchall())

conn.commit()
conn.close()