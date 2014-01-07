import os
from app.models import Server


def create_yml():
    preamble = "---\n\n"
    servers = Server.query.all()

    basepath = os.path.dirname(__file__)
    filepath = os.path.abspath(os.path.join(basepath, '..', 'vars', 'config.yml'))
    yml_file = open(filepath, 'w')
    yml_file.write(preamble)
    for server in servers:
        yml_file.write("\t" + server.name + ":\n")
        for variable in server.variables:
            yml_file.write("\t\t" + "- {" + variable.name + ": " + variable.value + "}\n")
    yml_file.close()