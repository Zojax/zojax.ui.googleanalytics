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
""" google ads portlet interfaces

$Id$
"""
from zope import schema, interface
from zope.i18nmessageid import MessageFactory
from zojax.widget.list import SimpleList

_ = MessageFactory('zojax.ui.googleanalytics')


class IGoogleAnalyticsHeaders(interface.Interface):
    """ google analytics headers """


class IGoogleAnalytics(interface.Interface):
    """ configlet interface """

    enabled = schema.Bool(
        title = _(u'Enabled'),
        description = _(u'Enable google analytics for this site.'),
        default = False,
        required = False)

    code = SimpleList(
        title = _(u'Tracking code'),
        description = _(u'Check your google analytics account for tracking code.'),
        value_type = schema.TextLine(),
        default = [],
        required = True)
