# Otros operadores relacionales - `between` e `in`

## Explicacion y Ejemplos


Ingresemos el siguiente lote de comandos en el SQL Server Management Studio:
```sql
if object_id ('libros') is not null
    drop table libros;
create table libros (
    codigo int identity,
    titulo varchar(40) not null,
    autor varchar(20) default 'Desconocido',
    editorial varchar(20),
    precio decimal(6,2),
);
go

insert into libros
    values('El aleph', 'Borges', 'Emece', 15.90);
insert into libros
    values('Cervantes y el quijote', 'Borges', 'Paidos', null);
insert into libros
    values('Alicia en el pais de las maravillas', 'Lewis Carroll',null,19.90);
insert into libros
    values('Martin Fierro', 'Jose Hernandez', 'Emece', 25.90);
insert into libros
    values('Matematica estas ahi', 'Paenza', 'Siglo XXI',15);
insert into libros (titulo, autor, precio)
    values('Antología poética', 'Borges', 25.50);
insert into libros (titulo, autor, precio)
    values('Java en 10 minutos', 'Mario Molina',45.80);
insert into libros (titulo, autor)
    values('Martin Fierro', 'Jose Hernandez');
insert into libros (titulo, autor)
    values('Aprenda PHP', 'Mario Molina');
```

### `is null`

```sql
select * from libros
    where editorial is null;

select * from libros
    where editorial is not null;
```

### `between`

Recuperamos los registros cuyo precio esté entre 20 y 40 empleando `between`:
```sql
select * from libros
    where precio between 20 and 40;
```

Para seleccionar los libros cuyo precio NO esté entre un intervalo de valores antecedemos `not` al `between`:
```sql
select * from libros
    where precio not between 20 and 35;
```

### `in`

Devuelve los registros del campo que coincidan con el listado (los valores dentro del parentesis)

```sql
--Muestra todos los registros donde el 'autor' coincida con el listado.
select * from libros
    where autor in('Borges','Paenza');

--Muestra todos los registros donde el 'autor' NO coincida con el listado.
select * from libros
    where autor not in('Borges','Paenza');

--Este es un ejemplo mostrando que se puede tener una subconsulta en vez de un listado.
select * from libros
    where autor in(select autor from autores where femenino='si');
```
