import pcap
from struct import unpack
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Capture packets and extract details functions (from Part 1)...

def train_model(data, n_clusters=3):
    """Train a KMeans clustering model on the provided data."""
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data)
    return kmeans

def detect_anomalies(model, data, threshold=2.5):
    """Detect anomalies based on the distance from the cluster centroids."""
    distances = model.transform(data)
    cluster_distances = distances.min(axis=1)
    mean_distance = cluster_distances.mean()
    std_distance = cluster_distances.std()
    anomalies = [i for i, d in enumerate(cluster_distances) if d > mean_distance + threshold * std_distance]
    return anomalies

if __name__ == '__main__':
    # Capture packets and preprocess data
    captured_packets = capture_packets()
    packet_details = [extract_packet_details(p) for p in captured_packets]
    
    # Convert IP addresses to numerical format for training
    le = LabelEncoder()
    src_ips = le.fit_transform([details[0] for details in packet_details])
    dst_ips = le.fit_transform([details[2] for details in packet_details])
    src_ports = [details[1] for details in packet_details]
    dst_ports = [details[3] for details in packet_details]
    
    # Prepare data for training
    training_data = list(zip(src_ips, src_ports, dst_ips, dst_ports))
    
    # Train the model
    model = train_model(training_data)
    
    # Detect anomalies
    anomalies = detect_anomalies(model, training_data)
    for index in anomalies:
        print(f'Anomalous traffic detected: {packet_details[index]}')