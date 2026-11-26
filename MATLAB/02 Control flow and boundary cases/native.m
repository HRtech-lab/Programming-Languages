x = [-4, 0, 5, 12, 18, 25, 31];
counts = [sum(x <= 0), sum(x > 0 & x < 20), sum(x >= 20)];
assert(sum(counts) == numel(x));
fprintf('%d ', counts);
