Qué se quiere:
- Un pool de hebras receptoras de peticiones REST (depende del servidor REST)
- Esas hebras atienden peticiones, validan el esquema y las meten en una cola para ser atendidas por un worker
- Hay un pool de workers que leen de la cola
- Cada worker lee una peticion de la cola y la atiende.
- Cualquier acceso a una estructura o variable común o una BD debe garantizarse que es transaccional (puede que se necesiten locks).
- En caso de caida de una hebra (receptoras o workers), debe seguirse algún criterio:
   - Salir matando todas las hebras y el programa principal
   - Reiniciar la hebra que murió 

Sin duda, mp1-mpqueue.py es util pues enseña como usar una cola del modulo multiprocessing. La cola es reentrante.


