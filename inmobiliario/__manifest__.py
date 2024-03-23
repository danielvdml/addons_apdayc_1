{
    "name": """Inmobiliario""",
    "summary": """
Este módulo permite la gestión de ventas,compra y alquiler de inmuebles""",
    "author": "Daniel Moreno <daniel@codlan.com>",
    "category": "sales",
    "version":"17.0.2.0",
    "depends":[
        "base",
        "mail"
    ],
    "data":[
        "security/ir_model_access.xml",
        "data/inmuebles.xml",
        "views/view_inmuebles.xml",
        "views/wizard_inmuebles.xml",
        "reports/paperformat.xml",
        "reports/report_inmobiliario.xml"
    ],
    "assets":{
        "web.report_assets_common":[
            "inmobiliario/static/src/scss/reporte_style.scss"
        ]
    }
}