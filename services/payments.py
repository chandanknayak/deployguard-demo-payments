from fastapi import APIRouter

router = APIRouter()


@router.post("/v1/payments/charge")
def process_charge_v1(order_id: str, amount: int) -> dict:
    """Process a card charge for an order."""
    return {"status": "charged", "order_id": order_id, "amount": amount}


def compute_fee(amount: int) -> int:
    return max(1, int(amount * 0.029) + 30)
