module Full_Adder(
    input x,y,c_in,
	 output s,c_out
	 );
	 
assign s = x ^ y ^ c_in;
assign c_out = (x & y) | (x & c_in) | (c_in & y);

endmodule 