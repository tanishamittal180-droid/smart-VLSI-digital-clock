iverilog -o clock rtl/*.v tb/*.v
vvp clock
gtkwave clock.vcd