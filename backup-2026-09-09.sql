CREATE DATABASE  IF NOT EXISTS `teste` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `teste`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: teste
-- ------------------------------------------------------
-- Server version	8.4.7

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `configuracao`
--

DROP TABLE IF EXISTS `configuracao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `configuracao` (
  `id` int NOT NULL AUTO_INCREMENT,
  `active` tinyint NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `peca1_id` int NOT NULL,
  `peca2_id` int NOT NULL,
  `peca3_id` int NOT NULL,
  `peca4_id` int NOT NULL,
  `peca5_id` int NOT NULL,
  `peca6_id` int NOT NULL,
  `peca7_id` int DEFAULT NULL,
  `peca8_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `configuracao_peca_id1` (`peca1_id`),
  KEY `configuracao_peca2_id` (`peca2_id`),
  KEY `configuracao_peca3_id` (`peca3_id`),
  KEY `configuracao_peca4_id` (`peca4_id`),
  KEY `configuracao_peca5_id` (`peca5_id`),
  KEY `configuracao_peca6_id` (`peca6_id`),
  KEY `configuracao_peca7_id` (`peca7_id`),
  KEY `configuracao_peca8_id` (`peca8_id`),
  CONSTRAINT `configuracao_peca2_id` FOREIGN KEY (`peca2_id`) REFERENCES `peca` (`id`),
  CONSTRAINT `configuracao_peca3_id` FOREIGN KEY (`peca3_id`) REFERENCES `peca` (`id`),
  CONSTRAINT `configuracao_peca4_id` FOREIGN KEY (`peca4_id`) REFERENCES `peca` (`id`),
  CONSTRAINT `configuracao_peca5_id` FOREIGN KEY (`peca5_id`) REFERENCES `peca` (`id`),
  CONSTRAINT `configuracao_peca6_id` FOREIGN KEY (`peca6_id`) REFERENCES `peca` (`id`),
  CONSTRAINT `configuracao_peca7_id` FOREIGN KEY (`peca7_id`) REFERENCES `peca` (`id`),
  CONSTRAINT `configuracao_peca8_id` FOREIGN KEY (`peca8_id`) REFERENCES `peca` (`id`),
  CONSTRAINT `configuracao_peca_id1` FOREIGN KEY (`peca1_id`) REFERENCES `peca` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configuracao`
--

LOCK TABLES `configuracao` WRITE;
/*!40000 ALTER TABLE `configuracao` DISABLE KEYS */;
INSERT INTO `configuracao` VALUES (5,1,'2026-09-08 23:20:57','2026-09-08 23:20:57',1,2,3,4,5,6,7,8),(6,1,'2026-09-08 23:36:02','2026-09-08 23:36:02',9,10,11,12,13,14,15,16),(7,1,'2026-09-08 23:36:23','2026-09-08 23:36:23',17,18,19,20,21,22,23,24);
/*!40000 ALTER TABLE `configuracao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fabricante`
--

DROP TABLE IF EXISTS `fabricante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fabricante` (
  `id` int NOT NULL AUTO_INCREMENT,
  `active` tinyint NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `nome` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `qualidade` smallint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fabricante`
--

LOCK TABLES `fabricante` WRITE;
/*!40000 ALTER TABLE `fabricante` DISABLE KEYS */;
INSERT INTO `fabricante` VALUES (1,1,'2026-09-08 22:34:57','2026-09-08 22:48:09','Gigabyte',10),(6,1,'2026-09-08 22:40:42','2026-09-08 22:40:42','mancer',2),(7,1,'2026-09-08 22:42:29','2026-09-08 22:42:29','asus',7),(8,1,'2026-09-08 22:43:07','2026-09-08 22:43:07','MSI',5),(9,1,'2026-09-08 22:47:21','2026-09-08 22:58:42','GALAX',7),(10,1,'2026-09-08 22:56:03','2026-09-08 22:56:28','Intel',9),(11,1,'2026-09-08 22:57:52','2026-09-08 22:58:54','AMD',9),(12,1,'2026-09-08 23:10:05','2026-09-08 23:10:30','kingston',7),(13,1,'2026-09-08 23:12:43','2026-09-08 23:12:43','Corsaire',7),(14,1,'2026-09-08 23:26:55','2026-09-08 23:26:55','Redragon',10),(15,1,'2026-09-08 23:28:03','2026-09-08 23:28:03','DeepCool',6),(16,1,'2026-09-08 23:32:26','2026-09-08 23:32:26','Samsung',10),(17,1,'2026-09-08 23:34:43','2026-09-08 23:34:43','Cooler Master',8);
/*!40000 ALTER TABLE `fabricante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peca`
--

DROP TABLE IF EXISTS `peca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peca` (
  `id` int NOT NULL AUTO_INCREMENT,
  `active` tinyint NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `nome` varchar(55) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tipo_id` int NOT NULL,
  `modelo` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fabricante_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `peca_tipo_id` (`tipo_id`),
  KEY `peca_fabricante_id` (`fabricante_id`),
  CONSTRAINT `peca_fabricante_id` FOREIGN KEY (`fabricante_id`) REFERENCES `fabricante` (`id`),
  CONSTRAINT `peca_tipo_id` FOREIGN KEY (`tipo_id`) REFERENCES `tipo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peca`
--

LOCK TABLES `peca` WRITE;
/*!40000 ALTER TABLE `peca` DISABLE KEYS */;
INSERT INTO `peca` VALUES (1,1,'2026-09-08 23:00:56','2026-09-08 23:00:56','Intel i5 12400f',1,'i5',10),(2,1,'2026-09-08 23:07:50','2026-09-08 23:07:50','Asus Prime H610M',2,'H610M',7),(3,1,'2026-09-08 23:09:03','2026-09-08 23:09:03','RTX 3050 GALAXY',3,'RTX',9),(4,1,'2026-09-08 23:10:57','2026-09-08 23:10:57','SSD 480GB',4,'SSD',12),(5,1,'2026-09-08 23:11:42','2026-09-08 23:11:42','8GB DDR4 3200',5,'Memoria Ram',12),(6,1,'2026-09-08 23:13:25','2026-09-08 23:13:25','500W 80+ Bronze',6,'fonte',13),(7,1,'2026-09-08 23:14:12','2026-09-08 23:14:12','Mancer CV100',7,'Gabinete',7),(8,1,'2026-09-08 23:14:43','2026-09-08 23:14:43','Cooler Box',8,'Cooler',10),(9,1,'2026-09-08 23:23:19','2026-09-08 23:23:19','Intel i5 13400F',1,'i5',10),(10,1,'2026-09-08 23:24:23','2026-09-08 23:24:23','Asus TUF B660M',2,'B660M',7),(11,1,'2026-09-08 23:25:05','2026-09-08 23:25:05','RTX 4060',3,'RTX',7),(12,1,'2026-09-08 23:25:33','2026-09-08 23:25:33','SSD 1TB NVMe',4,'SSD',12),(13,1,'2026-09-08 23:25:58','2026-09-08 23:25:58','16GB DDR4 3600',5,'memoria',12),(14,1,'2026-09-08 23:26:23','2026-09-08 23:26:23','600W 80+ Bronze',6,'fonte',13),(15,1,'2026-09-08 23:27:28','2026-09-08 23:27:28','Redragon Diamond Storm',7,'gabinete',14),(16,1,'2026-09-08 23:28:39','2026-09-08 23:28:39','Air Cooler 120mm',8,'Air Cooler',15),(17,1,'2026-09-08 23:30:17','2026-09-08 23:30:17','AMD Ryzen 7 7800X3D',1,'ryzen 7',11),(18,1,'2026-09-08 23:31:06','2026-09-08 23:31:06','Asus ROG Strix X670E',2,'X670E',7),(19,1,'2026-09-08 23:31:57','2026-09-08 23:31:57','Gigabyte RTX 5080',3,'RTX',1),(20,1,'2026-09-08 23:32:41','2026-09-08 23:32:41','SSD 2TB NVMe Gen4',4,'SSD',16),(21,1,'2026-09-08 23:33:14','2026-09-08 23:33:14','32GB DDR5 6000',5,'memoria',12),(22,1,'2026-09-08 23:33:41','2026-09-08 23:33:41','850W 80+ Gold',6,'fonte',13),(23,1,'2026-09-08 23:34:23','2026-09-08 23:34:23','Asus ROG Hyperion GR701',7,'Gabinete',7),(24,1,'2026-09-08 23:35:32','2026-09-08 23:35:32','Water Cooler Cooler Master MasterLiquid 240mm',8,'Water Cooler',17);
/*!40000 ALTER TABLE `peca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo`
--

DROP TABLE IF EXISTS `tipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `active` tinyint NOT NULL DEFAULT '1',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `nome` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo`
--

LOCK TABLES `tipo` WRITE;
/*!40000 ALTER TABLE `tipo` DISABLE KEYS */;
INSERT INTO `tipo` VALUES (1,1,'2026-09-08 22:24:35','2026-09-08 22:24:35','cpu'),(2,1,'2026-09-08 22:26:51','2026-09-08 22:26:51','placa-mae'),(3,1,'2026-09-08 22:26:51','2026-09-08 22:26:51','gpu'),(4,1,'2026-09-08 22:28:05','2026-09-08 22:32:48','armazenamento'),(5,1,'2026-09-08 22:33:15','2026-09-08 22:33:15','memoria'),(6,1,'2026-09-08 22:33:38','2026-09-08 22:33:38','fonte'),(7,1,'2026-09-08 22:33:46','2026-09-08 22:33:46','gabinete'),(8,1,'2026-09-08 22:49:47','2026-09-08 22:49:47','Cooler');
/*!40000 ALTER TABLE `tipo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-09 20:18:00
