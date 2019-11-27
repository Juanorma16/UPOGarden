# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    _name = 'upogarden.cliente'
    
    _rec_name="nombre"
    id_cliente = fields.Char('DNI', size=64, required=True)
    nombre = fields.Char('Nombre', size=64, required=True)
    apellidos = fields.Char('Apellidos', size=64, required=True)
    alquileres_ids = fields.One2many("upogarden.alquiler","cliente_id","Alquileres")
    contrataciones_ids = fields.One2many("upogarden.contratacion","cliente_id","Contrataciones")
