from setuptools import setup, find_packages

setup(
    name='django-conoha',
    version='0.0.1',
    description='ConoHaオブジェクトストレージのカスタムストレージ',
    author='Compeito',
    author_email='com0806peito@icloud.com',
    url='https://github.com/Compeito/django-conoha',
    license='MIT',
    packages=find_packages(where='.'),
    install_requires=['django', 'requests'],
)
