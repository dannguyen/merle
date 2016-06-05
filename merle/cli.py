import click
from collections import OrderedDict
from fetched_resource import FetchedResource
from extractor import extract_element
from newspaper import fulltext
import ruamel.yaml as ryaml
import re
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
    return ryaml.dump(obj, Dumper=ryaml.RoundTripDumper)

def excerpt(resource, wordcount=60):
    txt = re.sub('\s+', ' ', fulltext(resource.html)).strip()
    words = re.split(r' ', txt)
    exwords = words if len(words) < wordcount else words[:wordcount] + ['...']
    return ' '.join(exwords)

@click.command()
@click.argument('url')
def fetch_metadata(url):
    o = OrderedDict()
    f = FetchedResource(url)
    o['url'] = f.returned_url
    o['title'] = list(extract_element('title', f).values())[0]
    o['excerpt'] = excerpt(f)
    o['fetched_at'] = f.fetched_at

    click.echo(dumper(o))


if __name__ == '__main__':
    fetch_metadata()
