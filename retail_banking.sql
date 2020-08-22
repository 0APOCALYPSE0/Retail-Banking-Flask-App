-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2020 at 11:30 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `retail_banking`
--

-- --------------------------------------------------------

--
-- Table structure for table `accbalance`
--

CREATE TABLE `accbalance` (
  `acid` int(11) NOT NULL,
  `transactions` int(11) NOT NULL,
  `balance` int(11) NOT NULL,
  `transtype` int(11) NOT NULL,
  `lastupdated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accbalance`
--

INSERT INTO `accbalance` (`acid`, `transactions`, `balance`, `transtype`, `lastupdated`) VALUES
(7, 10000, 10000, 1, '2020-06-14 13:59:56'),
(7, 10000, 0, 0, '2020-06-14 14:16:21'),
(7, 1000, 1000, 1, '2020-06-14 15:45:27'),
(7, 5000, 6000, 1, '2020-06-14 15:56:58'),
(7, 2000, 4000, 0, '2020-06-14 16:15:22'),
(7, 10000, 10000, 1, '2020-06-16 10:36:02'),
(9, 20000, 20000, 1, '2020-06-16 10:36:58'),
(9, 4000, 4000, 1, '2020-06-16 10:37:15'),
(11, 5000, 5000, 1, '2020-06-16 10:38:03'),
(9, 30000, 30000, 1, '2020-06-16 10:38:15'),
(11, 30000, 30000, 1, '2020-06-16 10:39:06'),
(7, 1, 9999, 0, '2020-06-16 14:46:19'),
(7, 1, 9998, 0, '2020-06-16 14:46:24'),
(7, 1, 9997, 0, '2020-06-16 14:46:32'),
(7, 1, 9996, 0, '2020-06-16 14:53:18'),
(7, 1, 9995, 0, '2020-06-16 14:53:23'),
(7, 1, 9994, 0, '2020-06-16 14:54:35'),
(7, 1, 9993, 0, '2020-06-16 14:54:38'),
(7, 1, 9992, 0, '2020-06-16 14:57:10'),
(7, 1, 9991, 0, '2020-06-16 14:59:08'),
(7, 1, 9990, 0, '2020-06-16 14:59:11'),
(7, 1, 9989, 0, '2020-06-16 15:00:06'),
(11, 1, 30001, 1, '2020-06-16 15:00:06'),
(7, 4000, 4000, 1, '2020-06-16 15:37:47'),
(7, 10000, 10000, 1, '2020-06-16 15:38:20'),
(7, 10000, 10000, 1, '2020-06-16 15:39:49'),
(7, 10000, 10000, 1, '2020-06-16 15:41:39');

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `accid` int(11) NOT NULL,
  `custid` int(11) NOT NULL,
  `acctype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`accid`, `custid`, `acctype`) VALUES
(7, 10, 'S'),
(8, 10, 'C'),
(9, 11, 'S'),
(10, 11, 'C'),
(11, 12, 'S'),
(13, 12, 'C');

-- --------------------------------------------------------

--
-- Table structure for table `accstatus`
--

CREATE TABLE `accstatus` (
  `acid` int(11) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'active',
  `mssg` varchar(200) NOT NULL,
  `lastupdated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accstatus`
--

INSERT INTO `accstatus` (`acid`, `status`, `mssg`, `lastupdated`) VALUES
(7, 'active', 'Account Creation Completed.', '2020-06-14 13:08:36'),
(7, 'active', 'Account Creation Completed.', '2020-06-16 10:36:02'),
(9, 'active', 'Account Creation Completed.', '2020-06-16 10:36:58'),
(9, 'active', 'Account Creation Completed.', '2020-06-16 10:37:15'),
(11, 'active', 'Account Creation Completed.', '2020-06-16 10:38:03'),
(9, 'active', 'Account Creation Completed.', '2020-06-16 10:38:15'),
(11, 'active', 'Account Creation Completed.', '2020-06-16 10:39:06'),
(7, 'active', 'Account Creation Completed.', '2020-06-16 15:37:47'),
(7, 'active', 'Account Creation Completed.', '2020-06-16 15:38:19'),
(7, 'active', 'Account Creation Completed.', '2020-06-16 15:39:48'),
(7, 'active', 'Account Creation Completed.', '2020-06-16 15:41:39');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `ssnid` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `addr` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `ssnid`, `name`, `age`, `addr`, `city`, `state`) VALUES
(10, '987654321', 'user1', '23', 'Delhi', 'Delhi', 'Delhi'),
(11, '123456789', 'user2', '22', 'Delhi', 'Delhi', 'Delhi'),
(12, 'abc123456', 'user3', '24', 'Delhi', 'Delhi', 'Delhi');

-- --------------------------------------------------------

--
-- Table structure for table `custstatus`
--

CREATE TABLE `custstatus` (
  `custid` int(11) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'active',
  `mssg` varchar(200) NOT NULL,
  `lastupdated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `custstatus`
--

INSERT INTO `custstatus` (`custid`, `status`, `mssg`, `lastupdated`) VALUES
(10, 'active', 'Customer Creation Completed.', '2020-06-14 13:07:29'),
(11, 'active', 'Customer Creation Completed.', '2020-06-16 10:36:45'),
(12, 'active', 'Customer Creation Completed.', '2020-06-16 10:37:48'),
(10, 'active', 'Customer Creation Completed.', '2020-06-16 15:30:28');

-- --------------------------------------------------------

--
-- Table structure for table `userstore`
--

CREATE TABLE `userstore` (
  `id` int(11) NOT NULL,
  `login` varchar(50) NOT NULL,
  `password` varchar(200) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userstore`
--

INSERT INTO `userstore` (`id`, `login`, `password`, `timestamp`) VALUES
(1, 'admin', 'admin123', '2020-06-13 09:01:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accbalance`
--
ALTER TABLE `accbalance`
  ADD KEY `acid` (`acid`);

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`accid`),
  ADD KEY `custid` (`custid`);

--
-- Indexes for table `accstatus`
--
ALTER TABLE `accstatus`
  ADD KEY `acid` (`acid`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `custstatus`
--
ALTER TABLE `custstatus`
  ADD KEY `custid` (`custid`);

--
-- Indexes for table `userstore`
--
ALTER TABLE `userstore`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `accid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `userstore`
--
ALTER TABLE `userstore`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accbalance`
--
ALTER TABLE `accbalance`
  ADD CONSTRAINT `accbalance_ibfk_1` FOREIGN KEY (`acid`) REFERENCES `accounts` (`accid`) ON DELETE CASCADE;

--
-- Constraints for table `accounts`
--
ALTER TABLE `accounts`
  ADD CONSTRAINT `accounts_ibfk_1` FOREIGN KEY (`custid`) REFERENCES `customers` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `accstatus`
--
ALTER TABLE `accstatus`
  ADD CONSTRAINT `accstatus_ibfk_1` FOREIGN KEY (`acid`) REFERENCES `accounts` (`accid`) ON DELETE CASCADE;

--
-- Constraints for table `custstatus`
--
ALTER TABLE `custstatus`
  ADD CONSTRAINT `custstatus_ibfk_1` FOREIGN KEY (`custid`) REFERENCES `customers` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
