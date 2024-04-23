"""This package is used to build elements from data into
MarkDown format for the specification text.

Functions decorated in "define_env()" are callable throughout the
specification and are run/rendered with the mkdocs plugin "macros".
"""

import os
import sys

code_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(code_path)

import macros  # noqa E402


def define_env(env):
    """Define variables, macros and filters for the mkdocs-macros plugin.

    Parameters
    ----------
    env : :obj:`macros.plugin.MacrosPlugin`
        An object in which to inject macros, variables, and filters.

    Notes
    -----
    "variables" are the dictionary that contains the environment variables
    "macro" is a decorator function, to declare a macro.

    Macro aliases must start with "MACROS___"
    """
    env.macro(
        macros.generate_converter_table, "MACROS___generate_converter_table"
    )
    env.macro(macros.generate_tools_table, "MACROS___generate_tools_table")
    env.macro(macros.generate_members_table, "MACROS___generate_members_table")
    env.macro(macros.generate_beps_table, "MACROS___generate_beps_table")
    env.macro(macros.generate_grants_table, "MACROS___generate_grants_table")
