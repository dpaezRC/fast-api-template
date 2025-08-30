from fastapi import APIRouter

router = APIRouter(prefix="/products")


@router.get(
    "/",
    tags=["Products"],
    summary="List all products",
    description="Returns a list of all products.",
)
def list_products():
    return [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]


@router.post(
    "/",
    tags=["Products"],
    summary="Create a new product",
    description="Creates a new product.",
)
def create_product(product: dict):
    return {"id": 3, "name": product["name"]}


@router.put(
    "/{product_id}",
    tags=["Products"],
    summary="Update an existing product",
    description="Updates an existing product.",
)
def update_product(product_id: int, product: dict):
    return {"id": product_id, "name": product["name"]}


@router.delete(
    "/{product_id}",
    tags=["Products"],
    summary="Delete an existing product",
    description="Deletes an existing product.",
)
def delete_product(product_id: int):
    return {"id": product_id, "status": "deleted"}
