using System.Runtime.CompilerServices;
using System.Writers;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace Onyx.Distribution.Services.DependencyInjection;

public class DependencyInjection
{
	private readonly IConfiguration m_SystemWatcher;

	[MethodImpl(MethodImplOptions.NoInlining)]
	public DependencyInjection(IConfiguration configuration)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public void InjectDependencies(IServiceCollection services)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AwakeService()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool GetService()
	{
		return true;
	}

	static DependencyInjection()
	{
		IssuerWatcherWriter.CustomizeUtils();
	}
}
