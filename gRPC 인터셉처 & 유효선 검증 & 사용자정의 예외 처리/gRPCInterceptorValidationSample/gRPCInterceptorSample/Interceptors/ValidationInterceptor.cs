using Grpc.Core;
using Grpc.Core.Interceptors;
using System.Runtime.Serialization;

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
            try
            {
                await _ValidateRequest(request);
                return await continuation(request, context);
            }
            catch (CustomMessageException messageExteption)
            {
                throw new RpcException(new Status(StatusCode.InvalidArgument, "Customer is Terrible"));
            }
            catch(Exception exception)
            {
                throw new RpcException(new Status(StatusCode.Internal, exception.ToString()));
            }
        }
    }

    [Serializable]
    public class CustomMessageException : Exception
    {
        // 기본 생성자
        public CustomMessageException() : base() { }
        // 에러 메시지를 포함하는 생성자
        public CustomMessageException(string message) : base(message) { }
        // 에러 메시지와 내부 예외를 포함하는 생성자
        public CustomMessageException(string message, Exception e) : base(message, e) { }
        // 입력 스트림을 이용하는 생성자
        public CustomMessageException(SerializationInfo info, StreamingContext cxt) : base(info, cxt) { }
        public string ID
        {
            get; set;
        }
        public string Password
        {
            get; set;
        }
    }
}
