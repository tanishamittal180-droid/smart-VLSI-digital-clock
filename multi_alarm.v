module multi_alarm(

input [4:0] hour,
input [5:0] min,

input enable,

input [4:0] alarm_hour0,
input [5:0] alarm_min0,

input [4:0] alarm_hour1,
input [5:0] alarm_min1,

input [4:0] alarm_hour2,
input [5:0] alarm_min2,

input [4:0] alarm_hour3,
input [5:0] alarm_min3,

output reg alarm

);

always @(*)

begin

alarm=0;

if(enable)
begin

if(hour==alarm_hour0 && min==alarm_min0)
alarm=1;

else if(hour==alarm_hour1 && min==alarm_min1)
alarm=1;

else if(hour==alarm_hour2 && min==alarm_min2)
alarm=1;

else if(hour==alarm_hour3 && min==alarm_min3)
alarm=1;

end

end

endmodule