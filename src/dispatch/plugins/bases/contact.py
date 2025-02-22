"""
.. module: dispatch.plugins.bases.contact
    :platform: Unix
    :copyright: (c) 2019 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Kevin Glisson <kglisson@netflix.com>
"""
from dispatch.plugins.base import Plugin
from dispatch.models import PluginOptionModel


class ContactPlugin(Plugin):
    type = "contact"
    _schema = PluginOptionModel

    def get(self, key, **kwargs):
        raise NotImplementedError

    def create(self, key, **kwargs):
        raise NotImplementedError

    def update(self, key, **kwargs):
        raise NotImplementedError

    def delete(self, key, **kwargs):
        raise NotImplementedError
