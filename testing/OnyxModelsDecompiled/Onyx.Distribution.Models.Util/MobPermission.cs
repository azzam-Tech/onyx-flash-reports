using System.Runtime.CompilerServices;
using Onyx.Containers;
using Onyx.Distribution.Models.MainDTOs;
using Oracle.ManagedDataAccess.Client;

namespace Onyx.Distribution.Models.Util;

public static class MobPermission
{
	[CompilerGenerated]
	private sealed class WorkerRepository
	{
		public int t;

		[MethodImpl(MethodImplOptions.NoInlining)]
		public WorkerRepository()
		{
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool FillClass(int x)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool ForgotClass(int x)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal bool GetClass(int x)
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool AwakeExpression()
		{
			return true;
		}

		[MethodImpl(MethodImplOptions.NoInlining)]
		internal static bool GetExpression()
		{
			return true;
		}

		static WorkerRepository()
		{
			ThreadIndexerContainer.IncludeClass();
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static GeneralResult TestCheckLogin(int year, int activty, int sysno, int mod_id, int userno, string mob_srl, OracleConnection dbControl, int userType, int secType = 0)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string CheckMobDevPermission(OracleConnection OracleCon, int Sys_No, int Mod_Id, string mob_dev_srl, int user_typ, string user_id, int year, int activity, int secType)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static int InsertMobDevRegRequst(OracleConnection OracleCon, int Sys_No, int Mod_Id, string mob_dev_srl, int user_typ, string user_id, int year, int activity, string P_MOBILE_OS, int langNo, int secType)
	{
		return 0;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	private static GeneralResult SearchClass(int P_0, object P_1, int P_2, int P_3, int P_4, int P_5, object P_6, int P_7, int P_8)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static GeneralResult checkLiceinse(short systemNo)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RunObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RegisterObserver()
	{
		return true;
	}

	static MobPermission()
	{
		ThreadIndexerContainer.IncludeClass();
	}
}
