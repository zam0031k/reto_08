# Menú con Iterador de Pedidos

Este repositorio contiene la implementación de un sistema de menú del reto 3 al cual se le ha agregado una nueva clase `IterOrder` que permite iterar sobre los elementos de un pedido y mostrar cada uno de ellos junto con su cantidad y precio total.

## Estructura del Código

### Clases Implementadas

#### 1. `MenuItem`

Clase base para representar un ítem del menú.

**Atributos**: `name`, `price`

**Método**: `calculate_total(quantity=1)` para calcular el precio total según la cantidad.

#### 2. `Beverage`, `Appetizer`, `MainCourse`

Clases hijas de `MenuItem`, representan bebidas, aperitivos y platos principales respectivamente, agregando atributos adicionales específicos para cada tipo de ítem.

#### 3. `Order`

Clase que administra un pedido.

**Métodos**:

- `add_item(item, quantity=1)`: Agrega un ítem al pedido.

- `total_invoice()`: Calcula el total de la factura.

- `discount()`: Aplica un descuento dependiendo de la cantidad de ítems.

- `__str__()`: Devuelve un resumen del pedido con el total y el descuento aplicado.

#### 4. `IterOrder`

Clase implementada para permitir la iteración sobre los elementos de un pedido.

**Atributos**:

- `order`: Referencia al objeto Order.

- `index`: Índice actual de la iteración.

**Métodos**:

- `__iter__()`: Retorna el propio iterador.

- `__next__()`: Retorna el siguiente elemento en el pedido con su cantidad y precio total. Lanza una excepción StopIteration cuando se han recorrido todos los elementos.

## Implementación del Iterador

```python
class IterOrder:
    def __init__(self, order: Order):
        self.order = order
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.order.items):
            item, cant  = self.order.items[self.index]
            self.index += 1
            return f"{item.name} x {cant} = ${item.calculate_total(cant):.3f} COP"
        else:
            raise StopIteration
```
## Uso del Iterador en un Pedido

Para iterar sobre un pedido y mostrar los ítems con su cantidad y precio total, se usa la siguiente implementación:
```python
print("\nORDER 1:")
for item in IterOrder(order1):
    print(item)
  
print("\nORDER 2:")  
for item in IterOrder(order2):
    print(item)
   
print("\nORDER 3:")
for item in IterOrder(order3):
    print(item)
```
Cada iteración del bucle `for` llama al método `__next__()` de `IterOrder`, devolviendo un string con el nombre del producto, la cantidad y el precio total.

##  Salida: 
```
ORDER 1:
Coca Cola x 2 = $6.400 COP
French Fries x 1 = $4.300 COP
Hambuerger x 1 = $14.000 COP

ORDER 2:
Lemon Juice x 3 = $6.000 COP
Nachos x 2 = $10.000 COP
Pizza x 1 = $10.000 COP
Fruit Salad x 1 = $6.000 COP

ORDER 3:
Lemon Juice x 1 = $2.000 COP
Coca Cola x 3 = $9.600 COP
Sushi x 2 = $27.000 COP
Tacos x 3 = $33.900 COP
Fruit Salad x 1 = $6.000 COP
```
