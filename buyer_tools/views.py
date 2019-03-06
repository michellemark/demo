from django.shortcuts import render
from django.views.generic import TemplateView

from buyer_tools.forms import BuyerSearchForm
from buyer_tools.simply_rets import SimplyRets


class BuyerSearchView(TemplateView):
    template_name = "buyer_search.html"
    search_form = BuyerSearchForm

    def get_context_data(self, **kwargs):
        context = super(BuyerSearchView, self).get_context_data(**kwargs)
        context['page_title'] = "Buyer search simple proof of concept"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context["form"] = self.search_form()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context["form"] = self.search_form(request.POST)

        if context["form"].is_valid():
            context["search_results"] = SimplyRets().get_properties(context["form"].cleaned_data)

        return render(request, self.template_name, context)


