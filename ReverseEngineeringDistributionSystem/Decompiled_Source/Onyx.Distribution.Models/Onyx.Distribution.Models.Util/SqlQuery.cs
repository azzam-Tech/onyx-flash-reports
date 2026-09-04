using System.Runtime.CompilerServices;
using Onyx.Containers;
using Onyx.Writers;

namespace Onyx.Distribution.Models.Util;

public static class SqlQuery
{
	public static string Q1;

	public static string Q2;

	public static string Q3_USER;

	public static string Q3_EMP;

	public static string Q3_CUSTOMER;

	public static string Q4;

	public static string Q5;

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string RplsQrey(string sql, int Sys_No, int Mod_Id, string mob_dev_srl, int user_typ, string user_id, int year, int activity)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static SqlQuery()
	{
		ThreadIndexerContainer.IncludeClass();
		int num = 9;
		while (true)
		{
			int num2 = num;
			while (true)
			{
				int num3 = num2;
				while (true)
				{
					switch (num3)
					{
					case 2:
						goto end_IL_00e1;
					case 8:
						Q3_USER = ThreadIndexerContainer.FindClass(4256);
						goto case 3;
					case 9:
						while (true)
						{
							ProducerCustomerWriter.SLV0fFIsptsZtjvFft17();
							TestObserver();
							if (NewObserver())
							{
								break;
							}
							num2 = 3;
							if (true)
							{
								goto end_IL_00e5;
							}
						}
						num2 = 6;
						if (true)
						{
							break;
						}
						goto case 5;
					case 5:
						Q4 = ThreadIndexerContainer.FindClass(6406);
						num2 = 7;
						break;
					case 0:
						Q3_CUSTOMER = ThreadIndexerContainer.FindClass(5680);
						num2 = 5;
						if (true)
						{
							break;
						}
						goto case 7;
					case 7:
						Q5 = ThreadIndexerContainer.FindClass(6766);
						num3 = 10;
						continue;
					case 3:
					case 4:
						Q3_EMP = ThreadIndexerContainer.FindClass(4960);
						goto case 0;
					default:
						num2 = 0;
						if (TestObserver())
						{
							goto end_IL_00e1;
						}
						break;
					case 1:
					case 6:
						Q1 = ThreadIndexerContainer.FindClass(3270);
						num3 = 2;
						continue;
					case 10:
						return;
						end_IL_00e5:
						break;
					}
					break;
				}
				continue;
				end_IL_00e1:
				break;
			}
			Q2 = ThreadIndexerContainer.FindClass(3512);
			num = 8;
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool NewObserver()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool TestObserver()
	{
		return true;
	}
}
