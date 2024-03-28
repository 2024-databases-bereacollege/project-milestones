-- https://www.postgresqltutorial.com/

CREATE TABLE member (
    memberId integer PRIMARY KEY,
    firstName varchar(100),
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

CREATE TABLE demographics (
    memberId integer PRIMARY KEY,
    race varchar(50),
    age integer,
    gender varchar(50)
);

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

INSERT INTO member (memberID, Score, phoneNumber, firstName, lastName, NumberOfEventsAttended)
VALUES
('123456789', 987, 1234567890, 'John', 'Doe', 5),
('987654321', 654, 2345678901, 'Jane', 'Smith', 3),
('567890123', 321, 3456789012, 'Alex', 'Johnson', 2),
('765432109', 432, 4567890123, 'Maria', 'Garcia', 7),
('012345678', 876, 5678901234, 'Chen', 'Wei', 4);

INSERT INTO chapter (chapterName, numberofMembers, chapterLead, chapterEmail)
VALUES
    ('Tech Enthusiasts', 50, 'Alex Johnson', 'alex@example.com'),
    ('Community Builders', 30, 'Emily Brown', 'emily@example.com');


INSERT INTO demographics (memberId, race, age, gender)
VALUES
    (1, 'White', 30, 'Male'),
    (2, 'Asian', 25, 'Female');

INSERT INTO memberAddress (memberId, street, city, state, zipcode)
VALUES
    (1, '123 Main St', 'Anytown', 'KY', 40403),
    (2, '456 Elm St', 'Smallville', 'KY', 40501);

INSERT INTO donation (memberId, item, monetaryWorth)
VALUES
    (1, 'Laptop', 800),
    (2, 'Books', 100);

INSERT INTO event (eventName, venue, eventDate, attendance)
VALUES
    ('Hackathon', 'Convention Center', '2024-04-01', 200),
    ('Workshop', 'Community Center', '2024-04-15', 80);