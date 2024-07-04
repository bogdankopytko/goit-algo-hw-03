import random


def get_numbers_ticket(min, max, quantity):
    all_tickets = []
    if min >= 1 and max <= 1000 and quantity <= (max - min):
        for i in range (min, max + 1, 1):
            all_tickets.append(i)
        tickets = random.sample(all_tickets, quantity)
        return tickets
    else:
        return all_tickets


lottery_numbers = get_numbers_ticket(10, 20, 5)
print("Ваші лотерейні числа:", lottery_numbers)
