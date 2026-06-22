module clk_divider #(
parameter SIM_MODE=1
)
(
input clk,
input reset,
output reg tick
);

reg [31:0] count;

always @(posedge clk)
begin

if(reset)
begin
count<=0;
tick<=0;
end

else
begin

if(SIM_MODE)
begin

if(count==10)
begin
count<=0;
tick<=1;
end

else
begin
count<=count+1;
tick<=0;
end

end

else

begin

if(count==49999999)
begin
count<=0;
tick<=1;
end

else
begin
count<=count+1;
tick<=0;
end

end

end

end

endmodule