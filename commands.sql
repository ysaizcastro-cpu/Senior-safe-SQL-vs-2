--create
create table familiar (
  familiar_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  apellido TEXT NOT NULL,
  Cedula BIGINT,
  correo VARCHAR(50),
  telefono INTEGER,
  parentesco TEXT NOT NULL,
  direccion VARCHAR(60)NOT NULL,
  adultomayor_id INTEGER
);
--create
create table hogar(
  hogar_id INTEGER PRIMARY KEY,
  Direccion VARCHAR(100),
  municipio VARCHAR(100),
  tipodevivienda TEXT NOT NULL,
  adultomayor_id INTEGER
);
--create
create table diagnostico_cognitivo(
diagnostico_id INTEGER PRIMARY KEY,
nombre_patologia VARCHAR(50),
fase_etapa VARCHAR(50),
fecha_diagnostico DATE
);
--create
create table adultomayor(
  adultomayor_id INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  apellidos TEXT NOT NULL,
  Cedula INTEGER,
  edad INTEGER,
  telefono INTEGER,
  direccion VARCHAR(100),
  hogar_id INTEGER  
);
--create
create table padecer(
  adultomayor_id INTEGER,
  diagnostico_id INTEGER,
  FOREIGN KEY(adultomayor_id) REFERENCES adultomayor (adultomayor_id),
  FOREIGN KEY(diagnostico_id) REFERENCES diagnostico_cognitivo(diagnostico_id)
);
--create
create table alerta(
  alerta_id INTEGER PRIMARY KEY,
  fecha_hora TIMESTAMP,
  tipo_alerta VARCHAR(100),
  nivel_riesgo VARCHAR(100),
  estado VARCHAR(50),
  hogar_id INTEGER,
  FOREIGN KEY (alerta_id) REFERENCES hogar(hogar_id)
);
INSERT INTO adultomayor(adultomayor_id,nombre,apellidos) VALUES
(1,'Ana','perez'),
(2,'Miguel','perez'),
(3,'juan','barragan'),
(4,'sandra','ramirez'),
(5,'andres','saiz'),
(6,'mariana','castillo'),
(7,'martha','castro'),
(8,'sofia','alvarado'),
(9,'jampier','joya'),
(10,'harrison','orjuela'),
(11,'jose','castrillon'),
(12,'maria','nieves'),
(13,'alejandro','carrillo'),
(14,'cristhian','saiz'),
(15,'zuly','ochoa');
INSERT INTO diagnostico_cognitivo(diagnostico_id,nombre_patologia,fase_etapa) VALUES
(100,'alzheimer','Leve'),
(101,'alzheimer','moderada'),
(102,'demencia_cenil','grave'),
(103,'alzheimer','grave'),
(104,'demencia_cenil','leve'),
(105,'demencia_cenil','moderada'),
(106,'alzheimer','leve'),
(107,'alzheimer','moderada'),
(108,'demencia_cenil','grave'),
(109,'alzheimer','leve'),
(110,'alzheimer','moderada'),
(111,'alzheimer','grave'),
(112,'alzheimer','leve'),
(113,'demencia_cenil','moderada'),
(114,'alzheimer','leve');
INSERT INTO familiar(familiar_id,name,apellido,cedula,correo,parentesco,direccion) VALUES
(200,'oswal','saiz','1023528896','oswald@gmail.com','mama','calle 34 a sur n 31-61'),
(201,'juan','castro','102525252','juanpedro@gmail.com','papa','calle 13 n 30-242'),
(202,'jose','mendez','1033252525','jose@hotmail.com','hijo','calle 12 n 25-25'),
(203,'Miguel','castro','1036985852','miguelangelpi1@hotmail.com','hijo','calle 13 n 30-323'),
(204,'maria','sabogal','102588282','marias35@gmail.com','hija','calle 54 a sur 31-61'),
(205,'jose','salgado','1025639336','josesito@hotmail.com','hijo','calle 20 n 22-25'),
(206,'juana','herrera','1025863325','juana25@gmail.com','hija','carrera 25 n 98-85'),
(207,'gerardo','martinez','1025897722','gerardo83@gmail.com','hijo','diagonal 28 n 35-95'),
(208,'maritza','martinez','1025828285','mari123@gmail.com','hija','calle 14 25 852'),
(209,'manuel','alvarado','1025852582','manuelito25@hotmail.com','sobrino','transversal 14 85 98'),
(210,'cristian','saiz','1033923528','aguilyllo12@hotmail.com','hijo','calle 52 n 36 -95'),
(211,'diego','bernal','1252825828','diego1993@gmail.com','nieto','calle 20 15-89'),
(212,'sofia','castro','1025899828','sofi2021@hotmail.com','nieta','calle 12 58-85'),
(213,'zuly','castro','102582825828','zulybella@hotmail.com','hija','carrera 15 n 36-98'),
(214,'giovanny','beltran','1025852582','giova79@gmail.com','hijo','calle 54 a 25-98');
INSERT INTO hogar(hogar_id,direccion,tipodevivienda,adultomayor_id) VALUES
(300,'calle 13 n 20-98','rural','400'),
(301,'calle 25 n 21-30','urbana','401'),
(302,'calle 20 n 36-45','urbana','402'),
(303,'carrera 12 n 36-25','urbana','403'),
(304,'calle 20-25-12','rural','404'),
(305,'calle 52 n 85-25','urbana','405'),
(306,'calle 25 n 36-85','rural','406'),
(307,'diagonal 35- 32-96','rural','407'),
(308,'calle 25 32-85','urbana','408'),
(309,'carrera 12-85-89','rural','409'),
(310,'calle 85 98-36','rural','410'),
(311,'avenida 39-32','urbana','411'),
(312,'diagonal 56 32-89','rural','412'),
(313,'calle 52 85 -85','urbana','413'),
(314,'carrera 21 n 32-58','urbana','414');
INSERT INTO padecer(adultomayor_id,diagnostico_id) VALUES
(1,'100'),
(2,'101'),
(3,'102'),
(4,'103'),
(5,'104'),
(6,'105'),
(7,'106'),
(8,'107'),
(9,'108'),
(10,'109'),
(11,'110'),
(12,'111'),
(13,'112'),
(14,'113'),
(15,'114');








