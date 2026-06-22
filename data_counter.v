module date_counter(

input tick,
input reset,

output reg [4:0] day,
output reg [3:0] month

);

always @(posedge tick)

begin

if(reset)

begin

day<=1;
month<=1;

end

else

begin

if(day==30)

begin

day<=1;

if(month==12)

month<=1;

else
month<=month+1;

end

else

day<=day+1;

end

end

endmodule