from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    user_default_rights = fields.Boolean(
        "Default Access Rights", config_parameter='base_setup.default_user_rights')
    allowed_discount_account = fields.Many2one(
        'account.account', required=True, config_parameter='allowed_discount.allowed_discount_account')
    allowed_discount_product = fields.Many2one(
        'product.product', required=True, config_parameter='allowed_discount.allowed_discount_product')
