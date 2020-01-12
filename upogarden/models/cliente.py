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
    
    state = fields.Selection([('solicitante','Solicitante'),
                              ('admitido','Admitido'),],
                              'Estado',
                              default='solicitante')
    @api.one
    def btn_submit_to_admitido(self):
        self.write({'state':'admitido'})
        
    @api.onchange('alquileres_ids','contrataciones_ids')
    def onchange_gymclass(self):
        if self.state != 'admitido':
            raise models.ValidationError('El cliente debe estar admitido para asignarle alquileres y contrataciones.')
        
    _sql_constraints = [
        ('id_cliente', 'UNIQUE (id_cliente)',  'No se pueden crear dos clientes con el mismo DNI.')
    ]