x = (0:4)';
y = [2; 5; 8; 11; 14];
design = [ones(size(x)), x];
coefficients = design \ y;
new_x = [-1; 0; 2; 5];
predictions = [ones(size(new_x)), new_x] * coefficients;
fprintf('%.12g ', predictions);
