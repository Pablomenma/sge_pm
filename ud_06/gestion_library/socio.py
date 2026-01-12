# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class socio(models.Model):
    _name = 'library.socio'
    _description = 'library.socio'
    nombre_socio = fields.Char()        
    apellidos_socio = fields.Char()
 
    fecha_nac = fields.Date()
 
 
    email = fields.Char()
 
    telefono = fields.Char()