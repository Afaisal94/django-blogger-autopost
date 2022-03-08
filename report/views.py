from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Report
from django.views import View

class ReportIndex(LoginRequiredMixin, View):
    def get(self, request):
        reports = Report.objects.all()
        return render(request, 'report/index.html', {
            'reports': reports
        })


class ReportDelete(LoginRequiredMixin, View):
    def get(self, request, id):
        report = get_object_or_404(Report, id=id)
        report.delete()
        messages.success(request, 'Sukses Menghapus Report.')
        return HttpResponseRedirect(reverse('report-index'))