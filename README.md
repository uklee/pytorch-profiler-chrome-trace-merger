# PyTorch Profiler Chrome Trace Merger

## Introduction
This code merges chrome trace files from PyTorch Profiler into a single trace file.
This helps you to simply view multiple trace files in a single tab and intrinsically syncronize them.
It exploits the pid information space of the trace files, which does not contain useful information by default.

## Usage
Change `INPUT_FILES` and `OUTPUT_FILE` appropriately.

## Note
Will be changed to get `INPUT_FILES` and `OUTPUT_FILE` from parameter at a future version.
