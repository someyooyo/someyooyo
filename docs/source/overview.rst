Overview
========

Requirements
------------

Powerline requires Python 2.7 to work.

Vim plugin requirements
^^^^^^^^^^^^^^^^^^^^^^^

The vim plugin requires a vim version with Python 2.7 support compiled in.  
You can check if your vim supports Python 2 by running ``vim --version 
| grep +python``.

Vim version 7.3.661 or newer is recommended for performance reasons.

Installation
------------

Powerline is intended to be installed as a system-wide Python package that 
can be easily included in other projects.

Powerline is available `on the AUR 
<https://aur.archlinux.org/packages/powerline-git/>`_ for Arch Linux users.

.. note:: This project is currently unavailable on the PyPI due to a naming 
   conflict with an unrelated project.

Usage
-----

Vim usage
^^^^^^^^^

If Powerline is installed as a system-wide Python package, you can enable 
the plugin by adding the following line to your ``vimrc``::

    python import powerline.plugin.vim.load_vim_plugin

If Powerline is installed outside Python's search path (e.g. by having the 
git repo in your dotfiles folder) you'll have to source the vim plugin file 
with an absolute path to the plugin location.

Add the following line to your ``vimrc``, where ``{path}`` is the path to 
the main Powerline project folder::

    source {path}/powerline/plugin/vim/powerline.vim
