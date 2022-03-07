# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Geoscientific data analysis with Python"
copyright = "2022"
author = "D. Whipp, Department of Geosciences and Geography, University of Helsinki"

release = "site"
version = "2022"

# -- General configuration

extensions = [
    "sphinx.ext.mathjax",
    #"sphinx.ext.githubpages",
    #"sphinx.ext.todo",
    #"sphinx_thebe",
    #"sphinxcontrib.googleanalytics",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "myst_nb",
    "jupyter_sphinx"
]

templates_path = ["_templates"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output

html_theme = "sphinx_book_theme"
#html_logo = "_static/geopython.png"
html_title = ""

html_theme_options = {
    # "external_links": [],
    "repository_url": "https://github.com/GeoSciPy/site",
    "repository_branch": "main",
    "path_to_docs": "source/",
    # "twitter_url": "https://twitter.com/pythongis",
    # "google_analytics_id": "UA-159257488-1",
    "use_edit_page_button": True,
    "use_repository_button": True,
    "launch_buttons": {
        #"binderhub_url": "https://mybinder.org",
        #"thebe": True,
        "notebook_interface": "jupyterlab",
        "collapse_navigation": False,
    },
}

html_context = {
    # Enable the "Edit in GitHub link within the header of each page.
    "display_github": True,
    # Set the following variables to generate the resulting github URL for each page.
    # Format Template: https://{{ github_host|default("github.com") }}/{{ github_user }}/{{ github_repo }}/blob/{{ github_version }}{{ conf_py_path }}{{ pagename }}{{ suffix }}
    "github_user": "GeoSciPy",
    "github_repo": "site",
    "github_version": "main/",
    "conf_py_path": "/source/",
}

# Add last modified to all pages
html_last_updated_fmt = ""

# Allow errors
execution_allow_errors = True

# Execute cells only if any of the cells is missing output
jupyter_execute_notebooks = "auto"

# -- Options for EPUB output
epub_show_urls = 'footnote'
