from odoo import models, fields

class CustomSalesDashboard(models.Model):
    _name = "Pasteleria.dashboard"
 
    @api.one
    def _get_count(self):
        quotations_count = self.env['sale.order'].search(
            [('sate', '=', 'draft')])
        orders_count = self.env['sale.order'].search(
            [('sate', '=', 'sales_order')])
        orders_done_count = self.env['sale.order'].search(
            [('sate', '=', 'done')])
 
        self.orders_count = len(orders_count)
        self.quotations_count = len(quotations_count)
        self.orders_done_count = len(orders_done_count)
 
    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name")
    orders_count = fields.Integer(compute = '_get_count')
    quotations_count = fields.Integer(compute= '_get_count')
    orders_done_count = fields.Integer(compute= '_get_count')