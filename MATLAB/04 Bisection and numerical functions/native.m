values = [0, 0.5, 2, 10, 25];
roots = zeros(size(values));
for j = 1:numel(values)
    n = values(j);
    if n == 0
        continue
    end
    lo = 0;
    hi = max(1, n);
    for iteration = 1:55
        mid = (lo + hi) / 2;
        if mid * mid < n
            lo = mid;
        else
            hi = mid;
        end
    end
    roots(j) = (lo + hi) / 2;
end
fprintf('%.12g ', roots);
