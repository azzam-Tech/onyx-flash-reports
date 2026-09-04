using System.Runtime.CompilerServices;
using Onyx.Distribution.APIs.Filter;

namespace System.Containers;

internal class AuthenticationClientContainer
{
	internal static ModuleHandle m_Stub;

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static RuntimeTypeHandle e53w34m968awCm9P85taUZe(int token)
	{
		return m_Stub.GetRuntimeTypeHandleFromMetadataToken(token);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static RuntimeFieldHandle q3oMVe54wE47w4v68C7s2I(int token)
	{
		return m_Stub.GetRuntimeFieldHandleFromMetadataToken(token);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public AuthenticationClientContainer()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static AuthenticationClientContainer()
	{
		Decorator.EnablePage();
		m_Stub = typeof(AuthenticationClientContainer).Assembly.GetModules()[0].ModuleHandle;
	}

	internal static bool PatchObserver()
	{
		return true;
	}

	internal static bool ReflectObserver()
	{
		return false;
	}
}
