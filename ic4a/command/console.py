# -*- coding: utf-8 -*-

import click
from ic4a import ic4amainapp


@click.command(short_help='Run interactive console')
@click.pass_context
def console(ctx):  # pragma: no cover
    """
    Run interactive console.
    """
    print ctx.obj['args']

    ic4a = ic4amainapp.IC4A()
    ic4a.interactive()
