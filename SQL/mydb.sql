CREATE TABLE employees (
    id int DEFAULT '0' NOT NULL,
    first varchar(20),
    last varchar(20),
    address varchar(255),
    position varchar(50)
    );

INSERT INTO employees VALUES (1,'Bob','Smith','128 Here St, Cityname','Marketing Manager');

INSERT INTO employees VALUES (2,'John','Roberts','45 There St , Townville','Telephonist');
INSERT INTO employees VALUES (3,'Brad','Johnson','1/34 Nowhere Blvd,Snowston','Doorman');
