import json
import logging
import os
import uuid

import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        payload = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    order = {
        "orderId": str(uuid.uuid4()),
        "customerId": payload.get("customerId"),
        "items": payload.get("items", []),
        "status": "created",
    }

    connection = os.environ["SERVICE_BUS_CONNECTION"]
    topic_name = os.environ.get("ORDER_TOPIC_NAME", "orders")

    with ServiceBusClient.from_connection_string(connection) as client:
        sender = client.get_topic_sender(topic_name)
        with sender:
            sender.send_messages(ServiceBusMessage(json.dumps(order)))

    logging.info("Order created: %s", order["orderId"])
    return func.HttpResponse(json.dumps(order), mimetype="application/json", status_code=202)

