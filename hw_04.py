### HW_04: Абстрактные типы данных

# Вопрос 1.
def interval(a, b):
    """Создает интервал от a до b."""
    return (a, b)

def lower_bound(x):
    """Возвращает нижнюю границу интервала x."""
    return x[0]

def upper_bound(x):
    """Возвращает верхнюю границу интервала x."""
    return x[1]

def str_interval(x):
    """Возвращает строковое представление интервала x."""
    return f'от {lower_bound(x)} до {upper_bound(x)}'

def add_interval(x, y):
    """Возвращает интервал всевозможных сумм значений из x и y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Возвращает интервал всевозможных произведений значений из x и y."""
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Вопрос 2.
def div_interval(x, y):
    """Возвращает интервал, содержащий частные любых значений из x на 
    любые значения из y.
    """
    reciprocal_y = interval(1 / upper_bound(y), 1 / lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Вопрос 3.
def sub_interval(x, y):
    """Возвращает интервал, содержащий разности любых значений из x с 
    любыми значениями из y.
    """
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

# Вопрос 4.
def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# Пример, где par1 и par2 дают разные результаты:
r1 = interval(1, 2)
r2 = interval(1, 2)

print("par1:", str_interval(par1(r1, r2)))  # от 0.25 до 2.0
print("par2:", str_interval(par2(r1, r2)))  # от 0.5 до 1.0

# Вопрос 5.
def multiple_references_explanation():
    return """Проблема множественных ссылок возникает, когда один и тот же интервал
используется в выражении несколько раз. Интервальная арифметика считает каждое
вхождение независимым, поэтому результат может стать шире истинного. В par1
интервалы r1 и r2 входят и в числитель, и в знаменатель, но рассматриваются как
независимые. В par2 каждый резистор используется только один раз, поэтому
результат точнее."""

# Вопрос 6.
def quadratic(x, a, b, c):
    """Возвращает интервал значений квадратичной функции на интервале x."""
    L, U = lower_bound(x), upper_bound(x)

    def f(t):
        return a * t * t + b * t + c

    if a == 0:
        values = [f(L), f(U)]
    else:
        vertex = -b / (2 * a)
        values = [f(L), f(U)]
        if L <= vertex <= U:
            values.append(f(vertex))

    return interval(min(values), max(values))

# Вопрос 7.
def _poly_eval(coeffs, x):
    """Вычисляет полином. coeffs[0] — свободный член."""
    result = 0
    for i in range(len(coeffs) - 1, -1, -1):
        result = result * x + coeffs[i]
    return result

def _real_roots(coeffs, lo, hi, tol=1e-12):
    """Находит действительные корни полинома на отрезке [lo, hi]."""
    coeffs = list(coeffs)

    while len(coeffs) > 1 and abs(coeffs[-1]) < tol:
        coeffs.pop()

    if len(coeffs) <= 1:
        return []

    if len(coeffs) == 2:
        root = -coeffs[0] / coeffs[1]
        if lo - tol <= root <= hi + tol:
            return [root]
        return []

    derivative = [coeffs[i] * i for i in range(1, len(coeffs))]
    crits = _real_roots(derivative, lo, hi, tol)

    points = [lo] + sorted(crits) + [hi]
    roots = []

    def add_root(r):
        if lo - tol <= r <= hi + tol:
            if not any(abs(r - s) < 1e-8 for s in roots):
                roots.append(r)

    for p in points:
        if abs(_poly_eval(coeffs, p)) < 1e-8:
            add_root(p)

    for a, b in zip(points, points[1:]):
        fa = _poly_eval(coeffs, a)
        fb = _poly_eval(coeffs, b)

        if fa * fb < 0:
            left, right = a, b
            fleft = fa

            for _ in range(100):
                mid = (left + right) / 2
                fmid = _poly_eval(coeffs, mid)

                if abs(fmid) < 1e-14:
                    break

                if fleft * fmid <= 0:
                    right = mid
                else:
                    left = mid
                    fleft = fmid

            add_root((left + right) / 2)

    return sorted(roots)

def polynomial(x, c):
    """Возвращает интервал значений полинома с коэффициентами c.

    c[0] — свободный член, c[1] — коэффициент при x, и т.д.
    """
    L, U = lower_bound(x), upper_bound(x)

    derivative = [c[i] * i for i in range(1, len(c))]
    crits = _real_roots(derivative, L, U) if derivative else []

    candidates = [L, U] + crits
    values = [_poly_eval(c, t) for t in candidates]

    return interval(min(values), max(values))

# Метод Ньютона (оставлен как в условии)
def improve(update, close, guess=1, max_updates=100):
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def find_zero(f, df, guess=1):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero, guess)

def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update
