# -*- coding: utf-8 -*-

from odoo import models, fields, api


class alquiler(models.Model):
    _name = 'upogarden.alquiler'
    
    id_alquiler = fields.Char('ID', size=64, required=True)
    fecha_Inicio = fields.Datetime('Desde',required=True,autodate = True)
    fecha_Fin = fields.Datetime('Hasta',required=True, autodate = True)
    tiempo_Total = fields.Float('Tiempo total',required=True)
    productos_ids = fields.One2many('upogarden.producto','alquiler_id', 'Productos')
    #tiempo_Total = fecha_Fin - fecha_Inicio
    #poner el tiempo_Total automatico