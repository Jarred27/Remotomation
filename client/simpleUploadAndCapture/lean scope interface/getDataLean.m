function [k, XI, XQ, YI, YQ] = getDataLean(scope_obj)
    %% Freeze waveform for data transfer
	AcquireWaveformLean(scope_obj);

	%% Read the digitized waveforms
	WfmTmp{1} = ReadScopeWfmLean(scope_obj,'Chan1');
	WfmTmp{2} = ReadScopeWfmLean(scope_obj,'Chan2');
    WfmTmp{3} = ReadScopeWfmLean(scope_obj,'Chan3');
	WfmTmp{4} = ReadScopeWfmLean(scope_obj,'Chan4');
    
	k = 1:1:length(WfmTmp{1}.Data);
	XI = WfmTmp{1}.Data;
    XQ = WfmTmp{2}.Data;
	YI = WfmTmp{3}.Data;
    YQ = WfmTmp{4}.Data;
	
    %% Run scope again ('unfreeze' waveform)
    fprintf(scope_obj,':run');
	
	
end