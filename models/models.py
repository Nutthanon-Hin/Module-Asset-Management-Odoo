# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HinAsset(models.Model):
    _name = "hin.asset.asset"

    name = fields.Char("Asset Name", required=True)
    tag = fields.Char("Asset Tag", required=True)
    serial = fields.Char("Serial No.", required=True)
    status = fields.Many2one("hin.asset.status", "Status Description", required=True)
    registration_date = fields.Date("Registration", required=True)
    cost = fields.Float("Cost")
    category = fields.Many2one("hin.asset.category", "Category Description", required=True)
    location = fields.Many2one("hin.asset.location", "Location Description", required=True)
    brand = fields.Char("Brand", required=True)
    owner = fields.Many2one("hr.employee", "Owner", required=True)
    remark = fields.Char("Remark")
    
class HinStatus(models.Model):
    _name = "hin.asset.status"
    
#   status_id = fields.Integer("Status Id")
    name = fields.Char("Status Description")
    status_is_available = fields.Boolean()
    
class HinCategory(models.Model):
    _name = "hin.asset.category"
    
#    category_id = fields.Integer("Category_id")
    name = fields.Char("Category Description")
    category_is_active = fields.Boolean()
    
class HinLocation(models.Model):
    _name = "hin.asset.location"
    
#    location_id = fields.Integer("")
    name = fields.Char("Location Description")
    location_is_active = fields.Boolean()
    

    
    
    
    