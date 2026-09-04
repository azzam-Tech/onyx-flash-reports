using System.Diagnostics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Threading.Tasks;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class SignalRClass
{
	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003Csingal_003Ed__0 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder _003C_003Et__builder;

		[MethodImpl(MethodImplOptions.NoInlining)]
		private void MoveNext()
		{
		}

		void IAsyncStateMachine.MoveNext()
		{
			//ILSpy generated this explicit interface implementation from .override directive in MoveNext
			this.MoveNext();
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		[DebuggerHidden]
		private void SetStateMachine(IAsyncStateMachine stateMachine)
		{
		}

		void IAsyncStateMachine.SetStateMachine(IAsyncStateMachine stateMachine)
		{
			//ILSpy generated this explicit interface implementation from .override directive in SetStateMachine
			this.SetStateMachine(stateMachine);
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrintExpression()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalculateExpression()
		{
			return true;
		}

		static _003Csingal_003Ed__0()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003Csingal_003Ed__0))]
	private static Task PopClass()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public SignalRClass()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PrepareExpression()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool FlushExpression()
	{
		return true;
	}

	static SignalRClass()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
