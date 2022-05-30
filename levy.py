from config import n, M
from utils import F_big, f_small, integral, root


def get_p(c):
    try:
        return root(lambda x: ((1 - (1 - x) ** n) / (n * x) - c / M))
    except Exception:
        return 1


def expected_profit_organizer_levy(p):
    f_organizer = lambda y: y * n * p * f_small(y) * (p * F_big(y) + (1 - p)) ** (n - 1)
    quad_sol = integral(f_organizer)
    return quad_sol - M * (1 - (1 - p) ** n)


def expected_profit_agent_levy(p, c):
    f_agent = lambda y: f_small(y) * (p * F_big(y) + (1 - p)) ** (n - 1)
    quad_sol = integral(f_agent)
    return p * (M * quad_sol - c)
