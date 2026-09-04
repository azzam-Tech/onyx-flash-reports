using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Threading.Tasks;
using System.Writers;
using System.Xml.Linq;
using Dapper.Oracle;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Options;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Onyx.Distribution.Models.DTOs;
using Onyx.Distribution.Models.MainDTOs;
using Onyx.Distribution.Services.Instances;
using Onyx.Distribution.Services.Services.IServices;
using Oracle.ManagedDataAccess.Client;

namespace Onyx.Distribution.Services.Services;

public class Service : IService
{
	[Serializable]
	[CompilerGenerated]
	private sealed class TemplateFilterContainer
	{
		public static readonly TemplateFilterContainer _003C_003E9;

		public static Func<XElement, string> _003C_003E9__56_0;

		public static Func<string, string, string> _003C_003E9__56_1;

		public static Func<GeneralConfigerationData, bool> _003C_003E9__77_0;

		public static Action<GeneralConfigerationData> _003C_003E9__77_1;

		public static Func<GeneralConfigerationData, bool> _003C_003E9__77_2;

		public static Action<GeneralConfigerationData> _003C_003E9__77_3;

		public static Func<GeneralConfigerationData, bool> _003C_003E9__77_4;

		public static Action<GeneralConfigerationData> _003C_003E9__77_5;

		public static Func<GeneralConfigerationData, bool> _003C_003E9__77_6;

		public static Action<GeneralConfigerationData> _003C_003E9__77_7;

		public static Func<GeneralConfigerationData, bool> _003C_003E9__77_8;

		public static Action<GeneralConfigerationData> _003C_003E9__77_9;

		public static Func<AccountStatment, bool> _003C_003E9__146_0;

		public static Func<AccountStatment, double> _003C_003E9__146_1;

		public static Func<AccountStatment, double> _003C_003E9__147_0;

		public static Func<AccountStatment, double> _003C_003E9__147_1;

		public static Predicate<AccountStatment> _003C_003E9__147_2;

		public static Func<Driver, SFlag> _003C_003E9__206_1;

		public static Func<CustomerGroup, SFlag> _003C_003E9__206_2;

		public static Func<ReportNameModel, bool> _003C_003E9__206_3;

		public static Func<ReportNameModel, SFlag> _003C_003E9__206_4;

		public static Func<SManDocMoveVisit, SManDocMove> _003C_003E9__211_1;

		public static Func<ReportNameModel, bool> _003C_003E9__247_1;

		public static Func<ReportNameModel, bool> _003C_003E9__247_2;

		public static Func<ReportNameModel, bool> _003C_003E9__247_3;

		public static Func<ReportNameModel, bool> _003C_003E9__247_4;

		public static Func<ReportNameModel, bool> _003C_003E9__247_5;

		public static Func<ReportNameModel, bool> _003C_003E9__247_6;

		public static Func<ReportNameModel, bool> _003C_003E9__247_7;

		public static Func<CustomerStock, string> _003C_003E9__249_0;

		[MethodImpl(MethodImplOptions.NoInlining)]
		static TemplateFilterContainer()
		{
			IssuerWatcherWriter.CustomizeUtils();
			InvocationWatcher.SLV0fFIsptsZtjvFft17();
			_003C_003E9 = new TemplateFilterContainer();
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public TemplateFilterContainer()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal string ListWatcher(XElement x)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal string ValidateWatcher(string a, string b)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool MoveWatcher(GeneralConfigerationData c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void AwakeWatcher(GeneralConfigerationData s)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool RateWatcher(GeneralConfigerationData c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void PostWatcher(GeneralConfigerationData s)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool GetWatcher(GeneralConfigerationData c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void TestWatcher(GeneralConfigerationData s)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool CalculateWatcher(GeneralConfigerationData c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void StopWatcher(GeneralConfigerationData s)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool FillWatcher(GeneralConfigerationData c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal void EnableWatcher(GeneralConfigerationData s)
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool DeleteWatcher(AccountStatment c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal double PatchWatcher(AccountStatment d)
		{
			return 0.0;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal double LogoutWatcher(AccountStatment x)
		{
			return 0.0;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal double CloneWatcher(AccountStatment x)
		{
			return 0.0;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool ManageWatcher(AccountStatment c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal SFlag AddWatcher(Driver c)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal SFlag RestartWatcher(CustomerGroup c)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool InitWatcher(ReportNameModel e)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal SFlag FlushWatcher(ReportNameModel e)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal SManDocMove SelectWatcher(SManDocMoveVisit c)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool RunWatcher(ReportNameModel c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool PrintWatcher(ReportNameModel c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool PushWatcher(ReportNameModel c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool CheckWatcher(ReportNameModel c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool ResolveWatcher(ReportNameModel c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool WriteWatcher(ReportNameModel c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool VisitWatcher(ReportNameModel c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal string PrepareWatcher(CustomerStock x)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DisableService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CancelService()
		{
			return true;
		}
	}

	[Serializable]
	[CompilerGenerated]
	private sealed class RulesSystemModel<T> where T : notnull
	{
		public static readonly RulesSystemModel<T> _003C_003E9;

		public static Func<string, string> _003C_003E9__50_0;

		[MethodImpl(MethodImplOptions.NoInlining)]
		static RulesSystemModel()
		{
			IssuerWatcherWriter.CustomizeUtils();
			InvocationWatcher.SLV0fFIsptsZtjvFft17();
			_003C_003E9 = new RulesSystemModel<T>();
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		public RulesSystemModel()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal string ResetWatcher(string f)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RemoveService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InterruptService()
		{
			return true;
		}
	}

	[CompilerGenerated]
	private sealed class ClientWatcherDescriptor
	{
		public string modId;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public ClientWatcherDescriptor()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool SearchWatcher(SecData c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DefineService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ForgotService()
		{
			return true;
		}

		static ClientWatcherDescriptor()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class TaskStatusResolver
	{
		public RequstPostObject requstObject;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public TaskStatusResolver()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool CancelWatcher(IAS_WHTRNS_MST x)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FillService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SearchService()
		{
			return true;
		}

		static TaskStatusResolver()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class ExceptionAuthenticationInstance
	{
		public RequstPostObject requstObject;

		public Func<string, bool> _003C_003E9__0;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public ExceptionAuthenticationInstance()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool UpdateWatcher(string e)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool EnableService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InsertService()
		{
			return true;
		}

		static ExceptionAuthenticationInstance()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class FieldPoolCollection
	{
		public RequstPostObject requstObject;

		public Func<string, bool> _003C_003E9__0;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public FieldPoolCollection()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool CallWatcher(string e)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ViewService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InvokeService()
		{
			return true;
		}

		static FieldPoolCollection()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class DatabaseDefinitionFilter
	{
		public RequstPostObject requstObject;

		public Func<string, bool> _003C_003E9__0;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public DatabaseDefinitionFilter()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool ForgotWatcher(string e)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrintService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalculateService()
		{
			return true;
		}

		static DatabaseDefinitionFilter()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class SetterSystemModel
	{
		public RequstPostObject requstObject;

		public Func<string, bool> _003C_003E9__0;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public SetterSystemModel()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool RemoveWatcher(string e)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SelectService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CompareService()
		{
			return true;
		}

		static SetterSystemModel()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class ErrorWatcher
	{
		public RequstPostObject requstObject;

		public Func<string, bool> _003C_003E9__0;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public ErrorWatcher()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool StartWatcher(string e)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ManageService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CloneService()
		{
			return true;
		}

		static ErrorWatcher()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class AdapterDefinitionFilter
	{
		[StructLayout(LayoutKind.Auto)]
		private struct PolicyUtilsConsumer : IAsyncStateMachine
		{
			public int m_ObjectWatcher;

			public AsyncTaskMethodBuilder _CallbackWatcher;

			public AdapterDefinitionFilter _SingletonWatcher;

			public string m_PropertyWatcher;

			public Action<string> m_ParameterWatcher;

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
			private void SetStateMachine(IAsyncStateMachine P_0)
			{
			}

			void IAsyncStateMachine.SetStateMachine(IAsyncStateMachine P_0)
			{
				//ILSpy generated this explicit interface implementation from .override directive in SetStateMachine
				this.SetStateMachine(P_0);
			}

			[MethodImpl(MethodImplOptions.NoInlining)]
			internal static bool FlushAdapter()
			{
				return true;
			}

			[MethodImpl(MethodImplOptions.NoInlining)]
			internal static bool CheckAdapter()
			{
				return true;
			}

			static PolicyUtilsConsumer()
			{
				IssuerWatcherWriter.CustomizeUtils();
			}
		}

		public Service _003C_003E4__this;

		public string sql;

		public Value<ResponceObject> result;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public AdapterDefinitionFilter()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		[AsyncStateMachine(typeof(PolicyUtilsConsumer))]
		internal Task VerifyWatcher(string query, Action<string> paramSetter = null)
		{
			return null;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MoveService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReadService()
		{
			return true;
		}

		static AdapterDefinitionFilter()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class RecordFilterContainer
	{
		public Headers headers;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public RecordFilterContainer()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool QueryWatcher(GetBrachesDataOBjct c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool InterruptWatcher(GetBrachesDataOBjct c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RunService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RegisterService()
		{
			return true;
		}

		static RecordFilterContainer()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class PredicateWatcher
	{
		public Headers headers;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public PredicateWatcher()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool RevertWatcher(GetBrachesDataOBjct c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool NewService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CollectService()
		{
			return true;
		}

		static PredicateWatcher()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class ErrorSystemEntry
	{
		public Headers headers;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public ErrorSystemEntry()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool SortUtils(GetBrachesDataOBjct c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool CountUtils(GetBrachesDataOBjct c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool DefineUtils(GetBrachesDataOBjct c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LogoutService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LoginService()
		{
			return true;
		}

		static ErrorSystemEntry()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class DefinitionWatcher
	{
		public RequstPostObject requstObject;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public DefinitionWatcher()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool ReflectUtils(ReportNameModel c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool ConcatUtils((string, int, string, string) c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool LoginUtils((string, int, string, string) c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool FindUtils((string, int, string, string) c)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool QueryService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InitService()
		{
			return true;
		}

		static DefinitionWatcher()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private sealed class CustomerWatcher
	{
		public CustomerItemSold item;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public CustomerWatcher()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool ConnectUtils(CustomerStockDtl d)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RestartService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CreateService()
		{
			return true;
		}

		static CustomerWatcher()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private static class InvocationUtilsConsumer
	{
		public static CallSite<Func<CallSite, object, object, object>> _003C_003Ep__0;

		public static CallSite<Func<CallSite, object, bool>> _003C_003Ep__1;

		public static CallSite<Func<CallSite, Type, object, object>> _003C_003Ep__2;

		public static CallSite<Func<CallSite, string, object, object>> _003C_003Ep__3;

		public static CallSite<Func<CallSite, object, string>> _003C_003Ep__4;

		static InvocationUtilsConsumer()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private static class ContextWatcher<T> where T : notnull
	{
		public static CallSite<Func<CallSite, Type, object, JsonSerializerSettings, object>> _003C_003Ep__0;

		public static CallSite<Func<CallSite, object, string>> _003C_003Ep__1;

		static ContextWatcher()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[CompilerGenerated]
	private static class AuthenticationWatcher
	{
		public static CallSite<Func<CallSite, object, IDictionary<string, object>>> _003C_003Ep__0;

		static AuthenticationWatcher()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CAddArchiveData_003Ed__240 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private ResponceObject _003Cresult_003E5__2;

		private OracleTransaction _003Ctransaction_003E5__3;

		private string _003CExecuteSQL_003E5__4;

		private int _003CnewPrc_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private TaskAwaiter<int> _003C_003Eu__4;

		private List<ARCHV_DOCS>.Enumerator _003C_003E7__wrap8;

		private Exception _003Cex_003E5__10;

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
		internal static bool InstantiateService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AddService()
		{
			return true;
		}

		static _003CAddArchiveData_003Ed__240()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CCheckDstSettings_003Ed__76 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string Pda_Name;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003CUnChiperText_003E5__4;

		private int _003CUser_id_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private string _003CREP_CODE_003E5__8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<_RecordCount> _003C_003Eu__4;

		private Exception _003Ce_003E5__9;

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
		internal static bool RevertService()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DestroyWrapper()
		{
			return true;
		}

		static _003CCheckDstSettings_003Ed__76()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CCheckSetup_003Ed__172 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private FieldValueInt _003CFieldValueInt_003E5__3;

		private OracleTransaction _003Ctran_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private string _003CUnChiperText_003E5__7;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private OracleCommand _003Ccommand_003E5__9;

		private TaskAwaiter<int> _003C_003Eu__5;

		private Exception _003Cex_003E5__10;

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
		internal static bool PrepareWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FlushWrapper()
		{
			return true;
		}

		static _003CCheckSetup_003Ed__172()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CClosedPlan_003Ed__105 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public string DOC_SER;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CSql_003E5__3;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Ce_003E5__4;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool CheckWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SortWrapper()
		{
			return true;
		}

		static _003CClosedPlan_003Ed__105()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CDocDescription_003Ed__92 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<DocDescriptionObjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private DocDescriptionObjctResult _003CDocDescriptionObjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private DocDescriptionObjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

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
		internal static bool PushWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FindWrapper()
		{
			return true;
		}

		static _003CDocDescription_003Ed__92()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CDocsTransferMatching_003Ed__145 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private _RecordCount _003C_RecordCount_003E5__3;

		private string _003CSql_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Ci_003E5__8;

		private TaskAwaiter<_RecordCount> _003C_003Eu__3;

		private Exception _003Ce_003E5__9;

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
		internal static bool PatchWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReflectWrapper()
		{
			return true;
		}

		static _003CDocsTransferMatching_003Ed__145()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CEnrichWithLastStock_003Ed__249 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder _003C_003Et__builder;

		public string mstXml;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public ResponceObject result;

		public List<CustomerItemSold> tempResult;

		private string _003CsqlDtl_003E5__2;

		private CustomerStock _003CchosenStock_003E5__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__1;

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
		internal static bool CustomizeWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ValidateWrapper()
		{
			return true;
		}

		static _003CEnrichWithLastStock_003Ed__249()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CExecutePlan_003Ed__54 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public int P_DOC_TYPE;

		public string P_DOC_SER;

		public string P_C_CODE;

		public string P_REP_CODE;

		public string P_DOC_DATE;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CSql_003E5__3;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<int> _003C_003Eu__2;

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
		internal static bool ConnectWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool WriteWrapper()
		{
			return true;
		}

		static _003CExecutePlan_003Ed__54()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGeoLocations_003Ed__111 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeoLocationResult> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int S_Row;

		public int E_Row;

		private GeoLocationResult _003CGeoLocationResult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003CwhrCntry_003E5__4;

		private string _003CwhrCity_003E5__5;

		private string _003CwhrRegion_003E5__6;

		private string _003CwhrRout_003E5__7;

		private string _003CREP_CODE_003E5__8;

		private object _003C_003E7__wrap8;

		private int _003C_003E7__wrap9;

		private GeoLocationResult _003C_003E7__wrap10;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Ce_003E5__12;

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
		internal static bool OrderWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StartWrapper()
		{
			return true;
		}

		static _003CGeoLocations_003Ed__111()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccCurrencyInner_003Ed__52 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public int Op_id;

		public int Lang_No;

		private ResponceObject _003CGetAccCurrencyOBojctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<bool> _003C_003Eu__4;

		private Exception _003Ce_003E5__8;

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
		internal static bool UpdateWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool VerifyWrapper()
		{
			return true;
		}

		static _003CGetAccCurrencyInner_003Ed__52()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountConfirmBalances_003Ed__218 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool PopWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ComputeWrapper()
		{
			return true;
		}

		static _003CGetAccountConfirmBalances_003Ed__218()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountStatementConfirm_003Ed__227 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool CountWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AssetWrapper()
		{
			return true;
		}

		static _003CGetAccountStatementConfirm_003Ed__227()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountStatment_003Ed__146 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private FieldValueString _003CFieldValueString_003E5__3;

		private FieldValueInt _003CFieldValueInt_003E5__4;

		private int _003CCSTMR_BLNC_TYPE_003E5__5;

		private string _003Csql_003E5__6;

		private object _003C_003E7__wrap6;

		private int _003C_003E7__wrap7;

		private FieldValueString _003CfieldValueString_003E5__9;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__1;

		private ResponceObject _003C_003E7__wrap9;

		private TaskAwaiter<GeneralResult> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__5;

		private Exception _003Cex_003E5__11;

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
		internal static bool CallWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PublishWrapper()
		{
			return true;
		}

		static _003CGetAccountStatment_003Ed__146()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountStatmentDetails_003Ed__147 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject request;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Cwhr_003E5__4;

		private string _003CtableName_003E5__5;

		private int _003CCSTMR_BLNC_TYPE_003E5__6;

		private object _003C_003E7__wrap6;

		private int _003C_003E7__wrap7;

		private FieldValueString _003CfieldValue_003E5__9;

		private List<AccountStatment> _003CtempResult2_003E5__10;

		private ResponceObject _003C_003E7__wrap10;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private FieldValueInt _003CFieldValueInt_003E5__12;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__4;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__5;

		private Exception _003Cex_003E5__13;

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
		internal static bool SetupWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ChangeWrapper()
		{
			return true;
		}

		static _003CGetAccountStatmentDetails_003Ed__147()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAccountStatmentTotalNew_003Ed__231 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject request;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Cwhr_003E5__4;

		private string _003CtableName_003E5__5;

		private int _003CCSTMR_BLNC_TYPE_003E5__6;

		private FieldValueString _003CfieldValue_003E5__7;

		private object _003C_003E7__wrap7;

		private int _003C_003E7__wrap8;

		private FieldValueString _003CFieldValueString_003E5__10;

		private FieldValueInt _003CFieldValueInt_003E5__11;

		private ResponceObject _003C_003E7__wrap11;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__4;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__5;

		private Exception _003Cex_003E5__13;

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
		internal static bool CalcWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResolveWrapper()
		{
			return true;
		}

		static _003CGetAccountStatmentTotalNew_003Ed__231()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAllTaxItems_003Ed__165 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool ExcludeWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool IncludeWrapper()
		{
			return true;
		}

		static _003CGetAllTaxItems_003Ed__165()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAnswerQuestionnaireQuestions_003Ed__159 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool DeleteWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PostWrapper()
		{
			return true;
		}

		static _003CGetAnswerQuestionnaireQuestions_003Ed__159()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetAvlQtyOnline_003Ed__214 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CtempResult_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private Exception _003Cex_003E5__9;

		private ValueTaskAwaiter _003C_003Eu__5;

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
		internal static bool AwakeWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool GetWrapper()
		{
			return true;
		}

		static _003CGetAvlQtyOnline_003Ed__214()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBanksCurrenciesDetails_003Ed__81 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetBanksCurrenciesDetailsOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetBanksCurrenciesDetailsOBjctResult _003CGetBanksCurrenciesDetailsOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetBanksCurrenciesDetailsOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool DisableWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CancelWrapper()
		{
			return true;
		}

		static _003CGetBanksCurrenciesDetails_003Ed__81()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBanksDetails_003Ed__80 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetBanksDetailsOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetBanksDetailsOBjctResult _003CGetBanksDetailsOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetBanksDetailsOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool RemoveWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InterruptWrapper()
		{
			return true;
		}

		static _003CGetBanksDetails_003Ed__80()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillDataForPrint_003Ed__244 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private ResponceObject _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

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
		internal static bool MapWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DefineWrapper()
		{
			return true;
		}

		static _003CGetBillDataForPrint_003Ed__244()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillForNote_003Ed__242 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool ForgotWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FillWrapper()
		{
			return true;
		}

		static _003CGetBillForNote_003Ed__242()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillMasterData_003Ed__148 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool SearchWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool EnableWrapper()
		{
			return true;
		}

		static _003CGetBillMasterData_003Ed__148()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillQrData_003Ed__232 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private ResponceObject _003Cresult_003E5__2;

		private int _003Cbrno_003E5__3;

		private string _003Csql_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

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
		internal static bool InsertWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ViewWrapper()
		{
			return true;
		}

		static _003CGetBillQrData_003Ed__232()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBillSalesCharges_003Ed__204 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool InvokeWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ListWrapper()
		{
			return true;
		}

		static _003CGetBillSalesCharges_003Ed__204()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBranchesData_003Ed__91 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetBrachesDataOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int User_Id;

		private GetBrachesDataOBjctResult _003CGetBrachesDataOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private GetBrachesDataOBjctResult _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Ce_003E5__7;

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
		internal static bool PrintWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalculateWrapper()
		{
			return true;
		}

		static _003CGetBranchesData_003Ed__91()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetBrnchUserPriv_003Ed__115 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetBrnchUserPrivResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string User_No;

		private GetBrnchUserPrivResult _003CGetBrnchUserPrivResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetBrnchUserPrivResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool SelectWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CompareWrapper()
		{
			return true;
		}

		static _003CGetBrnchUserPriv_003Ed__115()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCalcTaxType_003Ed__166 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool ManageWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CloneWrapper()
		{
			return true;
		}

		static _003CGetCalcTaxType_003Ed__166()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCashCurrenciesDetails_003Ed__83 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCashCurrenciesDetailsOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public string REP_CODE;

		public int VerNo;

		public Headers headers;

		private GetCashCurrenciesDetailsOBjctResult _003CGetCashCurrenciesDetailsOBjctResult_003E5__2;

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
		internal static bool MoveWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReadWrapper()
		{
			return true;
		}

		static _003CGetCashCurrenciesDetails_003Ed__83()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCashCustomer_003Ed__209 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool RunWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RegisterWrapper()
		{
			return true;
		}

		static _003CGetCashCustomer_003Ed__209()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCashDetails_003Ed__82 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCashDetailsOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetCashDetailsOBjctResult _003CGetCashDetailsOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetCashDetailsOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool NewWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool TestWrapper()
		{
			return true;
		}

		static _003CGetCashDetails_003Ed__82()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCheckIsAdminSalsManResult_003Ed__61 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCheckIsAdminSalsManResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public string REP_CODE;

		public bool setglobltoNull;

		public string rep_code_fld_nm_in_whr;

		public string c_code;

		private GetCheckIsAdminSalsManResult _003CgetCheckIsAdminSalsManResult_003E5__2;

		private TaskAwaiter<_RecordCount> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

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
		internal static bool CollectWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LogoutWrapper()
		{
			return true;
		}

		static _003CGetCheckIsAdminSalsManResult_003Ed__61()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCreditCardTypes_003Ed__162 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool LoginWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool QueryWrapper()
		{
			return true;
		}

		static _003CGetCreditCardTypes_003Ed__162()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCshBlncWithLmt_003Ed__120 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public string Date;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool InitWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RestartWrapper()
		{
			return true;
		}

		static _003CGetCshBlncWithLmt_003Ed__120()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCurrncy_003Ed__78 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCurrncyOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int type_no;

		public string REP_CODE;

		public string C_Code;

		private GetCurrncyOBjctResult _003CGetCurrncyOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003CC_CODE_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private GetCurrncyOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<GetCheckIsAdminSalsManResult> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

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
		internal static bool CreateWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResetWrapper()
		{
			return true;
		}

		static _003CGetCurrncy_003Ed__78()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustCreditPreiod_003Ed__110 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<CustCreditPreiodResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public string C_CODE;

		private CustCreditPreiodResult _003CCustCreditPreiodResult_003E5__2;

		private OracleTransaction _003Ctran_003E5__3;

		private string _003CSql_003E5__4;

		private GetCheckIsAdminSalsManResult _003CgetCheckIsAdminSalsManResult_003E5__5;

		private string _003CappendWher_003E5__6;

		private CustCreditPreiodResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<GetCheckIsAdminSalsManResult> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<GetCurrncyOBjctResult> _003C_003Eu__4;

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
		internal static bool ConcatWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StopWrapper()
		{
			return true;
		}

		static _003CGetCustCreditPreiod_003Ed__110()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerClassData_003Ed__154 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private List<CUSTOMER_CLASS> _003CCustomerClassDataList_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

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
		internal static bool VisitWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetWrapper()
		{
			return true;
		}

		static _003CGetCustomerClassData_003Ed__154()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerCostCenter_003Ed__208 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool RateWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InstantiateWrapper()
		{
			return true;
		}

		static _003CGetCustomerCostCenter_003Ed__208()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerItemLimitSales_003Ed__203 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool AddWrapper()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RevertWrapper()
		{
			return true;
		}

		static _003CGetCustomerItemLimitSales_003Ed__203()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerItemSold_003Ed__248 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private ResponceObject _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Cwhr_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private List<CustomerItemSold> _003CtempResult_003E5__7;

		private string _003CsqlMst_003E5__8;

		private ResponceObject _003C_003E7__wrap8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__10;

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
		internal static bool DestroyOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrepareOrder()
		{
			return true;
		}

		static _003CGetCustomerItemSold_003Ed__248()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerItemsAvailableQuantity_003Ed__233 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool FlushOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CheckOrder()
		{
			return true;
		}

		static _003CGetCustomerItemsAvailableQuantity_003Ed__233()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerLimitSales_003Ed__202 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool FindOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PatchOrder()
		{
			return true;
		}

		static _003CGetCustomerLimitSales_003Ed__202()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerPlanTarget_003Ed__225 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		public RequstPostObject request;

		private ErrorSystemEntry _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private GetBrachesDataOBjctResult _003CBranchResult_003E5__7;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private TaskAwaiter<GetBrachesDataOBjctResult> _003C_003Eu__4;

		private Exception _003Cex_003E5__9;

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
		internal static bool ReflectOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CustomizeOrder()
		{
			return true;
		}

		static _003CGetCustomerPlanTarget_003Ed__225()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomerStock_003Ed__250 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Cwhr_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private FieldValueString _003CfieldValueString_003E5__7;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__9;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool ValidateOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConnectOrder()
		{
			return true;
		}

		static _003CGetCustomerStock_003Ed__250()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomers_003Ed__79 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetCustomersOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetCustomersOBjctResult _003CGetCustomersOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003CserachColmun_003E5__4;

		private string _003CselectColmun_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private string _003CappendWher_003E5__8;

		private GetCustomersOBjctResult _003C_003E7__wrap8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<GetCheckIsAdminSalsManResult> _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private TaskAwaiter _003C_003Eu__4;

		private Exception _003Ce_003E5__10;

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
		internal static bool WriteOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool OrderOrder()
		{
			return true;
		}

		static _003CGetCustomers_003Ed__79()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetCustomersTargetData_003Ed__171 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool StartOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool UpdateOrder()
		{
			return true;
		}

		static _003CGetCustomersTargetData_003Ed__171()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocBillsData_003Ed__116 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetDocBillsDataResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public string BILL_NO;

		public int BILL_DOC_TYPE;

		private GetDocBillsDataResult _003CGetDocBillsDataResult_003E5__2;

		private string _003CSql_003E5__3;

		private _RecordCount _003CRecordCount_003E5__4;

		private FieldValueString _003CFieldValueString_003E5__5;

		private string _003CBILL_SER_003E5__6;

		private int _003CIsBillDownToRtBill_003E5__7;

		private int _003CIsBillDownToRtBill_Br_003E5__8;

		private string _003CI_QTY_003E5__9;

		private string _003CFREE_QTY_003E5__10;

		private string _003CI_QTY_BR_003E5__11;

		private object _003C_003E7__wrap11;

		private int _003C_003E7__wrap12;

		private OracleDataReader _003Creader_003E5__14;

		private GetDocBillsDataResult _003C_003E7__wrap14;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueString> _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<_RecordCount> _003C_003Eu__4;

		private TaskAwaiter _003C_003Eu__5;

		private TaskAwaiter<bool> _003C_003Eu__6;

		private Exception _003Ce_003E5__16;

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
		internal static bool VerifyOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PopOrder()
		{
			return true;
		}

		static _003CGetDocBillsData_003Ed__116()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocDtls_003Ed__196 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private FieldValueString _003CfieldValueString1_003E5__7;

		private FieldValueString _003CfieldValueString2_003E5__8;

		private ResponceObject _003C_003E7__wrap8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__10;

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
		internal static bool ComputeOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CountOrder()
		{
			return true;
		}

		static _003CGetDocDtls_003Ed__196()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocInfoData_003Ed__177 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool AssetOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CallOrder()
		{
			return true;
		}

		static _003CGetDocInfoData_003Ed__177()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocMst_003Ed__195 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private ValueTaskAwaiter _003C_003Eu__5;

		private Exception _003Cex_003E5__9;

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
		internal static bool PublishOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetupOrder()
		{
			return true;
		}

		static _003CGetDocMst_003Ed__195()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocTypes_003Ed__90 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetDocTypesOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int User_Id;

		private GetDocTypesOBjctResult _003CGetDocTypesOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetDocTypesOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool ChangeOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalcOrder()
		{
			return true;
		}

		static _003CGetDocTypes_003Ed__90()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDocsSyncMethode_003Ed__169 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool ResolveOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ExcludeOrder()
		{
			return true;
		}

		static _003CGetDocsSyncMethode_003Ed__169()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDtsAccountStatmenDocDtl_003Ed__185 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private ValueTaskAwaiter _003C_003Eu__5;

		private Exception _003Cex_003E5__9;

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
		internal static bool IncludeOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DeleteOrder()
		{
			return true;
		}

		static _003CGetDtsAccountStatmenDocDtl_003Ed__185()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDtsCstAging_003Ed__170 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool PostOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AwakeOrder()
		{
			return true;
		}

		static _003CGetDtsCstAging_003Ed__170()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDtsDynamicScreenFileds_003Ed__188 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool GetOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DisableOrder()
		{
			return true;
		}

		static _003CGetDtsDynamicScreenFileds_003Ed__188()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetDtsExpnsTypes_003Ed__175 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool CancelOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RemoveOrder()
		{
			return true;
		}

		static _003CGetDtsExpnsTypes_003Ed__175()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetExtraScreenLabel_003Ed__207 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool InterruptOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MapOrder()
		{
			return true;
		}

		static _003CGetExtraScreenLabel_003Ed__207()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFieldPrivilege1_003Ed__241 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__7;

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
		internal static bool DefineOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ForgotOrder()
		{
			return true;
		}

		static _003CGetFieldPrivilege1_003Ed__241()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFieldPrivilege_003Ed__237 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__7;

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
		internal static bool FillOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SearchOrder()
		{
			return true;
		}

		static _003CGetFieldPrivilege_003Ed__237()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFieldValueDouble_003Ed__73 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<FieldValueDouble> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public int IsCompleteStatement;

		public string FieldName;

		public string TableName;

		private FieldValueDouble _003C_FieldValueDouble_003E5__2;

		private OracleDataReader _003Creader_003E5__3;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<bool> _003C_003Eu__2;

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
		internal static bool EnableOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InsertOrder()
		{
			return true;
		}

		static _003CGetFieldValueDouble_003Ed__73()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFieldValueInt_003Ed__74 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<FieldValueInt> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public int IsCompleteStatement;

		public string FieldName;

		public string TableName;

		private FieldValueInt _003C_FieldValueInt_003E5__2;

		private OracleDataReader _003Creader_003E5__3;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<bool> _003C_003Eu__2;

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
		internal static bool ViewOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InvokeOrder()
		{
			return true;
		}

		static _003CGetFieldValueInt_003Ed__74()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFieldValueString_003Ed__72 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<FieldValueString> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public int IsCompleteStatement;

		public string FieldName;

		public string TableName;

		private FieldValueString _003C_FieldValueString_003E5__2;

		private OracleDataReader _003Creader_003E5__3;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<bool> _003C_003Eu__2;

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
		internal static bool ListOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrintOrder()
		{
			return true;
		}

		static _003CGetFieldValueString_003Ed__72()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFormsPrivilege_003Ed__96 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetFormsPrivilegeResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int User_Id;

		private GetFormsPrivilegeResult _003CGetFormsPrivilegeResult_003E5__2;

		private string _003CMOD_BILL_FLD_NAME_003E5__3;

		private string _003CDEL_BILL_FLD_NAME_003E5__4;

		private string _003CMOD_VOUCHR_FLD_NAME_003E5__5;

		private string _003CDEL_VOUCHR_FLD_NAME_003E5__6;

		private string _003CMOD_Inv_FLD_NAME_003E5__7;

		private string _003CSql_003E5__8;

		private object _003C_003E7__wrap8;

		private int _003C_003E7__wrap9;

		private OracleDataReader _003Creader_003E5__11;

		private GetFormsPrivilegeResult _003C_003E7__wrap11;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<bool> _003C_003Eu__4;

		private Exception _003Ce_003E5__13;

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
		internal static bool CalculateOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SelectOrder()
		{
			return true;
		}

		static _003CGetFormsPrivilege_003Ed__96()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFreeSampleMovement_003Ed__230 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__7;

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
		internal static bool CompareOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ManageOrder()
		{
			return true;
		}

		static _003CGetFreeSampleMovement_003Ed__230()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetFunctionData_003Ed__210 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Cdata_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__4;

		private TaskAwaiter<GetItemsDetailsOBjctResult> _003C_003Eu__5;

		private TaskAwaiter<GetCustomersOBjctResult> _003C_003Eu__6;

		private Exception _003Cex_003E5__9;

		private ValueTaskAwaiter _003C_003Eu__7;

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
		internal static bool CloneOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MoveOrder()
		{
			return true;
		}

		static _003CGetFunctionData_003Ed__210()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGeneralInputData_003Ed__238 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool ReadOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RunOrder()
		{
			return true;
		}

		static _003CGetGeneralInputData_003Ed__238()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGlRequestData_003Ed__246 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private ResponceObject _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool RegisterOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool NewOrder()
		{
			return true;
		}

		static _003CGetGlRequestData_003Ed__246()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGnrTaxCode_003Ed__118 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetGnrTaxCodeResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetGnrTaxCodeResult _003CGetGnrTaxCodeResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetGnrTaxCodeResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool TestOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CollectOrder()
		{
			return true;
		}

		static _003CGetGnrTaxCode_003Ed__118()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGnrTaxItems_003Ed__119 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetGnrTaxItemsResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string Rep_Code;

		public int S_row;

		public int L_row;

		private GetGnrTaxItemsResult _003CGetGnrTaxItemsResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetGnrTaxItemsResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool LogoutOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LoginOrder()
		{
			return true;
		}

		static _003CGetGnrTaxItems_003Ed__119()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetGroupDetails_003Ed__149 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool QueryOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InitOrder()
		{
			return true;
		}

		static _003CGetGroupDetails_003Ed__149()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetInstallmentBills_003Ed__150 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool RestartOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CreateOrder()
		{
			return true;
		}

		static _003CGetInstallmentBills_003Ed__150()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetInvSerialParameter_003Ed__102 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetInvSerialParameterObjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetInvSerialParameterObjctResult _003CGetInvSerialParameterObjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private GetInvSerialParameterObjctResult _003C_003E7__wrap3;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool ResetOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConcatOrder()
		{
			return true;
		}

		static _003CGetInvSerialParameter_003Ed__102()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetInventroyTypes_003Ed__100 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetInventroyTypesOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetInventroyTypesOBjctResult _003CGetInventroyTypesOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private OracleDataReader _003Creader_003E5__4;

		private GetInventroyTypesOBjctResult _003C_003E7__wrap4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

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
		internal static bool StopOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool VisitOrder()
		{
			return true;
		}

		static _003CGetInventroyTypes_003Ed__100()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemCount_003Ed__95 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemCountResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int Type_No;

		public string REP_CODE;

		public int W_Code;

		private GetItemCountResult _003CGetItemCountResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetItemCountResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__3;

		private TaskAwaiter<bool> _003C_003Eu__4;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__5;

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
		internal static bool SetOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RateOrder()
		{
			return true;
		}

		static _003CGetItemCount_003Ed__95()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemSerialsData_003Ed__157 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private List<ITEM_SERIALNO> _003CItemSerialsDataList_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

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
		internal static bool InstantiateOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AddOrder()
		{
			return true;
		}

		static _003CGetItemSerialsData_003Ed__157()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsBarcode_003Ed__98 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsBarcodeOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetItemsBarcodeOBjctResult _003CGetItemsBarcodeOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private OracleDataReader _003Creader_003E5__4;

		private GetItemsBarcodeOBjctResult _003C_003E7__wrap4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

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
		internal static bool RevertOrder()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DestroyInfo()
		{
			return true;
		}

		static _003CGetItemsBarcode_003Ed__98()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsBarcodeData_003Ed__173 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool PrepareInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FlushInfo()
		{
			return true;
		}

		static _003CGetItemsBarcodeData_003Ed__173()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsDataByWHTransferNo_003Ed__128 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private Value<ResponceObject> _003CGetItemsDataOBjctResult_003E5__2;

		private string _003CLANG_NO_003E5__3;

		private string _003CSearch_Value_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

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
		internal static bool CheckInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SortInfo()
		{
			return true;
		}

		static _003CGetItemsDataByWHTransferNo_003Ed__128()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsDetailsPaging_003Ed__84 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsDetailsOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public int S_row;

		public int L_row;

		private GetItemsDetailsOBjctResult _003CGetItemsDetailsOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetItemsDetailsOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<bool> _003C_003Eu__4;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__5;

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
		internal static bool PushInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FindInfo()
		{
			return true;
		}

		static _003CGetItemsDetailsPaging_003Ed__84()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsGroupsData_003Ed__161 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private List<ItemsGroups> _003CItemsGroupsList_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

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
		internal static bool PatchInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReflectInfo()
		{
			return true;
		}

		static _003CGetItemsGroupsData_003Ed__161()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsMarktProperty_003Ed__199 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool CustomizeInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ValidateInfo()
		{
			return true;
		}

		static _003CGetItemsMarktProperty_003Ed__199()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsPriceLevelsPaging_003Ed__94 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsPriceLevelsResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public int S_row;

		public int L_row;

		private GetItemsPriceLevelsResult _003CGetItemsPriceLevelsResult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003CdecimalNo_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private OracleDataReader _003Creader_003E5__7;

		private GetItemsPriceLevelsResult _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueString> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<bool> _003C_003Eu__4;

		private Exception _003Ce_003E5__9;

		private ValueTaskAwaiter _003C_003Eu__5;

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
		internal static bool ConnectInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool WriteInfo()
		{
			return true;
		}

		static _003CGetItemsPriceLevelsPaging_003Ed__94()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsPrices_003Ed__101 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsPriceOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int Lvl_No;

		private GetItemsPriceOBjctResult _003CGetItemsPriceOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private OracleDataReader _003Creader_003E5__4;

		private GetItemsPriceOBjctResult _003C_003E7__wrap4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

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
		internal static bool StartInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool UpdateInfo()
		{
			return true;
		}

		static _003CGetItemsPrices_003Ed__101()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetItemsStorage_003Ed__99 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetItemsStorageOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetItemsStorageOBjctResult _003CGetItemsStorageOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private OracleDataReader _003Creader_003E5__4;

		private GetItemsStorageOBjctResult _003C_003E7__wrap4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

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
		internal static bool VerifyInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PopInfo()
		{
			return true;
		}

		static _003CGetItemsStorage_003Ed__99()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetKey_003Ed__121 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private ClientWatcherDescriptor _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Csubk_003E5__4;

		private string _003CencData_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__9;

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
		internal static bool ComputeInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CountInfo()
		{
			return true;
		}

		static _003CGetKey_003Ed__121()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetLevelPrices_003Ed__103 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetLevelPriceOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetLevelPriceOBjctResult _003CGetLevelPriceOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private OracleDataReader _003Creader_003E5__4;

		private GetLevelPriceOBjctResult _003C_003E7__wrap4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

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
		internal static bool AssetInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CallInfo()
		{
			return true;
		}

		static _003CGetLevelPrices_003Ed__103()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMandatoryField_003Ed__213 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool PublishInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetupInfo()
		{
			return true;
		}

		static _003CGetMandatoryField_003Ed__213()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMarktVisitFlag_003Ed__200 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool ChangeInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalcInfo()
		{
			return true;
		}

		static _003CGetMarktVisitFlag_003Ed__200()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMeasurments_003Ed__85 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetMeasurmentsOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetMeasurmentsOBjctResult _003CGetMeasurmentsOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetMeasurmentsOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool ResolveInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ExcludeInfo()
		{
			return true;
		}

		static _003CGetMeasurments_003Ed__85()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMessageDetails_003Ed__221 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__7;

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
		internal static bool IncludeInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DeleteInfo()
		{
			return true;
		}

		static _003CGetMessageDetails_003Ed__221()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetMobileRequest_003Ed__194 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private string _003Cwhr_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__9;

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
		internal static bool PostInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AwakeInfo()
		{
			return true;
		}

		static _003CGetMobileRequest_003Ed__194()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetParameters_003Ed__89 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetParametersObjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string Rep_Code;

		public int BrnNo;

		private GetParametersObjctResult _003CGetParametersObjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private int _003CuId_003E5__4;

		private FieldValueInt _003CFieldValueInt_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private GetParametersObjctResult _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private Exception _003Ce_003E5__9;

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
		internal static bool GetInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DisableInfo()
		{
			return true;
		}

		static _003CGetParameters_003Ed__89()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetPlanDetails_003Ed__86 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetPlanDetailsOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public string PLAN_DATE;

		public string DOC_SER;

		public string LANG_NO;

		private GetPlanDetailsOBjctResult _003CGetPlanDetailsOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private _RecordCount _003CRecordCount_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private GetPlanDetailsOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<_RecordCount> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private RequstPostObject _003CrequstObject_003E5__8;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__5;

		private Exception _003Ce_003E5__9;

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
		internal static bool CancelInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RemoveInfo()
		{
			return true;
		}

		static _003CGetPlanDetails_003Ed__86()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetPlanSubDetails_003Ed__234 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool InterruptInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DefineInfo()
		{
			return true;
		}

		static _003CGetPlanSubDetails_003Ed__234()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetPriceLevels_003Ed__93 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetPriceLevelsResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetPriceLevelsResult _003CGetPriceLevelsResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetPriceLevelsResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool ForgotInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FillInfo()
		{
			return true;
		}

		static _003CGetPriceLevels_003Ed__93()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQuestionnaireQuestions_003Ed__158 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool SearchInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool EnableInfo()
		{
			return true;
		}

		static _003CGetQuestionnaireQuestions_003Ed__158()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmDtlData_003Ed__152 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool InsertInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ViewInfo()
		{
			return true;
		}

		static _003CGetQutPrmDtlData_003Ed__152()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmDtlData_OLD_003Ed__123 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private ResponceObject _003C_003E7__wrap3;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

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
		internal static bool InvokeInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrintInfo()
		{
			return true;
		}

		static _003CGetQutPrmDtlData_OLD_003Ed__123()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmGrpDtlData_003Ed__125 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool CalculateInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SelectInfo()
		{
			return true;
		}

		static _003CGetQutPrmGrpDtlData_003Ed__125()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmGrpMstData_003Ed__126 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool CompareInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ManageInfo()
		{
			return true;
		}

		static _003CGetQutPrmGrpMstData_003Ed__126()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmMstData_003Ed__122 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool CloneInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MoveInfo()
		{
			return true;
		}

		static _003CGetQutPrmMstData_003Ed__122()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetQutPrmSubDtlData_003Ed__124 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool ReadInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RunInfo()
		{
			return true;
		}

		static _003CGetQutPrmSubDtlData_003Ed__124()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetRecordCount_003Ed__71 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<_RecordCount> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public string TableName;

		private _RecordCount _003CRecordCounts_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private OracleDataReader _003Creader_003E5__4;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<bool> _003C_003Eu__2;

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
		internal static bool RegisterInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool NewInfo()
		{
			return true;
		}

		static _003CGetRecordCount_003Ed__71()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReportAsPdfFromOnyx_003Ed__247 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private DefinitionWatcher _003C_003E8__1;

		private ResponceObject _003Cresult_003E5__2;

		private OracleCommand _003Ccomand_003E5__3;

		private string _003CSql_003E5__4;

		private List<(string, int, string, string)> _003Creports_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private string _003CfilePath_003E5__8;

		private ResponceObject _003C_003E7__wrap8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Ce_003E5__10;

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
		internal static bool CollectInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LogoutInfo()
		{
			return true;
		}

		static _003CGetReportAsPdfFromOnyx_003Ed__247()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReturnFromBill_003Ed__163 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__5;

		private Exception _003Cex_003E5__7;

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
		internal static bool LoginInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool QueryInfo()
		{
			return true;
		}

		static _003CGetReturnFromBill_003Ed__163()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReturnFromBillDetails_003Ed__164 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool InitInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RestartInfo()
		{
			return true;
		}

		static _003CGetReturnFromBillDetails_003Ed__164()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReturnFromRtRqst_003Ed__186 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private ValueTaskAwaiter _003C_003Eu__5;

		private Exception _003Cex_003E5__9;

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
		internal static bool CreateInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResetInfo()
		{
			return true;
		}

		static _003CGetReturnFromRtRqst_003Ed__186()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetReturnFromRtRqstDetails_003Ed__187 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private ValueTaskAwaiter _003C_003Eu__5;

		private Exception _003Cex_003E5__9;

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
		internal static bool ConcatInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StopInfo()
		{
			return true;
		}

		static _003CGetReturnFromRtRqstDetails_003Ed__187()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSFlagCode_003Ed__206 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject request;

		public Headers headers;

		private AdapterDefinitionFilter _003C_003E8__1;

		private object _003C_003E7__wrap1;

		private int _003C_003E7__wrap2;

		private ResponceObject _003C_003E7__wrap3;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccmd_003E5__5;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__4;

		private TaskAwaiter<GetCheckIsAdminSalsManResult> _003C_003Eu__5;

		private Exception _003Cex_003E5__6;

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
		internal static bool VisitInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetInfo()
		{
			return true;
		}

		static _003CGetSFlagCode_003Ed__206()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesCharges_003Ed__117 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetSales_ChargesResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetSales_ChargesResult _003CGetSales_ChargesResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetSales_ChargesResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool RateInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InstantiateInfo()
		{
			return true;
		}

		static _003CGetSalesCharges_003Ed__117()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesFreeQty_003Ed__108 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetSalesFreeQtyOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetSalesFreeQtyOBjctResult _003CGetSalesFreeQtyOBjctResult_003E5__2;

		private _RecordCount _003CRecordCount_003E5__3;

		private string _003CSql_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private OracleDataReader _003Creader_003E5__7;

		private GetSalesFreeQtyOBjctResult _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<_RecordCount> _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private TaskAwaiter _003C_003Eu__4;

		private TaskAwaiter<bool> _003C_003Eu__5;

		private Exception _003Ce_003E5__9;

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
		internal static bool AddInfo()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RevertInfo()
		{
			return true;
		}

		static _003CGetSalesFreeQty_003Ed__108()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesInfo_003Ed__215 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Cwhr_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__8;

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
		internal static bool DestroyDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrepareDic()
		{
			return true;
		}

		static _003CGetSalesInfo_003Ed__215()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesManBranchPrivilege_003Ed__217 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool FlushDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CheckDic()
		{
			return true;
		}

		static _003CGetSalesManBranchPrivilege_003Ed__217()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesManDocumentMovement_003Ed__211 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		private RecordFilterContainer _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Cwhr_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<GetBrachesDataOBjctResult> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool SortDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PushDic()
		{
			return true;
		}

		static _003CGetSalesManDocumentMovement_003Ed__211()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesManItemMovement_003Ed__212 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		private PredicateWatcher _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003Cwhr_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private List<SManItemMove> _003CtempResult_003E5__7;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<GetBrachesDataOBjctResult> _003C_003Eu__4;

		private Exception _003Cex_003E5__9;

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
		internal static bool FindDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PatchDic()
		{
			return true;
		}

		static _003CGetSalesManItemMovement_003Ed__212()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesOrderDtl_003Ed__181 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private ValueTaskAwaiter _003C_003Eu__5;

		private Exception _003Cex_003E5__9;

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
		internal static bool ReflectDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CustomizeDic()
		{
			return true;
		}

		static _003CGetSalesOrderDtl_003Ed__181()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesOrderMst_003Ed__180 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private ValueTaskAwaiter _003C_003Eu__5;

		private Exception _003Cex_003E5__9;

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
		internal static bool ValidateDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConnectDic()
		{
			return true;
		}

		static _003CGetSalesOrderMst_003Ed__180()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSalesSerialNo_003Ed__193 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool WriteDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool OrderDic()
		{
			return true;
		}

		static _003CGetSalesSerialNo_003Ed__193()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSales_discount_003Ed__107 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetSales_discountOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetSales_discountOBjctResult _003CGetSales_discountOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private _RecordCount _003CRecordCount_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private OracleDataReader _003Creader_003E5__7;

		private GetSales_discountOBjctResult _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<_RecordCount> _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private TaskAwaiter _003C_003Eu__4;

		private TaskAwaiter<bool> _003C_003Eu__5;

		private Exception _003Ce_003E5__9;

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
		internal static bool StartDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool UpdateDic()
		{
			return true;
		}

		static _003CGetSales_discount_003Ed__107()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSmanDailayPlan_003Ed__205 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private Exception _003Cex_003E5__9;

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
		internal static bool VerifyDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PopDic()
		{
			return true;
		}

		static _003CGetSmanDailayPlan_003Ed__205()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSmanPlanTrgt_003Ed__174 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool ComputeDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CountDic()
		{
			return true;
		}

		static _003CGetSmanPlanTrgt_003Ed__174()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetStorage_Br_003Ed__87 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetStorageOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetStorageOBjctResult _003CGetStorageOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetStorageOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<bool> _003C_003Eu__4;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__5;

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
		internal static bool AssetDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CallDic()
		{
			return true;
		}

		static _003CGetStorage_Br_003Ed__87()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetStorage_Br_Paging_003Ed__88 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetStorageOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		public int S_row;

		public int L_row;

		private GetStorageOBjctResult _003CGetStorageOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetStorageOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool PublishDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetupDic()
		{
			return true;
		}

		static _003CGetStorage_Br_Paging_003Ed__88()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetSysDateNew_003Ed__104 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetSysDateResult> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		public int ActvieNo;

		public int YearNo;

		public int VerNo;

		private GetSysDateResult _003CGetSysDateResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private string _003CSql_003E5__4;

		private FieldValueString _003CFieldValueString_003E5__5;

		private string _003CINV_CLOSE_003E5__6;

		private string _003CappPass_003E5__7;

		private object _003C_003E7__wrap7;

		private int _003C_003E7__wrap8;

		private GetSysDateResult _003C_003E7__wrap9;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Ce_003E5__11;

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
		internal static bool ChangeDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalcDic()
		{
			return true;
		}

		static _003CGetSysDateNew_003Ed__104()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetTargetPrometerData_003Ed__229 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__7;

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
		internal static bool ResolveDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ExcludeDic()
		{
			return true;
		}

		static _003CGetTargetPrometerData_003Ed__229()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetTaxInputData_003Ed__191 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool IncludeDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DeleteDic()
		{
			return true;
		}

		static _003CGetTaxInputData_003Ed__191()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetTrans_Seq_003Ed__109 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetTrans_SeqResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GetTrans_SeqResult _003CGetTrans_SeqResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetTrans_SeqResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool PostDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AwakeDic()
		{
			return true;
		}

		static _003CGetTrans_Seq_003Ed__109()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetUsers_003Ed__222 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool GetDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DisableDic()
		{
			return true;
		}

		static _003CGetUsers_003Ed__222()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetUsersWithTax_003Ed__77 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetUsersOBjctResult> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string Pda_Name;

		public string Token;

		public string Device_Type;

		private GetUsersOBjctResult _003CGetUsersOBjctResult_003E5__2;

		private FieldValueInt _003CFieldValueInt_003E5__3;

		private int _003CUSE_VAT_003E5__4;

		private string _003CSql_003E5__5;

		private string _003Cpass_003E5__6;

		private int _003CUser_id_003E5__7;

		private string _003CREP_CODE_003E5__8;

		private int _003CPRIV_CASH_003E5__9;

		private int _003CPRIV_CRDT_003E5__10;

		private int _003CPRIV_NTWRK_003E5__11;

		private int _003CPRIV_TRNSFR_003E5__12;

		private int _003CRT_PRIV_CASH_003E5__13;

		private int _003CRT_PRIV_CRDT_003E5__14;

		private int _003CRT_PRIV_NTWRK_003E5__15;

		private int _003CAR_ALLOW_SALES_PRV_DR_003E5__16;

		private int _003CNO_COLCT_003E5__17;

		private int _003CCONN_SP_SMAN_003E5__18;

		private int _003CNO_SAL_003E5__19;

		private int _003CPRV_RT_FROM_BILL_003E5__20;

		private int _003CPRV_RT_PRE_YR_003E5__21;

		private int _003CPRV_RT_WTH_OUT_NO_003E5__22;

		private int _003CuserNo_003E5__23;

		private string _003Cpassword_003E5__24;

		private _RecordCount _003CRecordCount_003E5__25;

		private object _003C_003E7__wrap25;

		private int _003C_003E7__wrap26;

		private GetCheckIsAdminSalsManResult _003CgetCheckIsAdminSalsManResult_003E5__28;

		private int _003CVCHR_PRIV_CASH_003E5__29;

		private int _003CVCHR_PRIV_CRDT_003E5__30;

		private int _003CVCHR_PRIV_TRNSFR_003E5__31;

		private int _003CVCHR_PRIV_CHK_003E5__32;

		private GetUsersOBjctResult _003C_003E7__wrap32;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__2;

		private TaskAwaiter _003C_003Eu__3;

		private TaskAwaiter<GetCheckIsAdminSalsManResult> _003C_003Eu__4;

		private TaskAwaiter<_RecordCount> _003C_003Eu__5;

		private Exception _003Ce_003E5__34;

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
		internal static bool CancelDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RemoveDic()
		{
			return true;
		}

		static _003CGetUsersWithTax_003Ed__77()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetVistFailReasons_003Ed__114 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetVistFailReasonsOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		private GetVistFailReasonsOBjctResult _003CGetVistFailReasonsOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private OracleDataReader _003Creader_003E5__6;

		private GetVistFailReasonsOBjctResult _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

		private Exception _003Ce_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool InterruptDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MapDic()
		{
			return true;
		}

		static _003CGetVistFailReasons_003Ed__114()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetWHTransferMstData_003Ed__127 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private TaskStatusResolver _003C_003E8__1;

		private Value<ResponceObject> _003CWHTransferMst_Result_003E5__2;

		private string _003CUser_No_003E5__3;

		private string _003CLANG_NO_003E5__4;

		private string _003CSearch_Value_003E5__5;

		private string _003Cwcode_003E5__6;

		private object _003C_003E7__wrap6;

		private int _003C_003E7__wrap7;

		private ResponceObject _003C_003E7__wrap8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Ce_003E5__10;

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
		internal static bool DefineDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ForgotDic()
		{
			return true;
		}

		static _003CGetWHTransferMstData_003Ed__127()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetWareHouse_003Ed__97 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GetWareHouseOBjctResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public int User_No;

		private GetWareHouseOBjctResult _003CGetWareHouseOBjctResult_003E5__2;

		private string _003CSql_003E5__3;

		private OracleDataReader _003Creader_003E5__4;

		private GetWareHouseOBjctResult _003C_003E7__wrap4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<bool> _003C_003Eu__3;

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
		internal static bool FillDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SearchDic()
		{
			return true;
		}

		static _003CGetWareHouse_003Ed__97()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetWhReceiveTypes_003Ed__130 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private Value<ResponceObject> _003CWHTransferMst_Result_003E5__2;

		private string _003CUser_No_003E5__3;

		private string _003CLANG_NO_003E5__4;

		private string _003CSql_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private FieldValueInt _003CFieldValueInt_003E5__8;

		private ResponceObject _003C_003E7__wrap8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__3;

		private Exception _003Ce_003E5__10;

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
		internal static bool EnableDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InsertDic()
		{
			return true;
		}

		static _003CGetWhReceiveTypes_003Ed__130()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CGetWhtransSerialNo_003Ed__129 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private FieldValueString _003CfieldValueString_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__8;

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
		internal static bool ViewDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InvokeDic()
		{
			return true;
		}

		static _003CGetWhtransSerialNo_003Ed__129()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CInsertApproveLevel_003Ed__53 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public bool auto_apprv;

		public int P_DOC_TYP;

		public string P_DOC_SER;

		public string P_DOC_NO;

		public int P_JV_TYP;

		public string P_DOC_DATE;

		public string P_CMP_NO;

		public int P_BRN_NO;

		public int P_BRN_YEAR;

		public int P_BRN_USR;

		public int P_AD_U_ID;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CSql_003E5__3;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<int> _003C_003Eu__2;

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
		internal static bool ListDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrintDic()
		{
			return true;
		}

		static _003CInsertApproveLevel_003Ed__53()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003COpenDb_003Ed__62 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public int VerNo;

		public int YearNo;

		public int ActiveNo;

		public Headers headers;

		public int checkSec;

		public int checkDvc;

		private GeneralResult _003CGeneralResult_003E5__2;

		private int _003CsysNo_003E5__3;

		private string _003CfilePath_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private GeneralResult _003C_003E7__wrap6;

		private string _003CDVC_SRL_003E5__8;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__2;

		private string _003CSql_003E5__9;

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
		internal static bool CalculateDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SelectDic()
		{
			return true;
		}

		static _003COpenDb_003Ed__62()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003COpenSysDb_003Ed__64 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public int VerNo;

		public Service _003C_003E4__this;

		private GeneralResult _003CGeneralResult_003E5__2;

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
		internal static bool CompareDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ManageDic()
		{
			return true;
		}

		static _003COpenSysDb_003Ed__64()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveBillNoteRequest_003Ed__243 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CCurrentDoc_srl_003E5__3;

		private string _003CCurrentDocNo_003E5__4;

		private int _003COpFailFLG_003E5__5;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__6;

		private string _003CdataXml_003E5__7;

		private object _003C_003E7__wrap7;

		private int _003C_003E7__wrap8;

		private ResponceObject _003C_003E7__wrap9;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand1_003E5__11;

		private TaskAwaiter<int> _003C_003Eu__3;

		private int _003Ci_003E5__12;

		private Exception _003Cex_003E5__13;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool CloneDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool MoveDic()
		{
			return true;
		}

		static _003CSaveBillNoteRequest_003Ed__243()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveConfirmCustomerBalance_003Ed__219 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private List<AccountConfirmBalance>.Enumerator _003C_003E7__wrap7;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private Exception _003Cex_003E5__9;

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
		internal static bool ReadDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RunDic()
		{
			return true;
		}

		static _003CSaveConfirmCustomerBalance_003Ed__219()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustGpsScan_003Ed__136 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public Cust_Gps_Scan Cust_Gps_Scan;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CSql_003E5__3;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Ci_003E5__4;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private TaskAwaiter<int> _003C_003Eu__4;

		private Exception _003Ce_003E5__5;

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
		internal static bool RegisterDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool NewDic()
		{
			return true;
		}

		static _003CSaveCustGpsScan_003Ed__136()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerAccountStatementConfirm_003Ed__228 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private List<SaveResult> _003CresultMsg_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private List<AccountStatementConfirm>.Enumerator _003C_003E7__wrap8;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private Exception _003Cex_003E5__10;

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
		internal static bool TestDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CollectDic()
		{
			return true;
		}

		static _003CSaveCustomerAccountStatementConfirm_003Ed__228()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerInv_003Ed__131 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public CustomerInv CustomerInv;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CInsertSql_003E5__3;

		private string _003CDOC_SER_003E5__4;

		private string _003CDOC_NO_003E5__5;

		private string _003CxmlData_003E5__6;

		private List<string> _003CResponce_Doc_Ser_003E5__7;

		private object _003C_003E7__wrap7;

		private int _003C_003E7__wrap8;

		private CustomerInv _003CtempCustInvData_003E5__10;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Cj_003E5__11;

		private ResponceObject _003CinnerResult_003E5__12;

		private Exception _003Ce_003E5__13;

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
		internal static bool LogoutDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LoginDic()
		{
			return true;
		}

		static _003CSaveCustomerInv_003Ed__131()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerTarget_003Ed__138 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public CustomerTarget CustomerTarget;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CInsertSql_003E5__3;

		private string _003Csql_003E5__4;

		private List<string> _003CResponce_Doc_Ser_003E5__5;

		private string _003CxmlData_003E5__6;

		private object _003C_003E7__wrap6;

		private int _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Cj_003E5__9;

		private CustomerTarget _003CtempcustomerTarget_003E5__10;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private ResponceObject _003CinnerResult_003E5__11;

		private Exception _003Ce_003E5__12;

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
		internal static bool QueryDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InitDic()
		{
			return true;
		}

		static _003CSaveCustomerTarget_003Ed__138()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerTargetImages_003Ed__167 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private List<string> _003CResponce_Doc_Ser_003E5__2;

		private Value<ResponceObject> _003Cresult_003E5__3;

		private string _003CimagesDirectory_003E5__4;

		private OracleCommand _003Ccommand_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Ci_003E5__9;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__10;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool RestartDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CreateDic()
		{
			return true;
		}

		static _003CSaveCustomerTargetImages_003Ed__167()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveCustomerTargetOld_003Ed__137 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public CustomerTarget CustomerTarget;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private string _003CInsertSql_003E5__4;

		private string _003Csql_003E5__5;

		private string _003CC_CODE_003E5__6;

		private FieldValueString _003CFieldValueString_003E5__7;

		private List<string> _003CResponce_Doc_Ser_003E5__8;

		private OracleTransaction _003Ctrans_003E5__9;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Cj_003E5__10;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private TaskAwaiter<int> _003C_003Eu__4;

		private Exception _003Ce_003E5__11;

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
		internal static bool ResetDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ConcatDic()
		{
			return true;
		}

		static _003CSaveCustomerTargetOld_003Ed__137()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveDeviceToken_003Ed__60 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public string HND_DVC_SRL;

		public int SYS_NO;

		public int U_ID;

		public int DVS_TYP;

		public string DVC_TOKEN;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CInsertSql_003E5__3;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<_RecordCount> _003C_003Eu__2;

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
		internal static bool StopDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool VisitDic()
		{
			return true;
		}

		static _003CSaveDeviceToken_003Ed__60()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveDtsBills_003Ed__189 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Headers headers;

		public Service _003C_003E4__this;

		private SetterSystemModel _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CCurrentDoc_srl_003E5__3;

		private string _003CCurrentDocNo_003E5__4;

		private string _003CdataXml_003E5__5;

		private int _003COpFailFLG_003E5__6;

		private int _003CdocFailFLG_003E5__7;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__8;

		private object _003C_003E7__wrap8;

		private int _003C_003E7__wrap9;

		private ResponceObject _003C_003E7__wrap10;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Ci_003E5__12;

		private TaskAwaiter<ResponceObject> _003C_003Eu__3;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__4;

		private Exception _003Cex_003E5__13;

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
		internal static bool SetDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RateDic()
		{
			return true;
		}

		static _003CSaveDtsBills_003Ed__189()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveDtsRtBills_003Ed__190 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private ErrorWatcher _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CCurrentDoc_srl_003E5__3;

		private string _003CCurrentDocNo_003E5__4;

		private int _003COpFailFLG_003E5__5;

		private int _003CdocFailFLG_003E5__6;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__7;

		private string _003CdataXml_003E5__8;

		private object _003C_003E7__wrap8;

		private int _003C_003E7__wrap9;

		private ResponceObject _003C_003E7__wrap10;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Ci_003E5__12;

		private TaskAwaiter<ResponceObject> _003C_003Eu__3;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__4;

		private Exception _003Cex_003E5__13;

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
		internal static bool InstantiateDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AddDic()
		{
			return true;
		}

		static _003CSaveDtsRtBills_003Ed__190()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveDynamicFieldDocument_003Ed__226 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private string _003CdataXml_003E5__4;

		private int _003COpFailFLG_003E5__5;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__6;

		private object _003C_003E7__wrap6;

		private int _003C_003E7__wrap7;

		private ResponceObject _003C_003E7__wrap8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Ci_003E5__10;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__11;

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
		internal static bool RevertDic()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DestroyField()
		{
			return true;
		}

		static _003CSaveDynamicFieldDocument_003Ed__226()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveExpansDoc_003Ed__176 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private List<string> _003CResponce_Doc_Ser_003E5__3;

		private string _003CdataXml_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

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
		internal static bool PrepareField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FlushField()
		{
			return true;
		}

		static _003CSaveExpansDoc_003Ed__176()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveExpiryOutgoingRequest_003Ed__216 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CCurrentDoc_srl_003E5__3;

		private string _003CCurrentDocNo_003E5__4;

		private int _003COpFailFLG_003E5__5;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__6;

		private string _003CdataXml_003E5__7;

		private object _003C_003E7__wrap7;

		private int _003C_003E7__wrap8;

		private ResponceObject _003C_003E7__wrap9;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand1_003E5__11;

		private TaskAwaiter<int> _003C_003Eu__3;

		private int _003Ci_003E5__12;

		private Exception _003Cex_003E5__13;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool CheckField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SortField()
		{
			return true;
		}

		static _003CSaveExpiryOutgoingRequest_003Ed__216()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveFileAsBlob1_003Ed__198 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private string _003CInsertSql_003E5__4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private string _003CSourceLoc_003E5__5;

		private string _003CDestinationLoc_003E5__6;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private TaskAwaiter<int> _003C_003Eu__4;

		private Exception _003Ce_003E5__7;

		private ValueTaskAwaiter _003C_003Eu__5;

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
		internal static bool PushField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FindField()
		{
			return true;
		}

		static _003CSaveFileAsBlob1_003Ed__198()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveGps_Event_003Ed__133 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public Gps_EventData Gps_EventData;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private OracleTransaction _003Ctran_003E5__4;

		private string _003CInsertSql_003E5__5;

		private string _003CDOC_SEQUENCE_003E5__6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Cj_003E5__7;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private int _003C_003E7__wrap7;

		private TaskAwaiter<int> _003C_003Eu__5;

		private Exception _003Ce_003E5__9;

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
		internal static bool PatchField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReflectField()
		{
			return true;
		}

		static _003CSaveGps_Event_003Ed__133()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveGps_EventCurrent_003Ed__143 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public GpsEventCurnt gpsEventCurnt;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private OracleTransaction _003Ctran_003E5__4;

		private string _003CInsertSql_003E5__5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Ce_003E5__6;

		private object _003C_003E7__wrap6;

		private int _003C_003E7__wrap7;

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
		internal static bool CustomizeField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ValidateField()
		{
			return true;
		}

		static _003CSaveGps_EventCurrent_003Ed__143()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveGps_EventCurrentNew_003Ed__144 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public GpsEventCurnt gpsEventCurnt;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private string _003CInsertSql_003E5__4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

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
		internal static bool ConnectField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool WriteField()
		{
			return true;
		}

		static _003CSaveGps_EventCurrentNew_003Ed__144()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveGps_EventNew_003Ed__134 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public Gps_EventData Gps_EventData;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private OracleTransaction _003Ctran_003E5__4;

		private string _003CInsertSql_003E5__5;

		private string _003CDOC_SEQUENCE_003E5__6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Cj_003E5__7;

		private Task<int> _003Ctask_003E5__8;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private TaskAwaiter<Task<int>> _003C_003Eu__4;

		private TaskAwaiter<int> _003C_003Eu__5;

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
		internal static bool OrderField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StartField()
		{
			return true;
		}

		static _003CSaveGps_EventNew_003Ed__134()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveMarkitingVisit_003Ed__201 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private List<string> _003CResponce_Doc_Ser_003E5__3;

		private List<SaveResult> _003CResponce_Doc_Ser2_003E5__4;

		private string _003CdataXml_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__9;

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
		internal static bool UpdateField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool VerifyField()
		{
			return true;
		}

		static _003CSaveMarkitingVisit_003Ed__201()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveMassage_003Ed__223 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private List<SaveResult> _003CresultMsg_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private List<MessageData>.Enumerator _003C_003E7__wrap8;

		private MessageData _003Citem_003E5__10;

		private Exception _003Cex_003E5__11;

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
		internal static bool PopField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ComputeField()
		{
			return true;
		}

		static _003CSaveMassage_003Ed__223()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveMobileRequest_003Ed__59 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__3;

		private List<string> _003CResponce_Doc_Ser2_003E5__4;

		private string _003Csql_003E5__5;

		private string _003Cid_003E5__6;

		private string _003Curl_003E5__7;

		private object _003C_003E7__wrap7;

		private int _003C_003E7__wrap8;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<FieldValueString> _003C_003Eu__2;

		private OracleCommand _003Ccmd_003E5__10;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__11;

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
		internal static bool CountField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AssetField()
		{
			return true;
		}

		static _003CSaveMobileRequest_003Ed__59()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveOtherVisitTasks_003Ed__235 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private List<string> _003CResponce_Doc_Ser_003E5__3;

		private string _003CdataXml_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__8;

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
		internal static bool CallField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PublishField()
		{
			return true;
		}

		static _003CSaveOtherVisitTasks_003Ed__235()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSavePromoter_003Ed__220 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private List<string> _003CResponce_Doc_Ser_003E5__3;

		private List<SaveResult> _003CResponce_Doc_Ser2_003E5__4;

		private string _003CdataXml_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private Exception _003Cex_003E5__9;

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
		internal static bool SetupField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ChangeField()
		{
			return true;
		}

		static _003CSavePromoter_003Ed__220()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveQuestionnaireDoc_003Ed__160 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private List<string> _003CResponce_Doc_Ser_003E5__3;

		private string _003CdataXml_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

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
		internal static bool CalcField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResolveField()
		{
			return true;
		}

		static _003CSaveQuestionnaireDoc_003Ed__160()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveQuotation_003Ed__132 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private ExceptionAuthenticationInstance _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CCurrentDoc_srl_003E5__3;

		private string _003CCurrentDocNo_003E5__4;

		private int _003COpFailFLG_003E5__5;

		private int _003CdocFailFLG_003E5__6;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__7;

		private string _003CdataXml_003E5__8;

		private object _003C_003E7__wrap8;

		private int _003C_003E7__wrap9;

		private ResponceObject _003C_003E7__wrap10;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand1_003E5__12;

		private TaskAwaiter<int> _003C_003Eu__3;

		private int _003Ci_003E5__13;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__4;

		private Exception _003Cex_003E5__14;

		private ValueTaskAwaiter _003C_003Eu__5;

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
		internal static bool ExcludeField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool IncludeField()
		{
			return true;
		}

		static _003CSaveQuotation_003Ed__132()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveRepPlan_003Ed__141 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RepPlan RepPlan;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private string _003CSql_003E5__4;

		private OracleTransaction _003Ctran_003E5__5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003CI_003E5__6;

		private TaskAwaiter<FieldValueInt> _003C_003Eu__3;

		private Exception _003Ce_003E5__7;

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
		internal static bool DeleteField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PostField()
		{
			return true;
		}

		static _003CSaveRepPlan_003Ed__141()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveRqTransfer_003Ed__140 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RqTransfer RqTransfer;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003CsuccFlg_003E5__4;

		private string _003CdataXml_003E5__5;

		private List<string> _003CResponce_Doc_Ser_003E5__6;

		private object _003C_003E7__wrap6;

		private int _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private int _003CI_003E5__9;

		private RqTransfer _003CrqTransfer_003E5__10;

		private Exception _003Ce_003E5__11;

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
		internal static bool AwakeField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool GetField()
		{
			return true;
		}

		static _003CSaveRqTransfer_003Ed__140()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveRqTransferOld_003Ed__139 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public RqTransfer RqTransfer;

		public Service _003C_003E4__this;

		public Headers headers;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private string _003CSql_003E5__4;

		private OracleTransaction _003Ctran_003E5__5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003CI_003E5__6;

		private TaskAwaiter<int> _003C_003Eu__3;

		private int _003CK_003E5__7;

		private Exception _003Ce_003E5__8;

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
		internal static bool DisableField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CancelField()
		{
			return true;
		}

		static _003CSaveRqTransferOld_003Ed__139()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveSaleOrder_003Ed__182 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private DatabaseDefinitionFilter _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003CCurrentDoc_srl_003E5__4;

		private string _003CCurrentDocNo_003E5__5;

		private string _003CdataXml_003E5__6;

		private int _003COpFailFLG_003E5__7;

		private int _003CdocFailFLG_003E5__8;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__9;

		private object _003C_003E7__wrap9;

		private int _003C_003E7__wrap10;

		private ResponceObject _003C_003E7__wrap11;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private bool _003CisAdmin_003E5__13;

		private int _003Ci_003E5__14;

		private TaskAwaiter<GetCheckIsAdminSalsManResult> _003C_003Eu__3;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__4;

		private Exception _003Cex_003E5__15;

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
		internal static bool RemoveField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InterruptField()
		{
			return true;
		}

		static _003CSaveSaleOrder_003Ed__182()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveSample_003Ed__192 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private List<string> _003CResponce_Doc_Ser2_003E5__3;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__4;

		private string _003CdataXml_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private ResponceObject _003C_003E7__wrap7;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private ValueTaskAwaiter _003C_003Eu__3;

		private Exception _003Cex_003E5__9;

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
		internal static bool MapField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool DefineField()
		{
			return true;
		}

		static _003CSaveSample_003Ed__192()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveShowItems_003Ed__155 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private OracleTransaction _003Ctran_003E5__4;

		private string _003CInsertSql_003E5__5;

		private List<string> _003CResponce_Doc_Ser_003E5__6;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Cj_003E5__8;

		private TaskAwaiter<int> _003C_003Eu__3;

		private int _003Ci_003E5__9;

		private Exception _003Ce_003E5__10;

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
		internal static bool ForgotField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool FillField()
		{
			return true;
		}

		static _003CSaveShowItems_003Ed__155()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveShowItemsImages_003Ed__156 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		private List<string> _003CResponce_Doc_Ser_003E5__2;

		private Value<ResponceObject> _003Cresult_003E5__3;

		private string _003CimagesDirectory_003E5__4;

		private IFormFileCollection _003Cfiles_003E5__5;

		private int _003Ci_003E5__6;

		private Stream _003CfileStream_003E5__7;

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
		internal static bool SearchField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool EnableField()
		{
			return true;
		}

		static _003CSaveShowItemsImages_003Ed__156()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveVists_003Ed__135 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public VistsData VistsData;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CInsertSql_003E5__3;

		private string _003CxmlData_003E5__4;

		private List<string> _003CResponce_Doc_Ser_003E5__5;

		private object _003C_003E7__wrap5;

		private int _003C_003E7__wrap6;

		private VistsData _003CtempVistsData_003E5__8;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Cj_003E5__9;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__3;

		private Exception _003Ce_003E5__10;

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
		internal static bool InsertField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ViewField()
		{
			return true;
		}

		static _003CSaveVists_003Ed__135()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveVouchers_new2_003Ed__151 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

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
		internal static bool InvokeField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ListField()
		{
			return true;
		}

		static _003CSaveVouchers_new2_003Ed__151()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveVouchers_new_003Ed__153 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		public Headers headers;

		private FieldPoolCollection _003C_003E8__1;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private string _003CCurrentDocNo_003E5__4;

		private string _003CCurrentDoc_srl_003E5__5;

		private string _003CCC_CODE_003E5__6;

		private int _003COpFailFLG_003E5__7;

		private int _003CdocFailFLG_003E5__8;

		private List<SaveResult> _003CResponce_Doc_Ser_003E5__9;

		private string _003CdataXml_003E5__10;

		private object _003C_003E7__wrap10;

		private int _003C_003E7__wrap11;

		private int _003Ci_003E5__13;

		private ResponceObject _003C_003E7__wrap13;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand1_003E5__15;

		private TaskAwaiter<int> _003C_003Eu__3;

		private OracleDynamicParameters _003CdapperParameters_003E5__16;

		private int _003Cn_003E5__17;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private TaskAwaiter<Value<ResponceObject>> _003C_003Eu__5;

		private ValueTaskAwaiter _003C_003Eu__6;

		private Exception _003Cex_003E5__18;

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
		internal static bool PrintField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CalculateField()
		{
			return true;
		}

		static _003CSaveVouchers_new_003Ed__153()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSaveWhTransferReciveDoc_003Ed__178 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject postRequstObject;

		private Value<ResponceObject> _003CGeneralResult_003E5__2;

		private string _003CdataXml_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private Exception _003Cex_003E5__7;

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
		internal static bool SelectField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CompareField()
		{
			return true;
		}

		static _003CSaveWhTransferReciveDoc_003Ed__178()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSendByWhatsup_003Ed__236 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public RequstPostObject requstObject;

		public Service _003C_003E4__this;

		private ResponceObject _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private TaskAwaiter _003C_003Eu__1;

		private Exception _003Cex_003E5__6;

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
		internal static bool ManageField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool CloneField()
		{
			return true;
		}

		static _003CSendByWhatsup_003Ed__236()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CSendVerficationMessage_003Ed__245 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<ResponceObject> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private ResponceObject _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

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
		internal static bool MoveField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ReadField()
		{
			return true;
		}

		static _003CSendVerficationMessage_003Ed__245()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CTestApi_003Ed__168 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public RequstPostObject requstObject;

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
		internal static bool RunField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RegisterField()
		{
			return true;
		}

		static _003CTestApi_003Ed__168()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CTestDb_003Ed__112 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		private GeneralResult _003CGeneralResult_003E5__2;

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
		internal static bool NewField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool TestField()
		{
			return true;
		}

		static _003CTestDb_003Ed__112()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateColumn_003Ed__183 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private OracleCommand _003Ccommand_003E5__7;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool CollectField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool LogoutField()
		{
			return true;
		}

		static _003CUpdateColumn_003Ed__183()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateColumnWithProc_003Ed__184 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__7;

		private ValueTaskAwaiter _003C_003Eu__4;

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
		internal static bool LoginField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool QueryField()
		{
			return true;
		}

		static _003CUpdateColumnWithProc_003Ed__184()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateCustomersData_003Ed__142 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public UpdateCustomerData UpdateCustomerData;

		public Headers headers;

		private GeneralResult _003CGeneralResult_003E5__2;

		private OracleCommand _003Ccommand_003E5__3;

		private OracleTransaction _003Ctran_003E5__4;

		private string _003CInsertSql_003E5__5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Cj_003E5__6;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Ce_003E5__7;

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
		internal static bool InitField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RestartField()
		{
			return true;
		}

		static _003CUpdateCustomersData_003Ed__142()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateReadMessage_003Ed__224 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public Headers headers;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private List<SaveResult> _003CresultMsg_003E5__4;

		private object _003C_003E7__wrap4;

		private int _003C_003E7__wrap5;

		private ResponceObject _003C_003E7__wrap6;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Cex_003E5__8;

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
		internal static bool CreateField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool ResetField()
		{
			return true;
		}

		static _003CUpdateReadMessage_003Ed__224()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateSyncStatues_003Ed__106 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public int SYNC_TYP;

		public Service _003C_003E4__this;

		public Headers headers;

		public int YearNo;

		public int ActvieNo;

		public int VerNo;

		public string REP_CODE;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CSql_003E5__3;

		private string _003CSync_fld_date_name_003E5__4;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private Exception _003Ce_003E5__5;

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
		internal static bool ConcatField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool StopField()
		{
			return true;
		}

		static _003CUpdateSyncStatues_003Ed__106()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUpdateUserPassword_003Ed__239 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		public Headers headers;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003CSql_003E5__3;

		private object _003C_003E7__wrap3;

		private int _003C_003E7__wrap4;

		private ResponceObject _003C_003E7__wrap5;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private TaskAwaiter<int> _003C_003Eu__3;

		private TaskAwaiter<FieldValueString> _003C_003Eu__4;

		private Exception _003Cex_003E5__7;

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
		internal static bool VisitField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool SetField()
		{
			return true;
		}

		static _003CUpdateUserPassword_003Ed__239()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUploadExpnsImages_003Ed__179 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public RequstPostObject requstObject;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private Stream _003Csw_003E5__3;

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
		internal static bool RateField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool InstantiateField()
		{
			return true;
		}

		static _003CUploadExpnsImages_003Ed__179()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CUploadFile_003Ed__197 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<GeneralResult> _003C_003Et__builder;

		public Headers headers;

		public Service _003C_003E4__this;

		private GeneralResult _003CGeneralResult_003E5__2;

		private string _003CfileName_003E5__3;

		private string _003CarchivePath_003E5__4;

		private string _003CfolderPath_003E5__5;

		private string _003Csql_003E5__6;

		private int _003CCON_NO_003E5__7;

		private RequstPostObject _003CrequstObject_003E5__8;

		private IFormFileCollection _003Cfiles_003E5__9;

		private ResponceObject _003Cresult_003E5__10;

		private ResponceObject _003C_003E7__wrap10;

		private TaskAwaiter<GeneralResult> _003C_003Eu__1;

		private TaskAwaiter _003C_003Eu__2;

		private int _003Ci_003E5__12;

		private Stream _003CfileStream_003E5__13;

		private FieldValueString _003CfieldValueString_003E5__14;

		private TaskAwaiter<FieldValueString> _003C_003Eu__3;

		private ValueTaskAwaiter _003C_003Eu__4;

		private TaskAwaiter<ResponceObject> _003C_003Eu__5;

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
		internal static bool AddField()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool RevertField()
		{
			return true;
		}

		static _003CUploadFile_003Ed__197()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	[StructLayout(LayoutKind.Auto)]
	[CompilerGenerated]
	private struct _003CgetSqlQuery_003Ed__75 : IAsyncStateMachine
	{
		public int _003C_003E1__state;

		public AsyncTaskMethodBuilder<Value<ResponceObject>> _003C_003Et__builder;

		public Service _003C_003E4__this;

		public string Dsh_NO;

		private Value<ResponceObject> _003Cresult_003E5__2;

		private string _003Csql_003E5__3;

		private TaskAwaiter _003C_003Eu__1;

		private TaskAwaiter<FieldValueString> _003C_003Eu__2;

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
		internal static bool DestroyAdapter()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool PrepareAdapter()
		{
			return true;
		}

		static _003CgetSqlQuery_003Ed__75()
		{
			IssuerWatcherWriter.CustomizeUtils();
		}
	}

	private JsonSerializerSettings _WatcherWatcher;

	internal readonly IWebHostEnvironment _VisitorWatcher;

	internal readonly IOptions<ApiConfig> utilsWatcher;

	public OracleConnection con;

	public int WsVer_No;

	public string WSversionCode;

	public int DBversionCode;

	public string SchemaName;

	public string Date_format;

	public string Date_time_format;

	public string SERVICE_NAME;

	public string HOST;

	public string PORT;

	public string Password;

	public string ImagesPath;

	public string UpdateUrl;

	public string CommandUrl;

	public string ActiveSaveDoc;

	public string MappDirectionsKey;

	public string ShowMappDirectionsPerDayLmt;

	public string OneDayAccountStatment;

	public string ApplyDublicateDocAsPosted;

	public string ENCRYPTED_QR;

	public string SHW_CST_ACC_STMNT_DAY;

	public string GpsPostIntervalInSec;

	public string GpsTrackIntervalInSec;

	public string InActiveGPSTrack;

	public string WhatsAppUrl;

	public string WhatsAppPort;

	public string GpsDistanceTrackInMetr;

	public string AppPass;

	public string UseArchived;

	public string pdfReportPath;

	public string pdfReportName;

	public string vocherOutVisit;

	public string hideCode;

	private string poolWatcher;

	private List<ReportNameModel> m_FilterWatcher;

	private int _StatusWatcher;

	public static int globcheckSec;

	public string[]? ActiveSaveDocRep;

	[MethodImpl(MethodImplOptions.NoInlining)]
	public Service(IOptions<ApiConfig> config, IWebHostEnvironment env)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private string SortWatcher(string P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private string CountWatcher(string P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private void DefineWatcher(string P_0)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public void LogWriteHistory(string data = "", dynamic model = null, string Type = "RQ", Headers headers = null)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public void LogHistory(string logMessage, TextWriter txtWriter)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private void ReflectWatcher(string P_0, TextWriter P_1)
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private GeneralResult ConcatWatcher(RequstPostObject P_0, string P_1, GetBrachesDataOBjct P_2)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static JObject LoginWatcher(object P_0, object P_1, int P_2)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static string FindWatcher<T>(object P_0, IEnumerable<T> P_1, List<string> P_2)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static string ConnectWatcher(object P_0, object P_1, object P_2, List<string> P_3)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAccCurrencyInner_003Ed__52))]
	private Task<ResponceObject> NewWatcher(int P_0, int P_1, string P_2, int P_3, int P_4, int P_5, Headers P_6)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CInsertApproveLevel_003Ed__53))]
	private Task<GeneralResult> InstantiateWatcher(int P_0, string P_1, string P_2, int P_3, string P_4, string P_5, int P_6, int P_7, int P_8, int P_9, bool P_10 = false)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CExecutePlan_003Ed__54))]
	private Task<GeneralResult> ViewWatcher(int P_0, string P_1, string P_2, string P_3, string P_4)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private ResponceObject PublishWatcher(OracleTransaction P_0, int P_1, string P_2, string P_3, string P_4)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private ResponceObject ComputeWatcher(string P_0, string P_1, string P_2, int P_3 = 1407, int P_4 = 1, int P_5 = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private string IncludeWatcher(string P_0, string P_1, string P_2, string P_3, string P_4, string P_5, string P_6, string P_7)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private string PopWatcher(string P_0, string P_1, string P_2, string P_3, string P_4, string P_5, string P_6, string P_7, string P_8, string P_9, string P_10, string P_11)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveMobileRequest_003Ed__59))]
	private Task<Value<ResponceObject>> CollectWatcher(RequstPostObject P_0, Headers P_1)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveDeviceToken_003Ed__60))]
	private Task<GeneralResult> CompareWatcher(int P_0, int P_1, string P_2, int P_3, string P_4)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCheckIsAdminSalsManResult_003Ed__61))]
	private Task<GetCheckIsAdminSalsManResult> RegisterWatcher(string P_0, string P_1, bool P_2, string P_3 = null)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003COpenDb_003Ed__62))]
	private Task<GeneralResult> SetupWatcher(Headers P_0, int P_1, int P_2, int P_3, int P_4 = 1, int P_5 = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private GeneralResult ExcludeWatcher(int P_0, int P_1, int P_2)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003COpenSysDb_003Ed__64))]
	private Task<GeneralResult> ReadWatcher(int P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private GeneralResult CreateWatcher(int P_0, string P_1)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private List<T> OrderWatcher<T>(string P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private void InvokeWatcher()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private string CustomizeWatcher(string P_0, OracleConnection P_1)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private List<List<string>> CalcWatcher(string P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static dynamic SetWatcher(object P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetRecordCount_003Ed__71))]
	private Task<_RecordCount> MapWatcher(string P_0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetFieldValueString_003Ed__72))]
	private Task<FieldValueString> DisableWatcher(string P_0, string P_1, int P_2 = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetFieldValueDouble_003Ed__73))]
	private Task<FieldValueDouble> ChangeWatcher(string P_0, string P_1, int P_2 = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetFieldValueInt_003Ed__74))]
	private Task<FieldValueInt> DestroyWatcher(string P_0, string P_1, int P_2 = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CgetSqlQuery_003Ed__75))]
	private Task<Value<ResponceObject>> InsertWatcher(int P_0, int P_1, string P_2)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CCheckDstSettings_003Ed__76))]
	public Task<GeneralResult> CheckDstSettings(int YearNo, int ActvieNo, int Branch_No, int Lnag_No, string Pda_Name, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetUsersWithTax_003Ed__77))]
	public Task<GetUsersOBjctResult> GetUsersWithTax(int YearNo, int ActvieNo, int Branch_No, string Pda_Name, int op_type, int VerNo, Headers headers, string Token = "", string Device_Type = "1")
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCurrncy_003Ed__78))]
	public Task<GetCurrncyOBjctResult> GetCurrncy(Headers headers, int YearNo, int ActvieNo, int Branch_No, int type_no, string REP_CODE, int VerNo, string C_Code = "")
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomers_003Ed__79))]
	public Task<GetCustomersOBjctResult> GetCustomers(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBanksDetails_003Ed__80))]
	public Task<GetBanksDetailsOBjctResult> GetBanksDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBanksCurrenciesDetails_003Ed__81))]
	public Task<GetBanksCurrenciesDetailsOBjctResult> GetBanksCurrenciesDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCashDetails_003Ed__82))]
	public Task<GetCashDetailsOBjctResult> GetCashDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCashCurrenciesDetails_003Ed__83))]
	public Task<GetCashCurrenciesDetailsOBjctResult> GetCashCurrenciesDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsDetailsPaging_003Ed__84))]
	public Task<GetItemsDetailsOBjctResult> GetItemsDetailsPaging(int YearNo, int ActvieNo, int Branch_No, int GRP_CODE, string REP_CODE, int S_row, int L_row, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetMeasurments_003Ed__85))]
	public Task<GetMeasurmentsOBjctResult> GetMeasurments(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetPlanDetails_003Ed__86))]
	public Task<GetPlanDetailsOBjctResult> GetPlanDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, string PLAN_DATE, int VerNo, Headers headers, string DOC_SER = "", string LANG_NO = "1")
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetStorage_Br_003Ed__87))]
	public Task<GetStorageOBjctResult> GetStorage_Br(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetStorage_Br_Paging_003Ed__88))]
	public Task<GetStorageOBjctResult> GetStorage_Br_Paging(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int S_row, int L_row, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetParameters_003Ed__89))]
	public Task<GetParametersObjctResult> GetParameters(int YearNo, int ActvieNo, string Rep_Code, int VerNo, Headers headers, int BrnNo = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDocTypes_003Ed__90))]
	public Task<GetDocTypesOBjctResult> GetDocTypes(int YearNo, int ActvieNo, int Branch_No, int User_Id, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBranchesData_003Ed__91))]
	public Task<GetBrachesDataOBjctResult> GetBranchesData(int YearNo, int ActvieNo, int Branch_No, int User_Id, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CDocDescription_003Ed__92))]
	public Task<DocDescriptionObjctResult> DocDescription(int YearNo, int ActvieNo, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetPriceLevels_003Ed__93))]
	public Task<GetPriceLevelsResult> GetPriceLevels(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsPriceLevelsPaging_003Ed__94))]
	public Task<GetItemsPriceLevelsResult> GetItemsPriceLevelsPaging(int YearNo, int ActvieNo, string REP_CODE, int S_row, int L_row, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemCount_003Ed__95))]
	public Task<GetItemCountResult> GetItemCount(int YearNo, int ActvieNo, string REP_CODE, int Type_No, int VerNo, int W_Code, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetFormsPrivilege_003Ed__96))]
	public Task<GetFormsPrivilegeResult> GetFormsPrivilege(int YearNo, int ActvieNo, int User_Id, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetWareHouse_003Ed__97))]
	public Task<GetWareHouseOBjctResult> GetWareHouse(int YearNo, int ActvieNo, int User_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsBarcode_003Ed__98))]
	public Task<GetItemsBarcodeOBjctResult> GetItemsBarcode(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsStorage_003Ed__99))]
	public Task<GetItemsStorageOBjctResult> GetItemsStorage(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetInventroyTypes_003Ed__100))]
	public Task<GetInventroyTypesOBjctResult> GetInventroyTypes(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsPrices_003Ed__101))]
	public Task<GetItemsPriceOBjctResult> GetItemsPrices(int YearNo, int ActvieNo, int Branch_No, int Lvl_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetInvSerialParameter_003Ed__102))]
	public Task<GetInvSerialParameterObjctResult> GetInvSerialParameter(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetLevelPrices_003Ed__103))]
	public Task<GetLevelPriceOBjctResult> GetLevelPrices(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSysDateNew_003Ed__104))]
	public Task<GetSysDateResult> GetSysDateNew(int YearNo, int ActvieNo, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CClosedPlan_003Ed__105))]
	public Task<GeneralResult> ClosedPlan(int YearNo, int ActvieNo, string REP_CODE, string DOC_SER, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUpdateSyncStatues_003Ed__106))]
	public Task<GeneralResult> UpdateSyncStatues(int YearNo, int ActvieNo, string REP_CODE, int SYNC_TYP, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSales_discount_003Ed__107))]
	public Task<GetSales_discountOBjctResult> GetSales_discount(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesFreeQty_003Ed__108))]
	public Task<GetSalesFreeQtyOBjctResult> GetSalesFreeQty(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetTrans_Seq_003Ed__109))]
	public Task<GetTrans_SeqResult> GetTrans_Seq(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustCreditPreiod_003Ed__110))]
	public Task<CustCreditPreiodResult> GetCustCreditPreiod(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers, string C_CODE)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGeoLocations_003Ed__111))]
	public Task<GeoLocationResult> GeoLocations(Headers headers, int YearNo, int ActvieNo, int VerNo, int S_Row = 0, int E_Row = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CTestDb_003Ed__112))]
	public Task<GeneralResult> TestDb()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public GeneralResult TestWs()
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetVistFailReasons_003Ed__114))]
	public Task<GetVistFailReasonsOBjctResult> GetVistFailReasons(int YearNo, int ActvieNo, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBrnchUserPriv_003Ed__115))]
	public Task<GetBrnchUserPrivResult> GetBrnchUserPriv(int YearNo, int ActvieNo, string User_No, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDocBillsData_003Ed__116))]
	public Task<GetDocBillsDataResult> GetDocBillsData(int YearNo, int ActvieNo, string REP_CODE, int BILL_DOC_TYPE, string BILL_NO, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesCharges_003Ed__117))]
	public Task<GetSales_ChargesResult> GetSalesCharges(int YearNo, int ActvieNo, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetGnrTaxCode_003Ed__118))]
	public Task<GetGnrTaxCodeResult> GetGnrTaxCode(int YearNo, int ActvieNo, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetGnrTaxItems_003Ed__119))]
	public Task<GetGnrTaxItemsResult> GetGnrTaxItems(int YearNo, int ActvieNo, string Rep_Code, int S_row, int L_row, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCshBlncWithLmt_003Ed__120))]
	public Task<Value<ResponceObject>> GetCshBlncWithLmt(int YearNo, int ActvieNo, string REP_CODE, string Date, int VerNo, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetKey_003Ed__121))]
	public Task<Value<ResponceObject>> GetKey(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQutPrmMstData_003Ed__122))]
	public Task<Value<ResponceObject>> GetQutPrmMstData(RequstObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQutPrmDtlData_OLD_003Ed__123))]
	public Task<Value<ResponceObject>> GetQutPrmDtlData_OLD(RequstObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQutPrmSubDtlData_003Ed__124))]
	public Task<Value<ResponceObject>> GetQutPrmSubDtlData(RequstObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQutPrmGrpDtlData_003Ed__125))]
	public Task<Value<ResponceObject>> GetQutPrmGrpDtlData(RequstObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQutPrmGrpMstData_003Ed__126))]
	public Task<Value<ResponceObject>> GetQutPrmGrpMstData(RequstObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetWHTransferMstData_003Ed__127))]
	public Task<Value<ResponceObject>> GetWHTransferMstData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsDataByWHTransferNo_003Ed__128))]
	public Task<Value<ResponceObject>> GetItemsDataByWHTransferNo(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetWhtransSerialNo_003Ed__129))]
	public Task<Value<ResponceObject>> GetWhtransSerialNo(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetWhReceiveTypes_003Ed__130))]
	public Task<Value<ResponceObject>> GetWhReceiveTypes(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustomerInv_003Ed__131))]
	public Task<GeneralResult> SaveCustomerInv(CustomerInv CustomerInv, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveQuotation_003Ed__132))]
	public Task<Value<ResponceObject>> SaveQuotation(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveGps_Event_003Ed__133))]
	public Task<GeneralResult> SaveGps_Event(Gps_EventData Gps_EventData, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveGps_EventNew_003Ed__134))]
	public Task<GeneralResult> SaveGps_EventNew(Gps_EventData Gps_EventData, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveVists_003Ed__135))]
	public Task<GeneralResult> SaveVists(VistsData VistsData, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustGpsScan_003Ed__136))]
	public Task<GeneralResult> SaveCustGpsScan(Cust_Gps_Scan Cust_Gps_Scan, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustomerTargetOld_003Ed__137))]
	public Task<GeneralResult> SaveCustomerTargetOld(CustomerTarget CustomerTarget, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustomerTarget_003Ed__138))]
	public Task<GeneralResult> SaveCustomerTarget(CustomerTarget CustomerTarget, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveRqTransferOld_003Ed__139))]
	public Task<GeneralResult> SaveRqTransferOld(RqTransfer RqTransfer, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveRqTransfer_003Ed__140))]
	public Task<GeneralResult> SaveRqTransfer(RqTransfer RqTransfer, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveRepPlan_003Ed__141))]
	public Task<GeneralResult> SaveRepPlan(RepPlan RepPlan, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUpdateCustomersData_003Ed__142))]
	public Task<GeneralResult> UpdateCustomersData(UpdateCustomerData UpdateCustomerData, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveGps_EventCurrent_003Ed__143))]
	public Task<GeneralResult> SaveGps_EventCurrent(GpsEventCurnt gpsEventCurnt, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveGps_EventCurrentNew_003Ed__144))]
	public Task<GeneralResult> SaveGps_EventCurrentNew(GpsEventCurnt gpsEventCurnt, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CDocsTransferMatching_003Ed__145))]
	public Task<Value<ResponceObject>> DocsTransferMatching(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAccountStatment_003Ed__146))]
	public Task<Value<ResponceObject>> GetAccountStatment(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAccountStatmentDetails_003Ed__147))]
	public Task<Value<ResponceObject>> GetAccountStatmentDetails(RequstPostObject request, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBillMasterData_003Ed__148))]
	public Task<Value<ResponceObject>> GetBillMasterData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetGroupDetails_003Ed__149))]
	public Task<Value<ResponceObject>> GetGroupDetails(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetInstallmentBills_003Ed__150))]
	public Task<Value<ResponceObject>> GetInstallmentBills(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveVouchers_new2_003Ed__151))]
	public Task<Value<ResponceObject>> SaveVouchers_new2(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQutPrmDtlData_003Ed__152))]
	public Task<Value<ResponceObject>> GetQutPrmDtlData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveVouchers_new_003Ed__153))]
	public Task<Value<ResponceObject>> SaveVouchers_new(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerClassData_003Ed__154))]
	public Task<Value<ResponceObject>> GetCustomerClassData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveShowItems_003Ed__155))]
	public Task<Value<ResponceObject>> SaveShowItems(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveShowItemsImages_003Ed__156))]
	public Task<Value<ResponceObject>> SaveShowItemsImages(Stream stream, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemSerialsData_003Ed__157))]
	public Task<Value<ResponceObject>> GetItemSerialsData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetQuestionnaireQuestions_003Ed__158))]
	public Task<Value<ResponceObject>> GetQuestionnaireQuestions(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAnswerQuestionnaireQuestions_003Ed__159))]
	public Task<Value<ResponceObject>> GetAnswerQuestionnaireQuestions(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveQuestionnaireDoc_003Ed__160))]
	public Task<Value<ResponceObject>> SaveQuestionnaireDoc(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsGroupsData_003Ed__161))]
	public Task<Value<ResponceObject>> GetItemsGroupsData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCreditCardTypes_003Ed__162))]
	public Task<Value<ResponceObject>> GetCreditCardTypes(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetReturnFromBill_003Ed__163))]
	public Task<Value<ResponceObject>> GetReturnFromBill(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetReturnFromBillDetails_003Ed__164))]
	public Task<Value<ResponceObject>> GetReturnFromBillDetails(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAllTaxItems_003Ed__165))]
	public Task<Value<ResponceObject>> GetAllTaxItems(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCalcTaxType_003Ed__166))]
	public Task<Value<ResponceObject>> GetCalcTaxType(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustomerTargetImages_003Ed__167))]
	public Task<Value<ResponceObject>> SaveCustomerTargetImages(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CTestApi_003Ed__168))]
	public Task<Value<ResponceObject>> TestApi(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDocsSyncMethode_003Ed__169))]
	public Task<Value<ResponceObject>> GetDocsSyncMethode(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDtsCstAging_003Ed__170))]
	public Task<Value<ResponceObject>> GetDtsCstAging(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomersTargetData_003Ed__171))]
	public Task<Value<ResponceObject>> GetCustomersTargetData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CCheckSetup_003Ed__172))]
	public Task<Value<ResponceObject>> CheckSetup(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsBarcodeData_003Ed__173))]
	public Task<Value<ResponceObject>> GetItemsBarcodeData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSmanPlanTrgt_003Ed__174))]
	public Task<Value<ResponceObject>> GetSmanPlanTrgt(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDtsExpnsTypes_003Ed__175))]
	public Task<Value<ResponceObject>> GetDtsExpnsTypes(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveExpansDoc_003Ed__176))]
	public Task<Value<ResponceObject>> SaveExpansDoc(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDocInfoData_003Ed__177))]
	public Task<Value<ResponceObject>> GetDocInfoData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveWhTransferReciveDoc_003Ed__178))]
	public Task<Value<ResponceObject>> SaveWhTransferReciveDoc(RequstPostObject postRequstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUploadExpnsImages_003Ed__179))]
	public Task<Value<ResponceObject>> UploadExpnsImages(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesOrderMst_003Ed__180))]
	public Task<Value<ResponceObject>> GetSalesOrderMst(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesOrderDtl_003Ed__181))]
	public Task<Value<ResponceObject>> GetSalesOrderDtl(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveSaleOrder_003Ed__182))]
	public Task<Value<ResponceObject>> SaveSaleOrder(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUpdateColumn_003Ed__183))]
	public Task<Value<ResponceObject>> UpdateColumn(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUpdateColumnWithProc_003Ed__184))]
	public Task<Value<ResponceObject>> UpdateColumnWithProc(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDtsAccountStatmenDocDtl_003Ed__185))]
	public Task<Value<ResponceObject>> GetDtsAccountStatmenDocDtl(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetReturnFromRtRqst_003Ed__186))]
	public Task<Value<ResponceObject>> GetReturnFromRtRqst(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetReturnFromRtRqstDetails_003Ed__187))]
	public Task<Value<ResponceObject>> GetReturnFromRtRqstDetails(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDtsDynamicScreenFileds_003Ed__188))]
	public Task<Value<ResponceObject>> GetDtsDynamicScreenFileds(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveDtsBills_003Ed__189))]
	public Task<Value<ResponceObject>> SaveDtsBills(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveDtsRtBills_003Ed__190))]
	public Task<Value<ResponceObject>> SaveDtsRtBills(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetTaxInputData_003Ed__191))]
	public Task<Value<ResponceObject>> GetTaxInputData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveSample_003Ed__192))]
	public Task<Value<ResponceObject>> SaveSample(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesSerialNo_003Ed__193))]
	public Task<Value<ResponceObject>> GetSalesSerialNo(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetMobileRequest_003Ed__194))]
	public Task<Value<ResponceObject>> GetMobileRequest(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDocMst_003Ed__195))]
	public Task<Value<ResponceObject>> GetDocMst(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetDocDtls_003Ed__196))]
	public Task<Value<ResponceObject>> GetDocDtls(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUploadFile_003Ed__197))]
	public Task<GeneralResult> UploadFile(Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveFileAsBlob1_003Ed__198))]
	public Task<GeneralResult> SaveFileAsBlob1(Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetItemsMarktProperty_003Ed__199))]
	public Task<Value<ResponceObject>> GetItemsMarktProperty(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetMarktVisitFlag_003Ed__200))]
	public Task<Value<ResponceObject>> GetMarktVisitFlag(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveMarkitingVisit_003Ed__201))]
	public Task<Value<ResponceObject>> SaveMarkitingVisit(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerLimitSales_003Ed__202))]
	public Task<Value<ResponceObject>> GetCustomerLimitSales(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerItemLimitSales_003Ed__203))]
	public Task<Value<ResponceObject>> GetCustomerItemLimitSales(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBillSalesCharges_003Ed__204))]
	public Task<Value<ResponceObject>> GetBillSalesCharges(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSmanDailayPlan_003Ed__205))]
	public Task<Value<ResponceObject>> GetSmanDailayPlan(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSFlagCode_003Ed__206))]
	public Task<Value<ResponceObject>> GetSFlagCode(RequstPostObject request, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetExtraScreenLabel_003Ed__207))]
	public Task<Value<ResponceObject>> GetExtraScreenLabel(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerCostCenter_003Ed__208))]
	public Task<Value<ResponceObject>> GetCustomerCostCenter(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCashCustomer_003Ed__209))]
	public Task<Value<ResponceObject>> GetCashCustomer(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetFunctionData_003Ed__210))]
	public Task<Value<ResponceObject>> GetFunctionData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesManDocumentMovement_003Ed__211))]
	public Task<Value<ResponceObject>> GetSalesManDocumentMovement(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesManItemMovement_003Ed__212))]
	public Task<Value<ResponceObject>> GetSalesManItemMovement(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetMandatoryField_003Ed__213))]
	public Task<Value<ResponceObject>> GetMandatoryField(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAvlQtyOnline_003Ed__214))]
	public Task<Value<ResponceObject>> GetAvlQtyOnline(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesInfo_003Ed__215))]
	public Task<Value<ResponceObject>> GetSalesInfo(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveExpiryOutgoingRequest_003Ed__216))]
	public Task<Value<ResponceObject>> SaveExpiryOutgoingRequest(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetSalesManBranchPrivilege_003Ed__217))]
	public Task<Value<ResponceObject>> GetSalesManBranchPrivilege(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAccountConfirmBalances_003Ed__218))]
	public Task<Value<ResponceObject>> GetAccountConfirmBalances(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveConfirmCustomerBalance_003Ed__219))]
	public Task<Value<ResponceObject>> SaveConfirmCustomerBalance(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSavePromoter_003Ed__220))]
	public Task<Value<ResponceObject>> SavePromoter(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetMessageDetails_003Ed__221))]
	public Task<Value<ResponceObject>> GetMessageDetails(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetUsers_003Ed__222))]
	public Task<Value<ResponceObject>> GetUsers(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveMassage_003Ed__223))]
	public Task<Value<ResponceObject>> SaveMassage(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUpdateReadMessage_003Ed__224))]
	public Task<Value<ResponceObject>> UpdateReadMessage(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerPlanTarget_003Ed__225))]
	public Task<Value<ResponceObject>> GetCustomerPlanTarget(RequstPostObject request, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveDynamicFieldDocument_003Ed__226))]
	public Task<Value<ResponceObject>> SaveDynamicFieldDocument(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAccountStatementConfirm_003Ed__227))]
	public Task<Value<ResponceObject>> GetAccountStatementConfirm(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveCustomerAccountStatementConfirm_003Ed__228))]
	public Task<Value<ResponceObject>> SaveCustomerAccountStatementConfirm(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetTargetPrometerData_003Ed__229))]
	public Task<Value<ResponceObject>> GetTargetPrometerData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetFreeSampleMovement_003Ed__230))]
	public Task<Value<ResponceObject>> GetFreeSampleMovement(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetAccountStatmentTotalNew_003Ed__231))]
	public Task<Value<ResponceObject>> GetAccountStatmentTotalNew(RequstPostObject request, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBillQrData_003Ed__232))]
	public Task<ResponceObject> GetBillQrData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerItemsAvailableQuantity_003Ed__233))]
	public Task<Value<ResponceObject>> GetCustomerItemsAvailableQuantity(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetPlanSubDetails_003Ed__234))]
	public Task<Value<ResponceObject>> GetPlanSubDetails(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveOtherVisitTasks_003Ed__235))]
	public Task<Value<ResponceObject>> SaveOtherVisitTasks(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSendByWhatsup_003Ed__236))]
	public Task<ResponceObject> SendByWhatsup(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetFieldPrivilege_003Ed__237))]
	public Task<Value<ResponceObject>> GetFieldPrivilege(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetGeneralInputData_003Ed__238))]
	public Task<Value<ResponceObject>> GetGeneralInputData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CUpdateUserPassword_003Ed__239))]
	public Task<Value<ResponceObject>> UpdateUserPassword(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CAddArchiveData_003Ed__240))]
	public Task<ResponceObject> AddArchiveData(Headers headers, RequstPostObject requstObject)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetFieldPrivilege1_003Ed__241))]
	public Task<Value<ResponceObject>> GetFieldPrivilege1(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBillForNote_003Ed__242))]
	public Task<Value<ResponceObject>> GetBillForNote(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSaveBillNoteRequest_003Ed__243))]
	public Task<Value<ResponceObject>> SaveBillNoteRequest(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetBillDataForPrint_003Ed__244))]
	public Task<ResponceObject> GetBillDataForPrint(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CSendVerficationMessage_003Ed__245))]
	public Task<ResponceObject> SendVerficationMessage(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetGlRequestData_003Ed__246))]
	public Task<ResponceObject> GetGlRequestData(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetReportAsPdfFromOnyx_003Ed__247))]
	public Task<ResponceObject> GetReportAsPdfFromOnyx(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerItemSold_003Ed__248))]
	public Task<ResponceObject> GetCustomerItemSold(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CEnrichWithLastStock_003Ed__249))]
	private Task AssetWatcher(string P_0, RequstPostObject P_1, List<CustomerItemSold> P_2, ResponceObject P_3)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	[AsyncStateMachine(typeof(_003CGetCustomerStock_003Ed__250))]
	public Task<Value<ResponceObject>> GetCustomerStock(RequstPostObject requstObject, Headers headers)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static Service()
	{
		IssuerWatcherWriter.CustomizeUtils();
		InvocationWatcher.SLV0fFIsptsZtjvFft17();
		globcheckSec = 1;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ExcludeService()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool IncludeService()
	{
		return true;
	}
}
