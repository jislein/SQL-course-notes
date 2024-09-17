# DELETE y UPDATE - Operaciones Clave para el Mantenimiento de Datos

## Borrar registros (`delete`)

Para eliminar registros de una tabla usamos el comando `delete`:

```sql
delete from nombre_tabla;
```

Este muestra un mensaje indicando la cantidad de registros que ha eliminado. Si no queremos eliminar todos los registros sino solamente algunos, debemos indicar cual o cuales, para ello utilizamos el comando `delete` junto con la clausula `where` con la cual establecemos la condición que deben cumplir los registros a borrar.

Por ejemplo queremos eliminar aquel registro cuyo nombre de usuario es `"Marcelo"`:

```sql
delete from usuarios
where nombre="Marcelo";
```

### Explicación y Ejemplos

Si solicitamos el borrado de un registro que no existe, es decir, ningún registro cumple con la condición especificada, ningún registro será eliminado.

>[!important]
>Debemos tener en cuenta que si no colocamos una condicion, se eliminaran todos los registros de la tabla nombrada.

#### Ejemplo

```sql
use Curso_DB;
go
if object_id('usuarios') is not null
    drop table usuarios;

create table usuarios(
    nombre varchar(30),
    clave varchar(10)
);

go

insert into usuarios (nombre,calve)
    values ('Marcelo','River');
insert into usuarios (nombre,calve)
    values ('Susana','chapita');
insert into usuarios (nombre,calve)
    values ('CarlosFuentes','Boca');
insert into usuarios (nombre,calve)
    values ('FerelicoLopez','Boca');

select * from usuarios;
```

Elimina el registro cuyo nombre de usuario es "Marcelo".
```sql
delete from usuarios
    where nombre='Marcelo';

select * from usuarios;
```

Intentamos eliminarlo nuevamente (no se borra registro)
```sql
delete from usuarios
    where nombre='Marcelo';

select * from usuarios;
```

Eliminamos todos los registros cuya clave es "Boca"
```sql
delete from usuarios
    where clave='Boca';

select * from usuarios;
```

De igual forma podemos usar los [**operadores relacionales**]() a la hora de utilizar el comando `delete` junto con la clausula `where`.

Eliminamos todos los registros
```sql
delete from usuarios;
```

## Actualizar registros (`update`)

Decimos que se actualiza un registro cuando modificamos alguno de sus valores. Para modificar uno o varios datos de una o varios registros utilizamos `update`. Por ejemplo en nuestra tabla `usuarios`, queremos cambiar los valores de todas las claves, por "RealMadrid".

```sql
update usuarios set clave='RealMadrid';
```

Utilizamos `update` junto al nombre de la tabla y `set` junto con el campo a modificar y su nuevo valor. Este cambio afectará a todos los registros.

Podemos modificar algunos registros, para ello debemos establecer condiciones de seleccion con `where`. Por ejemplo, queremos cambiar el valor correspondiente a la clave de nuestro usuario llamado "Federicolopez", queremos como nueva clave "Boca", necesitamos una condicion `where` que afecte solamente a este registro:

```sql
update usuarios set clave='Boca'
    where nombre='Federicolopez;
```

### Explicacion y Ejemplos

Si Microsoft SQL Server no encuentra registros que cumplan con la condicion del `where`, nos e modifica ninguno.

>[!important]
>Las condiciones no son obligatorias, pero si omitimos la clausula `where`, la actualizacion afectara a todos los registros.

Tambien podemos actualizar varios campos en una sola instrucción:
```sql
update nombre_tabla set nombre_campo1=nuevo_valor1, nombre_campo2=nuevo_valor2
    where nombre_campo=valor_campo;
```

Para ello colocamos `update`, el nombre de la tabla, `set` junto al nombre del campo y el nuevo valor y separado por coma, el otro nombre del campo con su nuevo valor.

#### Ejemplos

```sql
use Curso_DB;
go
if object_id('usuarios') is not null
    drop table usuarios;

create table usuarios(
    nombre varchar(30),
    clave varchar(10)
);

go

insert into usuarios (nombre,calve)
    values ('Marcelo','River');
insert into usuarios (nombre,calve)
    values ('Susana','chapita');
insert into usuarios (nombre,calve)
    values ('Carlosfuentes','Boca');
insert into usuarios (nombre,calve)
    values ('Ferelicolopez','Boca');

select * from usuarios;
```

```sql
-- En este ejemplo vemos como se actualiza del campo 'clave' de todos los registros de la tabla.
update usuarios set clave='RealMadrid';

select * from usuarios;
```

```sql
-- En este ejemplo vemos como al registro que cumple con la condicion se le actualiza el campo 'clave'.
update usuarios set clave='Boca'
    where nombre='Ferelicolopez';

select * from usuarios;
```

```sql
-- En este ejemplo vemos como no se actualiza nada porque ningun registro cumple con la condicion.
update usuarios set clave='payaso'
    where nombre='JuanaJuarez';
    
select * from usuarios;
```

```sql
-- Aqui podemos ver como actualizamos varios campos que cumplen con la condicion.
update usuarios set nombre='Marceloduarte', clave='Marce'
    where nombre='Marcelo';
    
select * from usuarios;
```