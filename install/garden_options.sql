-- MySQL dump 10.13  Distrib 5.5.31, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: garden
-- ------------------------------------------------------
-- Server version	5.5.31-0+wheezy1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `garden_options`
--

USE DATABASE `garden`;
DROP TABLE IF EXISTS `garden_options`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `garden_options` (
  `id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `meta_key` varchar(200) NOT NULL,
  `meta_value` varchar(200) NOT NULL,
  `pretty_name` varchar(250) DEFAULT NULL,
  `help_text` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `garden_options`
--

LOCK TABLES `garden_options` WRITE;
/*!40000 ALTER TABLE `garden_options` DISABLE KEYS */;
INSERT INTO `garden_options` VALUES 
       (1,'site-url','','Site Url',NULL),
       (2,'use-sensor-shtx','','SHT1X Sensor',NULL),
       (3,'use-network-weatherunderground','','Weather Unground System',NULL),
       (4,'weatherunderground-apikey','','Weather Underground API key',NULL),
       (5,'use-alert','','Alert System',NULL),
       (6,'alert-opt-temp-high','90','High Temperature Alert',NULL),
       (7,'alert-opt-temp-low','60','Low Temperature Alert',NULL),
       (8,'weatherunderground-zipcode','','Weather Underground: Zipcode',NULL),
       (9,'use-lighttiming','','Light Timing','Use the light timing features'),
       (10,'lighttiming-start','','Start Lights','The time you want to start the lights, ex: 23:32:00'),
       (11,'lighttiming-stop','','Stop Lights','The time you want to shut off the lights, ex: 23:32:00'),
       (12,'use-prowl','','Prowl Notifications','Use the prowl notification process'),
       (13,'prowl-apikey','','Prowl API Key','');
/*!40000 ALTER TABLE `garden_options` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-08-09 16:12:14
