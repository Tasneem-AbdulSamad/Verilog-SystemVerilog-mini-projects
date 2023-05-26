module FSM_101_1000(
	input clk, 
	input reset_n, 
	input x, 
	output y
);

reg [1:0] state_reg, state_next;

localparam s0 = 0;
localparam s1 = 1;
localparam s2 = 2;
localparam s3 = 3;

//State Register

always @(posedge clk, negedge reset_n)
begin
		if (~reset_n)
			state_reg = 'b0;
		else 
			state_reg = state_next;
end

//Next State Logic

always @(*)
begin
		case (state_reg)
			s0: if (x)
					state_next = s1;
				else
					state_next = s0;
			
			s1: if (x)
					state_next = s1;
				else
					state_next = s2;
			
			s2: if (x)
					state_next = s1;
				else
					state_next = s3;
			
			s3: if (x)
					state_next = s1;
				else
					state_next = s0;
			
			default: state_next = state_reg;
			
		endcase
end

//Output

assign y = ((state_reg == s3) & (x == 0)) | ((state_reg == s2) & (x == 1));

endmodule
