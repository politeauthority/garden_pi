-- MySQL dump 10.13  Distrib 5.5.31, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: garden
-- ------------------------------------------------------
-- Server version	5.5.31-0+wheezy1

--
-- Table structure for table `device_runtime`
--
CREATE DATABASE `garden`;
USE DATABASE `garden`;

DROP TABLE IF EXISTS `device_runtime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `device_runtime` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `device_id` int(30) NOT NULL,
  `date_on` varchar(50) NOT NULL,
  `date_off` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `devices`
--

DROP TABLE IF EXISTS `devices`;

CREATE TABLE `devices` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `status_bit` int(1) NOT NULL,
  `outlet_num` int(10) DEFAULT NULL,
  `type` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `devices_log`
--

DROP TABLE IF EXISTS `devices_log`;

CREATE TABLE `devices_log` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `device_id` varchar(200) NOT NULL,
  `user_id` int(1) NOT NULL,
  `state` int(1) NOT NULL,
  `date` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `garden_options`
--

DROP TABLE IF EXISTS `garden_options`;

CREATE TABLE `garden_options` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `meta_key` varchar(200) NOT NULL,
  `meta_value` varchar(200) NOT NULL,
  `pretty_name` varchar(250) DEFAULT NULL,
  `help_text` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;


--
-- Table structure for table `weather`
--

DROP TABLE IF EXISTS `weather`;

CREATE TABLE `weather` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `indoor_temp_f` varchar(10) DEFAULT NULL,
  `indoor_humidity` varchar(50) DEFAULT NULL,
  `outdoor_temp_f` varchar(50) DEFAULT NULL,
  `outdoor_temp_f_feels` varchar(50) DEFAULT NULL,
  `outdoor_humidity` varchar(60) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1546 DEFAULT CHARSET=latin1;

/* ACL SYSTEM */
CREATE TABLE `acl_app` (
  `ID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `restore` datetime NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1

 CREATE TABLE `acl_permissions` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `permKey` varchar(30) NOT NULL,
  `permName` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `permKey` (`permKey`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `acl_role_perms` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `roleID` bigint(20) NOT NULL,
  `permID` bigint(20) NOT NULL,
  `value` tinyint(1) NOT NULL DEFAULT '0',
  `addDate` datetime NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `roleID_2` (`roleID`,`permID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `acl_roles` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `roleName` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `roleName` (`roleName`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1

 CREATE TABLE `acl_user_perms` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `userID` bigint(20) NOT NULL,
  `permID` bigint(20) NOT NULL,
  `value` tinyint(1) NOT NULL DEFAULT '0',
  `addDate` datetime NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `userID` (`userID`,`permID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

CREATE TABLE `acl_user_roles` (
  `userID` bigint(20) NOT NULL,
  `roleID` bigint(20) NOT NULL,
  `addDate` datetime NOT NULL,
  UNIQUE KEY `userID` (`userID`,`roleID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 