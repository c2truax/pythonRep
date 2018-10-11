CREATE DATABASE  IF NOT EXISTS `walldb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `walldb`;
-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: walldb
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `update_at` datetime DEFAULT NULL,
  `recipient_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_message_user_idx` (`recipient_id`),
  KEY `fk_message_user1_idx` (`user_id`),
  CONSTRAINT `fk_message_user` FOREIGN KEY (`recipient_id`) REFERENCES `user` (`id`),
  CONSTRAINT `fk_message_user1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (5,'test','2018-10-09 22:24:54','2018-10-09 22:24:54',1,4),(8,'dobby','2018-10-09 23:59:37','2018-10-09 23:59:37',2,4),(9,'yes yes yes','2018-10-09 23:59:46','2018-10-09 23:59:46',3,4),(22,'rrrrrrrr','2018-10-10 13:17:04','2018-10-10 13:17:04',1,4),(24,'rrrrrr','2018-10-10 13:21:15','2018-10-10 13:21:15',1,4),(25,'rrrrrrr','2018-10-10 13:23:27','2018-10-10 13:23:27',1,4),(26,'rrrrrrr','2018-10-10 13:24:46','2018-10-10 13:24:46',1,4),(27,'rrrrrrr','2018-10-10 13:25:05','2018-10-10 13:25:05',1,4),(29,'rrrr','2018-10-10 13:45:24','2018-10-10 13:45:24',1,4),(30,'rrrrrr','2018-10-10 13:47:37','2018-10-10 13:47:37',2,4),(31,'rrrrrr','2018-10-10 13:49:25','2018-10-10 13:49:25',1,4),(32,'rrrrrr','2018-10-10 13:52:33','2018-10-10 13:52:33',1,5),(33,'rrrrrrr','2018-10-10 14:01:15','2018-10-10 14:01:15',1,4),(34,'rrrrrr','2018-10-10 14:01:31','2018-10-10 14:01:31',2,4),(35,'rrrrr','2018-10-10 14:01:34','2018-10-10 14:01:34',3,4),(36,'rrrr','2018-10-10 14:01:38','2018-10-10 14:01:38',5,4),(37,'rrrr','2018-10-10 14:06:15','2018-10-10 14:06:15',1,4),(38,'rrrrr','2018-10-10 14:06:24','2018-10-10 14:06:24',1,4),(39,'rrrr','2018-10-10 14:06:28','2018-10-10 14:06:28',3,4),(40,'rrrrrr','2018-10-10 14:12:25','2018-10-10 14:12:25',1,4),(41,'rrrr','2018-10-10 14:13:20','2018-10-10 14:13:20',1,4),(42,'rrrr','2018-10-10 14:15:21','2018-10-10 14:15:21',1,4),(43,'44444','2018-10-10 14:21:01','2018-10-10 14:21:01',1,4),(44,'fffff','2018-10-10 14:21:06','2018-10-10 14:21:06',1,4),(45,'fff','2018-10-10 14:21:09','2018-10-10 14:21:09',2,4),(46,'ffff','2018-10-10 14:21:12','2018-10-10 14:21:12',3,4),(48,'erererer','2018-10-10 14:21:34','2018-10-10 14:21:34',1,5),(49,'erererer','2018-10-10 14:21:38','2018-10-10 14:21:38',2,5),(50,'ffff','2018-10-10 14:23:13','2018-10-10 14:23:13',1,5),(51,'gggg','2018-10-10 14:23:32','2018-10-10 14:23:32',4,5),(52,'fffff\r\n','2018-10-10 14:43:40','2018-10-10 14:43:40',1,5),(53,'rrrrrrrrr','2018-10-10 14:43:46','2018-10-10 14:43:46',1,5),(54,'fff','2018-10-10 15:01:37','2018-10-10 15:01:37',1,5),(55,'ffff','2018-10-10 15:03:20','2018-10-10 15:03:20',1,5),(56,'ffff','2018-10-10 15:05:05','2018-10-10 15:05:05',5,4),(57,'iudwhfiushfiuahdihaidh\r\n\r\nasdiahdi\r\nasjdhiaushd\r\nasdihasidhas','2018-10-10 15:12:29','2018-10-10 15:12:29',1,4);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Admin','dump','ryan@ryan.com','$2b$12$x0KHZZ5.oZe1qwOKQOvAxOipD26C3ZDhZpHMFCiDWFVWsC6vIpOGq','2018-10-09 14:55:55','2018-10-09 14:55:55'),(2,'jose','altuve','altuve@altuve.com','$2b$12$p5Jar5BZYvoWIa7viHWOrexmHgWDcvqjqrsWszblrEUv0J/7jaWZe','2018-10-09 14:57:32','2018-10-09 14:57:32'),(3,'alex','bregman','abreg@breg.com','$2b$12$z2c8A4ly0blFcwDsUeE/w.rOQf6lk20mLq0w4AgCOS1VM/MhPyzzC','2018-10-09 14:57:56','2018-10-09 14:57:56'),(4,'Christopher','Truax','chris@truax.com','$2b$12$QUSNY3eb8zC4dvOrC0UrH.SknbgzJoc1eqvwkLOhrL9L1C9uyMr0a','2018-10-09 17:51:02','2018-10-09 17:51:02'),(5,'Natalie','Truax','natalie@truax.com','$2b$12$n0twgAV84rAy0PPImGxXP.51SVX3XeJVIWh0sH1xeB3eowpYrqe26','2018-10-09 19:04:58','2018-10-09 19:04:58');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-10 15:44:57
