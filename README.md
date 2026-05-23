# Serverless Event-Driven Order System on Azure

## Goal

Build a serverless order-processing platform using asynchronous messaging and event-driven workflows.

## Azure Services

- Azure Functions
- Azure Service Bus
- Azure Event Grid
- Azure Cosmos DB
- Azure Storage Account
- Application Insights

## DevOps Skills Demonstrated

- Event-driven architecture
- Serverless deployment automation
- Queue-based decoupling
- Observability with Application Insights
- Infrastructure as Code
- Cloud-native retry and dead-letter patterns

## Suggested Flow

```text
order-api -> service-bus-topic -> payment-function -> inventory-function -> event-grid -> notification-function
```

