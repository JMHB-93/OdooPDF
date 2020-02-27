from odoo import models, fields

class Embasados(models.Model):
    _name = 'Pasteleria.embasados'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    marca = fields.Char('Marca', required=True)
    precio = fields.Float('Precio', required=True)
