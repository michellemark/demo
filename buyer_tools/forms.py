from django.forms import Form, CharField, ChoiceField, IntegerField, SelectMultiple, MultipleChoiceField

from buyer_tools.templatetags.utility_tags import money


class BuyerSearchForm(Form):
    DEFAULT_SELECTED = "default"
    DEFAULT_VIEW = "Any"
    ACTIVE = "Active"
    PENDING = "Pending"
    CLOSED = "Closed"
    STATUS_CHOICES = (
        (DEFAULT_SELECTED, DEFAULT_VIEW),
        (ACTIVE, ACTIVE),
        (PENDING, PENDING),
        (CLOSED, CLOSED)
    )
    RESIDENTIAL = "residential"
    RENTAL = "rental"
    MULTI_FAMILY = "multifamily"
    TYPE_CHOICES = (
        (DEFAULT_SELECTED, DEFAULT_VIEW),
        (RESIDENTIAL, RESIDENTIAL),
        (RENTAL, RENTAL),
        (MULTI_FAMILY, "multi-family")
    )
    TOWN_HOUSE = "townhouse"
    TIME_SHARE = "timeshare"
    TRIPLEX = "triplex"
    MANUFACTURED_ON_LAND = "manufacturedonland"
    SUBTYPE_CHOICES = (
        (DEFAULT_SELECTED, DEFAULT_VIEW),
        (TOWN_HOUSE, TOWN_HOUSE),
        (TIME_SHARE, TIME_SHARE),
        (TRIPLEX, TRIPLEX),
        (MANUFACTURED_ON_LAND, "manufactured on land")
    )
    TEN_TH = 10000
    TWENTY_TH = 20000
    THIRTY_TH = 30000
    FOURTY_TH = 40000
    FIFTY_TH = 50000
    SIXTY_TH = 60000
    SEVENTY_TH = 70000
    EIGHTY_TH = 80000
    NINTY_TH = 90000
    ONE_HUNDRED_TH = 100000
    ONE_TEN_TH = 110000
    ONE_TWENTY_TH = 120000
    ONE_THIRTY_TH = 130000
    ONE_FOURTY_TH = 140000
    ONE_FIFTY_TH = 150000
    ONE_SIXTY_TH = 160000
    ONE_SEVENTY_TH = 170000
    ONE_EIGHTY_TH = 180000
    ONE_NINTY_TH = 190000
    TWO_HUNDRED_TH = 200000
    TW_TEN_TH = 210000
    TWO_TWENTY_TH = 220000
    TWO_THIRTY_TH = 230000
    TWO_FOURTY_TH = 240000
    TWO_FIFTY_TH = 250000
    TWO_SIXTY_TH = 260000
    TWO_SEVENTY_TH = 270000
    TWO_EIGHTY_TH = 280000
    TWO_NINTY_TH = 290000
    THREE_HUNDRED_TH = 300000
    PRICE_CHOICES = (
        (DEFAULT_SELECTED, money(DEFAULT_VIEW)),
        (ONE_HUNDRED_TH, money(ONE_HUNDRED_TH)),
        (ONE_TEN_TH, money(ONE_TEN_TH)),
        (ONE_TWENTY_TH, money(ONE_TWENTY_TH)),
        (ONE_THIRTY_TH, money(ONE_THIRTY_TH)),
        (ONE_FOURTY_TH, money(ONE_FOURTY_TH)),
        (ONE_FIFTY_TH, money(ONE_FIFTY_TH)),
        (ONE_SIXTY_TH, money(ONE_SIXTY_TH)),
        (ONE_SEVENTY_TH, money(ONE_SEVENTY_TH)),
        (ONE_EIGHTY_TH, money(ONE_EIGHTY_TH)),
        (ONE_NINTY_TH, money(ONE_NINTY_TH)),
        (TWO_HUNDRED_TH, money(TWO_HUNDRED_TH)),
        (TW_TEN_TH, money(TW_TEN_TH)),
        (TWO_TWENTY_TH, money(TWO_TWENTY_TH)),
        (TWO_THIRTY_TH, money(TWO_THIRTY_TH)),
        (TWO_FOURTY_TH, money(TWO_FOURTY_TH)),
        (TWO_FIFTY_TH, money(TWO_FIFTY_TH)),
        (TWO_SIXTY_TH, money(TWO_SIXTY_TH)),
        (TWO_SEVENTY_TH, money(TWO_SEVENTY_TH)),
        (TWO_EIGHTY_TH, money(TWO_EIGHTY_TH)),
        (TWO_NINTY_TH, money(TWO_NINTY_TH)),
        (THREE_HUNDRED_TH, money(THREE_HUNDRED_TH))
    )
    THIRTIES = 1930
    FOURTIES = 1940
    FIFTIES = 1950
    SIXTIES = 1960
    SEVENTIES = 1970
    EIGHTIES = 1980
    NINTIES = 1990
    TW_TH = 2000
    TW_TEN_TH = 2010
    TW_FIFTEEN_TH = 2015
    TW_SIXTEEN_TH = 2016
    TW_SEVENTEEN_TH = 2017
    TW_EIGHTEEN_TH = 2018
    TW_NINTEEN_TH = 2019
    YEAR_CHOICES = (
        (DEFAULT_SELECTED, DEFAULT_VIEW),
        (THIRTIES, THIRTIES),
        (FOURTIES, FOURTIES),
        (FIFTIES, FIFTIES),
        (SIXTIES, SIXTIES),
        (SEVENTIES, SEVENTIES),
        (EIGHTIES, EIGHTIES),
        (NINTIES, NINTIES),
        (TW_TH, TW_TH),
        (TW_TEN_TH, TW_TEN_TH),
        (TW_FIFTEEN_TH, TW_FIFTEEN_TH),
        (TW_EIGHTEEN_TH, TW_EIGHTEEN_TH),
        (TW_NINTEEN_TH, TW_NINTEEN_TH)
    )
    TRUE = "true"
    FALSE = "false"
    WATER_CHOICES = (
        (DEFAULT_SELECTED, DEFAULT_VIEW),
        (TRUE, TRUE),
        (FALSE, FALSE),
    )
    ASSOCIATION = "association"
    AGREEMENT = "agreement"
    GARAGE_SPACES = "garageSpaces"
    MAINTENANCE_EXPENSE = "maintenanceExpense"
    PARKING = "parking"
    POOL = "pool"
    TAX_ANNUAL_AMT = "taxAnnualAmount"
    TAX_YEAR = "taxYear"
    ROOMS = "rooms"
    INCLUDE_CHOICES = (
        (DEFAULT_SELECTED, DEFAULT_VIEW),
        (ASSOCIATION, ASSOCIATION),
        (AGREEMENT, AGREEMENT),
        (GARAGE_SPACES, GARAGE_SPACES),
        (MAINTENANCE_EXPENSE, MAINTENANCE_EXPENSE),
        (PARKING, PARKING),
        (POOL, POOL),
        (TAX_ANNUAL_AMT, TAX_ANNUAL_AMT),
        (TAX_YEAR, TAX_YEAR),
        (ROOMS, ROOMS)
    )
    keywords = CharField(max_length=100, required=False,
                         label="Keywords, comma separated")
    status = ChoiceField(choices=STATUS_CHOICES, required=False)
    property_type = ChoiceField(choices=TYPE_CHOICES, required=False)
    subtype = ChoiceField(choices=SUBTYPE_CHOICES, required=False)
    agent = CharField(max_length=20, required=False)
    sales_agent = CharField(max_length=20, required=False)
    brokers = CharField(max_length=50, required=False)
    min_price = ChoiceField(choices=PRICE_CHOICES, required=False)
    max_price = ChoiceField(choices=PRICE_CHOICES, required=False)
    min_area = IntegerField(label="Min Square Footage", required=False)
    max_area = IntegerField(label="Max Square Footage", required=False)
    min_baths = IntegerField(localize=True, required=False)
    max_baths = IntegerField(localize=True, required=False)
    min_beds = IntegerField(localize=True, required=False)
    max_beds = IntegerField(localize=True, required=False)
    max_dom = IntegerField(label="Days on Market", localize=True, required=False)
    min_year = ChoiceField(choices=YEAR_CHOICES, required=False)
    max_year = ChoiceField(choices=YEAR_CHOICES, required=False)
    min_acres = IntegerField(label="Min Acres", localize=True, required=False)
    max_acres = IntegerField(label="Max Acres", localize=True, required=False)
    min_garage = IntegerField(label="Min Garage Spaces", localize=True, required=False)
    max_garage = IntegerField(label="Max Garage Spaces", localize=True, required=False)
    postal_codes = CharField(label="Postal Codes, comma separated", required=False)
    features = CharField(label="Features, comma separated", required=False)
    exterior_features = CharField(label="Exterior features, comma separated", required=False)
    water = ChoiceField(choices=WATER_CHOICES, required=False)
    neighborhoods = CharField(label="Neighborhoods, comma separated", required=False)
    cities = CharField(label="Cities, comma separated", required=False)
    counties = CharField(label="Counties, comma separated", required=False)
    include = MultipleChoiceField(label="Include these extra fields",
                                  choices=INCLUDE_CHOICES,
                                  required=False)

    def clean(self):
        super().clean()
        cleaned_data = {}

        if len(self.cleaned_data.get("keywords")):
            cleaned_data["keywords"] = [x.strip() for x in self.cleaned_data.get("keywords").split(",")]

        status = self.cleaned_data.get("status")

        if status != self.DEFAULT_SELECTED:
            cleaned_data["status"] = list(status)

        property_type = self.cleaned_data.get("property_type")

        if property_type != self.DEFAULT_SELECTED:
            cleaned_data["property_type"] = list(property_type)

        subtype = self.cleaned_data.get("subtype")

        if subtype != self.DEFAULT_SELECTED:
            cleaned_data["subtype"] = list(subtype)

        if len(self.cleaned_data.get("agent")):
            cleaned_data["agent"] = self.cleaned_data.get("agent")

        if len(self.cleaned_data.get("sales_agent")):
            cleaned_data["sales_agent"] = self.cleaned_data.get("sales_agent")

        brokers = self.cleaned_data.get("brokers")

        if len(brokers):
            cleaned_data["brokers"] = [x.strip() for x in self.cleaned_data.get("brokers").split(",")]

        min_price = self.cleaned_data.get("min_price")

        if min_price != self.DEFAULT_SELECTED:
            cleaned_data["min_price"] = min_price

        max_price = self.cleaned_data.get("max_price")

        if max_price != self.DEFAULT_SELECTED:
            cleaned_data["max_price"] = max_price

        min_area = self.cleaned_data.get("min_area")

        if min_area:
            cleaned_data["min_area"] = min_area

        max_area = self.cleaned_data.get("max_area")

        if max_area:
            cleaned_data["max_area"] = max_area

        min_baths = self.cleaned_data.get("min_baths")

        if min_baths:
            cleaned_data["min_baths"] = min_area

        max_baths = self.cleaned_data.get("max_baths")

        if max_baths:
            cleaned_data["max_baths"] = max_baths

        min_beds = self.cleaned_data.get("min_beds")

        if min_beds:
            cleaned_data["min_beds"] = min_beds

        max_beds = self.cleaned_data.get("max_beds")

        if max_beds:
            cleaned_data["max_beds"] = max_beds

        max_dom = self.cleaned_data.get("max_dom")

        if max_dom:
            cleaned_data["max_dom"] = max_dom

        min_year = self.cleaned_data.get("min_year")

        if min_year != self.DEFAULT_SELECTED:
            cleaned_data["min_year"] = min_year

        max_year = self.cleaned_data.get("max_year")

        if max_year != self.DEFAULT_SELECTED:
            cleaned_data["max_year"] = max_year

        min_acres = self.cleaned_data.get("min_acres")

        if min_acres:
            cleaned_data["min_acres"] = min_acres

        max_acres = self.cleaned_data.get("max_acres")

        if max_acres:
            cleaned_data["max_acres"] = max_acres

        min_garage = self.cleaned_data.get("min_garage")

        if min_garage:
            cleaned_data["min_garage"] = min_garage

        max_garage = self.cleaned_data.get("max_garage")

        if max_garage:
            cleaned_data["max_garage"] = max_garage

        postal_codes = self.cleaned_data.get("postal_codes")

        if len(postal_codes):
            cleaned_data["postal_codes"] = [x.strip() for x in self.cleaned_data.get("postal_codes").split(",")]

        features = self.cleaned_data.get("features")

        if len(features):
            cleaned_data["features"] = [x.strip() for x in self.cleaned_data.get("features").split(",")]

        exterior_features = self.cleaned_data.get("exterior_features")

        if len(exterior_features):
            cleaned_data["exterior_features"] = [x.strip() for x in self.cleaned_data.get("exterior_features").split(",")]

        water = self.cleaned_data.get("water")

        if water != self.DEFAULT_SELECTED:
            cleaned_data["water"] = water

        neighborhoods = self.cleaned_data.get("neighborhoods")

        if len(neighborhoods):
            cleaned_data["neighborhoods"] = [x.strip() for x in self.cleaned_data.get("neighborhoods").split(",")]

        cities = self.cleaned_data.get("cities")

        if len(cities):
            cleaned_data["cities"] = [x.strip() for x in self.cleaned_data.get("cities").split(",")]

        counties = self.cleaned_data.get("counties")

        if len(counties):
            cleaned_data["counties"] = [x.strip() for x in self.cleaned_data.get("counties").split(",")]

        include = self.cleaned_data.get("include")

        if include != self.DEFAULT_SELECTED:
            cleaned_data["include"] = [x.strip() for x in include]

        return cleaned_data
