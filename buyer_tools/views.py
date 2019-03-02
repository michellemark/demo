import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from requests.auth import HTTPBasicAuth

from buyer_tools.forms import BuyerSearchForm
from gwenn_demo.settings.prod import SIMPLY_RETS_API_KEY, SIMPLY_RETS_API_SECRET


class BuyerSearchView(TemplateView):
    template_name = "buyer_search.html"
    search_form = BuyerSearchForm

    def make_rets_request(self, data, limit=500, offset=0):
        results = None
        url = "https://api.simplyrets.com/properties"
        parameters = {
            "limit": limit,
            "lastId": offset
        }

        if "keywords" in data:
            parameters["q"] = data.get("keywords")

        if "status" in data:
            parameters["status"] = data.get("status")

        if "property_type" in data:
            parameters["type"] = data.get("property_type")

        if "subtype" in data:
            parameters["subtype"] = data.get("subtype")

        if "agent" in data:
            parameters["agent"] = data.get("agent")

        if "sales_agent" in data:
            parameters["salesAgent"] = data.get("sales_agent")

        if "brokers" in data:
            parameters["brokers"] = data.get("brokers")

        if "min_price" in data:
            parameters["minprice"] = data.get("min_price")

        if "max_price" in data:
            parameters["maxprice"] = data.get("max_price")

        if "min_area" in data:
            parameters["minarea"] = data.get("min_area")

        if "max_area" in data:
            parameters["maxarea"] = data.get("max_area")

        if "min_baths" in data:
            parameters["minbaths"] = data.get("min_baths")

        if "max_baths" in data:
            parameters["maxbaths"] = data.get("max_baths")

        if "min_beds" in data:
            parameters["minbeds"] = data.get("min_beds")

        if "max_beds" in data:
            parameters["maxbeds"] = data.get("max_beds")

        if "max_dom" in data:
            parameters["maxdom"] = data.get("max_dom")

        if "min_year" in data:
            parameters["minyear"] = data.get("min_year")

        if "max_year" in data:
            parameters["maxyear"] = data.get("max_year")

        if "min_acres" in data:
            parameters["minacres"] = data.get("min_acres")

        if "max_acres" in data:
            parameters["maxacres"] = data.get("max_acres")

        if "min_garage" in data:
            parameters["minGarageSpaces"] = data.get("min_garage")

        if "max_garage" in data:
            parameters["maxGarageSpaces"] = data.get("max_garage")

        if "vendor" in data:
            parameters["vendor"] = data.get("vendor")

        if "postal_codes" in data:
            parameters["postalCodes"] = data.get("postal_codes")

        if "features" in data:
            parameters["features"] = data.get("features")

        if "exterior_features" in data:
            parameters["exteriorFeatures"] = data.get("exterior_features")

        if "water" in data:
            parameters["water"] = data.get("water")

        if "neighborhoods" in data:
            parameters["neighborhoods"] = data.get("neighborhoods")

        if "cities" in data:
            parameters["cities"] = data.get("cities")

        if "counties" in data:
            parameters["counties"] = data.get("counties")

        if "include" in data:
            parameters["include"] = data.get("include")

        if "sort" in data:
            parameters["sort"] = data.get("sort")

        if "count" in data:
            parameters["count"] = data.get("count")

        response = requests.get(url=url,
                                params=parameters,
                                auth=HTTPBasicAuth(SIMPLY_RETS_API_KEY, SIMPLY_RETS_API_SECRET))

        if response.ok:
            results = response.json()

        elif response.status_code == 400:
            results = {"error_message": "Bad Request"}
        elif response.status_code == 401:
            results = {"error_message": "Authentication Required"}
        elif response.status_code == 403:
            results = {"error_message": "Authorization Required"}
        elif response.status_code == 429:
            results = {"error_message": "Too Many Requests"}
        elif response.status_code == 500:
            results = {"error_message": "Internal Server Error"}

        return results

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
            context["search_results"] = self.make_rets_request(context["form"].cleaned_data)

        return render(request, self.template_name, context)


