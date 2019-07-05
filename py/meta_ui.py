from mod_python import apache
from mod_python import util
import pprint
import json
import collections
from pyzabbix import ZabbixAPI
from jinja2 import Environment, PackageLoader, FileSystemLoader
#from zabbixwidget import settings
#from zabbixwidget.controller import environnement
#from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

# chargement des templates
file_loader = FileSystemLoader('./')
environnement = Environment(loader=file_loader)

def handler(req):
  req.content_type = "text/html; charset=utf-8"
  itemId = util.FieldStorage(req).getfirst('itemid')
  req.write(_index(itemId))
  return(apache.OK)

def _index(itemId):
    """
    Affichage du champ description d'un Item Zabbix passe en parametre
    :param request: 
    """

    settings = {
        "zabbix": {
            "url": "<CHANGEME>",
            "user": "<CHANGEME>",
            "password": "<CHANGEME>"
        }
    }

    ("Render template 'production'...")
    template = environnement.get_template("/var/www/html/py/item_description.j2")

    zapi = ZabbixAPI(server = settings["zabbix"]["url"])
    zapi.login(settings["zabbix"]["user"], settings["zabbix"]["password"])

    api_params = {
        "itemids": itemId,
        "output": "extend",
    }
    item_infos = zapi.item.get(**api_params)
    description_dict = collections.OrderedDict()
    description_dict = json.loads(item_infos[0]["description"], object_pairs_hook=collections.OrderedDict)
    model = collections.OrderedDict() 
    model['description_dict'] = description_dict
    response = pprint.pformat(model, indent=2).encode('utf-8')
    response = template.render(model).encode('utf-8')
    return response



