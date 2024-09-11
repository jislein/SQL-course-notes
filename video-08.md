# NULL vs NOT NULL: Claves para la Integridad de Datos en SQL Server

Null significa dato desconocido o valor inexistente. No es lo mismo que un valor sea 0 o una cadena vacia a que sea literalmente nulo.

## Explicacion y Ejemplos

### Data Necesaria

```sql
Use Curso_DB;
go

if object_id('libros') is not null
    drop table libros;
```

### Ejemplos

Tenemos nuestra tabla "libros". El campo titulo no deberia estar vacio nunca, igualmente el campo "autor".

Para ello, al crear la tabla, debemos especificar que dichos campos no admitan valores nulos:

```sql
create table libros(
    titulo varchar(30) not null,
    autor varchar(20) not null,
    editorial varchar(15) null,
    precio float
);
```

Para especificar que un campo no admita valores nulos, debemos colocar `not null` luego de la definicio del campo. En el ejemplo anterior, los campos `editorial` y `precio` si admiten valores nulos.

Cuando colocamos `null` estamos diciendo que admite valores nulos (caso del campo `editorial`) por defecto, es decir, si no lo aclaramos, los campos permiten valores nulos (caso del campo `precio`).

Si ingresamos los datos de un libro, para el cual aun no hemos definido el precio podemos colocar `null` para mostrar que no tiene precio:

```sql
insert into (titulo, autor, editorial, precio)
    values('El aleph', 'Borges', 'Emece', null);

select * from libros;
```

>[!note]
>Notese que el valor `null` no es una cadena de caracteres, no se coloca entre comillas.

Entonces, si un campo acepta valores nulos, podemos ingresar `null` cuando no conocemos el valor.

Tambien podemos colocar `null` en el campo `editorial` si desconocemos el nombre de la editorial a la cual pertenece el libro que vamos a ingresar:

```sql
insert into (titulo, autor, editorial, precio)
    values('Alicia en el pais', 'Lewis Carroll', null, 25);
```

Si intentamos ingresar el valor `null` en campos que no admiten valores nulos (como `titulo` o `autor`), SQL Server no lo permite, muestra un mensaje y la insercion no se realiza. Por ejemplo:

```sql
insert into (titulo, autor, editorial, precio)
    values(null, 'Borges', 'Siglo XXI', 25);
```

Para ver cuales campos admiten valores nulos y cuales no, podemos emplear el procedimiento almacenado `sp columns` junto al nombre de la tabla. Nos muestra mucha informacion, en la columna `IS_NULLABLE` vemos que muestra `NO` en los campos que no permiten valores nulos y `YES` enlos campos que si los permiten.

```sql
exec sp_columns libros;
```

Para recuperar los registros que contengan el valor `null` en algun campo, no podemos utilizar los operadores relacionales vistos aneriormente: `=` (igua) y `<>` (distinto); debemos utilizar los operadores `is null` (es igual a null) y `is not null` (no es null):

```sql
select * from libros
    where precio is null;
```
La sentencia anterior tendra una salida diferente a la siguiente:

```sql
select * from libros
    where precio=0;
```
Con la primera sentencia veremos los libros cuyo `precio` es igual a `null` (desconocido); con la segunda, los libros cuyo `precio` es 0.

Igualmente para campos de tipo cadena, las siguientes sentencial `select` no retornaran los mismos registros:

```sql
select * from libros where editorial is null;
select * from libros where editorial='';
```

Con la primera sentencia veremos los libros cuya `editorial` es igual a `null`, con la segunda, los libros cuya `editorial` guarda una cadena vacia.

Entonces, para que un campo no permita valores nulos debemos especificarlo luego de definir el campo, agregando `not null`. Por defecto, los campos permiten valores nulos, pero podemos especificarlo igualmente agregando `null`.
