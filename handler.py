from splotr import network
import json
import os

def hello_splotr(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }


    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

    return response

def callGetLogMag(event, context):
    """
    """
    try:
        d = json.loads(event['body'])
    except:
        d = {
            "message": "Exception!",
            "input": event
        }

    # ftemp = open("temp.s2p", "w")
    # ftemp.write(d['raw_text'])
    # ftemp.close
    # fname = ftemp.name
    # net = network.Network(fname)
    # os.remove(fname)
    # d_ret = {}
    # d_ret['comments'] = net.comments 
    
    d_ret = d['raw_text']
    
    response = {
        "statusCode": 200,
        "body": json.dumps(d_ret)
    }
    return response

# def prototype_function(event, context):
# 
#     try:
#         d = json.loads(event['body'])
#     except:
#         d = {
#             "message": "Exception!",
#             "input": event
#         }
# 
#     d_ret = some_function(d)
#     
#     response = {
#         "statusCode": 200,
#         "body": json.dumps(d_ret)
#     }
#     return response
