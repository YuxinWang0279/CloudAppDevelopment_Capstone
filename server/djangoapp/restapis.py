import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth
from .models import CarDealer,CarMake,CarModel,DealerReview
# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {}".format(url))
    try:
        response = requests.get(url, headers={'Accept': 'application/json'},params = kwargs)
    except:
        print("Network exception occurred")
    status_code = response.status_code
    print("with status {}".format(status_code))
    json_data = json.loads(response.text)
    return json_data
# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
'''
def post_request(url,**kwargs):
    print(kwargs)
    print("POST from {}".format(url))
    try:
        response = requests.post(url, params=kwargs, json=payload)
    except:
        print("Network exception occurred")
    status_code = response.status_code
    print("with status {}".format(status_code))
    json_data = json.loads(response.text)
    return json_data
'''
# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url,**kwargs):
    results = []

    json_result = get_request(url)
    if json_result:
        dealers = json_result["rows"]
        for dealer in dealers:
            if 'address' not in dealer:
                continue
            dealer_obj = dealer_obj = CarDealer(address=dealer['address'], city=dealer["city"], full_name=dealer["full_name"],
                                   id=dealer["id"], lat=dealer["lat"], long=dealer["long"],
                                   short_name=dealer["short_name"],
                                   st=dealer["st"], state = dealer["state"],zip=dealer["zip"])
            results.append(dealer_obj)
    return results
# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



def get_dealer_reviews_from_cf(url,dealerId=None):
    results = []
    if dealerId!=None:
        json_result = get_request(url,dealerId = dealerId)
    else:
        json_result = get_request(url)
    if json_result:
        print(json_result)
        dealers = json_result["rows"]
        for dealer in dealers:
            if 'address' not in dealer:
                continue
            dealer_obj = DealerReview(dealership=dealer["dealership"],name = dealer['name'],purchase= dealer['purchase']
            ,review=dealer['review'],purchase_date=dealer['purchase_date'],car_make=dealer['car_make']
            ,car_model=dealer['car_model'],car_year=dealer['car_year'],sentiment=dealer['sentiment'],id = dealer['id'])
            
            results.append(dealer_obj)
    return results


