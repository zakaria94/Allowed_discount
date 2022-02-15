from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.model
    # def create(self, vals):
    #     res = super(SaleOrder, self).create(vals)
    #     self.env['sale.order.line'].create(
    #         {
    #             'order_id': res.id,
    #             'product_uom_qty': 1,
    #             'price_unit': res.partner_id.allowed_discount * -1,
    #             'product_account': res.env['ir.config_parameter'].sudo().get_param(
    #                      'allowed_discount_account') or False,
    #             'product_id': res.env['ir.config_parameter'].sudo().get_param('allowed_discount_product') or False,
    #             'name': " "
    #         })
    #     return res

    @api.onchange("partner_id")
    def onchanges_customer_id(self):
        for rec in self:
            lines = [(5, 0, 0)]
            account_id = self.env['res.config.settings'].search([]).allowed_discount_account.id
            product_id = self.env['res.config.settings'].search([]).allowed_discount_product.id
            for line in rec.partner_id.purchase_line_ids:
                if rec.partner_id.allowed_discount > 0:
                    vals = {
                        'product_id': line.id,
                        'product_uom_qty': 1,
                        'price_unit': line.partner_id.allowed_discount * -1,
                        'product_account': account_id,
                        'discount_product': product_id
                    }
                    lines.append((0, 0, vals))
            # print("lines", lines)
            rec.order_line = lines
