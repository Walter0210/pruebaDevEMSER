-- SQLite
--la cantidad de órdenes por campo ESTADO:
SELECT Estado, Count(ESTADO) as 'Cantidad de Ordenes'
from ORDENES
GROUP BY ESTADO

-- número de orden (NUM_OS) de aquellas órdenes que tenga un valor en el campo acceso_suministro.
SELECT *
FROM ORDENES
WHERE acceso_suministro <> ''

-- funcion para mostrar los campos [NUM_OS, RUTAITIN, RUTA, DIRECCION, ESTADO ] de 
--las órdenes que pertenecen a la ruta 12 y 13 o solo la ruta 15 (campo RUTA)

SELECT NUM_OS, RUTAITIN, RUTA, DIRECCION, ESTADO
FROM ORDENES
WHERE ruta in (12, 13) OR ruta=15