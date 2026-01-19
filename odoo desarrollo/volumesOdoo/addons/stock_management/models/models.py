# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class producto(models.Model):
#     _name = 'stock_management.producto'
#     _description = 'stock_management.producto'

#     name = fields.Char(string ="nombre_producto", required = True, )
# category: categoría del producto, será un Selection
from dataclasses import fields


category = fields.Selection([
        ('tablets', 'tablets'),
        ('Ordenadores_portatiles', 'portatiles'),
        ('auriculares', 'auriculares'),
    ], string='Categoría', required=True) 
# price: precio unitario del producto
price = .fields.Float(string='Precio unitario')
# quantity: cantidad en stock
cuantity =  fields.Float(string='Cantidad en stock')
    

# total_value: campo calculado con el valor total del stock (precio por la cantidad total)
total_value = fields.Float(
        string='Valor total', 
        compute='_compute_total_value', 
        store=True)

# minimum_quantity: valor entero
# stock_status: campo calculado de tipo Selection. Podrá ser normal si la cantidad es superior a la cantidad mímina y Low Stock si es inferior.
# full_name: el nombre completo será un campo calculado que generará a partir del nombre y de la categoría. Por ejemplo: Ryzen 7 5800X (Microprocesadores)
full_name = fields.Char(string='Nombre Completo', compute='_compute_full_name')
