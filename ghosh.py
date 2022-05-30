from config import LIMIT_UP, n, M, c_org
from utils import F_big, f_small, integral


def get_r(c):
    return (c / M) ** (1 / (n - 1))


def expected_profit_organizer_ghosh(r):
    f_organizer = lambda y: n * y * f_small(y) * F_big(y) ** (n - 1)
    quad_sol = integral(f_organizer, a=r, b=LIMIT_UP)
    return quad_sol - M * (1 - F_big(r) ** n) - n * c_org


def expected_profit_agent_ghosh(r, c):
    f_agent = lambda y: f_small(y) * F_big(y) ** (n - 1)
    quad_sol = integral(f_agent, a=r, b=LIMIT_UP)
    return M * quad_sol - c * (1 - F_big(r))
