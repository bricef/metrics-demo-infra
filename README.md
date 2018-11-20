Metrics Demo Infrastructure Repository
======================================

This is the companion repository to [the metrics-demo repo](https://github.com/bricef/metrics-demo/). 

It contains the infrastructure definition files for the metric demo.

The `deploy/local` directory includes Kubenetes manifests used to set up the demo on [Minikube](https://github.com/kubernetes/minikube) or similar local cluster, including the manifests for [Grafana](https://grafana.com/) and [Prometheus](https://prometheus.io).

The `deploy/cloud-common` directory includes Kubernetes manifests to set up the service on a [GKE](https://cloud.google.com/kubernetes-engine/) or [EKS](https://aws.amazon.com/eks/) cluster.

