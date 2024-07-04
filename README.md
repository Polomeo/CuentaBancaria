Gestor de Cuenta Bancaria programado para consola en Python
----------------------------------------------------

Esta aplicación es un ejercicio realizado para el curso "Python Total", dictado por el profesor Federico Garay en Udemy.

Los requerimientos del proyecto fueron los siguientes:

- El programa tiene en una clase "Persona", que tiene como atributos "nombre" y "apellido"
- Tiene también una clase "Cliente", que hereda de "Persona", y que agrega los atributos "numero de cuenta" y "balance"
- Además, la clase "Cliente" cuenta con métodos que permiten "depositar", "retirar" y ver el "balance" de la cuenta
- El programa debe permitir que el cliente elegir si hacer un depósito o retirar de la cuenta, y ver el balance de la misma
- Cuando el cliente desee, puede salir del programa. Mientras no lo haga, el programa sigue funcionando
- Al iniciar el programa, el sistema permite crear un nuevo cliente con una función llamada crear_cliente()
 
El proyecto tiene algunos agregados propios:
- Se utilizó un control "match" para administrar la opción elegida por el cliente.
- Se agregaron detalles a la interfaz gráfica, y algunas validaciones para verificar la entrada del cliente
