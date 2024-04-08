-- https://www.programiz.com/sql/insert-into

CREATE TABLE IF NOT EXISTS "member"
(
    memberId serial PRIMARY KEY NOT NULL,
    firstName NVARCHAR(100)  NOT NULL,
    middleName NVARCHAR(100),
    lastName NVARCHAR(100),
    phoneNumber NVARCHAR(15),
    score INTEGER NOT NULL,
    memberAddress NVARCHAR NOT NULL,
    NumberOfEventsAttended INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "chapter"
(
    chapterName NVARCHAR PRIMARY KEY NOT NULL,
    numberofMembers INTEGER  NOT NULL,
    chapterLead NVARCHAR(100),
    chapterEmail NVARCHAR(50),
    FOREIGN KEY (memberId) REFERENCES "member" (memberId) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS "event"
(
    eventName NVARCHAR PRIMARY KEY NOT NULL,
    venue NVARCHAR(100)  NOT NULL,
    theme NVARCHAR(100) NOT NULL,
    eventDate DATETIME,
    numberofMemebersAttended INTEGER
);

CREATE TABLE IF NOT EXISTS "donation"
(
    donationId serial PRIMARY KEY  NOT NULL,
    monetaryWorth INTEGER  NOT NULL,
    item NVARCHAR  NOT NULL
);