-- MySQL dump 10.16  Distrib 10.1.48-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.48-MariaDB-0+deb9u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dbo.Active_Customers_From_Same_City`
--

DROP TABLE IF EXISTS `dbo.Active_Customers_From_Same_City`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Active_Customers_From_Same_City` (
  `Customer_ID` varchar(10) DEFAULT NULL,
  `Customer_Name` varchar(9) DEFAULT NULL,
  `Order_IDs` varchar(8) DEFAULT NULL,
  `Order_Status` varchar(9) DEFAULT NULL,
  `Delivery_Location` varchar(9) DEFAULT NULL,
  `Origin_Location` varchar(14) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Active_Customers_From_Same_City`
--

LOCK TABLES `dbo.Active_Customers_From_Same_City` WRITE;
/*!40000 ALTER TABLE `dbo.Active_Customers_From_Same_City` DISABLE KEYS */;
INSERT INTO `dbo.Active_Customers_From_Same_City` VALUES ('Cust_00455','Sarjit','OD539599','Active','Lucknow','Shivamogga'),('Cust_00447','Ronak','OD539597','Delivered','Raipur','Agartala'),('Cust_00321','Shreyansh','OD539591','Active','Hyderabad','Bikaner'),('Cust_00311','Mayank','OD539587','Returned','Amravati','Rangpo'),('Cust_00455','Sarjit','OD538923','Active','Lucknow','Dindigul'),('Cust_00425','Aslam','OD538776','Active','Kolkata','Nellore'),('Cust_00301','Haider','OD538666','Delivered','Guwahati','Darbhanga'),('Cust_00447','Ronak','OD538599','Active','Raipur','Kollam'),('Cust_00311','Mayank','OD538593','Active','Amravati','Moga'),('Cust_00455','Sarjit','OD538590','Delivered','Lucknow','Kottayam'),('Cust_00455','Sarjit','OD537991','Returned','Lucknow','Margao'),('Cust_00455','Sarjit','OD537877','Delivered','Lucknow','Chamarajanagar'),('Cust_00447','Ronak','OD537875','Returned','Raipur','Pandharpur'),('Cust_00321','Shreyansh','OD537871','Delivered','Hyderabad','Kohima'),('Cust_00425','Aslam','OD536776','Returned','Kolkata','Tinsukia'),('Cust_00425','Aslam','OD536775','Returned','Kolkata','Leh'),('Cust_00425','Aslam','OD536772','Returned','Kolkata','Vidisha'),('Cust_00301','Haider','OD536663','Returned','Guwahati','Jammu'),('Cust_00297','Ravi','OD536523','Active','Raipur','Kangra');
/*!40000 ALTER TABLE `dbo.Active_Customers_From_Same_City` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.ComputedColumnTable_Query`
--

DROP TABLE IF EXISTS `dbo.ComputedColumnTable_Query`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.ComputedColumnTable_Query` (
  `VisitorID` tinyint(4) DEFAULT NULL,
  `VisitorName` varchar(6) DEFAULT NULL,
  `FeesPaid` decimal(4,1) DEFAULT NULL,
  `TaxCollected` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.ComputedColumnTable_Query`
--

LOCK TABLES `dbo.ComputedColumnTable_Query` WRITE;
/*!40000 ALTER TABLE `dbo.ComputedColumnTable_Query` DISABLE KEYS */;
INSERT INTO `dbo.ComputedColumnTable_Query` VALUES (1,'Sarjit',100.0,5.0),(2,'Aslam',200.0,10.0),(3,'Ronak',300.0,15.0);
/*!40000 ALTER TABLE `dbo.ComputedColumnTable_Query` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.ComputedColumnTable_UI`
--

DROP TABLE IF EXISTS `dbo.ComputedColumnTable_UI`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.ComputedColumnTable_UI` (
  `VisitorID` tinyint(4) DEFAULT NULL,
  `VisitorName` varchar(6) DEFAULT NULL,
  `FeesPaid` decimal(4,1) DEFAULT NULL,
  `TaxCollected` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.ComputedColumnTable_UI`
--

LOCK TABLES `dbo.ComputedColumnTable_UI` WRITE;
/*!40000 ALTER TABLE `dbo.ComputedColumnTable_UI` DISABLE KEYS */;
INSERT INTO `dbo.ComputedColumnTable_UI` VALUES (1,'Sarjit',100.0,5.0),(2,'Aslam',200.0,10.0),(3,'Ronak',300.0,15.0);
/*!40000 ALTER TABLE `dbo.ComputedColumnTable_UI` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.CutOff_STUDENTS`
--

DROP TABLE IF EXISTS `dbo.CutOff_STUDENTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.CutOff_STUDENTS` (
  `SId` tinyint(4) DEFAULT NULL,
  `SName` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.CutOff_STUDENTS`
--

LOCK TABLES `dbo.CutOff_STUDENTS` WRITE;
/*!40000 ALTER TABLE `dbo.CutOff_STUDENTS` DISABLE KEYS */;
INSERT INTO `dbo.CutOff_STUDENTS` VALUES (1,'Aquib'),(2,'Kumar'),(3,'Sarjit'),(4,'Mayank'),(5,'Shreyansh');
/*!40000 ALTER TABLE `dbo.CutOff_STUDENTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.CutOff_S_MARKS`
--

DROP TABLE IF EXISTS `dbo.CutOff_S_MARKS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.CutOff_S_MARKS` (
  `SId` tinyint(4) DEFAULT NULL,
  `SubName` varchar(7) DEFAULT NULL,
  `Marks` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.CutOff_S_MARKS`
--

LOCK TABLES `dbo.CutOff_S_MARKS` WRITE;
/*!40000 ALTER TABLE `dbo.CutOff_S_MARKS` DISABLE KEYS */;
INSERT INTO `dbo.CutOff_S_MARKS` VALUES (1,'Maths',35),(1,'English',45),(1,'Science',36),(2,'Maths',39),(2,'English',47),(2,'Science',43),(3,'Maths',42),(3,'English',41),(3,'Science',39),(4,'Maths',47),(4,'English',47),(4,'Science',49),(5,'Maths',48),(5,'English',43),(5,'Science',45);
/*!40000 ALTER TABLE `dbo.CutOff_S_MARKS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Department_Wise_Top_3_Salaries`
--

DROP TABLE IF EXISTS `dbo.Department_Wise_Top_3_Salaries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Department_Wise_Top_3_Salaries` (
  `EmpID` varchar(7) DEFAULT NULL,
  `EmpName` varchar(9) DEFAULT NULL,
  `DeptID` varchar(7) DEFAULT NULL,
  `EmpSalary` decimal(6,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Department_Wise_Top_3_Salaries`
--

LOCK TABLES `dbo.Department_Wise_Top_3_Salaries` WRITE;
/*!40000 ALTER TABLE `dbo.Department_Wise_Top_3_Salaries` DISABLE KEYS */;
INSERT INTO `dbo.Department_Wise_Top_3_Salaries` VALUES ('COMP001','Sarjit','DEPT003',45000.0),('COMP002','Ronak','DEPT001',49000.0),('COMP003','Aquib','DEPT003',45001.0),('COMP004','Shreyansh','DEPT002',57000.0),('COMP005','Mayank','DEPT001',51000.0),('COMP006','Ankit','DEPT004',61000.0),('COMP007','Ajay','DEPT004',63000.0),('COMP008','Pankaj','DEPT003',47000.0),('COMP009','Haider','DEPT003',48000.0),('COMP010','Sami','DEPT001',49500.0),('COMP011','Aslam','DEPT001',48500.0),('COMP012','Ravi','DEPT001',49000.0);
/*!40000 ALTER TABLE `dbo.Department_Wise_Top_3_Salaries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Dept_Wise_Top_3_Salaries_DeptDetails`
--

DROP TABLE IF EXISTS `dbo.Dept_Wise_Top_3_Salaries_DeptDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Dept_Wise_Top_3_Salaries_DeptDetails` (
  `EmpID` varchar(7) DEFAULT NULL,
  `DeptID` varchar(7) DEFAULT NULL,
  `DeptName` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Dept_Wise_Top_3_Salaries_DeptDetails`
--

LOCK TABLES `dbo.Dept_Wise_Top_3_Salaries_DeptDetails` WRITE;
/*!40000 ALTER TABLE `dbo.Dept_Wise_Top_3_Salaries_DeptDetails` DISABLE KEYS */;
INSERT INTO `dbo.Dept_Wise_Top_3_Salaries_DeptDetails` VALUES ('COMP001','DEPT003','Security'),('COMP002','DEPT001','IT'),('COMP003','DEPT003','Security'),('COMP004','DEPT002','Pantry'),('COMP005','DEPT001','IT'),('COMP006','DEPT004','Accounts'),('COMP007','DEPT004','Accounts'),('COMP008','DEPT003','Security'),('COMP009','DEPT003','Security'),('COMP010','DEPT001','IT'),('COMP011','DEPT001','IT'),('COMP012','DEPT001','IT');
/*!40000 ALTER TABLE `dbo.Dept_Wise_Top_3_Salaries_DeptDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Dept_Wise_Top_3_Salaries_EmpDetails`
--

DROP TABLE IF EXISTS `dbo.Dept_Wise_Top_3_Salaries_EmpDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Dept_Wise_Top_3_Salaries_EmpDetails` (
  `EmpID` varchar(7) DEFAULT NULL,
  `EmpName` varchar(9) DEFAULT NULL,
  `EmpSalary` decimal(6,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Dept_Wise_Top_3_Salaries_EmpDetails`
--

LOCK TABLES `dbo.Dept_Wise_Top_3_Salaries_EmpDetails` WRITE;
/*!40000 ALTER TABLE `dbo.Dept_Wise_Top_3_Salaries_EmpDetails` DISABLE KEYS */;
INSERT INTO `dbo.Dept_Wise_Top_3_Salaries_EmpDetails` VALUES ('COMP001','Sarjit',45000.0),('COMP002','Ronak',49000.0),('COMP003','Aquib',45001.0),('COMP004','Shreyansh',57000.0),('COMP005','Mayank',51000.0),('COMP006','Ankit',61000.0),('COMP007','Ajay',63000.0),('COMP008','Pankaj',47000.0),('COMP009','Haider',48000.0),('COMP010','Sami',49500.0),('COMP011','Aslam',48500.0),('COMP012','Ravi',49000.0);
/*!40000 ALTER TABLE `dbo.Dept_Wise_Top_3_Salaries_EmpDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Distinct_Without_Distinct`
--

DROP TABLE IF EXISTS `dbo.Distinct_Without_Distinct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Distinct_Without_Distinct` (
  `ID` decimal(2,1) DEFAULT NULL,
  `Name` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Distinct_Without_Distinct`
--

LOCK TABLES `dbo.Distinct_Without_Distinct` WRITE;
/*!40000 ALTER TABLE `dbo.Distinct_Without_Distinct` DISABLE KEYS */;
INSERT INTO `dbo.Distinct_Without_Distinct` VALUES (1.0,'Sarjit'),(2.0,'Aquib'),(3.0,'Shreyansh'),(4.0,'Mayank'),(5.0,'Kumar'),(2.0,'Aquib'),(4.0,'Mayank'),(3.0,'Shreyansh');
/*!40000 ALTER TABLE `dbo.Distinct_Without_Distinct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.EmpDeptWiseSalary`
--

DROP TABLE IF EXISTS `dbo.EmpDeptWiseSalary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.EmpDeptWiseSalary` (
  `EmpID` varchar(7) DEFAULT NULL,
  `EmpName` varchar(9) DEFAULT NULL,
  `DeptID` varchar(7) DEFAULT NULL,
  `EmpSalary` decimal(6,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.EmpDeptWiseSalary`
--

LOCK TABLES `dbo.EmpDeptWiseSalary` WRITE;
/*!40000 ALTER TABLE `dbo.EmpDeptWiseSalary` DISABLE KEYS */;
INSERT INTO `dbo.EmpDeptWiseSalary` VALUES ('COMP001','Sarjit','DEPT003',45000.0),('COMP002','Ronak','DEPT001',49000.0),('COMP003','Aquib','DEPT003',45001.0),('COMP004','Shreyansh','DEPT002',57000.0),('COMP005','Mayank','DEPT001',51000.0),('COMP006','Ankit','DEPT004',61000.0),('COMP007','Ajay','DEPT004',63000.0),('COMP008','Ravi','DEPT004',57000.0);
/*!40000 ALTER TABLE `dbo.EmpDeptWiseSalary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.EmpTable`
--

DROP TABLE IF EXISTS `dbo.EmpTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.EmpTable` (
  `EmpID` varchar(12) DEFAULT NULL,
  `EmpName` varchar(9) DEFAULT NULL,
  `ProjectCode` varchar(5) DEFAULT NULL,
  `Location` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.EmpTable`
--

LOCK TABLES `dbo.EmpTable` WRITE;
/*!40000 ALTER TABLE `dbo.EmpTable` DISABLE KEYS */;
INSERT INTO `dbo.EmpTable` VALUES ('2.02301001E8','Kumar','CMP01','Jaipur'),('2.02301002E8','Sarjit','CMP01','Agra'),('2.02301003E8','Aquib','CMP02','Bangalore'),('2.02301004E8','Mayank','CMP03','Lucknow'),('2.02301005E8','Shreyansh','CMP02','Bangalore'),('2.02301006E8','Ankit','CMP03','Allahabad'),('2.02301007E8','Ajay','CMP03','Jaunpur');
/*!40000 ALTER TABLE `dbo.EmpTable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Employees_Joined_Earlier_Than_Manager`
--

DROP TABLE IF EXISTS `dbo.Employees_Joined_Earlier_Than_Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Employees_Joined_Earlier_Than_Manager` (
  `Emp_ID` varchar(11) DEFAULT NULL,
  `Emp_Name` varchar(9) DEFAULT NULL,
  `Manager_ID` varchar(11) DEFAULT NULL,
  `Date_Of_Joining` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Employees_Joined_Earlier_Than_Manager`
--

LOCK TABLES `dbo.Employees_Joined_Earlier_Than_Manager` WRITE;
/*!40000 ALTER TABLE `dbo.Employees_Joined_Earlier_Than_Manager` DISABLE KEYS */;
INSERT INTO `dbo.Employees_Joined_Earlier_Than_Manager` VALUES ('COMPYLO_001','Tom','NULL','2021-02-11 00:00:00'),('COMPYLO_002','Mayank','COMPYLO_001','2021-07-21 00:00:00'),('COMPYLO_003','Ronak','COMPYLO_001','2021-07-25 00:00:00'),('COMPYLO_004','Aquib','COMPYLO_001','2021-08-01 00:00:00'),('COMPYLO_005','Sarjit','COMPYLO_002','2021-08-13 00:00:00'),('COMPYLO_006','Ankit','COMPYLO_002','2021-09-17 00:00:00'),('COMPYLO_007','Ajay','COMPYLO_003','2021-10-19 00:00:00'),('COMPYLO_008','Shreyansh','COMPYLO_003','2021-10-31 00:00:00'),('COMPYLO_009','Ravi','COMPYLO_003','2021-07-17 00:00:00'),('COMPYLO_010','Pankaj','COMPYLO_004','2021-11-09 00:00:00'),('COMPYLO_011','Sami','COMPYLO_005','2021-11-15 00:00:00'),('COMPYLO_012','Pranjal','COMPYLO_005','2021-12-04 00:00:00'),('COMPYLO_013','SK','COMPYLO_005','2021-12-13 00:00:00'),('COMPYLO_014','Manoj','COMPYLO_005','2022-01-05 00:00:00'),('COMPYLO_015','Himan','COMPYLO_006','2022-01-25 00:00:00'),('COMPYLO_016','Amir','COMPYLO_006','2022-02-05 00:00:00'),('COMPYLO_017','Sanjay','COMPYLO_007','2022-02-05 00:00:00'),('COMPYLO_018','Sameer','COMPYLO_008','2022-03-04 00:00:00'),('COMPYLO_019','Kush','COMPYLO_009','2022-03-04 00:00:00'),('COMPYLO_020','Aaryan','COMPYLO_010','2022-03-04 00:00:00');
/*!40000 ALTER TABLE `dbo.Employees_Joined_Earlier_Than_Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Employees_Who_Earn_More_Than_Manager`
--

DROP TABLE IF EXISTS `dbo.Employees_Who_Earn_More_Than_Manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Employees_Who_Earn_More_Than_Manager` (
  `EmpID` varchar(7) DEFAULT NULL,
  `EmpName` varchar(9) DEFAULT NULL,
  `Manager_ID` varchar(7) DEFAULT NULL,
  `EmpSalary` decimal(6,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Employees_Who_Earn_More_Than_Manager`
--

LOCK TABLES `dbo.Employees_Who_Earn_More_Than_Manager` WRITE;
/*!40000 ALTER TABLE `dbo.Employees_Who_Earn_More_Than_Manager` DISABLE KEYS */;
INSERT INTO `dbo.Employees_Who_Earn_More_Than_Manager` VALUES ('COMP001','Sarjit','COMP005',51500.0),('COMP002','Ronak','COMP003',49000.0),('COMP003','Aquib','COMP010',52000.0),('COMP004','Shreyansh','COMP010',70000.0),('COMP005','Mayank','COMP010',51000.0),('COMP006','Ankit','COMP005',50000.0),('COMP007','Ajay','COMP005',49000.0),('COMP008','Pankaj','COMP001',47000.0),('COMP009','Haider','COMP010',71000.0),('COMP010','Sami','NULL',79000.0),('COMP011','Aslam','COMP003',48500.0),('COMP012','Ravi','COMP002',48500.0);
/*!40000 ALTER TABLE `dbo.Employees_Who_Earn_More_Than_Manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Food_Web`
--

DROP TABLE IF EXISTS `dbo.Food_Web`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Food_Web` (
  `Living_Being_ID` decimal(2,1) DEFAULT NULL,
  `Living_Being_Name` varchar(7) DEFAULT NULL,
  `Eats` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Food_Web`
--

LOCK TABLES `dbo.Food_Web` WRITE;
/*!40000 ALTER TABLE `dbo.Food_Web` DISABLE KEYS */;
INSERT INTO `dbo.Food_Web` VALUES (1.0,'Lion','2.0'),(2.0,'Deer','3.0'),(3.0,'Plants',''),(4.0,'Insects','3.0'),(5.0,'Rabbit','3.0'),(6.0,'Fox','5.0'),(7.0,'Mouse','4.0'),(8.0,'Snake','7.0'),(9.0,'Peacock','8.0');
/*!40000 ALTER TABLE `dbo.Food_Web` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Food_Web_Copy`
--

DROP TABLE IF EXISTS `dbo.Food_Web_Copy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Food_Web_Copy` (
  `Living_Being_ID` decimal(2,1) DEFAULT NULL,
  `Living_Being_Name` varchar(7) DEFAULT NULL,
  `Eats` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Food_Web_Copy`
--

LOCK TABLES `dbo.Food_Web_Copy` WRITE;
/*!40000 ALTER TABLE `dbo.Food_Web_Copy` DISABLE KEYS */;
INSERT INTO `dbo.Food_Web_Copy` VALUES (1.0,'Lion','2.0'),(2.0,'Deer','3.0'),(3.0,'Plants',''),(4.0,'Insects','3.0'),(5.0,'Rabbit','3.0'),(6.0,'Fox','5.0'),(7.0,'Mouse','4.0'),(8.0,'Snake','7.0'),(9.0,'Peacock','8.0');
/*!40000 ALTER TABLE `dbo.Food_Web_Copy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Food_Web_Copy_1`
--

DROP TABLE IF EXISTS `dbo.Food_Web_Copy_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Food_Web_Copy_1` (
  `Living_Being_ID` varchar(0) DEFAULT NULL,
  `Living_Being_Name` varchar(0) DEFAULT NULL,
  `Eats` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Food_Web_Copy_1`
--

LOCK TABLES `dbo.Food_Web_Copy_1` WRITE;
/*!40000 ALTER TABLE `dbo.Food_Web_Copy_1` DISABLE KEYS */;
/*!40000 ALTER TABLE `dbo.Food_Web_Copy_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Food_Web_Copy_2`
--

DROP TABLE IF EXISTS `dbo.Food_Web_Copy_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Food_Web_Copy_2` (
  `Living_Being_ID` varchar(0) DEFAULT NULL,
  `Living_Being_Name` varchar(0) DEFAULT NULL,
  `Eats` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Food_Web_Copy_2`
--

LOCK TABLES `dbo.Food_Web_Copy_2` WRITE;
/*!40000 ALTER TABLE `dbo.Food_Web_Copy_2` DISABLE KEYS */;
/*!40000 ALTER TABLE `dbo.Food_Web_Copy_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Food_Web_Copy_3`
--

DROP TABLE IF EXISTS `dbo.Food_Web_Copy_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Food_Web_Copy_3` (
  `Living_Being_ID` decimal(2,1) DEFAULT NULL,
  `Living_Being_Name` varchar(7) DEFAULT NULL,
  `Eats` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Food_Web_Copy_3`
--

LOCK TABLES `dbo.Food_Web_Copy_3` WRITE;
/*!40000 ALTER TABLE `dbo.Food_Web_Copy_3` DISABLE KEYS */;
INSERT INTO `dbo.Food_Web_Copy_3` VALUES (1.0,'Lion','2.0'),(2.0,'Deer','3.0'),(3.0,'Plants',''),(4.0,'Insects','3.0'),(5.0,'Rabbit','3.0'),(6.0,'Fox','5.0'),(7.0,'Mouse','4.0'),(8.0,'Snake','7.0'),(9.0,'Peacock','8.0');
/*!40000 ALTER TABLE `dbo.Food_Web_Copy_3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Food_Web_Copy_4`
--

DROP TABLE IF EXISTS `dbo.Food_Web_Copy_4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Food_Web_Copy_4` (
  `Living_Being_ID` varchar(0) DEFAULT NULL,
  `Living_Being_Name` varchar(0) DEFAULT NULL,
  `Eats` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Food_Web_Copy_4`
--

LOCK TABLES `dbo.Food_Web_Copy_4` WRITE;
/*!40000 ALTER TABLE `dbo.Food_Web_Copy_4` DISABLE KEYS */;
/*!40000 ALTER TABLE `dbo.Food_Web_Copy_4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Holiday_Table`
--

DROP TABLE IF EXISTS `dbo.Holiday_Table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Holiday_Table` (
  `Calendar_Date` varchar(19) DEFAULT NULL,
  `Time` varchar(12) DEFAULT NULL,
  `Day` varchar(9) DEFAULT NULL,
  `Holiday` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Holiday_Table`
--

LOCK TABLES `dbo.Holiday_Table` WRITE;
/*!40000 ALTER TABLE `dbo.Holiday_Table` DISABLE KEYS */;
INSERT INTO `dbo.Holiday_Table` VALUES ('2023-01-01 00:00:00','00:00:00.000','Sunday','New Year\'s Day'),('2023-01-26 00:00:00','00:00:00.000','Thursday','Republic Day'),('2023-02-18 00:00:00','00:00:00.000','Saturday','Maha Shivaratri'),('2023-03-08 00:00:00','00:00:00.000','Wednesday','Holi'),('2023-03-30 00:00:00','00:00:00.000','Thursday','Ram Navami'),('2023-04-07 00:00:00','00:00:00.000','Friday','Good Friday'),('2023-04-14 00:00:00','00:00:00.000','Friday','Dr Ambedkar Jayanti'),('2023-04-22 00:00:00','00:00:00.000','Saturday','Idul Fitr'),('2023-06-29 00:00:00','00:00:00.000','Thursday','Bakrid / Eid al Adha'),('2023-07-29 00:00:00','00:00:00.000','Saturday','Muharram'),('2023-08-15 00:00:00','00:00:00.000','Tuesday','Independence Day'),('2023-08-31 00:00:00','00:00:00.000','Thursday','Raksha Bandhan'),('2023-09-07 00:00:00','00:00:00.000','Thursday','Janmashtami'),('2023-09-28 00:00:00','00:00:00.000','Thursday','Eid e Milad'),('2023-10-02 00:00:00','00:00:00.000','Monday','Gandhi Jayanti'),('2023-10-23 00:00:00','00:00:00.000','Tuesday','Vijaya Dashami'),('2023-11-12 00:00:00','00:00:00.000','Sunday','Diwali'),('2023-11-27 00:00:00','00:00:00.000','Monday','Guru Nanak Jayanti'),('2023-12-25 00:00:00','00:00:00.000','Monday','Christmas Day');
/*!40000 ALTER TABLE `dbo.Holiday_Table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Insert_Data_From_Excel`
--

DROP TABLE IF EXISTS `dbo.Insert_Data_From_Excel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Insert_Data_From_Excel` (
  `Name` varchar(14) DEFAULT NULL,
  `Monthly Income` decimal(7,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Insert_Data_From_Excel`
--

LOCK TABLES `dbo.Insert_Data_From_Excel` WRITE;
/*!40000 ALTER TABLE `dbo.Insert_Data_From_Excel` DISABLE KEYS */;
INSERT INTO `dbo.Insert_Data_From_Excel` VALUES ('Ronak Ron',145000.0),('Aslam',141000.0),('Raja Mishra',175000.0),('Ankit Sikarwar',137000.0),('Ritesh Yadav',141000.0);
/*!40000 ALTER TABLE `dbo.Insert_Data_From_Excel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Interview_Calendar`
--

DROP TABLE IF EXISTS `dbo.Interview_Calendar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Interview_Calendar` (
  `Cal_Date` varchar(19) DEFAULT NULL,
  `Working_Day` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Interview_Calendar`
--

LOCK TABLES `dbo.Interview_Calendar` WRITE;
/*!40000 ALTER TABLE `dbo.Interview_Calendar` DISABLE KEYS */;
INSERT INTO `dbo.Interview_Calendar` VALUES ('2010-01-01 00:00:00','Y'),('2010-01-02 00:00:00','N'),('2010-01-03 00:00:00','N'),('2010-01-04 00:00:00','Y'),('2010-01-05 00:00:00','Y'),('2010-01-06 00:00:00','Y'),('2010-01-07 00:00:00','Y'),('2010-01-08 00:00:00','Y'),('2010-01-09 00:00:00','N'),('2010-01-10 00:00:00','N'),('2010-01-11 00:00:00','Y'),('2010-01-12 00:00:00','Y'),('2010-01-13 00:00:00','Y'),('2010-01-14 00:00:00','Y'),('2010-01-15 00:00:00','Y'),('2010-01-16 00:00:00','N'),('2010-01-17 00:00:00','N'),('2010-01-18 00:00:00','Y'),('2010-01-19 00:00:00','Y'),('2010-01-20 00:00:00','Y'),('2010-01-21 00:00:00','Y'),('2010-01-22 00:00:00','Y'),('2010-01-23 00:00:00','N'),('2010-01-24 00:00:00','N'),('2010-01-25 00:00:00','Y'),('2010-01-26 00:00:00','Y'),('2010-01-27 00:00:00','Y'),('2010-01-28 00:00:00','Y'),('2010-01-29 00:00:00','Y'),('2010-01-30 00:00:00','N'),('2010-01-31 00:00:00','N'),('2010-02-01 00:00:00','Y'),('2010-02-02 00:00:00','Y'),('2010-02-03 00:00:00','Y'),('2010-02-04 00:00:00','Y'),('2010-02-05 00:00:00','Y'),('2010-02-06 00:00:00','N'),('2010-02-07 00:00:00','N'),('2010-02-08 00:00:00','Y'),('2010-02-09 00:00:00','Y'),('2010-02-10 00:00:00','Y'),('2010-02-11 00:00:00','Y'),('2010-02-12 00:00:00','Y'),('2010-02-13 00:00:00','N'),('2010-02-14 00:00:00','N'),('2010-02-15 00:00:00','Y'),('2010-02-16 00:00:00','Y'),('2010-02-17 00:00:00','Y'),('2010-02-18 00:00:00','Y'),('2010-02-19 00:00:00','Y'),('2010-02-20 00:00:00','N'),('2010-02-21 00:00:00','N'),('2010-02-22 00:00:00','Y'),('2010-02-23 00:00:00','Y'),('2010-02-24 00:00:00','Y'),('2010-02-25 00:00:00','Y'),('2010-02-26 00:00:00','Y'),('2010-02-27 00:00:00','N'),('2010-02-28 00:00:00','N'),('2010-03-01 00:00:00','Y'),('2010-03-02 00:00:00','Y'),('2010-03-03 00:00:00','Y'),('2010-03-04 00:00:00','Y'),('2010-03-05 00:00:00','Y'),('2010-03-06 00:00:00','N'),('2010-03-07 00:00:00','N'),('2010-03-08 00:00:00','Y'),('2010-03-09 00:00:00','Y'),('2010-03-10 00:00:00','Y'),('2010-03-11 00:00:00','Y'),('2010-03-12 00:00:00','Y'),('2010-03-13 00:00:00','N'),('2010-03-14 00:00:00','N'),('2010-03-15 00:00:00','Y'),('2010-03-16 00:00:00','Y'),('2010-03-17 00:00:00','Y'),('2010-03-18 00:00:00','Y'),('2010-03-19 00:00:00','Y'),('2010-03-20 00:00:00','N'),('2010-03-21 00:00:00','N'),('2010-03-22 00:00:00','Y'),('2010-03-23 00:00:00','Y'),('2010-03-24 00:00:00','Y'),('2010-03-25 00:00:00','Y'),('2010-03-26 00:00:00','Y'),('2010-03-27 00:00:00','N'),('2010-03-28 00:00:00','N'),('2010-03-29 00:00:00','Y'),('2010-03-30 00:00:00','Y'),('2010-03-31 00:00:00','Y'),('2010-04-01 00:00:00','Y'),('2010-04-02 00:00:00','Y'),('2010-04-03 00:00:00','N'),('2010-04-04 00:00:00','N'),('2010-04-05 00:00:00','Y'),('2010-04-06 00:00:00','Y'),('2010-04-07 00:00:00','Y'),('2010-04-08 00:00:00','Y'),('2010-04-09 00:00:00','Y'),('2010-04-10 00:00:00','N');
/*!40000 ALTER TABLE `dbo.Interview_Calendar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.MT_students`
--

DROP TABLE IF EXISTS `dbo.MT_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.MT_students` (
  `stu_id` int(11) DEFAULT NULL,
  `stu_name` varchar(8) DEFAULT NULL,
  `branch` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.MT_students`
--

LOCK TABLES `dbo.MT_students` WRITE;
/*!40000 ALTER TABLE `dbo.MT_students` DISABLE KEYS */;
INSERT INTO `dbo.MT_students` VALUES (1901401,'DEVA','C.S'),(1901402,'HARSH','C.S'),(1901403,'ABHISHEK','C.S'),(1901404,'GARVIT','C.S'),(1901405,'SAMPATH','C.S'),(1901406,'PRADEEP','C.S'),(1901407,'DEVESH','C.S');
/*!40000 ALTER TABLE `dbo.MT_students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.MagicTables`
--

DROP TABLE IF EXISTS `dbo.MagicTables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.MagicTables` (
  `Floor Number` decimal(3,1) DEFAULT NULL,
  `Company Name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.MagicTables`
--

LOCK TABLES `dbo.MagicTables` WRITE;
/*!40000 ALTER TABLE `dbo.MagicTables` DISABLE KEYS */;
INSERT INTO `dbo.MagicTables` VALUES (15.0,'Kipragno Technologies Pvt Ltd'),(21.0,'Compylo Ed-Tech Pvt Ltd'),(7.0,'ChatGuy LLC'),(12.0,'infotainment brothers LLP'),(9.0,'Ladakh Travel Company'),(11.0,'Port Blair Music Group Pvt Ltd');
/*!40000 ALTER TABLE `dbo.MagicTables` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Marks_As_CSV`
--

DROP TABLE IF EXISTS `dbo.Marks_As_CSV`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Marks_As_CSV` (
  `Student_ID` decimal(2,1) DEFAULT NULL,
  `Student_Name` varchar(11) DEFAULT NULL,
  `Marks` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Marks_As_CSV`
--

LOCK TABLES `dbo.Marks_As_CSV` WRITE;
/*!40000 ALTER TABLE `dbo.Marks_As_CSV` DISABLE KEYS */;
INSERT INTO `dbo.Marks_As_CSV` VALUES (1.0,'Ronak Ron','33, 35, 36'),(2.0,'Aquib Aslam','45, 44, 47'),(3.0,'Mayank Soni','49, 48, 49');
/*!40000 ALTER TABLE `dbo.Marks_As_CSV` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Max_Value_From_Table_1`
--

DROP TABLE IF EXISTS `dbo.Max_Value_From_Table_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Max_Value_From_Table_1` (
  `Student_ID` varchar(12) DEFAULT NULL,
  `Student_Name` varchar(9) DEFAULT NULL,
  `PC_Semester_1` decimal(3,1) DEFAULT NULL,
  `PC_Semester_2` decimal(3,1) DEFAULT NULL,
  `PC_Semester_3` decimal(3,1) DEFAULT NULL,
  `PC_Semester_4` decimal(3,1) DEFAULT NULL,
  `PC_Semester_5` decimal(3,1) DEFAULT NULL,
  `PC_Semester_6` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Max_Value_From_Table_1`
--

LOCK TABLES `dbo.Max_Value_From_Table_1` WRITE;
/*!40000 ALTER TABLE `dbo.Max_Value_From_Table_1` DISABLE KEYS */;
INSERT INTO `dbo.Max_Value_From_Table_1` VALUES ('COMPYLO_0001','Raja',67.1,64.3,65.4,66.8,79.2,81.4),('COMPYLO_0002','Ronak',71.6,73.3,72.1,59.0,57.0,61.0),('COMPYLO_0003','Aslam',67.0,63.2,65.1,67.6,71.4,75.2),('COMPYLO_0004','Shreyansh',75.3,77.2,75.1,78.9,81.5,82.0),('COMPYLO_0005','Mayank',79.2,81.3,77.3,78.7,83.6,87.3),('COMPYLO_0006','Himanta',74.9,75.3,75.9,74.3,76.7,81.0),('COMPYLO_0007','Ravi',66.0,65.1,63.4,61.9,62.3,67.0),('COMPYLO_0008','Ankit',67.7,69.4,68.2,71.3,70.4,75.8),('COMPYLO_0009','Ajay',75.2,76.9,75.8,81.6,81.3,85.2),('COMPYLO_0010','Pankaj',65.1,62.3,63.4,64.8,77.2,77.1);
/*!40000 ALTER TABLE `dbo.Max_Value_From_Table_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Max_Value_From_Table_2`
--

DROP TABLE IF EXISTS `dbo.Max_Value_From_Table_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Max_Value_From_Table_2` (
  `Item_ID` varchar(12) DEFAULT NULL,
  `Consumer_Name` varchar(9) DEFAULT NULL,
  `Date_Of_Delivery_iPhone` varchar(19) DEFAULT NULL,
  `Date_Of_Delivery_Laptop` varchar(19) DEFAULT NULL,
  `Date_Of_Delivery_SmartWatch` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Max_Value_From_Table_2`
--

LOCK TABLES `dbo.Max_Value_From_Table_2` WRITE;
/*!40000 ALTER TABLE `dbo.Max_Value_From_Table_2` DISABLE KEYS */;
INSERT INTO `dbo.Max_Value_From_Table_2` VALUES ('COMPYLO_0001','Raja','2022-10-19 00:00:00','2022-09-07 00:00:00','2022-12-29 00:00:00'),('COMPYLO_0002','Ronak','2023-01-30 00:00:00','2022-12-26 00:00:00','2022-11-30 00:00:00'),('COMPYLO_0003','Aslam','2022-04-20 00:00:00','2022-10-08 00:00:00','2022-12-26 00:00:00'),('COMPYLO_0004','Shreyansh','2022-08-14 00:00:00','2022-09-17 00:00:00','2022-12-19 00:00:00'),('COMPYLO_0005','Mayank','2022-12-30 00:00:00','2023-01-18 00:00:00','2022-12-13 00:00:00'),('COMPYLO_0006','Himanta','2022-12-02 00:00:00','2022-11-28 00:00:00','2023-01-29 00:00:00'),('COMPYLO_0007','Ravi','2022-12-26 00:00:00','2023-01-30 00:00:00','2022-04-20 00:00:00'),('COMPYLO_0008','Ankit','2022-08-06 00:00:00','2022-12-30 00:00:00','2023-01-18 00:00:00'),('COMPYLO_0009','Ajay','2022-05-15 00:00:00','2022-12-11 00:00:00','2022-06-12 00:00:00'),('COMPYLO_0010','Pankaj','2022-07-07 00:00:00','2022-10-19 00:00:00','2022-10-08 00:00:00');
/*!40000 ALTER TABLE `dbo.Max_Value_From_Table_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Milk_Products_Name`
--

DROP TABLE IF EXISTS `dbo.Milk_Products_Name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Milk_Products_Name` (
  `Product_ID` varchar(11) DEFAULT NULL,
  `Product_Name` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Milk_Products_Name`
--

LOCK TABLES `dbo.Milk_Products_Name` WRITE;
/*!40000 ALTER TABLE `dbo.Milk_Products_Name` DISABLE KEYS */;
INSERT INTO `dbo.Milk_Products_Name` VALUES ('COMPYLO_787','Milk'),('COMPYLO_803','Paneer'),('COMPYLO_433','Ghee'),('COMPYLO_584','Butter'),('COMPYLO_901','Buttermilk');
/*!40000 ALTER TABLE `dbo.Milk_Products_Name` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Milk_Products_SL`
--

DROP TABLE IF EXISTS `dbo.Milk_Products_SL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Milk_Products_SL` (
  `Product_ID` varchar(11) DEFAULT NULL,
  `Shelf_Life (in days)` decimal(4,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Milk_Products_SL`
--

LOCK TABLES `dbo.Milk_Products_SL` WRITE;
/*!40000 ALTER TABLE `dbo.Milk_Products_SL` DISABLE KEYS */;
INSERT INTO `dbo.Milk_Products_SL` VALUES ('COMPYLO_787',3.0),('COMPYLO_803',4.0),('COMPYLO_433',180.0),('COMPYLO_584',7.0),('COMPYLO_901',2.0);
/*!40000 ALTER TABLE `dbo.Milk_Products_SL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Most_Recent_Address`
--

DROP TABLE IF EXISTS `dbo.Most_Recent_Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Most_Recent_Address` (
  `Employee_ID` varchar(12) DEFAULT NULL,
  `Employee_Name` varchar(9) DEFAULT NULL,
  `Date_Of_Joining` varchar(19) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Date_of_Update` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Most_Recent_Address`
--

LOCK TABLES `dbo.Most_Recent_Address` WRITE;
/*!40000 ALTER TABLE `dbo.Most_Recent_Address` DISABLE KEYS */;
INSERT INTO `dbo.Most_Recent_Address` VALUES ('Compylo_0019','Sarjit','2020-01-05 00:00:00','4, Om Nagar, Lucknow, UP','2021-05-15 00:00:00'),('Compylo_0133','Shreyansh','2021-02-17 00:00:00','35/A, Virat Apartments, Varanasi, UP','2022-02-11 00:00:00'),('Compylo_0012','Sami','2019-11-19 00:00:00','512, Vigyan Colony, Hyderabad, Telangana','2022-10-17 00:00:00'),('Compylo_0101','Haider','2021-01-24 00:00:00','17, 6th Lane, Ramnathpuram, Tamil Nadu','2022-12-19 00:00:00'),('Compylo_0008','Aslam','2019-03-20 00:00:00','81, Punjabi Colony, Kolkata, West Bengal','2022-06-16 00:00:00'),('Compylo_0019','Sarjit','2020-01-05 00:00:00','332, City Heights, Sydney, Australia','2023-01-23 00:00:00'),('Compylo_0043','Ankit','2020-10-15 00:00:00','Village Rawatpur, Banda, UP','2021-04-30 00:00:00'),('Compylo_0009','Ajay','2019-09-17 00:00:00','19, Mill Colony, Bhatinda, Punjab','2022-09-14 00:00:00'),('Compylo_0021','Mayank','2020-01-05 00:00:00','77, Victoria Lane, Pifo, Ecuador','2023-01-17 00:00:00'),('Compylo_0043','Ankit','2020-10-15 00:00:00','A/90, Mushran House, Agartala, Tripura','2022-11-27 00:00:00'),('Compylo_0101','Haider','2021-01-24 00:00:00','90, Awas Vikas Colony, Itanagar, Arunachal Pradesh','2021-10-06 00:00:00'),('Compylo_0006','Ronak','2019-12-26 00:00:00','3, Block B, Arya Nagar, Raipur, Chattisgarh','2021-03-03 00:00:00'),('Compylo_0005','Ravi','2020-01-30 00:00:00','2612, Mini Emirates Towers, Dubai, UAE','2023-02-03 00:00:00'),('Compylo_0008','Aslam','2019-03-20 00:00:00','Z-92, Spirit Tower, Paris, France','2023-02-07 00:00:00'),('Compylo_0006','Ronak','2019-12-26 00:00:00','C-93, Totenham House, Dublin 24, Ireland','2023-01-30 00:00:00'),('Compylo_0021','Mayank','2020-01-05 00:00:00','433, Sadar Bazar, Amrawati, Maharashtra','2021-02-12 00:00:00'),('Compylo_0019','Sarjit','2020-01-05 00:00:00','A-19, Tower Corporate, Abu Dhabi, UAE','2020-07-21 00:00:00');
/*!40000 ALTER TABLE `dbo.Most_Recent_Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Multiple_To_1_Line_String_Agg`
--

DROP TABLE IF EXISTS `dbo.Multiple_To_1_Line_String_Agg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Multiple_To_1_Line_String_Agg` (
  `Student_ID` decimal(2,1) DEFAULT NULL,
  `Student_Name` varchar(10) DEFAULT NULL,
  `Subject` varchar(7) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Multiple_To_1_Line_String_Agg`
--

LOCK TABLES `dbo.Multiple_To_1_Line_String_Agg` WRITE;
/*!40000 ALTER TABLE `dbo.Multiple_To_1_Line_String_Agg` DISABLE KEYS */;
INSERT INTO `dbo.Multiple_To_1_Line_String_Agg` VALUES (3.0,'Raja Yadav','Maths'),(3.0,'Raja Yadav','Science'),(3.0,'Raja Yadav','Biology'),(4.0,'Ronak Ron','Maths'),(4.0,'Ronak Ron','Science'),(4.0,'Ronak Ron','Biology'),(2.0,'Aslam ','Maths'),(2.0,'Aslam ','Science'),(2.0,'Aslam ','Biology'),(1.0,'Mayank','Maths'),(1.0,'Mayank','Science'),(1.0,'Mayank','Biology'),(5.0,'Ankit','Maths'),(5.0,'Ankit','Science'),(5.0,'Ankit','Biology');
/*!40000 ALTER TABLE `dbo.Multiple_To_1_Line_String_Agg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Pivot_Data`
--

DROP TABLE IF EXISTS `dbo.Pivot_Data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Pivot_Data` (
  `Name` varchar(9) DEFAULT NULL,
  `Car` decimal(8,1) DEFAULT NULL,
  `Bike` decimal(7,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Pivot_Data`
--

LOCK TABLES `dbo.Pivot_Data` WRITE;
/*!40000 ALTER TABLE `dbo.Pivot_Data` DISABLE KEYS */;
INSERT INTO `dbo.Pivot_Data` VALUES ('Sarjit',1500000.0,200000.0),('Ronak',1100000.0,350000.0),('Shreyansh',1700000.0,100000.0),('Aquib',1400000.0,250000.0),('Mayank',2100000.0,85000.0);
/*!40000 ALTER TABLE `dbo.Pivot_Data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.ProjectManagerTable`
--

DROP TABLE IF EXISTS `dbo.ProjectManagerTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.ProjectManagerTable` (
  `ProjectCode` varchar(5) DEFAULT NULL,
  `ManagerID` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.ProjectManagerTable`
--

LOCK TABLES `dbo.ProjectManagerTable` WRITE;
/*!40000 ALTER TABLE `dbo.ProjectManagerTable` DISABLE KEYS */;
INSERT INTO `dbo.ProjectManagerTable` VALUES ('CMP01','2.02301001E8'),('CMP02','2.02301005E8'),('CMP03','2.02301004E8');
/*!40000 ALTER TABLE `dbo.ProjectManagerTable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Recursive_CTE_Store_hierarchy`
--

DROP TABLE IF EXISTS `dbo.Recursive_CTE_Store_hierarchy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Recursive_CTE_Store_hierarchy` (
  `Id` decimal(3,1) DEFAULT NULL,
  `Name` varchar(16) DEFAULT NULL,
  `ParentId` varchar(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Recursive_CTE_Store_hierarchy`
--

LOCK TABLES `dbo.Recursive_CTE_Store_hierarchy` WRITE;
/*!40000 ALTER TABLE `dbo.Recursive_CTE_Store_hierarchy` DISABLE KEYS */;
INSERT INTO `dbo.Recursive_CTE_Store_hierarchy` VALUES (1.0,'Asia',''),(2.0,'Australia',''),(3.0,'South America',''),(4.0,'India','1.0'),(5.0,'Srilanka','1.0'),(6.0,'Bangladesh','1.0'),(7.0,'Nepal','1.0'),(8.0,'Oman','1.0'),(9.0,'Indonesia','1.0'),(10.0,'New Zealand','2.0'),(11.0,'Peru','3.0'),(12.0,'Chile','3.0'),(13.0,'Uruguay','3.0'),(14.0,'Brazil','3.0'),(15.0,'Manipur','4.0'),(16.0,'Mizoram','4.0'),(17.0,'Ladakh','4.0'),(18.0,'Assam','4.0'),(19.0,'Kerala','4.0'),(20.0,'Orissa','4.0'),(21.0,'Sikkim','4.0'),(22.0,'Imphal','15.0'),(23.0,'Aizwal','16.0'),(24.0,'Thrissur','19.0'),(25.0,'Guwahati','18.0'),(26.0,'Brahmapur','20.0'),(27.0,'Gangtok','21.0'),(28.0,'Laksadweep','4.0'),(29.0,'Wellington','10.0'),(30.0,'Otatara','10.0'),(31.0,'Hambantota','5.0'),(32.0,'Anuradhapura','5.0'),(33.0,'Chattogram','6.0'),(34.0,'Rajshahi','6.0'),(35.0,'Dhankuta','7.0'),(36.0,'Chandannath','7.0'),(37.0,'Seeb','8.0'),(38.0,'Medan','9.0'),(39.0,'Surabaya','9.0'),(40.0,'Montevideo','13.0'),(41.0,'Temuco','12.0'),(42.0,'Tarapoto','11.0'),(43.0,'Fortaleza','14.0'),(44.0,'Millenium Centre','23.0'),(45.0,'Ima Market','15.0'),(46.0,'Leh','17.0'),(47.0,'Kavaratti','28.0');
/*!40000 ALTER TABLE `dbo.Recursive_CTE_Store_hierarchy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.SalesInfo`
--

DROP TABLE IF EXISTS `dbo.SalesInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.SalesInfo` (
  `SalesOrderID` decimal(6,1) DEFAULT NULL,
  `SalesOrderDetailID` decimal(7,1) DEFAULT NULL,
  `OrderQty` decimal(3,1) DEFAULT NULL,
  `ProductID` decimal(4,1) DEFAULT NULL,
  `UnitPrice` decimal(8,4) DEFAULT NULL,
  `UnitPriceDiscount` decimal(3,2) DEFAULT NULL,
  `TotalAmount` decimal(11,6) DEFAULT NULL,
  `CreatedDate` varchar(19) DEFAULT NULL,
  `InsertDate` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.SalesInfo`
--

LOCK TABLES `dbo.SalesInfo` WRITE;
/*!40000 ALTER TABLE `dbo.SalesInfo` DISABLE KEYS */;
INSERT INTO `dbo.SalesInfo` VALUES (71774.0,110562.0,1.0,836.0,356.8980,0.00,356.898000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71774.0,110563.0,1.0,822.0,356.8980,0.00,356.898000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71776.0,110567.0,1.0,907.0,63.9000,0.00,63.900000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110619.0,4.0,905.0,218.4540,0.00,873.816000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110617.0,2.0,983.0,461.6940,0.00,923.388000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110618.0,6.0,988.0,112.9980,0.40,406.792800,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110619.0,2.0,748.0,818.7000,0.00,1637.400000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110620.0,1.0,990.0,323.9940,0.00,323.994000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110621.0,1.0,926.0,149.8740,0.00,149.874000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110622.0,1.0,743.0,809.7600,0.00,809.760000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110623.0,4.0,782.0,1376.9940,0.00,5507.976000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110624.0,2.0,918.0,158.4300,0.00,316.860000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110625.0,5.0,780.0,1391.9940,0.00,5567.976000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110628.0,1.0,937.0,48.5940,0.00,48.594000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110627.0,6.0,867.0,41.9940,0.00,251.964000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110628.0,1.0,985.0,112.9980,0.40,67.798800,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110629.0,2.0,989.0,323.9940,0.00,647.988000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110630.0,3.0,991.0,323.9940,0.00,971.982000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110631.0,1.0,992.0,323.9940,0.00,323.994000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110632.0,2.0,993.0,323.9940,0.00,647.988000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110633.0,2.0,984.0,112.9980,0.40,135.597600,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110634.0,3.0,986.0,112.9980,0.40,203.396400,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110635.0,3.0,987.0,112.9980,0.40,203.396400,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110636.0,2.0,981.0,461.6940,0.00,923.388000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110637.0,3.0,982.0,461.6940,0.00,1385.082000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110638.0,5.0,783.0,1376.9940,0.00,6884.970000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110639.0,3.0,809.0,37.1520,0.00,111.456000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110640.0,1.0,810.0,72.1620,0.00,72.162000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110641.0,2.0,935.0,24.2940,0.00,48.588000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110642.0,1.0,925.0,149.8740,0.00,149.874000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110643.0,7.0,869.0,41.9940,0.00,293.958000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71780.0,110644.0,1.0,880.0,32.9940,0.00,32.994000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110667.0,3.0,714.0,29.9940,0.00,89.982000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110668.0,3.0,956.0,1430.4420,0.00,4291.326000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110669.0,1.0,954.0,1430.4420,0.00,1430.442000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110670.0,10.0,712.0,5.3940,0.00,53.940000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110670.0,10.0,877.0,4.7700,0.00,47.700000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110672.0,4.0,996.0,72.8940,0.00,291.576000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110673.0,6.0,864.0,38.1000,0.00,228.600000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110674.0,3.0,876.0,72.0000,0.00,216.000000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110675.0,4.0,959.0,445.4100,0.00,1781.640000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110676.0,4.0,971.0,728.9100,0.00,2915.640000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110677.0,6.0,870.0,2.9940,0.00,17.964000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110678.0,1.0,978.0,445.4100,0.00,445.410000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110679.0,1.0,955.0,1430.4420,0.00,1430.442000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110680.0,1.0,948.0,63.9000,0.00,63.900000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110681.0,1.0,994.0,32.3940,0.00,32.394000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110682.0,1.0,970.0,728.9100,0.00,728.910000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110683.0,2.0,966.0,1430.4420,0.00,2860.884000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110684.0,4.0,884.0,32.3940,0.00,129.576000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110685.0,2.0,885.0,602.3460,0.00,1204.692000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110686.0,8.0,715.0,29.9940,0.00,239.952000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110687.0,3.0,894.0,72.8760,0.00,218.628000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110688.0,1.0,957.0,1430.4420,0.00,1430.442000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110689.0,2.0,967.0,1430.4420,0.00,2860.884000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110690.0,7.0,708.0,20.9940,0.00,146.958000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110691.0,3.0,961.0,445.4100,0.00,1336.230000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110692.0,2.0,979.0,445.4100,0.00,890.820000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110693.0,2.0,958.0,445.4100,0.00,890.820000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110694.0,1.0,963.0,445.4100,0.00,445.410000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110695.0,1.0,953.0,728.9100,0.00,728.910000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110696.0,2.0,968.0,1430.4420,0.00,2860.884000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110697.0,2.0,951.0,242.9940,0.00,485.988000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110698.0,2.0,945.0,54.8940,0.00,109.788000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110699.0,1.0,916.0,31.5840,0.00,31.584000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110700.0,1.0,886.0,200.0520,0.00,200.052000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110701.0,1.0,892.0,602.3460,0.00,602.346000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110702.0,1.0,893.0,602.3460,0.00,602.346000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110703.0,6.0,881.0,32.3940,0.00,194.364000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110704.0,4.0,883.0,32.3940,0.00,129.576000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110705.0,1.0,859.0,14.6940,0.00,14.694000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110707.0,4.0,865.0,38.1000,0.00,152.400000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110707.0,9.0,880.0,32.9940,0.00,296.946000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110708.0,6.0,711.0,20.9940,0.00,125.964000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71782.0,110709.0,3.0,707.0,20.9940,0.00,62.982000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110710.0,4.0,738.0,202.3320,0.00,809.328000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110711.0,6.0,939.0,37.2540,0.00,223.524000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110712.0,3.0,793.0,1466.0100,0.00,4398.030000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110713.0,4.0,977.0,323.9940,0.00,1295.976000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110714.0,9.0,880.0,32.9940,0.00,296.946000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110715.0,7.0,859.0,14.6940,0.00,102.858000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110716.0,25.0,976.0,850.4950,0.10,19136.137500,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110717.0,6.0,714.0,29.9940,0.00,179.964000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110718.0,8.0,877.0,4.7700,0.00,38.160000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110719.0,1.0,813.0,72.1620,0.00,72.162000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110720.0,6.0,881.0,32.3940,0.00,194.364000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110721.0,6.0,873.0,1.3740,0.00,8.244000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110722.0,10.0,870.0,2.9940,0.00,29.940000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110723.0,1.0,822.0,356.8980,0.00,356.898000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110724.0,1.0,799.0,672.2940,0.00,672.294000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110725.0,2.0,858.0,14.6940,0.00,29.388000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110726.0,9.0,860.0,14.6940,0.00,132.246000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110727.0,15.0,864.0,34.9250,0.05,497.681250,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110728.0,3.0,938.0,24.2940,0.00,72.882000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110729.0,11.0,883.0,31.3142,0.02,337.567076,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110730.0,6.0,722.0,202.3320,0.00,1213.992000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110731.0,9.0,884.0,32.3940,0.00,291.546000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110732.0,7.0,998.0,323.9940,0.00,2267.958000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110733.0,5.0,999.0,323.9940,0.00,1619.970000,'2022-06-01 00:00:00','2023-03-18 00:00:00'),(71783.0,110732.0,4.0,797.0,672.2940,0.00,2689.176000,'2022-06-01 00:00:00','2023-03-18 00:00:00');
/*!40000 ALTER TABLE `dbo.SalesInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.SalesInfoHistory`
--

DROP TABLE IF EXISTS `dbo.SalesInfoHistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.SalesInfoHistory` (
  `SalesOrderID` mediumint(9) DEFAULT NULL,
  `OrderQty` smallint(6) DEFAULT NULL,
  `TotalLineTotal` decimal(9,4) DEFAULT NULL,
  `SalesDate` varchar(19) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.SalesInfoHistory`
--

LOCK TABLES `dbo.SalesInfoHistory` WRITE;
/*!40000 ALTER TABLE `dbo.SalesInfoHistory` DISABLE KEYS */;
INSERT INTO `dbo.SalesInfoHistory` VALUES (71774,2,713.7960,'2023-03-18 00:00:00'),(71776,1,63.9000,'2023-03-18 00:00:00'),(71780,77,29923.0080,'2023-03-18 00:00:00'),(71782,140,33319.9860,'2023-03-18 00:00:00'),(71783,288,65683.3680,'2023-03-18 00:00:00'),(71784,267,89869.2763,'2023-03-18 00:00:00'),(71796,60,47848.0260,'2023-03-18 00:00:00'),(71797,271,65123.4634,'2023-03-18 00:00:00'),(71815,5,926.9160,'2023-03-18 00:00:00'),(71816,13,2847.4080,'2023-03-18 00:00:00'),(71831,9,1712.9460,'2023-03-18 00:00:00'),(71832,76,28950.6781,'2023-03-18 00:00:00'),(71845,77,34118.5356,'2023-03-18 00:00:00'),(71846,6,1884.3948,'2023-03-18 00:00:00'),(71856,2,500.3040,'2023-03-18 00:00:00'),(71858,27,11528.8440,'2023-03-18 00:00:00'),(71863,20,2728.5551,'2023-03-18 00:00:00');
/*!40000 ALTER TABLE `dbo.SalesInfoHistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Simple_Join_Table_1`
--

DROP TABLE IF EXISTS `dbo.Simple_Join_Table_1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Simple_Join_Table_1` (
  `Simple_Join_Table_1` decimal(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Simple_Join_Table_1`
--

LOCK TABLES `dbo.Simple_Join_Table_1` WRITE;
/*!40000 ALTER TABLE `dbo.Simple_Join_Table_1` DISABLE KEYS */;
INSERT INTO `dbo.Simple_Join_Table_1` VALUES (1.0),(2.0),(3.0);
/*!40000 ALTER TABLE `dbo.Simple_Join_Table_1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Simple_Join_Table_2`
--

DROP TABLE IF EXISTS `dbo.Simple_Join_Table_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Simple_Join_Table_2` (
  `Simple_Join_Table_2` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Simple_Join_Table_2`
--

LOCK TABLES `dbo.Simple_Join_Table_2` WRITE;
/*!40000 ALTER TABLE `dbo.Simple_Join_Table_2` DISABLE KEYS */;
INSERT INTO `dbo.Simple_Join_Table_2` VALUES ('1.0'),('2.0'),('3.0'),('4.0'),('5.0'),('');
/*!40000 ALTER TABLE `dbo.Simple_Join_Table_2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Simple_Join_Table_3`
--

DROP TABLE IF EXISTS `dbo.Simple_Join_Table_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Simple_Join_Table_3` (
  `Simple_Join_Table_3` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Simple_Join_Table_3`
--

LOCK TABLES `dbo.Simple_Join_Table_3` WRITE;
/*!40000 ALTER TABLE `dbo.Simple_Join_Table_3` DISABLE KEYS */;
INSERT INTO `dbo.Simple_Join_Table_3` VALUES ('1.0'),('2.0'),('3.0'),('');
/*!40000 ALTER TABLE `dbo.Simple_Join_Table_3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Top_Bottom_20_pc`
--

DROP TABLE IF EXISTS `dbo.Top_Bottom_20_pc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Top_Bottom_20_pc` (
  `Records` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Top_Bottom_20_pc`
--

LOCK TABLES `dbo.Top_Bottom_20_pc` WRITE;
/*!40000 ALTER TABLE `dbo.Top_Bottom_20_pc` DISABLE KEYS */;
INSERT INTO `dbo.Top_Bottom_20_pc` VALUES (97.0),(93.0),(86.0),(83.0),(67.0),(55.0),(51.0),(49.0),(41.0),(39.0);
/*!40000 ALTER TABLE `dbo.Top_Bottom_20_pc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.Unpivot_Data`
--

DROP TABLE IF EXISTS `dbo.Unpivot_Data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.Unpivot_Data` (
  `Name` varchar(9) DEFAULT NULL,
  `Vehicle` varchar(4) DEFAULT NULL,
  `Cost` decimal(8,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.Unpivot_Data`
--

LOCK TABLES `dbo.Unpivot_Data` WRITE;
/*!40000 ALTER TABLE `dbo.Unpivot_Data` DISABLE KEYS */;
INSERT INTO `dbo.Unpivot_Data` VALUES ('Sarjit','Car',1500000.0),('Sarjit','Bike',200000.0),('Shreyansh','Car',1700000.0),('Shreyansh','Bike',100000.0),('Ronak','Car',1100000.0),('Ronak','Bike',350000.0),('Aquib','Car',1400000.0),('Aquib','Bike',250000.0),('Mayank','Car',2100000.0),('Mayank','Bike',85000.0);
/*!40000 ALTER TABLE `dbo.Unpivot_Data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.hundred_Duplicate_all_common`
--

DROP TABLE IF EXISTS `dbo.hundred_Duplicate_all_common`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.hundred_Duplicate_all_common` (
  `hundred_duplicate_all_common` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.hundred_Duplicate_all_common`
--

LOCK TABLES `dbo.hundred_Duplicate_all_common` WRITE;
/*!40000 ALTER TABLE `dbo.hundred_Duplicate_all_common` DISABLE KEYS */;
INSERT INTO `dbo.hundred_Duplicate_all_common` VALUES (1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0),(1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0);
/*!40000 ALTER TABLE `dbo.hundred_Duplicate_all_common` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.hundred_Duplicate_few_common`
--

DROP TABLE IF EXISTS `dbo.hundred_Duplicate_few_common`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.hundred_Duplicate_few_common` (
  `hundred_Duplicate` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.hundred_Duplicate_few_common`
--

LOCK TABLES `dbo.hundred_Duplicate_few_common` WRITE;
/*!40000 ALTER TABLE `dbo.hundred_Duplicate_few_common` DISABLE KEYS */;
INSERT INTO `dbo.hundred_Duplicate_few_common` VALUES (27.0),(15.0),(32.0),(3.0),(35.0),(34.0),(31.0),(24.0),(8.0),(11.0),(17.0),(21.0),(23.0),(36.0),(30.0),(33.0),(22.0),(16.0),(35.0),(25.0),(26.0),(29.0),(33.0),(14.0),(18.0),(28.0),(34.0),(2.0),(28.0),(31.0),(23.0),(34.0),(31.0),(15.0),(14.0),(35.0),(9.0),(3.0),(36.0),(24.0),(34.0),(30.0),(25.0),(16.0),(29.0),(8.0),(12.0),(33.0),(26.0),(23.0),(13.0),(17.0),(19.0),(35.0),(36.0),(37.0),(37.0),(4.0),(18.0),(1.0),(10.0),(32.0),(36.0),(20.0),(13.0),(14.0),(24.0),(22.0),(20.0),(27.0),(33.0),(6.0),(2.0),(37.0),(20.0),(30.0),(19.0),(19.0),(11.0),(5.0),(18.0),(11.0),(15.0),(34.0),(5.0),(12.0),(36.0),(37.0),(21.0),(1.0),(14.0),(4.0),(28.0),(13.0),(33.0),(22.0),(9.0),(15.0),(31.0),(21.0);
/*!40000 ALTER TABLE `dbo.hundred_Duplicate_few_common` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.hundred_Duplicate_no_common`
--

DROP TABLE IF EXISTS `dbo.hundred_Duplicate_no_common`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.hundred_Duplicate_no_common` (
  `hundred_duplicate_no_common` decimal(4,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.hundred_Duplicate_no_common`
--

LOCK TABLES `dbo.hundred_Duplicate_no_common` WRITE;
/*!40000 ALTER TABLE `dbo.hundred_Duplicate_no_common` DISABLE KEYS */;
INSERT INTO `dbo.hundred_Duplicate_no_common` VALUES (11.0),(12.0),(13.0),(14.0),(15.0),(16.0),(17.0),(18.0),(19.0),(20.0),(21.0),(22.0),(23.0),(24.0),(25.0),(26.0),(27.0),(28.0),(29.0),(30.0),(31.0),(32.0),(33.0),(34.0),(35.0),(36.0),(37.0),(38.0),(39.0),(40.0),(41.0),(42.0),(43.0),(44.0),(45.0),(46.0),(47.0),(48.0),(49.0),(50.0),(51.0),(52.0),(53.0),(54.0),(55.0),(56.0),(57.0),(58.0),(59.0),(60.0),(61.0),(62.0),(63.0),(64.0),(65.0),(66.0),(67.0),(68.0),(69.0),(70.0),(71.0),(72.0),(73.0),(74.0),(75.0),(76.0),(77.0),(78.0),(79.0),(80.0),(81.0),(82.0),(83.0),(84.0),(85.0),(86.0),(87.0),(88.0),(89.0),(90.0),(91.0),(92.0),(93.0),(94.0),(95.0),(96.0),(97.0),(98.0),(99.0),(100.0),(101.0),(102.0),(103.0),(104.0),(105.0),(106.0),(107.0),(108.0),(109.0),(110.0);
/*!40000 ALTER TABLE `dbo.hundred_Duplicate_no_common` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.hundred_Duplicate_one_common`
--

DROP TABLE IF EXISTS `dbo.hundred_Duplicate_one_common`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.hundred_Duplicate_one_common` (
  `hundred_Duplicate_one_common` decimal(2,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.hundred_Duplicate_one_common`
--

LOCK TABLES `dbo.hundred_Duplicate_one_common` WRITE;
/*!40000 ALTER TABLE `dbo.hundred_Duplicate_one_common` DISABLE KEYS */;
INSERT INTO `dbo.hundred_Duplicate_one_common` VALUES (1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0),(1.0);
/*!40000 ALTER TABLE `dbo.hundred_Duplicate_one_common` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.ten_unique`
--

DROP TABLE IF EXISTS `dbo.ten_unique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.ten_unique` (
  `ten_Unique` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.ten_unique`
--

LOCK TABLES `dbo.ten_unique` WRITE;
/*!40000 ALTER TABLE `dbo.ten_unique` DISABLE KEYS */;
INSERT INTO `dbo.ten_unique` VALUES (1.0),(2.0),(3.0),(4.0),(5.0),(6.0),(7.0),(8.0),(9.0),(10.0);
/*!40000 ALTER TABLE `dbo.ten_unique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dbo.testing_Calendar_Table`
--

DROP TABLE IF EXISTS `dbo.testing_Calendar_Table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dbo.testing_Calendar_Table` (
  `All_Dates` varchar(19) DEFAULT NULL,
  `Is_Working_Day` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dbo.testing_Calendar_Table`
--

LOCK TABLES `dbo.testing_Calendar_Table` WRITE;
/*!40000 ALTER TABLE `dbo.testing_Calendar_Table` DISABLE KEYS */;
INSERT INTO `dbo.testing_Calendar_Table` VALUES ('2014-09-21 00:00:00','Y'),('2014-09-22 00:00:00','Y'),('2014-09-23 00:00:00','Y'),('2014-09-24 00:00:00','Y'),('2014-09-25 00:00:00','Y'),('2014-09-26 00:00:00','Y'),('2014-09-27 00:00:00','Y'),('2014-09-28 00:00:00','Y'),('2014-09-29 00:00:00','Y'),('2014-09-30 00:00:00','Y'),('2014-10-01 00:00:00','Y'),('2014-10-02 00:00:00','Y'),('2014-10-03 00:00:00','Y'),('2014-10-04 00:00:00','Y'),('2014-10-05 00:00:00','Y'),('2014-10-06 00:00:00','Y'),('2014-10-07 00:00:00','Y'),('2014-10-08 00:00:00','Y'),('2014-10-09 00:00:00','Y'),('2014-10-10 00:00:00','Y'),('2014-10-11 00:00:00','Y'),('2014-10-12 00:00:00','Y'),('2014-10-13 00:00:00','Y'),('2014-10-14 00:00:00','Y'),('2014-10-15 00:00:00','Y'),('2014-10-16 00:00:00','Y'),('2014-10-17 00:00:00','Y'),('2014-10-18 00:00:00','Y'),('2014-10-19 00:00:00','Y'),('2014-10-20 00:00:00','Y'),('2014-10-21 00:00:00','Y'),('2014-10-22 00:00:00','Y'),('2014-10-23 00:00:00','Y'),('2014-10-24 00:00:00','Y'),('2014-10-25 00:00:00','Y'),('2014-10-26 00:00:00','Y'),('2014-10-27 00:00:00','Y'),('2014-10-28 00:00:00','Y'),('2014-10-29 00:00:00','Y'),('2014-10-30 00:00:00','Y'),('2014-10-31 00:00:00','Y'),('2014-11-01 00:00:00','Y'),('2014-11-02 00:00:00','Y'),('2014-11-03 00:00:00','Y'),('2014-11-04 00:00:00','Y'),('2014-11-05 00:00:00','Y'),('2014-11-06 00:00:00','Y'),('2014-11-07 00:00:00','Y'),('2014-11-08 00:00:00','Y'),('2014-11-09 00:00:00','Y'),('2014-11-10 00:00:00','Y'),('2014-11-11 00:00:00','Y'),('2014-11-12 00:00:00','Y'),('2014-11-13 00:00:00','Y'),('2014-11-14 00:00:00','Y'),('2014-11-15 00:00:00','Y'),('2014-11-16 00:00:00','Y'),('2014-11-17 00:00:00','Y'),('2014-11-18 00:00:00','Y'),('2014-11-19 00:00:00','Y'),('2014-11-20 00:00:00','Y'),('2014-11-21 00:00:00','Y'),('2014-11-22 00:00:00','Y'),('2014-11-23 00:00:00','Y'),('2014-11-24 00:00:00','Y'),('2014-11-25 00:00:00','Y'),('2014-11-26 00:00:00','Y'),('2014-11-27 00:00:00','Y'),('2014-11-28 00:00:00','Y'),('2014-11-29 00:00:00','Y'),('2014-11-30 00:00:00','Y'),('2014-12-01 00:00:00','Y'),('2014-12-02 00:00:00','Y'),('2014-12-03 00:00:00','Y'),('2014-12-04 00:00:00','Y'),('2014-12-05 00:00:00','Y'),('2014-12-06 00:00:00','Y'),('2014-12-07 00:00:00','Y'),('2014-12-08 00:00:00','Y'),('2014-12-09 00:00:00','Y'),('2014-12-10 00:00:00','Y'),('2014-12-11 00:00:00','Y'),('2014-12-12 00:00:00','Y'),('2014-12-13 00:00:00','Y'),('2014-12-14 00:00:00','Y'),('2014-12-15 00:00:00','Y'),('2014-12-16 00:00:00','Y'),('2014-12-17 00:00:00','Y'),('2014-12-18 00:00:00','Y'),('2014-12-19 00:00:00','Y'),('2014-12-20 00:00:00','Y'),('2014-12-21 00:00:00','Y'),('2014-12-22 00:00:00','Y'),('2014-12-23 00:00:00','Y'),('2014-12-24 00:00:00','Y'),('2014-12-25 00:00:00','Y'),('2014-12-26 00:00:00','Y'),('2014-12-27 00:00:00','Y'),('2014-12-28 00:00:00','Y'),('2014-12-29 00:00:00','Y');
/*!40000 ALTER TABLE `dbo.testing_Calendar_Table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-29 11:52:30
