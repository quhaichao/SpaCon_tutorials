# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SpaCon_tutorials'
copyright = '2025, quhaichao'
author = 'quhaichao'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',               # 将 .ipynb 当作源文件
    'sphinx_rtd_theme',       # RTD 默认主题
    # 如果用 MyST-NB，改成 'myst_nb'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# -- HTML 主题 --
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
html_static_path = ['_static']


# -- 如果希望在构建时自动执行 Notebook（无输出时） --
nbsphinx_execute = 'auto'  # 或 'always' / 'never'
