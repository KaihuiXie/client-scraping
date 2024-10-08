USE contact_db;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    mobileNo VARCHAR(50),
    phoneNum VARCHAR(50),
    address VARCHAR(255),
    companyName VARCHAR(255),
    jobTitle VARCHAR(255),
    domain VARCHAR(255),
    isMale VARCHAR(10),
    moreInfoLink VARCHAR(255),
    memberId VARCHAR(255) UNIQUE,
    qrCode VARCHAR(255),
    pageUrl VARCHAR(255),
    crawl_time DATETIME
);