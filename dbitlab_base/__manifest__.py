{
    'name': "DB IT Lab Base",
    'version': '17.1',
    'summary': """""",
    'category': "",
    'author': "",
    'depends': ['stock', 'product','contacts', 'sale'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'data/res_partner_category_data.xml',
        'views/product_view.xml',
        'views/prodcuct_group_view.xml',
        'views/product_brand.view.xml',
        'views/route_customer_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}

