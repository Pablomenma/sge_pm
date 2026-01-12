# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class autor(models.Model):
    _name = 'library.autor'
    _description = 'library.autor'
    nombre_autor = fields.Char()        
    apellidos_autor = fields.Char()
 
    fecha_nac = fields.Date()
 
 
    pais = fields.Char()
 