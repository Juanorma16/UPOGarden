# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime as dt

class alquiler(models.Model):
    _name = 'upogarden.alquiler'
    
    _rec_name="id_alquiler"
    id_alquiler = fields.Char('ID', size=64, required=True)
    fecha_Inicio = fields.Date('Desde',required=True,autodate = True)
    fecha_Fin = fields.Date('Hasta',required=True, autodate = True)
    productos_ids = fields.Many2many('upogarden.producto',string="Productos")
    cliente_id = fields.Many2one("upogarden.cliente","Cliente")
    entrega_id = fields.Many2one("upogarden.entrega","Entrega")
    tiempo_Total = fields.Float('Tiempo total', compute="calcula_tiempo_total", store=True)
    
    @api.depends('fecha_Inicio','fecha_Fin')
    def calcula_tiempo_total(self):
        self.tiempo_Total = (dt.strptime(self.fecha_Fin,'%Y-%m-%d') - dt.strptime(self.fecha_Inicio,'%Y-%m-%d')).days
        
    _sql_constraints = [
        ('id_alquiler', 'UNIQUE (id_alquiler)',  'No se pueden crear dos alquileres con el mismo id.')
    ]