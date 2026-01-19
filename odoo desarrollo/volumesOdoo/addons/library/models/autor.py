# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class autor(models.Model):
    _name = 'library.autor'
    _description = 'library.autor'
    nombre_autor = fields.Char(string = "nombre", required = True)        
    apellidos_autor = fields.Char(string = "apellidos", required = True)
 
    fecha_nac = fields.Date()
 
 
    pais = fields.Many2one(
        comodel_name="res.country",
        string="País de origen",
        ondelete="set null",
    )
    libros = fields.Many2one(string ="libros")
    