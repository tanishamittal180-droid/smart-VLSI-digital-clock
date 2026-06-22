`timescale 1ns/1ps

module clock_tb();

reg clk;
reg reset;

reg alarm_enable;
reg mode_12;
reg stopwatch_enable;

wire alarm;
wire buzz;

wire [5:0] sec;
wire [5:0] min;
wire [4:0] hour;

wire [5:0] sw_sec;

wire [4:0] day;
wire [3:0] month;

wire am_pm;

//////////////////////////////////////////
// DUT
//////////////////////////////////////////

top uut(

.clk(clk),
.reset(reset),

.alarm_enable(alarm_enable),
.mode_12(mode_12),
.stopwatch_enable(stopwatch_enable),

.alarm(alarm),
.buzz(buzz),

.sec(sec),
.min(min),
.hour(hour),

.sw_sec(sw_sec),

.day(day),
.month(month),

.am_pm(am_pm)

);

//////////////////////////////////////////
// Clock Generation
//////////////////////////////////////////

always #5 clk=~clk;

//////////////////////////////////////////
// Simulation
//////////////////////////////////////////

initial

begin

$dumpfile("clock.vcd");

$dumpvars(0,clock_tb);

clk=0;

reset=1;

alarm_enable=1;

mode_12=0;

stopwatch_enable=1;

#50

reset=0;

#5000

mode_12=1;

#5000

stopwatch_enable=0;

#5000

stopwatch_enable=1;

#10000

$finish;

end

//////////////////////////////////////////
// Self Checking
//////////////////////////////////////////

always @(posedge clk)

begin

$display(

"TIME=%d:%d:%d DAY=%d MONTH=%d STOPWATCH=%d AMPM=%d ALARM=%d",

hour,
min,
sec,

day,
month,

sw_sec,

am_pm,

alarm

);

if(hour>23)

begin

$display("ERROR: Hour Overflow");
$stop;

end


if(min>59)

begin

$display("ERROR: Minute Overflow");
$stop;

end


if(sec>59)

begin

$display("ERROR: Second Overflow");
$stop;

end

end

endmodule