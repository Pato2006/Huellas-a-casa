USE huellas_a_casa;
INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento,ruta_img,tipo)
VALUES ("Juan","Pérez","juan.perez@hotmail.com","CONTRASENA123!", "9876523", "11-4562-9902", "1950-01-01", "perfil5.jpg", "Usuario");
INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento,ruta_img,tipo)
VALUES ("Maria","Lopez","marialopezan@gmail.com","hfdsSf7h", "40987352", "11-0987-9902", "1950-01-01", "perfil6.jpg", "Usuario");
INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento,ruta_img,tipo)
VALUES ("Carlos","Gómez","carlos.gomez@gmail.com","Tr3s#Azu", "4455123", "11-2345-6781", "1962-03-14", "perfil7.jpg", "Usuario");
INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento,ruta_img,tipo)
VALUES ("Laura","Fernández","laura.fernandez@hotmail.com","Sol@9Mar", "5566234", "11-3456-7892", "1975-07-22", "perfil8.jpg", "Usuario");
INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento,ruta_img,tipo)
VALUES ("Martín","Rodríguez","martin.rodriguez@yahoo.com","Pato$7Xy", "6677345", "11-4567-8903", "1958-11-05", "perfil9.jpg", "Usuario");
INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento,ruta_img,tipo)
VALUES ("Sofía","Martínez","sofia.martinez@gmail.com","Luna#45K", "7788456", "11-5678-9014", "1983-01-30", "perfil10.jpg", "Usuario");
INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento,ruta_img,tipo)
VALUES ("Diego","Sánchez","diego.sanchez@outlook.com","Mesa!8Rq", "8899567", "11-6789-0125", "1970-09-18", "perfil11.jpg", "Usuario");
INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento,ruta_img,tipo)
VALUES ("Valentina","Romero","valentina.romero@gmail.com","Rio&2Ver", "9900678", "11-7890-1236", "1990-12-02", "perfil12.jpg", "Usuario");

SELECT nombre, apellido ,correo, telefono, dni, fecha_nacimiento, ruta_img FROM usuarios
WHERE correo = "luciaserdi1@gmail.com";

SELECT * FROM usuarios
WHERE tipo = 'Usuario';

SELECT correo, donaciones.estado FROM usuarios
INNER JOIN donaciones 
ON usuarios.id = donaciones.usuario_id
WHERE correo = "luciaserdi1@gmail.com";

SELECT correo, mascotas.nombre "nombre mascota", adopciones.estado FROM usuarios
INNER JOIN formularios 
ON usuarios.id = formularios.usuario_id
INNER JOIN adopciones
ON formularios.id = adopciones.formulario_id
INNER JOIN mascotas
ON adopciones.mascota_id = mascotas.id


UPDATE usuarios
SET nombre = "Lucrecia"
WHERE correo = "luciaserdi1@gmail.com";

UPDATE usuarios
SET apellido = "Serdi"
WHERE correo = "luciaserdi1@gmail.com";

UPDATE usuarios
SET correo = "mariogaspar@gmail.com"
WHERE correo = "mariomariogas@gmail.com";

UPDATE usuarios
SET telefono = "11-2316-1111"
WHERE correo = "mariomariogas@gmail.com";






