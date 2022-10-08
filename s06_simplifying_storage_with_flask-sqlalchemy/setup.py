from setuptools import setup, find_packages

setup(
    name='s06_simplifying_storage_with_flask-sqlalchemy',
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"":"src"}
)