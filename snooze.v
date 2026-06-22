module snooze(

input [5:0] current_min,

output [5:0] snooze_min

);

assign snooze_min=
(current_min+5>=60)
?
(current_min+5-60)
:
(current_min+5);

endmodule