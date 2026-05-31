# AI_ASSISTED_RTL_GENERATOR
Overview

AI-Assisted RTL Generator is a web-based application that automates the initial stages of RTL analysis and verification.

The tool accepts SystemVerilog RTL code, extracts important design information, converts it into structured JSON, and automatically generates a basic verification testbench.

The application is built using Python and Streamlit and is deployed on Hugging Face Spaces.

Features
SystemVerilog RTL Parsing
Module Name Extraction
Input Port Detection
Output Port Detection
JSON-Based RTL Representation
Automatic Testbench Generation
Web-Based User Interface
Public Cloud Deployment
Technology Stack
Frontend
Streamlit
Backend
Python
RTL Processing
Regular Expressions (Regex)
SystemVerilog Parsing Logic
Deployment
Hugging Face Spaces
Development Environment
Google Colab
Hugging Face Spaces
Project Workflow

SystemVerilog RTL
↓
RTL Parser
↓
JSON Extraction
↓
Testbench Generator
↓
Web-Based Display

Example RTL Input
module mux2to1(
    input logic a,
    input logic b,
    input logic sel,
    output logic y
);

always_comb begin
    if(sel)
        y = b;
    else
        y = a;
end

endmodule
Example JSON Output
{
  "module": "mux2to1",
  "inputs": ["a", "b", "sel"],
  "outputs": ["y"]
}
Example Generated Testbench
module tb;

reg a;
reg b;
reg sel;

wire y;

mux2to1 dut(
    .a(a),
    .b(b),
    .sel(sel),
    .y(y)
);

initial begin
    $dumpfile("wave.vcd");
    $dumpvars(0,dut);
end

endmodule
Live Demo

Add your Hugging Face Space link here.

Example:

https://huggingface.co/spaces/USERNAME/SPACE_NAME

Future Enhancements
File Upload Support (.sv)
Download Generated Testbench
Assertion Generation
AI-Powered RTL Explanation
Functional Coverage Suggestions
Verification Automation
EDA Playground Integration
Waveform Analysis
Repository Structure
src/
├── streamlit_app.py
├── rtl_parser.py
├── tb_generator.py

Dockerfile
requirements.txt
README.md
Author

Anurag Vats

Aspiring Silicon Design Engineer | RTL Design | Verification | Python | SystemVerilog

License

This project is released under the MIT License.
