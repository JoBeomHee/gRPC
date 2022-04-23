using FluentValidation;
using gRPCInterceptorSample.Interceptors;

namespace gRPCInterceptorSample.Validations.Account
{
    public class UserValidator : BaseValidator<HelloRequest>
    {
        public UserValidator(IConfiguration configuration) : base(configuration)
        {
            RuleFor(greeter => greeter.Name).Length(1, 5).OnAnyFailure(x =>
            {
                throw new CustomMessageException("Customer Exception 발생함");
            });
        }
    }
}

public class BaseValidator<T> : AbstractValidator<T> where T : class
{
    protected readonly IConfiguration Configuration;

    public BaseValidator(IConfiguration configuration)
    {
        Configuration = configuration ?? throw new ArgumentNullException();
    }
}