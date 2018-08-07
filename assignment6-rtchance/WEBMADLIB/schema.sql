DROP TABLE if exists businesses;
CREATE TABLE businesses (
    id INTEGER, 
    business_name varchar(20) NOT NULL,
    business_type varchar(30) NOT NULL,
    market_type varchar(50) NOT NULL,
    job_to_be_done varchar(100) NOT NULL,
    revenue_model varchar(50) NOT NULL
);

insert into businesses values(0,'Amazon','for-profit organization', 'B2C and B2B customers','various services and affordable and convenient product delivery','direct sales and services');

insert into businesses values(1,'Apple','for-profit organization', 'B2C customers','technology products and services','direct sales');

insert into businesses values(2,'Netflix','for-profit organization','B2C customers','to stream videos in order to "Netflix and chill"','direct sales');

insert into businesses values(3,'Tesla','for-profit organization', 'B2C customers','both transportation and clean air','direct sales');


