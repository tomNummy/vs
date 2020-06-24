from distutils.core import setup

setup(
    name='vs-graph',
    author="tomNummy",
    author_email="tom.nummy@gmail.com",
    description="A small tool for visualizing concept graphs us Google search",
    url="https://github.com/tomNummy/vs-graph",
    version='0.1.0',
    packages=['networkx', 'click'],
    license='MIT License'
)