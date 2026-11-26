from fastapi import APIRouter
from services.payments import process_charge_v1

router = APIRouter()


@router.post("/checkout/pay")
def checkout_pay(order_id: str, amount: int) -> dict:
    """Checkout endpoint calling payments service."""
    return process_charge_v1(order_id=order_id, amount=amount)
