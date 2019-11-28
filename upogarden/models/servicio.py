# -*- coding: utf-8 -*-

from odoo import models, fields, api


class servicio(models.Model):
    _name = 'upogarden.servicio'
    
    _rec_name="nombre"
    id_servicio = fields.Char('ID', size=64, required=True)
    nombre = fields.Char('Nombre', size=64, required=True)
    descripcion = fields.Char('Descripcion', size=64, required=True)
    precio_Hora = fields.Float('Precio por hora',required=True)
    contrataciones_ids = fields.Many2many('upogarden.contratacion',string="Contrataciones")