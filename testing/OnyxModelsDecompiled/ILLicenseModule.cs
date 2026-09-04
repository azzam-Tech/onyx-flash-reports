using System.Runtime.CompilerServices;
using Onyx.Containers;

internal class ILLicenseModule
{
	[MethodImpl(MethodImplOptions.NoInlining)]
	public ILLicenseModule()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool MoveExpression()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReadExpression()
	{
		return true;
	}

	static ILLicenseModule()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
