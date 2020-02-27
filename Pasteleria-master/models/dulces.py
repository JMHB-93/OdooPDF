from odoo import models, fields

class Dulces(models.Model):
    _name = 'Pasteleria.dulces'
    codigo = fields.Integer('Codigo', required=True)
    nombre = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio', required=True)
    temporada = fields.Char('Temporada', required=False)
    precio = fields.Integer()
    cantidadDulces = fields.Integer('Cantidad de Dulces', required=True)
    resultado = fields.Integer()
    multiplicar = fields.Integer(compute='multiplicar')
    

    def name_get(self):
        res = []
        for record in self:
            name = record.cod
            res.append((record.id, name))
        return res

    def suma(self):
        self.resultado = self.cantidadDulces * self.precio

   
