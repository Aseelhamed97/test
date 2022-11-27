from odoo import models, fields, api


class employee_department(models.Model):
    _inherit = 'res.partner'
    birthday = fields.Datetime('Date of birth')
   
