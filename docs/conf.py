import sys
import os

dir_ = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_)
sys.path.insert(0, os.path.abspath(os.path.join(dir_, "..")))

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

import hooky

extensions = ['sphinx.ext.autodoc']
# extensions += ['sphinxcontrib.programoutput']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'hooky'
copyright = u'2017, Chen Meng'
author = u'Chen Meng'


version = hooky.__version__
release = hooky.__version__

language = None

exclude_patterns = ['_build']

pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']

# htmlhelp_basename = 'ipodshuffledoc'

# man_pages = [
#    (master_doc, 'ipodshuffle', u'ipodshuffle Documentation',
#     [author], 1)
# ]

# texinfo_documents = [
#  (master_doc, 'ipodshuffle', u'ipodshuffle Documentation',
#   author, 'ipodshuffle', 'One line description of project.',
#   'Miscellaneous'),
# ]

autoclass_content = 'both'
autodoc_member_order = 'bysource'

latex_elements = {

# The paper size ('letterpaper' or 'a4paper').
# 'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
'preamble': '''
\\hypersetup{unicode=true}
\\usepackage{CJKutf8}
\\begin{CJK}{UTF8}{gbsn}
\\AtEndDocument{\\end{CJK}}
'''
}
