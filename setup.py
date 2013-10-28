from setuptools import setup

setup(
    name='histo',
    version=0.1,
    description='Statistical histograms based on Sturges rule',
    author='Pavel Paulau',
    author_email='pavel.paulau@gmail.com',
    py_modules=['histo'],
    entry_points={
        'console_scripts': ['histo = histo:main']
    },
)
