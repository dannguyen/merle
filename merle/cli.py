import click
import rtyaml as ryaml
from collections import OrderedDict
from merle.fetched_resource import FetchedResource

def dumper(obj):
    return ryaml.dump(obj)


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
