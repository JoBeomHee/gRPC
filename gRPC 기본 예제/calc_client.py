import grpc

import calc_pb2
import calc_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50050')
    stub = calc_pb2_grpc.CalculatorStub(channel)
    
    respones = stub.Add(calc_pb2.AddRequest(n1=20, n2=10))
    print(respones.n1)
    
    respones = stub.Substract(calc_pb2.SubstractRequest(n1=20, n2=10))
    print(respones.n1)
    
    respones = stub.Multiply(calc_pb2.MultiplyRequest(n1=20, n2=10))
    print(respones.n1)
    
    respones = stub.Divide(calc_pb2.DivideRequest(n1=10, n2=2))
    print(respones.f1)
    
if __name__ == '__main__':
    run()