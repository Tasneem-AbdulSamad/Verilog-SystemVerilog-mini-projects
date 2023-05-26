module Edg_Detector(
	input  logic clk, reset_n,
	input  logic signal,
	output logic tick
);

logic [1:0] state_reg, state_next;

localparam low  = 0;
localparam edg  = 1;
localparam high = 2;

//State register

always_ff @(posedge clk, negedge reset_n)
	begin
		if (~reset_n)
			state_reg <= low;
		else 
			state_reg <= state_next; 
	end
	
//Next State Logic

always_comb
	begin
	
		case(state_reg)
		
			low:if (signal)
					state_next = edg;
				 else
					state_next = low;
					
			edg:if (signal)
					state_next = high;
				 else
					state_next = low;
					
			high:if (signal)
					state_next = high;
				 else
					state_next = low;

			default: state_next = state_reg;
		
		endcase
			
	end


//Output

assign tick = (state_reg == edg);

endmodule 