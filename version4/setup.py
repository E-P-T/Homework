import setuptools

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setuptools.setup(
    include_package_data=True,
    name="RSS Reader",
    version="2.0.0",
    description="Pure Python command-line RSS reader.",
    author="arslan",
    packages=setuptools.find_packages(),
    install_requires=[requirements],
    py_modules=["rss_reader"],
    entry_points='''
    [console_scripts]
    rss_reader=rss_reader:main
    ''',
    python_requires='>=3.9'
)
