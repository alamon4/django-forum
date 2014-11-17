f = dsolve('cos(t) = y + Dy','y(0)=0')
t = 0:.0001:10;
ezplot(f,[t(1) t(end)]);

% function HW2
% t=0:0.0001:10;
% initial_y=0;
% [y,t]=ode45( @rhs, t, initial_y);
% 
% plot(y,t);
% xlabel('y'); ylabel('t');
%     
%     function dydt=rhs(t,y)
%             dydt = cos(t)-y;
%     end
% end
