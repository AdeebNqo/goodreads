from setuptools import setup

setup(
    name='goodreads',
    description="Python wrapper for Goodreads API",
    long_description=open("README.rst").read(),
    author='Sefa Kilic, Zola Mahlaza',
    author_email='sefakilic@gmail.com, adeebnqo@gmail.com',
    url='https://github.com/adeebnqo/goodreads/',
    version='0.2.4',
    install_requires=['nose', 'xmltodict', 'requests', 'rauth'],
    packages=['goodreads'],
    scripts=[],
    license='MIT',
)
