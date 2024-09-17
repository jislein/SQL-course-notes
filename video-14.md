 # Introducción a las Funciones

Una función es un conjunto de sentencias que operan como una unidad lógica. Una función tiene un nombre, retorna un parámetro de salida y opcionalmente acepta parámetros de entrada. Las funciones de SQL Server no pueden ser modificada, las funciones definidas por el usuario si.

SQL Server ofrece varios tipos de funciones para realizar distintas operaciones. Se pueden clasificar de la siguiente manera:

1. De agregado: realizan operaciones que combinan varios valores y retornan un único valor. Son `count`, `sum`, `min`, `max`.
2. Escalares: toman un solo valor y retornan un único valor.
3. De conjuntos de filas: retornan conjuntos de registros.

## Funciones Escalares

Las funciones escalares pueden agruparse en:

- De configuración: retornan información referida a la configuración.
- De cursores: retornan información sobre el estado de un cursor.
- De fecha y hora: reciben un parámetro de tipo fecha y hora y retornan un valor de cadena, numérico o de fecha y hora.
- Matemáticas: realizan operaciones numéricas, geométricas y trigonométricas.
- De metadatos: informan sobre las bases de datos y los objetos.
- De seguridad: devuelven información referente a usuarios y funciones.
- De cadena: devuelven un valor de cadena o numérico.
- Del sistema: informan sobre opciones, objetos y configuraciones del sistema.
- Estadísticas del sistema: retornan información referente al rendimiento del sistema.
- Texto e imagen: realizan operaciones con valor de entrada de tipo `text` o `image` y retornan información referente al mismo.

## Explicación y Ejemplos

### Funciones Matemáticas

Las funciones matemáticas realizan operaciones con expresiones numéricas y retornan un resultado, operan con tipos de datos numéricos.

Microsoft SQL Server tiene algunas funciones para trabajar con números. Aquí presentamos algunas.

`abs(x)`: retorna el valor absoluto del argumento `x`. Ejemplo:
```sql
select abs(-20); --retorna 20.
```

`ceiling(x)`: redondea hacia arriba el argumento `x`. Ejemplo:
```sql
select ceiling(12.34); --retorna 13.
```

`floor(x)`: redondea hacia abajo el argumento `x`. Ejemplo:
```sql
select floor(12.34); --retorna 12.
```

`%`: devuelve el resto de una división. Ejemplo:
```sql
select 10%3; --retorna 1.
```

`power(x,y)`: retorna el valor de `x` elevado a la `y` potencia. Ejemplo:
```sql
select power(2,3); --retorna 8.
```

`round(numero,longitud)`: retorna un número redondeado a la longitud especificada. `longitud` debe ser `tinyint`, `smallint` o `int`. Si `longitud` es positivo, el número de decimales es redondeado según `longitud`; si es negativo, el número es redondeado desde la parte entera según el valor de `longitud`. Ejemplos:
```sql
select round(123.456,1); --retorna 123.400, es decir, redondea desde el primer decimal.

select round(123.456,2); --retorna 123.460, es decir, redondea desde el segundo decimal.

select round(123.456,-1); --retorna 120.000, es decir, redondea desde el primer valor entero (hacia la izquierda).

select round(123.456,-2); --retorna 100.000, es decir, redondea desde el segundo valor entero (hacia la izquierda).
```

`sign(x)`: si el argumento es un valor positivo devuelve `1`; `-1` si es negativo y `0` si es 0.

`square(x)`: retorna el cuadrado del argumento. Ejemplo:
```sql
select square(3); --retorna 9.
```

`sqrt(x)`: devuelve la raíz cuadrada del valor enviado como argumento.

SQL Server dispone de funciones trigonométricas que retornan radianes.

Se pueden emplear estas funciones enviando como argumento el nombre de un campo de tipo numérico.

### Funciones para el manejo de cadenas

Microsoft SQL Server tiene algunas funciones para trabajar con cadenas de caracteres. Estas son algunas:

`substring(cadena,inicio,longitud)`: devuelve una parte de la cadena especificada como primer, argumento, empezando desde la posición especificada por el segundo argumento y de tantos caracteres de longitud como indica el tercer argumento. Ejemplo:
```sql
select substring('Buenas tardes mas caracteres',8,6); --retorna 'tardes'.
```

`str(numero,longitud,cantidades_decimales)`: convierte número a caracteres; el primer parámetro indica el valor numérico a convertir, el segundo la longitud del resultado (debe ser mayor o igual a la parte entera del número más el signo si lo tuviese) y el tercero, la cantidad de decimales. El segundo y tercer argumento son opcionales y deben ser positivos. String significa cadena en inglés. Ejemplo: se convierte el valor numérico de `123.456` a cadena, especificando `7` de longitud y `3` decimales:
```sql
select str(1243.456,7,3); --retorna '1243.456'.
select str(-123.46,7,3); --retorna '-123.46'.
```

Si no se colocan el segundo y tercer argumento, la `longitud` predeterminada es 10 y la cantidad de decimales es 0 y se redondea a entero. Ejemplo: se convierte el valor numérico `123.456` a cadena:
```sql
select str(123.456); --retorna '123'.
select str(123.456,3); --retorna '123'.
```

Si el segundo parámetro es menor a la parte entera del número, devuelve asteriscos (`*`). Ejemplo:
```sql
select str(123.456,2,3); --retorna "**".
```

`stuff(cadena1,inicio,cantidad,cadena2)`: inserta la cadena enviada como cuarto argumento, en la posición indicada en el segundo argumento, reemplazando la cantidad de caracteres indicada por el tercer argumento en la cadena que es primer parámetro. Stuff significa rellenar en inglés. Ejemplo:
```sql
select stuff('abcde',3,2,'opqrs'); --retorna 'abopqrse'.
``


Es decir, coloca en la posición 2 la cadena la cadena `"opqrs"` y reemplaza 2 caracteres de la primera cadena. Los argumento numéricos deben ser positivos y menor o igual a la longitud de la primera cadena, caso contrario, retorna `null`. Si el tercer argumento es mayor que la primera cadena, se elimina hasta el primer carácter.

`len(cadena)`: retorna la longitud de la cadena enviada como argumento. `"len"` viene de **length**. Ejemplo:
```sql
select len('Hola'); --retorna 4.
```

`char(x)`; retorna un carácter en código ASCII del entero enviado como argumento. Ejemplo:
```sql
select char(65); --retorna "A".
```

`left(cadena,longitud)`: retorna la cantidad (`longitud`) de caracteres de la cadena comenzando desde la izquierda, es decir, desde el primer carácter. Ejemplo:
```sql
select left('buenos dias',8); --retorna "buenos d".
```

`right(cadena,longitud)`: retorna la cantidad (`longitud`) de caracteres de la cadena comenzando desde la derecha, es decir, desde el último carácter. Ejemplo:
```sql
select left('buenos dias',8); --retorna "nos días".
```

`lower(cadena)`: retorna la cadena con todos los caracteres en minúsculas. `lower` significa reducir en inglés. Ejemplo:
```sql
select lower('HOLA ESTUDIAnte'); --retorna "hola estudiante".
```

`upper(cadena)`: retorna la cadena con todos los caracteres en mayúsculas. Ejemplo:
```sql
select upper('hola estudiante'); --retorna "HOLA ESTUDIANTE".
```

`ltrim(cadena)`: retorna la cadena con los espacios en blanco de la izquierda eliminados. Trim significa recortar en inglés. Ejemplo:
```sql
select ltrim('     Hola     '); --retorna "Hola     ".
```

`rtrim(cadena)`: retorna la cadena con los espacios en blanco de la derecha eliminados. Ejemplo:
```sql
select rtrim('     Hola     '); --retorna "     Hola".
```

`replace(cadena,cadena_objetivo,cadena_nueva)`: retorna la cadena con todas las ocurrencias de la `cadena_objetivo` reemplazadas por la `cadena_nueva`. Ejemplo:
```sql
select replace('xxx.sqlserverya.com','x','w'); -- retorna "www.sqlserverya.com".
```

`reverse(cadena)`: devuelve la cadena invirtiendo el orden de los caracteres. Ejemplo:
```sql
select reverse('Hola'); -- retorna 'aloH'.
```

`patindex(patron,cadena)`: devuelve la posición de comienzo (de la primera ocurrencia) del patrón especificado en la cadena enviada como segundo argumento. Si no lo encuentra retorna 0. Ejemplos:
```sql
select patindex('%Luis%', 'Jorge Luis Borges'); --retorna 7.

select patindex('%or%', 'Jorge Luis Borges'); --retorna 2.

select patindex('%ar%', 'Jorge Luis Borges'); --retorna 0.
```

`charindex(subcadena,cadena,inicio)`: devuelve la posición donde comienza la `subcadena` en la `cadena`, comenzando la búsqueda desde la posición indicada por `inicio`. Si el tercer argumento no se coloca, la búsqueda inicia desde 0. Si no lo encuentra retorna 0. Ejemplos:
```sql
select charindex('or', 'Jorge Luis Borges',5); --retorna 13.

select charindex('or', 'Jorge Luis Borges'); --retorna 2.

select charindex('or', 'Jorge Luis Borges',14); --retorna 0.
```

`replicate(cadena,cantidad)`: repite una `cadena` la `cantidad` de veces especificada. Ejemplo:
```sql
select replicate('Hola',3); --retorna HolaHolaHola.
```

`space(cantidad)`: retorna una cadena de espacios de longitud indicada por `cantidad`, que debe ser un valor positivo. Ejemplo:
```sql
select 'Hola'+space(1)+'que tal'; --retorna 'Hola que tal'.
```

Se pueden emplear estas funciones enviando como argumento el nombre de un campo de tipo carácter.

### Funciones para el manejo de Fechas

Microsoft SQL Server ofrece algunas funciones para trabajar con fechas y horas. Estas son algunas:

`getdate()`: retorna la fecha y hora actuales. Ejemplo:
```sql
select getdate();
```

`datepart(parteDeFecha,fecha)`: retorna la parte específica de una `fecha`, el año, trimestre, día, hora, etc.

Los valores para `parteDeFecha` pueden ser:

- `year` (año)
- `quarter` (cuarto)
- `month` (mes)
- `day` (dia)
- `week` (semana)
- `hour` (hora)
- `minute` (minuto)
- `second` (segundo)
- `millisecond` (milisegundo)

Ejemplos:
```sql
select datepart(month,getdate()); -- retorna el número de mes actual.
select datepart(day,getdate()); -- retorna el día actual.
select datepart(hour,getdate()); -- retorna la hora actual.
```

`datename(partedefecha,fecha)`: retorna el nombre de una parte específica de una `fecha`. Los valores para `partedefecha` pueden ser los mismos que se explicaron anteriormente. Ejemplos:
```sql
select datename(month,getdate()); --retorna el nombre del mes actual;
select datename(day,getdate()); --retorna el nombre del dia actual;
```

`dateadd(partedelafecha,numero,fecha)`: agrega un intervalo a la `fecha` especificada, es decir, retorna una `fecha` adicionando a la fecha enviada como tercer argumento, el intervalo de tiempo indicado por el primer parámetro, tantas veces como lo indica el segundo parámetro. Los valores para el primer argumento pueden ser: `year` (año), `quarter` (cuarto), `month` (mes), `day` (día), `week` (semana), `hour` (hora), `minute` (minuto), `second` (segundo), `millisecond` (milisegundo). Ejemplos:
```sql
select dateadd(day,3,'1980/11/02'); --retorna "1980/11/05", agrega 3 dias.

select dateadd(month,3,'1980/11/02'); --retorna "1981/02/02", agrega 3 meses.

select dateadd(hour,2,'1980/11/02'); --retorna "1980/11/02 2:00:00", agrega 2 horas.

select dateadd(minute,16,'1980/11/02'); --retorna "1980/11/02 00:16:00", agrega 16 minutos.
```

`datediff(partedelafecha,fecha1,fecha2)`: calcula el intervalo de tiempo (según el primer argumento) entre las 2 fechas. El resultado es un valor entero que corresponde a `fecha2-fecha1`. Los valores de `partedelafecha` pueden ser los mismos que se explicaron anteriormente. Ejemplos:
```sql
select datediff(day, '2005/10/28', '2006/10/28'); --retorna 365 (días).

select datediff(month, '2005/10/28', '2006/11/29'); --retorna 13 (meses).
```

`day(fecha)`: retorna el día de la fecha especificada. Ejemplo:
```sql
select day(getdate());
```

`day(fecha)`: retorna el mes de la fecha especificada. Ejemplo:
```sql
select month(getdate());
```

`year(fecha)`: retorna el año de la fecha especificada. Ejemplo:
```sql
select year(getdate());
```