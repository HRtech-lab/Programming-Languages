group = [1, 2, 1, 3, 2]';
values = [3, 8, 5, 2, NaN]';
valid = ~isnan(values);
sums = accumarray(group(valid), values(valid), [3, 1]);
counts = accumarray(group(valid), 1, [3, 1]);
averages = sums ./ counts;
fprintf('%.10g ', averages);
