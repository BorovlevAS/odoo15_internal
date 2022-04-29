from odoo import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    margin_percent = fields.Float('Margin (%)')

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['margin_percent'] = ", SUM(l.margin_percent * 100) AS margin_percent"
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)


    # dssdffsdf