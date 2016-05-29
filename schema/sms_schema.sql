# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: localhost (MySQL 5.7.10)
# Database: sms_db
# Generation Time: 2016-05-29 08:35:23 +0000
# ************************************************************


# Dump of table member
# ------------------------------------------------------------

DROP TABLE IF EXISTS `member`;
CREATE TABLE `member` (
  `stu_id` char(8) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  `age` int(11) unsigned DEFAULT NULL,
  `gender` varchar(6) NOT NULL DEFAULT '',
  `phone` char(11) NOT NULL DEFAULT '',
  `password` varchar(30) NOT NULL DEFAULT '123456',
  `level` int(11) unsigned NOT NULL DEFAULT '1',
  `society_list` mediumtext,
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
