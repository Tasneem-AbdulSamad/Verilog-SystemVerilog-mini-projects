`timescale 1ns/1ps

module Edg_Detector_tb;

//Signal declration

localparam T = 20;

logic clk, reset_n;
logic signal;
logic tick;

//Instantiate UUT

Edg_Detector uut0(.*);

//Clock generator (20 ns)

always
	begin
		clk = 1'b1;
		#(T/2);
		clk = 1'b0; 
		#(T/2);
	end
	
//Reset for the first half cycle

initial
	begin
		reset_n = 1'b0;
		#(T/2);
		reset_n = 1'b1;
	end
	

//Stimuli

initial
	begin
	
		@(negedge clk);
		signal = 1'b0;
		
		repeat(2) @(negedge clk);
		#3
		signal = 1'b1;
		
		repeat(2) @(negedge clk);
		signal = 1'b0;
		
		@(negedge clk);
		signal = 1'b1;
		
		#15
		signal = 1'b0;
		
		#(5*T); //Wait for 100
		
		$stop;
	end

endmodule 

