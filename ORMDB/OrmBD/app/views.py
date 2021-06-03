from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from .models import *

from . import appbuilder, db


class LeadView(ModelView):
    datamodel = SQLAInterface(Lead)
    list_label = {'cust_rel': 'клиент'}
    list_columns = ['id', 'personid', 'date', 'price', 'goodid', 'cust_rel', 'good_rel']


class GoodView(ModelView):
    datamodel = SQLAInterface(Good)
    list_columns = ['id', 'name', 'size']


class CustomerView(ModelView):
    datamodel = SQLAInterface(Customer)
    list_columns = ['id', 'name', 'phone', 'index']


class WarehouseView(ModelView):
    datamodel = SQLAInterface(Warehouse)
    list_columns = ['id', 'goodid', 'admission_date', 'cost']


appbuilder.add_view(
    LeadView,
    "Leads",
    icon="fa-folder-open-o",
    category="Товарка1",
    category_icon="fa-envelope"
)
appbuilder.add_view(
    GoodView,
    "Goods",
    icon="fa-folder-open-o",
    category="Товарка1",
    category_icon="fa-envelope"
)
appbuilder.add_view(
    WarehouseView,
    "Sklad",
    icon="fa-folder-open-o",
    category="Товарка1",
    category_icon="fa-envelope"
)
appbuilder.add_view(
    CustomerView,
    "Покупатели",
    icon="fa-folder-open-o",
    category="Товарка1",
    category_icon="fa-envelope"
)

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
