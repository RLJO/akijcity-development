from odoo import fields, models, api

class SmsHistory(models.Model):
    _name = 'sms.notification.history'
    _order = "id desc"

    message = fields.Char(string="Message")
    mobile = fields.Char(string="Mobile Number")
    status = fields.Char(string="Status")
    reference_id = fields.Char(string="Reference")
    error_msg = fields.Text(string="Error Message")
    response = fields.Text(string="Response Message")



