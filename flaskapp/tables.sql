-- https://www.postgresqltutorial.com/

-- CREATE TABLE othertable (
--     otherid integer PRIMARY KEY,
--     data varchar
-- );

-- CREATE TABLE example (
--     id serial PRIMARY KEY,
--     username varchar(32) UNIQUE,
--     description varchar(255) NOT NULL,
--     fkey_other integer REFERENCES othertable(otherid), 
--     isInt smallint NOT NULL DEFAULT(0),
--     isBool boolean
-- );

CREATE TABLE Volunteer (
    VolunteerID SERIAL PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    HasRecordAccess BOOLEAN
);

CREATE TABLE Neighbor (
    NeighborID SERIAL PRIMARY KEY,
    VolunteerID INT REFERENCES Volunteer(VolunteerID),
    Organization VARCHAR(255),
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DateOfBirth DATE,
    Phone VARCHAR(20),
    Address TEXT,
    Email VARCHAR(255),
    HasStateID BOOLEAN,
    HasPet BOOLEAN
);

CREATE TABLE Service_Providers (
    Organization VARCHAR(255) PRIMARY KEY,
    ContactPerson VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    DateOfStart DATE
);

CREATE TABLE Services (
    ServiceType VARCHAR(255) PRIMARY KEY,
    Organization VARCHAR(255) REFERENCES Service_Providers(Organization)
);

CREATE TABLE Inventory (
    NameOfItem VARCHAR(255) PRIMARY KEY,
    VolunteerID INT REFERENCES Volunteer(VolunteerID),
    ExpirationDate DATE,
    NumberOfItem INT
);

CREATE TABLE Visit_Service (
    ServiceOrder SERIAL PRIMARY KEY,
    Organization VARCHAR(255) REFERENCES Service_Providers(Organization),
    NeighborID INT REFERENCES Neighbor(NeighborID),
    ServiceType VARCHAR(255) REFERENCES Services(ServiceType),
    Description TEXT,
    VolunteerID INT REFERENCES Volunteer(VolunteerID)
);

CREATE TABLE Visit_Record (
    RecordID SERIAL,
    ServiceOrder INT,
    Date DATE,
    Time TIME,
    PRIMARY KEY (RecordID, ServiceOrder),
    FOREIGN KEY (ServiceOrder) REFERENCES Visit_Service(ServiceOrder)
);
