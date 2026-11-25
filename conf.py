# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

import json
import os

# -- Project information -----------------------------------------------------

project = 'WP fail2ban CLI'
copyright = '2026, Charles Lecklider'
author = 'Charles Lecklider'

_pkg = json.load(open(os.path.join(os.path.dirname(__file__), 'version.json')))
# Docs titles are major.minor. A patch release does not publish a new manual.
_core = _pkg.get('version', '').split('-', 1)[0].split('+', 1)[0]
_parts = _core.split('.')
version = '.'.join(_parts[:2]) if len(_parts) >= 2 else _core
release = version
if _pkg.get('version_label'):
    release = '%s (%s)' % (version, _pkg['version_label'])


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.intersphinx'
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv', 'venv']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = []

master_doc = 'index'

intersphinx_mapping = {
    'wp-fail2ban': (
        'https://docs.wp-fail2ban.com/en/stable/', (
            '../../plugin/sphinx/_build/html/objects.inv', None
        )
    ),
}

lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
