# -*- coding: utf-8 -*-

from odoo import models, fields, api


class perezapis_clientov(models.Model):
    _name = 'perezapis_clientov.perezapis_clientov'
    _description = 'perezapis_clientov.perezapis_clientov'

    name = fields.Char()
    Company = fields.Char()
    value = fields.Integer()
    value3 = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    description2 = fields.Char(compute="_value_pc2", store=True)


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    @api.onchange("value")
    def _onchange_partner_id(self):
        self.value3 = 1500


    # @api.depends('name', 'Company')
    # def _value_pc2(self):
    #     for refd in self:
    #         refd.description2 = refd.name + refd.Company

    def action_do_something(self):
        for record in self:
            record.description = record.Company + "__" + record.name

# class fdg(models.Model):
#     _name = 'fdg'



