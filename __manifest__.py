{
    'name': 'Appointment Manager',
    'version': '1.0',
    'summary': 'Módulo para gestionar citas o reservas',
    'author': 'Tu Nombre',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/appointment_views.xml',
    ],
    'installable': True,
    'application': True,
}
