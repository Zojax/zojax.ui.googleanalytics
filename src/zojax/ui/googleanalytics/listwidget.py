##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from xml.sax import saxutils

from zope import schema, component

from z3c.form import converter
from z3c.form.browser import textarea
from z3c.form.widget import FieldWidget


class ListWidget(textarea.TextAreaWidget):

    rows = 6


class ListDataConverter(converter.BaseDataConverter):
    component.adapts(schema.interfaces.IList, ListWidget)

    def toWidgetValue(self, value):
        """See interfaces.IDataConverter"""
        if value is self.field.missing_value:
            return u''
        return '\n'.join(value)

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        return [elem.strip() for elem in value.split('\n') if elem]


def ListFieldWidget(field, request):
    return FieldWidget(field, ListWidget(request))
