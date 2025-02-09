from odoo import models, fields, api

class Appointment(models.Model):
    _name = 'appointment.manager'
    _description = 'Gestión de Citas'

    name = fields.Char(string="Título", required=True)
    date = fields.Datetime(string="Fecha y Hora", required=True)
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
