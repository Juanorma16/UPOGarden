# -*- coding: utf-8 -*-
from odoo import http

# class Upogarden(http.Controller):
#     @http.route('/upogarden/upogarden/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upogarden/upogarden/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upogarden.listing', {
#             'root': '/upogarden/upogarden',
#             'objects': http.request.env['upogarden.upogarden'].search([]),
#         })

#     @http.route('/upogarden/upogarden/objects/<model("upogarden.upogarden"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upogarden.object', {
#             'object': obj
#         })