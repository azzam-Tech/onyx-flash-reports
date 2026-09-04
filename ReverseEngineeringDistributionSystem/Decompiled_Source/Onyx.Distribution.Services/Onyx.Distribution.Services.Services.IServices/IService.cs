using System.IO;
using System.Threading.Tasks;
using Onyx.Distribution.Models.MainDTOs;

namespace Onyx.Distribution.Services.Services.IServices;

public interface IService
{
	Task<GetCashDetailsOBjctResult> GetCashDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers);

	Task<GetBanksDetailsOBjctResult> GetBanksDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers);

	Task<GetCustomersOBjctResult> GetCustomers(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers);

	Task<GetUsersOBjctResult> GetUsersWithTax(int YearNo, int ActvieNo, int Branch_No, string Pda_Name, int op_type, int VerNo, Headers headers, string Token = "", string Device_Type = "1");

	Task<GetBanksCurrenciesDetailsOBjctResult> GetBanksCurrenciesDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers);

	Task<GetCurrncyOBjctResult> GetCurrncy(Headers headers, int YearNo, int ActvieNo, int Branch_No, int type_no, string REP_CODE, int VerNo, string C_Code = "");

	Task<GetCashCurrenciesDetailsOBjctResult> GetCashCurrenciesDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers);

	Task<GetItemsDetailsOBjctResult> GetItemsDetailsPaging(int YearNo, int ActvieNo, int Branch_No, int GRP_CODE, string REP_CODE, int S_row, int L_row, int VerNo, Headers headers);

	Task<GetMeasurmentsOBjctResult> GetMeasurments(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers);

	Task<GetPlanDetailsOBjctResult> GetPlanDetails(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, string PLAN_DATE, int VerNo, Headers headers, string DOC_SER, string LANG_NO);

	Task<GetStorageOBjctResult> GetStorage_Br(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int VerNo, Headers headers);

	Task<GetStorageOBjctResult> GetStorage_Br_Paging(int YearNo, int ActvieNo, int Branch_No, string REP_CODE, int S_row, int L_row, int VerNo, Headers headers);

	Task<GetParametersObjctResult> GetParameters(int YearNo, int ActvieNo, string Rep_Code, int VerNo, Headers headers, int BrnNo);

	Task<GetDocTypesOBjctResult> GetDocTypes(int YearNo, int ActvieNo, int Branch_No, int User_Id, int VerNo, Headers headers);

	Task<GetBrachesDataOBjctResult> GetBranchesData(int YearNo, int ActvieNo, int Branch_No, int User_Id, int VerNo, Headers headers);

	Task<GetWareHouseOBjctResult> GetWareHouse(int YearNo, int ActvieNo, int User_No, int VerNo, Headers headers);

	Task<GetItemsBarcodeOBjctResult> GetItemsBarcode(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers);

	Task<GetItemsStorageOBjctResult> GetItemsStorage(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers);

	Task<GetInventroyTypesOBjctResult> GetInventroyTypes(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers);

	Task<GetItemsPriceOBjctResult> GetItemsPrices(int YearNo, int ActvieNo, int Branch_No, int Lvl_No, int VerNo, Headers headers);

	Task<GetInvSerialParameterObjctResult> GetInvSerialParameter(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers);

	Task<GetLevelPriceOBjctResult> GetLevelPrices(int YearNo, int ActvieNo, int Branch_No, int VerNo, Headers headers);

	Task<DocDescriptionObjctResult> DocDescription(int YearNo, int ActvieNo, int VerNo, Headers headers);

	Task<GetSysDateResult> GetSysDateNew(int YearNo, int ActvieNo, int VerNo, Headers headers);

	Task<GeneralResult> ClosedPlan(int YearNo, int ActvieNo, string REP_CODE, string DOC_SER, int VerNo, Headers headers);

	Task<GeneralResult> UpdateSyncStatues(int YearNo, int ActvieNo, string REP_CODE, int SYNC_TYP, int VerNo, Headers headers);

	Task<GetSales_discountOBjctResult> GetSales_discount(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers);

	Task<GetSalesFreeQtyOBjctResult> GetSalesFreeQty(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers);

	Task<GetTrans_SeqResult> GetTrans_Seq(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers);

	Task<CustCreditPreiodResult> GetCustCreditPreiod(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers, string C_CODE);

	Task<GeoLocationResult> GeoLocations(Headers headers, int YearNo, int ActvieNo, int VerNo, int S_Row = 0, int E_Row = 0);

	GeneralResult TestWs();

	Task<GeneralResult> TestDb();

	Task<GetVistFailReasonsOBjctResult> GetVistFailReasons(int YearNo, int ActvieNo, int VerNo, Headers headers);

	Task<GetBrnchUserPrivResult> GetBrnchUserPriv(int YearNo, int ActvieNo, string User_No, int VerNo, Headers headers);

	Task<GetPriceLevelsResult> GetPriceLevels(int YearNo, int ActvieNo, string REP_CODE, int VerNo, Headers headers);

	Task<GetItemsPriceLevelsResult> GetItemsPriceLevelsPaging(int YearNo, int ActvieNo, string REP_CODE, int S_row, int L_row, int VerNo, Headers headers);

	Task<GetItemCountResult> GetItemCount(int YearNo, int ActvieNo, string REP_CODE, int Type_No, int VerNo, int W_Code, Headers headers);

	Task<GetFormsPrivilegeResult> GetFormsPrivilege(int YearNo, int ActvieNo, int User_Id, int VerNo, Headers headers);

	Task<GetDocBillsDataResult> GetDocBillsData(int YearNo, int ActvieNo, string REP_CODE, int BILL_DOC_TYPE, string BILL_NO, int VerNo, Headers headers);

	Task<GetSales_ChargesResult> GetSalesCharges(int YearNo, int ActvieNo, int VerNo, Headers headers);

	Task<GetGnrTaxCodeResult> GetGnrTaxCode(int YearNo, int ActvieNo, int VerNo, Headers headers);

	Task<GetGnrTaxItemsResult> GetGnrTaxItems(int YearNo, int ActvieNo, string Rep_Code, int S_row, int L_row, int VerNo, Headers headers);

	Task<Value<ResponceObject>> GetCshBlncWithLmt(int YearNo, int ActvieNo, string REP_CODE, string Date, int VerNo, Headers headers);

	Task<Value<ResponceObject>> GetQutPrmMstData(RequstObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetQutPrmDtlData_OLD(RequstObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetQutPrmSubDtlData(RequstObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetQutPrmGrpDtlData(RequstObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetQutPrmGrpMstData(RequstObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetWHTransferMstData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetItemsDataByWHTransferNo(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetWhReceiveTypes(RequstPostObject requstObject, Headers headers);

	Task<GeneralResult> SaveCustomerInv(CustomerInv CustomerInv, Headers headers);

	Task<Value<ResponceObject>> SaveQuotation(RequstPostObject requstObject, Headers headers);

	Task<GeneralResult> SaveGps_Event(Gps_EventData Gps_EventData, Headers headers);

	Task<GeneralResult> SaveGps_EventNew(Gps_EventData Gps_EventData, Headers headers);

	Task<GeneralResult> SaveVists(VistsData VistsData, Headers headers);

	Task<GeneralResult> SaveCustGpsScan(Cust_Gps_Scan Cust_Gps_Scan, Headers headers);

	Task<GeneralResult> SaveCustomerTarget(CustomerTarget CustomerTarget, Headers headers);

	Task<GeneralResult> SaveRqTransfer(RqTransfer RqTransfer, Headers headers);

	Task<GeneralResult> SaveRepPlan(RepPlan RepPlan, Headers headers);

	Task<GeneralResult> UpdateCustomersData(UpdateCustomerData UpdateCustomerData, Headers headers);

	Task<GeneralResult> SaveGps_EventCurrent(GpsEventCurnt gpsEventCurnt, Headers headers);

	Task<GeneralResult> SaveGps_EventCurrentNew(GpsEventCurnt gpsEventCurnt, Headers headers);

	Task<Value<ResponceObject>> DocsTransferMatching(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetAccountStatment(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetBillMasterData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetGroupDetails(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetInstallmentBills(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveVouchers_new(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetQutPrmDtlData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCustomerClassData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveShowItems(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveShowItemsImages(Stream stream, Headers headers);

	Task<Value<ResponceObject>> GetItemSerialsData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetQuestionnaireQuestions(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetAnswerQuestionnaireQuestions(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveQuestionnaireDoc(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetItemsGroupsData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCreditCardTypes(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetReturnFromBill(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetReturnFromBillDetails(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetAllTaxItems(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCalcTaxType(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveCustomerTargetImages(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> TestApi(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetDocsSyncMethode(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetDtsCstAging(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCustomersTargetData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> CheckSetup(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetItemsBarcodeData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSmanPlanTrgt(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetDtsExpnsTypes(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveExpansDoc(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetDocInfoData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveWhTransferReciveDoc(RequstPostObject postRequstObject, Headers headers);

	Task<Value<ResponceObject>> UploadExpnsImages(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSalesOrderMst(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSalesOrderDtl(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveSaleOrder(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> UpdateColumn(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> UpdateColumnWithProc(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetDtsAccountStatmenDocDtl(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetReturnFromRtRqst(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetReturnFromRtRqstDetails(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetDtsDynamicScreenFileds(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveDtsBills(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveDtsRtBills(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetTaxInputData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetWhtransSerialNo(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveSample(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSalesSerialNo(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetMobileRequest(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetDocMst(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetDocDtls(RequstPostObject requstObject, Headers headers);

	Task<GeneralResult> UploadFile(Headers headers);

	Task<GeneralResult> SaveFileAsBlob1(Headers headers);

	Task<Value<ResponceObject>> GetItemsMarktProperty(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetMarktVisitFlag(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveMarkitingVisit(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCustomerLimitSales(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCustomerItemLimitSales(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetBillSalesCharges(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSmanDailayPlan(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSFlagCode(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetExtraScreenLabel(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCustomerCostCenter(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCashCustomer(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetFunctionData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSalesManDocumentMovement(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSalesManItemMovement(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetMandatoryField(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetAvlQtyOnline(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetKey(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSalesInfo(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveExpiryOutgoingRequest(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetSalesManBranchPrivilege(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetAccountConfirmBalances(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveConfirmCustomerBalance(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SavePromoter(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetMessageDetails(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetUsers(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveMassage(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> UpdateReadMessage(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCustomerPlanTarget(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetAccountStatmentDetails(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveDynamicFieldDocument(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetAccountStatementConfirm(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveCustomerAccountStatementConfirm(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetTargetPrometerData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetFreeSampleMovement(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCustomerItemsAvailableQuantity(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveOtherVisitTasks(RequstPostObject requstObject, Headers headers);

	Task<ResponceObject> SendByWhatsup(RequstPostObject requstObject, Headers headers);

	Task<ResponceObject> GetBillQrData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetFieldPrivilege(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetGeneralInputData(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> UpdateUserPassword(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetBillForNote(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> SaveBillNoteRequest(RequstPostObject requstObject, Headers headers);

	Task<ResponceObject> GetBillDataForPrint(RequstPostObject requstObject, Headers headers);

	Task<ResponceObject> SendVerficationMessage(RequstPostObject requstObject, Headers headers);

	Task<ResponceObject> GetGlRequestData(RequstPostObject requstObject, Headers headers);

	Task<ResponceObject> GetReportAsPdfFromOnyx(RequstPostObject requstObject, Headers headers);

	Task<ResponceObject> GetCustomerItemSold(RequstPostObject requstObject, Headers headers);

	Task<Value<ResponceObject>> GetCustomerStock(RequstPostObject requstObject, Headers headers);
}
