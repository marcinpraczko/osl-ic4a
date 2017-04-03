# -*- coding: utf-8 -*-

import click
from ic4a import ic4amainapp


@click.command(short_help='Create required initial configuration')
@click.pass_context
def init(ctx):  # pragma: no cover
    """
    Create required files and folders in user home directory.
    """
    print ctx.obj['args']

    ic4a = ic4amainapp.IC4A()
    ic4a.command_init()
