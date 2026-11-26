function verify_matlab_examples()
% Verify actual numerical stdout from each of the eight teaching scripts.
root = fileparts(mfilename('fullpath'));
chapters = dir(root);
names = {chapters([chapters.isdir]).name};
names = sort(names(~cellfun('isempty',regexp(names,'^[0-9][0-9] ','once'))));
expected = {[-10,0,10,20,30] .* 9 ./ 5 + 32, [2,3,2], ...
    [3,2,6,4,4,6], sqrt([0,.5,2,10,25]), [4,8,2], ...
    [4,21,2,9,2], [-1,2,8,17], [0,.25,14/9,2.5]};
assert(numel(names) == numel(expected));
for chapter = 1:numel(names)
    folder = fullfile(root,names{chapter});
    observed = execute_one(folder);
    target = expected{chapter}(:);
    assert(isequal(size(observed),size(target)));
    assert(all(abs(observed-target) <= 2e-7 .* max(1,abs(target))));
    fprintf('%s: %s\n', names{chapter}, mat2str(observed', 10));
end
end

function observed = execute_one(folder)
previous = pwd;
restore = onCleanup(@() cd(previous));
cd(folder);
output = evalc('native');
observed = sscanf(output, '%f');
end
