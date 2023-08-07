tercera pre-entrega| Python comision-43860 

  

apps: 

Home (aquí está la parte más visual de la app web) 

Register (aquí están los formularios y controla la base de datos) 

  

descripción general: 

Este programa web cuenta con una página principal (esta página cuenta), de regístrate (esta página contiene un formulario para registrarte), de iniciar sesión (la cual no está funcional) y una para reservar un día (para que el mecánico te pueda ver el auto). 

Como ejecutar el programa: 

(si no hay países cargar algunos países desde admin, hay que hacer lo mismo para sexos (agregar: hombre, mujer y prefiero no mencionarlo)) 

En register cargar alguna persona. 

Posteriormente en reservar hay que hacer una reserva, esta se subirá a la base de datos, y desde admin veremos una casilla que no está en la página (esta atendido?), esta es un buleano que podremos modificar para saber si ya está atendido, este lo podríamos modificar. 

 

URLs: 

Home = http://127.0.0.1:8000 

Regístrate= http://127.0.0.1:8000/register/ 

Iniciar sesión = http://127.0.0.1:8000/login/ 

Reservas = http://127.0.0.1:8000/reservas/ 

Admin = http://127.0.0.1:8000/admin/ 

Usuario: admin 

Contraseña: 123 

 

Errores conocidos: 

En la página Regístrate (en el código) se utilizan demasiados “<br>” para lograr que quede bien la página. 

Los nombres de las apps no siguen las convenciones de django (no empiezan con mayúscula) 

 

Cosas a mejorar: 

La página login no es funcional. 

Le falta estilos para mejorar el aspecto.

cosas a instalar en el entorno virtual:
django: comando (win10): pip install django
pillow: comando (win 10): pip install pillow


anotaciones para el creador:
resuelto:/  *le falta corregir el bug de las imagenes en el CRUD de Productos*
resuelto:/  *(no es muy nesesario) le falta poner la variable cuerpo del slider.html el el html productos_show*
resuelto:/  *le falta poner las URLs del CRUD de productos en la APP de producto*
resuelto:/  *le falta hacer un buscador de elementos en el CRUD de productos*


le falta hacer el CRUD en el Perfil
le falta agregar para que el usuario pueda elegir su foto de perfil


resuelto:/  *le falta crear proveedores con su CRUD pertinente*
resuelto:/  *le falta agregar al formulario de "Registrate" los campos de apellido y nombre los cuales no deben ser opcionales y el email hay que hacerlo que no sea opcional*
