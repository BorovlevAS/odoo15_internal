from odoo import models, fields

class obrabotka(models.TransientModel):
    _name = 'perezapis_clientov.obrabotka'

    hai = fields.Char()