import ast
import re
import setuptools
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text(encoding="UTF-8")

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open("requirements.txt") as stream:
    raw = stream.read().splitlines()
    requirements = [x for x in raw if not x.startswith("git+")]
    dependencies = [x for x in raw if x.startswith("git+")]

with open('discord/ext/cluster/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('UTF-8')).group(1)))

setuptools.setup(
    author="DaPandaOfficial",
    python_requires=">=3.8.0",
    license="MIT License",
    author_email="miroslav.rosenov39@gmail.com",
    long_description_content_type="text/markdown",
    description="A high-performance inter-process communication library designed to handle communication between multiple shards",
    long_description=long_description,
    url="https://github.com/MiroslavRosenov/better-cluster",
    packages=[
        "discord.ext.cluster"
    ],
    project_urls={
        "Source": "https://github.com/MiroslavRosenov/better-cluster",
        "Issue Tracker": "https://github.com/MiroslavRosenov/better-cluster/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Communications",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=requirements,
    dependencies=dependencies,
    keywords=["better-cluster", "cluster", "python", "discord.py"],
    name="better-cluster",
    version=version,
)
