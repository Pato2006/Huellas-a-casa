USE huellas_a_casa;
--Todas las donaciones
SELECT donaciones.id, donaciones.monto, usuarios.nombre, usuarios.apellido, usuarios.ruta_img, donaciones.ruta_comp 
FROM donaciones 
INNER JOIN usuarios 
ON donaciones.usuario_id = usuarios.id

--Donaciones de una persona
SELECT donaciones.monto, donaciones.estado, donaciones.mensaje, usuarios.nombre, usuarios.apellido 
FROM donaciones 
INNER JOIN usuarios
ON donaciones.usuario_id= usuarios.id
WHERE usuarios.id = 5