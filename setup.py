from setuptools import setup

setup(
    name='Flask-CORS',
    version='0.1.1',
    url='https://github.com/crgwbr/flask_cors',
    license='BSD',
    author='Craig Weber',
    author_email='craig@crgwbr.com',
    maintainer='Craig Weber',
    maintainer_email='craig@crgwbr.com',
    description='Flask extension for Cross Origin Resource Sharing',
    packages=[
        'flask_cors',
    ],
    package_data={
    },
    zip_safe=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
