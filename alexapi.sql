-- MySQL dump 10.13  Distrib 5.5.50, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: alexapi
-- ------------------------------------------------------
-- Server version	5.5.50-0+deb8u1

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
-- Table structure for table `cardio`
--

DROP TABLE IF EXISTS `cardio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cardio` (
  `run_id` int(11) NOT NULL AUTO_INCREMENT,
  `run_time` datetime DEFAULT NULL,
  `start_steps` decimal(10,0) DEFAULT NULL,
  `end_steps` decimal(10,0) DEFAULT NULL,
  `start_distance` decimal(10,0) DEFAULT NULL,
  `end_distance` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`run_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardio`
--

LOCK TABLES `cardio` WRITE;
/*!40000 ALTER TABLE `cardio` DISABLE KEYS */;
INSERT INTO `cardio` VALUES (24,'0000-00-00 00:00:00',5596,NULL,3,NULL),(25,'0000-00-00 00:00:00',5596,NULL,3,NULL),(26,'0000-00-00 00:00:00',5596,NULL,3,NULL),(27,'0000-00-00 00:00:00',5596,NULL,3,NULL),(28,'0000-00-00 00:00:00',5596,NULL,3,NULL),(29,'0000-00-00 00:00:00',5596,NULL,3,NULL),(30,'0000-00-00 00:00:00',5596,NULL,3,NULL),(31,NULL,0,NULL,0,NULL),(32,NULL,0,NULL,0,NULL),(33,NULL,0,NULL,0,NULL),(34,NULL,0,NULL,0,NULL),(35,'0000-00-00 00:00:00',0,NULL,0,NULL),(36,'0000-00-00 00:00:00',0,NULL,0,NULL),(37,'0000-00-00 00:00:00',0,NULL,0,NULL);
/*!40000 ALTER TABLE `cardio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercises`
--

DROP TABLE IF EXISTS `exercises`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercises` (
  `exercise_id` int(11) NOT NULL AUTO_INCREMENT,
  `day_id` decimal(10,0) DEFAULT NULL,
  `exercise` text,
  `sets` decimal(10,0) DEFAULT NULL,
  `reps` decimal(10,0) DEFAULT NULL,
  `rest` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`exercise_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercises`
--

LOCK TABLES `exercises` WRITE;
/*!40000 ALTER TABLE `exercises` DISABLE KEYS */;
INSERT INTO `exercises` VALUES (1,0,'barbell bench press',5,8,60),(2,0,' incline dumbbell bench press',4,12,60),(3,0,'cable flys',4,20,45),(4,0,'dips',3,8,45),(5,1,'barbell deadlifts',5,5,60),(6,1,'lat pulldowns',4,12,45),(7,1,'one arm dumbbell rows',4,12,45),(8,1,'weighted pull ups',4,8,45),(9,2,'barbell back squats',10,10,60),(10,2,'leg extensions',4,20,60),(11,2,'leg press',4,12,60),(12,2,'leg curls',4,20,45),(13,5,'barbell back squats',10,10,60),(14,5,'leg extensions',4,20,60),(15,5,'leg press',4,12,60),(16,5,'leg curls',4,20,45);
/*!40000 ALTER TABLE `exercises` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sets`
--

DROP TABLE IF EXISTS `sets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sets` (
  `set_id` int(11) NOT NULL AUTO_INCREMENT,
  `exercise_id` decimal(10,0) DEFAULT NULL,
  `set_number` decimal(10,0) DEFAULT NULL,
  `weight` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`set_id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sets`
--

LOCK TABLES `sets` WRITE;
/*!40000 ALTER TABLE `sets` DISABLE KEYS */;
INSERT INTO `sets` VALUES (1,1,1,45),(2,1,2,45),(3,1,3,45),(4,1,4,45),(5,1,5,45),(6,2,1,50),(7,2,2,50),(8,2,3,50),(9,2,4,50),(10,3,1,50),(11,3,2,50),(12,3,3,50),(13,3,4,50),(14,4,1,50),(15,4,2,50),(16,4,3,50),(17,5,1,50),(18,5,2,50),(19,5,3,50),(20,5,4,50),(21,5,5,225),(22,6,1,50),(23,6,2,50),(24,6,3,50),(25,6,4,225),(26,7,1,50),(27,7,2,NULL),(28,7,3,NULL),(29,7,4,NULL),(30,8,1,NULL),(31,8,2,NULL),(32,8,3,NULL),(33,8,4,NULL),(34,9,1,NULL),(35,9,2,NULL),(36,9,3,NULL),(37,9,4,NULL),(38,9,5,NULL),(39,9,6,NULL),(40,9,7,NULL),(41,9,9,NULL),(42,9,9,NULL),(43,9,10,NULL),(44,9,1,NULL),(45,9,2,NULL),(46,9,3,NULL),(47,9,4,NULL),(48,10,1,NULL),(49,10,2,NULL),(50,10,3,NULL),(51,10,4,NULL),(52,11,1,NULL),(53,11,2,NULL),(54,11,3,NULL),(55,11,4,NULL),(56,12,1,NULL),(57,12,2,NULL),(58,12,3,NULL),(59,12,4,NULL),(60,13,1,NULL),(61,13,2,NULL),(62,13,3,NULL),(63,13,4,NULL),(64,13,5,NULL),(65,13,6,NULL),(66,13,7,NULL),(67,13,13,NULL),(68,13,13,NULL),(69,13,10,NULL),(70,13,1,NULL),(71,13,2,NULL),(72,13,3,NULL),(73,13,4,NULL),(74,14,1,NULL),(75,14,2,NULL),(76,14,3,NULL),(77,14,4,NULL),(78,15,1,NULL),(79,15,2,NULL),(80,15,3,NULL),(81,15,4,NULL),(82,16,1,NULL),(83,16,2,NULL),(84,16,3,NULL),(85,16,4,NULL);
/*!40000 ALTER TABLE `sets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workouts`
--

DROP TABLE IF EXISTS `workouts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `workouts` (
  `day` decimal(10,0) NOT NULL DEFAULT '0',
  `muscle_group` text,
  `workout_date` date DEFAULT NULL,
  PRIMARY KEY (`day`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workouts`
--

LOCK TABLES `workouts` WRITE;
/*!40000 ALTER TABLE `workouts` DISABLE KEYS */;
INSERT INTO `workouts` VALUES (0,'Chest','2016-08-21'),(1,'Back','2016-08-22'),(2,'Legs','2016-08-23'),(3,'Chest','2016-08-28'),(4,'Back','2016-08-29'),(5,'Legs','2016-08-30');
/*!40000 ALTER TABLE `workouts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

