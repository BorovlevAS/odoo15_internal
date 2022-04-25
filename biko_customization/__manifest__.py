{
    "name": "BIKO: customization",
    "summary": """
        1. В PIVOT добавил расчет % маржи (считает с ошибкой!!! нужно переделать на отчет)
        2. При клике раздела Sales автоматически открывается панель команд
        3. Добавил фильтр Мои и открытые
        4. При открытии списка автоматом открывается список, а не канбан
    """,
    "category": "",
    "version": "15.0.1.1.3",
    'author': 'BIKO Solutions',
    'company': 'BIKO Solutions',
    'maintainer': 'BIKO Solutions',
    "depends": ['base', 'crm', 'sale_management', 'sale_margin'],
    "data": [
        'views/res_partner_views.xml',
        'views/crm_lead_views.xml',
        'views/biko_custom_menus.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
