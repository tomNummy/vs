from setuptools import find_packages, setup

setup(
    name="vs_graph",
    author="tomNummy",
    author_email="tom.nummy@gmail.com",
    description="A small tool for visualizing concept graphs us Google search",
    url="https://github.com/tomNummy/vs-graph",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["networkx", "click", "pydantic", "bokeh", "requests"],
    license="MIT License",
    entry_points={"console_scripts": ["vs-graph=cli:vs_graph"]},
)
