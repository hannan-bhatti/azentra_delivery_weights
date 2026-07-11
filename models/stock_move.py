from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move'

    # The custom gross weight field has been removed.
    az_net_weight = fields.Float(string="Net weight")