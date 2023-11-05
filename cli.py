import click

@click.group()
def cli():
    pass

@cli.command()
def os():
    from user_agent_maker import UserAgentMaker
    print(UserAgentMaker.load_os_info())

if __name__ == '__main__':
    cli()