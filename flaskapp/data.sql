-- https://www.programiz.com/sql/insert-into

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS "member"
(
    memberId serial PRIMARY KEY NOT NULL,
    firstName VARCHAR(100)  NOT NULL,
    middleName VARCHAR(100),
    lastName VARCHAR(100),
    phoneNumber VARCHAR(15),
    score INTEGER NOT NULL,
    memberAddress VARCHAR NOT NULL,
    NumberOfEventsAttended INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "chapter"
(
    chapterName VARCHAR PRIMARY KEY NOT NULL,
    memberId INTEGER,
    numberofMembers INTEGER  NOT NULL,
    chapterLead VARCHAR(100),
    chapterEmail VARCHAR(50),
    FOREIGN KEY (memberId) REFERENCES member(memberId)
		ON DELETE NO ACTION 
        ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS "event"
(
    eventName VARCHAR PRIMARY KEY NOT NULL,
    venue VARCHAR(100)  NOT NULL,
    theme VARCHAR(100) NOT NULL,
    eventDate DATETIME,
    numberofMemebersAttended INTEGER
);

CREATE TABLE IF NOT EXISTS "donation"
(
    donationId serial PRIMARY KEY  NOT NULL,
    monetaryWorth INTEGER  NOT NULL,
    item VARCHAR  NOT NULL
);