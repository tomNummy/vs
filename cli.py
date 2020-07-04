import re

import click

from graph import build_graph
from plot import build_plot


def get_valid_filename(s):
    """
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    >>> get_valid_filename("john's portrait in 2004.jpg")
    'johns_portrait_in_2004.jpg'
    """
    s = str(s).strip().replace(" ", "_")
    return re.sub(r"(?u)[^-\w.]", "", s)


@click.command(name="vs-graph")
@click.argument("term")
@click.option(
    "--radius",
    "-r",
    type=click.IntRange(min=1, max=10, clamp=False),
    required=False,
    default=3,
)
@click.option("--fpath", "-f", type=click.Path(), required=False, default=None)
def vs_graph(term, radius, fpath):
    """Build a neighborhood graph of the search term

    \b
    Args:
        term: Word to search for
        radius: Maximum distance away from the central node to keep in the graph
        fpath: Where to save the html output.
    """

    if not fpath:
        fpath = get_valid_filename(term) + ".html"
    g = build_graph(term)
    breakpoint()
    build_plot(term, g, fpath)
