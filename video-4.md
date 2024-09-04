# Dominando la Creación de Tablas

## Crear una tabla

Para crear una tabla mediante un query utilizamos la siguiente sintaxis:

```sql
/* Sintaxis */
create table NOMBRETABLA(
	NOMBRECAMPO1 TIPODATO,
	NOMBRECAMPO2 TIPODATO,
	...
	NOMBRECAMPON TIPODATO
);

/* Ejemplo */
create table usuarios(
	nombre varchar(30),
	clave varchar(10)
);
```

>[!nota]
>Si intentamos crear una tabla con un nombre ya existente, mostrará un mensaje indicando que ya hay un objeto llamado 'usuarios' en la base de datos y la sentencia no se ejecutará.

>[!important] Importante
>- Cada campo con su tipo debe separarse con una coma, a excepción del ultimo.
>- Los nombres de las tablas pueden usar cualquier carácter permitido para crear directorios (carpetas), el primer carácter debe ser un carácter alfabético y no puede contener espacios. La longitud maxima es de 128 caracteres.

## Eliminar una tabla

Para eliminar una tabla de la base de datos utilizamos:

```sql
/* Sintaxis */
drop table NOMBRETABLA;

/* Esto eliminaria la tabla 'usuarios' */
drop table usuarios;
```

Cuando intentamos eliminar una tabla que no existe nos marca el siguiente error: 

![[./images/Pasted_image_20240904054756.png]]

Para evitar esto podemos utilizar lo siguiente:

```sql
--Con esto especificamos que solo elimine la tabla si esta existe.
if object_id('usuarios') is not null
	drop table usuarios;
```

## Mostrar tablas

Para ver todas las tablas dentro de una base de datos:

```sql
exec sp_tables;
```

![[./images/Pasted_image_20240904044540.png]]

Para mostrar solo las tablas de un dueño (table_owner) en especifico:

```sql
/* Sintaxis */
exec sp_tables @table_owner='DUEÑOTABLA';

/*Ejemplo:
Esto mostraria solo las tablas donde el dueño sea dbo.*/
exec sp_tables @table_owner='dbo';
```

![[./images/Pasted_image_20240904045302.png]]

Para mostrar la estructura de una tabla usamos:

```sql
--Sintaxis
exec sp_columns NOMBRETABLA;

--Ejemplo
exec sp_columns usuarios;
```

![[./images/Pasted_image_20240904052105.png]]

