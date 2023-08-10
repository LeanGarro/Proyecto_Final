tercera pre-entrega| Python comision-43860 

  

apps: 

Home (aquí está la parte más visual de la app web) 

Register (aquí están los formularios y controla la base de datos) 

  

descripción general: 

Este programa web cuenta con una página principal, de regístrate (esta página contiene un formulario para registrarte), de iniciar sesión, una para reservar un día (para que el mecánico te pueda ver el auto), de about (llamada nosotros), de ver proveedores (esto gracias a un for, cuenta con un CRUD al cual solo el staff puede acceder lo mismo para el aspecto distinto que tiene la pagina a la hora de verla como staff e imagenes ademas de un slider), una de ver proveedores (esto gracias a un for, cuenta con un CRUD al cual solo el staff puede acceder lo mismo para el aspecto distinto que tiene la pagina a la hora de verla como staff e imagenes ademas de un slider) y un prefil (en el cual puedes cambiar tu avatar y modificar tu informacion).

Como ejecutar el programa: 

(si no hay países cargar algunos países desde admin, hay que hacer lo mismo para sexos (agregar: hombre, mujer y prefiero no mencionarlo)) 

En register cargar alguna persona.

el login, logearte

Posteriormente en reservar hay que hacer una reserva, esta se subirá a la base de datos, y desde admin veremos una casilla que no está en la página (esta atendido?), esta es un buleano que podremos modificar para saber si ya está atendido, este lo podríamos modificar.

despues podriamos ir a nuestro perfil (el celeste con tu user y avatar predeterminado) y modificar nuestra informacion (en este caso hay que cambiar el username si o si) y/o cambiar nuestro avatar

y por ultimo podriamos ir y ver los proveedores y productos o buscar alguno gracias a la barra de navegacioon, y si somos del staff podriamos usar el CRUD

URLs: 

Home = http://127.0.0.1:8000 

Regístrate= http://127.0.0.1:8000/register/register/ 

Iniciar sesión = http://127.0.0.1:8000/register/login/ 

Reservas = http://127.0.0.1:8000/register/reservas/ 

Admin = http://127.0.0.1:8000/admin/    (Usuario: admin | Contraseña: 123)

productos= http://127.0.0.1:8000/productos/productos/

proveedores= http://127.0.0.1:8000/proveedores/proveedores/

about= http://127.0.0.1:8000/about/

perfil= http://127.0.0.1:8000/perfil/ (solo logeado)



 

Errores conocidos: 

resuelto:/  *En la página Regístrate (en el código) se utilizan demasiados “<br>” para lograr que quede bien la página.*

Los nombres de las apps no siguen las convenciones de django (no empiezan con mayúscula)

cuando se pone la pagina en modo celular en la pagina de proveedores se bugea haciendo que se vea raro, pero la informacion se ve

cuando modificamos nuestra informacion en perfil hay que cambiar si o si el username, porque si no dice que ya esta registrado


 

Cosas a mejorar: 
corregir algunos errores como el del prefil cuando modificamos la informacion


cosas a instalar en el entorno virtual:
django: comando (win10): pip install django
pillow: comando (win10): pip install pillow


anotaciones para el creador:
resuelto:/  *le falta corregir el bug de las imagenes en el CRUD de Productos*
resuelto:/  *(no es muy nesesario) le falta poner la variable cuerpo del slider.html el el html productos_show*
resuelto:/  *le falta poner las URLs del CRUD de productos en la APP de producto*
resuelto:/  *le falta hacer un buscador de elementos en el CRUD de productos*
resuelto:/  *le falta hacer el CRUD en el Perfil*
resuelto:/  *le falta agregar para que el usuario pueda elegir su foto de perfil (bugs si no tenes avatar anteriormente)*
resuelto:/  *le falta crear proveedores con su CRUD pertinente*
resuelto:/  *le falta agregar al formulario de "Registrate" los campos de apellido y nombre los cuales no deben ser opcionales y el email hay que hacerlo que no sea opcional*
