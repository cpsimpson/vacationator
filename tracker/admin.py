from django.contrib import admin
from tracker.models import Allotment, AllotmentType, AllotmentTypeOverride, \
    RequestState, Request, ActionRecord


admin.site.register(Allotment)
admin.site.register(AllotmentType)
admin.site.register(AllotmentTypeOverride)
admin.site.register(RequestState)
admin.site.register(Request)
admin.site.register(ActionRecord)
