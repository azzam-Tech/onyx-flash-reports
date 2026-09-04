using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Writers;

namespace System.Common;

[AttributeUsage(AttributeTargets.Assembly | AttributeTargets.Class | AttributeTargets.Struct | AttributeTargets.Enum | AttributeTargets.Method | AttributeTargets.Property | AttributeTargets.Field | AttributeTargets.Event | AttributeTargets.Interface | AttributeTargets.Parameter | AttributeTargets.Delegate, AllowMultiple = true, Inherited = false)]
[ComVisible(true)]
internal sealed class ClientRole : Attribute
{
	private bool _ConsumerWatcher;

	private bool m_RoleWatcher;

	private bool _TaskWatcher;

	private object _IdentifierWatcher;

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool LogoutUtils()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void CloneUtils(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool AddUtils()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void RestartUtils(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public string FlushUtils()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void SelectUtils(string P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public bool PrintUtils()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[SpecialName]
	public void PushUtils(bool P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public ClientRole()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PublishAdapter()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetupAdapter()
	{
		return true;
	}

	static ClientRole()
	{
		IssuerWatcherWriter.CustomizeUtils();
	}
}
