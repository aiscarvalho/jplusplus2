#!/usr/bin/env python
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 14-Apr-2014
# Last mod : 15-Apr-2014
# -----------------------------------------------------------------------------
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import WhatWeDo, Project, ProjectPluginModel

class WhatWeDoPlugin(CMSPluginBase):
    name            = _("What we do")
    render_template = "jplusplus/whatwedo.html"

    def render(self, context, instance, placeholder):
        items = WhatWeDo.objects.all()
        context.update({
            'instance' : instance,
            'items'    : items,
        })
        return context 

class ProjectsPlugin(CMSPluginBase):
    model           = ProjectPluginModel
    name            = _("J++ Projects")
    render_template = "jplusplus/partials/projects.html"

    def render(self, context, instance, placeholder):
    	# filter projects by offices, retrieve with translations
        ln               = context.get("LANGUAGE_CODE")
        selected_offices = instance.offices.all()
        if selected_offices:
        	items = Project.objects.language(ln).filter(offices__in=selected_offices)
        else:
        	items = Project.objects.language(ln).all()
        # add to context
        context.update({
            'instance' : instance,
            'projects' : items,
        })
        return context
 
plugin_pool.register_plugin(WhatWeDoPlugin)
plugin_pool.register_plugin(ProjectsPlugin)

# EOF