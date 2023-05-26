module UpDown_Counter
		#(parameter n = 4)
(
		input clk, reset_n,
		input [n-1:0]D,
		input load,
		input UpDown,
		output [n-1:0]Q
);

reg [n-1:0]Q_reg, Q_next;
assign Q = Q_reg;

always @(posedge clk, negedge reset_n)
	begin
			if (!reset_n)
				Q_reg <= 'b0;
			else 
				Q_reg <= Q_next;
	end
	
//Next State Logic

always @(*)
	begin 
			casex ({load, UpDown})
				2'b00: Q_next = Q_reg - 1;
				2'b01: Q_next = Q_reg + 1;
				2'b1x: Q_next = D;
				default: Q_reg = Q_reg;
			endcase
	end
	
endmodule
