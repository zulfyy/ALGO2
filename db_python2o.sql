-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 10, 2025 at 02:04 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_python2o`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `name`, `address`) VALUES
(2, 'John', 'Banjarmasin');

-- --------------------------------------------------------

--
-- Table structure for table `mhs`
--

CREATE TABLE `mhs` (
  `nama` varchar(100) NOT NULL,
  `jurusan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mhs`
--

INSERT INTO `mhs` (`nama`, `jurusan`) VALUES
('Ahmadi', 'Teknik Informatika'),
('Nor Asmah', 'Teknik Informatika'),
('Rendi', 'Teknik Informatika'),
('Muhammad Zulfy', 'Teknik Informatika'),
('Reika', 'Sistem Informasi');

-- --------------------------------------------------------

--
-- Table structure for table `mhs4`
--

CREATE TABLE `mhs4` (
  `npm` bigint(20) NOT NULL,
  `nama_lengkap` varchar(255) NOT NULL,
  `nama_panggilan` varchar(100) NOT NULL,
  `telepon` varchar(12) NOT NULL,
  `email` varchar(100) NOT NULL,
  `kelas` varchar(255) NOT NULL,
  `matkul` varchar(100) NOT NULL,
  `lok_kampus` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mhs4`
--

INSERT INTO `mhs4` (`npm`, `nama_lengkap`, `nama_panggilan`, `telepon`, `email`, `kelas`, `matkul`, `lok_kampus`) VALUES
(242311231, 'Ariel Bahta', 'Ariel', '08*********', 'ariel@ariel.temp', '2O Banjarmasin', 'Sistem Informasi', 'Banjarmasin'),
(2410010331, 'Muhammad Zulfy', 'Zulfy', '08*********', 'sebuahemail@gmail.com', '2O Banjarmasin', 'Algo Praktikum 2', 'Banjarmasin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mhs4`
--
ALTER TABLE `mhs4`
  ADD PRIMARY KEY (`npm`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
