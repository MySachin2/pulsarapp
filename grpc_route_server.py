import grpc
from concurrent import futures
import time
import proto.route_pb2_grpc as pb2_grpc
import proto.route_pb2 as pb2
from grpc_reflection.v1alpha import reflection

class RouteService(pb2_grpc.RouteGuideServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetFeature(self, request, context):
        latitude = request.latitude
        longitude = request.longitude
        return pb2.Feature(name="Get Feature", location=pb2.Point(
            latitude=latitude,
            longitude=longitude,
        ))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_RouteGuideServicer_to_server(RouteService(), server)
    port = 8999
    server.add_insecure_port(f'[::]:{port}')
    SERVICE_NAMES = (
        pb2.DESCRIPTOR.services_by_name['RouteGuide'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    print(f'Running GRPC Server at port {port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()