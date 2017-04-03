# -*- coding: utf-8 -*-

"""
This module should be used for CLI commands

"""

# TODO: Add to doc: pip install --editable .
# TODO: So far based on molecule code
# - https://github.com/metacloud/molecule/blob/master/molecule/cli.py

import click
import command


@click.group()
@click.option('--verbose', '-v',
              is_flag=True, default=False,
              help='Enables verbose mode.')
# TODO: Seems be not working with dynamic version so far
# @click.version_option(version=ic4a.__version__)
@click.version_option("0.1.0")
@click.pass_context
def cli(ctx, verbose):  # pragma: no cover
    """
    IC4A - Interactive Console for Automation

    For help on any individual command run `ic4a COMMAND --help`
    """
    ctx.obj['args'] = {}
    ctx.obj['args']['verbose'] = verbose


def main():
    """ Ic4a ... UPDATE ME"""
    cli(obj={})

cli.add_command(command.init.init)
cli.add_command(command.template.template)
