# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class socio(models.Model):
    _name = 'library.socio'
    _description = 'library.socio'
    nombre_socio = fields.Char(string = "nombre_socio", required = True)        
    apellidos_socio = fields.Char(string ="apellidos_socio", required = True)
 
    fecha_nac = fields.Date()
    libros = fields.Many2many(
        comodel_name = 'library.libro',
        string='Libros'
    )