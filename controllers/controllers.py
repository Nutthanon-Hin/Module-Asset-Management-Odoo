# -*- coding: utf-8 -*-
from odoo import http

# class HinAsset(http.Controller):
#     @http.route('/hin_asset/hin_asset/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hin_asset/hin_asset/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hin_asset.listing', {
#             'root': '/hin_asset/hin_asset',
#             'objects': http.request.env['hin_asset.hin_asset'].search([]),
#         })

#     @http.route('/hin_asset/hin_asset/objects/<model("hin_asset.hin_asset"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hin_asset.object', {
#             'object': obj
#         })