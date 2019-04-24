Como esta estructurada la aplicación
====================================

Los proyectos hechos en djangos consisten en dividir tus aplicaciones en
“apps”. Las apps son solamente carpetas dentro de tu proyecto que pueden
ser reusable en otras aplicaciones.

.. tip:: Puedes pensar en apps analogo a lo que es componentes en react.

Cada aplicación contiene distintos archivos que hacen funcionar una
parte de todo tu proyecto. Los archivos mas comunes que contiene son:

1. Views.py -
2. models.py
3. apps.py
4. admin.py

Cada aplicación tambien puede contener otras carpetas adentros como:

1. static

   1. Css
   2. Javascript
   3. A veces va a contener img

2. Templates
3. Migrations

Cada carpeta dentro del proyecto es bien repetitivo todas van a tener un
nimbre diferente que va a ser referente a una parte importante del
sistema. Dentro de cada carpeta siempre va a contener **minimo** los
cuatros archivos que mencione arriba.

.. nota:: Puede echarle un vistazo **solamente** a la tabla de contenido de la pagina de  :doc:`index-modules` y va entender lo que digo