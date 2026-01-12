# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class libro(models.Model):
    #nombre modulo nombre modelo
    _name = 'library.libro'
    _description = 'library.libro'
 

# Nombre
# Autor, nuevamente, este campo debería estar relacionado con el tro modelo. Por ahora lo dejaremos de tipo char
# Fecha de publicación
# ISBN
# Sinopsis
    nombre_libro = fields.Char()
 
 
    autor = fields.Char()
 
    fecha_public = fields.Date()
 
    isbn = fields.Char()

    sinopsis = fields.Char()