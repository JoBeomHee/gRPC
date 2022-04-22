using Grpc.Core;
using Grpc.Core.Interceptors;

namespace gRPCInterceptorSample.Interceptors
{
    public class ValidationInterceptor : Interceptor
    {
        private readonly IValidatorLocator _locator;
        private readonly IValidatorErrorMessageHandler _handler;

        public ValidationInterceptor(IValidatorLocator locator, IValidatorErrorMessageHandler handler)
        {
            _locator = locator ?? throw new ArgumentNullException(nameof(locator));
            _handler = handler ?? throw new ArgumentNullException(nameof(handler));
        }

        private async Task _ValidateRequest<TRequest>(TRequest request) where TRequest : class
        {
            if (_locator.TryGetValidator<TRequest>(out var validator))
            {
                var results = await validator.ValidateAsync(request);

                if (!results.IsValid && results.Errors.Any())
                {
                    var message = await _handler.HandleAsync(results.Errors);
                    throw new RpcException(new Status(StatusCode.InvalidArgument, message));
                }
            }
        }

        public override async Task<TResponse> UnaryServerHandler<TRequest, TResponse>(
            TRequest request, 
            ServerCallContext context,
            UnaryServerMethod<TRequest, TResponse> continuation)
        {
            await _ValidateRequest(request);
            return await continuation(request, context);
        }
    }
}
