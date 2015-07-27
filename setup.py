from distutils.core import setup

setup(
    name='Foreman',
    version='0.9',
    author='David Blaisonneau, Arnaud Morin',
    author_email='david.blaisonneau@orange.com, arnaud1.morin@orange.com',
    packages=['Foreman'],
    scripts=[],
    url='http://pypi.python.org/pypi/Foreman/',
    license='LICENSE',
    description='Python library to manipulate The Foreman through the API',
    long_description=open('README.txt').read(),
    install_requires=['requests-futures', 'requests', 'json'],
)
