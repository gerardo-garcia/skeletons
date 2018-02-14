.. OSM documentation master file, created by
   sphinx-quickstart on Thu Nov 23 16:46:31 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to OSM's documentation!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


ReST intro
==========

Sections
--------
Section headers are created by underlining (and optionally overlining) the section title with a punctuation character, at least as long as the text.

Normally, there are no heading levels assigned to certain characters as the structure is determined from the succession of headings.
However, this convention is used:
* # with overline, for parts
* * with overline, for chapters
* =, for sections
* -, for subsections
* ^, for subsubsections
* ", for paragraphs

Lists
-----

* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

* this is
* a list

  * with a nested list
  * and some subitems

* and here the parent list continues

And below a definition list:

term (up to a line of text)
   Definition of the term, which must be indented

   and can even consist of multiple paragraphs

next term
   Description.

Code blocks
-----------

Code is introduced by ending a paragraph with the special marker ::. The code block must be indented (and, like all paragraphs, separated from the surrounding ones by blank lines):

This is a normal text paragraph. The next paragraph is a code sample::

   It is not processed in any way, except
   that the indentation is removed.

   It can span multiple lines.

This is a normal text paragraph again.

Code can also be created with directive code followed by the language. Below an example of Python code:

.. code:: python

  def my_function():
      "just a test"
      print 8/2

Line breaks
-----------

| These lines are
| broken exactly like in
| the source file.


Comments
--------

Every explicit markup block with `..` which isn’t a valid markup construct is regarded as a comment.:

.. This is a comment.

You can indent text after a comment start to form multiline comments:

..
   This whole indented block
   is a comment.

   Still in the comment.

Footnotes
---------
For footnotes, use `[#name]_` to mark the footnote location, and add the footnote body at the bottom of the document after a “Footnotes” rubric heading, like so:

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

Citations
---------
Citation usage is similar to footnote usage, but with a label that is not
numeric or begins with ``#``.

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

Another citation below:
.. [CIT2002] Another citation.

Hyperlinks
----------

External links
^^^^^^^^^^^^^^

This is a link to `OSM web page <http://osm.etsi.org/>`_

If the link text should be the web address, you don’t need special markup at all: http://osm.etsi.org

You can also separate the link and the target definition (ref), like this:

This is a paragraph that contains `a link`_.

.. _a link: http://osm.etsi.org/

Internal links
^^^^^^^^^^^^^^

Internal linking is done via a special reST role provided by Sphinx, see the
section on specific markup, :ref:`ref-role`.

Images
------

Below an image

.. image:: images/picture.jpg
   :width: 200px
   :height: 100px
   :scale: 50 %
   :alt: alternate text
   :align: right

And below a figure, with a caption.

.. figure:: images/picture.jpg
   :scale: 50 %
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.
