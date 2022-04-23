using FluentValidation.Results;

namespace gRPCInterceptorSample.Interceptors
{
    public interface IValidatorErrorMessageHandler
    {
        Task<string> HandleAsync(IList<ValidationFailure> failures);
    }
}
