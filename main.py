import csv
from time import time

from config import LIMIT_UP, LIMIT_DOWN, STEPS, M, k, n, c_org
from ghosh import expected_profit_agent_ghosh, expected_profit_organizer_ghosh, get_r
from levy import expected_profit_agent_levy, expected_profit_organizer_levy, get_p
from simon import expected_profits as expected_profits_simon, equilibrium, optimal_threshold


def write(array):
    with open('results/n={:d},k={:d},M={:.2f},c_org={:.2f}.csv'.format(n, k, M, c_org), 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(array)


def main():
    start = time()
    write(['c', 'p', 'T_optimal', 'p_levy', 'r', 'organizer', 'organizer_ghosh', 'organizer_levy',
           'agent_not_disclosed', 'agent_disclosed', 'agent_ghosh', 'agent_levy'])
    for c_index in range(0, int(M * STEPS) + 1):
        c = c_index / STEPS
        if c == 0.38:
            print('!')
        print(c)
        T_p_0 = optimal_threshold(0, c)
        T_p_1 = optimal_threshold(1, c)
        found = False

        r = get_r(c)
        organizer_ghosh = expected_profit_organizer_ghosh(r)
        agent_ghosh = expected_profit_agent_ghosh(r, c)

        p_levy = get_p(c)
        organizer_levy = expected_profit_organizer_levy(p_levy)
        agent_levy = expected_profit_agent_levy(p_levy, c)

        for p_index in range(LIMIT_DOWN, LIMIT_UP * STEPS + 1):
            p1 = p_index / STEPS
            p2 = (p_index + 1) / STEPS
            [T1, EB1] = equilibrium(p1, c)
            [T2, EB2] = equilibrium(p2, c)
            if EB1 * EB2 <= 0:
                found = True
                if EB1 > EB2:
                    p = p1
                    T_optimal = T1
                else:
                    p = p2
                    T_optimal = T2
                [organizer, agent_not_disclosed, agent_disclosed] = expected_profits_simon(p, T_optimal, c)
                write([c, p, T_optimal, p_levy, r, organizer, organizer_ghosh, organizer_levy, agent_not_disclosed,
                       agent_disclosed, agent_ghosh, agent_levy])
        if not found:
            if EB1 > 0:
                p = 1
                T_optimal = T_p_1
            else:
                p = 0
                T_optimal = T_p_0
            [organizer, agent_not_disclosed, agent_disclosed] = expected_profits_simon(p, T_optimal, c)
            write([c, p, T_optimal, p_levy, r, organizer, organizer_ghosh, organizer_levy, agent_not_disclosed,
                   agent_disclosed, agent_ghosh, agent_levy])

    seconds = round(time() - start)
    print('duration: {:2d} m {:2d} sec '.format(seconds // 60, seconds % 60))


if __name__ == '__main__':
    main()
