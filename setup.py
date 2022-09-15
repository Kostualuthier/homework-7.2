from setuptools import setup, find_namespace_packages

setup(
    name='clean-folder',
    version='1.2',
    description='Code to clean and sort folders on a computer',
    url='https://github.com/Kostualuthier/goit-homework-phyton/tree/main/clean-folder',
    author='Kostyantyn Boyko',
    author_email='kostualuthier@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['shutil', 'sys', 'os', 'datetime'],
    entry_points={'console_scripts': ['clean-folder = useful.sort:get_dir_name']}
)