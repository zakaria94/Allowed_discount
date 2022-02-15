from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    total_discount = fields.Float(compute='_compute_discount_total', string="Total Discount", default=0)

    @api.depends('order_line.discount')
    def _compute_discount_total(self):
        count = 0
        for line in self.order_line:
            if line.discount:
                count += (line.discount / 100) * line.price_unit
        self.total_discount = count

    def _add_supplier_to_product(self):
        """Insert a mapping of products to PO lines to be picked up
        in supplierinfo's create()"""
        self.ensure_one()
        po_line_map = {
            line.product_id.product_tmpl_id.id: line for line in self.order_line
        }
        return super(PurchaseOrder, self.with_context(po_line_map=po_line_map))._add_supplier_to_product()