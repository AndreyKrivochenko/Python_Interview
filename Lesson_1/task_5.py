"""Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
 ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов для
  пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
   Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает сумму
    дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода."""


def calc_procent(product: dict, summ: int, deposit_term: int):
    result = 0
    if deposit_term == 6:
        result = (summ * product[6] / 100) / 2 + summ
    elif deposit_term == 12:
        result = summ * product[12] / 100 + summ
    elif deposit_term == 24:
        result = (summ * product[24] / 100) * 2 + summ
    result = int(result)
    return result


def calc_deposit(summ: int, deposit_term: int, refill: int):

    def calc_refill(product: dict, deposit_term: int, refill: int):
        result = 0
        if deposit_term == 6:
            result = ((refill * product[6] / 100) / 12 + refill) * 4
        elif deposit_term == 12:
            result = ((refill * product[12] / 100) / 12 + refill) * 10
        elif deposit_term == 24:
            result = ((refill * product[24] / 100) / 12 + refill) * 22
        result = int(result)
        return result

    if summ < 1000 or summ > 1_000_000:
        print(f'Для суммы {summ} руб. нет банковского продукта')
        return
    if deposit_term not in [6, 12, 24]:
        print(f'Невозможно положить деньги на {deposit_term} месяцев')

    summ_10_000 = {
        'begin_sum': 1000,
        'end_sum': 10_000,
        6: 5,
        12: 6,
        24: 5
    }
    summ_100_000 = {
        'begin_sum': 10_000,
        'end_sum': 100_000,
        6: 6,
        12: 7,
        24: 6.5
    }
    summ_1_000_000 = {
        'begin_sum': 100_000,
        'end_sum': 1_000_000,
        6: 7,
        12: 8,
        24: 7.5
    }

    if summ_10_000['begin_sum'] <= summ < summ_10_000['end_sum']:
        return calc_procent(summ_10_000, summ, deposit_term) + calc_refill(summ_10_000, deposit_term, refill)
    elif summ_100_000['begin_sum'] <= summ < summ_100_000['end_sum']:
        return calc_procent(summ_100_000, summ, deposit_term) + calc_refill(summ_100_000, deposit_term, refill)
    else:
        return calc_procent(summ_1_000_000, summ, deposit_term) + calc_refill(summ_1_000_000, deposit_term, refill)


def main():
    dep = calc_deposit(31_000, 24, 500)
    print(f'Сумма депозита составит {dep} рублей.')


if __name__ == '__main__':
    main()
