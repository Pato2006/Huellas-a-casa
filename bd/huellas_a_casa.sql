-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-11-2026 a las 21:19:12
-- Versión del servidor: 10.11.16-MariaDB
-- Versión de PHP: 8.5.12

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

--
-- Volcado de datos para la tabla `adopciones`
--

INSERT INTO `adopciones` (`id`, `formulario_id`, `mascota_id`, `estado`) VALUES
(1, 1, 6, 'En proceso'),
(2, 2, 7, 'Aceptado'),
(3, 3, 8, 'Rechazado'),
(4, 4, 6, 'En proceso'),
(5, 5, 7, 'Aceptado'),
(6, 6, 8, 'Rechazado');

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

--
-- Volcado de datos para la tabla `donaciones`
--

INSERT INTO `donaciones` (`id`, `usuario_id`, `monto`, `estado`, `mensaje`, `ruta_comp`) VALUES
(1, 1, 25000, 'Recibido', 'Espero que puedan seguir ayudando a muchos animales', 'comprobante6.jpg'),
(2, 2, 75000, 'No recibido', '', 'comprobante7.jpg'),
(3, 4, 150000, 'Recibido', 'Una pequeña ayuda para los gastos veterinarios', 'comprobante8.jpg'),
(4, 4, 35000, 'Recibido', 'Gracias por cuidar a los animales que necesitan un hogar', 'comprobante9.jpg'),
(5, 3, 5000, 'No recibido', 'Para colaborar con lo que haga falta', 'comprobante10.jpg'),
(6, 5, 200000, 'Recibido', 'Espero que este aporte sirva para comprar alimento', 'comprobante11.jpg'),
(7, 7, 45000, 'No recibido', '', 'comprobante12.jpg');

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

--
-- Volcado de datos para la tabla `formularios`
--

INSERT INTO `formularios` (`id`, `usuario_id`, `grupo_familiar`, `alergias`, `otras_mascotas`, `cuidador_ausencia`, `tiempo_solo`, `ubicacion`) VALUES
(1, 1, 'Vivo con mi esposa y dos hijos', 'Ninguna', 'Si, un perro de 5 años', 'Mi esposa trabaja desde casa', '2 horas por dia', 'Casa'),
(2, 2, 'Vivo sola con mi pareja', 'Si, al polvo', 'No tengo otras mascotas', 'Mi pareja puede cuidarlo', '6 horas, cuando trabajo', 'Departamento'),
(3, 3, 'Vivo con mis padres y mi hermano', 'Ninguna', 'Si, dos gatos de 3 años', 'Mis padres pueden cuidarlo', '4 horas por la mañana', 'Casa'),
(4, 4, 'Vivo con mi hija de 10 años', 'Mi hija es alergica al polen', 'No', 'Mi madre vive a pocas cuadras y ', '5 horas cuando estoy trabajando', 'PH'),
(5, 5, 'Vivo con mi hermano', 'Ninguna', 'Si, un gato de 2 años', 'Mi hermano puede quedarse con el', 'Nunca, siempre hay alguien en ca', 'Departamento'),
(6, 6, 'Vivo sola', 'Ninguna', 'Si, un conejo', 'Una amiga puede cuidarlo si es n', '8 horas durante la semana', 'PH'),
(7, 7, 'Vivo con mi esposa y mi hijo', 'Si, al pelo de gato', 'No tenemos mascotas actualmente', 'Mi esposa trabaja desde casa', '3 horas como maximo', 'Casa');

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
(1, 'Rocky', 6, 22.5, 'Activo y protector', 'Negro con pecho blanco y patas m', 1, 'Perro', 'Macho', 'imagen_1.jpg'),
(2, 'Mora', 2, 8.3, 'Tranquila y cariñosa', 'Marron claro con manchas blancas', 1, 'Perro', 'Hembra', 'imagen_2.jpg'),
(3, 'Toby', 3, 14.7, 'Jugueton y sociable', 'Pelaje dorado con orejas oscuras', 0, 'Perro', 'Macho', 'imagen_3.jpg'),
(4, 'Milo', 2, 4.5, 'Curioso y travieso', 'Gris atigrado con ojos verdes', 1, 'Gato', 'Macho', 'imagen_4.jpg'),
(5, 'Cleo', 4, 3.8, 'Independiente y afectuosa', 'Blanca con manchas grises en el ', 1, 'Gato', 'Hembra', 'imagen_5.jpg'),
(6, 'Duke', 7, 28.2, 'Leal y compañero', 'Marron oscuro con hocico negro', 1, 'Perro', 'Macho', 'imagen_6.jpg'),
(7, 'Pipa', 1, 2.9, 'Energica y juguetona', 'Tricolor con manchas negras y na', 0, 'Gato', 'Hembra', 'imagen_7.jpg'),
(8, 'Bruno', 5, 19.6, 'Amigable y obediente', 'Blanco con manchas marrones en e', 1, 'Perro', 'Macho', 'imagen_8.jpg');

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
(1, 'German', 'Gomez', 'gergomez1@gmail.com', 'G3rM@nGomez', '11-2342-1234', 18234621, '2000-11-08', 'perfil_1.jpg', 'Admin'),
(2, 'Maria', 'Laura', 'marianalaura@gmail.com', 'M@r1lauR0', '11-2318-0231', 83273162, '2002-10-01', 'perfil_2.jpg', 'Usuario'),
(3, 'Lautaro', 'Britez', 'lautabri@gmail.com', 'L@uatRB1as', '11-3924-1298', 22842731, '2001-12-03', 'perfil_3.jpg', 'Usuario'),
(4, 'Maria', 'Saenz', 'mrzaens@gmail.com', 'm@R1aS3Az', '11-5823-1650', 11394574, '2003-11-25', 'perfil_4.jpg', 'Usuario'),
(5, 'Emiliano', 'Vargas', 'emiliano.vargas@gmail.com', 'EmiR@a6G', '11-3145-8296', 39124567, '1994-06-18', 'perfil5.jpg', 'Usuario'),
(6, 'Abril', 'Navarro', 'abril.navarro@hotmail.com', 'ABR1kl2A@c\\', '11-6284-1937', 42876135, '2000-02-11', 'perfil6.jpg', 'Usuario'),
(7, 'Ramiro', 'Medina', 'ramiro.medina@yahoo.com', 'AR@S82asO', '11-7953-4628', 35412879, '1988-09-27', 'perfil7.jpg', 'Usuario');

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
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ruta_img` (`ruta_img`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `donaciones`
--
ALTER TABLE `donaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `formularios`
--
ALTER TABLE `formularios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `mascotas`
--
ALTER TABLE `mascotas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
