# Explorando el poder de las Primary Key

## Explicacion y Ejemplos

En el siguiente definimos una clave primaria, para nuestra tabla `usuarios` para asegurarnos que cada usuario tenga un nombre diferente y unico:

```sql
create table usuarios(
    nombre varchar(20),
    clave varchar(10),
    primary key(nombre)
);
```
Lo que hacemos es agregar, luego de la definicion de cada campo, `primary key` y entre parentesis, el nombre del campo que sera la clave primaria.

Una tabla solo puede tener una clave primaria. Cualquier campo (de cualquier tipo) puede ser clave primaria, debe cumplir como requisito, que sus valores no se repitan ni sean nulos. Por ello, al definir un campo como clave primaria, automaticamente SQL Server lo convierte a `not null`. Esto no quiere decir que solo un campo pueder una clave primaria, sino que todos los campos establecidos dentro de la definicion son la clave primaria. Ejemplo:

```sql
primary key(nombre_campo_1, nombre_campo_2, ..., nombre_campo_n)
```

Luego de haber establecido un campo como clave primaria, al ingresar los registros, SQL Server controla que los valores para el campo establecido como clave primaria no esten repetidos en la tabla; si estuviesen repetidos, muestra un mensaje y la insercion no se realiza. Es decir, si en nuestra tabla `usuarios` ya existe un usuario con nombre `"juanperez"` e intentamos ingresar un nuevo usuario con nombre `"juanperez"`, aparece un mensaje y la instruccion `insert` no se ejecuta.

Igualmente, si realizamos una actualizacion, SQL Server controla que los valores para el campo establecido como clave primaria no esten repetidos en la tabla, si lo estuviese, aparece un mensaje indicando que se viola la clave primaria y la actualizacion no se realiza.

### Ejemplos

Ingresamos el siguiente lote de comandos en el SSMS:

```sql
if object_id('usuarios') is not null
    drop table usuarios;

create table usuarios(
    nombre varchar(20),
    clave varchar(10),
    primary key(nombre)
);
go

exec sp_help usuarios;

insert into usuarios (nombre, clave)
    values ('juanperez','Boca');
insert into usuarios (nombre, clave)
    values ('raulgarcia','River');
```

Intentando ingresar un valor de clave primaria existente (genera error):

```sql
insert into usuarios (nombre, clave)
    values ('juanperez','payaso');
```

Intentamos ingresar el valor `null` en el campo clave primaria (genera error):

```sql
insert into usuarios (nombre, clave)
    values (null,'payaso');
```

Intentemos actualizar el nombre de un usuario colocando un nombre existente (genera error):

```sql
update usuarios set nombre='juanperez'
    where nombre='raulgarcia';
```

