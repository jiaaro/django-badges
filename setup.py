__doc__ = """
An easy to use app that provides Stack Overflow style badges with a minimum ammount of effort in django

See the README file for details, usage info, and a list of gotchas.
"""

from setuptools import setup

setup(
    name='django-badges',
    version='0.1',
    author='Jim Robert',
    description=('An easy to use app that provides Stack Overflow style badges'
                'with a minimum ammount of effort in django'),
    license='GPLv3',
    keywords='django badges social',
    url='http://bitbucket.org/jiaaro/django-badges/',
    packages=['badges'],
    long_description=__doc__,
    classifiers=[
        'License :: OSI Approved :: GPL License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)
