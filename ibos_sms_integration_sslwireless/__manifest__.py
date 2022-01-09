{
    "name": "SSL Wireless SMS Integration",
    "summary": """ SSL Wireless SMS Integration """,
    "category": "Tools",
    "images": [],
    "version": "13.0.1.0.0",
    "application": False,
    "author": "iBOS, Kamrul",
    "support": "info@ibos.io",
    "website": "https://ibos.io",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["base", "web", "point_of_sale",],
    "data": [
        'views/assets.xml',
        'security/ir.model.access.csv',
        'views/sms_notification.xml',
    ],
    "qweb": [
    ],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}
