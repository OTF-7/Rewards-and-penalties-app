from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rewards_and_penalties/__init__.py
from rewards_and_penalties import __version__ as version

setup(
	name="rewards_and_penalties",
	version=version,
	description="An app for managing employee rewards and penalties",
	author="ERP batch 1",
	author_email="erp@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
