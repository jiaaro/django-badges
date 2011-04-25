__doc__ = """
An easy to use app that provides Stack Overflow style badges with a minimum ammount of effort in django

See the README file for details, usage info, and a list of gotchas.
"""

from setuptools import setup

setup(
    name='django-badges',
    version='0.1.4',
    author='James Robert',
    author_email='jiaaro@gmail.com',
    description=('An easy to use app that provides Stack Overflow style badges'
                'with a minimum ammount of effort in django'),
    license='GPLv3',
    keywords='django badges social',
    url='http://bitbucket.org/jiaaro/django-badges/',
    packages=['badges'],
    long_description=__doc__,
    classifiers=[
    	'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)
