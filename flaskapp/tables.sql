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
