using System;
using System.Runtime.CompilerServices;
using System.Writers;

namespace Onyx.Distribution.Services.Filter;

internal class QueueDefinitionFilter
{
	internal static ModuleHandle valWatcher;

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static RuntimeTypeHandle e53w34m968awCm9P85taUZe(int token)
	{
		return valWatcher.GetRuntimeTypeHandleFromMetadataToken(token);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static RuntimeFieldHandle q3oMVe54wE47w4v68C7s2I(int token)
	{
		return valWatcher.GetRuntimeFieldHandleFromMetadataToken(token);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public QueueDefinitionFilter()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static QueueDefinitionFilter()
	{
		IssuerWatcherWriter.CustomizeUtils();
		valWatcher = typeof(QueueDefinitionFilter).Assembly.GetModules()[0].ModuleHandle;
	}

	internal static bool ComputeAdapter()
	{
		return true;
	}

	internal static bool CountAdapter()
	{
		return false;
	}
}
