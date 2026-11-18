from fastapi import FastAPI, Request
import uvicorn

app=FastAPI(
    title="Swiggy order System",
    description=(
        "Internal api for managing orders"
        "handling order placement, tracking, and status updates"
    ),
    version="1.2.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json" 
)

@app.get('/')
def read_root():
    """Root endpoint to check the health of the application."""
    # fastApi convert this dict into json
    return {"message":"welcome to swiggy order service","status":"healthy"}

@app.get("/about")
def about():
    """retrun api metadata"""
    return {
        "title": app.title,
        "description": app.description,
        "version": app.version,
        "docs_url": app.docs_url,
        "redoc_url": app.redoc_url,
        "openapi_url": app.openapi_url
    }

@app.get("/orders")
def get_orders():
    """Endpoint to retrieve a list of orders."""
    # Placeholder for order retrieval logic
    return {"orders": [
        {"id": 1, "item": "Pizza", "quantity": 2, "status": "delivered"},
        {"id": 2, "item": "Burger", "quantity": 1, "status": "in progress"},
        {"id": 3, "item": "Sushi", "quantity": 3, "status": "pending"}
    ]}

@app.post("/orders/status")
def order_status():
    """Endpoint to update the status of an order."""
    # Placeholder for order status update logic
    return {
        "total_orders": 3,
        "top_city": "New York",
        "top_item": "Pizza",
    }

@app.get("/debug/request-info")
def request_info(request: Request):
    """Endpoint to retrieve request information for debugging purposes."""
    return {
        "client_host": request.client.host,
        "client_port": request.client.port,
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }

@app.get(
    "/orders/active",
    summary="Get active orders",
    description=(
        "Retrieve a list of active orders that are currently being processed."
        " This endpoint provides details about each active order, including its ID, item name, quantity, and current status."
        ),
    tags=["Orders"],
    response_description="A list of active orders with their details.",
    deprecated=False,
    )
def get_active_orders():
    """Endpoint to retrieve a list of active orders."""
    # Placeholder for active order retrieval logic
    return {"active_orders": [
        {"id": 2, "item": "Burger", "quantity": 1, "status": "in progress"},
        {"id": 3, "item": "Sushi", "quantity": 3, "status": "pending"}
    ]}  