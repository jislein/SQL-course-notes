# TRUNCATE vs DELETE vs DROP

Para borrar todos los registros de una tabla se usa `delete` sin condicion `where`. Tambien podemos eliminar todos los registros de una tabla con `truncate table`.

Por ejemplo, queremos vacial la tabla `libros`, usamos:

```sql
truncate table libros;
```

La sentencia `truncate table` vacia la tabla (elimina todos los registros) y conserva la estructura de la tabla.

La diferencia con `drop table` es que esta sentencia borra la tabla, `truncate table` la vacia.

La diferencia con `delete` es la velocidad, es mas rapido `truncate table` que `delete` ( se nota cuando la cantidad de registros es muy grande) ya que este borra los registros uno a uno.

Otra diferencia es la siguiente: cuando la tabla tiene un campo `identity`, si borramos todos los registros con `delete` y luego ingresamos un registro, al cargarse el valor en el campo de identidad,cojntinua con la secuencia teniendo en cuanta el valor mayor que se habia guardado; si usamos `truncate table` para borrar todos los registros, al ingresar otra vez un registro, la secuencia del campo de identidad vuelve a iniciarse en `1`.

>[!important]
>Con el `truncate table` no se puede usar `where`.

## Ejemplos

```sql
if object_id('libros') is not null
    drop table libros;

create table libros(
    codigo int identity,
    titulo varchar(30),
    autor varchar(20),
    editorial varchar(15),
    precio float
);

go

insert into libros (titulo, autor, editorial, precio)
    values ('El aleph','Borges','Emece',25.60);
insert into libros (titulo, autor, editorial, precio)
    values ('Uno','Richard Bach','Planeta',18);

select * from libros;
```

Truncamos la tabla:
```sql
truncate table libros;
```

Ingresamos nuevamente algunos registros:
```sql
insert into libros (titulo, autor, editorial, precio)
    values ('El aleph','Borges','Emece',25.60);
insert into libros (titulo, autor, editorial, precio)
    values ('Uno','Richard Bach','Planeta',18);
```

Si seleccionamos todos los registros vemos que la secuencia se reinició en `1`:
```sql
select * from libros;
```

Eliminemos todos los registros con `delete`:
```sql
delete from libros;
```

Ingresamos nuevamente algunos registros:
```sql
insert into libros (titulo, autor, editorial, precio)
    values ('El aleph','Borges','Emece',25.60);
insert into libros (titulo, autor, editorial, precio)
    values ('Uno','Richard Bach','Planeta',18);
```