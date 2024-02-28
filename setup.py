import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Perkiraan cuaca bekasi",
    version="1.0",
    author="call me dam",
    author_email="cosmodanang@gmail.com",
    description="This package will get the latest weather from BMKG | Meteorological, Climatological, and "
                "Geophysical Agency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tamabii/Perkiraan-cuaca",
    project_urls={
        "Website": "https://remoteworker.id",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
