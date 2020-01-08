# -- coding: utf-8 --

from odoo import models, fields, api


class presupuesto(models.Model):
    _name = 'upogarden.presupuesto'
    
    _rec_name="id_presupuesto"
    id_presupuesto = fields.Char('ID', size=64, required=True)
    coste_Total = fields.Float('Coste total', required=True)
    descripcion = fields.Char('Descripcion', size=64, required=True)
    