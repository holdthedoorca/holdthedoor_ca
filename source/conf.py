# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HoldTheDoor'
copyright = '2024, HoldTheDoor'
author = 'HoldTheDoor'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


import os
import sys
# Insert the '_extension' directory into the path so Sphinx can find it
sys.path.insert(0, os.path.abspath('_extension'))
from datetime import date
import ablog

import logging
logging.getLogger('sphinx').setLevel(logging.DEBUG)


extensions = [
    'myst_parser',
    'sphinx_design', 
    'gallery_directive',
    'component_directive',
    'ablog',                # Blogging (optional)
    'sphinx.ext.autodoc',   # Code documentation from docstrings
    'sphinx.ext.intersphinx', # External links to other docs (optional)

    'sphinx_togglebutton',  # Collapsible content
    'sphinx_favicon',       # Favicon management (optional)
    'sphinxcontrib.youtube',
    'sphinx.ext.autosectionlabel',
]

autosectionlabel_prefix_document = True

# ABlog configuration
# ABlog configuration
blog_basepath = 'news'
blog_path = 'news'
blog_post_pattern = 'news/articles/*/*/*.rst'
blog_feed_fulltext = True
blog_feed_subtitle = "Immigration News and Updates"
blog_feed_length = 20

# Fixed blog_authors configuration - note the space after 'Henry'!
blog_authors = {
    "AAA": ("CCC", None),
}

# Location configuration
blog_locations = {
    'Canada': ('Canada', None),
}
blog_default_location = 'Canada'

# Language configuration
blog_languages = {
    'en': ('English', None),
}
blog_default_language = 'en'

# Post related settings
post_auto_excerpt = 1
post_auto_image = 0
post_date_format = '%Y-%m-%d'
post_date_format_short = '%B %d, %Y'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = "We Hold The Door Open to Canada for You!"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]


# -- Sitemap -----------------------------------------------------------------


# -- MyST options ------------------------------------------------------------

# This allows us to use ::: to denote directives, useful for admonitions
myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}

# -- Internationalization ----------------------------------------------------

# specifying the natural language populates some key tags
language = "en"

# -- Ablog options -----------------------------------------------------------

blog_path = "examples/blog/index"
blog_authors = {
    "pydata": ("PyData", "https://pydata.org"),
    "jupyter": ("Jupyter", "https://jupyter.org"),
}


# -- sphinx_ext_graphviz options ---------------------------------------------

graphviz_output_format = "svg"
inheritance_graph_attrs = dict(
    rankdir="LR",
    fontsize=14,
    ratio="compress",
)


# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.svg"
html_favicon = "_static/logo.svg"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""  # to reveal the build date in the pages meta


html_theme_options = {
    "external_links": [
        {
            "url": "https://www.canada.ca/en/immigration-refugees-citizenship.html",
            "name": "Official Website of IRCC",
        },
        {
            "url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/application/account.html",
            "name": "Official Website of GCKey",
        },
        {
            "url": "https://ircc-tracker-suivi.apps.cic.gc.ca/en/login",
            "name": "Official Website of Tracker",
        },
        {
            "url": "https://atip-aiprp.apps.gc.ca/atip/privacyTerms.do?requestflow=ircc",
            "name": "Official Website of ATIP(IRCC)",
        },
        {
            "url": "https://atip-aiprp.tbs-sct.gc.ca/",
            "name": "Official Website of ATIP(CBSA)",
        },
        {
            "url": "https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-processing-times.html",
            "name": "Official Website of Processing Time",
        },

    ],
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "X",
            "url": "https://x.com/holdthedoor_ca",
            "icon": "fa-brands fa-x-twitter",
        }
    ],
    # alternative way to set twitter and github header icons
    # "github_url": "https://github.com/pydata/pydata-sphinx-theme",
    # "twitter_url": "https://twitter.com/PyData",
    "logo": {
        "text": "HoldTheDoor.ca",
        "image_dark": "_static/logo-dark.svg",
    },
    "use_edit_page_button": False,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    # "show_nav_level": 2,
    #"announcement": "<div class='sidebar-message'>🇨🇦 Canada is famous for its friendliness, diversity, and freedom. If you'd like to travel/study/work, or immigrate here, we'd like to hold the door for you.</div>",
    "show_version_warning_banner": True,
    #"navbar_center": ["version-switcher", "navbar-nav"],
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template", "sidebar-ethical-ads"],
    # "article_footer_items": ["test", "test"],
    # "content_footer_items": ["test", "test"],
    "footer_start": "",
    #"footer_center": ["sphinx-version"],
    "footer_end": ["copyright"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "sourcelink"],
        "examples/no-sidebar": [],
    },
    # "back_to_top_button": False,
}

html_sidebars = {
    "immigration/index": [
        "sidebar-nav-bs",
        "custom-template",
    ],  # This ensures we test for custom sidebars
    "examples/no-sidebar": [],  # Test what page looks like with no sidebar items
    "examples/persistent-search-field": ["search-field"],
    # Blog sidebars
    # ref: https://ablog.readthedocs.io/manual/ablog-configuration-options/#blog-sidebars
    "examples/blog/*": [
        "ablog/postcard.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/authors.html",
        "ablog/languages.html",
        "ablog/locations.html",
        "ablog/archives.html",
    ],
}

html_context = {
    "doc_path": "docs",
    "title": "HoldTheDoor - Your Custom Slogan Here"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["pydata-icon.js", "custom-icon.js"]
todo_include_todos = True

# -- favicon options ---------------------------------------------------------

# see https://sphinx-favicon.readthedocs.io for more information about the
# sphinx-favicon extension
favicons = [
    # generic icons compatible with most browsers
    "favicon-32x32.png",
    "favicon-16x16.png",
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
    # chrome specific
    "android-chrome-192x192.png",
    # apple icons
    {"rel": "mask-icon", "color": "#459db9", "href": "safari-pinned-tab.svg"},
    {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    # msapplications
    {"name": "msapplication-TileColor", "content": "#459db9"},
    {"name": "theme-color", "content": "#ffffff"},
    {"name": "msapplication-TileImage", "content": "mstile-150x150.png"},
]