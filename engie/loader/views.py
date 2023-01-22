from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
import pandas as pd
import json

from django.http import HttpResponse, JsonResponse

from .serializers import PayloadSerializer, ResultSerializer

@extend_schema(
        request=PayloadSerializer,
        responses={200: ResultSerializer,
                   400: JsonResponse},
        methods=["POST"]
    )
@api_view(['POST'])
def calculThePower(request):
    """
    End point to calculate the powerplant list
    Take a JSON as input
    Return a JSON as output
    """

    # Clean the JSON
    cleaned_json = clean_json(request.data)
    
    payload = PayloadSerializer(data=cleaned_json)

    if payload.is_valid():
        load = int(payload.data["load"])
        fuels = payload.data["fuels"]
        powerplants = payload.data["powerplants"]

        response = compute_best_powerplants(load, fuels, powerplants)

        return HttpResponse(response, status=200)
    
    return JsonResponse(payload.errors, status=400)

def clean_json(input_json):
    raw_json = str(input_json)
    raw_json = raw_json.replace("gas(euro/MWh)", "gas")
    raw_json = raw_json.replace("kerosine(euro/MWh)", "kerosine")
    raw_json = raw_json.replace("co2(euro/ton)", "co2")
    raw_json = raw_json.replace("wind(%)", "wind_percentage")
    raw_json = raw_json.replace("\'", "\"")
    
    return json.loads(raw_json)

def compute_best_powerplants(load, fuels, powerplants):
    # Create a dataframe with the powerplants
    df = pd.DataFrame(powerplants)

    # add the cost column: 1MW of electricity cost X euros
    df["cost"] = df.apply(lambda row: get_cost(row["type"], row["efficiency"], fuels), axis=1)
    
    df.sort_values(by=["cost", "pmin"], ascending=True, inplace=True)
    df.reset_index(drop=True, inplace=True)
    # add the p column with the default value = 0
    df["p"] = 0

    # add the p column: the powerplant will produce X MW of electricity
    for row in df.itertuples():
        df.at[row[0], "p"] = get_p(row[4], row[5], load)
        load -= df.at[row[0], "p"]
        if load <= 0:
            break

    return df[["name", "p"]].to_json(orient="records")
   
def get_cost(type, efficiency, fuels):
    if type == "gasfired":
        return fuels["gas"] / efficiency
    elif type == "turbojet":
        return fuels["kerosine"] / efficiency
    elif type == "windturbine":
        return 0
    else:
        return 0

def get_p(pmin, pmax, load):
    print(pmin, pmax, load)
    if load <= 0:
        return 0
    elif load > pmax:
        return pmax
    elif load < pmin:
        return 0
    else:
        return load

