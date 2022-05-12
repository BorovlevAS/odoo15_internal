from odoo import models, fields
import base64
import json

class ImportRecs(models.TransientModel):
    _name = 'biko.import.recs'

    file = fields.Binary(string='File name')
    file_name = fields.Char()

    def action_import_records(self):
        data = base64.b64decode(self.file)
        data = data.decode('windows-1251')
        jsdata = json.loads(data)

        env_deals = self.env['crm.lead'].env

        for deal in jsdata.values():

            comments_list = deal['comments']
            # self.env.ref
            if not comments_list:
                continue

            external_id = deal['external_id']
            id = deal['id']

            # env_deals.search()
