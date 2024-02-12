# project-milestones
For working with each project milestone 

# Milestone 1: Creating A Data Model
**Learning Objective:** Setup your teams, decide roles, and practice Git while you're at it

## List and description of data sources 

UP data: Since UP is a local, small non-profit, the only data they want to use is directly related to their operational process. Thus, the list of data is:
	Neighbors: each individual who needs assistance from the organization. As part of its policies, UP only registers them on their second visit. This registration includes name, 
	Partners: what is the partner and what service do they provide.
	Inventory: the organization is almost completely privately funded on the basis of donations, and the different forms of products they receive are registered on paper.



## Business Rules (both data and non-data) 

A NEIGHBOR is registered by an ADMINISTRATOR on the RECORD only once on their second visit to UP, whereas the RECORD registers optional one NEIGHBOR by at least one ADMINISTRATOR.

A NEIGHBOR can receive many SERVICES, and a SERVICE can be received by optional one NEIGHBOR. 

 A NEIGHBOR follows guidelines on the usage of INVENTORY items. The NEIGHBOR can acquire optional many items from the INVENTORY, whereas the INVENTORY may have a NEIGHBOR acquiring items optionally many times. 

 An ADMINISTRATOR has access to many RECORD data, whereas the RECORD can be accessed by many ADMINISTRATORS.

Using the RECORD, an ADMINISTRATOR can start a process to assist the NEIGHBOR in receiving many SERVICES. 

A SERVICE is provided by optional one PARTNER ORGANIZATION, whereas a PARTNER ORGANIZATION can provide at least one SERVICE. The SERVICE is then tracked on the NEIGHBOR’s record and followed up as necessary by at least one UP ADMINISTRATOR. 


## Entity Names and Definitions

Neighbors: a houseless person who seeks UP for support. They can be classified as emergency housed (e.g. a person sleeps in someone’s house), underhoused (they may have a shelter, but it is not optimal. e.g. a shed or trailer without access to electricity or water, or similar precarious situations).
Attributes: ID, Name, Date of Birth, Contact Information (phone, email), Mailing Address, Services Accessed (list of service IDs), Case Manager ID, Document Assistance (IDs, SS cards, etc.), Notes.

Services: different forms of assistance that UP facilitates to individuals
Attributes: Service ID, Service Type (Laundry, Meals, Emergency Shelter, Case Management, ID Assistance, SS Card Assistance, Referrals with SNAP, etc.), Description, Date/Time Offered.

Partner Organizations: UP partners support their Neighbors on each specific possible help (for example, a case manager)
Attributes: Organization ID, Name, Contact Information, Services Offered, Referral Contact (person or department within the organization).

Service Access Records: access to the database information
Attributes: Record ID, Individual ID, Service ID, Date/Time of Access, Outcome (for services with measurable outcomes).

Inventory: the organization has an inventory of clothing, hygiene kits, and food, and there are some guidelines about how many items can a neighbor have. These guidelines are always changing on a case-by-case basis. UP also envisions this process being automatize and displayed on their website so donors can see what the organization needs the most.
Attributes: Item ID, Type (Clothing, Hygiene, Food), Description, Quantity Available, Reorder Level.

Service Access Record:
Attributes: Record ID, Individual ID, Type (ID, SS Card, etc.), Status (Requested, In Process, Completed), Date of Request, Date of Completion.




## Relationships

Individuals to Services


Many-to-Many: An individual can access multiple services, and a service can be accessed by multiple individuals. This relationship is mediated by the Service Access Records entity.


Individuals to Case Management


One-to-Many: A single case manager can assist multiple individuals, but an individual's case is primarily managed by one case manager at a time.
Case Management can Access many records but records can only be accessed by one Case Manager.


Services to Partner Organizations


Many-to-Many: A service may be provided in partnership with multiple organizations, and an organization can offer multiple services. This might be more indirect, depending on how closely services are tied to specific partners.
Partner Organizations can see many inventory and inventory can be seen by many Partner organizations.


Individuals to Document Assistance Records


One-to-Many: An individual can have multiple document assistance records (for different documents or repeated assistance).


Inventory to Case Managers
Inventory can be modified by many Case managers, Inventory needs a Case Manager to be modified.



## **Entity Relationship Diagram (ERD)**: 

![brief alt text](B240470A-174B-47F5-A750-61DDDB946791.png)
