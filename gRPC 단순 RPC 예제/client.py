from google.protobuf import wrappers_pb2
import grpc
import order_pb2
import order_pb2_grpc

import time

def run():
    ip = 'localhost'
    port = 50051
    channel = grpc.insecure_channel(f'{ip}:{port}')
    
    # 스텁 생성
    stub = order_pb2_grpc.OrderManagementStub(channel)
    
    order1 = order_pb2.Order(items=['Item - A', 'Item - B', 'Item - C'],
                             price=1000,
                             description='This is a Sample order - 1 : description.', 
                             destination='Seoul, Guro')
    
    order = stub.getOrder(order_pb2.Order(id='101'))
    print("Order service response", order)
    
    
if __name__ == '__main__':
    run()