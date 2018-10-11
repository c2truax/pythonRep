-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: mydb
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
-- Table structure for table `emails`
--

DROP TABLE IF EXISTS `emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emails`
--

LOCK TABLES `emails` WRITE;
/*!40000 ALTER TABLE `emails` DISABLE KEYS */;
INSERT INTO `emails` VALUES (8,'art@gmail.com','2018-10-09 00:29:17'),(9,'big@gmail.com','2018-10-09 00:30:57'),(10,'tall@gmail.com','2018-10-09 00:31:49'),(11,'tommy@gmail.com','2018-10-09 00:34:38'),(12,'cct@gmail.com','2018-10-09 00:37:48'),(13,'joe@gmail.com','2018-10-09 00:38:50'),(14,'ali@gmail.com','2018-10-09 00:43:18'),(15,'steph@gmail.com','2018-10-09 00:43:59'),(16,'tbar@gmail.com','2018-10-09 00:45:43'),(17,'george@gmail.com','2018-10-09 00:46:43'),(18,'henry@gmail.com','2018-10-09 00:47:41'),(19,'al@gmail.com','2018-10-09 00:49:10'),(20,'a@gmail.com','2018-10-09 00:50:46'),(21,'chris.truax@e3partners.org','2018-10-09 00:53:00'),(22,'c2truax@gmail.com','2018-10-09 00:55:40'),(23,'gg@gmail.com','2018-10-09 00:57:22'),(24,'b@gmail.com','2018-10-09 00:59:35'),(25,'crittertruax@yahoo.com','2018-10-09 01:15:13'),(26,'t@yahoo.com','2018-10-09 01:17:03'),(27,'t@juno.com','2018-10-09 01:21:24'),(28,'c2truax@juno.com','2018-10-09 01:22:28');
/*!40000 ALTER TABLE `emails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-09  1:24:09
