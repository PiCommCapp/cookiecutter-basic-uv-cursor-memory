"""A sample CLI."""

import click

@click.command()
def main():
    click.echo("Hello, World!")


if __name__ == '__main__':  # pragma: no cover
    main()  # pylint: disable=no-value-for-parameter