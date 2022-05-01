{
    "name": "BIKO: Hide pager",
    "summary": """
        A module that lets the user hide pager 
        """,
    "author": "BIKO Solutions",
    "website": "",
    "category": "web",
    "version": "15.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["web"],

    'assets': {
        'web.assets_qweb': ['biko_hide_pager/static/src/**/*.xml'],
        'web.assets_backend': [
            'biko_hide_pager/static/src/js/hide_panel_toggle.js',
        ],
    },
    "installable": True,
}