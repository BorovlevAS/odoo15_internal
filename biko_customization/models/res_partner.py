from odoo import api, models

class Partner(models.Model):
    _inherit = 'res.partner'

    def _get_contact_name(self, partner, name):
        company_name = partner.commercial_company_name or partner.sudo().parent_id.name
        return "%s, %s" % (name, company_name)