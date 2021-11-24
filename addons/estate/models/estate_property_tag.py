# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.tag"
    _description = "Real Estate Property Tags"
    
    name = fields.Char('Property Tag',required=True)
    active = fields.Boolean('Active',default=True)
