from distutils.core import setup

setup(
    name='Foreman',
    version='0.9',
    author='David Blaisonneau, Arnaud Morin',
    author_email='david.blaisonneau@orange.com, arnaud1.morin@orange.com',
    packages=['Foreman'],
    scripts=[],
    url='https://github.com/davidblaisonneau-orange/foreman',
    download_url='https://pypi.python.org/packages/source/F/Foreman/Foreman-0.9.tar.gz',
    license='LICENSE',
    description='Python library to manipulate The Foreman through the API',
    long_description=open('README.rst').read(),
    install_requires=['requests-futures', 'requests', 'json'],
    keywords = ['foreman'],
)
