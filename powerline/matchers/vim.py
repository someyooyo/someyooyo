# -*- coding: utf-8 -*-

from __future__ import absolute_import

import vim


def help():
	return bool(int(vim.eval('&buftype is# "help"')))
