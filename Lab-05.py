import doctest

# Вопрос 1.
def acorn_finder(t):
    """Возвращает True, если t содержит узел со значением 'жёлудь', иначе False.

    >>> scrat = tree('жёлудь')
    >>> acorn_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('ветвь1', [tree('лист'), tree('жёлудь')]), tree('ветвь2')])
    >>> acorn_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> acorn_finder(numbers)
    False
    """
    if label(t) == 'жёлудь':
        return True
    return any(acorn_finder(b) for b in branches(t))

# Вопрос 2.
def prune_leaves(t, vals):
    # Если узел изначально является листом — проверяем его по списку vals
    if is_leaf(t):
        if label(t) in vals:
            return None
        return t
    
    # Рекурсивно обрабатываем ветви
    new_branches = []
    for b in branches(t):
        pruned_b = prune_leaves(b, vals)
        if pruned_b is not None:
            new_branches.append(pruned_b)
            
    # Возвращаем дерево с обновленными ветвями (даже если они стали пустыми)
    return tree(label(t), new_branches)


# Вопрос 3.
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def helper(f):
        nonlocal n
        n = f(n)
        return n
    return helper

###########
# Деревья #
###########

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'ветви должны быть деревьями'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Вспомогательная функция для вывода дерева, нужная для тестов."""
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

# Запуск тестов при запуске файла
if __name__ == "__main__":
    doctest.testmod(verbose=True)
