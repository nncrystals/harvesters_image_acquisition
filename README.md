# Motivation
This project is created as a sidecar of the MATLAB GenTL image acquisition utility. It has been observed that MATLAB function having hard time pacing up with the real time when high frame rate acquisition was used. I hope this cross-platform implementation of GenTL image acquisition tool can help remedy the issue.


With this project, the image will no longer be fed from Simulink with the dedicated S-Function. This script should be started along with the simulink simulation (possibly by callback)
 