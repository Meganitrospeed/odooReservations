{
    'name': 'Appointment Manager',
    'version': '1.1',
    'summary': 'Módulo para gestionar citas o reservas',
    'author': 'Juan Thielmann',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/appointment_views.xml',
        'views/appointment_calendar_view.xml',
    ],
    'installable': True,
    'application': True,
}
