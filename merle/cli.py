import click
from collections import OrderedDict
from jinja2 import Environment, PackageLoader
from merle.fetched_resource import FetchedResource
from slugify import slugify as string_slugify

DEFAULT_TEMPLATE = 'yaml.jinja2.txt'


def dumper(obj, template_name=DEFAULT_TEMPLATE):
    env = Environment(loader=PackageLoader('merle', 'templates'),
                      trim_blocks=True, lstrip_blocks=True)
    t = env.get_template(template_name)
    return t.render(f=obj)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
def slugify(title):
    click.echo(string_slugify(title))

@cli.command()
@click.argument('url')
@click.option('--anchor-link', '-a', is_flag=True)
@click.option('--tabular', '-t', is_flag=True)
@click.option('--markdown', '-m', is_flag=True)
def meta(url, tabular, markdown, anchor_link):
    o = OrderedDict()
    f = FetchedResource(url)
    o['slug'] = f.slug
    o['url'] = f.returned_url
    o['title'] = f.title
    o['description'] = f.description
    o['fetched_at'] = f.fetched_at
    o['published_at'] = f.published_at
    o['authors'] = f.authors
    o['word_count'] = f.word_count
    o['excerpt'] = f.excerpt

    if tabular:
        click.echo(dumper(o), err=True)
        click.echo('\t'.join(
            [o['title'], o['url'], o['description'], str(o['word_count'])]
        ))
    elif markdown:
        click.echo("""[%s](%s)""" % (o['title'], o['url']))
    elif anchor_link:
        click.echo("""<a href="%s">%s</a>""" % (o['url'], o['title']))
    else:
        click.echo(dumper(o))




if __name__ == '__main__':
    cli()
