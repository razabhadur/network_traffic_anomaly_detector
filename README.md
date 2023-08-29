# Network Traffic Anomaly Detector

This project provides a basic implementation of a network traffic anomaly detector using packet capture and machine learning.

## Overview

The script captures network traffic, preprocesses the data to extract relevant features (source and destination IP addresses and ports), trains a KMeans clustering model on typical traffic patterns, and then detects deviations from the norm.

## Prerequisites

- Python 3.x
- Libraries: `pcap`, `struct`, `scikit-learn`

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   ```
2. Navigate to the project directory and install the required libraries:
   ```bash
   pip install pcap scikit-learn
   ```

## Usage

1. Ensure you have the necessary permissions to capture network traffic. On Unix-like systems, you might need to run the script with `sudo`.

2. Execute the script:
   ```bash
   python network_traffic_anomaly_detector.py
   ```

3. Observe the output for any detected anomalies.

## Note

This is a basic and conceptual implementation. For real-world applications, consider capturing a larger dataset, using more sophisticated algorithms, and incorporating additional features for better accuracy.

## License

[MIT License](LICENSE)
