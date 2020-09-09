# Students Server
This repository is meant as a reference server when discussing certain issues with web-grpc client libraries. 

# Requirements
* docker
* `$ pip install -r requirements.txt`

# Runing and testing access
```
$ make run
$ grpcurl --plaintext -d '{}' localhost:50051 StudentService.GetStudentInfo
```