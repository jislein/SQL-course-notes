# Dominando el Identity en SQL Server

El atributo `identity` permite indicar el valor de inicio de la secuencia y el incremento, para ellos usamos la siguiente sintaxis:

```sql
create table libros(
    codigo int identity(100,2),
    titulo varchar(20),
    autor varchar(30),
    precio float
);
```

Los valores comenzarán en `100` y se incrementarán de 2 en 2; es decir, el primer registro ingresado tendra el valor de `100`, los siguientes `102`, `104`, `106`, etc.

La funcion `ident_seed()` retorna el valor de inicio del campo `identity` de la tabla que nombramos.
La funcion `ident_incr()` retorna el valor de incremento del campo `identity` de la tabla nombrada.

```sql
select ident_seed('libros');
select ident_incr('libros');
```

## Explicación y Ejemplos

Cuando un campo tiene el atributo `identity` no se puede ingresar valor para él, porque se inserta automáticamente tomando el ultimo valor como referencia, o `1` si es el primero.

Para ingresar registros omitidos el campo definido como `identity`, por ejemplo:

```sql
insert intro libros (titulo,autor,editorial,precio)
 values('El aleph','Borges','Emece',23);
 ```

 Este primer registro ingresado guardará el valor en 1 en el campo correspondiente al codigo.

 Si continuamos ingresando registros, el codigo (dato que no ingresamos) se cargará automaticamente siguiendo la secuencia de autoincremento.

 No esta permitido ingresar el valor correspondiente al campo `identity`, por ejemplo:

 ```sql
 insert into libros (codigo,titulo,autor,editorial,precio)
    values(5,'Martin Fierro','Jose Hernandez','Paidos',25);
-- generará un mensaje de error.
```

`identity`permite indicar el valor de inicio de la secuencia y el incremento, pero lo veremos posteriormente.

Un campo definido como `identity` generalmente se establece como clave primaria.

Un campo `identity` no es editable, es decir, no se puede ingresar un valor ni actualizarlo.

Un campo `identity` no permite valores nulos, aunque no se indique específicamente.

Si ejecutamos el procedimiento `sp_columns()` veremos que en el campo `codigo` en la columna `TYPE_NAME` aparece `init identity` y en la columna `IS NULLABLE` aparece `NO`.

Los valores secuenciales de un campo ` identity` se generan tomando como referencia el ultimo valor ingresado si se elimina el ultimo registro ingresado (por ejemplo 3) y luego se inserta otro registro, SQL Server seguirá la secuencia, es decir, colocar el valor `4`.

---

### Ejemplos

Desafortunadamente el instructor saltó la parte de los ejemplos.

---

Hemos visto que en un campo declarado `identity` no puede ingresarse explícitamente un valor.

Para permitir ingresar un valor en un campo de identidad se debe activar la opción `identity_insert`:

```sql
set identity_insert libros on;
```

Es decir, podemos ingresar valor en un campo `identity` seteado con la opción `identity_insert` en `on`.

Cuando cunado `identity_insert` esta en `ON`, las instrucciones `insert deben explicar un valor:

```sql
insert into libros (codigo,titulo)
    values(5,'Alicia en el pais de las maravillas');
```

Si no se coloca un valor para el campo de identidad, la sentencia no se ejecuta y aparece un mensaje de error:

```sql
insert into libros (titulo,autor,editorial)
    values('Matematica estas ahi','Paenza','Paidos');
```

El atributo `identity` no implica unicidad, es decir, permite repeticion de valores; por ello hay que tener cuidado al explicitar un valor porque se puede ingresar un valor repetido.

Para desactivar la opcion `identity_insert` tipeamos:

```sql
set identity_insert libros off;
```

### Ejemplos

Desafortunadamente el instructor termino el video sin mostrar la parte de los ejemplos.
