# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gestion_sala(models.Model):
    _name = 'gestion_sala.gestion_sala'
    _description = 'gestion_sala.gestion_sala'

    # Nombre de la Sala, de tipo texto.
    nombre_sala = fields.Char()

    # Capacidad, de tipo entero.
    capacidad = fields.Integer()
    # Fecha de Reserva, de tipo fecha.
    fecha_reserva = fields.Date()

    # Reservada, de tipo booleano,indicará si está disponible o no.
    reservada = fields.Boolean()

    # Comentarios de tipo texto.
    comentarios = fields.Char()