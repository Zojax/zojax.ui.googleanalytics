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
from zope import component  # , interface
from zope.component import getUtility
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

        tracker_create = ""
        tracker_send = ""
        for idx, code in enumerate(self.configlet.code):
            if idx > 0:
                tracker_create = ", {'name': 'newTracker%s'}" % idx
                tracker_send = "newTracker%s." % idx

            js.insert(idx, jstracker_create % (code, tracker_create))
            js.insert(idx + idx + 1, jstracker_send % (tracker_send))

        return jscode % '\n'.join(js)

    def isAvailable(self):
        return self.configlet.enabled and self.configlet.code

    @cache('pageelement:portal.ui.googleanalytics', GoogleAnalyticsTag)
    def updateAndRender(self):
        return super(GoogleAnalyticsPageElement, self).updateAndRender()


jscode = """<script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

%s

    </script>"""

jstracker_create = "      ga('create', '%s', 'auto'%s);"

jstracker_send = "      ga('%ssend', 'pageview');"


@component.adapter(IGoogleAnalytics, IObjectModifiedEvent)
def configletChangeHandler(configlet, ev):
    GoogleAnalyticsTag.update()
