# Explorando SELECT y la Cláusula WHERE para Recuperación de Registros

## Recuperar campos específicos (`select`)

Para ver todos los registros de una tabla utilizamos `select`.

```sql
select * from nombre_tabla;
```

El asterisco (*) indica que se seleccionan todos los campos de la tabla.

Tambien podemos especificar el nombre de los campos que queremos ver separándolos por comas:

```sql
select nombre_campo_1, nombre_campo_2 from nombre_tabla;
```

### Explicación

#### Data necesaria

Ingresamos el siguiente lote de comandos en el SQL Server Management Studio:

```sql
Use Curso_DB;

if object_id('libros') is not null
    drop table libros;

-- Creamos la tabla libos
create table libros(
    titulo varchar(40),
    autor varchar(30),
    editorial varchar(15),
    -- Se podria usar tanto un tipo de dato 'float' como un tipo de dato 'decimal'.
    -- Parametros que recibe el 'decimal': decimal(CantidadDeCaracteresAntesDelPunto, CantidadDeCaracteresDespuesDelPunto)
    precio decimal(13,2),
    -- El tipo de dato 'integer' tambien se puede abreviar 'int'.
    cantidad int
);
```

#### Ejemplo

Llamamos al procedimiento almacenado `sp_columns` para conocer los campos de la tabla libros.

```sql
exec sp_columns libros;
```

Insertamos varias filas en la tabla libros:

```sql
insert into libros (titulo, autos, editorial, precio, cantidad)
    values ('El aleph', 'Borges', 'Emece', 25.50, 100);
insert into libros (titulo, autos, editorial, precio, cantidad)
    values ('Alicia en el pais de las maravillas', 'Lewis Carroll', 'Atlantida', 10, 200);
insert into libros (titulo, autos, editorial, precio, cantidad)
    values ('Matematica estas ahi', 'Paenza', 'Siglo XXI', 18.8, 200);
```

Recuperamos todos los datos de la tabla libros:

```sql
select * from libros;
```

Recuperamos sol el `titulo`, `autor` y `editorial` de la tabla libros.

```sql
select titulo,autor,editorial from libros;
```

Recuperamos el `titulo` y el `precio`.

```sql
select titulo,precio from libros;
```

Recuperamos la `editorial` y la `cantidad`.

```sql
select editorial,cantidad from libros;
```

Para agregar un comentario y que no lo tenga en cuenta el servidor SQL Server debemos agregar `--` antes del comentario.

```sql
-- Es bueno comentar los algoritmos que implementamos sobre todo aquellos que sean complejos de entender.
```

>[!hint]
>Dentro del SQL Server Management Studio podemos posicionarnos en una linea y presionar `Ctrl + C` y se comentará la linea completa.

## Recuperar algunos registros (`where`)

Existe una cláusula, `where` con la cual podemos especificar condiciones para una consulta `select`. Esto quiere decir que podemos recuperar algunos registros que cumplan con ciertas condiciones indicadas en la cláusula `where`. Por ejemplo, queremos ver el usuario cuyo nombre es "Marcelo", para ello utilizamos `where` y luego de ella, la condición.

Sintaxis:

```sql
select nombre_campo_1, nombre_campo_2, ..., nombre_campo_n
    from nombre_tabla
    where condicion;
```

### Explicación

#### Data necesaria

Ingresamos el siguiente lote de comandos:

```sql
Use Curso_DB;
go

if object_id('usuario') is not null
    drop table usuarios;

create table usuarios (
    nombre varchar(30),
    clave varchar(10)
);
go

exec sp_columns usuarios;

insert into usuarios (nombre, clave)
    values ('Marcelo', 'Boca');
insert into usuarios (nombre, clave)
    values ('JuanPerez', 'Juancito');
insert into usuarios (nombre, clave)
    values ('Susana', 'River');
insert into usuarios (nombre, clave)
    values ('Luis', 'River');
```

#### Explicación y ejemplos

Para las condiciones se utilizan operadores relacionales. El signo igual (`=`) es un operador relacional.

Para la siguiente selección de registros especificamos una condición que solicita a los usuarios cuya clave es igual a `'River'`:

```sql
select nombre,clave
    from usuarios
    where clave='River';
```

Si ningun registro cumple la condicion establecida con el `where`, no aparecera ningun registro.

Recuperamos el usuario cuyo nombre es `'Leonardo'`

```sql
select * from usuarios
    where nombre='Leonardo';
```

Para recuperar algunos campos de algunos registros combinamos en la consulta la lista de campos y la cláusula `where`:

```sql
select nombre
    from usuarios
    where clave='River'
```

En la consulta anterior solicitamos el nombre de todos los usuarios cuya clave sea igual a `'River'`.

## Clausula `go` 

La clausula `go` se utiliza para separar bloques de comandos. En algunos casos veremos la necesidad de que primero se ejecute algun bloque de comandos antes de continuar con el siguiente. Esto nos permite detener la ejecucion de un query si en algun bloque se presenta un error o no se cumple alguna condición.

## Operadores relacionales

Los operadores son simbolos que permiten realizar operacionies matematicas, concatenar cadenas, hacer comparaciones. SQL Server tiene 4 tipos de operadores:

1. Relacionales
2. Aritmeticos
3. De concatenacion
4. Logicos

De momento solo veremos los relacionales los cuales son los siguientes:

`=` - igual a...
`<>` - distinto/diferente de...
`>` - mayor que...
`<` - menor que...
`>=` - mayor o igual a...
`<=` - menor o igual a...

### Explicación

#### Datos necesarios

Ingresamos el siguiente lote de comandos:

```sql
Use Curso_DB;
go

if object_id('libros') is not null
    drop table libros;

create table libros(
    titulo varchar(30),
    autor varchar(30),
    editorial varchar(15),
    precio float
);
go

insert into libros (titulo,autor,editorial,precio)
    values ('El aleph','Borges','Emece',24.50);
insert into libros (titulo,autor,editorial,precio)
    values ('Martin Fierro','Jose Hernandez','Emece',16.00);
insert into libros (titulo,autor,editorial,precio)
    values ('Aprender PHP','Mario Molina','Emece',35.40);
insert into libros (titulo,autor,editorial,precio)
    values ('Cervantes y el quijote','Borges','Paidos',50.90);
```

#### Explicaciones y Ejemplos

Podemos seleccionar los registros cuyo autor sea diferente de `'Borges'`, para ello usamos la condicion:

```sql
select * from libros
    where autor<>'Borges'
```

Podemos comprar valores numericos. Por ejemplo, queremos mostrar los titulos y precios de ls libros cuyo precio sea mayor a 20 pesos:

```sql
select titulo, precio
    from libros
    where precio>20;
```

Queremos seleccionar los libros cuyo precio sea menor o igual a 30:

```sql
select * from libros
    where precio<=30;
```

>[!important]
>Los operadores relacionales comparan valores del mismo tipo. Se emplean para comprobar si un campo cumple con una condicion.