using System;
using System.Runtime.CompilerServices;
using Onyx.Containers;

namespace Onyx.Common;

internal class ProcessRepository
{
	internal static ModuleHandle m_RuleRepository;

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static RuntimeTypeHandle e53w34m968awCm9P85taUZe(int token)
	{
		return m_RuleRepository.GetRuntimeTypeHandleFromMetadataToken(token);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static RuntimeFieldHandle q3oMVe54wE47w4v68C7s2I(int token)
	{
		return m_RuleRepository.GetRuntimeFieldHandleFromMetadataToken(token);
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public ProcessRepository()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static ProcessRepository()
	{
		ThreadIndexerContainer.IncludeClass();
		m_RuleRepository = typeof(ProcessRepository).Assembly.GetModules()[0].ModuleHandle;
	}

	internal static bool CreateExpression()
	{
		return true;
	}

	internal static bool ResetExpression()
	{
		return false;
	}
}
