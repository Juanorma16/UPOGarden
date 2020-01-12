# -*- coding: utf-8 -*-

from odoo import models, fields, api


class producto(models.Model):
    _name = 'upogarden.producto'
    
    _rec_name="nombre"
    id_producto = fields.Char('ID', size=64, required=True)
    nombre = fields.Char('Nombre', size=64, required=True)
    foto = fields.Binary('Photo')
    descripcion = fields.Char('Descripcion', size=64, required=True)
    precio_Hora = fields.Float('Precio por hora',required=True)
    alquiler_ids = fields.Many2many('upogarden.alquiler',string="Alquileres")
    proveedor_id = fields.Many2one("upogarden.proveedor","Proveedor")
    
    _sql_constraints = [
        ('id_producto', 'UNIQUE (id_producto)',  'No se pueden crear dos productos con el mismo id.')
    ]