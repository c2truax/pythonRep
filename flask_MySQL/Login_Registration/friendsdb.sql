-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: friendsdb
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
-- Table structure for table `friends`
--

DROP TABLE IF EXISTS `friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `friends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `occupation` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `salt` varchar(60) DEFAULT NULL,
  `password` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friends`
--

LOCK TABLES `friends` WRITE;
/*!40000 ALTER TABLE `friends` DISABLE KEYS */;
INSERT INTO `friends` VALUES (1,'ryan','churay','programmer','2018-10-08 14:49:50',NULL,'ryan@ryan.com',NULL,NULL),(2,'bob','robertson','builder','2018-10-08 14:49:54',NULL,'bob@bob.com',NULL,NULL),(3,'george','springer','hitter of dingers','2018-10-08 14:49:57',NULL,'george@george.com',NULL,NULL),(4,'jose','altuve','baseball','2018-10-08 15:40:13','2018-10-08 15:40:13','jose@jose.com',NULL,NULL),(5,'alex','bregman',NULL,'2018-10-09 12:08:54','2018-10-09 12:08:54','abreg@astros.com',NULL,'$2b$12$LZ2PBRWKY1p9hMqlKxPdveGUSDdz1kRNZSwXBWaY.bA1mP4GGDN7u'),(6,'chris','truax',NULL,'2018-10-09 12:17:31','2018-10-09 12:17:31','chris@t.com',NULL,'$2b$12$CHGECfQ6Q4Dnw9PjY9vgie3Taq6HLdjIEJWElFkX3UU2QNAtFPb5i'),(7,'bob','bobbertson',NULL,'2018-10-09 12:19:27','2018-10-09 12:19:27','bobby@b.com',NULL,'$2b$12$.I2TdjoIGSqAZUDifWoy7e5Wo08w78EbZ5GFUf51oAUpKW6oMBqkC'),(8,'marwin','gonzales',NULL,'2018-10-09 13:48:40','2018-10-09 13:48:40','mg@gon.com',NULL,'$2b$12$EgZKJ5.pDlstGjBIzXE7n.ImGqlKOSowONDshMUw0U2sIGk8yp7nC'),(9,'josh','reddick',NULL,'2018-10-09 14:03:19','2018-10-09 14:03:19','jreddick@astros.com',NULL,'$2b$12$lDZ4W7TXmpVxG7aMZQPyI.wJGRCgZefJcb0dPf7gHeQUnd1Jgp3Jq');
/*!40000 ALTER TABLE `friends` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-09 14:07:21
