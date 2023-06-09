from setuptools import setup

setup(
    author = 'AyoBlue',
    url = 'https://github.com/AyoBlue/RoCloud',
    version = '1.0.0',
    install_requires = [
        'aiohttp>=3.7.4'
    ],
    packages = [
        'roblox'
    ],
    description = 'Roblox Cloud API',
    python_requires = '>=3.8.0'
)
