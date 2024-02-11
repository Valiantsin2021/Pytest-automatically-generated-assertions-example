import requests

def get_request(base_url):
    response = requests.get(f"{base_url}", verify=False)
    return response
def get_request_qp(base_url, qp):
    response = requests.get(f"{base_url}/{qp}", verify=False)
    return response

def post_request(base_url, body, token):
    response = requests.post(f"{base_url}", data=body, headers=token, verify=False)
    return response
