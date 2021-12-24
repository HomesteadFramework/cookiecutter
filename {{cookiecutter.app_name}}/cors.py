from typing import List


def get_cors_domains(env: str) -> List:
    '''Return a list of domains we accept for cors'''
    if env == 'local':
        return [
            'http://{{cookiecutter.app_domain}}:{{app_port}}',
        ]