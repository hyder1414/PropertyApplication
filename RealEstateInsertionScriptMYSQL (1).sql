--
-- Sample Data for RealEstateDBWithNoCircular
delete from PropertyOwnership;
delete from PropertyOwner;
delete from Property;
delete from Employee;
delete from SalesOffice;
delete from Manager;
delete from Firm;


-- Note: Pay attention to the order in which the data is inserted into ttables.
-- The data is first inserted into most independent tables and then into the dependent tables.
insert into Firm values
(1,	'Caldwell');
insert into Firm values
(2, 'MinMax');
insert into Firm values
(3,'SouthWest');
--
insert into Manager values
(1, 8000);
insert into Manager values
(3, 7000);
insert into Manager values
(7, 6000);
insert into Manager values
(8,5000);
insert into Manager values
(10,10000);
--
insert into SalesOffice Values
(1, '123 Elm Street','Lubbock','TX','79424','8067899999',1,1);
insert into SalesOffice Values
(2, '4500 Salem Street',	'Dallas',	'TX', '75201','2126788888',1,3);
insert into SalesOffice Values
(3,	'3410 Spanish Oaks',	'Houston',	'TX',	'77542',	'7132452222',2	,7);
insert into SalesOffice Values
(4,	'3450 Slide Ave',	'Lubbock',	'TX',	'79419',	'8065764545',	3,	8);
insert into SalesOffice Values
(5,	'9800 Quaker Ave'	,'Lubbock',	'TX',	'79425'	, '8066583333',	3,	10);
--
insert into Employee values
(1,	'Squire',	'Exie', 	1),
(2,	'Dishon',	'Aleen', 	1),
(3,	'Dozier',	'Florencia', 	2),
(4,	'Legette',	'Gennie', 	2),
(5,	'Pooler',	'Barbar', 	2),
(6,	'Marietta',	'Anitra', 	3),
(7,	'Lucien',	'Minh', 	3),
(8,	'Samford',	'Katlyn', 	4),
(9,	 'Neal',	'Tristan',	4),
(10,	'Greenspan',	'Luke', 	5);

--
insert into Property values
(1,	'4508 78th Street',	'Lubbock',	'TX',	'79422',	'2009-10-12',	'2009-12-12',	200000,	1),
(2,	'3510 79th Street',	'Lubbock',	'TX',	'79423',	'2010-10-12',	'2010-9-12',	250000,	1),
(3,	'4535 80th Street',	'Lubbock',	'TX',	'79424',	'2009-9-12',	'2010-3-12',	300000,	1),
(4,	'5612 112th Street',	'Lubbock',	'TX',	'79426',	'2015-8-8',	'2015-12-8',	780000,	1),
(5,	'2300 Lamar Street',	'Dallas',	'TX',	'75200',	'2015-8-8',	'2015-11-8',	580000,	2),
(6,	'4500 Lamar Street',	'Dallas',	'TX',	'75201',	'2015-8-8',	'2015-12-20',	900000,	2),
(7,	'5600 Commerce Street',	'Dallas',	'TX',	'75211',	'2014-1-8',	'2015-12-8',	860000,	2),
(8,	'2300 Spanish Oaks Blvd',	'Houston',	'TX',	'77210',	'2014-2-8',	'2015-12-8',	680000,	2),
(9,	'2345 Spanish Oaks Blvd',	'Houston',	'TX',	'77209',	'2015-2-8',	'2015-12-8',	880000,3),
(10,'1000 Green Briar Street',	'Houston',	'TX',	'77201',	'2015-2-8',	'2015-12-8',	480000,	3),
(11,'2000 Green Briar Street',	'Houston',	'TX',	'77201',	'2015-2-8',	'2015-12-8',	380000,	3),
(12,'9812 Salem Ave',	'Lubbock',	'TX',	'79422',	'2009-1-12',	'2009-12-12',	450000,	4),
(13,'9813 Vicksburg Ave',	'Lubbock',	'TX',	'79423',	'2010-10-12',	'2010-9-12',	350000,	4),
(14,'9915 Frankford Ave',	'Lubbock',	'TX',	'79424',	'2015-9-12',	'2015-12-12',	450000,	4),
(15,'9945 Iola Ave',	'Lubbock',	'TX',	'79424',	'2015-9-12',null,389000,	4),
(16,'8812 Salem Ave',	'Lubbock',	'TX','79422','2009-1-12',	'2009-12-12',	560000,5),
(17,	'7813 Vicksburg Ave',	'Lubbock',	'TX',	'79423',	'2010-10-12',	'2010-9-12',	355000,	5),
(18,	'7915 Frankford Ave',	'Lubbock',	'TX',	'79424',	'2015-9-12'	,'2015-12-12',	460000,	5),
(19,	'8845 Iola Ave',	'Lubbock',	'TX',	'79424',	'2015-9-12',	'2015-11-12',	409000,	5),
(20,	'9989 Memphis Ave',	'Lubbock',	'TX',	'79424',	'2015-10-12',null, 	390000,	5);
--
insert into PropertyOwner values
(1,	 'Moe',	'Kati'),
(2,	 'Schindler',	'Sharika'),
(3,	 'Scheck',	'Vicente'),
(4,	 'Kovac',	'Antoinette'),
(5,	 'Mitcham',	'Cassie'),
(6,	'High',	'Jannie'),
(7,	'Yoshida',	'Bruna'),
(8,	'Nolen',	'Karon'),
(9,	 'Waldon',	'Dolores'),
(10,	'Caroll',	'Lyla' ),
(11,	'Gonsoulin',	'Ronni'),
(12,	'Piehl',	'Edie' ),
(13,	'Steinhauser',	'Delmar' ),
(14,	'Mcconnaughey',	'Dorcas' ),
(15,	'Davie',	'Darcey' ),
(16,	'Sorensen',	'Franchesca' );
--
insert into PropertyOwnership (propertyID, OwnerID, PercentOwned) values
(1,	1,	50),
(1,	2,	20),
(1,	4,	30),
(2	,1,	60),
(2,	3,	40),
(3	,4,	100),
(4	,5,	45),
(4	,11,	55),
(5	,6,	100),
(6	,7,	35),
(6	,8,	65),
(7	,8,	65),
(7	,9,	35),
(8	,10,	100),
(9	,11	,100),
(10	,12,	80),
(10	,2,	20),
(11,	13,	100),
(12	,3	,50),
(12	,14	,50),
(13	,9	,100),
(14	,15	,45),
(14	,14	,55),
(15	,16	,100),
(16	,14	,45),
(16	,15	,55),
(17	,10	,100),
(18	,16	,30),
(18	,13	,70),
(19	,1	,100),
(20	,12	,20),
(20	,13	,30),
(20	,15	,40),
(20	,16	,10);
