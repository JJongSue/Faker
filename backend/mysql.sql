create database hns_db;
use hns_db;


create table USER (
	USER_ID int not null AUTO_INCREMENT,
    USERNAME VARCHAR(100) NOT NULL unique,
    PASSWORD VARCHAR(100) NOT NULL,
    GENDER VARCHAR(10),
    AGE INT,
    PRIMARY KEY(USER_ID, USERNAME)
) DEFAULT CHARSET=UTF8;

CREATE TABLE CONTENTS (
	CONTENTS_ID INT NOT NULL AUTO_INCREMENT,
    USER_ID INT NOT NULL,
    CONTENTS_TYPE VARCHAR(10) NOT NULL,
    CONTENTS_SRC VARCHAR(100) NOT NULL,
    primary key(CONTENTS_ID),
    foreign key(USER_ID) references USER(USER_ID) ON DELETE CASCADE

) DEFAULT CHARSET=UTF8;

CREATE TABLE BOARDER (
	BOARDER_ID INT NOT NULL AUTO_INCREMENT,
    CONTENTS_ID INT NOT NULL,
    VIEW_CNT INT NOT NULL,
    BOARDER_TITLE varchar(100) NOT NULL,
    BOARDER_DESCRIPTION text NOT NULL,
    primary key(BOARDER_ID),
    foreign key(CONTENTS_ID) references CONTENTS(CONTENTS_ID) ON DELETE CASCADE
) DEFAULT CHARSET=UTF8;

insert into user(user_id, username, password, gender, age) values(123, "123", "123", "male", 12);

select * from user;
drop table user;
drop table contents;
drop table boarder;