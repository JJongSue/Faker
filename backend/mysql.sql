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

CREATE TABLE CONTENT (
	CONTENT_ID INT NOT NULL AUTO_INCREMENT,
    USER_ID INT NOT NULL,
    CONTENT_TYPE VARCHAR(10) NOT NULL,
    CONTENT_SRC VARCHAR(100) NOT NULL,
    primary key(CONTENT_ID),
    foreign key(USER_ID) references USER(USER_ID) ON DELETE CASCADE

) DEFAULT CHARSET=UTF8;

CREATE TABLE BOARDER (
	BOARDER_ID INT NOT NULL AUTO_INCREMENT,
    CONTENT_ID INT NOT NULL,
    VIEW_CNT INT NOT NULL,
    BOARDER_TITLE varchar(100) NOT NULL,
    BOARDER_DESCRIPTION text NOT NULL,
    primary key(BOARDER_ID),
    foreign key(CONTENT_ID) references CONTENT(CONTENT_ID) ON DELETE CASCADE
) DEFAULT CHARSET=UTF8;

insert into user(user_id, username, password, gender, age) values(123, "123", "123", "male", 12);

select * from user;
drop table user;
drop table content;
drop table boarder;