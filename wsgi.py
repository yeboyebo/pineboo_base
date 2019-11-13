"""
WSGI config for AQNEXT project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
from .local import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AQNEXT.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from pineboolib.loader.projectconfig import ProjectConfig
from pineboolib.core.settings import config
from pineboolib.loader import main
from pineboolib.application.parsers import qsaparser

qsaparser.USE_THREADS = False


SQL_CONN = ProjectConfig(database=DATABASES["default"]["NAME"], host=DATABASES["default"]["HOST"], port=DATABASES["default"]["PORT"], type="PostgreSQL (PSYCOPG2)", username=DATABASES["default"]["USER"], password=DATABASES["default"]["PASSWORD"])

if StaticLoader:

    print("Usando encoding para consola", sys.stdout.encoding)

    config.set_value("StaticLoader/%s/enabled" % (DATABASES["default"]["NAME"]), True)  # Para activar carga estática

    config.set_value("ebcomportamiento/SLConsola", True)  # Muestra debug por consola

    config.set_value("StaticLoader/%s/dirs" % DATABASES["default"]["NAME"], dirs)


config.set_value("application/dbadmin_enabled", True) # para dbadmin (comprobación de mtd's)
main.startup_framework(SQL_CONN)

# print("llamada api")
#from pineboolib.qsa import qsa
#from pineboolib import application
#valor = qsa.from_project("flfactppal").iface.valorDefectoEmpresa('codalmacen')
#print("valor = " + str(valor))

#print("Cargado pineboolib versión", application.project.version)

# from pineboolib.qsa import qsa
# iface = qsa.from_project("formRecordgt_proyectos").iface
# print("El iface es", iface)

# print(iface.calculateField("c1"))
