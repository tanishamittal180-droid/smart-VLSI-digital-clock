module top(

input clk,
input reset,

input alarm_enable,
input mode_12,
input stopwatch_enable,

output alarm,
output buzz,

output [5:0] sec,
output [5:0] min,
output [4:0] hour,

output [5:0] sw_sec,

output [4:0] day,
output [3:0] month,

output am_pm

);

wire tick;

wire [4:0] display_hour;

//////////////////////////////////////////
// Clock Divider
//////////////////////////////////////////

clk_divider #(.SIM_MODE(1))

d1(

.clk(clk),
.reset(reset),
.tick(tick)

);

//////////////////////////////////////////
// Time Counter
//////////////////////////////////////////

time_counter d2(

.tick(tick),
.reset(reset),
.mode_12(mode_12),

.sec(sec),
.min(min),
.hour(hour),

.display_hour(display_hour)

);

assign am_pm=(hour<12)?0:1;

//////////////////////////////////////////
// Multiple Alarm System
//////////////////////////////////////////

multi_alarm d3(

.hour(hour),
.min(min),

.enable(alarm_enable),

.alarm_hour0(5'd0),
.alarm_min0(6'd1),

.alarm_hour1(5'd0),
.alarm_min1(6'd2),

.alarm_hour2(5'd0),
.alarm_min2(6'd3),

.alarm_hour3(5'd0),
.alarm_min3(6'd4),

.alarm(alarm)

);

//////////////////////////////////////////
// Buzzer
//////////////////////////////////////////

buzzer d4(

.alarm(alarm),
.buzz(buzz)

);

//////////////////////////////////////////
// Stopwatch
//////////////////////////////////////////

stopwatch d5(

.tick(tick),
.reset(reset),
.enable(stopwatch_enable),

.sw_sec(sw_sec)

);

//////////////////////////////////////////
// Date Counter
//////////////////////////////////////////

date_counter d6(

.tick(tick),
.reset(reset),

.day(day),
.month(month)

);

endmodule