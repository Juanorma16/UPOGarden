# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cliente(models.Model):
    _name = 'upogarden.cliente'
    
    id_cliente = fields.Char('DNI', size=64, required=True)
    nombre = fields.Char('Nombre', size=64, required=True)
    apellidos = fields.Char('Apellidos', size=64, required=True)
