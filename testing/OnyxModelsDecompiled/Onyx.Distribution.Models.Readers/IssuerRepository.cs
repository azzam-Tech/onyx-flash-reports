using System;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using Onyx.Containers;

namespace Onyx.Distribution.Models.Readers;

[AttributeUsage(AttributeTargets.Assembly | AttributeTargets.Class | AttributeTargets.Struct | AttributeTargets.Enum | AttributeTargets.Method | AttributeTargets.Property | AttributeTargets.Field | AttributeTargets.Event | AttributeTargets.Interface | AttributeTargets.Parameter | AttributeTargets.Delegate, AllowMultiple = true, Inherited = false)]
[ComVisible(true)]
internal sealed class IssuerRepository : Attribute
{
	private bool m_MappingRepository;

	private bool parameterRepository;

	private bool _OrderRepository;

	private object _ParamsRepository;

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool InterruptClass()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void MoveClass(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool ChangeClass()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void DeleteClass(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public string CancelClass()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void LoginClass(string P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool StopClass()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void SetClass(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public IssuerRepository()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool VisitExpression()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetExpression()
	{
		return true;
	}

	static IssuerRepository()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
