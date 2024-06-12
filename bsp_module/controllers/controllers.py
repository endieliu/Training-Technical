# -*- coding: utf-8 -*-
# from odoo import http


# class BspModule(http.Controller):
#     @http.route('/bsp_module/bsp_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bsp_module/bsp_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bsp_module.listing', {
#             'root': '/bsp_module/bsp_module',
#             'objects': http.request.env['bsp_module.bsp_module'].search([]),
#         })

#     @http.route('/bsp_module/bsp_module/objects/<model("bsp_module.bsp_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bsp_module.object', {
#             'object': obj
#         })

