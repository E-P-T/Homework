import re
import shutil

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info
from setuptools.command.install import install

VERSION_FILE = 'rss_parse/__init__.py'


def version():
    _version_re = re.compile(r'^\s*__version__\s*=\s*[\'"](.*)[\'"]\s*$')

    with open(VERSION_FILE, 'r') as f:
        res = _version_re.search(f.read())
        if res is None:
            raise RuntimeError(f"Unable to find version string in {VERSION_FILE}.")
        ver = res.group(1)

    return ver


fonts_installed = False


def install_fdpf_fonts():
    global fonts_installed
    if fonts_installed:
        return

    try:
        import os
        import fpdf

        local_fonts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

        fpdf_fonts_dir = os.path.join(os.path.dirname(fpdf.__file__), 'font')
        if not os.path.exists(fpdf_fonts_dir):
            os.mkdir(fpdf_fonts_dir)

        font_file_names = [f for f in os.listdir(local_fonts_dir) if f.endswith(".ttf")]
        for font_file_name in font_file_names:
            full_file_name = os.path.join(local_fonts_dir, font_file_name)
            shutil.copy(full_file_name, fpdf_fonts_dir)

        fonts_installed = True
    except ModuleNotFoundError:
        pass


class CustomInstallCommand(install):

    def run(self):
        install.run(self)
        install_fdpf_fonts()


class CustomDevelopCommand(develop):

    def run(self):
        develop.run(self)
        install_fdpf_fonts()


class CustomEggInfoCommand(egg_info):

    def run(self):
        egg_info.run(self)
        install_fdpf_fonts()


setup(
    name='rss_reader',
    version=version(),
    description='Pure Python command-line RSS reader.',
    author='Aleksandra Khorosheva',
    zip_safe=False,
    author_email='Aleksandra_Khorosheva@epam.com',
    keywords=['RSS Reader', 'RSS Feed Parser'],
    install_requires=[
        'setuptools~=57.0.0',
        'requests~=2.27.1',
        'xmltodict~=0.13.0',
        'fpdf2>=2.5.5',
        'python-dateutil~=2.8.0',
        'html2text>=2020.1.16',
    ],
    python_requires=">=3.8",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rss_reader=rss_parse.rss_reader:main_wrapper',
        ],
    },
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
        'egg_info': CustomEggInfoCommand,
    },
)
