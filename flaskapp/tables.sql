CREATE TABLE member (
    memberid serial PRIMARY KEY,
    firstName varchar(100),
    middleName varchar(100) DEFAULT '',
    lastName varchar(100),
    phoneNumber varchar(20),
    score integer NOT NULL,
    memberAddress varchar(100),
    NumberOfEventsAttended integer, 
    -- chapterName varchar(50)
    status varchar(15)
);


CREATE TABLE chapter (
    chapterName varchar(100) PRIMARY KEY,
    numberofMembers integer,
    chapterLead varchar(100),
    chapterEmail varchar(50)
);

CREATE TABLE event (
    eventname varchar(100) PRIMARY KEY,
    venue varchar(100),
    theme varchar(100),
    eventDate date,
    numberofMemebersAttended integer
    -- chapterName VARCHAR(50) REFERENCES chapter(chapterName)
);

CREATE TABLE donation (
    donationId serial PRIMARY KEY,
    donorId integer REFERENCES member(memberId),
    item VARCHAR(50),
    monetaryWorth INTEGER
);

-- CREATE TABLE event_attendance (
--    memberid integer REFERENCES member(memberid),
--    eventName VARCHAR(100) REFERENCES event(eventName),
--    PRIMARY KEY (memberid, eventName)
-- );

CREATE TABLE event_attendance (
   member INTEGER REFERENCES member(memberid),
   event1 VARCHAR(100) REFERENCES event(eventname),
   PRIMARY KEY (member, event1)
);


