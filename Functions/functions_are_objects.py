import logging
from functools import partial
from typing import Callable


def handle_payment_stripe(amount: int) -> None:
    logging.info(f"Charging ${amount/100:.2f} using Stripe")
    

PRICES = {
    "burger": 10_00,
    "fries": 5_00,
    "drink": 2_00,
    "salad": 15_00
}


HandlePaymentFn = Callable[[int], None]

def order_food(items: list[str], payment_handler: HandlePaymentFn) -> None:
    total = sum((PRICES[item] for item in items), start=0)
    logging.info(f"The total order is ${total/100:.2f}")
    payment_handler(total)
    logging.info("Order Completed")
    

order_food_stripe = partial(order_food, payment_handler=handle_payment_stripe)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    order_food_stripe(["burger", "drink", "salad"])
    
    
if __name__ == "__main__":
    main()
    
    