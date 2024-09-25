# SQL Joins: Diferencias Entre Inner/Left/Right/Outer/Cross Joins

Un `join` es una operación que relaciona dos o más tablas para obtener un resultado que incluya datos (campos y registros) de ambas; las tablas participantes se combinan según los campos comunes a ambas tablas.

Hay tres tipos de combinaciones:

- Combinanciones internas (`inner join` o `join`).
- Combinaciones externas (`left outer join`, `right outer join`, ` full outer join`).
- Combinaciones cruzadas (`cross join`).

## Combinacion interna (`inner join`)

La combinacion interna emplea `join`, que es la forma abreviada de `inner join`. Se emplea para obtener información de dos tablas y combinar dicha información en una salida.

la sintaxis básica es la siguiente:
```sql
select campo1, campo2, ...
    from tabla1
    join tabla2 on CondicionDeCombinacion;
```

### Explicación y Ejemplos

Data necesaria:
```sql
if object_id('libros') is not null
    drop table libros;
if object_id('editoriales') is not null
    drop table editoriales;

create table libros(
    codigo int identity,
    titulo varchar(40),
    autor varchar(30) default 'Desconocido',
    codigoeditorial tinyint not null,
    precio decimal(5,2)
);

create table editoriales(
    codigo tinyint identity,
    nombre varchar(20),
    primary key (codigo)
);

go

insert into editoriales values('Planeta');
insert into editoriales values('Emece');
insert into editoriales values('Siglo XXI');

insert into libros values('El aleph','Borges',2,20);
insert into libros values('Martin Fierro','Jose Hernandez',1,30);
insert into libros values('Aprenda PHP','Mario Molina',3,50);
insert into libros values('Java en 10 minutos',default,3,45);
```
---

```sql
select * from libros
    join editoriales on codigoeditorial=editoriales.codigo;
```

Analicemos la consulta anterior.

- Especificamos los campos que apareceran en el resultado en la lista de selección.
- Indicamos el nombre de la tabla luego del `from` (`libros`).
- Combinamos esa tabla con `join` y el nombre de la otra tabla (`editoriales`); se especifica qué tablas se van a combianr y cómo.

Cuando se combina informacion de varias tablas, es necesario especificar qué registro de una tabla se combinará con qué registro de la otra tabla, con `on`. Se debe especificar la condición para enlazarlas, es decir, el campo por el cual se combinarán, que tienen en común.

`on` hace coincidir registros de ambas tablas basándose en el valor de tal campo, en el ejemplo, el campo `codigoeditorial` de `libros` y el campo `codigo` de `editoriales` son los que enlazarán ambas tablas. Se emplean campos comunes, que deben tener tipos de datos iguales o similares.

La condicion de combinacion, es decir, el o los campos por los que se va a combinar (parte `on`), se especifica segun las claves primarias y externas.

Note que en la consulta, al nombrar el campo usamos el nombre de la tabla tambien. Cuando las tablas referenciadas tienen campos en igual nombre, esto es necesario para evitar confusiones y ambiguedades al momento de referenciar un campo. En el ejemplo, si no especificamos `editoriales.codigo` y solamente tipeamos `codigo`, SQL Server no sabra si nos referimos al campo `codigo` de `libros` o de `editoriales` y mostrara un mensaje de error indicando que `codigo` es ambiguo.

Entonces, si las tablas que combinamos tienen nombres de campos iguales, **DEBE** especificarse a que tabla pertenece anteponiendo el nombre de la tabla al nombre del campo, separandolo por un punto (`.`).

Si una de las tablas tiene clave primaria compuesta, al combinarla con la otra, en la clausula `on` se debe acer referencia a la clave completa, es decir, la condicion referenciara a todos los campos clave que identifican al registro.

Se puede incluir en la consulta `join` la clausula `where` para restringir los registros que retorna el resultado; tambien `order by`, `distinct`, etc...

Se emplea este tipo de combinaciones para encontrar registros de la primera tabla que se correspondan con los registros de la otra, es decir, que cumplan la condicion del `on`. Si un valor de la primera tabla no se encuentra en la segunda tabla, el registro no aparece.

Para simplificar la sentencia podemos usar un alias para cada tabla:
```sql
select l.codigo,titulo,autor,nombre
from libros as l
join editoriales as e
on l.codigoeditorial=e.codigo;
```

en algunos casos (como en este ejemplo) el uso de alias es para fines de simplificacion y ace ,as legible la consulta si es larga y compleja, pero en algunas consultas es absolutamente necesario.

## Combinacion externa

Vimos que una combinacion interna (`join`) encuentra registros de la primera tabla que se correspondan con los registros de la segunda, es decir, que cumplan la condicion del `on` y si un valor de la primera tabla no se encuentra en la segunda tabla, el registro no aparece.

Si queremos saber que registros de una tabla **NO** encuentran correspondencia en la otra, es decir, no existe valor coincidente en la segunda, necesitamos otro tipo de combinacion, `outer join` (combinacion externa).

Las combinaciones externas combinan registros de dos tablas que cumplen la condicion, mas los registros de la segunda tabla que no la cumplen; es decir, muestran todos los registros de las tablas relacionadas, aun cuando no aya valores coincidentes entre ellas.

Este tipo de combinacion se emplea cuando se necesita una lista completa de los datos de una de las tablas y la informacion que cumple con la condicion. **La combinaciones externas se realizan solamente entre 2 tablas**.

Hay tres tipos de combinaciones externas: `left outer join`, `right outer join` y `full outer join`; se pueden abreviar con `left join`, `right join` y `full join` respectivamente.

### `left join` - Explicacion y Ejemplos

Data necesaria:
```sql
if object_id('libros') is not null
    drop table libros;
if object_id('editoriales') is not null
    drop table editoriales;

create table libros(
    codigo int identity,
    titulo varchar(40),
    autor varchar(30) default 'Desconocido',
    codigoeditorial tinyint not null,
    precio decimal(5,2)
);

create table editoriales(
    codigo tinyint identity,
    nombre varchar(20),
    primary key (codigo)
);

go

insert into editoriales values('Planeta');
insert into editoriales values('Emece');
insert into editoriales values('Siglo XXI');

insert into libros values('El aleph','Borges',1,20);
insert into libros values('Martin Fierro','Jose Hernandez',1,30);
insert into libros values('Aprenda PHP','Mario Molina',2,50);
insert into libros values('Java en 10 minutos',default,4,45);
```
---

Se emplea una combinacion externa izquierda para mostrar todos los registros de la tabla de la izquierda.

Si no encuentra coincidencia en la table derecha, el registro muestra los campos de la segunda tabla seteados a `null`.

En el siguiente ejemplo solicitamos el titulo y nombre de la editorial de los libros:
```sql
select l.titulo,e.nombre
from editoriales as e
left join libros as l on l.codigoeditorial = e.codigo;
```

El resultado mostrara el titulo y el nombre de la editorial; las editoriales de las cuales no hay libros, es decir cuyo codigo de editorial no este presente en `libros` aparece en el resultado, pero con el valor `null` en el campo `titulo`.

Es importante la posicion en que se colocan las tablas en un `left join`, la tabla de la izquierda es la que se usa para localizar registros en la tabla de la dereca.

Entonces, un `left join` se usa para hacer coincidir registros en una tabla (izquierda) con otra tabla (derecha); si un valor de la tabla de la izquierda no encuentra coincidencia en la tabla de la derecha, se genera una fila extra (una por cada valor no encontrado) con todos los campos correspondientes a la tabla derecha seteados a `null`.

La sintexis básica es la siguiene:
```sql
select CAMPOS
    from TABLA_IZQUIERDA
    left join TABLA_DERECHA
    on CONDICION;
```

En el siguiente ejemplo solicitamos el título y el nombre de la editorial, la sentencia es similar a la anterior, la diferencia está en el orden de las tablas:
```sql
select from titulo,nombre
    from libros as l
    left join editoriales as  e
    on l.codigoeditorial = e.codigo;
```

El resultado mostrará el título del libro y el nombre de la editorial no está presente en `editoriales` aparecen en el resultado, pero con un valor `null` en el campo `nombre`.

Un `left join` puede tener cláusula `where` que restrinja el resultado de la consulta considerando solamente los registros que encuentran coincidencia en la tabla de la derecha, es decir, cuyo valor de código está presente en `libros`:
```sql
select titulo,nombre
from editoriales as e
left join libros as l
on e.codigo = l.codigoeditorial
where l.codigoeditorial is not null;
```

También podemos mostrar las editoriales que **NO** estan presentes en `libros`, es decir, que **NO** encuentran coincidencia en la tabla de la derecha:
```sql
select titulo, nombre
from editoriales as e
left join libros as l
on e.codigo = l.codigoeditorial
where l.codigoeditorial is null;
```

### `right join`

Basicamente lo mismo que el `left join`. Con la unicoa diferencia de que la tabla de la derecha será la que se utilizará para buscar los registros que coincidan con la de la izquierda y si un valor de la tabla derecha no se encuentra en la tabla izquierda, el registro muestra los campos correspondientes a la tabla de la izquierda seteados a `null`.

### `full join` - Explicacion y ejemplos

Vimos que un `left join` encuentra registros de la tabla izquierda que correspondan con los registros de la tabla derecha y si un valor de la tabla izquierda no se encuentra en la tabla derecha, el registro muestra los campos correspondientes a la tabla de la derecha seteados a `null`. Aprendimos también que un `right join` opera del mismo modo sólo que la tabla derecha es la que localiza los registros en la tabla izquierda.

Una combinación externa completa (`full outer join` o `full join`) retorna todos los registros de ambas tablas. Si un registro de una tabla izquierda no encuentra coincidencia en la tabla derecha, las columnas correspondientes a campos de la tabla derecha aparecen seteados a `null`, y si la tabla de la derecha no encuentra correspondencia en la tabla izquierda, los campos de esta última aparecen conteniendo `null`.

Usando la misma data que utilizamos para la explacion del `left join`, veamos un ejemplo:
```sql
select titulo,nombre
from editoriales as e
full join libros as l
on codigoeditorial = e.codigo;
```

La salida del `full join` precedente muestra todos los registros de ambas tabalas, incluyendo los libros cuyos `codigo` de editorial no existen en la tabla `editoriales` y las editoriales de las cuales no hay correspondencia en `libros`.

### `cross join` - Explicación y ejemplos

Vimos que hay 3 tipos de combinaciones:

1) Combinaciones internas (`join`).
2) Combinaciones externas (`left`, `right` y `full join`)
3) Combinaciones cruzadas.

Las combinaciones cruzadas (`cross join`) muestran todas las combinaciones de todos los registros de las tablas combinadas. Para este tipo de `join` no se incluye una condición de enlace. Se genera el producto cartesiano en el que el número de filas del resultado es igual al numero de registros de la primera tabla multiplicado por el número de registros de la segunda tabla, es decir, si hay 5 registros en una tabla y 6 en la otra, retorna 30 filas.

La sintaxis básica es ésta:
```sql
select CAMPOS
from TABLA1
cross join TABLA2;
```
---

Data necesaria:
```sql
if object_id('comidas') is not null
    drop table comidas;
if object_id('postres') is not null
    drop table postres;

create table comidas(
    codigo tinyint identity,
    nombre varchar(30),
    precio decimal(4,2)
);

create table postres(
    codigo tinyint identity,
    nombre varchar(30),
    precio decimal(4,2)
);

go

insert into comidas values('ravioles',5);
insert into comidas values('tallarines',4);
insert into comidas values('milanesa',7);
insert into comidas values('cuarto de pollo',6);

insert into postres values('flan',2.5);
insert into postres values('porcion torta',3.5)
```

Veamos un ejemplo. Un perqueo restaurante almacena los nombres y precios de sus comidas en una tabla llamada `comidas`. ye en una tabla denominada `postres` los mismos datos de sus postres.

Si necesitamos conocer todas las combinaciones posibles para un men, cada comida con cada postre, empleamos un `cross join`:
```sql
select c.nombre as 'plato principal', p.nombre as 'postre'
from comidas as c
cross join postres as p;
```

La salida muestra cada plato combinado con cada uno de los postres.

Como cualquier tipo de `join`, puede emplearse una cláusula `where` que condicione la salida.

## Autocombinaciones

Data necesaria:
```sql

if object_id('comidas') is not null
    drop table comidas;

create table comidas(
    codigo int identity,
    nombre varchar(30),
    precio decimal(4,2),I
    rubro char(6),-- 'plato'=plato principal', 'postre'=postre 
    primary key(codigo)
);

go

insert into comidas values('ravioles',5, 'plato');
insert into comidas values ('tallarines',4, 'plato');
insert into comidas values('milanesa',7, 'plato');
insert into comidas values ('cuarto de pollo',6, 'plato');
insert into comidas values('flan', 2.5, 'postre');
insert into comidas values ('porcion torta',3.5, 'postre');
```

Dijimos que es posible combinar una tabla consigo misma.

Un pequeño restaurante tiene almacenadas sus comidas en una tabla llamada `comidas` que consta de los siguientes campos:

```sql
nombre varchar(20),
precio decimal(4,2)
rubro char(6)-- que indica con 'plato' si es plato principal y 'postre' si es un postre.
```

Podemos obtener la combinación de los platos empleando un `cross join` con una sola tabla:

```sql
select c1.nombre as 'plato principal',
    c2.nombre as 'postre',
    c1.precio+c2.precio as total
    from comidas as c1
    cross join comidas as c2;
```

En la consulta anterior aparecen filas duplicadas, para evitarlo debemos emplear un `where`:
```sql
select c1.nombre as 'plato principal',
    c2.nombre as 'postre',
    c1.precio+c2.precio as total
    from comidas as c1
    cross join comidas as c2
    where c1.rubro='plato' and c2.rubro='postre';
```

En la consulta anterior se empleó un `where`que especifica que se combine `"plato"` con `"postre"`.

En una autocombinación se combina una tabla con una copia de si misma. Para ello debemos utilizar 2 alias para la tabla. Para evitar que aparezcan filas duplicadas debemos emplear un `where`.

Tambien se puede realizar una autocombinación con `join`:
```sql
select c1.nombre as 'plato principal',
    c2.nombre as postre,
    c1.precio+c2.precio as total
    from comidas as c1
    join comidas as c2 on c1.codigo<>c2.codigo
    where c1.rubro='plato' and c2.rubro='postre';
```

Para que no aparezcan filas duplicadas se agrega un `where`.

## Uso de combinaciones
 
 Como ya hemos visto distintos tipos de combinaciones:
 1) Combinaciones internas (`join`).
 2) Combinaciones externas (`left`, `right` y `full join`).
 3) Combinaciones cruzadas (`cross join`).

Veamos en lo adelamte mas usos y caracteristicas de estas combinaciones como son:

1) Combinaciones y funciones de agrupamiento
2) Combinaciones de mas de dos tablas
3) Combinaciones con `update` y `delete`

### Combinaciones y Funciones de Agrupamiento

Data necesaria:
```sql
if object_id('libros') is not null
    drop table libros;
if object_id('editoriales') is not null
    drop table editoriales;

create table libros(
    codigo int identity,
    titulo varchar(40),
    autor varchar(30),
    codigoeditorial tinyint not null,
    precio decimal(5,2)
);

create table editoriales(
    codigo tinyint identity,
    nombre varcar(20),
    primary key (codigo)
);

go

insert into editoriales values('Planeta')
insert into editoriales values('Emece')
insert into editoriales values('Siglo XXI')

insert into libros values('El aleph','Borges',1,20);
insert into libros values('Martin Fierro','Jose Hernandez',1,30);
insert into libros values('Aprenda PHP','Mario Molina',3,50);
insert into libros values('Uno','Richard Bach',3,15);
insert into libros values('Java en 10 minutos',default,4,45);
```

Podemos usar `group by` y las funciones de agrupamiento con combinaciones de tablas.

Para ver la cantidad de libros de cada editorial consultando la tabla `libros` y `editoriales`, tipeamos:
```sql
select nombre as editorial,
count(*) as cantidad
from editoriales as e
join libros as l on codigoeditorial=e.codigo
group by e.nombre;
```

Note que las editoriales que no tienen libros no aparecen en la salida porque empleamos un `join`.

Empleamos otra funcion de agrupamiento con `left join`. Para conocer el mayor precio de los libros de cada editorial usamos la funcion `max()`, hacemos un `left join` y agrupamos por `nombre` de la editorial.
```sql
select nombre as editorial,
max(precio) as 'mayor precio'
from editoriales as e
left join libros as l on codigoeditorial=e.codigo
group by nombre;
```

En la sentencia anterior, mostrara, para la editoria la cual no aya libros, el valor `null` en la columna calculada.

### Combinaciones de mas de dos tablas

Data necesaria:
```sql

if object_id('libros') is not null
    drop table libros;
if object_id('autores') is not null
    drop table autores;
if object_id('editoriales') is not null
    drop table editoriales;

create table libros(
    codigo int identity,
    titulo varchar (40),
    codigoautor int not null,
    codigoeditorial tinyint not null,
    precio decimal(5,2),
    primary key (codigo)
);

create table autores(
    codigo int identity,
    nombre varchar(20),
    primary key (codigo)
);

create table editoriales(
    codigo tinyint identity,
    nombre varchar(20),
    primary key (codigo)
);

go

insert into editoriales values ('Planeta');
insert into editoriales values ('Emece');
insert into editoriales values ('Siglo XXI');
insert into editoriales values ('Plaza');

insert into autores values ('Richard Bach');
insert into autores values ('Borges');
insert into autores values ('Jose Hernandez');
insert into autores values ('Mario Molina');
insert into autores values ('Paenza');

insert into libros values ('El aleph',2,2,20);
insert into libros values ('Martin Fierro',3,1,30);
insert into libros values ('Aprenda PHP',4,3,50);
insert into libros values ('Uno',1,1,15);
insert into libros values ('Java en 10 minutos',0,3,45);
insert into libros values ('Matematica estas ahi',0,0,15);
insert into libros values ('Java de la A a la Z',4,0,50);
```

Podemos hacer un `join` con mas de dos tablas.

Cada `join` combina 2 tablas. Se pueden emplear varios `join` para enlazar varias tablas. Cada resultado de un ` join` es una tabla que puede combinarse con otro `join`.

La libreria almacena los datos de sus libros en 3 tablas: `libros`, `editoriales` y `autores`. En la tabla `libros` un campo `codigoautor` ace referencia al autor y un campo `codigoeditorial` referencia la editorial.

Para recuperar todos los datos de los libros empleamos la siguiente consulta:
```sql
select titulo,a.nombre,e.nombre
from autories as a
join libros as l on codigoautor=a.codigo
join editoriales as e on codigoeditorial=e.codigo;
```

Analicemos la consulta anterior. Indicamos el nombre de la tabla luego del `from` (`autores`), combinamos esa tabla con la tabla `libros` especificando con `on` el campo por el cual se combinaran; luego debemos hacer coincidir los valores para el enlace con la tabla `editoriales` enlazandolas por los campos correspondientes. Utilizamos alias para una sentencia mas sencilla y comprensible.

Note que especificamos a que tabla pertenecen los campos cuyo nombre se repiten en las tablas, esto es necesario para evitar confusiones y ambiguedades al momento de referenciar un campo.

Note que no aparecen libros cuyo codigo de autor no se encuentra en `autores` y cuya editorial no existe en `editoriales`, esto es porque realizamos una combinacion interna.

Podemos combinar varios tipos de join en una misma sentencia:
```sql
select titulo,a.nombre,e.nombre
from autores as a
right join libros as l on codigoautor=a.codigo
left join editoriales as e on codigoeditorial=e.codigo;
```
En la consulta anterior solicitamos el titulo, autor y editorial de todods los libros que encuentren o no coincidencia con `autores` (`right join`) y a ese resultado lo combinamos con `editoriales`, encuentren o no coincidencia.

Es posible realizar varias combinaciones para obtener informacion de varias tablas. Las tablas deben tener claves externas relacionadas con las tablas a combinar.

En consultas en las cuales empleamos varios `join` es importante tener en cuenta el orden de las tablas y los tipos de `join`; recuerde que la tabla resultado del primer `join` es la que se combina con el segundo `join`, no la segunda tabla nombrada. En el ejemplo anterior, el `left join` no se realiza entre las tablas `libros` y `editoriales` sino entre el resultado del `right join` y la tabla `editoriales`.
