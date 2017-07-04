from setuptools import setup

setup(
    name='school',
    version='0.1',
    py_modules=['school'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        school=school:cli
    ''',
)
