using System.Diagnostics;
using System.IO;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using Onyx.Distribution.APIs.Filter;
using Onyx.Distribution.Models.MainDTOs;
using Onyx.Distribution.Services.Services.IServices;
using Onyx.IX.Distribution.Track.Models.DTOs;

namespace Onyx.Distribution.APIs.Controllers;

[Route("Service1.svc")]
[ApiController]
public class DistributionController : ControllerBase
{
	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CCheckSetup_003Ed__99 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool GetCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DisableCandidate()
		{
			return true;
		}

		static _003CCheckSetup_003Ed__99()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CClosedPlan_003Ed__37 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public string DOC_SER;

		public int VerNo;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool CancelCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RemoveCandidate()
		{
			return true;
		}

		static _003CClosedPlan_003Ed__37()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CDocDescription_003Ed__24 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<DocDescriptionObjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private TaskAwaiter<DocDescriptionObjctResult> _003C_003Eu__1;

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
		internal static bool InterruptCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MapCandidate()
		{
			return true;
		}

		static _003CDocDescription_003Ed__24()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CDocsTransferMatching_003Ed__73 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool DefineCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ForgotCandidate()
		{
			return true;
		}

		static _003CDocsTransferMatching_003Ed__73()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGeoLocations_003Ed__43 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeoLocationResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int S_Row;

		public int E_Row;

		private TaskAwaiter<GeoLocationResult> _003C_003Eu__1;

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
		internal static bool FillCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SearchCandidate()
		{
			return true;
		}

		static _003CGeoLocations_003Ed__43()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountConfirmBalances_003Ed__145 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool EnableCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InsertCandidate()
		{
			return true;
		}

		static _003CGetAccountConfirmBalances_003Ed__145()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountStatementConfirm_003Ed__154 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ViewCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InvokeCandidate()
		{
			return true;
		}

		static _003CGetAccountStatementConfirm_003Ed__154()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountStatment_003Ed__74 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ListCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrintCandidate()
		{
			return true;
		}

		static _003CGetAccountStatment_003Ed__74()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountStatmentDetails_003Ed__75 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CalculateCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SelectCandidate()
		{
			return true;
		}

		static _003CGetAccountStatmentDetails_003Ed__75()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAllTaxItems_003Ed__92 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CompareCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ManageCandidate()
		{
			return true;
		}

		static _003CGetAllTaxItems_003Ed__92()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAnswerQuestionnaireQuestions_003Ed__86 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ReadCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RunCandidate()
		{
			return true;
		}

		static _003CGetAnswerQuestionnaireQuestions_003Ed__86()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAvlQtyOnline_003Ed__141 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool RegisterCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool NewCandidate()
		{
			return true;
		}

		static _003CGetAvlQtyOnline_003Ed__141()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBanksCurrenciesDetails_003Ed__13 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetBanksCurrenciesDetailsOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetBanksCurrenciesDetailsOBjctResult> _003C_003Eu__1;

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
		internal static bool TestCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CollectCandidate()
		{
			return true;
		}

		static _003CGetBanksCurrenciesDetails_003Ed__13()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBanksDetails_003Ed__12 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetBanksDetailsOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetBanksDetailsOBjctResult> _003C_003Eu__1;

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
		internal static bool LogoutCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LoginCandidate()
		{
			return true;
		}

		static _003CGetBanksDetails_003Ed__12()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillDataForPrint_003Ed__167 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<ResponceObject> _003C_003Eu__1;

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
		internal static bool QueryCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InitCandidate()
		{
			return true;
		}

		static _003CGetBillDataForPrint_003Ed__167()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillForNote_003Ed__165 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool RestartCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CreateCandidate()
		{
			return true;
		}

		static _003CGetBillForNote_003Ed__165()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillMasterData_003Ed__76 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ResetCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConcatCandidate()
		{
			return true;
		}

		static _003CGetBillMasterData_003Ed__76()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillQrData_003Ed__161 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<ResponceObject> _003C_003Eu__1;

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
		internal static bool StopCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool VisitCandidate()
		{
			return true;
		}

		static _003CGetBillQrData_003Ed__161()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillSalesCharges_003Ed__131 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool SetCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RateCandidate()
		{
			return true;
		}

		static _003CGetBillSalesCharges_003Ed__131()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBrachesData_003Ed__23 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetBrachesDataOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int User_Id;

		public int VerNo;

		private TaskAwaiter<GetBrachesDataOBjctResult> _003C_003Eu__1;

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
		internal static bool InstantiateCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AddCandidate()
		{
			return true;
		}

		static _003CGetBrachesData_003Ed__23()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBrnchUserPriv_003Ed__47 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetBrnchUserPrivResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string User_No;

		public int VerNo;

		private TaskAwaiter<GetBrnchUserPrivResult> _003C_003Eu__1;

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
		internal static bool RevertCandidate()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DestroyAdvisor()
		{
			return true;
		}

		static _003CGetBrnchUserPriv_003Ed__47()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCalcTaxType_003Ed__93 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PrepareAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FlushAdvisor()
		{
			return true;
		}

		static _003CGetCalcTaxType_003Ed__93()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCashCurrenciesDetails_003Ed__15 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCashCurrenciesDetailsOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetCashCurrenciesDetailsOBjctResult> _003C_003Eu__1;

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
		internal static bool CheckAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SortAdvisor()
		{
			return true;
		}

		static _003CGetCashCurrenciesDetails_003Ed__15()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCashCustomer_003Ed__136 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PushAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FindAdvisor()
		{
			return true;
		}

		static _003CGetCashCustomer_003Ed__136()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCashDetails_003Ed__14 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCashDetailsOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetCashDetailsOBjctResult> _003C_003Eu__1;

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
		internal static bool PatchAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReflectAdvisor()
		{
			return true;
		}

		static _003CGetCashDetails_003Ed__14()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCreditCardTypes_003Ed__89 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CustomizeAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ValidateAdvisor()
		{
			return true;
		}

		static _003CGetCreditCardTypes_003Ed__89()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCshBlncWithLmt_003Ed__52 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public string Date;

		public int VerNo;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ConnectAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool WriteAdvisor()
		{
			return true;
		}

		static _003CGetCshBlncWithLmt_003Ed__52()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCurrncy_003Ed__10 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCurrncyOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int type_no;

		public string REP_CODE;

		public int VerNo;

		public string C_Code;

		private TaskAwaiter<GetCurrncyOBjctResult> _003C_003Eu__1;

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
		internal static bool OrderAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StartAdvisor()
		{
			return true;
		}

		static _003CGetCurrncy_003Ed__10()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustCreditPreiod_003Ed__42 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<CustCreditPreiodResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int VerNo;

		public string C_CODE;

		private TaskAwaiter<CustCreditPreiodResult> _003C_003Eu__1;

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
		internal static bool UpdateAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool VerifyAdvisor()
		{
			return true;
		}

		static _003CGetCustCreditPreiod_003Ed__42()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerClassData_003Ed__81 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PopAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ComputeAdvisor()
		{
			return true;
		}

		static _003CGetCustomerClassData_003Ed__81()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerCostCenter_003Ed__135 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CountAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AssetAdvisor()
		{
			return true;
		}

		static _003CGetCustomerCostCenter_003Ed__135()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerItemLimitSales_003Ed__130 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CallAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PublishAdvisor()
		{
			return true;
		}

		static _003CGetCustomerItemLimitSales_003Ed__130()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerItemSold_003Ed__172 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<ResponceObject> _003C_003Eu__1;

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
		internal static bool SetupAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ChangeAdvisor()
		{
			return true;
		}

		static _003CGetCustomerItemSold_003Ed__172()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerItemsAvailableQuantity_003Ed__158 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CalcAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResolveAdvisor()
		{
			return true;
		}

		static _003CGetCustomerItemsAvailableQuantity_003Ed__158()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerLimitSales_003Ed__129 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ExcludeAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool IncludeAdvisor()
		{
			return true;
		}

		static _003CGetCustomerLimitSales_003Ed__129()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerPlanTarget_003Ed__152 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool DeleteAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PostAdvisor()
		{
			return true;
		}

		static _003CGetCustomerPlanTarget_003Ed__152()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerStock_003Ed__173 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool AwakeAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool GetAdvisor()
		{
			return true;
		}

		static _003CGetCustomerStock_003Ed__173()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomers_003Ed__11 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCustomersOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetCustomersOBjctResult> _003C_003Eu__1;

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
		internal static bool DisableAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CancelAdvisor()
		{
			return true;
		}

		static _003CGetCustomers_003Ed__11()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomersTargetData_003Ed__98 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool RemoveAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InterruptAdvisor()
		{
			return true;
		}

		static _003CGetCustomersTargetData_003Ed__98()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocBillsData_003Ed__48 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetDocBillsDataResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int BILL_DOC_TYPE;

		public string BILL_NO;

		public int VerNo;

		private TaskAwaiter<GetDocBillsDataResult> _003C_003Eu__1;

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
		internal static bool MapAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DefineAdvisor()
		{
			return true;
		}

		static _003CGetDocBillsData_003Ed__48()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocDtls_003Ed__123 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ForgotAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FillAdvisor()
		{
			return true;
		}

		static _003CGetDocDtls_003Ed__123()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocInfoData_003Ed__104 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool SearchAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool EnableAdvisor()
		{
			return true;
		}

		static _003CGetDocInfoData_003Ed__104()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocMst_003Ed__122 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool InsertAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ViewAdvisor()
		{
			return true;
		}

		static _003CGetDocMst_003Ed__122()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocTypes_003Ed__22 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetDocTypesOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int User_Id;

		public int VerNo;

		private TaskAwaiter<GetDocTypesOBjctResult> _003C_003Eu__1;

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
		internal static bool InvokeAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ListAdvisor()
		{
			return true;
		}

		static _003CGetDocTypes_003Ed__22()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocsSyncMethode_003Ed__96 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PrintAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalculateAdvisor()
		{
			return true;
		}

		static _003CGetDocsSyncMethode_003Ed__96()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDtsAccountStatmenDocDtl_003Ed__112 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool SelectAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CompareAdvisor()
		{
			return true;
		}

		static _003CGetDtsAccountStatmenDocDtl_003Ed__112()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDtsCstAging_003Ed__97 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ManageAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CloneAdvisor()
		{
			return true;
		}

		static _003CGetDtsCstAging_003Ed__97()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDtsDynamicScreenFileds_003Ed__115 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool MoveAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReadAdvisor()
		{
			return true;
		}

		static _003CGetDtsDynamicScreenFileds_003Ed__115()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDtsExpnsTypes_003Ed__102 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool RunAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RegisterAdvisor()
		{
			return true;
		}

		static _003CGetDtsExpnsTypes_003Ed__102()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetExtraScreenLabel_003Ed__134 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool NewAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool TestAdvisor()
		{
			return true;
		}

		static _003CGetExtraScreenLabel_003Ed__134()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFieldPrivilege_003Ed__162 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CollectAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LogoutAdvisor()
		{
			return true;
		}

		static _003CGetFieldPrivilege_003Ed__162()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFormsPrivilege_003Ed__28 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetFormsPrivilegeResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int User_Id;

		public int VerNo;

		private TaskAwaiter<GetFormsPrivilegeResult> _003C_003Eu__1;

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
		internal static bool LoginAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool QueryAdvisor()
		{
			return true;
		}

		static _003CGetFormsPrivilege_003Ed__28()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFreeSampleMovement_003Ed__157 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool InitAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RestartAdvisor()
		{
			return true;
		}

		static _003CGetFreeSampleMovement_003Ed__157()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFunctionData_003Ed__137 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CreateAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResetAdvisor()
		{
			return true;
		}

		static _003CGetFunctionData_003Ed__137()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGeneralInputData_003Ed__163 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ConcatAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StopAdvisor()
		{
			return true;
		}

		static _003CGetGeneralInputData_003Ed__163()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGlRequestData_003Ed__170 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<ResponceObject> _003C_003Eu__1;

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
		internal static bool VisitAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetAdvisor()
		{
			return true;
		}

		static _003CGetGlRequestData_003Ed__170()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGnrTaxCode_003Ed__50 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetGnrTaxCodeResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private TaskAwaiter<GetGnrTaxCodeResult> _003C_003Eu__1;

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
		internal static bool RateAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InstantiateAdvisor()
		{
			return true;
		}

		static _003CGetGnrTaxCode_003Ed__50()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGnrTaxItems_003Ed__51 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetGnrTaxItemsResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string Rep_Code;

		public int S_row;

		public int L_row;

		public int VerNo;

		private TaskAwaiter<GetGnrTaxItemsResult> _003C_003Eu__1;

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
		internal static bool AddAdvisor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RevertAdvisor()
		{
			return true;
		}

		static _003CGetGnrTaxItems_003Ed__51()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGroupDetails_003Ed__77 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool DestroyVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrepareVisitor()
		{
			return true;
		}

		static _003CGetGroupDetails_003Ed__77()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetInstallmentBills_003Ed__78 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool FlushVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CheckVisitor()
		{
			return true;
		}

		static _003CGetInstallmentBills_003Ed__78()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetInvSerialParameter_003Ed__34 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetInvSerialParameterObjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int VerNo;

		private TaskAwaiter<GetInvSerialParameterObjctResult> _003C_003Eu__1;

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
		internal static bool SortVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PushVisitor()
		{
			return true;
		}

		static _003CGetInvSerialParameter_003Ed__34()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetInventroyTypes_003Ed__32 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetInventroyTypesOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int VerNo;

		private TaskAwaiter<GetInventroyTypesOBjctResult> _003C_003Eu__1;

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
		internal static bool FindVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PatchVisitor()
		{
			return true;
		}

		static _003CGetInventroyTypes_003Ed__32()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemCount_003Ed__27 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemCountResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int Type_No;

		public int VerNo;

		public int W_Code;

		private TaskAwaiter<GetItemCountResult> _003C_003Eu__1;

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
		internal static bool ReflectVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CustomizeVisitor()
		{
			return true;
		}

		static _003CGetItemCount_003Ed__27()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemSerialsData_003Ed__84 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ValidateVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConnectVisitor()
		{
			return true;
		}

		static _003CGetItemSerialsData_003Ed__84()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsBarcode_003Ed__30 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsBarcodeOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int VerNo;

		private TaskAwaiter<GetItemsBarcodeOBjctResult> _003C_003Eu__1;

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
		internal static bool WriteVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool OrderVisitor()
		{
			return true;
		}

		static _003CGetItemsBarcode_003Ed__30()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsBarcodeData_003Ed__100 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool StartVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool UpdateVisitor()
		{
			return true;
		}

		static _003CGetItemsBarcodeData_003Ed__100()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsDataByWHTransferNo_003Ed__60 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool VerifyVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PopVisitor()
		{
			return true;
		}

		static _003CGetItemsDataByWHTransferNo_003Ed__60()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsDetailsPaging_003Ed__16 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsDetailsOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int GRP_CODE;

		public string REP_CODE;

		public int S_row;

		public int L_row;

		public int VerNo;

		private TaskAwaiter<GetItemsDetailsOBjctResult> _003C_003Eu__1;

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
		internal static bool ComputeVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CountVisitor()
		{
			return true;
		}

		static _003CGetItemsDetailsPaging_003Ed__16()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsGroupsData_003Ed__88 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool AssetVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CallVisitor()
		{
			return true;
		}

		static _003CGetItemsGroupsData_003Ed__88()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsMarktProperty_003Ed__126 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PublishVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetupVisitor()
		{
			return true;
		}

		static _003CGetItemsMarktProperty_003Ed__126()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsPriceLevelsPaging_003Ed__26 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsPriceLevelsResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int S_row;

		public int L_row;

		public int VerNo;

		private TaskAwaiter<GetItemsPriceLevelsResult> _003C_003Eu__1;

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
		internal static bool ChangeVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalcVisitor()
		{
			return true;
		}

		static _003CGetItemsPriceLevelsPaging_003Ed__26()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsPrices_003Ed__33 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsPriceOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int Lvl_No;

		public int VerNo;

		private TaskAwaiter<GetItemsPriceOBjctResult> _003C_003Eu__1;

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
		internal static bool ResolveVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ExcludeVisitor()
		{
			return true;
		}

		static _003CGetItemsPrices_003Ed__33()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsStorage_003Ed__31 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsStorageOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int VerNo;

		private TaskAwaiter<GetItemsStorageOBjctResult> _003C_003Eu__1;

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
		internal static bool IncludeVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DeleteVisitor()
		{
			return true;
		}

		static _003CGetItemsStorage_003Ed__31()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetKey_003Ed__58 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PostVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AwakeVisitor()
		{
			return true;
		}

		static _003CGetKey_003Ed__58()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetLevelPrices_003Ed__35 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetLevelPriceOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int VerNo;

		private TaskAwaiter<GetLevelPriceOBjctResult> _003C_003Eu__1;

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
		internal static bool GetVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DisableVisitor()
		{
			return true;
		}

		static _003CGetLevelPrices_003Ed__35()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMandatoryField_003Ed__140 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CancelVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RemoveVisitor()
		{
			return true;
		}

		static _003CGetMandatoryField_003Ed__140()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMarktVisitFlag_003Ed__127 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool InterruptVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MapVisitor()
		{
			return true;
		}

		static _003CGetMarktVisitFlag_003Ed__127()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMeasurments_003Ed__17 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetMeasurmentsOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public int VerNo;

		private TaskAwaiter<GetMeasurmentsOBjctResult> _003C_003Eu__1;

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
		internal static bool DefineVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ForgotVisitor()
		{
			return true;
		}

		static _003CGetMeasurments_003Ed__17()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMessageDetails_003Ed__148 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool FillVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SearchVisitor()
		{
			return true;
		}

		static _003CGetMessageDetails_003Ed__148()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMobileRequest_003Ed__121 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool EnableVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InsertVisitor()
		{
			return true;
		}

		static _003CGetMobileRequest_003Ed__121()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetParameters_003Ed__21 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetParametersObjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string Rep_Code;

		public int VerNo;

		public int BrnNo;

		private TaskAwaiter<GetParametersObjctResult> _003C_003Eu__1;

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
		internal static bool ViewVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InvokeVisitor()
		{
			return true;
		}

		static _003CGetParameters_003Ed__21()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetPlanDetails_003Ed__18 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetPlanDetailsOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string REP_CODE;

		public string PLAN_DATE;

		public int VerNo;

		public string DOC_SER;

		public string LANG_NO;

		private TaskAwaiter<GetPlanDetailsOBjctResult> _003C_003Eu__1;

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
		internal static bool ListVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrintVisitor()
		{
			return true;
		}

		static _003CGetPlanDetails_003Ed__18()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetPriceLevels_003Ed__25 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetPriceLevelsResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetPriceLevelsResult> _003C_003Eu__1;

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
		internal static bool CalculateVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SelectVisitor()
		{
			return true;
		}

		static _003CGetPriceLevels_003Ed__25()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQuestionnaireQuestions_003Ed__85 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CompareVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ManageVisitor()
		{
			return true;
		}

		static _003CGetQuestionnaireQuestions_003Ed__85()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmDtlData_003Ed__79 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CloneVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MoveVisitor()
		{
			return true;
		}

		static _003CGetQutPrmDtlData_003Ed__79()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmDtlData_OLD_003Ed__54 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ReadVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RunVisitor()
		{
			return true;
		}

		static _003CGetQutPrmDtlData_OLD_003Ed__54()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmGrpDtlData_003Ed__56 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool RegisterVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool NewVisitor()
		{
			return true;
		}

		static _003CGetQutPrmGrpDtlData_003Ed__56()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmGrpMstData_003Ed__57 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool TestVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CollectVisitor()
		{
			return true;
		}

		static _003CGetQutPrmGrpMstData_003Ed__57()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmMstData_003Ed__53 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool LogoutVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LoginVisitor()
		{
			return true;
		}

		static _003CGetQutPrmMstData_003Ed__53()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmSubDtlData_003Ed__55 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool QueryVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InitVisitor()
		{
			return true;
		}

		static _003CGetQutPrmSubDtlData_003Ed__55()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReportAsPdfFromOnyx_003Ed__171 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<ResponceObject> _003C_003Eu__1;

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
		internal static bool RestartVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CreateVisitor()
		{
			return true;
		}

		static _003CGetReportAsPdfFromOnyx_003Ed__171()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReturnFromBill_003Ed__90 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ResetVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConcatVisitor()
		{
			return true;
		}

		static _003CGetReturnFromBill_003Ed__90()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReturnFromBillDetails_003Ed__91 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool StopVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool VisitVisitor()
		{
			return true;
		}

		static _003CGetReturnFromBillDetails_003Ed__91()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReturnFromRtRqst_003Ed__113 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool SetVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RateVisitor()
		{
			return true;
		}

		static _003CGetReturnFromRtRqst_003Ed__113()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReturnFromRtRqstDetails_003Ed__114 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool InstantiateVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AddVisitor()
		{
			return true;
		}

		static _003CGetReturnFromRtRqstDetails_003Ed__114()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSFlagCode_003Ed__133 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool RevertVisitor()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DestroyVal()
		{
			return true;
		}

		static _003CGetSFlagCode_003Ed__133()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesCharges_003Ed__49 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetSales_ChargesResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private TaskAwaiter<GetSales_ChargesResult> _003C_003Eu__1;

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
		internal static bool PrepareVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FlushVal()
		{
			return true;
		}

		static _003CGetSalesCharges_003Ed__49()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesFreeQty_003Ed__40 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetSalesFreeQtyOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetSalesFreeQtyOBjctResult> _003C_003Eu__1;

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
		internal static bool CheckVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SortVal()
		{
			return true;
		}

		static _003CGetSalesFreeQty_003Ed__40()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesInfo_003Ed__142 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PushVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FindVal()
		{
			return true;
		}

		static _003CGetSalesInfo_003Ed__142()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesManBranchPrivilege_003Ed__144 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PatchVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReflectVal()
		{
			return true;
		}

		static _003CGetSalesManBranchPrivilege_003Ed__144()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesManDocumentMovement_003Ed__138 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CustomizeVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ValidateVal()
		{
			return true;
		}

		static _003CGetSalesManDocumentMovement_003Ed__138()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesManItemMovement_003Ed__139 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ConnectVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool WriteVal()
		{
			return true;
		}

		static _003CGetSalesManItemMovement_003Ed__139()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesOrderDtl_003Ed__108 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool OrderVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StartVal()
		{
			return true;
		}

		static _003CGetSalesOrderDtl_003Ed__108()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesOrderMst_003Ed__107 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool UpdateVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool VerifyVal()
		{
			return true;
		}

		static _003CGetSalesOrderMst_003Ed__107()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesSerialNo_003Ed__120 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PopVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ComputeVal()
		{
			return true;
		}

		static _003CGetSalesSerialNo_003Ed__120()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSales_discount_003Ed__39 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetSales_discountOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetSales_discountOBjctResult> _003C_003Eu__1;

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
		internal static bool CountVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AssetVal()
		{
			return true;
		}

		static _003CGetSales_discount_003Ed__39()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSmanDailayPlan_003Ed__132 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CallVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PublishVal()
		{
			return true;
		}

		static _003CGetSmanDailayPlan_003Ed__132()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSmanPlanTrgt_003Ed__101 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool SetupVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ChangeVal()
		{
			return true;
		}

		static _003CGetSmanPlanTrgt_003Ed__101()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetStorage_Br_003Ed__19 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetStorageOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetStorageOBjctResult> _003C_003Eu__1;

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
		internal static bool CalcVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResolveVal()
		{
			return true;
		}

		static _003CGetStorage_Br_003Ed__19()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetStorage_Br_Paging_003Ed__20 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetStorageOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string REP_CODE;

		public int S_row;

		public int L_row;

		public int VerNo;

		private TaskAwaiter<GetStorageOBjctResult> _003C_003Eu__1;

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
		internal static bool ExcludeVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool IncludeVal()
		{
			return true;
		}

		static _003CGetStorage_Br_Paging_003Ed__20()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSysDateNew_003Ed__36 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetSysDateResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private TaskAwaiter<GetSysDateResult> _003C_003Eu__1;

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
		internal static bool DeleteVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PostVal()
		{
			return true;
		}

		static _003CGetSysDateNew_003Ed__36()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetTargetPrometerData_003Ed__156 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool AwakeVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool GetVal()
		{
			return true;
		}

		static _003CGetTargetPrometerData_003Ed__156()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetTaxInputData_003Ed__118 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool DisableVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CancelVal()
		{
			return true;
		}

		static _003CGetTaxInputData_003Ed__118()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetTrans_Seq_003Ed__41 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetTrans_SeqResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int VerNo;

		private TaskAwaiter<GetTrans_SeqResult> _003C_003Eu__1;

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
		internal static bool RemoveVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InterruptVal()
		{
			return true;
		}

		static _003CGetTrans_Seq_003Ed__41()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetUsers_003Ed__149 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool MapVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DefineVal()
		{
			return true;
		}

		static _003CGetUsers_003Ed__149()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetUsersWithTax_003Ed__9 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetUsersOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int Branch_No;

		public string Pda_Name;

		public int op_type;

		public int VerNo;

		public string Token;

		public string Device_Type;

		private TaskAwaiter<GetUsersOBjctResult> _003C_003Eu__1;

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
		internal static bool ForgotVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FillVal()
		{
			return true;
		}

		static _003CGetUsersWithTax_003Ed__9()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetVistFailReasons_003Ed__46 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetVistFailReasonsOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private TaskAwaiter<GetVistFailReasonsOBjctResult> _003C_003Eu__1;

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
		internal static bool SearchVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool EnableVal()
		{
			return true;
		}

		static _003CGetVistFailReasons_003Ed__46()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetWHTransferMstData_003Ed__59 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool InsertVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ViewVal()
		{
			return true;
		}

		static _003CGetWHTransferMstData_003Ed__59()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetWareHouse_003Ed__29 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetWareHouseOBjctResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int User_No;

		public int VerNo;

		private TaskAwaiter<GetWareHouseOBjctResult> _003C_003Eu__1;

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
		internal static bool InvokeVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ListVal()
		{
			return true;
		}

		static _003CGetWareHouse_003Ed__29()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetWhReceiveTypes_003Ed__62 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PrintVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalculateVal()
		{
			return true;
		}

		static _003CGetWhReceiveTypes_003Ed__62()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetWhtransSerialNo_003Ed__61 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool SelectVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CompareVal()
		{
			return true;
		}

		static _003CGetWhtransSerialNo_003Ed__61()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CReadRequestBody_003Ed__6 : IAsyncStateMachine
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
		internal static bool ManageVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CloneVal()
		{
			return true;
		}

		static _003CReadRequestBody_003Ed__6()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveBillNoteRequest_003Ed__166 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool MoveVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReadVal()
		{
			return true;
		}

		static _003CSaveBillNoteRequest_003Ed__166()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveConfirmCustomerBalance_003Ed__146 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool RunVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RegisterVal()
		{
			return true;
		}

		static _003CSaveConfirmCustomerBalance_003Ed__146()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustGpsScan_003Ed__67 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public Cust_Gps_Scan Cust_Gps_Scan;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool NewVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool TestVal()
		{
			return true;
		}

		static _003CSaveCustGpsScan_003Ed__67()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerAccountStatementConfirm_003Ed__155 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool CollectVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LogoutVal()
		{
			return true;
		}

		static _003CSaveCustomerAccountStatementConfirm_003Ed__155()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerInv_003Ed__63 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public CustomerInv CustomerInv;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<GeneralResult> _003C_003Eu__2;

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
		internal static bool LoginVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool QueryVal()
		{
			return true;
		}

		static _003CSaveCustomerInv_003Ed__63()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerTarget_003Ed__68 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public CustomerTarget CustomerTarget;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<GeneralResult> _003C_003Eu__2;

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
		internal static bool InitVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RestartVal()
		{
			return true;
		}

		static _003CSaveCustomerTarget_003Ed__68()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerTargetImages_003Ed__94 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CreateVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResetVal()
		{
			return true;
		}

		static _003CSaveCustomerTargetImages_003Ed__94()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveDtsBills_003Ed__116 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool ConcatVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StopVal()
		{
			return true;
		}

		static _003CSaveDtsBills_003Ed__116()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveDtsRtBills_003Ed__117 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool VisitVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetVal()
		{
			return true;
		}

		static _003CSaveDtsRtBills_003Ed__117()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveDynamicFieldDocument_003Ed__153 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool RateVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InstantiateVal()
		{
			return true;
		}

		static _003CSaveDynamicFieldDocument_003Ed__153()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveExpansDoc_003Ed__103 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool AddVal()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RevertVal()
		{
			return true;
		}

		static _003CSaveExpansDoc_003Ed__103()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveExpiryOutgoingRequest_003Ed__143 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool DestroyClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrepareClient()
		{
			return true;
		}

		static _003CSaveExpiryOutgoingRequest_003Ed__143()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveFileAsBlob1_003Ed__125 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool FlushClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CheckClient()
		{
			return true;
		}

		static _003CSaveFileAsBlob1_003Ed__125()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveGpsEventNew_003Ed__65 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public Gps_EventData Gps_EventData;

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
		internal static bool SortClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PushClient()
		{
			return true;
		}

		static _003CSaveGpsEventNew_003Ed__65()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveGps_EventCurrentNew_003Ed__72 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public GpsEventCurnt gpsEventCurnt;

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
		internal static bool FindClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PatchClient()
		{
			return true;
		}

		static _003CSaveGps_EventCurrentNew_003Ed__72()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveMarkitingVisit_003Ed__128 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool ReflectClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CustomizeClient()
		{
			return true;
		}

		static _003CSaveMarkitingVisit_003Ed__128()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveMassage_003Ed__150 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool ValidateClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConnectClient()
		{
			return true;
		}

		static _003CSaveMassage_003Ed__150()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveOtherVisitTasks_003Ed__159 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool WriteClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool OrderClient()
		{
			return true;
		}

		static _003CSaveOtherVisitTasks_003Ed__159()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSavePromoter_003Ed__147 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool StartClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool UpdateClient()
		{
			return true;
		}

		static _003CSavePromoter_003Ed__147()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveQuestionnaireDoc_003Ed__87 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool VerifyClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PopClient()
		{
			return true;
		}

		static _003CSaveQuestionnaireDoc_003Ed__87()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveQuotation_003Ed__64 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool ComputeClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CountClient()
		{
			return true;
		}

		static _003CSaveQuotation_003Ed__64()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveRepPlan_003Ed__70 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RepPlan RepPlan;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<GeneralResult> _003C_003Eu__2;

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
		internal static bool AssetClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CallClient()
		{
			return true;
		}

		static _003CSaveRepPlan_003Ed__70()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveRqTransfer_003Ed__69 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RqTransfer RqTransfer;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<GeneralResult> _003C_003Eu__2;

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
		internal static bool PublishClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetupClient()
		{
			return true;
		}

		static _003CSaveRqTransfer_003Ed__69()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveSaleOrder_003Ed__109 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool ChangeClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalcClient()
		{
			return true;
		}

		static _003CSaveSaleOrder_003Ed__109()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveSample_003Ed__119 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool ResolveClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ExcludeClient()
		{
			return true;
		}

		static _003CSaveSample_003Ed__119()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveShowItems_003Ed__82 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool IncludeClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DeleteClient()
		{
			return true;
		}

		static _003CSaveShowItems_003Ed__82()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveShowItemsImages_003Ed__83 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public IFormFileCollection stream;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool PostClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AwakeClient()
		{
			return true;
		}

		static _003CSaveShowItemsImages_003Ed__83()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveVists_003Ed__66 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public VistsData VistsData;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<GeneralResult> _003C_003Eu__2;

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
		internal static bool GetClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DisableClient()
		{
			return true;
		}

		static _003CSaveVists_003Ed__66()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveVouchers_new_003Ed__80 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool CancelClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RemoveClient()
		{
			return true;
		}

		static _003CSaveVouchers_new_003Ed__80()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveWhTransferReciveDoc_003Ed__105 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private StreamReader _003Creader_003E5__2;

		private Headers _003C_003E7__wrap2;

		private TaskAwaiter<string> _003C_003Eu__1;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__2;

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
		internal static bool InterruptClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MapClient()
		{
			return true;
		}

		static _003CSaveWhTransferReciveDoc_003Ed__105()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSendByWhatsup_003Ed__160 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<ResponceObject> _003C_003Eu__1;

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
		internal static bool DefineClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ForgotClient()
		{
			return true;
		}

		static _003CSendByWhatsup_003Ed__160()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSendVerficationMessage_003Ed__169 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<ResponceObject> _003C_003Eu__1;

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
		internal static bool FillClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SearchClient()
		{
			return true;
		}

		static _003CSendVerficationMessage_003Ed__169()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CTestApi_003Ed__95 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool EnableClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InsertClient()
		{
			return true;
		}

		static _003CTestApi_003Ed__95()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CTestDb_003Ed__44 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool ViewClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InvokeClient()
		{
			return true;
		}

		static _003CTestDb_003Ed__44()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CTestVersion_003Ed__168 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public string version;

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
		internal static bool ListClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrintClient()
		{
			return true;
		}

		static _003CTestVersion_003Ed__168()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateColumn_003Ed__110 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CalculateClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SelectClient()
		{
			return true;
		}

		static _003CUpdateColumn_003Ed__110()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateColumnWithProc_003Ed__111 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool CompareClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ManageClient()
		{
			return true;
		}

		static _003CUpdateColumnWithProc_003Ed__111()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateCustomersData_003Ed__71 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public UpdateCustomerData UpdateCustomerData;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool CloneClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MoveClient()
		{
			return true;
		}

		static _003CUpdateCustomersData_003Ed__71()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateReadMessage_003Ed__151 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool ReadClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RunClient()
		{
			return true;
		}

		static _003CUpdateReadMessage_003Ed__151()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateSyncStatues_003Ed__38 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int SYNC_TYP;

		public int VerNo;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool RegisterClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool NewClient()
		{
			return true;
		}

		static _003CUpdateSyncStatues_003Ed__38()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateUserPassword_003Ed__164 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool TestClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CollectClient()
		{
			return true;
		}

		static _003CUpdateUserPassword_003Ed__164()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUploadExpnsImages_003Ed__106 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public RequstPostObject requstObject;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

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
		internal static bool LogoutClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LoginClient()
		{
			return true;
		}

		static _003CUploadExpnsImages_003Ed__106()
		{
			Decorator.EnablePage();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUploadFile_003Ed__124 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public DistributionController _003C_003E4__this;

		public IFormFileCollection stream;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool QueryClient()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InitClient()
		{
			return true;
		}

		static _003CUploadFile_003Ed__124()
		{
			Decorator.EnablePage();
		}
	}

	internal Headers m_Page;

	internal readonly IService m_Dispatcher;

	internal readonly IOptions<ApiConfig> m_Rules;

	private readonly IOptions<TokenSetting> _Manager;

	[MethodImpl(MethodImplOptions.NoInlining)]
	public DistributionController(IOptions<ApiConfig> config, IService service, IOptions<TokenSetting> configToken)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private void NewPage()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CReadRequestBody_003Ed__6))]
	private Task<string> PrintPage(HttpRequest P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	protected void LogWriteAsync(string logMessage)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private string SetPage(string P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetUsersWithTax_003Ed__9))]
	[HttpGet]
	[Route("GetUsersWithTax")]
	[AllowAnonymous]
	public Task<GetUsersOBjctResult> GetUsersWithTax(int YearNo, int ActvieNo, int Branch_No, string Pda_Name, int op_type, int VerNo, string Token = "", string Device_Type = "")
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCurrncy_003Ed__10))]
	[HttpGet]
	[Route("GetCurrncy")]
	public Task<GetCurrncyOBjctResult> GetCurrncy(int YearNo, int ActvieNo, int Branch_No, int type_no, string REP_CODE, int VerNo, string C_Code = "")
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetCustomers")]
	[AsyncStateMachine(typeof(_003CGetCustomers_003Ed__11))]
	[HttpGet]
	public Task<GetCustomersOBjctResult> GetCustomers(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetBanksDetails")]
	[AsyncStateMachine(typeof(_003CGetBanksDetails_003Ed__12))]
	[HttpGet]
	public Task<GetBanksDetailsOBjctResult> GetBanksDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetBanksCurrenciesDetails_003Ed__13))]
	[Route("GetBanksCurrenciesDetails")]
	public Task<GetBanksCurrenciesDetailsOBjctResult> GetBanksCurrenciesDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetCashDetails_003Ed__14))]
	[Route("GetCashDetails")]
	public Task<GetCashDetailsOBjctResult> GetCashDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetCashCurrenciesDetails")]
	[AsyncStateMachine(typeof(_003CGetCashCurrenciesDetails_003Ed__15))]
	[HttpGet]
	public Task<GetCashCurrenciesDetailsOBjctResult> GetCashCurrenciesDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetItemsDetailsPaging")]
	[AsyncStateMachine(typeof(_003CGetItemsDetailsPaging_003Ed__16))]
	[HttpGet]
	public Task<GetItemsDetailsOBjctResult> GetItemsDetailsPaging(int YearNo, int ActvieNo, int Branch_No, int GRP_CODE, string REP_CODE, int S_row, int L_row, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetMeasurments")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetMeasurments_003Ed__17))]
	public Task<GetMeasurmentsOBjctResult> GetMeasurments(int YearNo, int ActvieNo, int Branch_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetPlanDetails")]
	[AsyncStateMachine(typeof(_003CGetPlanDetails_003Ed__18))]
	[HttpGet]
	public Task<GetPlanDetailsOBjctResult> GetPlanDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, string PLAN_DATE, int VerNo, string DOC_SER = "", string LANG_NO = "1")
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetStorage_Br")]
	[AsyncStateMachine(typeof(_003CGetStorage_Br_003Ed__19))]
	[HttpGet]
	public Task<GetStorageOBjctResult> GetStorage_Br(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[Route("GetStorage_Br_Paging")]
	[AsyncStateMachine(typeof(_003CGetStorage_Br_Paging_003Ed__20))]
	public Task<GetStorageOBjctResult> GetStorage_Br_Paging(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int S_row, int L_row, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetParameters_003Ed__21))]
	[Route("GetParameters")]
	[HttpGet]
	public Task<GetParametersObjctResult> GetParameters(int YearNo, int ActvieNo, string Rep_Code, int VerNo, int BrnNo = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetDocTypes_003Ed__22))]
	[Route("GetDocTypes")]
	public Task<GetDocTypesOBjctResult> GetDocTypes(int YearNo, int ActvieNo, int Branch_No, int User_Id, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetBrachesData")]
	[AsyncStateMachine(typeof(_003CGetBrachesData_003Ed__23))]
	[HttpGet]
	public Task<GetBrachesDataOBjctResult> GetBrachesData(int YearNo, int ActvieNo, int Branch_No, int User_Id, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CDocDescription_003Ed__24))]
	[Route("DocDescription")]
	[HttpGet]
	public Task<DocDescriptionObjctResult> DocDescription(int YearNo, int ActvieNo, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetPriceLevels_003Ed__25))]
	[Route("GetPriceLevels")]
	public Task<GetPriceLevelsResult> GetPriceLevels(int YearNo, int ActvieNo, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetItemsPriceLevelsPaging_003Ed__26))]
	[Route("GetItemsPriceLevelsPaging")]
	public Task<GetItemsPriceLevelsResult> GetItemsPriceLevelsPaging(int YearNo, int ActvieNo, string REP_CODE, int S_row, int L_row, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[Route("GetItemCount")]
	[AsyncStateMachine(typeof(_003CGetItemCount_003Ed__27))]
	public Task<GetItemCountResult> GetItemCount(int YearNo, int ActvieNo, string REP_CODE, int Type_No, int VerNo, int W_Code)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetFormsPrivilege")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetFormsPrivilege_003Ed__28))]
	public Task<GetFormsPrivilegeResult> GetFormsPrivilege(int YearNo, int ActvieNo, int User_Id, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[Route("GetWareHouse")]
	[AsyncStateMachine(typeof(_003CGetWareHouse_003Ed__29))]
	public Task<GetWareHouseOBjctResult> GetWareHouse(int YearNo, int ActvieNo, int User_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetItemsBarcode")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetItemsBarcode_003Ed__30))]
	public Task<GetItemsBarcodeOBjctResult> GetItemsBarcode(int YearNo, int ActvieNo, int Branch_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetItemsStorage")]
	[AsyncStateMachine(typeof(_003CGetItemsStorage_003Ed__31))]
	[HttpGet]
	public Task<GetItemsStorageOBjctResult> GetItemsStorage(int YearNo, int ActvieNo, int Branch_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetInventroyTypes_003Ed__32))]
	[HttpGet]
	[Route("GetInventroyTypes")]
	public Task<GetInventroyTypesOBjctResult> GetInventroyTypes(int YearNo, int ActvieNo, int Branch_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[Route("GetItemsPrices")]
	[AsyncStateMachine(typeof(_003CGetItemsPrices_003Ed__33))]
	public Task<GetItemsPriceOBjctResult> GetItemsPrices(int YearNo, int ActvieNo, int Branch_No, int Lvl_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetInvSerialParameter")]
	[AsyncStateMachine(typeof(_003CGetInvSerialParameter_003Ed__34))]
	[HttpGet]
	public Task<GetInvSerialParameterObjctResult> GetInvSerialParameter(int YearNo, int ActvieNo, int Branch_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetLevelPrices_003Ed__35))]
	[HttpGet]
	[Route("GetLevelPrices")]
	public Task<GetLevelPriceOBjctResult> GetLevelPrices(int YearNo, int ActvieNo, int Branch_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSysDateNew_003Ed__36))]
	[HttpGet]
	[AllowAnonymous]
	[Route("GetSysDateNew")]
	public Task<GetSysDateResult> GetSysDateNew(int YearNo, int ActvieNo, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("ClosedPlan")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CClosedPlan_003Ed__37))]
	public Task<GeneralResult> ClosedPlan(int YearNo, int ActvieNo, string REP_CODE, string DOC_SER, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUpdateSyncStatues_003Ed__38))]
	[HttpGet]
	[Route("UpdateSyncStatues")]
	public Task<GeneralResult> UpdateSyncStatues(int YearNo, int ActvieNo, string REP_CODE, int SYNC_TYP, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSales_discount_003Ed__39))]
	[HttpGet]
	[Route("GetSales_discount")]
	public Task<GetSales_discountOBjctResult> GetSales_discount(int YearNo, int ActvieNo, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesFreeQty_003Ed__40))]
	[Route("GetSalesFreeQty")]
	[HttpGet]
	public Task<GetSalesFreeQtyOBjctResult> GetSalesFreeQty(int YearNo, int ActvieNo, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetTrans_Seq")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetTrans_Seq_003Ed__41))]
	public Task<GetTrans_SeqResult> GetTrans_Seq(int YearNo, int ActvieNo, string REP_CODE, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[Route("GetCustCreditPreiod")]
	[AsyncStateMachine(typeof(_003CGetCustCreditPreiod_003Ed__42))]
	public Task<CustCreditPreiodResult> GetCustCreditPreiod(int YearNo, int ActvieNo, string REP_CODE, int VerNo, string C_CODE = "")
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GeoLocations")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGeoLocations_003Ed__43))]
	public Task<GeoLocationResult> GeoLocations(int YearNo, int ActvieNo, int VerNo, int S_Row = 0, int E_Row = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("TestDb")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CTestDb_003Ed__44))]
	public Task<GeneralResult> TestDb()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[Route("TestWs")]
	public GeneralResult TestWs()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetVistFailReasons_003Ed__46))]
	[Route("GetVistFailReasons")]
	[HttpGet]
	public Task<GetVistFailReasonsOBjctResult> GetVistFailReasons(int YearNo, int ActvieNo, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBrnchUserPriv_003Ed__47))]
	[Route("GetBrnchUserPriv")]
	[HttpGet]
	public Task<GetBrnchUserPrivResult> GetBrnchUserPriv(int YearNo, int ActvieNo, string User_No, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetDocBillsData")]
	[AsyncStateMachine(typeof(_003CGetDocBillsData_003Ed__48))]
	[HttpGet]
	public Task<GetDocBillsDataResult> GetDocBillsData(int YearNo, int ActvieNo, string REP_CODE, int BILL_DOC_TYPE, string BILL_NO, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesCharges_003Ed__49))]
	[Route("GetSalesCharges")]
	[HttpGet]
	public Task<GetSales_ChargesResult> GetSalesCharges(int YearNo, int ActvieNo, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetGnrTaxCode")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetGnrTaxCode_003Ed__50))]
	public Task<GetGnrTaxCodeResult> GetGnrTaxCode(int YearNo, int ActvieNo, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetGnrTaxItems_003Ed__51))]
	[HttpGet]
	[Route("GetGnrTaxItems")]
	public Task<GetGnrTaxItemsResult> GetGnrTaxItems(int YearNo, int ActvieNo, string Rep_Code, int S_row, int L_row, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[Route("GetCshBlncWithLmt")]
	[AsyncStateMachine(typeof(_003CGetCshBlncWithLmt_003Ed__52))]
	public Task<Value<ResponceObject>> GetCshBlncWithLmt(int YearNo, int ActvieNo, string REP_CODE, string Date, int VerNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQutPrmMstData_003Ed__53))]
	[HttpGet]
	[Route("GetQutPrmMstData")]
	public Task<Value<ResponceObject>> GetQutPrmMstData(RequstObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQutPrmDtlData_OLD_003Ed__54))]
	[HttpPost]
	[Route("GetQutPrmDtlData_OLD")]
	public Task<Value<ResponceObject>> GetQutPrmDtlData_OLD(RequstObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpGet]
	[Route("GetQutPrmSubDtlData")]
	[AsyncStateMachine(typeof(_003CGetQutPrmSubDtlData_003Ed__55))]
	public Task<Value<ResponceObject>> GetQutPrmSubDtlData(RequstObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetQutPrmGrpDtlData")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetQutPrmGrpDtlData_003Ed__56))]
	public Task<Value<ResponceObject>> GetQutPrmGrpDtlData(RequstObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetQutPrmGrpMstData")]
	[HttpGet]
	[AsyncStateMachine(typeof(_003CGetQutPrmGrpMstData_003Ed__57))]
	public Task<Value<ResponceObject>> GetQutPrmGrpMstData(RequstObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetKey_003Ed__58))]
	[Route("GetKey")]
	public Task<Value<ResponceObject>> GetKey(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetWHTransferMstData")]
	[AsyncStateMachine(typeof(_003CGetWHTransferMstData_003Ed__59))]
	public Task<Value<ResponceObject>> GetWHTransferMstData(RequstPostObject requstObject1)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetItemsDataByWHTransferNo")]
	[AsyncStateMachine(typeof(_003CGetItemsDataByWHTransferNo_003Ed__60))]
	public Task<Value<ResponceObject>> GetItemsDataByWHTransferNo(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetWhtransSerialNo_003Ed__61))]
	[Route("GetWhtransSerialNo")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetWhtransSerialNo(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetWhReceiveTypes")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetWhReceiveTypes_003Ed__62))]
	public Task<Value<ResponceObject>> GetWhReceiveTypes(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SaveCustomerInv")]
	[AsyncStateMachine(typeof(_003CSaveCustomerInv_003Ed__63))]
	[HttpPost]
	public Task<GeneralResult> SaveCustomerInv(CustomerInv CustomerInv)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveQuotation_003Ed__64))]
	[Route("SaveQuotation")]
	public Task<Value<ResponceObject>> SaveQuotation(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AllowAnonymous]
	[Route("SaveGpsEvent")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveGpsEventNew_003Ed__65))]
	public Task<GeneralResult> SaveGpsEventNew(Gps_EventData Gps_EventData)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SaveVists")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveVists_003Ed__66))]
	public Task<GeneralResult> SaveVists(VistsData VistsData)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("SaveCustGpsScan")]
	[AsyncStateMachine(typeof(_003CSaveCustGpsScan_003Ed__67))]
	public Task<GeneralResult> SaveCustGpsScan(Cust_Gps_Scan Cust_Gps_Scan)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustomerTarget_003Ed__68))]
	[HttpPost]
	[Route("SaveCustomerTarget")]
	public Task<GeneralResult> SaveCustomerTarget(CustomerTarget CustomerTarget)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("SaveRqTransfer")]
	[AsyncStateMachine(typeof(_003CSaveRqTransfer_003Ed__69))]
	public Task<GeneralResult> SaveRqTransfer(RqTransfer RqTransfer)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveRepPlan_003Ed__70))]
	[HttpPost]
	[Route("SaveRepPlan")]
	public Task<GeneralResult> SaveRepPlan(RepPlan RepPlan)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("UpdateCustomersData")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CUpdateCustomersData_003Ed__71))]
	public Task<GeneralResult> UpdateCustomersData(UpdateCustomerData UpdateCustomerData)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("SaveGpsEventCurrent")]
	[AsyncStateMachine(typeof(_003CSaveGps_EventCurrentNew_003Ed__72))]
	[AllowAnonymous]
	public Task<GeneralResult> SaveGps_EventCurrentNew(GpsEventCurnt gpsEventCurnt)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("DocsTransferMatching")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CDocsTransferMatching_003Ed__73))]
	public Task<Value<ResponceObject>> DocsTransferMatching(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAccountStatment_003Ed__74))]
	[HttpPost]
	[Route("GetAccountStatment")]
	public Task<Value<ResponceObject>> GetAccountStatment(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetAccountStatmentDetails")]
	[AsyncStateMachine(typeof(_003CGetAccountStatmentDetails_003Ed__75))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetAccountStatmentDetails(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBillMasterData_003Ed__76))]
	[HttpPost]
	[Route("GetBillMasterData")]
	public Task<Value<ResponceObject>> GetBillMasterData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetGroupDetails")]
	[AsyncStateMachine(typeof(_003CGetGroupDetails_003Ed__77))]
	public Task<Value<ResponceObject>> GetGroupDetails(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetInstallmentBills")]
	[AsyncStateMachine(typeof(_003CGetInstallmentBills_003Ed__78))]
	public Task<Value<ResponceObject>> GetInstallmentBills(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetQutPrmDtlData")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetQutPrmDtlData_003Ed__79))]
	public Task<Value<ResponceObject>> GetQutPrmDtlData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveVouchers_new_003Ed__80))]
	[Route("SaveVouchers_new")]
	public Task<Value<ResponceObject>> SaveVouchers_new(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetCustomerClassData")]
	[AsyncStateMachine(typeof(_003CGetCustomerClassData_003Ed__81))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetCustomerClassData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("SaveShowItems")]
	[AsyncStateMachine(typeof(_003CSaveShowItems_003Ed__82))]
	public Task<Value<ResponceObject>> SaveShowItems(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveShowItemsImages_003Ed__83))]
	[Route("SaveShowItemsImages")]
	[HttpPost]
	public Task<Value<ResponceObject>> SaveShowItemsImages(IFormFileCollection stream)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemSerialsData_003Ed__84))]
	[HttpPost]
	[Route("GetItemSerialsData")]
	public Task<Value<ResponceObject>> GetItemSerialsData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQuestionnaireQuestions_003Ed__85))]
	[HttpPost]
	[Route("GetQuestionnaireQuestions")]
	public Task<Value<ResponceObject>> GetQuestionnaireQuestions(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAnswerQuestionnaireQuestions_003Ed__86))]
	[HttpPost]
	[Route("GetAnswerQuestionnaireQuestions")]
	public Task<Value<ResponceObject>> GetAnswerQuestionnaireQuestions(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SaveQuestionnaireDoc")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveQuestionnaireDoc_003Ed__87))]
	public Task<Value<ResponceObject>> SaveQuestionnaireDoc(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsGroupsData_003Ed__88))]
	[HttpPost]
	[Route("GetItemsGroupsData")]
	public Task<Value<ResponceObject>> GetItemsGroupsData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetCreditCardTypes")]
	[AsyncStateMachine(typeof(_003CGetCreditCardTypes_003Ed__89))]
	public Task<Value<ResponceObject>> GetCreditCardTypes(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetReturnFromBill")]
	[AsyncStateMachine(typeof(_003CGetReturnFromBill_003Ed__90))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetReturnFromBill(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetReturnFromBillDetails_003Ed__91))]
	[Route("GetReturnFromBillDetails")]
	public Task<Value<ResponceObject>> GetReturnFromBillDetails(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAllTaxItems_003Ed__92))]
	[HttpPost]
	[Route("GetAllTaxItems")]
	public Task<Value<ResponceObject>> GetAllTaxItems(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCalcTaxType_003Ed__93))]
	[Route("GetCalcTaxType")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetCalcTaxType(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustomerTargetImages_003Ed__94))]
	[HttpPost]
	[Route("SaveCustomerTargetImages")]
	public Task<Value<ResponceObject>> SaveCustomerTargetImages(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("TestApi")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CTestApi_003Ed__95))]
	public Task<Value<ResponceObject>> TestApi(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetDocsSyncMethode")]
	[AsyncStateMachine(typeof(_003CGetDocsSyncMethode_003Ed__96))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetDocsSyncMethode(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetDtsCstAging")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetDtsCstAging_003Ed__97))]
	public Task<Value<ResponceObject>> GetDtsCstAging(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetCustomersTargetData")]
	[AsyncStateMachine(typeof(_003CGetCustomersTargetData_003Ed__98))]
	public Task<Value<ResponceObject>> GetCustomersTargetData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("CheckSetup")]
	[AsyncStateMachine(typeof(_003CCheckSetup_003Ed__99))]
	public Task<Value<ResponceObject>> CheckSetup(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetItemsBarcodeData_003Ed__100))]
	[Route("GetItemsBarcodeData")]
	public Task<Value<ResponceObject>> GetItemsBarcodeData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSmanPlanTrgt_003Ed__101))]
	[Route("GetSmanPlanTrgt")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetSmanPlanTrgt(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDtsExpnsTypes_003Ed__102))]
	[HttpPost]
	[Route("GetDtsExpnsTypes")]
	public Task<Value<ResponceObject>> GetDtsExpnsTypes(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SaveExpansDoc")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveExpansDoc_003Ed__103))]
	public Task<Value<ResponceObject>> SaveExpansDoc(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetDocInfoData_003Ed__104))]
	[Route("GetDocInfoData")]
	public Task<Value<ResponceObject>> GetDocInfoData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("SaveWhTransferReciveDoc")]
	[AsyncStateMachine(typeof(_003CSaveWhTransferReciveDoc_003Ed__105))]
	public Task<Value<ResponceObject>> SaveWhTransferReciveDoc(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUploadExpnsImages_003Ed__106))]
	[HttpPost]
	[Route("UploadExpnsImages")]
	public Task<Value<ResponceObject>> UploadExpnsImages(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetSalesOrderMst")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetSalesOrderMst_003Ed__107))]
	public Task<Value<ResponceObject>> GetSalesOrderMst(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesOrderDtl_003Ed__108))]
	[HttpPost]
	[Route("GetSalesOrderDtl")]
	public Task<Value<ResponceObject>> GetSalesOrderDtl(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SaveSaleOrder")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveSaleOrder_003Ed__109))]
	public Task<Value<ResponceObject>> SaveSaleOrder(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CUpdateColumn_003Ed__110))]
	[Route("UpdateColumn")]
	public Task<Value<ResponceObject>> UpdateColumn(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CUpdateColumnWithProc_003Ed__111))]
	[Route("UpdateColumnWithProc")]
	public Task<Value<ResponceObject>> UpdateColumnWithProc(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetDtsAccountStatmenDocDtl")]
	[AsyncStateMachine(typeof(_003CGetDtsAccountStatmenDocDtl_003Ed__112))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetDtsAccountStatmenDocDtl(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetReturnFromRtRqst_003Ed__113))]
	[Route("GetReturnFromRtRqst")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetReturnFromRtRqst(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetReturnFromRtRqstDetails")]
	[AsyncStateMachine(typeof(_003CGetReturnFromRtRqstDetails_003Ed__114))]
	public Task<Value<ResponceObject>> GetReturnFromRtRqstDetails(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDtsDynamicScreenFileds_003Ed__115))]
	[Route("GetDtsDynamicScreenFileds")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetDtsDynamicScreenFileds(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveDtsBills_003Ed__116))]
	[Route("SaveDtsBills")]
	public Task<Value<ResponceObject>> SaveDtsBills(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SaveDtsRtBills")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveDtsRtBills_003Ed__117))]
	public Task<Value<ResponceObject>> SaveDtsRtBills(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetTaxInputData_003Ed__118))]
	[Route("GetTaxInputData")]
	public Task<Value<ResponceObject>> GetTaxInputData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("SaveSample")]
	[AsyncStateMachine(typeof(_003CSaveSample_003Ed__119))]
	public Task<Value<ResponceObject>> SaveSample(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetSalesSerialNo")]
	[AsyncStateMachine(typeof(_003CGetSalesSerialNo_003Ed__120))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetSalesSerialNo(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetMobileRequest_003Ed__121))]
	[Route("GetMobileRequest")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetMobileRequest(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetDocMst")]
	[AsyncStateMachine(typeof(_003CGetDocMst_003Ed__122))]
	public Task<Value<ResponceObject>> GetDocMst(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDocDtls_003Ed__123))]
	[HttpPost]
	[Route("GetDocDtls")]
	public Task<Value<ResponceObject>> GetDocDtls(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUploadFile_003Ed__124))]
	[HttpPost]
	[Route("UploadFile")]
	public Task<GeneralResult> UploadFile(IFormFileCollection stream)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveFileAsBlob1_003Ed__125))]
	[Route("SaveFileAsBlob1")]
	public Task<GeneralResult> SaveFileAsBlob1()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsMarktProperty_003Ed__126))]
	[Route("GetItemsMarktProperty")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetItemsMarktProperty(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetMarktVisitFlag_003Ed__127))]
	[HttpPost]
	[Route("GetMarktVisitFlag")]
	public Task<Value<ResponceObject>> GetMarktVisitFlag(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveMarkitingVisit_003Ed__128))]
	[Route("SaveMarkitingVisit")]
	[HttpPost]
	public Task<Value<ResponceObject>> SaveMarkitingVisit(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetCustomerLimitSales")]
	[AsyncStateMachine(typeof(_003CGetCustomerLimitSales_003Ed__129))]
	public Task<Value<ResponceObject>> GetCustomerLimitSales(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerItemLimitSales_003Ed__130))]
	[HttpPost]
	[Route("GetCustomerItemLimitSales")]
	public Task<Value<ResponceObject>> GetCustomerItemLimitSales(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetBillSalesCharges")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetBillSalesCharges_003Ed__131))]
	public Task<Value<ResponceObject>> GetBillSalesCharges(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSmanDailayPlan_003Ed__132))]
	[HttpPost]
	[Route("GetSmanDailayPlan")]
	public Task<Value<ResponceObject>> GetSmanDailayPlan(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSFlagCode_003Ed__133))]
	[Route("GetSFlagCode")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetSFlagCode(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetExtraScreenLabel")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetExtraScreenLabel_003Ed__134))]
	public Task<Value<ResponceObject>> GetExtraScreenLabel(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetCustomerCostCenter")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetCustomerCostCenter_003Ed__135))]
	public Task<Value<ResponceObject>> GetCustomerCostCenter(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetCashCustomer")]
	[AsyncStateMachine(typeof(_003CGetCashCustomer_003Ed__136))]
	public Task<Value<ResponceObject>> GetCashCustomer(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetFunctionData")]
	[AsyncStateMachine(typeof(_003CGetFunctionData_003Ed__137))]
	public Task<Value<ResponceObject>> GetFunctionData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetSalesManDocumentMovement")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetSalesManDocumentMovement_003Ed__138))]
	public Task<Value<ResponceObject>> GetSalesManDocumentMovement(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetSalesManItemMovement")]
	[AsyncStateMachine(typeof(_003CGetSalesManItemMovement_003Ed__139))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetSalesManItemMovement(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetMandatoryField")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetMandatoryField_003Ed__140))]
	public Task<Value<ResponceObject>> GetMandatoryField(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetAvlQtyOnline")]
	[AsyncStateMachine(typeof(_003CGetAvlQtyOnline_003Ed__141))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetAvlQtyOnline(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetSalesInfo_003Ed__142))]
	[Route("GetSalesInfo")]
	public Task<Value<ResponceObject>> GetSalesInfo(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SaveExpiryOutgoingRequest")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveExpiryOutgoingRequest_003Ed__143))]
	public Task<Value<ResponceObject>> SaveExpiryOutgoingRequest(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetSalesManBranchPrivilege")]
	[AsyncStateMachine(typeof(_003CGetSalesManBranchPrivilege_003Ed__144))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetSalesManBranchPrivilege(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetAccountConfirmBalances")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetAccountConfirmBalances_003Ed__145))]
	public Task<Value<ResponceObject>> GetAccountConfirmBalances(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveConfirmCustomerBalance_003Ed__146))]
	[HttpPost]
	[Route("SaveConfirmCustomerBalance")]
	public Task<Value<ResponceObject>> SaveConfirmCustomerBalance(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSavePromoter_003Ed__147))]
	[Route("SavePromoter")]
	public Task<Value<ResponceObject>> SavePromoter(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetMessageDetails")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetMessageDetails_003Ed__148))]
	public Task<Value<ResponceObject>> GetMessageDetails(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetUsers")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetUsers_003Ed__149))]
	public Task<Value<ResponceObject>> GetUsers(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("SaveMassage")]
	[AsyncStateMachine(typeof(_003CSaveMassage_003Ed__150))]
	public Task<Value<ResponceObject>> SaveMassage(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("UpdateReadMessage")]
	[AsyncStateMachine(typeof(_003CUpdateReadMessage_003Ed__151))]
	public Task<Value<ResponceObject>> UpdateReadMessage(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetCustomerPlanTarget")]
	[AsyncStateMachine(typeof(_003CGetCustomerPlanTarget_003Ed__152))]
	[HttpPost]
	public Task<Value<ResponceObject>> GetCustomerPlanTarget(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SaveDynamicFieldDocument")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CSaveDynamicFieldDocument_003Ed__153))]
	public Task<Value<ResponceObject>> SaveDynamicFieldDocument(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAccountStatementConfirm_003Ed__154))]
	[Route("GetAccountStatementConfirm")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetAccountStatementConfirm(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustomerAccountStatementConfirm_003Ed__155))]
	[Route("SaveCustomerAccountStatementConfirm")]
	[HttpPost]
	public Task<Value<ResponceObject>> SaveCustomerAccountStatementConfirm(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetTargetPrometerData")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetTargetPrometerData_003Ed__156))]
	public Task<Value<ResponceObject>> GetTargetPrometerData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetFreeSampleMovement")]
	[AsyncStateMachine(typeof(_003CGetFreeSampleMovement_003Ed__157))]
	public Task<Value<ResponceObject>> GetFreeSampleMovement(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetCustomerItemsAvailableQuantity")]
	[AsyncStateMachine(typeof(_003CGetCustomerItemsAvailableQuantity_003Ed__158))]
	public Task<Value<ResponceObject>> GetCustomerItemsAvailableQuantity(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveOtherVisitTasks_003Ed__159))]
	[HttpPost]
	[Route("SaveOtherVisitTasks")]
	public Task<Value<ResponceObject>> SaveOtherVisitTasks(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("SendByWhatsup")]
	[AsyncStateMachine(typeof(_003CSendByWhatsup_003Ed__160))]
	[HttpPost]
	public Task<ResponceObject> SendByWhatsup(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetBillQrData")]
	[AsyncStateMachine(typeof(_003CGetBillQrData_003Ed__161))]
	[HttpPost]
	public Task<ResponceObject> GetBillQrData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetFieldPrivilege")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetFieldPrivilege_003Ed__162))]
	public Task<Value<ResponceObject>> GetFieldPrivilege(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetGeneralInputData_003Ed__163))]
	[Route("GetGeneralInputData")]
	[HttpPost]
	public Task<Value<ResponceObject>> GetGeneralInputData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CUpdateUserPassword_003Ed__164))]
	[Route("UpdateUserPassword")]
	public Task<Value<ResponceObject>> UpdateUserPassword(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetBillForNote")]
	[HttpPost]
	[AsyncStateMachine(typeof(_003CGetBillForNote_003Ed__165))]
	public Task<Value<ResponceObject>> GetBillForNote(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveBillNoteRequest_003Ed__166))]
	[HttpPost]
	[Route("SaveBillNoteRequest")]
	public Task<Value<ResponceObject>> SaveBillNoteRequest(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBillDataForPrint_003Ed__167))]
	[Route("GetBillDataForPrint")]
	[HttpPost]
	public Task<ResponceObject> GetBillDataForPrint(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CTestVersion_003Ed__168))]
	[HttpGet]
	[Route("TestVersion")]
	public Task<ResponceObject> TestVersion(string version)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSendVerficationMessage_003Ed__169))]
	[HttpPost]
	[Route("SendVerficationMessage")]
	public Task<ResponceObject> SendVerficationMessage(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetGlRequestData_003Ed__170))]
	[HttpPost]
	[Route("GetGlRequestData")]
	public Task<ResponceObject> GetGlRequestData(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[Route("GetReportAsPdfFromOnyx")]
	[AsyncStateMachine(typeof(_003CGetReportAsPdfFromOnyx_003Ed__171))]
	[HttpPost]
	public Task<ResponceObject> GetReportAsPdfFromOnyx(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[HttpPost]
	[Route("GetCustomerItemSold")]
	[AsyncStateMachine(typeof(_003CGetCustomerItemSold_003Ed__172))]
	public Task<ResponceObject> GetCustomerItemSold(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerStock_003Ed__173))]
	[HttpPost]
	[Route("GetCustomerStock")]
	public Task<Value<ResponceObject>> GetCustomerStock(RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool AssetCandidate()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CallCandidate()
	{
		return true;
	}

	static DistributionController()
	{
		Decorator.EnablePage();
	}
}
