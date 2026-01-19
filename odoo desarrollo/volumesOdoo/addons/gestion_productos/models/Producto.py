# -*- coding: utf-8 -*-

from odoo import models, fields, api
 

 
class producto(models.Model):
    _name = 'gestion_productos.producto'
    _description = 'gestion_productos.producto'
 
    nombre_prod = fields.Char()
 
 
 
    descripcion_prod = fields.Char()
 
    cod_prod = fields.Char()

    categoria = fields.Char()
    ()

    imagen = fields.Char()

    activo = fields.Boolean()

    peso = fields.Integer()

    precio = fields.Integer()