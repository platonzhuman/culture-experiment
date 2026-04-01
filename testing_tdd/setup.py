from setuptools import (
    setup, 
    find_packages,

)

setup(
    name="Platonxa_ndfl",
    version= "0.0.0",
    long_description='calculate_ndfl_lax',
    long_description_content_type= "text/markdown",
    package_dir= {"":"src"},
    packages = find_packages(where="src")
)