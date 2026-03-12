import click

@click.command()
@click.argument("desde")
@click.argument("hasta")

def run(desde, hasta):

    print("Scanning device...")