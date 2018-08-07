from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
# from polls_cms_integration.models import SerialPluginModel
from .models import SerialPluginModel
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin  # register the plugin
class SerialPluginPublisher(CMSPluginBase):
    model = SerialPluginModel  # model where plugin data are saved
    module = _("serials")
    name = _("Serial Plugin")  # name of the plugin in the interface
    render_template = "plugin/serial_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context