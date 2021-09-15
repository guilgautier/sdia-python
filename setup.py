# From pip >= 21.1, setup.cfg suffices: setup.py is not mandatory https://pip.pypa.io/en/stable/news/#v21-1
# For pip < 21.1, here is a shim that makes an editable install possible:
# pip install -e .

import setuptools

if __name__ == "__main__":
    setuptools.setup()
