# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstateProperty(models.Model):
	_name = "estate.property"
	_description = "Real Estate Property Data"
    
	name = fields.Char('Property Name',required=True)
	description = fields.Text('Property Description')
	postcode = fields.Char('Postal Code')
	date_availability = fields.Datetime('Available From',copy=False,default=lambda self: fields.Date.add(fields.Date.today(),months=3))
	expected_price = fields.Float('Expected Price',required=True)
	selling_price = fields.Float('Selling Price',readonly=True,copy=False)
	bedrooms = fields.Integer('Bedrooms',default=2)
	living_area = fields.Integer('Living Area (sqm)')
	facades = fields.Integer('Facades')
	garage = fields.Boolean('Garage')
	garden = fields.Boolean('Garden')
	garden_area = fields.Integer('Garden Area (sqm)')
	garden_orientation = fields.Selection(
    	string='Garden Orientation',
    	selection=[('north','North'),('south','South'),('east','East'),('west','West')],
    	help="Garden Orientation tells us where the garden faces.")
	active = fields.Boolean('Active', default=True)
	state = fields.Selection(
    	string='Status',
    	selection=[('new','New'),('offer received','Offer Received'),('offer accepted','Offer Accepted'),('sold','Sold'),('canceled','Canceled')],
    	help="Select the property's status.",
    	required=True,
    	copy=False,
    	default='new')
	property_type_id = fields.Many2one(
    	'estate.property.type',
    	string='Property Type',
    	required=True,
    	copy=False)
	buyer_id = fields.Many2one(
    	'res.partner',
    	string='Buyer',
    	required=True,
    	copy=False)
	seller_id = fields.Many2one(
    	'res.users',
    	string='Salesperson',
    	required=True,
    	default=lambda self: self.env.user)
	tag_ids = fields.Many2many(
    	'estate.property.tag',
    	string="Tags",
    	copy=False)
	offer_ids = fields.One2many(
		'estate.property.offer',
		'property_id',
		string="Offers",
		copy=False)