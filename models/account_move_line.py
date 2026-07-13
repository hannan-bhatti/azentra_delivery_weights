from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # Custom net weight field for invoice line items
    az_net_weight = fields.Float(string="Net weight")