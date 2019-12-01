# -*- coding: utf-8 -*-

from odoo import models, fields, api


class entrega(models.Model):
    _name = 'upogarden.entrega'
    
    _rec_name="id_entrega"
    id_entrega = fields.Char('ID', size=64, required=True)
    lugar_Entrega = fields.Char('Lugar', size=64, required=True)
    fecha_Entrega = fields.Datetime('Fecha',required=True, autodate = True)
    alquiler_id = fields.Many2one("upogarden.alquiler","Alquiler")