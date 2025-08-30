from fastapi import APIRouter, HTTPException, status
from typing import List
from bson import ObjectId
from src.models.product import Product, Category

router = APIRouter(prefix="/products")


@router.get(
    "/",
    tags=["Products"],
    summary="List all products",
    description="Returns a list of all products.",
    response_model=List[Product],
)
async def list_products():
    """Obtiene todos los productos"""
    try:
        products = await Product.find_all().to_list()
        return products
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener productos: {str(e)}",
        )


@router.get(
    "/{product_id}",
    tags=["Products"],
    summary="Get a product by ID",
    description="Returns a single product by its ID.",
    response_model=Product,
)
async def get_product(product_id: str):
    """Obtiene un producto por su ID"""
    try:
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="ID de producto inválido",
            )

        product = await Product.get(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
            )
        return product
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener el producto: {str(e)}",
        )


@router.post(
    "/",
    tags=["Products"],
    summary="Create a new product",
    description="Creates a new product.",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(product_data: Product):
    """Crea un nuevo producto"""
    try:
        product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            category=product_data.category,
        )

        await product.insert()
        return product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear el producto: {str(e)}",
        )


@router.put(
    "/{product_id}",
    tags=["Products"],
    summary="Update an existing product",
    description="Updates an existing product.",
    response_model=Product,
)
async def update_product(product_id: str, product_data: Product):
    """Actualiza un producto existente"""
    try:
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="ID de producto inválido",
            )

        existing_product = await Product.get(product_id)
        if not existing_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
            )

        existing_product.name = product_data.name
        existing_product.description = product_data.description
        existing_product.price = product_data.price
        existing_product.category = product_data.category

        await existing_product.save()
        return existing_product
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el producto: {str(e)}",
        )


@router.patch(
    "/{product_id}",
    tags=["Products"],
    summary="Partially update an existing product",
    description="Partially updates an existing product.",
    response_model=Product,
)
async def patch_product(product_id: str, product_data: dict):
    """Actualiza parcialmente un producto existente"""
    try:
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="ID de producto inválido",
            )

        existing_product = await Product.get(product_id)
        if not existing_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
            )

        update_data = {k: v for k, v in product_data.items() if v is not None}

        if "category" in update_data and isinstance(update_data["category"], dict):
            update_data["category"] = Category(**update_data["category"])

        for field, value in update_data.items():
            if hasattr(existing_product, field):
                setattr(existing_product, field, value)

        await existing_product.save()
        return existing_product
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar el producto: {str(e)}",
        )


@router.delete(
    "/{product_id}",
    tags=["Products"],
    summary="Delete an existing product",
    description="Deletes an existing product.",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_product(product_id: str):
    """Elimina un producto existente"""
    try:
        if not ObjectId.is_valid(product_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="ID de producto inválido",
            )

        existing_product = await Product.get(product_id)
        if not existing_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado"
            )

        await existing_product.delete()
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar el producto: {str(e)}",
        )
