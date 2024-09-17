# Descubriendo los Valores por Defecto (Default) en SQL Server

## Valores por defecto (`default`)

Al insertar registros no se especifica un valor para un campo que admite valores nulos, se ingresa automaticamente `null` y si el campo esta declarado `identity`, se inserta el siguiente de la secuencia. A estos valores se les denomina **valores por defecto o predeterminados**.

Un valor por defecto se inserta cuando no está presente al ingresar un registro y en algunos casos en que el dato ingresado es inválido.

Para campos de cualquier tipo no declarados `not null`, es decir, que admiten valores nulos, el valor por defecto es `null`. Para campos declarados `not null`, no existe valor por defecto, a menos que se declare explicitamente con la cláusula `default`.

Para todos los tipos, exepto los declarados `identity`, se pueden explicar valores por defecto con la clausula `default`.

## Explicacion

Podemos establecer valores por defecto para los campos cuando creamos la tabla. Para Ello utilizamos `default` al definir el campo. Por ejemplo, queremos que el valor por defecto del campo `autor` de la tabla `libros` sea `"Desconocido"` y el valor por defecto del campo `cantidad` sea `0`:

```sql
create table libros(
    codigo int identity,
    titulo varchar(40),
    autor varchar(30) null default 'Desconocido',
    editorial varchar(20),
    precio decimal(5,2),
    cantidad int default 0
);
```

Si al ingresar un nuevo registro omitimos los valores para el campo `autor` y `cantidad`, SQL Server insertará los valores por defecto; el siguiente valor de la secuencia en `codigo`, en `autor` colocará `"Desconocido"` y en cantidad `0`.

Entonces, si al definir un campo explicitamos un valor mediante la cláusula `default`, ése será el valor por defecto.

Ahora, al visualizar la estructura de la tabla con `sp_columns` podemos entender lo que informa la columna `COLUMN_DEF`, muestra el valor por defecto del campo.

Tambien se puede utilizar `default` para dar el valor por defecto alos campos en sentencias `insert`, por ejemplo:

```sql
insert into libros (titulo, autor, precio, cantidad)
    values ('El gato con botas',default,default,100);

select * from libros;
```

Si todos los campos de una tabla toenen valores predeterminados (ya sea por ser `identity`, permitir valores nulos o tener un valor por defecto), se puede ingresar un registro de la siguiente manera:

```sql
insert into libros default values;
```

La sentencia anterior almacenará un registro con los valores predeterminados para cada uno de sus campos.

Entonces, la cláusula `default` permite especificar el valor por defecto de un campo. Si no se explicita, el valor por defecto es `null`, siempre que el campo no hata sido declarado `not null`.

Los campos para los cuales no se ingresan valores en un `insert` tomarán los valores por defecto:

- Si tiene el atributo `identity`: el valor de inicio de la secuencia si es el primero o el siguiente valor de la secuencia, no admite cláusula `default`.
- Si permite valores nulos y no tiene cláusula `default`, almacenará `null`.
- Si está declarado explicitamente `not null`, no tiene valor `default` y no tiene el atributo `identity`, no hay valor por defecto, asi que causará un error y el `insert` no se ejecutará.
- Si tiene cláusula `default` (admita o no valores nulos), el valor definido como predeterminado.
- Para campos de tipo fecha y hora, si omitimos la parte de la fecha, el valor predeterminado para la fecha es `"1900-01-01"` y si omitimos la parte de la hora, `"00:00:00"`.

Un campo solo puede tener un valor por defecto. Una tabla puede tener todos sus campos con valores por defecto.

Que un campo tenga valor por defecto no significa que no admita valores nulos, puede o no admitirlos.