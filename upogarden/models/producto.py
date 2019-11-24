# -*- coding: utf-8 -*-

from odoo import models, fields, api


class producto(models.Model):
    _name = 'upogarden.producto'
    
    id_producto = fields.Char('ID', size=64, required=True)
    nombre = fields.Char('Nombre', size=64, required=True)
    descripcion = fields.Char('Descripcion', size=64, required=True)
    precio_Hora = fields.Float('Precio por hora',required=True)
    alquiler_id = fields.Many2one('upogarden.alquiler','Alquiler')
    