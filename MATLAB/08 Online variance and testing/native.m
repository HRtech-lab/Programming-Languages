values = 1e9 + [1, 2, 4, 5];
count = 0;
centre = 0;
m2 = 0;
for value = values
    count = count + 1;
    delta = value - centre;
    centre = centre + delta / count;
    m2 = m2 + delta * (value - centre);
    fprintf('%.12g ', m2 / count);
end
