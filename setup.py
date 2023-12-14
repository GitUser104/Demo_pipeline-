from setuptools import setup, find_namespace_packages

setup(name="census_income",
      version="0.0.1",
      author="nishant",
      author_email="nishantwestern@gmail.com",
      packages=find_namespace_packages(),
      install_requires=["pandas","numpy","flask"]
    )

"""to install our census income as a package in our local venv"""


