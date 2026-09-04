using System.Runtime.CompilerServices;
using Onyx.Containers;
using Onyx.Writers;

namespace Onyx.Distribution.Models.DTOs;

public class GeneralSql
{
	public static string SqlQutPrmMst;

	public static string SqlQutPrmDtl;

	public static string SqlQutPrmSubDtl;

	public static string SqlQutPrmGrpDtl;

	public static string SqlQutPrmGrpMst;

	public static string SqlGetAccountStatement;

	public static string SqlGetAccountStatementBalance;

	public static string SqlGetAccountStatementEndnigBalance;

	public static string SqlGetBillMasterData;

	public static string SqlGetReturnFromBill;

	public static string SqlGetReturnFromBillDetails;

	public static string SqlGetReturnFromBillOtherCharge;

	public static string SqlGetReturnFromBillTax;

	public static string SqlGetGroupDetails;

	public static string SqlGetInstallmentBills;

	public static string SqlGetCustomerClassData;

	public static string SqlGetItemSerialsData;

	public static string SqlGetQuestionnaireQuestions;

	public static string SqlGetAnswerQuestionnaireQuestions;

	public static string SqlGetItemsGroups;

	public static string SqlGetCreditCardTypes;

	public static string SqlGetAllTaxItems;

	public static string SqlGetCalcTaxType;

	public static string SqlGetDocsSyncMethode;

	public static string SqlGetCustomersTargetData;

	public static string SqlGetItemsBarcodeData;

	public static string SqlGetItemSerialNo;

	public static string SqlGetDynamicSreenFileds;

	public static string SqlGetDtsCstAgingV2;

	public static string SqlGetAccountStatementV2;

	public static string SqlGetDtsAccountStatmenDocDtl;

	public static string GetSalesOrderMst;

	public static string GetSalesOrderDtl;

	public static string GetReturnFromRtRqst;

	public static string GetReturnFromRtRqstDetails;

	public static string GetReturnFromRtRqsOthrChrg;

	public static string GetSalesOrderDtlOthrChrg;

	public static string GetTaxInputData;

	public static string GetWhtransSerialNo;

	public static string GetSalesSerialNo;

	public static string GetMobileRequest;

	public static string GetMobileRequest1;

	public static string GetDocMst;

	public static string GetDocDtls;

	public static string GetDocTaxs;

	public static string GetDocOtherCharges;

	public static string GetDocItemSerail;

	public static string GetItmMarktProperty;

	public static string GetMarktVisitFlag;

	public static string GetSmanDailayPlan;

	public static string GetCustomerLimitSales;

	public static string GetCustomerItemLimitSales;

	public static string GetBillSalesCharges;

	public static string GetSFlagCodeOld;

	public static string GetSFlagCode;

	public static string GetExtraScreenLabel;

	public static string GetExtraScreenLabelNew;

	public static string InsertDvcSerail;

	public static string GetCustomerCostCenter;

	public static string GetCashCustomer;

	public static string GetSalesManDocumentMovement;

	public static string GetSalesManDocumentMovement2;

	public static string GetSalesManItemMovement;

	public static string GetMandatoryField;

	public static string GetAvlQtyOnline;

	public static string GetKey;

	public static string GetSalesInfo;

	public static string GetSalesManBranchPrivilege;

	public static string GetAccountConfirmBalances;

	public static string SaveConfirmCustomerBalance;

	public static string SaveMassage;

	public static string UpdateReadMessage;

	public static string GetCustomerPlanTarget;

	public static string GetCustomerPlanTarget_New;

	public static string GetUsers;

	public static string GetAccountStatementConfirm;

	public static string SaveCustomerAccountStatementConfirm;

	public static string SaveDynamicFieldDocument;

	public static string GetTargetPrometerData;

	public static string GetCustomerActvty;

	public static string GetCustomerCostCenters;

	public static string GetCustomerProject;

	public static string GetRepCodeListForAdminRep;

	public static string GetFreeSampleMovement;

	public static string PrivilegaFixedColumn;

	public static string GetCustomerItemsAvailableQuantity;

	public static string GetMessageDetails;

	public static string GetPlanSubDetails;

	public static string GetFieldPrivilege;

	public static string GetGeneralInputData;

	public static string UpdateUserPassword;

	public static string GetBillForNoteMst;

	public static string GetBillForNoteDtl;

	public static string GetCollectPlan;

	public static string GetDtsCstindebtedness;

	public static string GetCustomerStockMst;

	public static string GetCustomerStockDtl;

	public static string GetCreditCard;

	public static string GetAccountStatementDocTypeSum;

	public static string GetAccountStatementDetailOpenBal;

	public static string SendVerficationMessage;

	public static string GetCustomerItemSold;

	[MethodImpl(MethodImplOptions.NoInlining)]
	public static string GetSqlByOnyxDocType(int doc_type)
	{
		return null;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	public GeneralSql()
	{
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	static GeneralSql()
	{
		ThreadIndexerContainer.IncludeClass();
		int num = 50;
		while (true)
		{
			int num2 = num;
			while (true)
			{
				int num3;
				switch (num2)
				{
				case 27:
					GetDocMst = ThreadIndexerContainer.FindClass(149438);
					num3 = 70;
					goto IL_06d4;
				case 61:
					SqlQutPrmSubDtl = ThreadIndexerContainer.FindClass(31316);
					num = 84;
					if (!RunIdentifier())
					{
						break;
					}
					goto case 59;
				case 59:
					SqlGetInstallmentBills = ThreadIndexerContainer.FindClass(77544);
					num3 = 51;
					goto IL_06d4;
				case 91:
					GetSFlagCode = ThreadIndexerContainer.FindClass(161864);
					num2 = 72;
					continue;
				case 49:
					SqlGetAccountStatementV2 = ThreadIndexerContainer.FindClass(121356);
					num2 = 104;
					continue;
				case 24:
					UpdateReadMessage = ThreadIndexerContainer.FindClass(180848);
					num = 42;
					if (ReadIdentifier())
					{
						break;
					}
					goto case 9;
				case 9:
					SqlQutPrmGrpMst = ThreadIndexerContainer.FindClass(35092);
					num3 = 100;
					goto IL_06d4;
				case 30:
					GetAvlQtyOnline = ThreadIndexerContainer.FindClass(170456);
					num3 = 93;
					goto IL_06d4;
				case 36:
					GetCustomerItemSold = ThreadIndexerContainer.FindClass(267972);
					num3 = 106;
					goto IL_06d4;
				case 82:
					GetSalesManItemMovement = ThreadIndexerContainer.FindClass(169376);
					num = 15;
					if (true)
					{
						break;
					}
					goto case 44;
				case 44:
					SqlGetAllTaxItems = ThreadIndexerContainer.FindClass(105766);
					num = 43;
					if (!RunIdentifier())
					{
						break;
					}
					goto case 100;
				case 74:
					GetCashCustomer = ThreadIndexerContainer.FindClass(163984);
					num3 = 45;
					goto IL_06d4;
				case 79:
					SqlGetAnswerQuestionnaireQuestions = ThreadIndexerContainer.FindClass(85998);
					num = 18;
					break;
				case 77:
					GetReturnFromRtRqst = ThreadIndexerContainer.FindClass(137796);
					num3 = 31;
					goto IL_06d4;
				case 92:
					GetFieldPrivilege = ThreadIndexerContainer.FindClass(229212);
					num2 = 34;
					continue;
				case 3:
					GetCustomerStockDtl = ThreadIndexerContainer.FindClass(255340);
					num3 = 86;
					goto IL_06d4;
				case 86:
					GetCreditCard = ThreadIndexerContainer.FindClass(256280);
					num = 73;
					break;
				case 31:
					GetReturnFromRtRqstDetails = ThreadIndexerContainer.FindClass(142046);
					goto case 37;
				case 37:
				case 40:
					GetReturnFromRtRqsOthrChrg = ThreadIndexerContainer.FindClass(143468);
					num = 96;
					if (true)
					{
						break;
					}
					goto case 93;
				case 93:
					GetKey = ThreadIndexerContainer.FindClass(173008);
					num = 80;
					break;
				case 8:
					GetCustomerProject = ThreadIndexerContainer.FindClass(196000);
					num = 38;
					if (true)
					{
						break;
					}
					goto case 80;
				case 80:
					GetSalesInfo = ThreadIndexerContainer.FindClass(173242);
					num3 = 10;
					goto IL_06d4;
				case 10:
					GetSalesManBranchPrivilege = ThreadIndexerContainer.FindClass(175166);
					num2 = 33;
					continue;
				case 88:
					GetDocTaxs = ThreadIndexerContainer.FindClass(154826);
					num = 78;
					break;
				case 2:
					SqlGetAccountStatementEndnigBalance = ThreadIndexerContainer.FindClass(40852);
					num2 = 52;
					continue;
				case 0:
					SendVerficationMessage = ThreadIndexerContainer.FindClass(264580);
					num3 = 36;
					goto IL_06d4;
				case 78:
					GetDocOtherCharges = ThreadIndexerContainer.FindClass(155948);
					num = 102;
					break;
				case 57:
					GetMessageDetails = ThreadIndexerContainer.FindClass(226574);
					num = 21;
					break;
				case 46:
					SqlGetDtsCstAgingV2 = ThreadIndexerContainer.FindClass(118870);
					num3 = 49;
					goto IL_06d4;
				case 72:
					GetExtraScreenLabel = ThreadIndexerContainer.FindClass(162714);
					num3 = 35;
					goto IL_06d4;
				case 48:
					SqlGetReturnFromBillOtherCharge = ThreadIndexerContainer.FindClass(69216);
					num = 64;
					break;
				case 1:
					SaveConfirmCustomerBalance = ThreadIndexerContainer.FindClass(177352);
					num = 23;
					break;
				case 100:
					SqlGetAccountStatement = ThreadIndexerContainer.FindClass(36238);
					num = 29;
					break;
				case 16:
					GetTargetPrometerData = ThreadIndexerContainer.FindClass(192648);
					num2 = 81;
					continue;
				case 83:
					GetUsers = ThreadIndexerContainer.FindClass(186382);
					num = 19;
					break;
				case 58:
					SqlGetCreditCardTypes = ThreadIndexerContainer.FindClass(103006);
					num = 44;
					if (0 == 0)
					{
						break;
					}
					goto case 104;
				case 104:
					SqlGetDtsAccountStatmenDocDtl = ThreadIndexerContainer.FindClass(130734);
					num = 103;
					break;
				case 41:
					GetCustomerCostCenter = ThreadIndexerContainer.FindClass(163728);
					num2 = 74;
					continue;
				case 54:
					GetSalesOrderDtl = ThreadIndexerContainer.FindClass(136364);
					num2 = 77;
					continue;
				case 33:
					GetAccountConfirmBalances = ThreadIndexerContainer.FindClass(175350);
					num3 = 1;
					goto IL_06d4;
				case 35:
					GetExtraScreenLabelNew = ThreadIndexerContainer.FindClass(162972);
					num = 60;
					if (0 == 0)
					{
						break;
					}
					goto case 103;
				case 103:
					GetSalesOrderMst = ThreadIndexerContainer.FindClass(132110);
					num3 = 54;
					goto IL_06d4;
				case 62:
					GetBillForNoteDtl = ThreadIndexerContainer.FindClass(238374);
					num = 90;
					if (true)
					{
						break;
					}
					goto case 6;
				case 6:
					GetCustomerItemsAvailableQuantity = ThreadIndexerContainer.FindClass(224964);
					num2 = 57;
					continue;
				case 68:
					return;
				case 26:
					GetMobileRequest = ThreadIndexerContainer.FindClass(147940);
					num2 = 101;
					continue;
				case 102:
					GetDocItemSerail = ThreadIndexerContainer.FindClass(157044);
					num = 63;
					if (0 == 0)
					{
						break;
					}
					goto case 69;
				case 69:
					GetMarktVisitFlag = ThreadIndexerContainer.FindClass(159688);
					num = 67;
					if (ReadIdentifier())
					{
						break;
					}
					goto case 53;
				case 53:
					SqlGetCustomersTargetData = ThreadIndexerContainer.FindClass(108890);
					num = 14;
					if (true)
					{
						break;
					}
					goto case 39;
				case 39:
					GetCustomerCostCenters = ThreadIndexerContainer.FindClass(194606);
					num = 8;
					if (true)
					{
						break;
					}
					goto case 73;
				case 73:
					GetAccountStatementDocTypeSum = ThreadIndexerContainer.FindClass(258278);
					num = 55;
					if (true)
					{
						break;
					}
					goto case 11;
				case 11:
					GetBillSalesCharges = ThreadIndexerContainer.FindClass(160794);
					num3 = 99;
					goto IL_06d4;
				case 97:
					GetDtsCstindebtedness = ThreadIndexerContainer.FindClass(242170);
					num3 = 13;
					goto IL_06d4;
				case 89:
					GetWhtransSerialNo = ThreadIndexerContainer.FindClass(146032);
					num3 = 17;
					goto IL_06d4;
				case 94:
					SqlQutPrmDtl = ThreadIndexerContainer.FindClass(21810);
					num2 = 61;
					continue;
				case 67:
					GetSmanDailayPlan = ThreadIndexerContainer.FindClass(159944);
					num3 = 28;
					goto IL_06d4;
				case 66:
					SqlGetGroupDetails = ThreadIndexerContainer.FindClass(76956);
					num2 = 59;
					continue;
				case 50:
					if (!ThreadIndexerContainer.DestroyClass(32))
					{
						ProducerCustomerWriter.SLV0fFIsptsZtjvFft17();
						num3 = 65;
						goto IL_06d4;
					}
					num = 68;
					if (0 == 0)
					{
						break;
					}
					goto case 4;
				case 4:
					GetCustomerPlanTarget_New = ThreadIndexerContainer.FindClass(183278);
					num3 = 83;
					goto IL_06d4;
				case 7:
					SqlGetReturnFromBill = ThreadIndexerContainer.FindClass(43386);
					num2 = 85;
					continue;
				case 42:
					GetCustomerPlanTarget = ThreadIndexerContainer.FindClass(180974);
					num2 = 4;
					continue;
				case 63:
					GetItmMarktProperty = ThreadIndexerContainer.FindClass(158920);
					num = 69;
					if (ReadIdentifier())
					{
						break;
					}
					goto case 28;
				case 28:
					GetCustomerLimitSales = ThreadIndexerContainer.FindClass(160210);
					goto case 47;
				default:
					num3 = 47;
					goto IL_06d4;
				case 51:
					SqlGetCustomerClassData = ThreadIndexerContainer.FindClass(80472);
					num3 = 105;
					goto IL_06d4;
				case 70:
					GetDocDtls = ThreadIndexerContainer.FindClass(153502);
					num = 88;
					break;
				case 55:
					GetAccountStatementDetailOpenBal = ThreadIndexerContainer.FindClass(262942);
					num3 = 0;
					goto IL_06d4;
				case 43:
					SqlGetCalcTaxType = ThreadIndexerContainer.FindClass(107354);
					ReadIdentifier();
					if (RunIdentifier())
					{
						num = 40;
						break;
					}
					num = 76;
					if (0 == 0)
					{
						break;
					}
					goto case 38;
				case 38:
					GetRepCodeListForAdminRep = ThreadIndexerContainer.FindClass(197222);
					num2 = 98;
					continue;
				case 81:
					GetCustomerActvty = ThreadIndexerContainer.FindClass(193392);
					num = 39;
					break;
				case 23:
					SaveMassage = ThreadIndexerContainer.FindClass(179314);
					num2 = 24;
					continue;
				case 34:
					GetGeneralInputData = ThreadIndexerContainer.FindClass(233170);
					num = 56;
					break;
				case 20:
					GetBillForNoteMst = ThreadIndexerContainer.FindClass(235392);
					num = 62;
					if (0 == 0)
					{
						break;
					}
					goto case 15;
				case 15:
					GetMandatoryField = ThreadIndexerContainer.FindClass(170382);
					num2 = 30;
					continue;
				case 32:
					GetSalesManDocumentMovement2 = ThreadIndexerContainer.FindClass(167232);
					num = 82;
					if (true)
					{
						break;
					}
					goto case 29;
				case 29:
					SqlGetAccountStatementBalance = ThreadIndexerContainer.FindClass(39216);
					num = 2;
					if (true)
					{
						break;
					}
					goto case 75;
				case 75:
					PrivilegaFixedColumn = ThreadIndexerContainer.FindClass(199942);
					num = 6;
					if (ReadIdentifier())
					{
						break;
					}
					goto case 24;
				case 85:
					SqlGetReturnFromBillDetails = ThreadIndexerContainer.FindClass(54662);
					num = 48;
					if (ReadIdentifier())
					{
						break;
					}
					goto case 1;
				case 95:
					SaveCustomerAccountStatementConfirm = ThreadIndexerContainer.FindClass(189088);
					num = 87;
					if (!RunIdentifier())
					{
						break;
					}
					goto case 96;
				case 96:
					GetSalesOrderDtlOthrChrg = ThreadIndexerContainer.FindClass(144588);
					num2 = 5;
					continue;
				case 5:
					GetTaxInputData = ThreadIndexerContainer.FindClass(145744);
					num2 = 89;
					continue;
				case 71:
					SqlGetItemSerialNo = ThreadIndexerContainer.FindClass(116576);
					num = 22;
					break;
				case 25:
				case 76:
					SqlGetDocsSyncMethode = ThreadIndexerContainer.FindClass(108514);
					num = 53;
					break;
				case 13:
					GetCustomerStockMst = ThreadIndexerContainer.FindClass(252838);
					num = 3;
					if (ReadIdentifier())
					{
						break;
					}
					goto case 21;
				case 21:
					GetPlanSubDetails = ThreadIndexerContainer.FindClass(228032);
					num = 92;
					if (0 == 0)
					{
						break;
					}
					goto case 60;
				case 60:
					InsertDvcSerail = ThreadIndexerContainer.FindClass(163234);
					num2 = 41;
					continue;
				case 101:
					GetMobileRequest1 = ThreadIndexerContainer.FindClass(149354);
					num = 27;
					if (0 == 0)
					{
						break;
					}
					goto case 14;
				case 14:
					SqlGetItemsBarcodeData = ThreadIndexerContainer.FindClass(114316);
					num = 71;
					if (ReadIdentifier())
					{
						break;
					}
					goto case 31;
				case 90:
					GetCollectPlan = ThreadIndexerContainer.FindClass(240244);
					num = 97;
					break;
				case 64:
					SqlGetReturnFromBillTax = ThreadIndexerContainer.FindClass(71376);
					num3 = 66;
					goto IL_06d4;
				case 12:
					SqlGetQuestionnaireQuestions = ThreadIndexerContainer.FindClass(84260);
					num3 = 79;
					goto IL_06d4;
				case 65:
					SqlQutPrmMst = ThreadIndexerContainer.FindClass(15536);
					num2 = 94;
					continue;
				case 17:
					GetSalesSerialNo = ThreadIndexerContainer.FindClass(146804);
					num3 = 26;
					goto IL_06d4;
				case 19:
					GetAccountStatementConfirm = ThreadIndexerContainer.FindClass(186634);
					num2 = 95;
					continue;
				case 105:
					SqlGetItemSerialsData = ThreadIndexerContainer.FindClass(82274);
					num = 12;
					break;
				case 18:
					SqlGetItemsGroups = ThreadIndexerContainer.FindClass(87420);
					num2 = 58;
					continue;
				case 84:
					SqlQutPrmGrpDtl = ThreadIndexerContainer.FindClass(33526);
					num2 = 9;
					continue;
				case 47:
					GetCustomerItemLimitSales = ThreadIndexerContainer.FindClass(160482);
					num = 11;
					break;
				case 22:
					SqlGetDynamicSreenFileds = ThreadIndexerContainer.FindClass(118222);
					num3 = 46;
					goto IL_06d4;
				case 52:
					SqlGetBillMasterData = ThreadIndexerContainer.FindClass(42494);
					num3 = 7;
					goto IL_06d4;
				case 98:
					GetFreeSampleMovement = ThreadIndexerContainer.FindClass(198076);
					num2 = 75;
					continue;
				case 99:
					GetSFlagCodeOld = ThreadIndexerContainer.FindClass(161550);
					num = 91;
					if (true)
					{
						break;
					}
					goto case 87;
				case 87:
					SaveDynamicFieldDocument = ThreadIndexerContainer.FindClass(190640);
					num = 16;
					break;
				case 56:
					UpdateUserPassword = ThreadIndexerContainer.FindClass(233428);
					num = 20;
					break;
				case 45:
					GetSalesManDocumentMovement = ThreadIndexerContainer.FindClass(164466);
					num = 32;
					if (!ReadIdentifier())
					{
						return;
					}
					break;
				case 106:
					return;
					IL_06d4:
					num = num3;
					break;
				}
				break;
			}
		}
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool ReadIdentifier()
	{
		return true;
	}

	[MethodImpl(MethodImplOptions.NoInlining)]
	internal static bool RunIdentifier()
	{
		return true;
	}
}
