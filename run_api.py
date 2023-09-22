import os

from admin_api.web.app import setup_app
from aiohttp.web import run_app

if __name__ == "__main__":
    run_app(
        setup_app(
            config_path=os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "etc", "config.yaml"
            )
        ), host='127.0.0.1', port='8000'
    )