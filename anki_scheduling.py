"""
Anki scheduling simulation
"""


import math
from pprint import pprint
import random


DEFAULT_EASE = 2.5
DEFAULT_INTERVAL_MULT = 1.0
N_CARDS_SIMULATE = 15
N_DAYS_SIMULATE = 90
ROUNDING_FUNC = math.ceil


def compare_intervals():
    for n, ease, mult, first_interval in (
            (10, 2.5, 1.0, 1),
            (10, 2.5, 1.25, 3),
            (10, 2.5, 2.0, 3),
            (10, 2.5, 2.0, 30),
            (10, 3.0, 1.0, 3),
            (10, 3.15, 1.0, 3),
            (10, 3.25, 1.0, 3),
            (10, 3.5, 1.0, 3),
    ):
        show_intervals(n, ease, mult, first_interval)
        show_intervals_accum(n, ease, mult, first_interval)


def get_next_interval(
        curr_interval: float,
        ease: float = DEFAULT_EASE,
        mult: float = DEFAULT_INTERVAL_MULT,
):
    factor = ease * mult
    return curr_interval * factor


def get_nth_interval(
        n: int,
        ease: float = DEFAULT_EASE,
        mult: float = DEFAULT_INTERVAL_MULT,
        first_interval: int = 1,
):
    factor = ease * mult
    return factor ** n * first_interval


def print_sim_results(
        n_cards: int,
        n_days: int,
        ease: float,
        mult: float,
        first_interval: int,
        first_occurrences: dict,
        schedule: list,
        card_intervals: dict):
    print(f'cards: {n_cards}, days: {n_days}, ease: {ease}, mult: {mult}, '
          f'first_interval: {first_interval}')
    print('first occurrences:')
    pprint(first_occurrences)
    print('\nschedule:')
    print('\t'.join(
        [f'{day + 1}: {card}' for day, card in enumerate(schedule)]
    ))
    print('\nintervals:')
    pprint(card_intervals)


def show_intervals(
        n: int,
        ease: float = DEFAULT_EASE,
        mult: float = DEFAULT_INTERVAL_MULT,
        first_interval: int = 1,
):
    print(f'intervals for ease: {ease}, mult: {mult}, first_interval: {first_interval}')
    print('\t'.join(
        [str(ROUNDING_FUNC(get_nth_interval(
            x,
            ease=ease,
            mult=mult,
            first_interval=first_interval,
        ))) for x in range(n)]
    ))


def show_intervals_with_lapses(
        n: int,
        ease: float = DEFAULT_EASE,
        mult: float = DEFAULT_INTERVAL_MULT,
        first_interval: int = 1,
        lapse_prob: float = 0.1,
        after_lapse_coef: float = 0.6,
        n_sim: int = 10,
):
    print(f'intervals for ease: {ease}, mult: {mult}, first_interval: {first_interval}, '
          f'lapse_prob: {lapse_prob}, after_lapse_coef: {after_lapse_coef}, n_sim: {n_sim}')
    for sim in range(n_sim):
        intervals = [first_interval]
        _ease = ease
        for rep in range(n):
            if random.random() <= lapse_prob:
                _ease = max(1.3, _ease - 0.2)
                interval = max(intervals[-1] * after_lapse_coef, 2)
            else:
                interval = get_next_interval(intervals[-1], _ease, mult)
            intervals.append(interval)
        print('\t'.join(str(round(interval)) for interval in intervals))
    print()


def show_intervals_accum(
        n: int,
        ease: float = DEFAULT_EASE,
        mult: float = DEFAULT_INTERVAL_MULT,
        first_interval: int = 1,
        lapse_prob: float = 0.1,
        after_lapse_coef: float = 0.6,
        n_sim: int = 10,
):
    print(f'average intervals for ease: {ease}, mult: {mult}, first_interval: {first_interval}, '
          f'lapse_prob: {lapse_prob}, after_lapse_coef: {after_lapse_coef}, n_sim: {n_sim}')
    intervals = [0.0] * n
    intervals[0] = first_interval
    for sim in range(n_sim):
        beta = 1.0 / (sim + 1)
        prev = first_interval
        _ease = ease
        for rep in range(1, n):
            if random.random() <= lapse_prob:
                _ease = max(1.3, _ease - 0.2)
                interval = max(prev * after_lapse_coef, 2)
            else:
                interval = get_next_interval(prev, _ease, mult)
            prev = interval
            intervals[rep] = interval * beta + intervals[rep] * (1.0 - beta)
    print('\t'.join(str(round(interval)) for interval in intervals))
    print()


def simulate(
        n_cards: int,
        n_days: int,
        ease: float,
        mult: float,
        first_interval: int,
):
    # days and cards: [[card_id1, card_id2, ...], ...]
    schedule = [list() for _ in range(n_days + 1)]  # avoid IndexError
    new_cards = list(reversed(range(1, n_cards + 1)))
    # {card_id: next_interval}
    card_intervals = {card_id: first_interval for card_id in range(1, n_cards + 1)}
    first_occurrences = {}  # card: day

    for day in range(n_days):

        # get card to learn
        cards_to_review = schedule[day]
        n_cards_to_review = len(cards_to_review)
        if not n_cards_to_review:
            if not new_cards:
                # noinspection PyTypeChecker
                schedule[day] = 0
                if 0 not in first_occurrences:
                    first_occurrences[0] = day + 1
                continue
            else:
                new_card = new_cards.pop()
                first_occurrences[new_card] = day + 1
                card_to_review = new_card
        elif n_cards_to_review == 1:
            card_to_review = cards_to_review[0]
        else:
            card_to_review = random.choice(cards_to_review)
            for card in cards_to_review:
                if card != card_to_review:
                    schedule[day + 1].append(card)
                    card_intervals[card] += 1

        schedule[day] = card_to_review

        # reschedule card
        curr_interval = card_intervals[card_to_review]
        next_revision = day + ROUNDING_FUNC(curr_interval)
        if next_revision <= n_days:
            schedule[next_revision].append(card_to_review)
        next_interval = get_next_interval(curr_interval, ease, mult)
        card_intervals[card_to_review] = next_interval

    schedule.pop()  # no need for extra day

    print_sim_results(n_cards, n_days, ease, mult, first_interval, first_occurrences, schedule,
                      card_intervals)


def main():
    simulate(
        n_cards=10,
        n_days=60,
        ease=2.5,
        mult=1.25,
        first_interval=3,
    )
    compare_intervals()


if __name__ == '__main__':
    main()
