>>> from polls.models import Osoba

>>> from polls.serializers import OsobaModelSerializer
>
>>> from rest_framework.renderers import JSONRenderer

>>> from rest_framework.parsers import JSONParser


>>> osoba = Osoba(imie='test shell osoba', nazwisko='nazwisko-shell', miesiac_urodzenia=2)

>>> osoba.save()


>>> serializer = OsobaModelSerializer(osoba)
>
>>> serializer.data
>
{'id': 3, 'imie': 'test shell osoba', 'nazwisko': 'nazwisko-shell', 'miesiac_urodzenia': 2, 'druzyna': None}

>>> content = JSONRenderer().render(serializer.data)
>
>>> content
>
b'{"id":3,"imie":"test shell osoba","nazwisko":"nazwisko-shell","miesiac_urodzenia":2,"druzyna":null}'

>>> import io
>
>> stream = io.BytesIO(content)
>
>>> data = JSONParser().parse(stream)
>
>>> deserializer = OsobaModelSerializer(data=data)
>
>>> deserializer.is_valid()
>
True

>>> repr(deserializer)
>
"OsobaModelSerializer(data={'id': 3, 'imie': 'test shell osoba', 'nazwisko': 'nazwisko-shell', 'miesiac_urodzenia':
 2, 'druzyna': None}):\n    id = IntegerField(read_only=True)\n    imie = CharField(required=True)\n    nazwisko =
CharField(required=True)\n    miesiac_urodzenia = ChoiceField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 'Marzec'),
(4, 'Kwiecien'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'),
 (11, 'Listopad'), (12, 'Grudzien')], default=1)\n    druzyna = PrimaryKeyRelatedField(allow_null=True, queryset=<Q
uerySet [<Druzyna: Tigers (PL)>, <Druzyna: lions (DE)>]>)"

>>> deserializer.validated_data
OrderedDict([('imie', 'test shell osoba'), ('nazwisko', 'nazwisko-shell'), ('miesiac_urodzenia', 2), ('druzyna', No
ne)])

>>> deserializer.save()
>
<Osoba: test shell osoba nazwisko-shell>

>>> deserializer.data
>
{'id': 4, 'imie': 'test shell osoba', 'nazwisko': 'nazwisko-shell', 'miesiac_urodzenia': 2, 'druzyna': None}


















>>> from polls.models import Druzyna
>
>>> from polls.serializers import DruzynaModelSerializer
>
>>> from rest_framework.renderers import JSONRenderer
>
>>> from rest_framework.parsers import JSONParser
>

>>> druzyna = Druzyna(nazwa='uwm', kraj='PL')
>
>>> druzyna.save()

>>> serializer = DruzynaModelSerializer(druzyna)
>
>>> serializer.data
>
{'id': 4, 'nazwa': 'uwm', 'kraj': 'PL'}

>>> content = JSONRenderer().render(serializer.data)
>
>>> content
>
b'{"id":4,"nazwa":"uwm","kraj":"PL"}'
 
>>> import io
>

>>> stream = io.BytesIO(content)
>
>>> data = JSONParser().parse(stream)
>
>>> deserializer = DruzynaModelSerializer(data=data)
>
>>> deserializer.is_valid()
>
True

>>> repr(deserializer)
>
"DruzynaModelSerializer(data={'id': 4, 'nazwa': 'uwm', 'kraj': 'PL'}):\n    id = IntegerField(read_only=True)\n
 nazwa = CharField(required=True)\n    kraj = CharField(required=True)"

>>> deserializer.save()
>
<Druzyna: uwm (PL)>

>>> deserializer.data
>
{'id': 5, 'nazwa': 'uwm', 'kraj': 'PL'}





