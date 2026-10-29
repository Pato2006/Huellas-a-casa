-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-10-2026 a las 12:41:02
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `huellas_a_casa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `adopciones`
--

CREATE TABLE `adopciones` (
  `id` int(11) NOT NULL,
  `formulario_id` int(11) NOT NULL,
  `mascota_id` int(11) NOT NULL,
  `estado` enum('Aceptado','Rechazado','En proceso') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `donaciones`
--

CREATE TABLE `donaciones` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `monto` int(11) NOT NULL,
  `estado` enum('Recibido','No recibido') NOT NULL,
  `mensaje` text NOT NULL,
  `ruta_comp` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `formularios`
--

CREATE TABLE `formularios` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `grupo_familiar` varchar(32) NOT NULL,
  `alergias` varchar(32) NOT NULL,
  `otras_mascotas` varchar(32) NOT NULL,
  `cuidador_ausencia` varchar(32) NOT NULL,
  `tiempo_solo` varchar(32) NOT NULL,
  `ubicacion` enum('PH','Departamento','Casa') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascotas`
--

CREATE TABLE `mascotas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(16) NOT NULL,
  `edad` int(8) NOT NULL,
  `peso` float NOT NULL,
  `personalidad` varchar(32) NOT NULL,
  `descripcion` varchar(32) NOT NULL,
  `castrado` tinyint(1) NOT NULL,
  `tipo` enum('Perro','Gato') NOT NULL,
  `genero` enum('Macho','Hembra') NOT NULL,
  `ruta_img` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mascotas`
--

INSERT INTO `mascotas` (`id`, `nombre`, `edad`, `peso`, `personalidad`, `descripcion`, `castrado`, `tipo`, `genero`, `ruta_img`) VALUES
(1, 'Terry', 12, 19.4, 'Muy cariñoso', 'Perro salchicha', 1, 'Perro', 'Macho', 'mascota1.jpg'),
(2, 'Sergio', 9, 12.4, 'Gruñon', 'Gato blanco con manchas', 0, 'Gato', 'Hembra', 'mascota2.png'),
(3, 'Hanna', 2, 5.2, 'Muy tranquila', 'Gata marron con ojos verdes', 1, 'Gato', 'Hembra', 'mascota3.jpg'),
(4, 'Felipe', 8, 12.4, 'Se lleva bien con los niños', 'Bulldog frances', 1, 'Perro', 'Macho', 'mascota4.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(16) NOT NULL,
  `apellido` varchar(16) NOT NULL,
  `correo` varchar(64) NOT NULL,
  `contrasena` varchar(16) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `dni` int(8) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `ruta_img` varchar(64) NOT NULL,
  `tipo` enum('Admin','Usuario') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellido`, `correo`, `contrasena`, `telefono`, `dni`, `fecha_nacimiento`, `ruta_img`, `tipo`) VALUES
(1, 'German', 'Garmendia', 'germangamendi@gmail.com', 'G3rm@Ans1s', '11-1352-5123', 82472312, '2001-10-03', 'perfil1.jpg', 'Admin'),
(2, 'Lucia', 'Aserda', 'luciaserdi1@gmail.com', 'LUc1C@ana1s', '11-2323-1245', 82312950, '2004-10-03', 'perfil2.jpg', 'Usuario'),
(3, 'Mario', 'Gaspar', 'mariomariogas@gmail.com', 'M@rt1GasPAR', '11-2316-3412', 82642612, '2000-06-21', 'perfil3.jpg', 'Usuario'),
(4, 'Camila', 'Angeles', 'camirange@gmail.com', 'C@mi1Las2', '11-6342-1270', 45129423, '2001-12-13', 'perfil4.png', 'Usuario');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `adopciones`
--
ALTER TABLE `adopciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk__formulario_id__formularios` (`formulario_id`),
  ADD KEY `fk__mascota_id__mascotas` (`mascota_id`);

--
-- Indices de la tabla `donaciones`
--
ALTER TABLE `donaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk__usuario_id__usuarios` (`usuario_id`);

--
-- Indices de la tabla `formularios`
--
ALTER TABLE `formularios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk__form_usuario_id__usuarios` (`usuario_id`);

--
-- Indices de la tabla `mascotas`
--
ALTER TABLE `mascotas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `un__correo__usuarios` (`correo`),
  ADD UNIQUE KEY `un__telefono__usuarios` (`telefono`),
  ADD UNIQUE KEY `un__dni__usuarios` (`dni`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `adopciones`
--
ALTER TABLE `adopciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `donaciones`
--
ALTER TABLE `donaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `formularios`
--
ALTER TABLE `formularios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `mascotas`
--
ALTER TABLE `mascotas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `adopciones`
--
ALTER TABLE `adopciones`
  ADD CONSTRAINT `fk__formulario_id__formularios` FOREIGN KEY (`formulario_id`) REFERENCES `formularios` (`id`),
  ADD CONSTRAINT `fk__mascota_id__mascotas` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`);

--
-- Filtros para la tabla `donaciones`
--
ALTER TABLE `donaciones`
  ADD CONSTRAINT `fk__usuario_id__usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `formularios`
--
ALTER TABLE `formularios`
  ADD CONSTRAINT `fk__form_usuario_id__usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
