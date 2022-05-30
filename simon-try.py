# from utils import binom, F_big, f_small, integral, root
#
#
# class Simon:
#     def __init__(self, n, k, M, c, c_org):
#         self.c = c
#         self.n = n
#         self.k = k
#         self.M = M
#         self.c_org = c_org
#
#     def set_c(self, c):
#         self.c = c
#
#     @staticmethod
#     def derivative_F_by_y(y, T, p):
#         inner = (n - k) * p * f_small(y) * (p * F_big(y) + (1 - p)) ** (n - k - 1)
#         if y > T:
#             return F_big(T) ** k * inner
#         else:
#             return k * F_big(y) ** (k - 1) * (p * F_big(y) + (1 - p)) ** (n - k) + F_big(y) ** k * inner
#
#     def optimal_threshold(self, p):
#         return root(lambda t: self.prob_win(t, t, p) * M - c)
#
#     def equilibrium_participate(self, p, T_optimal):
#         eq2 = lambda t: f_small(t) * self.prob_win_tag(t, T_optimal, p)
#         quad_sol = integral(eq2)
#         return quad_sol * M - c
#
#     def expected_profit_organizer(self, p, T_optimal):
#         f_simon = lambda y: y * self.derivative_F_by_y(y, T_optimal, p)
#         quad_sol = integral(f_simon)
#         return quad_sol - M * (1 - (F_big(T_optimal) ** k * (1 - p) ** (n - k))) - k * c_org
#
#     @staticmethod
#     def prob_win(t, T, p):
#         prob = 0
#         for w in range(n - k + 1):
#             prob += binom(w, n - k, p) * F_big(t) ** w
#         return prob * F_big(max(T, t)) ** (k - 1)
#
#     @staticmethod
#     def prob_win_tag(t, T, p):
#         prob = 0
#         for w in range(n - k):
#             prob += binom(w, n - k - 1, p) * F_big(t) ** w
#         return prob * F_big(max(T, t)) ** k
#
#     def equilibrium(self, p):
#         T = self.optimal_threshold(p)
#         eb = self.equilibrium_participate(p, T)
#         return [T, eb]
#
#         # for t_index in range(LIMIT_DOWN, LIMIT_UP * 10000 + 1):
#         #     t1 = t_index / 10000
#         #     t2 = (t_index + 1) / 10000
#         #     eb1 = prob_win(t1, t1, p) * M - c
#         #     eb2 = prob_win(t2, t2, p) * M - c
#         #     if eb1 * eb2 <= 0:
#         #         return t1
#         # raise Exception('optimal threshold not found')
#         # sol = root(lambda threshold: prob_win(threshold, threshold, p) * M - c, 0.5)
#         # r = sol.x[0]
#         # return 0 if r < 0 else (1 if r > 1 else r)
#
#     # def prob_win(y, threshold, p):
#     #   return F_big(max(threshold, y)) ** k * (p * F_big(y) + (1 - p)) ** (n - k - 1)
#     # def prob_win_tag(y, threshold, p):
#     #    return F_big(max(threshold, y)) ** (k - 1) * (p * F_big(y) + (1 - p)) ** (n - k)
