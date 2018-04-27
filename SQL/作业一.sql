-- --------------------
-- create S table
-- --------------------
CREATE TABLE S
(
	sno         char(2)  UNIQUE ,
	sname    char(6) ,
	status     char(2) ,
	city         char(4)
);
-- --------------------
-- create P table
-- --------------------
CREATE TABLE P
(
	pno			  char(2)  UNIQUE,
	pname		  char(6),
	color	      char(2),
	weight	      INT
);
-- --------------------
-- create J table
-- --------------------
CREATE  TABLE  J
(
	jno  			char(2) UNIQUE,
	jname  	char(8),
	city 			char(4)
);
-- -----------------------
-- create SPJ table
-- -----------------------
CREATE TABLE SPJ
(
	sno  	char(2),
	pno  	char(2),
	jno 	    char(2),
    qty  	    INT
);
