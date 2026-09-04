using System.Runtime.CompilerServices;
using Onyx.Distribution.APIs.Filter;

internal class ILLicenseModule
{
	[MethodImpl(MethodImplOptions.NoInlining)]
	public ILLicenseModule()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetClient()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RateClient()
	{
		return true;
	}

	static ILLicenseModule()
	{
		Decorator.EnablePage();
	}
}
