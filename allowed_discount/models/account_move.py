from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = "account.move"

    discount = fields.Float(string="Discount")
