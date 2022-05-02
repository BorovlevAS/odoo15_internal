# -*- coding: utf-8 -*-

from odoo import models, fields, api


class perezapis_clientov(models.Model):
    _inherit = 'res.partner'


    def action_do_something(self):
        for partner in self:
            partner.name = partner.name + "+"
            partner.name = ''.join(partner.name[0:-1])





