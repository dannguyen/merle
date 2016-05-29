import click
CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}

@click.group(context_settings=CONTEXT_SETTINGS)
def hello_world():
    pass


@hello_world.command()
@click.argument('url')
def info(**kwargs):
    url = kwargs['url']
    print(url)

if __name__ == '__main__':
    hello_world()
