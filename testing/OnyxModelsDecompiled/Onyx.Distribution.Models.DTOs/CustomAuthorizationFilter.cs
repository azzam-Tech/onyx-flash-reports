using System.Diagnostics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Authorization.Policy;
using Microsoft.AspNetCore.Mvc.Filters;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class CustomAuthorizationFilter : ActionFilterAttribute, IAsyncAuthorizationFilter, IFilterMetadata
{
	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003COnAuthorizationAsync_003Ed__4 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder _003C_003Et__builder;

		public AuthorizationFilterContext context;

		public CustomAuthorizationFilter _003C_003E4__this;

		private IPolicyEvaluator _003CpolicyEvaluator_003E5__2;

		private TaskAwaiter<AuthenticateResult> _003C_003Eu__1;

		private TaskAwaiter<PolicyAuthorizationResult> _003C_003Eu__2;

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
		internal static bool InsertExpression()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ViewExpression()
		{
			return true;
		}

		static _003COnAuthorizationAsync_003Ed__4()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	[CompilerGenerated]
	private readonly AuthorizationPolicy m_InstanceWriter;

	public AuthorizationPolicy Policy
	{
		[MethodImpl(MethodImplOptions.NoInlining)]
		[CompilerGenerated]
		get
		{
			return null;
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public CustomAuthorizationFilter()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003COnAuthorizationAsync_003Ed__4))]
	public Task OnAuthorizationAsync(AuthorizationFilterContext context)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool PublishAuthentication()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool SetupAuthentication()
	{
		return true;
	}

	static CustomAuthorizationFilter()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
