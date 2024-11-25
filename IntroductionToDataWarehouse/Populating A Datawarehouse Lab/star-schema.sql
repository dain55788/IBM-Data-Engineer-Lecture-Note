CREATE TABLE "DimCustomer"(customerid integer NOT NULL PRIMARY KEY,category varchar(10) NOT NULL,country varchar(40) NOT NULL,industry varchar(40) NOT NULL);


CREATE TABLE "DimMonth"(monthid integer NOT NULL PRIMARY KEY,year integer NOT NULL,month integer NOT NULL,monthname varchar(10) NOT NULL,quarter integer NOT NULL,quartername varchar(2) NOT NULL);


CREATE TABLE "FactBilling"(billid integer not null primary key,customerid integer NOT NULL,monthid integer NOT NULL,billedamount integer NOT NULL,
FOREIGN KEY (customerid) REFERENCES "DimCustomer" (customerid),FOREIGN KEY (monthid) REFERENCES "DimMonth" (monthid));







