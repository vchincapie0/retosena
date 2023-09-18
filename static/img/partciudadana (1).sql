-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 18, 2023 at 01:31 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `partciudadana`
--

-- --------------------------------------------------------

--
-- Table structure for table `administradores`
--

CREATE TABLE `administradores` (
  `id` int(11) NOT NULL,
  `nombres` char(50) NOT NULL,
  `apellidos` char(50) NOT NULL,
  `email` char(50) NOT NULL,
  `contraseña` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `administradores`
--

INSERT INTO `administradores` (`id`, `nombres`, `apellidos`, `email`, `contraseña`) VALUES
(1, 'Juan', 'Rodriguez', 'juan@gmail.com', '123456juan');

-- --------------------------------------------------------

--
-- Table structure for table `ciudadanos`
--

CREATE TABLE `ciudadanos` (
  `id` int(11) NOT NULL,
  `tipoDocumento` enum('Cédula Ciudadanía','Tarjeta de Identidad','Cédula Extranjería') NOT NULL,
  `numeroDocumento` int(11) NOT NULL,
  `nombres` char(50) NOT NULL,
  `apellidos` char(50) NOT NULL,
  `sexo` enum('Hombre','Mujer','Intersexual','Indefinido','Prefiere no decir') DEFAULT NULL,
  `fechaNacimiento` date NOT NULL,
  `telefonoCelular` char(10) DEFAULT NULL,
  `telefonoFijo` char(10) DEFAULT NULL,
  `nivelEducativo` char(20) NOT NULL,
  `conectividad` enum('Si','No') DEFAULT NULL,
  `etnia` enum('Indígena','Afrodecendiente','Mestizo','Caucásico','Otro') NOT NULL,
  `dicapacidad` enum('Si','No') NOT NULL,
  `dispositivosTecnologicos` enum('Si','No') NOT NULL,
  `cualesDispTecn` enum('PC','Tablet','Smartphone','Otro') DEFAULT NULL,
  `regimenAfiliacion` enum('Contributivo','Subsidiado') NOT NULL,
  `municipio` char(50) NOT NULL,
  `barrioVereda` char(50) NOT NULL,
  `direccion` char(70) DEFAULT NULL,
  `estrato` tinyint(4) NOT NULL,
  `email` char(50) NOT NULL,
  `contraseña` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ciudadanos`
--

INSERT INTO `ciudadanos` (`id`, `tipoDocumento`, `numeroDocumento`, `nombres`, `apellidos`, `sexo`, `fechaNacimiento`, `telefonoCelular`, `telefonoFijo`, `nivelEducativo`, `conectividad`, `etnia`, `dicapacidad`, `dispositivosTecnologicos`, `cualesDispTecn`, `regimenAfiliacion`, `municipio`, `barrioVereda`, `direccion`, `estrato`, `email`, `contraseña`) VALUES
(2, 'Cédula Ciudadanía', 1019132790, 'vivian carolina', 'hincapie escobar', 'Mujer', '1997-08-23', '3194091311', '6014747592', 'bachiller', 'No', 'Caucásico', 'No', 'Si', 'PC', 'Subsidiado', 'cundinamarca', 'Portales', 'Calle 168a#73a', 3, 'carohinca1997@gmail.com', '123456Ch'),
(3, 'Tarjeta de Identidad', 1020816856, 'daniel', 'hernandez', 'Hombre', '1998-06-22', '3198726535', '6017867245', 'tecnico', 'Si', 'Mestizo', 'No', 'Si', 'Tablet', 'Contributivo', 'Antioquia', 'comuna 1', 'cerrito 72', 4, 'dhernandez@gmail.com', '123456dh'),
(4, 'Cédula Ciudadanía', 39127198, 'Ruben Dario', 'Hincapie Orrego', 'Hombre', '1965-10-14', '1284347372', '23244532', 'Tecnologo', 'Si', 'Otro', 'No', 'Si', 'PC', 'Contributivo', 'cundinamarca', 'Portales', 'Calle 168a#73a', 3, 'rubenhincapie@hotmail.com', '123456R'),
(5, 'Cédula Ciudadanía', 79787265, 'Martha Helena', 'Escobar', 'Mujer', '1969-02-22', '123456789', '1234567', 'bachiller', 'Si', '', 'No', 'Si', 'PC', 'Subsidiado', 'cundinamarca', 'Portales', 'Calle 168a#73a', 3, 'martha@gmail.com', '123456M');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administradores`
--
ALTER TABLE `administradores`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `ciudadanos`
--
ALTER TABLE `ciudadanos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `administradores`
--
ALTER TABLE `administradores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `ciudadanos`
--
ALTER TABLE `ciudadanos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
