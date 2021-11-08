import os
from setuptools import setup

descr = """A linear regression tool"""

version = None
with open(os.path.join("linear_regression", "__init__.py"), "r") as fid:
    for line in (line.strip() for line in fid):
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip("'")
            break
if version is None:
    raise RuntimeError("Could not determine version")


DISTNAME = "linear_regression"
DESCRIPTION = descr
MAINTAINER = "Pierre Ablin"
MAINTAINER_EMAIL = "xxx@xxx.fr"
LICENSE = "MIT"
DOWNLOAD_URL = "https://github.com/pierreablin/test_package.git"
VERSION = version
URL = "https://github.com/pierreablin/test_package"


def get_requirements():
    """Return the requirements of the projects in requirements.txt"""
    with open("requirements.txt") as f:
        requirements = [r.strip() for r in f.readlines()]
    return [r for r in requirements if r != ""]


def package_tree(pkgroot):
    """Get the submodule list."""
    # Adapted from VisPy
    path = os.path.dirname(__file__)
    subdirs = [
        os.path.relpath(i[0], path).replace(os.path.sep, ".")
        for i in os.walk(os.path.join(path, pkgroot))
        if "__init__.py" in i[2]
    ]
    return sorted(subdirs)


if __name__ == "__main__":
    setup(
        name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        version=VERSION,
        url=URL,
        download_url=DOWNLOAD_URL,
        classifiers=[
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS",
            "Programming Language :: Python :: 3",
        ],
        platforms="any",
        python_requires=">=3.7",
        packages=package_tree("linear_regression"),
        install_requires=["numpy"],
    )