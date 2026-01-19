# -*- coding: utf-8 -*-
# from odoo import http


# class GestionSala(http.Controller):
#     @http.route('/gestion_sala/gestion_sala', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_sala/gestion_sala/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_sala.listing', {
#             'root': '/gestion_sala/gestion_sala',
#             'objects': http.request.env['gestion_sala.gestion_sala'].search([]),
#         })

#     @http.route('/gestion_sala/gestion_sala/objects/<model("gestion_sala.gestion_sala"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_sala.object', {
#             'object': obj
#         })
