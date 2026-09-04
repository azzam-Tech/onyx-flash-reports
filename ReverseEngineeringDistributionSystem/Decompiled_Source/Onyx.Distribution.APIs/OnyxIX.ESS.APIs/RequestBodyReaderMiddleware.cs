using System.Diagnostics;
using System.IO;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Onyx.Distribution.APIs.Filter;

namespace OnyxIX.ESS.APIs;

public class RequestBodyReaderMiddleware
{
	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CInvoke_003Ed__2 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder _003C_003Et__builder;

		public HttpContext context;

		public RequestBodyReaderMiddleware _003C_003E4__this;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

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
		internal static bool RestartClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CreateClient()
		{
			return true;
		}

		static _003CInvoke_003Ed__2()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CReadRequestBody_003Ed__3 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<string> _003C_003Et__builder;

		public HttpRequest request;

		private StreamReader _003Creader_003E5__2;

		private TaskAwaiter<string> _003C_003Eu__1;

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
		internal static bool ResetClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConcatClient()
		{
			return true;
		}

		static _003CReadRequestBody_003Ed__3()
		{
			Decorator.EnablePage();
		}
	}

	private readonly RequestDelegate m_Client;

	[MethodImpl(MethodImplOptions.NoInlining)]
	public RequestBodyReaderMiddleware(RequestDelegate next)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CInvoke_003Ed__2))]
	public Task Invoke(HttpContext context)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CReadRequestBody_003Ed__3))]
	private Task<string> CancelPage(HttpRequest P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public string CalculateHash(string bodyContent)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string CalculatePublicKeyFingerprint(string certificateFilePath)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string CalculatePublicKeyFingerprint(X509Certificate2 certificate)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ChangeCandidate()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CalcCandidate()
	{
		return true;
	}

	static RequestBodyReaderMiddleware()
	{
		Decorator.EnablePage();
	}
}
