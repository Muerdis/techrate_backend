import csv

from django.contrib import admin
from django.http import HttpResponse
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from project.models import Token, Blockchain


def download_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=tokens.csv"

    writer = csv.writer(response)

    fields = [
        "created", "modified",
        "name", "score", "blockchain", "audit", "twitter",
        "website", "audit_date", "is_partner", "contract_address"
    ]

    writer.writerow(fields)
    for item in queryset:
        data = []
        for field in fields:
            if field == "blockchain":
                blockchain = getattr(item, field, None)
                if blockchain:
                    data.append(getattr(blockchain, "name"))
                else:
                    data.append("")
            else:
                data.append(getattr(item, field, ""))

        writer.writerow(data)

    return response


class TokenAdmin(admin.ModelAdmin, DynamicArrayMixin):
    actions = [download_csv]


admin.site.register(Blockchain)
admin.site.register(Token, TokenAdmin)
