using Grpc.Net.Client;
using gRPCInterceptor;

var channel = GrpcChannel.ForAddress("https://localhost:7063");
var greeterClient = new Greeter.GreeterClient(channel);

var reply = await greeterClient.SayHelloAsync(new HelloRequest { Name = "Beom" });

Console.WriteLine(reply.Message);