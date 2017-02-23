drop table if exists room;
drop table if exists staff;



create table room(
	id integer primary key,
	num text,
	department text,
	tel text,
	tel2 text,
	littletel text, 
	littletel2 text
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

create table document(
	id integer primary key autoincrement,
	serial_number integer, -- 顺序号
	received_date date, -- 收文日期
	from_department text, -- 来文机关
	document_number text, -- 文件号码
	secret_degree text, -- 秘密程度
	document_date date, -- 文件日期
	document_name text, -- 文件名称
	copy integer, -- 份数
	to_staff text, -- 交办人
	recycle_date date -- 收回日期
);

