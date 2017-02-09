drop table if exists room;
drop table if exists staff;



create table room(
	id integer primary key,
	num text,
	department text,
	tel text,
	tel2 text
);

create table staff(
	id integer primary key,
	name text,
	room_id integer,
	cellphone text,
	cellphone2 text,
	littlephone text, 
	littlephone2 text,
	ipaddress text
);


