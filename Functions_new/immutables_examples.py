import random 


def main() -> None:
    test_list = [120, 34, -78, 89, 728]
    
    # built in immutable sort
    sorted_list = sorted(test_list)
    print(f"Original list: {test_list}")
    print(f"Sorted list: {sorted_list}")
    
    # built in mutable list
    test_list.sort()
    print(f"Original list: {test_list}")
    
    # other examples 
    cards = ["2", "3", "J", "Q"]
    
    shuffled_cards = random.sample(cards, k=len(cards))
    print(f"Shuffled cards: {shuffled_cards}")
    print(f"Original Cards: {cards}")
    
    random.shuffle(cards)
    print(f"Cards: {cards}")
    
    
if __name__ == "__main__":
    main()
    
    