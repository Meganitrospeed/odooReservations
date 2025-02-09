from odoo import models, fields, api


class AppointmentManager(models.Model):
    _name = 'appointment.manager'
    _description = 'Appointment Manager'

    name = fields.Char('Appointment Name')
    date = fields.Datetime('Appointment Date')
    # Additional fields
    customer = fields.Many2one('res.partner', string="Cliente", required=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmada'),
        ('cancelled', 'Cancelada'),
    ], string="Estado", default='draft')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'cancelled'
