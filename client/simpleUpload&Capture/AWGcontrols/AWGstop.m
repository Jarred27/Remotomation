function AWGstop()
% stops signal output of AWG
% Usage:
%	AWGstop();
% Inputs:
%	none
% Outputs:
%	none



AWGadd = "TCPIP0::localhost::inst1::INSTR";
Command = ":ABOR";

% in the form of ">python (python_command) (device) (device_command)"
cmdStr = "python write.py " + AWGadd + " " + Command;

[status,cmdOut] = system(cmdStr);
if status~=0
    warning("syetem error: "+cmdOut)
end
end