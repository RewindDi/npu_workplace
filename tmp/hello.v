module hello;
    initial begin
        $display("Hello, NPU!");
        #10 $display("Time: %0t", $time);
        $finish;
    end
endmodule
