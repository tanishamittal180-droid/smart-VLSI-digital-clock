module alarm_comparator(

input [4:0] hour,
input [5:0] min,

input [4:0] alarm_hour,
input [5:0] alarm_min,

input alarm_enable,

output reg alarm

);

always @(*)

begin

if(
hour==alarm_hour &&
min==alarm_min &&
alarm_enable
)

alarm=1;

else
alarm=0;

end

endmodule