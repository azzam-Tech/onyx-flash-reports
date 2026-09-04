using System.Runtime.CompilerServices;
using System.Writers;

internal class ILLicenseModule
{
	[MethodImpl(MethodImplOptions.NoInlining)]
	public ILLicenseModule()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FindAdapter()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PatchAdapter()
	{
		return true;
	}

	static ILLicenseModule()
	{
		IssuerWatcherWriter.CustomizeUtils();
	}
}
