using System.Collections.Generic;
using System.Runtime.CompilerServices;
using Onyx.Containers;
using Onyx.Writers;

namespace Onyx.Distribution.Models.DTOs;

public class Constatnts
{
	public static List<string> NET_SALES_REP_HEADER;

	public static List<string> NET_SALES_CUST_TARGT;

	public static List<string> NET_SALES_CUST_TARGT_ORGNAL;

	public static List<string> SalesManItemMovement;

	public static List<string> SalesManDocMovementOperations;

	public static List<string> SalesManDocMovementVisits;

	[MethodImpl(MethodImplOptions.NoInlining)]
	public Constatnts()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static Constatnts()
	{
		ThreadIndexerContainer.IncludeClass();
		int num = 4;
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
					case 4:
						if (ThreadIndexerContainer.DestroyClass(28))
						{
							num2 = 0;
							if (!CountAuthentication())
							{
								goto end_IL_016d;
							}
							goto case 6;
						}
						return;
					case 6:
						NET_SALES_CUST_TARGT_ORGNAL = new List<string>
						{
							ThreadIndexerContainer.FindClass(8336),
							ThreadIndexerContainer.FindClass(8352),
							ThreadIndexerContainer.FindClass(8368),
							ThreadIndexerContainer.FindClass(8388),
							ThreadIndexerContainer.FindClass(8406),
							ThreadIndexerContainer.FindClass(8428),
							ThreadIndexerContainer.FindClass(8460),
							ThreadIndexerContainer.FindClass(8492),
							ThreadIndexerContainer.FindClass(8534),
							ThreadIndexerContainer.FindClass(8564),
							ThreadIndexerContainer.FindClass(8580),
							ThreadIndexerContainer.FindClass(8592),
							ThreadIndexerContainer.FindClass(8608),
							ThreadIndexerContainer.FindClass(8624),
							ThreadIndexerContainer.FindClass(8640),
							ThreadIndexerContainer.FindClass(8658),
							ThreadIndexerContainer.FindClass(8670),
							ThreadIndexerContainer.FindClass(8686)
						};
						goto case 1;
					default:
						num2 = 1;
						goto end_IL_016d;
					case 8:
						break;
					case 2:
						SalesManDocMovementOperations = new List<string>
						{
							ThreadIndexerContainer.FindClass(9022),
							ThreadIndexerContainer.FindClass(9298),
							ThreadIndexerContainer.FindClass(9172),
							ThreadIndexerContainer.FindClass(8970),
							ThreadIndexerContainer.FindClass(8954),
							ThreadIndexerContainer.FindClass(9072),
							ThreadIndexerContainer.FindClass(9090),
							ThreadIndexerContainer.FindClass(8914),
							ThreadIndexerContainer.FindClass(8934),
							ThreadIndexerContainer.FindClass(8874),
							ThreadIndexerContainer.FindClass(8894),
							ThreadIndexerContainer.FindClass(8336),
							ThreadIndexerContainer.FindClass(9324),
							ThreadIndexerContainer.FindClass(8352),
							ThreadIndexerContainer.FindClass(9340),
							ThreadIndexerContainer.FindClass(9372),
							ThreadIndexerContainer.FindClass(9402),
							ThreadIndexerContainer.FindClass(9418),
							ThreadIndexerContainer.FindClass(9436),
							ThreadIndexerContainer.FindClass(9454),
							ThreadIndexerContainer.FindClass(9470),
							ThreadIndexerContainer.FindClass(9006),
							ThreadIndexerContainer.FindClass(9486),
							ThreadIndexerContainer.FindClass(9144),
							ThreadIndexerContainer.FindClass(9154),
							ThreadIndexerContainer.FindClass(9506),
							ThreadIndexerContainer.FindClass(9524),
							ThreadIndexerContainer.FindClass(9548),
							ThreadIndexerContainer.FindClass(9568),
							ThreadIndexerContainer.FindClass(9594),
							ThreadIndexerContainer.FindClass(8812),
							ThreadIndexerContainer.FindClass(8842),
							ThreadIndexerContainer.FindClass(9610),
							ThreadIndexerContainer.FindClass(8824),
							ThreadIndexerContainer.FindClass(8864),
							ThreadIndexerContainer.FindClass(8696),
							ThreadIndexerContainer.FindClass(9630),
							ThreadIndexerContainer.FindClass(8792),
							ThreadIndexerContainer.FindClass(8712),
							ThreadIndexerContainer.FindClass(8732),
							ThreadIndexerContainer.FindClass(8752),
							ThreadIndexerContainer.FindClass(9648),
							ThreadIndexerContainer.FindClass(8768)
						};
						goto case 7;
					case 1:
						SalesManItemMovement = new List<string>
						{
							ThreadIndexerContainer.FindClass(8696),
							ThreadIndexerContainer.FindClass(8712),
							ThreadIndexerContainer.FindClass(8732),
							ThreadIndexerContainer.FindClass(8752),
							ThreadIndexerContainer.FindClass(8768),
							ThreadIndexerContainer.FindClass(8792),
							ThreadIndexerContainer.FindClass(8336),
							ThreadIndexerContainer.FindClass(8352),
							ThreadIndexerContainer.FindClass(8624),
							ThreadIndexerContainer.FindClass(8564),
							ThreadIndexerContainer.FindClass(8812),
							ThreadIndexerContainer.FindClass(8824),
							ThreadIndexerContainer.FindClass(8842),
							ThreadIndexerContainer.FindClass(8864),
							ThreadIndexerContainer.FindClass(8874),
							ThreadIndexerContainer.FindClass(8894),
							ThreadIndexerContainer.FindClass(8914),
							ThreadIndexerContainer.FindClass(8934),
							ThreadIndexerContainer.FindClass(8954),
							ThreadIndexerContainer.FindClass(8970),
							ThreadIndexerContainer.FindClass(8640),
							ThreadIndexerContainer.FindClass(9006),
							ThreadIndexerContainer.FindClass(9022),
							ThreadIndexerContainer.FindClass(9042),
							ThreadIndexerContainer.FindClass(9072),
							ThreadIndexerContainer.FindClass(9090),
							ThreadIndexerContainer.FindClass(9110),
							ThreadIndexerContainer.FindClass(9124),
							ThreadIndexerContainer.FindClass(9144),
							ThreadIndexerContainer.FindClass(9154),
							ThreadIndexerContainer.FindClass(9172),
							ThreadIndexerContainer.FindClass(9202),
							ThreadIndexerContainer.FindClass(9218),
							ThreadIndexerContainer.FindClass(9236),
							ThreadIndexerContainer.FindClass(9252),
							ThreadIndexerContainer.FindClass(9278)
						};
						num = 2;
						goto end_IL_0169;
					case 0:
						ProducerCustomerWriter.SLV0fFIsptsZtjvFft17();
						num2 = 8;
						goto end_IL_016d;
					case 7:
					case 9:
						SalesManDocMovementVisits = new List<string>
						{
							ThreadIndexerContainer.FindClass(8696),
							ThreadIndexerContainer.FindClass(9630),
							ThreadIndexerContainer.FindClass(8792),
							ThreadIndexerContainer.FindClass(8712),
							ThreadIndexerContainer.FindClass(8732),
							ThreadIndexerContainer.FindClass(8752),
							ThreadIndexerContainer.FindClass(9648),
							ThreadIndexerContainer.FindClass(8768)
						};
						num = 10;
						goto end_IL_0169;
					case 3:
					case 5:
						NET_SALES_CUST_TARGT = new List<string>
						{
							ThreadIndexerContainer.FindClass(7988),
							ThreadIndexerContainer.FindClass(8012),
							ThreadIndexerContainer.FindClass(8028),
							ThreadIndexerContainer.FindClass(8054),
							ThreadIndexerContainer.FindClass(8078),
							ThreadIndexerContainer.FindClass(8100),
							ThreadIndexerContainer.FindClass(8124),
							ThreadIndexerContainer.FindClass(8148),
							ThreadIndexerContainer.FindClass(8174),
							ThreadIndexerContainer.FindClass(8198),
							ThreadIndexerContainer.FindClass(8212),
							ThreadIndexerContainer.FindClass(8226),
							ThreadIndexerContainer.FindClass(8246),
							ThreadIndexerContainer.FindClass(8268),
							ThreadIndexerContainer.FindClass(7888),
							ThreadIndexerContainer.FindClass(8290),
							ThreadIndexerContainer.FindClass(8304),
							ThreadIndexerContainer.FindClass(8320)
						};
						num2 = 6;
						if (false)
						{
							return;
						}
						goto end_IL_016d;
					case 10:
						return;
					}
					NET_SALES_REP_HEADER = new List<string>
					{
						ThreadIndexerContainer.FindClass(7742),
						ThreadIndexerContainer.FindClass(7760),
						ThreadIndexerContainer.FindClass(7776),
						ThreadIndexerContainer.FindClass(7792),
						ThreadIndexerContainer.FindClass(7816),
						ThreadIndexerContainer.FindClass(7838),
						ThreadIndexerContainer.FindClass(7856),
						ThreadIndexerContainer.FindClass(7872),
						ThreadIndexerContainer.FindClass(7888),
						ThreadIndexerContainer.FindClass(7904),
						ThreadIndexerContainer.FindClass(7930),
						ThreadIndexerContainer.FindClass(7958)
					};
					_ = 1;
					num3 = (CountAuthentication() ? 9 : 5);
					continue;
					end_IL_016d:
					break;
				}
				continue;
				end_IL_0169:
				break;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ComputeAuthentication()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool CountAuthentication()
	{
		return true;
	}
}
