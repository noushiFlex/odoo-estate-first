#estate_property.py

from odoo import models, fields

class EstateProperty(models.Model):

    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(required=True)
    price = fields.Float(string="Price")
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    tag_ids = fields.Many2many('estate.property.tag', string="Tags")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    postcode = fields.Char()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled')
    ], required=True, default='new')
    best_price = fields.Float(compute="_compute_best_price")
    user_id = fields.Many2one(
        'res.users', 
        string='Salesperson', 
        default=lambda self: self.env.user,
        tracking=True
    )