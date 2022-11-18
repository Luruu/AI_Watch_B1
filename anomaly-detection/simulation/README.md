# TRACKER SIMULATOR DATA

this folder contains the coordinates acquired by the **Real Tracker (module A1)**. Each folder contains a simulation that can be used by the **Tracker Simulator**.

## What is Tracker Simulator?
The tracker simulator is the software `tracker_simulator.py` that allows the simulation of the tracker (module A1). It was used when the A1 module was not yet developed. But in this version of the project it is useful to use it when you don't want to carry out a complete test of the system but only a partial one (between module B1 and C1).

## How it works?
The tracker simulator reads [data acquired by tracker](../dataset/simulation1) and send one frame of coordinates to the **Streaming Anomaly Detector** at a time with a delay.
