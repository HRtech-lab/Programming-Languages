fid = fopen('readings.csv', 'rt');
assert(fid >= 0, 'Cannot open readings.csv');
cleanup = onCleanup(@() fclose(fid));
fgetl(fid);
values = [];
rejected = 0;
line = fgetl(fid);
while ischar(line)
    if isempty(regexp(strtrim(line), '^[+-]?[0-9]+$', 'once'))
        rejected = rejected + 1;
    else
        values(end+1) = str2double(line);
    end
    line = fgetl(fid);
end
assert(~isempty(values));
fprintf('%g ', [numel(values), sum(values), min(values), max(values), rejected]);
