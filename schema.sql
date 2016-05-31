# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.11)
# Database: sms
# Generation Time: 2016-05-30 19:36:38 +0000
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


DELIMITER ;;
/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION" */;;
/*!50003 CREATE */ /*!50017 DEFINER=`root`@`localhost` */ /*!50003 TRIGGER `member_insert` AFTER INSERT ON `member` FOR EACH ROW update society
set society.total_member = count(member.stu_id)
where society.soc_id = inserted.soc_id and member.soc_id = inserted.soc_id */;;
/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION" */;;
/*!50003 CREATE */ /*!50017 DEFINER=`root`@`localhost` */ /*!50003 TRIGGER `member_delete` AFTER DELETE ON `member` FOR EACH ROW update society
set society.total_member = count(member.stu_id)
where society.soc_id = inserted.soc_id and member.soc_id = inserted.soc_id */;;
DELIMITER ;
/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;


# Dump of table society
# ------------------------------------------------------------

DROP TABLE IF EXISTS `society`;

CREATE TABLE `society` (
  `soc_id` int(3) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL DEFAULT '',
  `founded_date` date NOT NULL,
  `tutor` varchar(20) NOT NULL DEFAULT '',
  `founder` varchar(20) DEFAULT 'Unknown',
  `president` varchar(20) NOT NULL DEFAULT '',
  `total_member` int(3) unsigned NOT NULL DEFAULT '1' COMMENT 'update after member table changed',
  PRIMARY KEY (`soc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `stu_id` char(8) NOT NULL DEFAULT '',
  `name` varchar(20) NOT NULL DEFAULT '',
  `password` varchar(20) NOT NULL DEFAULT '',
  `email` varchar(50) NOT NULL,
  `gender` int(1) unsigned DEFAULT '0' COMMENT '0: unknown, 1: male, 2: female',
  `phone` varchar(20) DEFAULT NULL,
  `age` int(3) unsigned DEFAULT '0',
  PRIMARY KEY (`stu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
