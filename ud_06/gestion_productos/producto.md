# Sistemas de gestión empresarial.

## practica 601 creación del modelo productos en gestion_productos.

el modelo de producto es el siguiente:

```python
# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class productos(models.Model):
#     _name = 'gestion_productos.producto'
#     _description = 'gestion_productos.producto'     
#nombre del producto
# nombre_prod = fields.Char()
#descripcion
descripcion_producto = fields.Char()

# Código de producto, este campo debe ser obligatorio
Cod_producto = fields.Char()

# Imagen del producto
imagen = fields.Binary

# Categoría: el usuario podrá escoger entre Jardín, Hogar y Electrodomésticos
categoria = fields.Selection([
    ('jardin', 'jardin'),
    ('hogar', 'hogar'),
    ('electrodomesticos', 'electrodomesticos')
], string='categoria del producto') 

# Tipo de producto: indica si es un producto destacable o no.
destacable = fields.Boolean()


# Precio de venta
precio = fields.Integer()
# Stock disponible: la cantidad de unidades disponible
stock_disponible = fields.Integer()

# Fecha de creación, será la fecha actual
fecha_creacion = fields.Date.context_today

# Fecha de última actualización
fecha_actualizacion = fields.Date()

# Activo, indica si el producto está disponible o no, su valor por defecto será True
activo = fields.Boolean()
# peso de tipo decimal.
peso = fields.Float(string='Peso en kg', digits=(5, 2))
```