from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_account = fields.Many2one('account.account')
    discount_product = fields.Many2one('product.product')


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_account = fields.Many2one('account.account')
    discount_product = fields.Many2one('product.product')
