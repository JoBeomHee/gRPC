# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import order_pb2 as order__pb2


class OrderManagementStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getOrder = channel.unary_unary(
                '/ecommerce.OrderManagement/getOrder',
                request_serializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
                response_deserializer=order__pb2.Order.FromString,
                )


class OrderManagementServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderManagementServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.getOrder,
                    request_deserializer=google_dot_protobuf_dot_wrappers__pb2.StringValue.FromString,
                    response_serializer=order__pb2.Order.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ecommerce.OrderManagement', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrderManagement(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ecommerce.OrderManagement/getOrder',
            google_dot_protobuf_dot_wrappers__pb2.StringValue.SerializeToString,
            order__pb2.Order.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
