# Usos del `having` y su diferencia con `where`

 Así como la cláusula `whee` permite seleccionar (o rechazar) registros individuales, la cláusula `having` permite seleccionar (o rechazar) un grupo de registros.

 Una cláusula `having` en SQL especifica que una declaración SQL `select` solo debe devolver filas donde los valores agregados cumplan con las condiciones especificadas.

 ## Explicacion y Ejemplos

Data necesaria:
```sql
if object_id('libros') is not null
	drop table libros;

create table libros (
	codigo int identity, 
	titulo varchar(40), 
	autor varchar(30), 
	editorial varchar(15), 
	precio decimal(5,2), 
	cantidad tinyint, 
	primary key(codigo)
);

go

insert into libros
	values('El aleph', 'Borges', 'Planeta', 35, null);
insert into libros
	values('Martin Fierro', 'Jose Hernandez', 'Emece', 22.20,200); 
insert into libros
	values('Martin Fierro', 'Jose Hernandez', 'Planeta',40, 200); 
insert into libros
	values('Antologia poetica','J.L. Borges','Planeta',null,150); 
insert into libros
	values('Aprenda PHP', 'Mario Molina', 'Emece', 18, null); 
insert into libros
	values('Manual de PHP', 'J.C. Paez', 'Siglo XXI',56,120); 
insert into libros
values('Cervantes y el quijote', 'Bioy Casares- J.L. Borges', 'Paidos',null,100); 
insert into libros
	values('Harry Potter y la piedra filosofal', 'J.K. Rowling', default, 45.00,90); 
insert into libros
	values('Harry Potter y la camara secreta', 'J.K. Rowling', 'Emece', null,100);
```

 Si queremos saber la cantidad de libros agrupados por editorial usamos la siguiente instruccion ya aprendida:
 ```sql
 select editorial, count(*)
    from libros
    group by editorial;
```

Si queremos saber la cantidad de libros agrupados por editorial pero considerando solo algunos grupos, por ejemplo, los que devuelvan un valor mayor a 2, usamos la siguiente instruccion:
```sql
 select editorial, count(*) from libros
    group by editorial
    having count(*)>2;
```

Se utiliza `having`, seguido de la condicion de busqueda,, para seleccionar ciertas filas retornadas por la cláusula `group by`.

Veamos otros ejemplos. Queremos el promedio de los precios de los libros agrupados por `editorial`, pero solamente de aquellos grupos cuyo promedio supere los 25 pesos:
```sql
 select editorial, avg(precio) from libros
    group by editorial
    having avg(precio)>25;
```

En algunos casos es posible confundir las cláusulas `where` y `having`. Queremos contar los registros agrupados por `editorial` sin tener en cuenta la editorial `"Planeta"`.

Analicemos las siguientes sentencias:
```sql
 select editorial, count(*) from libros
    where editorial<>"Planeta"
    group by editorial;

select editorial, count(*) from libros
    group by editorial
    having editorial<>"Planeta";
```

Ambas devuelven el mismo resultado, pero son diferentes. La primera, selecciona todos los registros rechazando los de la editorial `"Planeta"` y luego los agrupa para contarlos. La segunda, selecciona todos los registros, los agrupa para contarlos y finalmente rechaza fila con la cuenta correspondiente a la editorial `"Planeta"`.

No debemos confundir la cláusula `where` con la cláusula `having`; la primera establece condiciones para la seleccion de registros de un `select`; la segunda establece condiciones para la seleccion de registros de una salida `group by`.

Veamos otros ejemplos combinando `where` y `having`. Queremos la cantidad de libros, sin considerar los que tienen `precio` nulo, agrupados por `editorial`, sin considerar la editorial `"Planeta"`:
```sql
select editorial, count(*) from libros
    where precio is not null
    group by editorial
    having editorial<>"Planeta";
```

Aqui, selecciona los registros rechazando los que no cumplan con la condicion dada en `where`, luego los agrupa por `editorial`y finalmente rechaza los grupos que no cumplan con la condicion dada en el `having`.

Se emplea la cláusula `having` con funciones de agrupamiento, esto no puede hacerlo la cláusula `where`. Poe ejemplo, queremos el promedio de los precios agrupados por `editorial`, de aquellas editoriales que tienen mas de 2 libros:
```sql
select editorial, avg(precio) from libros
group by editorial
having count(*) > 2;
```
En una cláusla `having` puede haber **hasta 128 condiciones**. Cuando utilice varias condiciones, tiene que combinarlas con operadores logicos (`and`, `or`, `not`).

Podemos encontrar el mayor valor de los libros agrupados y ordenados por `editorial` y selecionar las filas que tengan un valor menor a `100` y mayor a `30`:
```sql
select editorial, max(precio) as 'mayor'
    from libros
    group by editorial
     having min(precio) < 100 and max(precio) < 30
     order by editorial;
```

Entonces usamos la cláusula `having` para restringir las filas que devuelve una salida `group by`. Va siempre despues de la cláusula `group by` y antes de la cláusula òrder by`si la hubiere.




