CREATE TABLE member (
    memberId serial PRIMARY KEY,
    firstName varchar(100),
    middleName varchar(100) DEFAULT '',
    lastName varchar(100),
    phoneNumber varchar(20),
    score integer NOT NULL,
    memberAddress varchar(100),
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
    theme varchar(100),
    eventDate date,
    numberofMemebersAttended integer
);

CREATE TABLE donation (
    donationId serial PRIMARY KEY,
    donorId integer REFERENCES member(memberId),
    item VARCHAR(50),
    monetaryWorth INTEGER
);

INSERT INTO member (Score, phoneNumber, firstName, middleName, lastName, memberAddress, NumberOfEventsAttended)
VALUES
    (987, 1234567890, 'Betty', 'M', 'Hibler', '314 Prospect St, Berea, KY, 40403',  5),
    (654, 2345678901, 'Landra', '', 'Lewis', '619 Chestnut St, Berea, KY, 40403', 3),
    (321, 3456789012, 'Travis', '', 'Bolinger', '314 University Dr Apt A, Richmond, KY, 2841',  2),
    (432, 4567890123, 'Rachel', '',  'White', '1101 Elm St, Danville, KY, 40422', 7),
    (876, 5678901234, 'Joanie', '', 'Lukins', '503 Ohara Dr, Daville, KY, 40422', 4);

INSERT INTO chapter (chapterName, numberofMembers, chapterLead, chapterEmail)
VALUES
    ('Madison County', 50, 'Landra Lewis', 'alex@example.com'),
    ('Wilderness Trace', 30, 'Emily Brown', 'emily@example.com');


INSERT INTO donation (item, monetaryWorth)
VALUES
    ('Laptop', 800),
    ('Books', 100),
    ('Laptop', 800),
    ('Books', 100),
    ('Laptop', 800);

INSERT INTO event (eventName, venue, theme, eventDate, numberofMemebersAttended)
VALUES
    ('Community Building', 'Convention Center', 'Environmental Preservation', '2024-04-01', 200),
    ('Workshop', 'Community Center', 'Environmental Preservation', '2024-04-15', 80),
    ('Hackathon', 'Convention Center', 'Environmental Preservation', '2024-04-01', 200),
    ('Seedy Workshop', 'Community Center', 'Environmental Preservation', '2024-04-15', 80),
    ('How to sleep in class', 'Community Center', 'Sleep', '2024-04-15', 80);