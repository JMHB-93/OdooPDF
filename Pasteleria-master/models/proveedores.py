from odoo import models, fields

class Proveedores(models.Model):
    _name = 'Pasteleria.proveedores'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    nombreRep = fields.Char('Nombre Representante', required=True)
    telefono = fields.Char('Telefono', required=True)
    diasVisita = fields.Char('Dias que Visita', required=False)

    def name_get(self):
        res=[]
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
