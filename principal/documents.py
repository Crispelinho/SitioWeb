
# -*- coding: utf-8 -*-
from django_elasticsearch_dsl import DocType, Index, fields

from .models import Contacto

item = Index('item')


@item.doc_type
class ItemDocument(DocType):
    """Document in elasticsearch with index item """

    price = fields.FloatField()

    class Meta:
        model = Item
        fields = [
            'id',
            'nombre',
            'apellido',
            'Ncelular',
            'fotogragia',
            'correo'
        ]

    def prepare_price(self, instance):
        return float(instance.price)