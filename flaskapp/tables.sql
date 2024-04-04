-- https://www.postgresqltutorial.com/

CREATE TABLE member (
    memberId integer PRIMARY KEY,
    firstName varchar(100),
    middleName varchar(100) DEFAULT '',
    lastName varchar(100),
    phoneNumber varchar(15),
    score integer NOT NULL,
    NumberOfEventsAttended integer
);

CREATE TABLE chapter (
    chapterName varchar(100) PRIMARY KEY,
    numberofMembers integer,
    chapterLead varchar(100),
    chapterEmail varchar(50)
);

CREATE TABLE event (
    eventName varchar(100) PRIMARY KEY,
    venue varchar(100),
    eventDate date,
    attendance integer
);

-- CREATE TABLE demographics (
--     memberId integer PRIMARY KEY,
--     race varchar(50),
--     age integer,
--     gender varchar(50)
-- );

CREATE TABLE memberAddress (
    memberId integer PRIMARY KEY,
    street varchar(50),
    city varchar(50),
    state varchar(50),
    zipcode integer
);

CREATE TABLE donation (
    memberId integer PRIMARY KEY,
    item varchar(50),
    monetaryWorth integer
);

INSERT INTO member (memberId, Score, phoneNumber, firstName, middleName, lastName, NumberOfEventsAttended)
VALUES
(01, 987, 1234567890, 'Betty', 'M', 'Hibler', 5),
(02, 654, 2345678901, 'Landra', 'Lewis', 3),
(03,321, 3456789012, 'Travis', 'Bolinger', 2),
(04, 432, 4567890123, 'Rachel', 'White', 7),
(05, 876, 5678901234, 'Joanie', 'Lukins', 4),

INSERT INTO chapter (chapterName, numberofMembers, chapterLead, chapterEmail)
VALUES
    ('Madison County', 50, 'Landra Lewis', 'alex@example.com'),
    ('Wilderness Trace', 30, 'Emily Brown', 'emily@example.com')


-- INSERT INTO demographics (memberId, race, age, gender)
-- VALUES
--     (1, 'White', 30, 'Male'),
--     (2, 'Asian', 25, 'Female');

INSERT INTO memberAddress (memberId, street, city, state, zipcode)
VALUES
    (01,'314 Prospect St', 'Berea', 'KY', 40403),
    (02,'619 Chestnut St', 'Berea', 'KY', 40403),
    (03,'314 University Dr Apt A', 'Richmond', 'KY', 2841),
    (04,'1101 Elm St', 'Danville', 'KY', 40422),
    (05,'503 Ohara Dr', 'Daville', 'KY', 40422),
    


INSERT INTO donation (memberId, item, monetaryWorth)
VALUES
    (01,'Laptop', 800),
    (02,'Books', 100),
    (03,'Laptop', 800),
    (04,'Books', 100),
    (05,'Laptop', 800),

INSERT INTO event (eventName, venue, theme, eventDate, attendance)
VALUES
    ('Hackathon', 'Convention Center', 'Environmental Preservation', '2024-04-01', 200),
    ('Workshop', 'Community Center', 'Environmental Preservation', '2024-04-15', 80),
    ('Hackathon', 'Convention Center', 'Environmental Preservation', '2024-04-01', 200),
    ('Seedy Workshop', 'Community Center', 'Environmental Preservation', '2024-04-15', 80),
    ('How to sleep in class', 'Community Center', 'Sleep', '2024-04-15', 80)