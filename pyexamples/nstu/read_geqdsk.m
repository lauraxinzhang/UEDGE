function out = read_geqdsk(strload,nr,nz)

fid = fopen(strload,'r');
a = fscanf(fid,'%s',inf);

out = [];

str = strcat('0',num2str(nr),num2str(nz));

j = strfind(a,str);

%str = strcat('geqdsk',num2str(nr),num2str(nz));
%j=strfind(a,str);
a = a(j+1:end);

dum = num2str(nr);
nw = str2double(a(1:length(dum)));
dum1 = num2str(nz);
nh = str2double(a(length(dum)+1:length(dum)+length(dum1)));

b1 = a(length(dum)+length(dum1)+1:end);
jE=strfind(b1,'E');

dum = b1(1:jE(1)+3);
data = str2double(dum);
for j=2:length(jE)-1
   dum = b1(jE(j-1)+4:jE(j)+3);
   data = cat(1,data,str2double(dum));
end

out.rdim = data(1);
out.zdim = data(2);
out.rcentr= data(3);
out.rleft= data(4);
out.zmid = data(5);
out.rmaxis=data(6);
out.zmaxis=data(7);
out.simag =data(8);
out.sibry =data(9);
out.bcentr=data(10);
out.current=data(11);
out.rmaxis=data(14);
data(1:20)=[];
out.fpol =data(1:nw);
data(1:nw)=[];
out.pres =data(1:nw);
data(1:nw)=[];
out.ffprim=data(1:nw); 
data(1:nw)=[];
out.pprime=data(1:nw);
data(1:nw)=[];
psirz=data(1:nw*nh);
out.psirz = zeros(nw,nh);
for j=1:nh
   jmin=(j-1)*nw+1;
   jmax=j*nw;
   out.psirz(:,j)=psirz(jmin:jmax);
end
data(1:nw*nh)=[];
out.qpsi = data(1:nw);
data(1:nw)=[];

out.nbdry = data(1)
out.limitr = data(2)


data(1:2)=[];
%out.rbbbs = data(1:out.nbdry);
%data(1:out.nbdry)=[];
%out.zbbbs = data(1:out.out.nbdry);
%data(1:out.nbdry)=[];
%out.rlim = data(1:out.limitr);
%data(1:out.limitr)=[];
%out.zlim = data(1:out.limitr);


R=linspace(out.rleft,out.rleft+out.rdim,nr);
out.R = R(:);

z = linspace(out.zmid-0.5*out.zdim,out.zmid+0.5*out.zdim,nz);
out.Z = z(:);






