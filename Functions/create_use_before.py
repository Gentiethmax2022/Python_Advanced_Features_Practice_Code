import logging

class StripepaymentHandler:
    
    def handle_payment(self, amount: int) -> None:
        logging.info(f"Charging ${amount/100:.2f} using Stripe")
        

PRICES = {
    "burger": 10_00,
    "fries": 5_20,
    "drink": 2_13,
    "salad": 15_12
}


def order_food(items: list[str]) -> None:
    total = sum(PRICES[item] for item in items)
    logging.info(f"The total order is: ${total/100:.2f}")
    payment_handler = StripepaymentHandler()
    payment_handler.handle_payment(total)
    logging.info("Order is completed")
    

def main() -> None:
    logging.basicConfig(level=logging.INFO)
    order_food(["burger", "fries", "drink"])
    
    
if __name__ == "__main__":
    main()
    
    