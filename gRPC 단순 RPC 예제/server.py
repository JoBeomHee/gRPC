from concurrent import futures
import time

import uuid
from google.protobuf import wrappers_pb2

import grpc
import order_pb2
import order_pb2_grpc

class OrderManagementServicer(order_pb2_grpc.OrderManagementServicer):
    
    def __init__(self):
        self.orderDict = {}
        
        self.orderDict['101'] = order_pb2.Order(id='101', 
                                                price=1000, 
                                                items=['Item - A', 'Item - B'], 
                                                description='Sample order description.',
                                                destination='Seoul')
        
    
    def getOrder(self, request, context):
        order = self.orderDict.get(request.value)
        
        if order is not None: 
            print(f'{request.value} 주문이 성공적으로 이루어졌습니다.')
            return order
        else: 
            # Error handling 
            print('Order not found ' + request.value)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Order : ', request.value, ' Not Found.')
            return order_management_pb2.Order()

# Server gRPC 생성
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
order_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
print('서버 시작. 포트 열림 50051.')
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()