from odoo import models, fields # type: ignore

class StockMove(models.Model):
    _inherit = 'stock.move'

    az_gross_weight = fields.Float(string="G.W")
    az_net_weight = fields.Float(string="N.W")