from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    allowed_discount = fields.Float(string="Allowed Discount (%)", digits="Discount",
                                    help="This value will be used as the default one, for each new")


class StockMove(models.Model):
    _inherit = "stock.move"

    def _get_price_unit(self):
        price_unit = False
        po_line = self.purchase_line_id
        if po_line and self.product_id == po_line.product_id:
            price = po_line._get_discounted_price_unit()
            if price != po_line.price_unit:
                # Only change value if it's different
                price_unit = po_line.price_unit
                po_line.price_unit = price
        res = super()._get_price_unit()
        if price_unit:
            po_line.price_unit = price_unit
        return res


class ProductSupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    discount = fields.Float(string="Discount (%)", digits="Discount")

    @api.onchange("name")
    def onchange_name(self):
        """ Apply the default supplier discount of the selected supplier """
        for supplierinfo in self.filtered("name"):
            supplierinfo.discount = supplierinfo.discount

    @api.model
    def _get_po_to_supplierinfo_synced_fields(self):
        """Overwrite this method for adding other fields to be synchronized
        with product.supplierinfo.
        """
        return ["discount"]

    @api.model_create_multi
    def create(self, vals_list):
        """Insert discount (or others) from context from purchase.order's
        _add_supplier_to_product method"""
        for vals in vals_list:
            product_tmpl_id = vals["product_tmpl_id"]
            po_line_map = self.env.context.get("po_line_map", {})
            if product_tmpl_id in po_line_map:
                po_line = po_line_map[product_tmpl_id]
                for field in self._get_po_to_supplierinfo_synced_fields():
                    if not vals.get(field):
                        vals[field] = po_line[field]
        return super().create(vals_list)
