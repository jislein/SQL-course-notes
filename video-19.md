# Búsqueda de patrones (`like` - `not like`)

## Explicación y Ejemplos

Podemos comparar trozos de cadenas de caracteres para realizar consultas. Para recuperar todos los registros cuyo autor contenga la cadena `"Borges"` debemos tipear:
```sql
select * from libros
    where autor like '%Borges%';
```

El símbolo `%` (porcentaje) reemplaza cualquier cantidad de caracteres (incluyendo ningún carácter). Es un carácter comodín. `like` y `no like` son operadores de comparación que señalan igualdad o diferencia.


Para seleccionar todos los libros que comiencen con `"M"`:
```sql
select * from libros
    where titulo like 'M%';
```

Note que el símbolo `%` ya no está al comienzo, con esto indicamos que el título debe tener como primera letra la `M` y luego, cualquier cantidad de caracteres.

Para seleccionar todos los libros que NO comiencen con `"M"`:
```sql
select * from libros
    where titulo not like 'M%';
```

Así como `%` reemplaza cualquier carácter, el guión bajo " reemplaza un carácter, es otro carácter comodín. Por ejemplo, queremos ver los libros de `"Lewis Carroll"` pero no recordamos si se escribe `"Carroll"`  o `"Carrolt"`, entonces tipeamos esta condición:
```sql
select * from libros
    where titulo like '%Carrol_';
```

Otro carácter comodín es `[]` reemplaza cualquier carácter contenido en el conjunto especificado dentro de los corchetes.

Para seleccionar los libros cuya editorial comienza con las letras entre la `"P"` y la `"S"` usamos la siguiente sintaxis:
```sql
select titulo,autor,editorial
    from libros
    where editorial like '[P-S]%';
```

Ejemplos:
- `like '[a-cf-i]%'`: busca cadenas que comiencen con `a`, `b`, `c`, `f`, `g`, `h` o `i`.
- `like '[-acfi]%'`: busca cadenas que comiencen con `-`, `a`, `c`, `f` o `i`.
- `like 'A[_]9%'`: busca cadenas que comiencen con `A_9`.
- `like 'A[nm]%'`: busca cadenas que comiencen con `An` o `Am`.

El cuarto carácter comodín es `[^]` reemplaza cualquier carácter NO presente en el conjunto especificado dentro de los corchetes.

Par seleccionar los libros cuya editorial NO comienza con las letra `"P"` ni `"N"` tipeamos:
```sql
select titulo,autor,editorial
    from libros
    where editorial like '[^PN]%';
```

`like` se emplea con tipos de datos `char`, `nchar`, `varchar`, `nvarchar` o `datetime`. Si empleamos `like` con tipos de datos que no son caracteres, SQL Server convierte (si es posible) el tipo de dato a carácter. Por ejemplo, queremos buscar todos los libros cuyo precio se encuentre entre `10.00` y `19.99`:
```sql
select titulo,precio
    from libros
    where precio like '1_.%';
```

Queremos los libros que NO incluyen centavos en sus precios:
```sql
select titulo,precio from libros
    where precio like '%.00';
```

Para búsqueda de caracteres comodines como literales, debe incluirlo dentro de corchetes, por ejemplo si busca:

- `like '%[%]%`: busca cadenas que contengan el signo `%`.
- `like '%[_]%`: busca cadenas que contengan el signo `_`.
- `like '%[[]%`: busca cadenas que contengan el signo `[`.
