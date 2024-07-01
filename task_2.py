import random


def get_numbers_ticket(min, max, quantity):
    all_tickets = []
    for i in range (min, max + 1, 1):
        all_tickets.append(i)
    tickets = random.sample(all_tickets, quantity)
    return tickets


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
