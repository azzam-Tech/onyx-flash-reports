using System;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using Onyx.Distribution.APIs.Filter;

namespace Onyx.Distribution.APIs.Serialization;

[ComVisible(true)]
[AttributeUsage(AttributeTargets.Assembly | AttributeTargets.Class | AttributeTargets.Struct | AttributeTargets.Enum | AttributeTargets.Method | AttributeTargets.Property | AttributeTargets.Field | AttributeTargets.Event | AttributeTargets.Interface | AttributeTargets.Parameter | AttributeTargets.Delegate, AllowMultiple = true, Inherited = false)]
internal sealed class PropertyValueSerializer : Attribute
{
	private bool broadcaster;

	private bool parameter;

	private bool m_Annotation;

	private object _Resolver;

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool RunPage()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void StartPage(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool AddPage()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void SetupPage(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public string CheckPage()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void QueryPage(string P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool ReadPage()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void ComparePage(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public PropertyValueSerializer()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CustomizeObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ValidateObserver()
	{
		return true;
	}

	static PropertyValueSerializer()
	{
		Decorator.EnablePage();
	}
}
