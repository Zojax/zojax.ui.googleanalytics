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
from zope import interface, component
from zope.component import getUtility
from zope.traversing.browser import absoluteURL
from zope.app.component.hooks import getSite
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from zojax.cache.view import cache
from zojax.cache.tag import SiteTag

from interfaces import IGoogleAnalytics

GoogleAnalyticsTag = SiteTag('ui.googleanalytics')


class GoogleAnalyticsPageElement(object):

    def update(self):
        self.configlet = getUtility(IGoogleAnalytics)

    def render(self):
        js = []
        for code in self.configlet.code:
            js.append(jstracker%code)

        url = absoluteURL(getSite(), self.request)

        return jscode%url + '\n'.join(js)

    def isAvailable(self):
        return self.configlet.enabled and self.configlet.code

    @cache('pageelement:portal.ui.googleanalytics', GoogleAnalyticsTag)
    def updateAndRender(self):
        return super(GoogleAnalyticsPageElement, self).updateAndRender()


jscode = '<script type="text/javascript" src="%s/@@/google-analytics.js" type="text/javascript"></script>'

jstracker="""
<script type="text/javascript">
var pageTracker = _gat._getTracker("%s");
pageTracker._trackPageview();
</script>
"""

@component.adapter(IGoogleAnalytics, IObjectModifiedEvent)
def configletChangeHandler(configlet, ev):
    GoogleAnalyticsTag.update()
