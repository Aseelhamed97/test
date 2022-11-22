# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeDepartment(http.Controller):
#     @http.route('/employee_department/employee_department', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_department/employee_department/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_department.listing', {
#             'root': '/employee_department/employee_department',
#             'objects': http.request.env['employee_department.employee_department'].search([]),
#         })

#     @http.route('/employee_department/employee_department/objects/<model("employee_department.employee_department"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_department.object', {
#             'object': obj
#         })
