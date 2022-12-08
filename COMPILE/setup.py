import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="django-admin-compare",
    version="0.1",
    author="Slava Ukolov",
    author_email="ukolovsl88@gmail.com",
    description="adds an action 'compare' to the admin panel on a page with a list of objects.",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="package_github_page",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=['Django>=3.2', 'numpy'],
    include_package_data=True
)
