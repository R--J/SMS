# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: localhost (MySQL 5.7.10)
# Database: sms_db
# Generation Time: 2016-05-31 13:54:08 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table activity
# ------------------------------------------------------------

DROP TABLE IF EXISTS `activity`;

CREATE TABLE `activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL DEFAULT '',
  `abstract` varchar(200) DEFAULT '',
  `content` varchar(10000) NOT NULL DEFAULT '',
  `level` varchar(50) NOT NULL DEFAULT '0',
  `publisher_id` char(8) NOT NULL DEFAULT '',
  `start_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `end_time` timestamp NULL DEFAULT NULL,
  `soc_id` int(3) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `publisher_id` (`publisher_id`),
  KEY `society_id` (`soc_id`),
  CONSTRAINT `publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `user` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `society_id` FOREIGN KEY (`soc_id`) REFERENCES `society` (`soc_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table member
# ------------------------------------------------------------

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `stu_id` char(8) NOT NULL DEFAULT '',
  `soc_id` int(3) unsigned NOT NULL,
  `level` varchar(20) NOT NULL DEFAULT '0' COMMENT '0: member, 1: manager',
  PRIMARY KEY (`id`),
  KEY `stu` (`stu_id`),
  KEY `soc` (`soc_id`),
  CONSTRAINT `soc` FOREIGN KEY (`soc_id`) REFERENCES `society` (`soc_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `stu` FOREIGN KEY (`stu_id`) REFERENCES `user` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;

INSERT INTO `member` (`id`, `stu_id`, `soc_id`, `level`)
VALUES
  (5,'13311111',1,'0');

/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

DELIMITER ;;
/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION" */;;
/*!50003 CREATE */ /*!50017 DEFINER=`root`@`localhost` */ /*!50003 TRIGGER `member_insert` AFTER INSERT ON `member` FOR EACH ROW update society
set society.total_member = (
  select count(stu_id) 
  from member 
  where member.soc_id = new.soc_id
)
where society.soc_id = new.soc_id */;;
/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION" */;;
/*!50003 CREATE */ /*!50017 DEFINER=`root`@`localhost` */ /*!50003 TRIGGER `member_delete` AFTER DELETE ON `member` FOR EACH ROW update society
set society.total_member = (
  select count(stu_id) 
  from member 
  where member.soc_id = old.soc_id
)
where society.soc_id = old.soc_id */;;
DELIMITER ;
/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;


# Dump of table society
# ------------------------------------------------------------

DROP TABLE IF EXISTS `society`;

CREATE TABLE `society` (
  `soc_id` int(3) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL DEFAULT '',
  `founded_date` date NOT NULL,
  `tutor` varchar(20) DEFAULT 'None',
  `founder` varchar(20) NOT NULL DEFAULT 'Unknown',
  `president` varchar(20) NOT NULL DEFAULT '',
  `total_member` int(3) unsigned NOT NULL DEFAULT '1' COMMENT 'update after member table changed',
  PRIMARY KEY (`soc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `society` WRITE;
/*!40000 ALTER TABLE `society` DISABLE KEYS */;

INSERT INTO `society` (`soc_id`, `name`, `founded_date`, `tutor`, `founder`, `president`, `total_member`)
VALUES
  (1,'abc','2008-07-04','abc','Unknown','abc',1);

/*!40000 ALTER TABLE `society` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `stu_id` char(8) NOT NULL DEFAULT '',
  `name` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(20) NOT NULL DEFAULT '',
  `email` varchar(50) NOT NULL,
  `gender` int(1) unsigned NOT NULL COMMENT '0:male, 1: female',
  `phone` varchar(20) DEFAULT NULL,
  `age` int(3) unsigned DEFAULT '0',
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;

INSERT INTO `user` (`stu_id`, `name`, `password`, `email`, `gender`, `phone`, `age`)
VALUES
  ('13311111','alice','123','abc',2,NULL,20),
  ('13311112','bob','123','abc',1,NULL,20),
  ('13354023','cjh','123','abcdefg',1,'13750036269',20);

/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
