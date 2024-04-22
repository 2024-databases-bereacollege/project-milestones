-- https://www.postgresqltutorial.com/

-- Volunteer Table
CREATE TABLE IF NOT EXISTS Volunteer (
    VolunteerID SERIAL PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Password VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    HasRecordAccess BOOLEAN
);

-- Service_Provider Table
CREATE TABLE IF NOT EXISTS Service_Provider (
    OrganizationID VARCHAR(255) PRIMARY KEY,
    OrganizationName VARCHAR(255),
    ContactPerson VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    DateOfStart DATE
);

-- Services Table
CREATE TABLE IF NOT EXISTS Services (
    ServiceID SERIAL PRIMARY KEY,
    ServiceType VARCHAR(255),
    OrganizationID VARCHAR(255) REFERENCES Service_Provider(OrganizationID)
);

-- Neighbor Table
CREATE TABLE IF NOT EXISTS Neighbor (
    NeighborID SERIAL PRIMARY KEY,
    VolunteerID INT REFERENCES Volunteer(VolunteerID),
    OrganizationID VARCHAR(255) REFERENCES Service_Provider(OrganizationID),
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DateOfBirth DATE,
    Phone VARCHAR(20),
    Location TEXT,
    Email VARCHAR(255),
    Created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    HasStateID BOOLEAN,
    HasPet BOOLEAN
);

-- Visit_Record Table
CREATE TABLE IF NOT EXISTS Visit_Record (
    RecordID SERIAL PRIMARY KEY,
    NeighborID INT REFERENCES Neighbor(NeighborID),
    VolunteerID INT REFERENCES Volunteer(VolunteerID),
    Date DATE
);

-- Inventory Table
CREATE TABLE IF NOT EXISTS Inventory (
    InventoryID SERIAL PRIMARY KEY,
    NameOfItem VARCHAR(255),
    VolunteerID INT REFERENCES Volunteer(VolunteerID),
    Description_of_Item VARCHAR(255),
    ExpirationDate DATE,
    Number_Of_Item INT
);

-- Inventory_Usage Table
CREATE TABLE IF NOT EXISTS Inventory_Usage (
    Inventory_UseID SERIAL PRIMARY KEY,
    InventoryID INT REFERENCES Inventory(InventoryID),
    RecordID INT REFERENCES Visit_Record(RecordID),
    Description_of_Item VARCHAR(255),
    Number_Of_Item_Used INT
);
















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

-- CREATE TABLE Volunteer (
--     VolunteerID SERIAL PRIMARY KEY,
--     FirstName VARCHAR(255),
--     LastName VARCHAR(255),
--     Email VARCHAR(255),
--     Phone VARCHAR(20),
--     HasRecordAccess BOOLEAN
-- );

-- CREATE TABLE Neighbor (
--     NeighborID SERIAL PRIMARY KEY,
--     VolunteerID INT REFERENCES Volunteer(VolunteerID),
--     Organization VARCHAR(255),
--     FirstName VARCHAR(255),
--     LastName VARCHAR(255),
--     DateOfBirth DATE,
--     Phone VARCHAR(20),
--     Address TEXT,
--     Email VARCHAR(255),
--     HasStateID BOOLEAN,
--     HasPet BOOLEAN
-- );

-- CREATE TABLE Service_Providers (
--     Organization VARCHAR(255) PRIMARY KEY,
--     ContactPerson VARCHAR(255),
--     Email VARCHAR(255),
--     Phone VARCHAR(20),
--     DateOfStart DATE
-- );

-- CREATE TABLE Services (
--     ServiceType VARCHAR(255) PRIMARY KEY,
--     Organization VARCHAR(255) REFERENCES Service_Providers(Organization)
-- );

-- CREATE TABLE Inventory (
--     NameOfItem VARCHAR(255) PRIMARY KEY,
--     VolunteerID INT REFERENCES Volunteer(VolunteerID),
--     ExpirationDate DATE,
--     NumberOfItem INT
-- );

-- CREATE TABLE Visit_Service (
--     ServiceOrder SERIAL PRIMARY KEY,
--     Organization VARCHAR(255) REFERENCES Service_Providers(Organization),
--     NeighborID INT REFERENCES Neighbor(NeighborID),
--     ServiceType VARCHAR(255) REFERENCES Services(ServiceType),
--     Description TEXT,
--     VolunteerID INT REFERENCES Volunteer(VolunteerID)
-- );

-- CREATE TABLE Visit_Record (
--     RecordID SERIAL PRIMARY KEY,
--     ServiceOrder INT NOT NULL,
--     Date DATE,
--     Time TIME,
--     Notes TEXT,
--     FOREIGN KEY (ServiceOrder) REFERENCES Visit_Service(ServiceOrder)
-- );
