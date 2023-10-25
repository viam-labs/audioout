buf-generate:
	buf generate --template ./src/audioout/proto/buf.gen.yaml ./src/audioout/proto -o ./src/audioout/proto

bundle:
	tar -czf module.tar.gz *.sh .env src requirements.txt

upload:
	viam module upload --version $(version) --platform linux/arm64 module.tar.gz
	viam module upload --version $(version) --platform darwin/arm64 module.tar.gz
	viam module upload --version $(version) --platform darwin/amd64 module.tar.gz

clean:
	rm module.tar.gz

publish: bundle upload clean
