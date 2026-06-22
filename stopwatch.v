module stopwatch(

input tick,
input reset,
input enable,

output reg [5:0] sw_sec

);

always @(posedge tick)

begin

if(reset)

sw_sec<=0;

else if(enable)

begin

if(sw_sec==59)
sw_sec<=0;

else
sw_sec<=sw_sec+1;

end

end

endmodule