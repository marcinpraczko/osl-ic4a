# -*- coding: utf-8 -*-

import click
from ic4a import ic4amainapp


@click.command(short_help='Create files from templates')
@click.pass_context
def template(ctx):  # pragma: no cover
    """
    Create files or file structure from selection of templates
    """
    print ctx.obj['args']

    ic4a = ic4amainapp.IC4A()
    ic4a.command_template()
