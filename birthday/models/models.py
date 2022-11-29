from odoo import models, fields, api


class employee_department(models.Model):
    _inherit = 'hr.employee'
    birthday = fields.Date('Date of birth')
   
