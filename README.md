# sen1-poc-zabbix-descriptions

Nous manquons de temps pour bien documenter ce code.

Pour l'installation :
- installer apache et mod_python
- ajouter à la configuration apache :
```
        <Directory /var/www/html/py/>
                Options Indexes FollowSymLinks MultiViews
                AllowOverride None
                Order allow,deny
                allow from all
                AddHandler mod_python .py
                #PythonHandler mod_python.publisher
                PythonHandler meta_ui
                PythonDebug On
        </Directory>
```
- cd /var/www/html
- git clone https://github.com/consometers/sen1-poc-zabbix-descriptions

Ce code permet d'afficher une page avec des informations récupérées de Zabbix, dans le champ description d'un item. Par exemple : 
```
{
  "Type": "Consommation",
  "Titre": "Ecole de Kersabiec",
  "Batiment": "Ecole",
  "Chauffage": "Chaudière à gaz",
  "ECS": "Chaudière à gaz",
  "Consommation": "53 930"
}
```
Ce code s'appelle comme ceci : https://<serveur>/py/meta_ui.py?itemid=<ID Zabbix de l'item>.
Pour utiliser ce code, il est nécessaire de créer un utilisateur type API dans Zabbix et de le renseigner dans le fichier py/meta_ui.py avec l'URL du serveur Zabbix : 
```
    settings = {
        "zabbix": {
            "url": "<CHANGEME>",
            "user": "<CHANGEME>",
            "password": "<CHANGEME>"
        }
    }

```
