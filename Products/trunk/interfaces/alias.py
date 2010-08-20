# -*- coding: utf-8 -*-
# $Id$

from zope.interface import Interface

class IAlias(Interface):
    """Marker interface for the type"""
    pass

class IAliasTool(Interface):
    """Marker interface for SimpleAlias tool"""

class IAliasLinkedTo(Interface):
    """
    Marker interface for objects that Alias' link to.
    """
    pass

__all__ = ('IAlias', 'IAliasTool','IAliasLinkedTo')