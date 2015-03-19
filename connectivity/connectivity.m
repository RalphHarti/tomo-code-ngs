clear all

w_image = [];

for k = 1000:3047       % iterates through binray images
    filename = strcat('/media/lovelace/932C-E76A/combined_cropping/pos3_1461x1462x1461/pos3_combined', num2str(k), '.tif');
    imageData = imread(filename);
    i = k-999;
    A(:,:,i) = imageData;
    disp('read file ')
    disp(i)
end
disp('read all the files ...')

[L, NUM] = bwlabeln(A);   % default is 26 connecting neighbours
cc = bwlabeln(A);

for i = 1:2048          % iterates through images and labels them
    RGB = label2rgb(cc(:,:,i));
    imwrite(RGB, ['t_rgb_' num2str(i) '.tif']);
    disp('wrote file ')
    disp(i)
end

disp('Number of connected objects: ')
disp(NUM)
