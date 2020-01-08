# -*- coding: utf-8 -*-

from odoo import models, fields, api


class trabajador(models.Model):
    _name = 'upogarden.trabajador'
    
    _rec_name="nombre"
    id_trabajador = fields.Char('ID', size=64, required=True)
    nombre = fields.Char('Nombre', size=64, required=True)
    sueldo = fields.Fload('Sueldo',requiered=True)
    
    