import json

def get_default_headers():
    return {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",  # Allow all origins
        "Access-Control-Allow-Methods": "GET",  # Allowed HTTP method
        "Access-Control-Allow-Headers": "Content-Type, Authorization"  # Allowed headers
    }

# Move this to JS
# common_status_dict = {
#     100: "Continue",
#     101: "Switching Protocols",
#     200: "OK",
#     201: "Created",
#     202: "Accepted",
#     204: "No Content",
#     300: "Multiple Choices",
#     301: "Moved Permanently",
#     302: "Found",
#     304: "Not Modified",
#     400: "Bad Request",
#     401: "Unauthorized",
#     403: "Forbidden",
#     404: "Not Found",
#     405: "Method Not Allowed",
#     409: "Conflict",
#     413: "Payload Too Large",
#     429: "Too Many Requests",
#     500: "Internal Server Error",
#     501: "Not Implemented",
#     503: "Service Unavailable",
# }


def build_response(
    status_code: int = 200,
    error_message: str = "",
    headers: dict = None,
    body_data: dict = None,
    body_alternative_message: str = ""
):
    response = {
        "statusCode": status_code,
        "errorMessage": error_message,
        "headers": headers if headers is not None else get_default_headers(),
        "body": json.dumps({
            "bodyData": body_data if body_data is not None else {},
            "bodyAlternativeMessage": body_alternative_message,
        })
    }
    return response


# examples
# suppose detect parameter is missing
# 400 = Bad request, implement in JS
response = build_response(status_code=400)
print(response)
# {'statusCode': 400, 'errorMessage': '', 'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*',
# 'Access-Control-Allow-Methods': 'GET', 'Access-Control-Allow-Headers': 'Content-Type, Authorization'}, 'body': '{"bodyData": {}, "bodyAlternativeMessage": ""}'}


# suppose try to establish connection to a data source but fail
# 500 = Internal Server Error, implement in JS
response = build_response(status_code=500, error_message="Network unreachable")
print(response)
# {'statusCode': 500, 'errorMessage': 'Network unreachable', 'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*',
# 'Access-Control-Allow-Methods': 'GET', 'Access-Control-Allow-Headers': 'Content-Type, Authorization'}, 'body': '{"bodyData": {}, "bodyAlternativeMessage": ""}'}


# fetch successful and record found
body_data = {"boxlink": "www.bruh.com"}
response = build_response(body_data=body_data)
print(response)
# {'statusCode': 200, 'errorMessage': '', 'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET',
# 'Access-Control-Allow-Headers': 'Content-Type, Authorization'}, 'body': '{"bodyData": {"boxlink": "www.bruh.com"}, "bodyAlternativeMessage": ""}'}


# fetch successful but record not found
body_alternative_message = "boxlink not found"
response = build_response(body_alternative_message=body_alternative_message)
print(response)
# {'statusCode': 200, 'errorMessage': '', 'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET',
# 'Access-Control-Allow-Headers': 'Content-Type, Authorization'}, 'body': '{"bodyData": {}, "bodyAlternativeMessage": "boxlink not found"}'}

# JS comb
# if statusCode >= 400, then display red (statusCode, codeToDescription[statusCode], errorMessage)
# else if bodyAlternativeMessage is not "", then display yellow (bodyAlternativeMessage)
# else display bodyData