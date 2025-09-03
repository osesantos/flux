# Flux

**Flux** – Multi-Model LLM Router & Load Balancer  
*The backbone for scalable, cost-aware, multi-LLM orchestration.*

---

## Overview

Flux is a **Kubernetes-native LLM Router** designed to act as a universal interface between clients (like GoMind) and multiple LLM providers (Ollama, OpenAI, Gemini, Claude, etc.).  

It provides:  
- Smart routing by **task type, latency, or cost**.  
- Multi-model orchestration with **automatic fallback**.  
- Observability: track **latency, tokens, costs**, and expose metrics via Prometheus.  
- Semantic caching for faster responses and cost reduction.  
- Kubernetes-ready deployment with Helm charts and autoscaling.  

Flux is essentially the **Nginx/Envoy for LLMs**, giving you a unified, scalable, and maintainable AI infrastructure layer.

---

## Quickstart

Clone the repository:
```sh
git clone https://github.com/osesantos/flux.git
cd flux
```

Configure your LLM providers in config.yaml.

Start the server (development mode):
```sh
python -m flux.main
```

Access the API endpoints:

/query – send requests for model inference.
/metrics – Prometheus metrics.

## Contributing
Flux is designed to be extensible. Feel free to add new providers, routing policies, or observability features.

## License
MIT License
