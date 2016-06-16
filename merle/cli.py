import click
from collections import OrderedDict
from jinja2 import Environment, PackageLoader
from merle.fetched_resource import FetchedResource


DEFAULT_TEMPLATE = 'yaml.jinja2.txt'

def dumper(obj, template_name=DEFAULT_TEMPLATE):
    env = Environment(loader=PackageLoader('merle', 'templates'),
                      trim_blocks=True, lstrip_blocks=True)
    t = env.get_template(template_name)
    return t.render(f=obj)


@click.command()
@click.argument('url')
def fetch_metadata(url):
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


    click.echo(dumper(o))



if __name__ == '__main__':
    fetch_metadata()
