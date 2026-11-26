changes = [3, -1, 4, -2, 0, 2];
balances = cumsum(changes);
assert(balances(end) == sum(changes));
fprintf('%d ', balances);
