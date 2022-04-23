using Grpc.Core;
using Grpc.Net.Client;
using gRPCInterceptorSample;


using var channel = GrpcChannel.ForAddress("https://localhost:7081");

try
{
    var client = new Greeter.GreeterClient(channel);
    var reply = await client.SayHelloAsync(
        new HelloRequest { Name = "Beom12312312312312312312" }
        );

    Console.WriteLine($"Greeting {reply.Message}");
}
catch (RpcException exception) when (exception.StatusCode == StatusCode.InvalidArgument)
{
    Console.WriteLine($"Validator Inteceptor 에러가 발생했습니다.");
}
catch (Exception ex)
{
    Console.WriteLine(ex.Message);
}
