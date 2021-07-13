# Copyright 2021 Ecosoft
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Requests -> Purchase Request",
    "version": "14.0.1.0.0",
    "category": "Purchase Management",
    "website": "https://github.com/OCA/server-ux",
    "summary": """
        This module adds to the requests workflow the possibility to generate
        Purchase Request from an Requests of Purchase Request.
    """,
    "author": "Ecosoft, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["base_requests", "purchase_request"],
    "data": [
        "data/ir_actions_server.xml",
        "data/request_category_data.xml",
        "views/request_views.xml",
        "views/request_category_views.xml",
        "views/purchase_request_views.xml",
    ],
    "application": False,
    "installable": True,
}
