# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alquiler(models.Model):
    _name = 'upogarden.alquiler'
    
    _rec_name="id_alquiler"
    id_alquiler = fields.Char('ID', size=64, required=True)
    fecha_Inicio = fields.Datetime('Desde',required=True,autodate = True)
    fecha_Fin = fields.Datetime('Hasta',required=True, autodate = True)
    tiempo_Total = fields.Float('Tiempo total',required=True)
    productos_ids = fields.Many2many('upogarden.producto',string="Productos")
    cliente_id = fields.Many2one("upogarden.cliente","Cliente")
    #tiempo_Total = fecha_Fin - fecha_Inicio
    #poner el tiempo_Total automatico