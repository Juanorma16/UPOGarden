# -*- coding: utf-8 -*-

from odoo import models, fields, api


class proveedor(models.Model):
    _name = 'upogarden.proveedor'
    
    _rec_name="nombre"
    id_proveedor = fields.Char('ID', size=64, required=True)
    nombre = fields.Char('Nombre', size=64, required=True)
    localizacion = fields.Char('Localizacion', size=64, required=True)
    productos_ids = fields.One2many("upogarden.producto","proveedor_id","Productos")