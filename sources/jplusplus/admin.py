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
# Last mod : 14-Apr-2014
# -----------------------------------------------------------------------------

from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import WhatWeDo, Office, Project
from adminsortable.admin import SortableAdminMixin

class WhatWeDoAdmin(SortableAdminMixin, TranslatableAdmin):
    pass

class OfficeAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(SortableAdminMixin, TranslatableAdmin):
    def __init__(self, *args, **kwargs):
    	# for prepopulate fields
    	# See : https://github.com/KristianOellegaard/django-hvad/issues/10#issuecomment-5572524
        super(ProjectAdmin, self).__init__(*args, **kwargs)
        self.prepopulated_fields = {'slug': ('title',)}

admin.site.register(WhatWeDo, WhatWeDoAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Project, ProjectAdmin)

# EOF
