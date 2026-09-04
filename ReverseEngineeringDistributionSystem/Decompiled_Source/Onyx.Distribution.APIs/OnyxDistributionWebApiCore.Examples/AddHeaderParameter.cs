using System.Runtime.CompilerServices;
using Microsoft.OpenApi.Models;
using Onyx.Distribution.APIs.Filter;
using Swashbuckle.AspNetCore.SwaggerGen;

namespace OnyxDistributionWebApiCore.Examples;

public class AddHeaderParameter : IOperationFilter
{
	[MethodImpl(MethodImplOptions.NoInlining)]
	public void Apply(OpenApiOperation operation, OperationFilterContext context)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public AddHeaderParameter()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ComputeCandidate()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CountCandidate()
	{
		return true;
	}

	static AddHeaderParameter()
	{
		Decorator.EnablePage();
	}
}
