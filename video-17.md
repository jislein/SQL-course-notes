# Operadores Logicos `AND`, `OR` y `NOT`

## Explicacion y Ejemplos

Si queremos recuperar todos los libros cuyo autor sea igual a `"Borges"` y cuyo precio no supere los 20 pesos, necesitamos 2 condiciones:
```sql
select * from libros
    where (autor='Borges') and
    (precio<=20);
```

Los registros recuperados en una sentencia que une 2 condiciones con el operador `and`, cumplen con las 2 condiciones.

Queremos ver los libros cuyo autor sea `"Borges"` y/o cuya editorial sea `"Planeta"`:
```sql
select * from libros
    where autor='Borges' or
    editorial='Planeta';
```

En la sentencia anterior usamos el operador `or`; indicamos que recupere los registros en los cuales el valor del campo `autor` sea `"Borges"` y/o el valor del campo `editorial` sea `"Planeta"`, es decir, seleccionará los registros que cumplan con la primera condición, con la segunda condición o con ambas condiciones.

Los registros recuperados con una sentencia que une 2 condiciones con el operador `or`, cumplen 1 de las condiciones.

Queremos recuperar los libros que NO cumplan con la condicion dada, por ejemplo, aqueyos cuya editorial NO sea `"Planeta"`:
```sql
select * from libros
    where not editorial='Planeta';
```

El poerador `not` invierte el resultado de la condición a la cual antecede.

Los registros recuperados en una sentencia en la cual aparece el operador `not`, no cumplen con la condición. 

Los parentesis se usan para encerrar condiciones, para que se evalúen como una sola expresión. Cuando explicitamso varias condiciones con diferentes operadores lógicos (combinamos `and`, `or`) permite establecer el orden de prioridad de la evaluacion.

Por ejemplo, las siguientes expresiones devuelven un resultado diferente:
```sql
select * from libros
    where (autor='Borges') or
    (editorial='Paidos' and precio<20);

select * from libros
    where (autor='Borges' or editorial='Paidos') and
    (precio<20);
```

El orden de prioridad de los operadores logicos es el siguiente: `not` se aplica antes que `and` y `and` antes que `or`, si no se especifica un orden de evaluacion mediante el uso de parentesis.
