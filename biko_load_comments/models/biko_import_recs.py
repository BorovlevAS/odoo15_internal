from odoo import models, fields
import base64
import json
from datetime import datetime
import requests

class ImportRecs(models.TransientModel):
    _name = 'biko.import.recs'

    file = fields.Binary(string='File name')
    file_name = fields.Char()

    def action_import_records(self):
        data = base64.b64decode(self.file)
        data = data.decode('windows-1251')
        jsdata = json.loads(data)

        env_deals = self.env['crm.lead'].env
        i = 0

        for deal in jsdata.values():
            if i >= 3: break

            comments_list = deal['comments']
            # self.env.ref
            if not comments_list:
                continue

            external_id = deal['external_id']
            id = deal['id']

            record = env_deals.ref('__import__.' + external_id)

            if record:
                for comment in comments_list.values():
                    date_time = datetime.fromisoformat(comment['CREATED']).replace(tzinfo=None)
                    msg = comment['COMMENT']
                    f_attachments = []
                    # TODO: заполнить тут прикрепленные файлы и передать их в функцию
                    if ('FILES' in comment.keys()):
                        i += 1
                        for c_file in comment['FILES'].values():
                            f_name = c_file['name']
                            req = requests.get(c_file['urlDownload'])
                            f_attachments.append((f_name, req.content))
                        message_rec = record.message_post(body=msg, message_type='comment', attachments=f_attachments)
                        message_rec['date'] = date_time
