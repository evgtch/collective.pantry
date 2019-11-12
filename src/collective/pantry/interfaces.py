# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.pantry import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.app.textfield import RichText


PANTRY_DIRECTORY = 'pantry'


class ICollectivePantryLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ISnippet(Interface):

    title = schema.TextLine(
        title=_(u'Title'),
        required=True,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    body = RichText(
        title=_(u'Body'),
        required=False,
    )
