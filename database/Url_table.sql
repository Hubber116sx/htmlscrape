use html_scraper;

CREATE TABLE URL (
     id BIGINT NOT NULL AUTO_INCREMENT,
     URL TEXT CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
     FD VARCHAR(3),
     PRIMARY KEY (id),
     CAT1 VARCHAR(10) NOT NULL,
     CAT2 VARCHAR(10) NOT NULL,
     LOC VARCHAR(20) NOT NULL,
     UNIQUE KEY `URL` (`URL`(200))
);
