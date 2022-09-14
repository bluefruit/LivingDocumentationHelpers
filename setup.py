from setuptools import setup

setup(
    name='living_documentation_helpers',
    version='1.0.0',
    description='Helper files for living documentation using Sphinx and Behave',
    url='https://www.bluefruit.co.uk',
    author='Byran Wills-Heath',
    author_email='byran@bluefruit.co.uk',
    license='MIT',
    packages=[
        'living_documentation_helpers'
    ],
    entry_points={
        "console_scripts": [
            "behave2sphinx = living_documentation_helpers.create_sphinx_feature_file_page:main",
            "behave2sphinx-all = living_documentation_helpers.create_sphinx_feature_file_page:process_files_in_current_directory",
            "userneeds2sphinx = living_documentation_helpers.create_userneeds_page:main"
        ]
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'behave >= 1.2.6'
    ]
)
