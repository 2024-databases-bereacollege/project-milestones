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
    event varchar(200),
    eventDate date,
    attendance integer,
    theme varchar(200) -- Added the theme column as per the insert statements
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

INSERT INTO member (memberId, score, phoneNumber, firstName, middleName, lastName, NumberOfEventsAttended)
VALUES
(1, 987, '1234567890', 'Betty', 'M', 'Hibler', 5),
(2, 654, '2345678901', 'Landra', '', 'Lewis', 3),
(3, 321, '3456789012', 'Travis', '', 'Bolinger', 2),
(4, 432, '4567890123', 'Rachel', '', 'White', 7),
(5, 876, '5678901234', 'Joanie', '', 'Lukins', 4);

INSERT INTO chapter (chapterName, numberofMembers, chapterLead, chapterEmail)
VALUES
('Madison County', 50, 'Landra Lewis', 'alex@example.com'),
('Wilderness Trace', 30, 'Emily Brown', 'emily@example.com');

INSERT INTO memberAddress (memberId, street, city, state, zipcode)
VALUES
(1, '314 Prospect St', 'Berea', 'KY', 40403),
(2, '619 Chestnut St', 'Berea', 'KY', 40403),
(3, '314 University Dr Apt A', 'Richmond', 'KY', 40475), -- Corrected ZIP code
(4, '1101 Elm St', 'Danville', 'KY', 40422),
(5, '503 Ohara Dr', 'Daville', 'KY', 40422);

INSERT INTO donation (memberId, item, monetaryWorth)
VALUES
(1, 'Laptop', 800),
(2, 'Books', 100),
(3, 'Laptop', 800),
(4, 'Books', 100),
(5, 'Laptop', 800);

INSERT INTO event (eventName, venue, event, eventDate, attendance, theme)
VALUES
('Hackathon', 'Convention Center', 'Environmental Preservation', '2024-04-01', 200, 'Tech and Innovation'),
('Workshop', 'Community Center', 'Environmental Preservation', '2024-04-15', 80, 'Community Building'),
('Seedy Workshop', 'Community Center', 'Environmental Preservation', '2024-04-15', 80, 'Gardening'),
('How to sleep in class', 'Community Center', 'Sleep Education', '2024-04-15', 80, 'Health');
