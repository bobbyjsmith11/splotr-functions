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

    net = network.Network()
    net.read_touchstone_string(d['filedata'], d['filename'])
    
    
    d = { 'f':                  net.f.tolist(),
          'number_of_ports':    int(net.nports)
          }
    for j in range(net.nports):         # j is second port
        for k in range(net.nports):      # k is first port
            d["s"+str(j+1)+str(k+1)+"db"] = net.s_db[:,j,k].tolist()
    
    response = {
        "statusCode": 200,
        "body": json.dumps(d)
    }
    return response

