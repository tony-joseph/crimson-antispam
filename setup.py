import os
from setuptools import setup


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='crimson_antispam',
    packages=['antispam'],
    version='0.1.2',
    include_package_data=True,
    license='BSD License',
    description='Anti-spam package for django framework',
    author='Tony J',
    author_email='tony@crimsonhack.com',
    url='https://github.com/tony-joseph/crimson_antispam',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
