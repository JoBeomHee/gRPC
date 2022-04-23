using FluentValidation;

namespace gRPCInterceptorSample.Interceptors
{
    public interface IValidatorLocator
    {
        bool TryGetValidator<TRequest>(out IValidator<TRequest> result) where TRequest : class;
    }
}
