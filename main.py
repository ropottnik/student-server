from concurrent import futures

import grpc

from Students_pb2 import StudentResponse
from grpc_reflection.v1alpha import reflection
import Students_pb2_grpc
import Students_pb2


class StudentServer(Students_pb2_grpc.StudentServiceServicer):
    def GetStudentInfo(self, request, context):
        return StudentResponse(
            firstName="Thomas",
            lastName="Winkler",
            major="Anthropology",
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Students_pb2_grpc.add_StudentServiceServicer_to_server(
        StudentServer(), server)
    SERVICE_NAMES = (
        Students_pb2.DESCRIPTOR.services_by_name['StudentService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
