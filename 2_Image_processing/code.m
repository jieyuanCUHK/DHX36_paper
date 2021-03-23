clear all
%read in images:
filename=strcat('D:\XN_images\SC G4\FISC\fisc 5_b0t0z0c0-2x0-512y0-512.tif');
aa=imread(filename)
%green channel
aab=aa(:,:,2)

%first label individual cells with green bounding boxes
L = bwlabeln(aab, 4);
S = regionprops(L, 'BoundingBox');
%left top width height

tempred=aa(:,:,1)
result=[]
for areas=1:length(S)
    BoundingBox=S(areas).BoundingBox 
    xMin = ceil(BoundingBox(1))
    xMax = xMin + BoundingBox(3)-1
    yMin = ceil(BoundingBox(2))
    yMax = yMin + BoundingBox(4)-1

    tt=tempred(yMin:yMax,xMin:xMax)
    tmp=tt(:)
    %remove pixels with intensity value<5
    tmp(tmp<5)=[]

    %conduct quantification
    result(areas)=mean(tmp)
end
