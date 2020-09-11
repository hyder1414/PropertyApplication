/*
The RealEstateDB contains the following tables (Non-CircularDesign):
Firm(FirmID, FirmName)
Employee(EmplID, EmplLastName, EmplFirtName, OfficeID)
Manager(EmplID, Bonus)
SalesOffice(OfficeID, OfficeStreet, OfficeCity, OfficeState, OfficeZip, OfficePhone, FirmID, ManagerID)
Property(PropertyID, PropAddress, PropCity, PropState, PropZip, ListingDate,SoldDate, SalePrice, OfficeID)
PropertyOwner(OwnerID, OwnerLastName, OwnerFirstName)
PropertyOwnership(PropertyID,OwnerID, PercentOwned)
*/

-- Drop tables in case they already exist
-- Note:  See the order in which the tables are dropped. The most dependent tables are dropped first.
drop table if exists PropertyOwnership;
drop table if exists PropertyOwner;
drop table if exists Property;
drop table if exists Employee;
drop table if exists SalesOffice;
drop table if exists Manager;
drop table if exists Firm;

-- create tables
-- Note the order in which the tables are created. The most independent tables are created first.
Create Table Firm (
FirmID int not null primary key,
FirmName varchar(60) not null
);

Create Table Manager (
EmplID int not null Primary Key,
Bonus decimal
);

create Table SalesOffice (
OfficeID int not null primary key,
OfficeStreet varchar(30) not null,
OfficeCity varchar(30) not null,
OfficeState Char(2) not null,
OfficeZip varchar(9) not null,
OfficePhone varchar(11),
FirmID int not null,
 constraint FK_FirmID Foreign key  (firmID) references
Firm (FirmID),
ManagerID int not null ,
constraint FK_MngrID Foreign key (ManagerID) references Manager(EmplID)
);

Create Table Employee (
EmplID int not null primary key,
EmplLastName varchar(35) not null,
EmplFirstName varchar(20) not null,
OfficeID int not null,
 constraint FK_OfficeID foreign key (officeID) references
SalesOffice(OfficeID)
);

Create Table Property (
PropertyID int not null primary key,
PropAddress varchar(35) not null,
PropCity Varchar(30) not null,
PropState char(2) not null,
PropZip varchar(9),
ListingDate date,
SoldDate date,
SalePrice decimal,
OfficeID int not null,
 constraint FK_PropSaleOffID Foreign Key (officeID) references SalesOffice (OfficeID)
);

create table PropertyOwner(
OwnerID int not null primary key,
OwnerLastName varchar(30) not null,
OwnerFirstName varchar(20) not null
);

Create Table PropertyOwnership(
PropOwnershipID int not null primary key auto_increment,
PropertyID int not null ,
constraint FK_PropertyID Foreign Key (propertyID)
references Property(PropertyID),
OwnerID int not null ,
constraint FK_OwnerID Foreign key (ownerID)
references PropertyOwner(OwnerID),
PercentOwned decimal(5,2) not null
);
-- Create Indexes
create index EmplLastNameX on Employee (EmplLastName);
create index OffCityX on SalesOffice (OfficeCity);
create index OffFirmIDX on SalesOffice (FirmID);
create index OffMngrIDX on SalesOffice (ManagerID);
create index PropCityX on Property(PropCity);
create index PropListDateX on Property (ListingDate);
create index PropSoldDateX on Property (SoldDate);
create index PropOfficeX on Property (OfficeID);