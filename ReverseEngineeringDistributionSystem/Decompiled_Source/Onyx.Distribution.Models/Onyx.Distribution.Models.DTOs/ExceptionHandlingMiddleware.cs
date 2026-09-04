using System.Diagnostics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using Onyx.Containers;

namespace Onyx.Distribution.Models.DTOs;

public class ExceptionHandlingMiddleware
{
	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CInvokeAsync_003Ed__3 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder _003C_003Et__builder;

		public ExceptionHandlingMiddleware _003C_003E4__this;

		public HttpContext context;

		private object _003C_003E7__wrap1;

		private int _003C_003E7__wrap2;

		private TaskAwaiter _003C_003Eu__1;

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
		internal static bool InvokeExpression()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ListExpression()
		{
			return true;
		}

		static _003CInvokeAsync_003Ed__3()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	private readonly RequestDelegate m_ServiceSetter;

	private readonly ILogger<ExceptionHandlingMiddleware> _ExporterSetter;

	[MethodImpl(MethodImplOptions.NoInlining)]
	public ExceptionHandlingMiddleware(RequestDelegate next, ILogger<ExceptionHandlingMiddleware> logger)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CInvokeAsync_003Ed__3))]
	public Task InvokeAsync(HttpContext context)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static Task CountClass(object P_0, object P_1)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool StartIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool UpdateIdentifier()
	{
		return true;
	}

	static ExceptionHandlingMiddleware()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
