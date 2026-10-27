USE huellas_a_casa;
--Todas las adopciones
SELECT mascotas.nombre, mascotas.edad, mascotas.peso, mascotas.personalidad, mascotas.descripcion, mascotas.tipo, mascotas.genero, mascotas.ruta_img, adopciones.estado
FROM adopciones
INNER JOIN mascotas
ON adopciones.mascota_id = mascotas.id
