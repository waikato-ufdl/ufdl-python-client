"""
Automatically generates model packages for working with particular models.
"""
import os


MODELS = {
    "organisation": {
        "name": "str"
    },
    "membership": {
        "user": "int",
        "organisation": "int",
        "permissions": "str"
    },
    "project": {
        "name": "str",
        "organisation": "int"
    },
    "user": {
        "username": "str",
        "password": "str",
        "first_name": "str",
        "last_name": "str",
        "email": "str"
    },
    "dataset":{
        "name": "str",
        "version": "int",
        "project": "int",
        "licence": "str",
        "is_public": "bool",
        "tags": "str"
    }
}

PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))

# Read the template for _actions.py
with open(os.path.join(PACKAGE_DIR, "_actions.py.template"), "r") as file:
    TEMPLATE = file.read()

for model, params in MODELS.items():
    model_package_dir = os.path.join(PACKAGE_DIR, model)

    # Create the package for the model
    if not os.path.exists(model_package_dir):
        os.mkdir(model_package_dir)

    # Write the __init__.py file for the package
    with open(os.path.join(model_package_dir, "__init__.py"), "w") as file:
        file.write("from ._actions import list, create, retrieve, update, partial_update, destroy\n")

    # Create the parameter/argument lists
    PARAMS = ", ".join(f"{name}: {type}" for name, type in params.items())
    OPTIONAL_PARAMS = ", ".join(f"{name}: Optional[{type}] = None" for name, type in params.items())
    ARGS = ", ".join(f"{name}={name}" for name in params)

    # Write the _actions.py file for the package
    with open(os.path.join(model_package_dir, "_actions.py"), "w") as file:
        file.write(TEMPLATE.format(URL=f"{model.upper()}S_URL",
                                   PARAMS=PARAMS,
                                   OPTIONAL_PARAMS=OPTIONAL_PARAMS,
                                   ARGS=ARGS,
                                   OPEN_BRACE="{",
                                   CLOSE_BRACE="}"))
