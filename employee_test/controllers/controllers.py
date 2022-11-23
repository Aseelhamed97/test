# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeTest(http.Controller):
#     @http.route('/employee_test/employee_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_test/employee_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_test.listing', {
#             'root': '/employee_test/employee_test',
#             'objects': http.request.env['employee_test.employee_test'].search([]),
#         })

#     @http.route('/employee_test/employee_test/objects/<model("employee_test.employee_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_test.object', {
#             'object': obj
#         })
