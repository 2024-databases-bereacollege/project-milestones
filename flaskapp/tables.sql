-- https://www.postgresqltutorial.com/

CREATE TABLE member (
    memberId integer PRIMARY KEY,
    firstName varchar(100),
    lastName varchar(100),
    phoneNumber varchar(15),
    score integer NOT NULL,
    address varchar(100),
    numberofEventAttended integer
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

CREATE TABLE address (
    memberId integer FOREIGN KEY,
    street varchar(50),
    city varchar(50),
    state varchar(50)
    zipcode integer
);

CREATE TABLE donation (
    memberId integer FOREIGN KEY,
    item varchar(50),
    monetaryWorth integer
);