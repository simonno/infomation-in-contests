from config import n, k, M, c_org
from utils import binom, F_big, f_small, integral, root


def derivative_F_by_y(y, T, p):
    inner = (n - k) * p * f_small(y) * (p * F_big(y) + (1 - p)) ** (n - k - 1)
    if y <= T:
        return F_big(T) ** k * inner
    else:
        return k * F_big(y) ** (k - 1) * (p * F_big(y) + (1 - p)) ** (n - k) + F_big(y) ** k * inner


def optimal_threshold(p, c):
    return root(lambda t: prob_win(t, t, p) * M - c)


def equilibrium_participate(p, T_optimal, c):
    eq2 = lambda t: f_small(t) * prob_win_tag(t, T_optimal, p)
    quad_sol = integral(eq2)
    return quad_sol * M - c


def expected_profit_organizer(p, T_optimal):
    f_simon = lambda y: y * derivative_F_by_y(y, T_optimal, p)
    quad_sol = integral(f_simon)
    return quad_sol - M * (1 - (F_big(T_optimal) ** k * (1 - p) ** (n - k))) - k * c_org


def expected_profit_agent_not_disclosed(p, T_optimal, c):
    f = lambda y: f_small(y) * F_big(max(T_optimal, y)) ** k * (p * F_big(y) + (1 - p)) ** (n - k - 1)
    quad_sol = integral(f)
    return p * (M * quad_sol - c)


def expected_profit_agent_disclosed(p, T_optimal, c):
    f = lambda y: f_small(y) * F_big(y) ** (k - 1) * (p * F_big(y) + (1 - p)) ** (n - k)
    quad_sol = integral(f, a=T_optimal)
    return M * quad_sol - c * (1 - F_big(T_optimal))


def expected_profits(p, T_optimal, c):
    return [expected_profit_organizer(p, T_optimal), expected_profit_agent_not_disclosed(p, T_optimal, c),
            expected_profit_agent_disclosed(p, T_optimal, c)]


def prob_win(t, T, p):
    prob = 0
    for w in range(n - k + 1):
        prob += binom(w, n - k, p) * F_big(t) ** w
    return prob * F_big(max(T, t)) ** (k - 1)


def prob_win_tag(t, T, p):
    prob = 0
    for w in range(n - k):
        prob += binom(w, n - k - 1, p) * F_big(t) ** w
    return prob * F_big(max(T, t)) ** k


def equilibrium(p, c):
    T = optimal_threshold(p, c)
    eb = equilibrium_participate(p, T, c)
    return [T, eb]
