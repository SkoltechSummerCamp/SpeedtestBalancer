#!/usr/bin/env python3
# Patched by AleksandrVi vinogradov.alek@gmail.com

import connexion

from swagger_server import encoder
import os


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Balancer'}, pythonic_params=True)
    app.run(port=os.getenv('BALANCER_PORT', "8080"))


if __name__ == '__main__':
    main()
