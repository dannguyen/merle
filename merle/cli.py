import click
from collections import OrderedDict
from fetched_resource import FetchedResource
from extractor import extract_element
import rtyaml as ryaml
# CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}
#
# @click.group(context_settings=CONTEXT_SETTINGS)
# def hello_world():
#     pass
#

# @hello_world.command()
# @click.argument('url')
# def info(**kwargs):
#     url = kwargs['url']
#     print(url)

def dumper(obj):
    return ryaml.dump(obj)


## temp


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
