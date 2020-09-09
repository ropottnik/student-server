envoy:
	docker kill envoy-students || true
	docker run --rm -d --name envoy-students -v `pwd`/envoy-localhost.yml:/etc/envoy/envoy.yaml --network=host envoyproxy/envoy:v1.10.0

start:
	make envoy
	python -m main