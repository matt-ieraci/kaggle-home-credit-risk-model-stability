from setuptools import setup, find_packages

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(
    name='home_credit',
    version='0.0.1',
    description='home-credit-risk-kaggle',
    author='matt-ieraci',
    author_email='mattieraci7@gmail.com',
    #url='https://github.com/matt-ieraci/kaggle-home-credit-risk-model-stability',
    install_requires=requirements,
    packages=find_packages(),
    test_suite='tests',
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    zip_safe=False
    )