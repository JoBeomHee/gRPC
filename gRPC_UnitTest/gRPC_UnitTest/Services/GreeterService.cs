using Grpc.Core;

namespace gRPC_UnitTest.Services
{
    public class GreeterService : Greeter.GreeterBase
    {
        private readonly ILogger<GreeterService> _logger;
        private readonly IGreeter _service;
        public GreeterService(ILogger<GreeterService> logger, IGreeter service)
        {
            _logger = logger;
            _service = service;
        }

        public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
        {

            var result = _service.Greet(request.Name);

            return Task.FromResult(new HelloReply
            {
                Message = result
            });
        }
    }
}