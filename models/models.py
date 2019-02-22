# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools
import datetime

class HinAsset(models.Model):
    _name = "hin.asset.asset"

    name = fields.Char("Asset Name", required=True)
    tag = fields.Char("Asset Tag", required=True)
    serial = fields.Char("Serial No.", required=True)
    status = fields.Many2one("hin.asset.status", "Status Description", required=True, default=1)
    registration_date = fields.Date("Registration", required=True)
    check_history = fields.Many2one("hin.asset.hincheckasset", "Check History" )
    is_created = fields.Boolean('Created', copy=False)
    cost = fields.Float("Cost")
    category = fields.Many2one( "hin.asset.category", "Category Description", required=True)
    location = fields.Many2one("hin.asset.location", "Location Description", required=True)
    brand = fields.Char("Brand", required=True)
    owner = fields.Many2one("hr.employee", "Owner", required=True)
    remark = fields.Char("Remark")  
    image = fields.Binary("Photo", attachment=True)
    image_small = fields.Binary("Photo Small", attachment=True)
    image_medium = fields.Binary("Photo Medium", attachment=True)
    life_time_year = fields.Integer("Year")
    current_value = fields.Float(compute="_depreciationhin", digits=(20, 2))
    descript = fields.One2many("hin.asset.maintenance", "name")
    
    _sql_constraints = [
        ("name_uniq", "unique (name)", "Name must be uinque"),
        ("tag_uniq", "unique (tag)", "Tag must be uinque"),

    ]
    

    @api.depends("registration_date", "cost", "life_time_year")
    def _depreciationhin(self):
        current_date = datetime.date.today()
        current_date2 = datetime.datetime.strptime(str(current_date), "%Y-%m-%d")
        
        #reg_date = datetime.strftime(str(a.registration_date),"%Y-%m-%d")
        for a in self:
            if a.registration_date is not False and a.life_time_year is not 0: 
                reg = datetime.datetime.strptime(str(a.registration_date), "%Y-%m-%d")
                dif = abs((current_date2 - reg).days)
                a.current_value = (1-(dif / (a.life_time_year * 365))) * a.cost
            else:
                a.current_value = None
    
    
    

            
    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        vals.update({'is_created':True})
        lot = super(HinAsset, self).create(vals)
        return lot
        
    @api.multi
    def write(self, vals):
        tools.image_resize_images(vals)
        lot = super(HinAsset, self).write(vals)
        return lot       
    
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

    
class HinCheckAsset(models.Model):
    _name = "hin.asset.hincheckasset"
    
    name = fields.Date("Check Date")
    tag = fields.Many2one("hin.asset.asset", "tag")
    
class HinMaintenance(models.Model):
    _name ="hin.asset.maintenance"
    
    name = fields.Many2one("hin.asset.asset", index=True)
    descript = fields.Char("Maintenance Description")
    scheduled_date = fields.Date("Scheduled Date")
    quantity = fields.Float("Quantity")
    price = fields.Float("Price")
    subtotal = fields.Float("Subtotal")