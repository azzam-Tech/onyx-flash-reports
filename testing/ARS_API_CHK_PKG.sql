--- SPEC ---
Package ARS_API_CHK_PKG
Is
--##-----------------------------------------------------------------------------------------------------##--                                                                
   Type Tp_Qt_Prm_Rec   Is Record
          (  Qt_Prm_Type              Number,
             Qt_Prm_Method            Number,
             Qt_Prm_Itm_Type          Number, 
             Qt_No                    Number,
             Qt_Ser                   Number,
             Qt_Icode                 Varchar2(30),
             Qt_Itm_Unt               Varchar2(10),
             Qt_Rcrd_No               Number,
             Dis_Per                  Number,
             Dis_Amt                  Number,
             Price                    Number,                              
             Fqty                     Number,
             Card_Amt                 Number,
             Qt_Rem_Qty               Number,                              
             Apprvd_Freeqty_As_Dscnt  Number                                  
           );                               
--##---------------------------------------------------------------------------------##--             
   Type Tp_Qt_Prm_Rfc Is Ref Cursor ;               
--##---------------------------------------------------------------------------------##--
   G_Qt_Prm  Tp_Qt_Prm_Rec ;                          
--##---------------------------------------------------------------------------------##--                        
   Type Tp_Qt_Prm_Tbl   Is Table Of Tp_Qt_Prm_Rec ;
--##-----------------------------------------------------------------------------------------------------##--
       Type Tp_disc_Rec   Is Record
        (  row_id   varchar2(4000)
         ,i_code    varchar2(300)
         ,i_qty      number
         ,free_qty  number
         ,p_size   Number
         ,i_price   Number
         ,i_price_vat  Number
         ,vat_per      Number
         ,Dis_Amt_Dtl   Number
         ,Dis_Amt_Dtl2  Number
         ,Dis_Amt_Dtl3   Number
         ,Dis_Amt_Dtl_vat  Number
         ,Dis_Amt_Dtl2_vat  Number
         ,Dis_Amt_Dtl3_vat  Number
         ,dis_per           Number
         ,dis_per2  Number
         ,dis_peR3  Number
         ,Dis_Amt_Mst_Vat  Number
         ,Dis_Amt_Mst   Number
         ,Dis_Amt      Number
         ,Vat_Amt_Dis_Dtl_Vat    Number
         ,Vat_Amt_Dis_Dtl2_Vat  Number
         ,Vat_Amt_Dis_Dtl3_Vat  Number
         ,Vat_Amt_Dis_Mst_Vat  Number
         ,Vat_Amt_Bfr_Dis  Number
         ,Vat_Amt_Aftr_Dis  Number
          );
TYPE TP_DISC_RFC     IS REF CURSOR ; 
G_DISC_REC      TP_DISC_REC ;                                              
TYPE TP_DISC_TBL   IS TABLE OF TP_DISC_REC ;   
Type BLK_DISC Is Table Of TP_DISC_REC Index By Binary_Integer;       
V_Blk_DISC BLK_DISC;  
--##---------------------------------------------------------------------------------##--  
Function Get_Qt_Prm  (   P_Date                    In  Date,
                          P_Bill_Ser                In  Number,
                          P_A_Cy                    In  Varchar2,
                          P_Icode                   In  Varchar2,
                          P_ItmUnt                  In  Varchar2,
                          P_Wcode                   In  Number,
                          P_Batch_No                In  Varchar2,
                          P_Exp_Date                In  Date,
                          P_Iqty                    In  Number,
                          P_P_Size                  In  Number,
                          P_Qt_Free_Qty             In  Number,
                          P_Qt_Dis_Per              In  Number,
                          P_Qt_Dis_Amt_Dtl          In  Number,
                          P_Rcrd_No                 In  Number,
                          P_IPrice                  In  Number,
                          P_Bill_Amt                In  Number,
                          P_Bill_Rate               In  Number,
                          P_Bill_Doc_Type           In  Number Default Null ,
                          P_C_Code                  In  Varchar2,
                          P_C_Group_Code            In  Number,
                          P_C_Class                 In  Number, 
                          P_C_Degree                In  Number,
                          P_C_Code_Csh              In  Varchar2,
                          P_Doc_Seq_Tmp             In  Number,
                          P_Chk_qtn_prm_css_sys     In  Number Default 0,
                          P_No_Of_Dcml              In  Number,
                          P_Usr_No                  In  Number)  Return Tp_Qt_Prm_Tbl Pipelined;
--##-----------------------------------------------------------------------------------------------------##---  
Function  Chk_Qt_Prm(P_I_Code       In Ias_Itm_Mst.I_Code%Type,
                     P_Bill_Doc_Typ In Number,
                     P_Doc_Date     In Date) Return Number; 
--##-----------------------------------------------------------------------------------------------------##---  
  Procedure Updt_Bill_Disc_Prc_OLD ( P_Doc_Typ             In     Number
                                ,P_Pst_Typ             In     Number
                                ,P_Doc_Ser             In     Number
                                ,P_Use_Vat             In     Number Default Null
                                ,P_Clc_Vat_Price_Typ   In     Number Default Null
                                ,P_Clc_Typ_No_Tax      In     Number Default Null
                                ,P_Fld_Doc_Ser         In     Varchar2                                
                                ,P_Tbl_Mvmnt_Nm        In     Varchar2
                                ,P_Tbl_Mst_Nm          In     Varchar2
                                ,P_Tbl_Dtl_Nm          In     Varchar2
                                ,P_Fld_MST_AMT         In     Varchar2
                                ,P_Lng_No              In     Number Default 1
                                ,P_Msg_Txt             Out Varchar2
                                ,P_ERR_NO            Out Varchar2
                                ,P_Pkg_Nm              Out Varchar2);

   --##-----------------------------------------------------------------------------------------------------##--
   Procedure Updt_Bill_Disc_Prc (P_Doc_Typ             In     Number
                             ,P_Pst_Typ             In     Number
                             ,P_Doc_Ser             In     Number
                             ,P_Use_Vat             In     Number Default Null
                             ,P_Bill_Doc_Type       In     Number Default Null
                             ,P_Clc_Vat_Price_Typ   In     Number Default Null
                             ,P_Clc_Typ_No_Tax      In     Number Default Null
                             ,P_CALC_TAX_AUTO_FLG   In     Number Default 0
                             ,P_Fld_Doc_Ser         In     Varchar2
                             ,P_Tbl_Mvmnt_Nm        In     Varchar2
                             ,P_Tbl_Mst_Nm          In     Varchar2
                             ,P_Tbl_Dtl_Nm          In     Varchar2
                             ,P_Fld_Mst_Amt         In     Varchar2
                             ,P_DIFF_AMT            In     Number Default Null
                             ,P_Lng_No              In     Number Default 1
                             ,P_Msg_Txt                Out Varchar2
                             ,P_Err_No                 Out Varchar2
                             ,P_Pkg_Nm                 Out Varchar2);
--##-----------------------------------------------------------------------------------------------------##--                             
    Procedure Chk_Conn_Cst_Col (P_C_Code     In     Customer.C_Code%Type Default Null
                              ,P_Col_No     In     Collerctor.Col_No%Type Default Null
                              ,P_Lng_No     In     Number Default 1
                              ,P_Msg_Txt    Out Varchar2
                              ,P_ERR_NO   Out Varchar2
                              ,P_Pkg_Nm     Out Varchar2);
--##-----------------------------------------------------------------------------------------------------##-- 
Procedure   Chk_Sman_Conn_Data (P_Sys_No           In     Number
                                ,P_Doc_Type        In     Number Default Null
                                ,P_Rep_Code        In     Sales_Man.Reprs_Code%Type Default Null
                                ,P_Bill_Doc_Type   In     Number Default Null
                                ,P_W_Code          In     Number Default Null
                                ,P_Cash_No         In     Number Default Null
                                ,P_Cc_Code         In     Varchar2 Default Null
                                ,P_Pj_No           In     Varchar2 Default Null
                                ,P_Actv_No         In     Varchar2 Default Null
                                ,P_Brn_Usr         In     Number   Default Null
                                ,P_Lng_No          In     Number Default 1
                                ,P_Msg_Txt         Out Varchar2
                                ,P_ERR_NO        Out Varchar2
                                ,P_Pkg_NM          Out Varchar2) ;
--##-----------------------------------------------------------------------------------------------------##-- 
Procedure Chk_Cr_Card_Prc (P_Bill_Doc_Type          In     Ias_Bill_Mst.Bill_Doc_Type%Type
                          ,P_Crdno                  In     Number
                          ,P_W_Code                 In     Ias_Bill_Mst.W_Code%Type
                          ,P_Cur_Code               In     Ex_Rate.Cur_Code%Type
                          ,P_Cr_Card_No             In     Ias_Bill_Mst.Cr_Card_No%Type
                          ,P_Cr_Card_Amt            In     Ias_Bill_Mst.Cr_Card_Amt%Type
                          ,P_Credit_Card            In Out Ias_Bill_Mst.Credit_Card%Type
                          ,P_Cr_A_Code              In Out Account.A_Code%Type
                          ,P_Cr_Card_Comm_Per       In Out Ias_Bill_Mst.Cr_Card_Comm_Per%Type                        
                          ,P_Cr_Card_Max_Comm_Amt   In Out Ias_Bill_Mst.Cr_Card_Max_Comm_Amt%Type                          
                          ,P_Online                 In     Number Default 1
                          ,P_Lng_No                 In     Number Default 1
                          ,P_Msg_Txt                   Out Varchar2
                          ,P_Err_No                    Out Varchar2
                          ,P_Pkg_Nm                    Out Varchar2);
--##-----------------------------------------------------------------------------------------------------##--                           
Procedure  Chk_Amt_And_Itm_Tax( P_Clc_Typ_No_Tax   In     Gnr_Tax_Itm_Movmnt.Clc_Typ_No%Type Default Null,
                                P_Use_Vat          In     Number Default Null ,
                                P_CLC_TAX_FREE_QTY_FLG  In   NUMBER Default Null, 
                                P_Calc_Vat_Amt_Type IN    NUMBER Default 1  ,
                                P_CALC_TAX_AUTO_FLG IN    NUMBER Default 0  ,
                                P_Doc_Typ          In     Gnr_Tax_Itm_Movmnt.Doc_Type%Type,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                P_Doc_No           In     Gnr_Tax_Itm_Movmnt.Doc_No%Type,
                                P_Doc_Ser          In     Gnr_Tax_Itm_Movmnt.Doc_Ser%Type,
                                P_Fld_Doc_No       In     Varchar2,
                                P_Fld_Doc_Ser      In     Varchar2,
                                P_Fld_MST_AMT      In     Varchar2,
                                P_Tbl_Mvmnt_Nm     In     Varchar2,
                                P_Tbl_Mst_Nm       In     Varchar2,
                                P_Tbl_Dtl_Nm       In     Varchar2,                                
                                P_No_Of_Decimal    In     Number ,
                                P_DIFF_AMT         In     Number Default Null,
                                P_DOC_AMT_XML      OUT    CLOB,
                                P_Lng_No           In     Number Default 1,
                                P_Msg_Txt          Out Varchar2,
                                P_ERR_NO         Out Varchar2,
                                P_Pkg_Nm           Out Varchar2);
--##-----------------------------------------------------------------------------------------------------##--
Procedure CHK_MNDTRY_FLIDS (P_Doc_Typ           IN  IAS_POST_DTL.DOC_TYPE%TYPE,
                            P_REP_CODE          IN  SALES_MAN.REPRS_CODE %Type  Default Null,
                            P_DOC_Desc          IN  IAS_POST_DTL.DOC_DESC %Type Default Null,
                            P_Use_Vat           In  Number Default Null , 
                            P_REF_NO            IN  Varchar2                    Default Null,
                            P_C_Code            IN  CUSTOMER.C_CODE %Type       Default Null,
                            P_Bill_Doc_Type     IN  CUSTOMER.C_CODE %Type       Default Null,
                            P_Lng_No            In     Number Default 1,
                            P_Msg_Txt           Out Varchar2,
                            P_ERR_NO          Out Varchar2,
                            P_Pkg_Nm            Out Varchar2      ); 
--##-----------------------------------------------------------------------------------------------------##--
Procedure Chk_Credit_Period (   P_CHK_CRDT_PRD    In     Number   --## 0-UNCHECK Credit_Period 1-CHECK_Credit_Period
                               ,P_C_Code          In     Customer.C_Code%Type
                               ,P_Doc_Ser         In     Ias_Post_Mst.Doc_Ser%Type Default Null
                               ,P_Doc_Date        In     Ias_Bill_Mst.Bill_Date%Type Default Null
                               ,P_Bill_Doc_Type   In     Ias_Bill_Mst.Bill_Doc_Type%Type
                               ,P_Stand_By        In     Ias_Bill_Mst.Stand_By%Type Default 0
                               ,P_Usr_No          In     User_R.U_Id%Type
                               ,P_Lng_No          In     Number Default 1
                               ,P_Msg_No          Out Number);
--##-----------------------------------------------------------------------------------------------------##-- 
Procedure Chk_Credit_Limit (   P_Chk_CrDT_LMIT  In    NUMBER --## 0 UNCHECKCredit_Limit  1- CHECK Credit_Limit 
                              ,P_Doc_Date       In    Ias_Bill_Mst.Bill_Date%Type Default Null
                              ,P_Doc_Ser        In    Ias_Bill_Mst.BILL_Ser%Type
                              ,P_Bill_Doc_Type  In    Ias_Bill_Mst.BILL_Ser%Type                            
                              ,P_Ac_Code        In    Account.A_Code%Type Default Null
                              ,P_Ac_Code_Dtl    In    Ias_Bill_Mst.Ac_Code_Dtl%Type Default Null
                              ,P_C_CODE         In     Ias_Bill_Mst.C_CODE%Type Default Null
                              ,P_Cash_No        In     Ias_Bill_Mst.Cash_No%Type Default Null                              
                              ,P_Brn_No         In     Ias_Bill_Mst.Brn_No%Type Default Null
                              ,P_User_No        In     User_R.U_Id%Type Default Null
                              ,P_Cur_Code       In     Ias_Bill_Mst.Bill_Currency%Type Default Null
                              ,P_CUR_RATE       In     NUMBER
                              ,P_Frc_No         In     Number Default 2
                              ,P_Stand_By       In     Number Default 0                              
                              ,P_Fld_Doc_Ser    In     Varchar2
                              ,P_Fld_MST_AMT    In     Varchar2
                              ,P_Tbl_Mst_Nm     In     Varchar2
                              ,P_Tbl_Dtl_Nm     In     Varchar2   Default Null
                              ,P_Lng_No         In     Number Default 1
                              ,P_Msg_Txt        OUT  Varchar2
                              ,P_ERR_NO         Out Varchar2
                              ,P_Pkg_Nm         Out Varchar2);
--##-----------------------------------------------------------------------------------------------------##--
Procedure Update_Other_Charges_OLD (P_Doc_Typ          In     Number
                               ,P_Doc_Ser          In     Number
                               ,P_Clc_Typ_No_Tax   In     Number
                               ,P_No_Of_Decimal    In     Number
                               ,P_Lng_No           In     Number Default 1
                               ,P_Msg_Txt             Out Varchar2
                               ,P_Err_No              Out Varchar2
                               ,P_Pkg_Nm              Out Varchar2) ;
--##-----------------------------------------------------------------------------------------------------##--
Procedure Update_Other_Charges (P_Doc_Typ          In     Number
                               ,P_Doc_Ser          In     Number
                               ,P_Use_Vat          In     Number Default Null 
                               ,P_Clc_Typ_No_Tax   In     Number
                               ,P_No_Of_Decimal    In     Number
                               ,P_Bill_Type        In     Number
                               ,P_CALC_TAX_AUTO_FLG   In     Number Default 0
                               ,P_Fld_Doc_Ser         In     Varchar2
                               ,P_TBL_OTHER_CHRG_NM   In     Varchar2
                               ,P_Tbl_INPT_Mvmnt_Nm   In     Varchar2
                               ,P_Tbl_Mst_Nm          In     Varchar2
                               ,P_Tbl_Dtl_Nm          In     Varchar2
                               ,P_Fld_Mst_Amt         In     Varchar2
                               ,P_DIFF_AMT            In     Number Default Null
                               ,P_Lng_No           In     Number Default 1
                               ,P_Msg_Txt             Out Varchar2
                               ,P_Err_No              Out Varchar2
                               ,P_Pkg_Nm              Out Varchar2);
--##-----------------------------------------------------------------------------------------------------##--                               
Procedure Chk_Rt_Bill_Info (P_Rt_Bill_Ser       In     Ias_Rt_Bill_Mst.Rt_Bill_Ser%Type Default Null
                           ,P_RT_Bill_No        In     Ias_Rt_Bill_Mst.Rt_Bill_no%Type Default Null
                           ,P_P_Year            In     Number Default Null
                           ,P_Pst_Typ           In     Number Default Null                          
                           ,P_Bill_No           In     Ias_Bill_Mst.Bill_No%Type Default Null
                           ,P_Bill_Ser          In     Ias_Bill_Mst.Bill_Ser%Type Default Null
                           ,P_I_Code            In     Ias_Bill_Dtl.I_Code%Type Default Null
                           ,P_P_Size            In     Ias_Bill_Dtl.P_Size%Type Default Null
                           ,P_I_Qty             In     Ias_Bill_Dtl.I_Qty%Type Default Null
                           ,P_Free_Qty          In     Ias_Bill_Dtl.I_Qty%Type Default Null
                           ,P_Expiredate        In     Ias_Bill_Dtl.Expire_Date%Type Default Null
                           ,P_Batchno           In     Ias_Bill_Dtl.Batch_No%Type Default Null
                           ,P_Doc_Sequence_Si   In Out Number 
                           ,P_Si_Rcrd_No        In Out Number 
                           ,P_Lng_No            In     Number Default 1
                           ,P_Msg_Txt              Out Varchar2
                           ,P_Err_No               Out Varchar2
                           ,P_Pkg_Nm               Out Varchar2);
--##-----------------------------------------------------------------------------------------------------##-- 
Procedure CHK_RETRN_BILL_INSTLL(P_SYS_NO            In NUMBER                               
                               ,P_rep_code          In Varchar2 Default Null 
                               ,P_c_code            In Varchar2 Default Null 
                               ,P_RT_BILL_DOC_TYPE  In ias_rt_bill_mst.RT_BILL_DOC_TYPE%TYPE 
                               ,P_Bill_Currency     In ias_bill_mst.Bill_Currency%TYPE
                               ,P_W_code            In ias_rt_bill_mst.w_code%TYPE       Default Null
                               ,P_RT_BILL_DATE      In ias_rt_bill_mst.RT_BILL_DATE%TYPE Default Null
                               ,P_Use_Vat           In     Number Default Null
                               ,P_CLC_TYP_NO_TAX    in number Default Null
                               ,P_p_year            In ias_rt_bill_mst.P_year%TYPE
                               ,P_Prev_Year         In Number
                               ,P_Brn_No            In S_brn.Brn_no%TYPE Default Null
                               ,P_Brn_Usr           In Number                                                                                        
                               ,P_Rt_Bill_Ser       In     Ias_Rt_Bill_Mst.Rt_Bill_Ser%Type Default Null
                               ,P_RT_Bill_No        In     Ias_Rt_Bill_Mst.Rt_Bill_no%Type Default Null                               
                               ,P_Pst_Typ           In     Number Default Null
                               ,P_Bill_No           In     Ias_Bill_Mst.Bill_No%Type Default Null
                               ,P_Bill_Ser          In     Ias_Bill_Mst.Bill_Ser%Type Default Null
                               ,P_I_Code            In     Ias_Bill_Dtl.I_Code%Type Default Null
                               ,P_P_Size            In     Ias_Bill_Dtl.P_Size%Type Default Null
                               ,P_I_Qty             In     Ias_Bill_Dtl.I_Qty%Type Default Null
                               ,P_Free_Qty          In     Ias_Bill_Dtl.I_Qty%Type Default Null
                               ,P_Expiredate        In     Ias_Bill_Dtl.Expire_Date%Type Default Null
                               ,P_Batchno           In     Ias_Bill_Dtl.Batch_No%Type Default Null
                               ,P_Doc_Sequence_Si   In Out Number
                               ,P_Si_Rcrd_No        In Out Number
                               ,P_Rtrn_From_Othr_Sman       In Number Default 0   --## 0 same sman-1 other sman                                
                               ,P_Usr_no            In Number 
                               ,P_Lng_No            In     Number Default 1
                               ,P_Msg_Txt              Out Varchar2
                               ,P_Err_No               Out Varchar2
                               ,P_Pkg_Nm               Out Varchar2); 
--##-----------------------------------------------------------------------------------------------------##--
Procedure INSRT_DOC_BY_XML (   P_Doc_Typ          In       Ias_Post_Mst.Doc_Type%Type
                              ,P_Xml              In OUT   Clob
                              ,P_COMMIT_FLG       In       NUMBER  --## 0 ROLLBACK ,1 COMMIT ,2 ,MANUAL COMMIT
                              ,P_CLC_TAX_METHOD   In       NUMBER  --## 0 CALC TAX IN EXTRNAL ,1-AOUTO CALC TAX                                                        
                              ,P_Pst_Typ          In       Number --## 1 to br tables ,2 to onyx tables
                              ,P_Pst_FROM_BR      In       Number  --## 1- POSTING FORM BR TABLE  0- NOT FROM BR
                              ,P_DTS_ONLINE       In     NUMBER DEFAULT 0 --## 0 OFFLINE ,1-ONLINE
                              ,P_Lng_No           In       Number Default 1                          
                              ,P_Msg_Txt          Out   Varchar2
                              ,P_ERR_NO           Out   Varchar2
                              ,P_Pkg_Nm           Out   Varchar2);
--##-----------------------------------------------------------------------------------------------------##--
Procedure Check_Duplicate (  P_Sys_No        IN   NUMBER, 
                              P_DOC_TYP       IN   NUMBER,
                              P_Pst_Typ       IN   NUMBER DEFAULT NULL, 
                              P_Doc_Ser       IN   NUMBER DEFAULT NULL,  
                              P_Bill_Doc_Type  IN   NUMBER DEFAULT NULL,      
                              P_BRN_YEAR      IN   NUMBER,
                              P_BRN_NO        IN   S_BRN.BRN_NO%TYPE ,
                              P_CC_CODE       IN   COST_CENTERS.CC_CODE%TYPE DEFAULT NULL,
                              P_W_CODE        IN   WAREHOUSE_DETAILS.W_CODE%TYPE DEFAULT NULL,
                              P_TYP_NO        IN   NUMBER ,
                              P_DOC_NO        IN   NUMBER  ,                           
                              P_Usr_No        In User_R.U_Id%Type  Default Null,
                              P_Trmnl_No      In Number            Default Null,
                              P_Lng_No       In User_R.U_Id%Type  Default Null,                       
                              P_Msg_Txt      Out Varchar2,
                              P_Err_No       Out Varchar2,
                              P_Pkg_Nm       Out Varchar2)  ;
--##-----------------------------------------------------------------------------------------------------##--
Procedure Calc_Other_Charges (P_Doc_Typ          In     Number
                             ,P_Bill_Doc_Type    In     Number
                             ,P_Doc_Ser          In     Number
                             ,P_Doc_Date         In     DATE
                             ,P_Brn_No           In     Number
                             ,P_Use_Vat          In     Number
                             ,P_Cur_Code         In     Ex_Rate.Cur_Code%Type
                             ,P_Cur_Rate         In     Number
                             ,P_Clc_Typ_No_Tax   In     Number
                             ,P_Fld_Doc_Ser      In     Varchar2
                             ,P_Fld_Mst_Amt      In     Varchar2                            
                             ,P_Tbl_Mst_Nm       In     Varchar2                             
                             ,P_No_Of_Decimal    In     Number
                             ,P_Lng_No           In     Number Default 1
                             ,P_Msg_Txt             Out Varchar2
                             ,P_Err_No              Out Varchar2
                             ,P_Pkg_Nm              Out Varchar2);
--##-----------------------------------------------------------------------------------------------------##-- 
Procedure Chk_Prmtr (          P_Sys_No          In       Number
                            ,  P_Doc_Typ          In      Number                            
                              ,P_COMMIT_FLG       In       NUMBER  --## 0 ROLLBACK ,1 COMMIT ,2 ,MANUAL COMMIT
                              ,P_CLC_TAX_METHOD   In       NUMBER  --## 0 CALC TAX IN EXTRNAL ,1-AOUTO CALC TAX                                                        
                              ,P_Pst_Typ          In       Number --## 1 to br tables ,2 to onyx tables
                              ,P_Pst_FROM_BR      In       Number  --## 1- POSTING FORM BR TABLE  0- NOT FROM BR
                              ,P_DTS_ONLINE       In     NUMBER DEFAULT 0 --## 0 OFFLINE ,1-ONLINE
                              ,P_Lng_No           In       Number Default 1                          
                              ,P_Msg_Txt          Out   Varchar2
                              ,P_ERR_NO           Out   Varchar2
                              ,P_Pkg_Nm           Out   Varchar2) ;
--##-----------------------------------------------------------------------------------------------------##--
PROCEDURE SND_ALRT_SAVE_DOC_PRC   (  P_SYS_NO      IN NUMBER ,
                                     P_DOC_TYP     IN NUMBER ,  
                                     P_DOC_SER     IN NUMBER ,                                                                
                                     P_SCHMA_NM    IN VARCHAR2 DEFAULT NULL,                                   
                                     P_U_ID        IN NUMBER,                                    
                                     P_DTS_ONLINE  IN NUMBER,
                                     P_COMMIT_FLG  IN NUMBER,
                                     P_Pst_Typ     IN NUMBER DEFAULT 1,                        
                                     P_LNG_NO      IN NUMBER     DEFAULT 1
                                   ) ;
--##-----------------------------------------------------------------------------------------------------##--
Procedure Chk_Sale_Outlet ( P_Sys_No                      In  Number     Default Null  
                           ,P_Cc_Code                     In  Ias_Bill_Mst.C_Code%Type Default Null  
                           ,P_Lang                        In  Number Default 1
                           ,P_Msg_Txt                     Out Varchar2
                           ,P_Err_No                      Out Varchar2
                           ,P_Pkg_Nm                      Out Varchar2  ) ; 
--##-----------------------------------------------------------------------------------------------------##--                                                                                                                                                                              
END ARS_API_CHK_PKG; 

--- BODY ---
Package Body ARS_API_CHK_PKG
IS
--##-----------------------------------------------------------------------------------------------------##--
Function Get_Qt_Prm  (   P_Date                    In  Date,
                          P_Bill_Ser                In  Number,
                          P_A_Cy                    In  Varchar2,
                          P_Icode                   In  Varchar2,
                          P_ItmUnt                  In  Varchar2,
                          P_Wcode                   In  Number,
                          P_Batch_No                In  Varchar2,
                          P_Exp_Date                In  Date,
                          P_Iqty                    In  Number,
                          P_P_Size                  In  Number,
                          P_Qt_Free_Qty             In  Number,
                          P_Qt_Dis_Per              In  Number,
                          P_Qt_Dis_Amt_Dtl          In  Number,
                          P_Rcrd_No                 In  Number,
                          P_IPrice                  In  Number,
                          P_Bill_Amt                In  Number,
                          P_Bill_Rate               In  Number,
                          P_Bill_Doc_Type           In  Number Default Null ,
                          P_C_Code                  In  Varchar2,
                          P_C_Group_Code            In  Number,
                          P_C_Class                 In  Number, 
                          P_C_Degree                In  Number,
                          P_C_Code_Csh              In  Varchar2,
                          P_Doc_Seq_Tmp             In  Number,
                          P_Chk_qtn_prm_css_sys     In  Number Default 0,
                          P_No_Of_Dcml              In  Number,
                          P_Usr_No                  In  Number)Return Tp_Qt_Prm_Tbl Pipelined Is 
Pragma Autonomous_Transaction;
V_Qt_Prm_Type Number(15);
V_Qt_Prm_Method Number;
V_Qt_Prm_Itm_Type Number;
V_Qt_Prm_No       Number(15);
V_Qt_Prm_Ser      Number;
v_Qt_Icode        Varchar2(30);
v_Qt_Itm_Unt      Varchar2(10);
V_Qt_Prm_Rcrd_No  Number;
v_dis_per         Number;
v_dis_amt         Number;
v_free_qty        number;
v_i_price         Number;
v_Card_Amt        Number;
v_Qt_Rem_Qty      Number;
V_Apprvd_Freeqty_As_Dscnt Number;
V_Use_Qt_Prm_Tmp_Tbl  Number;
V_Use_Qt_Prm_Less_Price Number;
V_Use_Qt_Prm_PrmGrp      Number;
V_Use_Qt_Prm_PrmGrp_Dsc  Number;
V_Use_Qt_Prm_Prm    Number;
V_Doc_Seq_Tmp       Number;
V_Qt_Prm_Grp_No     Number;
Begin
    Begin

      Ias_Qt_Prm_Pkg.Ias_Get_Qt_Prm ( P_Date                    => P_Date       ,
                                      P_Bill_Ser                => P_Bill_Ser   ,
                                      P_Icode                   => P_Icode      ,
                                      P_ItmUnt                  => P_ItmUnt     ,
                                      P_Wcode                   => P_Wcode     ,
                                      P_Batch_No                => P_Batch_No                    ,
                                      P_Exp_Date                => P_Exp_Date                   ,
                                      P_Iqty                    => P_Iqty                        ,
                                      P_Iprice                  => P_Iprice                     ,
                                      P_Bill_Amt                => P_Bill_Amt                   ,
                                      P_Bill_Rate               => Ias_gen_pkg.Get_cur_rate ( P_acy       => P_A_Cy,
                                                                                              P_Usr_No    => P_Usr_No),
                                      P_Bill_Doc_Type           => P_Bill_Doc_Type              ,                                              
                                      P_C_Code                  => P_C_Code         ,
                                      P_C_Group_Code            => P_C_Group_Code               ,
                                      P_Cst_Grp_Csh             =>NULL,
                                      P_C_Class                 => P_C_Class                     ,
                                      P_C_Degree                => P_C_Degree                  ,
                                      P_C_Code_Csh              => P_C_Code_Csh   ,
                                      P_Doc_Seq_Tmp             => P_Doc_Seq_Tmp     ,                                              
                                      P_Chk_qtn_prm_css_sys     => P_Chk_qtn_prm_css_sys,
                                      P_Qt_Prm_Type             => V_Qt_Prm_Type                 ,
                                      P_Qt_Prm_Method           => V_Qt_Prm_Method               ,
                                      P_Qt_Prm_Itm_Type         => V_Qt_Prm_Itm_Type             ,      
                                      P_Qt_No                   => V_Qt_Prm_No                   ,
                                      P_Qt_Ser                  => V_Qt_Prm_Ser                  ,
                                      P_Qt_Icode                => v_Qt_Icode                    ,
                                      P_Qt_Itm_Unt              => v_Qt_Itm_Unt                  ,
                                      P_Qt_Rcrd_No              => V_Qt_Prm_Rcrd_No              ,
                                      P_Dis_Per                 => v_dis_per                     ,
                                      P_Dis_Amt                 => v_dis_amt                     ,
                                      P_Price                   => v_i_price                     ,
                                      P_Fqty                    => v_free_qty                    ,
                                      P_Card_Amt                => v_Card_Amt                    ,
                                      P_Qt_Rem_Qty              => v_Qt_Rem_Qty                  ,
                                      P_Sys_Typ                 =>1,
                                      P_Apprvd_Freeqty_As_Dscnt => V_Apprvd_Freeqty_As_Dscnt     ,
                                      P_No_Of_Dcml              => P_No_Of_Dcml     ); 
    Exception When Others Then 
        V_Qt_Prm_Type :=Null;
        V_Qt_Prm_Method :=Null;
        V_Qt_Prm_Itm_Type :=Null;
        V_Qt_Prm_No       :=Null;
        V_Qt_Prm_Ser      :=Null;
        v_Qt_Icode        :=Null;
        v_Qt_Itm_Unt      :=Null;
        V_Qt_Prm_Rcrd_No  :=Null;
        v_dis_per         :=Null;
        v_dis_amt         :=Null;
        v_free_qty        :=Null;
        v_i_price         :=Null;
        v_Card_Amt        :=Null;
        v_Qt_Rem_Qty      :=Null;
        V_Apprvd_Freeqty_As_Dscnt :=Null;
    End;   
    If V_Qt_Prm_Ser Is Not Null Then
             Begin                                                        
                 Select 
                   V_Qt_Prm_Type,
                   V_Qt_Prm_Method,
                   V_Qt_Prm_Itm_Type,
                   V_Qt_Prm_No,
                   V_Qt_Prm_Ser , 
                   v_Qt_Icode ,
                   v_Qt_Itm_Unt,
                   V_Qt_Prm_Rcrd_No,
                   v_dis_per,
                   v_dis_amt,
                   v_i_price,
                   v_free_qty,
                   v_Card_Amt,
                   v_Qt_Rem_Qty ,
                   V_Apprvd_Freeqty_As_Dscnt
                 Into G_Qt_Prm
                 From Dual;
                   
                  Pipe Row(G_Qt_Prm);                                          
             Exception 
               When Others Then
                Raise_Application_Error(-20006, 'Err When Get Qt Prm '||Sqlcode||' : '||Sqlerrm) ; 
             End;
    Else
       Begin
         ---------------------------------------------------------------------------------------------------------------------------
         Begin
            Select 1 InTo V_Use_Qt_Prm_Tmp_Tbl From Ias_Qut_Prm_Mst Where P_Date Between F_Date And T_Date 
             And (Qt_Prm_Type In (4,5) Or (Qt_Prm_Type In (1,2) And Qt_Prm_Method In (6,7)) Or (Qt_Prm_Type=2 And Qt_Prm_Method=1 And Nvl(CALC_ALL_SLIDES,0)=1) Or (Qt_Prm_Type=2 And Qt_Prm_Method=4 And Nvl(By_Comp_Qty,0)=1 And Nvl(Cmltv_Mnth_Flg,0)=1) ) And RowNum<=1;     
         Exception When Others Then
           V_Use_Qt_Prm_Tmp_Tbl  :=0; 
         End ;
         ---------------------------------------------------------------------------------------------------------------------------
         Begin
            Select 1 InTo V_Use_Qt_Prm_Less_Price From Ias_Qut_Prm_Mst Where Qt_Prm_Type In (4,5) And P_Date Between F_Date And T_Date And RowNum<=1;
         Exception When Others Then
            V_Use_Qt_Prm_Less_Price:=0; 
         End ;
         ---------------------------------------------------------------------------------------------------------------------------
         Begin
            Select 1 InTo V_Use_Qt_Prm_PrmGrp From Ias_Qut_Prm_Mst Where Qt_Prm_Type In (1,2) And Qt_Prm_Method In (6,7) And P_Date Between F_Date And T_Date And RowNum<=1;        
         Exception When Others Then
            V_Use_Qt_Prm_PrmGrp :=0; 
         End ;
         Begin
            Select 1 InTo V_Use_Qt_Prm_PrmGrp_Dsc From Ias_Qut_Prm_Mst Where ((Qt_Prm_Type In (1,2) And Qt_Prm_Method=6) Or Qt_Prm_Type In (4,5)) And P_Date Between F_Date And T_Date And RowNum<=1;
         Exception When Others Then
          V_Use_Qt_Prm_PrmGrp_Dsc :=0; 
         End ;
         
         Begin
            Select 1 InTo V_Use_Qt_Prm_Prm From Ias_Qut_Prm_Mst Where P_Date Between F_Date And T_Date And RowNum<=1;
         Exception When Others Then
           V_Use_Qt_Prm_Prm:=0; 
         End ;     
       End;
       
       If V_Use_Qt_Prm_Tmp_Tbl=1 Then
              Begin
                Select Ias_Doc_Seq_Othr.Nextval Into V_Doc_Seq_Tmp From Dual;
              Exception
                  When Others Then
                   RAISE_APPLICATION_ERROR(-20177,'Err. When Get Doc_Seq_Tmp '||SQLERRM) ;
              End;
          
                     Begin
                    begin
                      Delete  IAS_BILL_DTL_ITM_TMP where Doc_Seq=V_Doc_Seq_Tmp;
                    Exception
                      When No_Data_Found Then Null;
                    End;
                       

                    If P_ICODE Is Not Null AND P_ItmUnt Is Not Null Then
                       Insert Into IAS_BILL_DTL_ITM_TMP (Bill_Doc_Type, I_Code, Itm_Unt,P_Size,I_Qty,Qt_Free_Qty,I_Price, W_Code, C_Code, Dis_Per, Dis_Amt_Dtl, Rcrd_No, Doc_Seq,Chng_Flg)
                           Values (P_Bill_Doc_Type, P_ICODE, P_ItmUnt,P_P_Size,P_Iqty,P_Qt_Free_Qty,P_IPrice, P_Wcode, P_C_Code, P_Qt_Dis_Per, P_Qt_Dis_Amt_Dtl,P_Rcrd_No,V_Doc_Seq_Tmp, 0);
                    End If;                   
                  Exception
                      When Others Then
                         RAISE_APPLICATION_ERROR(-20178,'Err. When Insert Tbl Tmp '||SQLERRM) ;
                  End;
            If V_Use_Qt_Prm_Less_Price=1 Then 
               Ias_Qt_Prm_Pkg.IAS_Calc_Quot_Prm_Prc ( P_Date => P_Date , P_Bill_Doc_Type => P_Bill_Doc_Type , P_No_Of_Dcml => P_No_Of_Dcml,P_Sys_Typ =>1);
            End If; 
            
            If V_Use_Qt_Prm_PrmGrp=1 Then  
               Ias_Qt_Prm_Pkg.IAS_Clc_Qtn_Prm_Grp_Prc (  P_Date           => P_Date     , 
                                                         P_Bill_Doc_Type  => P_Bill_Doc_Type , 
                                                         P_C_Code         => P_C_Code        ,
                                                         P_C_Group_Code   => P_C_Group_Code               ,
                                                         P_C_Class        => P_C_Class                    ,
                                                         P_C_Degree       => P_C_Degree                   ,
                                                         P_Cst_Grp_Csh    =>NULL,
                                                         P_Sys_Typ        =>1,
                                                         P_No_Of_Dcml     => P_No_Of_Dcml     );  
            End If;  
           If V_Use_Qt_Prm_Tmp_Tbl=1 Then
              Begin
                Select Qt_Free_Qty, I_Price, Dis_Per, Dis_Amt_Dtl, Qt_Prm_No, Qt_Prm_Ser, Qt_Prm_Rcrd_No
                  Into v_free_qty,v_i_price,v_dis_per,v_dis_amt,V_Qt_Prm_No,V_Qt_Prm_Ser,V_Qt_Prm_Rcrd_No
                  From IAS_BILL_DTL_ITM_TMP
                 Where Nvl(Chng_Flg,0)=1
                   And I_Code=P_ICode
                   And Doc_Seq=V_Doc_Seq_Tmp;
              Exception When Others Then
               --RAISE_APPLICATION_ERROR(-20178,'Err. IAS_BILL_DTL_ITM_TMP P_ICode'||P_ICode||','||'V_Doc_Seq_Tmp='||V_Doc_Seq_Tmp||SQLERRM) ;
                v_free_qty   :=Null;
                v_i_price  :=Null;
                v_dis_per:=Null;
                v_dis_amt :=Null;
                V_Qt_Prm_No:=Null;
                V_Qt_Prm_Ser:=Null;
                V_Qt_Prm_Rcrd_No:=Null;
              End ;
              
               Begin                                                        
                 Select 
                   V_Qt_Prm_Type,
                   V_Qt_Prm_Method,
                   V_Qt_Prm_Itm_Type,
                   V_Qt_Prm_No,
                   V_Qt_Prm_Ser , 
                   v_Qt_Icode ,
                   v_Qt_Itm_Unt,
                   V_Qt_Prm_Rcrd_No,
                   v_dis_per,
                   v_dis_amt,
                   v_i_price,
                   v_free_qty,
                   v_Card_Amt,
                   v_Qt_Rem_Qty ,
                   V_Apprvd_Freeqty_As_Dscnt
                 Into G_Qt_Prm
                 From Dual;
                  COMMIT;
                  Pipe Row(G_Qt_Prm);                                          
             Exception 
               When Others Then
                Raise_Application_Error(-20006, 'Err When Get Qt Prm '||Sqlcode||' : '||Sqlerrm) ; 
             End;
             
              Begin
                  Update Ias_Bill_Dtl_ITM_TMP Set Chng_Flg=0 Where Doc_Seq=V_Doc_Seq_Tmp; 
                  COMMIT;                            
              Exception
                  When No_Data_Found Then Null;    
              End; 
           End If;                
       End If;
       
    End If;
       
End Get_Qt_Prm;
--##-----------------------------------------------------------------------------------------------------##--
Function  Chk_Qt_Prm(P_I_Code       In Ias_Itm_Mst.I_Code%Type,
                     P_Bill_Doc_Typ In Number,
                     P_Doc_Date     In Date)  Return Number Is
V_Cnt Number:=0;
Begin
    Begin
      Select 1 InTo V_Cnt
          From Ias_Qut_Prm_Mst,Ias_Qut_Prm_Dtl
         Where Ias_Qut_Prm_Mst.Quot_Ser = Ias_Qut_Prm_Dtl.Quot_Ser
           And Ias_Qut_Prm_Dtl.I_Code= P_I_Code
           And Nvl(Ias_Qut_Prm_Mst.Inactive,0)=0
           And Decode(P_Bill_Doc_Typ,4,2,1) = Decode(Ias_Qut_Prm_Mst.Bill_Doc_Type,Null,Decode(P_Bill_Doc_Typ,4,2,1),Ias_Qut_Prm_Mst.Bill_Doc_Type)
           And P_Doc_Date Between F_Date And T_Date
           And To_Char(To_Date(P_Doc_Date),'D') In (Fld_Day1,Fld_Day2,Fld_Day3,Fld_Day4,Fld_Day5,Fld_Day6,Fld_Day7) 
           And RowNum <=1 ;
    Exception WHen Others Then
        V_Cnt :=0;
    End;
    
    Return(V_Cnt);  
End Chk_Qt_Prm;  
--##-----------------------------------------------------------------------------------------------------##--
Procedure Updt_Bill_Disc_Prc_OLD (P_Doc_Typ             In     Number
                             ,P_Pst_Typ             In     Number
                             ,P_Doc_Ser             In     Number
                             ,P_Use_Vat             In     Number Default Null
                             ,P_Clc_Vat_Price_Typ   In     Number Default Null
                             ,P_Clc_Typ_No_Tax      In     Number Default Null
                             ,P_Fld_Doc_Ser         In     Varchar2
                             ,P_Tbl_Mvmnt_Nm        In     Varchar2
                             ,P_Tbl_Mst_Nm          In     Varchar2
                             ,P_Tbl_Dtl_Nm          In     Varchar2
                             ,P_Fld_Mst_Amt         In     Varchar2
                             ,P_Lng_No              In     Number Default 1
                             ,P_Msg_Txt                Out Varchar2
                             ,P_Err_No                 Out Varchar2
                             ,P_Pkg_Nm                 Out Varchar2)
Is
   V_Bill_Amt                      Number;
   V_Bill_Amt_Vat                  Number;
   V_Discount                      Number;
   V_Disc_Amt_Mst                  Number;
   V_Disc_Amt                      Number;
   V_Disc_Amt_Dtl                  Number;
   V_Disc_Amt_Mst_Vat              Number;
   --V_disc_amt_mst_vat
   V_Sum_Dis_Amt_Dtl_Vat           Number;
   V_Sum_Dis_Amt_Dtl               Number;
   V_No_Of_Decimal                 Number;
   V_Show_Dis_Per_Item             Number;
   Calc_Si_Disc_Without_Itm_Disc   Number;
   V_Clc_Tax_Dscnt2                NUMBER;
   V_Clc_Tax_Dscnt3                NUMBER;
Begin
   If P_Clc_Typ_No_Tax Is Null And Nvl (P_Use_Vat, 0) = 1 Then
      P_Err_No    := 20214;
      P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 1601) || ' P_CLC_TYP_NO_TAX ';
      Goto Rtn_Rslt;
   End If;


   --------------------------------------------------------------------------

   --##PARA
   Select Nvl (Calc_Si_Disc_Without_Itm_Disc, 0), Nvl (No_Of_Decimal_Ar, 2), Nvl (Show_Disc_Per_Items_Ar, 0)
   ,NVL(Clc_Tax_Dscnt2,0),NVL(Clc_Tax_Dscnt3,0)
     Into Calc_Si_Disc_Without_Itm_Disc, V_No_Of_Decimal, V_Show_Dis_Per_Item
     ,V_Clc_Tax_Dscnt2,V_Clc_Tax_Dscnt3
     From Ias_Para_Ar;

   --#----------------------------------------------------------------------------------------------------------------------------------------##---
   Execute Immediate 'SELECT NVL(SUM((NVL(I_QTY,0) * NVL(I_PRICE,0))),0),NVL(SUM((NVL(I_QTY,0) * NVL(I_PRICE_VAT,0))),0) 
                         FROM ' || P_Tbl_Dtl_Nm || '
                         WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser Into V_Bill_Amt, V_Bill_Amt_Vat;

   ------------------------------------
   Execute Immediate 'SELECT  nvl(disc_amt_Mst,0) ,NVL(disc_amt_mst_vat,0)
                       FROM ' || P_Tbl_Mst_Nm || ' 
                       WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser Into V_Disc_Amt_Mst, V_Disc_Amt_Mst_Vat;

   --#----------------------------------------------------------------------------------------------------------------------------------------##---

   If Nvl (P_Clc_Vat_Price_Typ, 1) = 2 Then
      --## dis_amt_dtl_vat
      Begin
         ------------------------
         If V_Show_Dis_Per_Item = 1 Then
            --------------------------------------------------------------
            Begin
               Execute Immediate ' UPDATE ' || P_Tbl_Dtl_Nm || ' SET 
                                                                     dis_per= (nvl(dis_amt_dtl_vat,0)/nvl(i_price_vat,0))*100 ,
                                                                     Dis_Amt_Dtl= (nvl(dis_amt_dtl_vat,0) /((Nvl(Vat_Per,0)/100)+1))    
                                                     WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || '
                                                        AND nvl(dis_amt_dtl_vat,0)>0
                                                        AND Nvl(i_price_vat,0) > 0 ';
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20363;
                  Goto Rtn_Rslt;
            End;

            --------------------------------------------------------------
            Begin
               Execute Immediate '  UPDATE  ' || P_Tbl_Dtl_Nm || ' SET 
                                                                         dis_per2=(nvl(Dis_Amt_Dtl2_vat,0)/(nvl(i_price_vat,0)-Nvl(Dis_Amt_Dtl_vat,0)))*100, 
                                                                         Dis_Amt_Dtl2=DECODE('||V_Clc_Tax_Dscnt2||',1,NVL(Dis_Amt_Dtl2_Vat,0) /((Nvl(Vat_Per,0)/100)+1),Dis_Amt_Dtl2_Vat)     
                                                         WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || '
                                                           AND Nvl(i_price_vat,0) > 0
                                                           AND nvl(Dis_Amt_Dtl2_Vat,0)>0
                                                           And (nvl(i_price_vat,0)-Nvl(Dis_Amt_Dtl_vat,0))>0 ';
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20364;
                  Goto Rtn_Rslt;
            End;

            --------------------------------------------------------------
            Begin
               Execute Immediate '  UPDATE ' || P_Tbl_Dtl_Nm || ' SET 
                                                                         dis_per3=(nvl(Dis_Amt_Dtl3_Vat,0)/(nvl(i_price_Vat,0)-Nvl(Dis_Amt_Dtl_Vat,0)-Nvl(Dis_Amt_Dtl2_Vat,0)))*100, 
                                                                         Dis_Amt_Dtl3=DECODE('||V_Clc_Tax_Dscnt3||',1, NVL(Dis_Amt_Dtl3_Vat,0) /((Nvl(Vat_Per,0)/100)+1),Dis_Amt_Dtl3_Vat)     
                                                         WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || '
                                                           AND Nvl(i_price_vat,0) > 0
                                                           AND nvl(Dis_Amt_Dtl3_Vat,0)>0
                                                           And (nvl(i_price_Vat,0)-Nvl(Dis_Amt_Dtl_Vat,0)-Nvl(Dis_Amt_Dtl2_Vat,0))>0 ';
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20365;
                  Goto Rtn_Rslt;
            End;
       
            --------------------------------------------------------------
             Begin
               Execute Immediate '  UPDATE ' || P_Tbl_Dtl_Nm || ' 
                                              set   dis_per=(nvl(dis_amt_dtl,0)/nvl(i_price,0))*100
                                                   ,dis_per2=(nvl(dis_amt_dtl2,0)/(nvl(i_price,0)-Nvl(dis_amt_dtl,0)))*100 
                                                  ,dis_per3=(nvl(dis_amt_dtl3,0)/(nvl(i_price,0)-Nvl(dis_amt_dtl,0)-Nvl(dis_amt_dtl2,0)))*100     
                                             WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || '
                                                           AND Nvl(i_price,0) > 0 ';                                                          
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20426;
                  Goto Rtn_Rslt;
            end;
             --------------------------------------------------------------     
            If Nvl (Ys_Tax_Pkg.Get_Clc_Tax_Typ (P_Clc_Typ_No => P_Clc_Typ_No_Tax), 0) = 0 Then
               Begin
                  Execute Immediate '  UPDATE ' || P_Tbl_Dtl_Nm || ' SET 
                                                                 Vat_Amt_Dis_Dtl_Vat  = Nvl(dis_amt_dtl_Vat,0)-Nvl(dis_amt_dtl,0),
                                                                 Vat_Amt_Dis_Dtl2_Vat = Nvl(dis_amt_dtl2_Vat,0)-Nvl(dis_amt_dtl2,0),
                                                                 Vat_Amt_Dis_Dtl3_Vat = Nvl(dis_amt_dtl3_Vat,0)-Nvl(dis_amt_dtl3,0)
                                                           WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || '
                                                               AND Nvl(i_price_vat,0) > 0  ';
               Exception
                  When No_Data_Found Then
                     Null;
                  When Others Then
                     Raise_Application_Error (-20366, 'Errt When Update Disc' || Chr (10) || Sqlerrm);
               End;
            Else
               Begin
                  Execute Immediate '  UPDATE ' || P_Tbl_Dtl_Nm || ' SET 
                                                                 Vat_Amt_Dis_Dtl_Vat  =0,
                                                                 Vat_Amt_Dis_Dtl2_Vat =0,
                                                                 Vat_Amt_Dis_Dtl3_Vat = 0
                                                         WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || '
                                                               AND Nvl(i_price_vat,0) > 0 ';
               Exception
                  When No_Data_Found Then
                     Null;
                  When Others Then
                     Raise_Application_Error (-20367, 'Errt When Update Disc' || Chr (10) || Sqlerrm);
               End;
            End If;
         End If;
      End;
   End If;

   --##---------------------------------------------------------------------------------------------------------------------------------------##--

   --##--------------------------------------------------------------------------------------##--
   Begin
      If Nvl (P_Clc_Vat_Price_Typ, 0) = 2 Then
         Begin
            Execute Immediate 'SELECT SUM((NVL(DIS_AMT_DTL_VAT,0)+NVL(DIS_AMT_DTL2_VAT,0)+NVL(DIS_AMT_DTL3_VAT,0))*NVL(I_QTY,0)) 
                                               FROM ' || P_Tbl_Dtl_Nm || ' 
                                    WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser Into V_Sum_Dis_Amt_Dtl_Vat;
         Exception
            When No_Data_Found Then
               Null;
            When Others Then
               P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
               P_Err_No    := 20368;
               Goto Rtn_Rslt;
         End;
      Else
         Begin
            Execute Immediate ' SELECT SUM((NVL(DIS_AMT_DTL,0)+NVL(DIS_AMT_DTL2,0)+NVL(DIS_AMT_DTL3,0))*NVL(I_QTY,0)) 
                                      FROM ' || P_Tbl_Dtl_Nm || '
                                     WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser Into V_Sum_Dis_Amt_Dtl;
         Exception
            When No_Data_Found Then
               Null;
            When Others Then
               P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
               P_Err_No    := 20369;
               Goto Rtn_Rslt;
         End;
      End If;
   Exception
      When Others Then
         Null;
   End;

   --##--------------------------------------------------------------------------------------##--

   If Nvl (P_Clc_Vat_Price_Typ, 0) = 2 Then
      If Nvl (V_Bill_Amt_Vat, 0) > 0 Then
         If Calc_Si_Disc_Without_Itm_Disc = 1 And (Nvl (V_Bill_Amt_Vat, 0) - Nvl (V_Sum_Dis_Amt_Dtl_Vat, 0)) > 0 Then
            V_Discount   := (100 * Nvl (V_Disc_Amt_Mst_Vat, 0)) / (Nvl (V_Bill_Amt_Vat, 0) - Nvl (V_Sum_Dis_Amt_Dtl_Vat, 0));

            Begin
               Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' SET Disc_Amt_Mst_Vat=Round((((' || Nvl (V_Bill_Amt_Vat, 0) || '- ' || Nvl (V_Sum_Dis_Amt_Dtl_Vat, 0) || ')*' || Nvl (V_Discount, 0) || ')/100),' || V_No_Of_Decimal || ') 
                         WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20370;
                  Goto Rtn_Rslt;
            End;
         Elsif Calc_Si_Disc_Without_Itm_Disc = 0 Then
            V_Discount   := (100 * Nvl (V_Disc_Amt_Mst_Vat, 0)) / V_Bill_Amt_Vat;

            Begin
               Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' SET Disc_Amt_Mst_Vat=Round(((' || Nvl (V_Bill_Amt_Vat, 0) || '*' || Nvl (V_Discount, 0) || ')/100),' || V_No_Of_Decimal || ') 
                                           WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20371;
                  Goto Rtn_Rslt;
            End;
         End If;
      End If;
   Else
      If Nvl (V_Bill_Amt, 0) > 0 Then
         If Calc_Si_Disc_Without_Itm_Disc = 1 And (Nvl (V_Bill_Amt, 0) - Nvl (V_Sum_Dis_Amt_Dtl, 0)) > 0 Then
            V_Discount   := (100 * Nvl (V_Disc_Amt_Mst, 0)) / (Nvl (V_Bill_Amt, 0) - Nvl (V_Sum_Dis_Amt_Dtl, 0));

            Begin
               Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' SET Disc_Amt_Mst=Round((((' || Nvl (V_Bill_Amt, 0) || '- ' || Nvl (V_Sum_Dis_Amt_Dtl, 0) || ')*' || Nvl (V_Discount, 0) || ')/100),' || V_No_Of_Decimal || ')
                                                     WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20372;
                  Goto Rtn_Rslt;
            End;
         Elsif Calc_Si_Disc_Without_Itm_Disc = 0 Then
            V_Discount   := (100 * Nvl (V_Disc_Amt_Mst, 0)) / V_Bill_Amt;

            Begin
               Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' SET Disc_Amt_Mst=Round(((' || Nvl (V_Bill_Amt, 0) || ' *' || Nvl (V_Discount, 0) || ')/100),' || V_No_Of_Decimal || ') 
                                WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20373;
                  Goto Rtn_Rslt;
            End;
         End If;
      End If;
   End If;

   --##--------------------------------------------------------------------------------------------##--
   If Nvl (P_Clc_Vat_Price_Typ, 0) = 2 Then
      Begin
         Execute Immediate ' SELECT NVL(disc_amt_mst_vat,0)  FROM ' || P_Tbl_Mst_Nm || ' 
                                        WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || ' 
                                        AND ROWNUM<=1' Into V_Disc_Amt_Mst_Vat;
      Exception
         When No_Data_Found Then
            V_Disc_Amt_Mst_Vat   := 0;
         When Others Then
            P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
            P_Err_No    := 20374;
            Goto Rtn_Rslt;
      End;

      Begin
         Execute Immediate ' UPDATE  ' || P_Tbl_Dtl_Nm || ' Set Dis_Amt_Mst_Vat = ((((100 *' || Nvl (V_Disc_Amt_Mst_Vat, 0) || ')/' || V_Bill_Amt_Vat || ')*Nvl(i_price_vat,0))/100),
                                  Dis_Amt_Mst     = ((((100 * ' || Nvl (V_Disc_Amt_Mst_Vat, 0) || ')/' || V_Bill_Amt_Vat || ')*Nvl(i_price_vat,0))/100) /((Nvl(Vat_Per,0)/100)+1),    
                                  Vat_Amt_Dis_Mst_Vat = ((((100 * ' || Nvl (V_Disc_Amt_Mst_Vat, 0) || ')/' || V_Bill_Amt_Vat || ')*Nvl(i_price_vat,0))/100) - ((((100 * ' || Nvl (V_Disc_Amt_Mst_Vat, 0) || ')/' || V_Bill_Amt_Vat || ')*Nvl(i_price_vat,0))/100) /((Nvl(Vat_Per,0)/100)+1)
           Where ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
      Exception
         When No_Data_Found Then
            Null;
         When Others Then
            P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
            P_Err_No    := 20375;
            Goto Rtn_Rslt;
      End;

      Begin
         Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' Set Disc_Amt_Mst = (Select SUM(Nvl(I_Qty,0)*Nvl(Dis_Amt_Mst,0))
                                                                     From ' || P_Tbl_Dtl_Nm || ' Where ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || ')
                                                                  , Disc_Amt_Dtl = (Select SUM((NVL(DIS_AMT_DTL,0)+NVL(DIS_AMT_DTL2,0)+NVL(DIS_AMT_DTL3,0))*NVL(I_QTY,0)) 
                                                                     From ' || P_Tbl_Dtl_Nm || ' Where ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || ')                              
           Where ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
      Exception
         When No_Data_Found Then
            Null;
         When Others Then
            P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
            P_Err_No    := 20376;
            Goto Rtn_Rslt;
      End;


      Begin
         Execute Immediate ' UPDATE  ' || P_Tbl_Dtl_Nm || '  Set Dis_Amt = Nvl(Dis_Amt_Mst,0)+NVL(Dis_Amt_Dtl,0)+NVL(Dis_Amt_Dtl2,0)+NVL(Dis_Amt_Dtl3,0)
           Where ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
      Exception
         When No_Data_Found Then
            Null;
         When Others Then
            P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
            P_Err_No    := 20377;
            Goto Rtn_Rslt;
      End;

      Begin
         -- Update Ias_Bill_Mst Set Disc_Amt = Nvl(Disc_Amt_Mst,0)+Nvl(Disc_Amt_Dtl,0) Where Bill_Ser=P_DOC_SER;
         Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' SET Disc_Amt=Round((nvl(disc_amt_mst,0)+nvl(disc_amt_dtl,0)+nvl(Disc_Amt_Aftr_Vat,0)),' || V_No_Of_Decimal || ') 
                        WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
      Exception
         When No_Data_Found Then
            Null;
         When Others Then
            P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
            P_Err_No    := 20378;
            Goto Rtn_Rslt;
      End;
   Else
      Begin
         Execute Immediate
               ' UPDATE  '|| P_Tbl_Dtl_Nm|| ' a Set dis_amt_mst =(Select (nvl(disc_amt_mst,0)/nvl('|| P_Fld_Mst_Amt|| ',0))*nvl(a.i_price,0) 
                                                        From '|| P_Tbl_Mst_Nm|| ' Where '|| P_Fld_Doc_Ser|| '=a.'|| P_Fld_Doc_Ser|| '
                                                                                        and '|| P_Fld_Doc_Ser|| '='|| P_Doc_Ser|| '),
                                                  dis_amt =(Select ((nvl(disc_amt_mst,0)/nvl('|| P_Fld_Mst_Amt|| ',0))*nvl(a.i_price,0)) + nvl(a.dis_amt_dtl,0)+ nvl(a.dis_amt_dtl2,0)+ nvl(a.dis_amt_dtl3,0)
                                                         From '|| P_Tbl_Mst_Nm|| ' Where '|| P_Fld_Doc_Ser|| '=a.'|| P_Fld_Doc_Ser|| '
                                                                                        and '|| P_Fld_Doc_Ser|| '='|| P_Doc_Ser|| ' ) 
                WHERE '|| P_Fld_Doc_Ser|| '='|| P_Doc_Ser;
      Exception
         When No_Data_Found Then
            Null;
         When Others Then
            P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
            P_Err_No    := 20379;
            Goto Rtn_Rslt;
      End;



      Begin
         Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' m Set Disc_Amt_Dtl=(select SUM((NVL(DIS_AMT_DTL,0)+NVL(DIS_AMT_DTL2,0)+NVL(DIS_AMT_DTL3,0))*NVL(I_QTY,0))
                                                                                           from ' || P_Tbl_Dtl_Nm || ' d 
                                                                                             where m.' || P_Fld_Doc_Ser || '=d.' || P_Fld_Doc_Ser || ' )
                 Where M.' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
      Exception
         When No_Data_Found Then
            Null;
         When Others Then
            P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
            P_Err_No    := 20380;
            Goto Rtn_Rslt;
      End;

      Begin
         Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' SET Disc_Amt=Round(nvl(disc_amt_mst,0)+nvl(disc_amt_dtl,0),' || V_No_Of_Decimal || ') 
                      WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
      Exception
         When No_Data_Found Then
            Null;
         When Others Then
            P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
            P_Err_No    := 20381;
            Goto Rtn_Rslt;
      End;
   End If;

   --##--------------------------------------------------------------------------------------------##--
   --## VAT_AMT_BFR_DIS
   Begin
      Execute Immediate ' UPDATE  ' || P_Tbl_Dtl_Nm || ' SET Vat_Amt_Bfr_Dis= (Nvl(i_price,0)*Nvl(vat_per,0))/100
                               WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
   Exception
      When No_Data_Found Then
         Null;
      When Others Then
         P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
         P_Err_No    := 20382;
         Goto Rtn_Rslt;
   End;

   --##---------------------------------------------------------------------------------------------------------------------------------------##--
   --## VAT_AMT_AFTR_DIS
   Begin
      Execute Immediate ' UPDATE  ' || P_Tbl_Dtl_Nm || ' SET Vat_Amt_Aftr_Dis = ((Nvl(i_price,0)-(Nvl(Dis_Amt_Dtl,0)+Nvl(Dis_Amt_Dtl2,0)+Nvl(Dis_Amt_Dtl3,0)+Nvl(Dis_Amt_Mst,0)))*Nvl(vat_per,0))/100          
           WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
   Exception
      When No_Data_Found Then
         Null;
      When Others Then
         P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
         P_Err_No    := 20383;
         Goto Rtn_Rslt;
   End;

  --##---------------------------------------------------------------------------------------------------------------------------------------##--
  --####################--
  <<RTN_RSLT>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then      
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := nvl(P_Pkg_Nm,'Ars_Api_Chk_Pkg.Updt_Bill_Disc_Prc');
      Return;
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;      
   End If;
--####################--

Exception
   When Others Then
      P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
      P_Err_No    := 20384;
      P_Pkg_Nm    := 'Ars_Api_Chk_Pkg.Updt_Bill_Disc_Prc';
End Updt_Bill_Disc_Prc_OLD;
--##-----------------------------------------------------------------------------------------------------##--
Procedure Updt_Bill_Disc_Prc (P_Doc_Typ             In     Number
                             ,P_Pst_Typ             In     Number
                             ,P_Doc_Ser             In     Number
                             ,P_Use_Vat             In     Number Default Null
                             ,P_Bill_Doc_Type       In     Number Default Null
                             ,P_Clc_Vat_Price_Typ   In     Number Default Null
                             ,P_Clc_Typ_No_Tax      In     Number Default Null
                             ,P_CALC_TAX_AUTO_FLG   In     Number Default 0
                             ,P_Fld_Doc_Ser         In     Varchar2
                             ,P_Tbl_Mvmnt_Nm        In     Varchar2
                             ,P_Tbl_Mst_Nm          In     Varchar2
                             ,P_Tbl_Dtl_Nm          In     Varchar2
                             ,P_Fld_Mst_Amt         In     Varchar2
                             ,P_DIFF_AMT            In     Number Default Null
                             ,P_Lng_No              In     Number Default 1
                             ,P_Msg_Txt                Out Varchar2
                             ,P_Err_No                 Out Varchar2
                             ,P_Pkg_Nm                 Out Varchar2)
Is
   V_Bill_Amt                      Number;
   V_Bill_Amt_Vat                  Number;
   V_SUM_Bill_Amt                  Number:=0;
   V_SUM_Bill_Amt_Vat              Number:=0;
   V_Discount                      Number;
   V_Disc_Amt_Mst                  Number;
   V_Disc_Amt                      Number;
   V_Disc_Amt_Dtl                  Number;
   V_Disc_Amt_Mst_Vat              Number;   
   V_Sum_Dis_Amt_Dtl_Vat           Number;
   V_Sum_Dis_Amt_Dtl               Number;
   V_No_Of_Decimal                 Number;
   V_Show_Dis_Per_Item             Number;
   Calc_Si_Disc_Without_Itm_Disc   Number;
   V_Clc_Tax_Dscnt2                NUMBER;
   V_Clc_Tax_Dscnt3                NUMBER;
   V_SQL                           VARCHAR2(4000);
   V_CHEQUE_AMT                    NUMBER;
   --------
     V_i_price     number;
     V_i_price_vat  number;
     V_vat_per   number;
     V_Dis_Amt_Dtl  number;
     V_Dis_Amt_Dtl2  number;
     V_Dis_Amt_Dtl3 number;
     V_Dis_Amt_Dtl_vat number;
     V_Dis_Amt_Dtl2_vat number;
     V_Dis_Amt_Dtl3_vat  number;
     V_dis_per    number;
     V_dis_per2   number;
     V_dis_per3   number;
     V_Dis_Amt_Mst_Vat number;
     V_Dis_Amt_Mst number;
     V_Dis_Amt number;
     V_Vat_Amt_Dis_Dtl_Vat  number; 
     V_Vat_Amt_Dis_Dtl2_Vat number;
     V_Vat_Amt_Dis_Dtl3_Vat number;
     V_Vat_Amt_Dis_Mst_Vat number;
     V_Vat_Amt_Bfr_Dis   number;
     V_Vat_Amt_Aftr_Dis   number;
   -----------
   V_SUM_Disc_Amt_Dtl    number:=0;
   V_SUM_Disc_Amt_MST    number:=0;
   V_Disc_Amt_M         number:=0;
   V_Clc_Typ_No         NUMBER(5);
   V_AMT_DIFF          number:=NVL(P_DIFF_AMT,0.1);
   -----------
Begin
   If P_Clc_Typ_No_Tax Is Null And Nvl (P_Use_Vat, 0) = 1 Then
      P_Err_No    := 20497;
      P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 1601) || ' P_CLC_TYP_NO_TAX ';
      Goto Rtn_Rslt;
   End If;
   --------------------------------------------------------------------------
   --##PARA
   Select Nvl (Calc_Si_Disc_Without_Itm_Disc, 0), Nvl (No_Of_Decimal_Ar, 2), Nvl (Show_Disc_Per_Items_Ar, 0)
   ,NVL(Clc_Tax_Dscnt2,0),NVL(Clc_Tax_Dscnt3,0)
     Into Calc_Si_Disc_Without_Itm_Disc, V_No_Of_Decimal, V_Show_Dis_Per_Item
     ,V_Clc_Tax_Dscnt2,V_Clc_Tax_Dscnt3
     From Ias_Para_Ar;

   --#----------------------------------------------------------------------------------------------------------------------------------------##---
   Execute Immediate 'SELECT NVL(SUM((NVL(I_QTY,0) * NVL(I_PRICE_VAT,0))),0) 
                         FROM ' || P_Tbl_Dtl_Nm || '
                         WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser Into  V_Bill_Amt_Vat;  
                         
   Execute Immediate 'SELECT  '||P_Fld_Mst_Amt||', nvl(disc_amt_Mst,0) ,NVL(disc_amt_mst_vat,0),NVL(Disc_Amt,0),NVL(Disc_Amt_DTL,0)
                       FROM ' || P_Tbl_Mst_Nm || ' 
                       WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser Into V_Bill_Amt, V_Disc_Amt_Mst, V_Disc_Amt_Mst_Vat,V_Disc_Amt,V_Disc_Amt_DTL;
                         
   --#----------------------------------------------------------------------------------------------------------------------------------------##---
   If Nvl (P_Clc_Vat_Price_Typ, 0) = 2 And NVL(P_CALC_TAX_AUTO_FLG,0)=1 And Nvl (P_Use_Vat, 0) = 1  Then         
      V_Disc_Amt_Mst_Vat := Case when nvl(V_Disc_Amt_Mst_Vat,0) =0 Then Nvl (V_Disc_Amt_Mst, 0) Else Nvl (V_Disc_Amt_Mst_Vat, 0) End;                                   
   End If;
   --#----------------------------------------------------------------------------------------------------------------------------------------##---          
          
   V_SQL:=' select 
                  rowid row_id
                 ,i_code
                 ,NVL(i_qty,0) i_qty      
                 ,NVL(free_qty,0)free_qty  
                 ,NVL(p_size,1) p_size   
                 ,NVL(i_price,0)i_price 
                 ,NVL(i_price_vat,0) i_price_vat
                 ,NVL(vat_per,0)      vat_per
                 ,NVL(Dis_Amt_Dtl,0)  Dis_Amt_Dtl
                 ,NVL(Dis_Amt_Dtl2,0) Dis_Amt_Dtl2
                 ,NVL(Dis_Amt_Dtl3,0) Dis_Amt_Dtl3
                 ,NVL(Dis_Amt_Dtl_vat,0) Dis_Amt_Dtl_vat
                 ,NVL(Dis_Amt_Dtl2_vat,0) Dis_Amt_Dtl2_vat
                 ,NVL(Dis_Amt_Dtl3_vat,0) Dis_Amt_Dtl3_vat
                 ,NVL(dis_per,0) dis_per
                 ,NVL(dis_per2,0) dis_per2
                 ,NVL(dis_peR3,0) dis_peR3
                 ,NVL(Dis_Amt_Mst_Vat,0) Dis_Amt_Mst_Vat
                 ,NVL(Dis_Amt_Mst,0)  Dis_Amt_Mst
                 ,NVL(Dis_Amt,0) Dis_Amt
                 ,NVL(Vat_Amt_Dis_Dtl_Vat,0) Vat_Amt_Dis_Dtl_Vat 
                 ,NVL(Vat_Amt_Dis_Dtl2_Vat,0) Vat_Amt_Dis_Dtl2_Vat
                 ,NVL(Vat_Amt_Dis_Dtl3_Vat,0) Vat_Amt_Dis_Dtl3_Vat
                 ,NVL(Vat_Amt_Dis_Mst_Vat,0) Vat_Amt_Dis_Mst_Vat
                 ,NVL(Vat_Amt_Bfr_Dis,0) Vat_Amt_Bfr_Dis
                 ,NVL(Vat_Amt_Aftr_Dis ,0)  Vat_Amt_Aftr_Dis
           FROM ' || P_Tbl_DTL_Nm || ' 
              WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser ;
              
  Execute Immediate V_Sql Bulk Collect Into V_Blk_DISC ;                   
  For I In 1..V_Blk_DISC.Count
  Loop        
         V_i_price_vat          :=V_Blk_DISC(I).i_price_vat;
         V_I_Price   := V_Blk_DISC(I).I_Price;
         V_Vat_Per   := V_Blk_DISC(I).Vat_Per;       
         V_Dis_Amt_Dtl          :=V_Blk_DISC(I).Dis_Amt_Dtl;
         V_Dis_Amt_Dtl2         :=V_Blk_DISC(I).Dis_Amt_Dtl2;
         V_Dis_Amt_Dtl3         :=V_Blk_DISC(I).Dis_Amt_Dtl3;
         V_Dis_Amt_Dtl_vat      :=V_Blk_DISC(I).Dis_Amt_Dtl_vat;
         V_Dis_Amt_Dtl2_vat     :=V_Blk_DISC(I).Dis_Amt_Dtl2_vat;
         V_Dis_Amt_Dtl3_vat     :=V_Blk_DISC(I).Dis_Amt_Dtl3_vat;
         V_dis_per              :=V_Blk_DISC(I).dis_per;
         V_dis_per2             :=V_Blk_DISC(I).dis_per2;
         V_dis_per3              :=V_Blk_DISC(I).dis_peR3;
         V_Dis_Amt_Mst_Vat      :=V_Blk_DISC(I).Dis_Amt_Mst_Vat;
         V_Dis_Amt_Mst          :=V_Blk_DISC(I).Dis_Amt_Mst;
         V_Dis_Amt              :=V_Blk_DISC(I).Dis_Amt;
         V_Vat_Amt_Dis_Dtl_Vat  :=V_Blk_DISC(I).Vat_Amt_Dis_Dtl_Vat; 
         V_Vat_Amt_Dis_Dtl2_Vat :=V_Blk_DISC(I).Vat_Amt_Dis_Dtl2_Vat;
         V_Vat_Amt_Dis_Dtl3_Vat :=V_Blk_DISC(I).Vat_Amt_Dis_Dtl3_Vat;
         V_Vat_Amt_Dis_Mst_Vat  :=V_Blk_DISC(I).Vat_Amt_Dis_Mst_Vat;
         V_Vat_Amt_Bfr_Dis      :=V_Blk_DISC(I).Vat_Amt_Bfr_Dis;
         V_Vat_Amt_Aftr_Dis     :=V_Blk_DISC(I).Vat_Amt_Aftr_Dis;                  
     --====================================================================================--            
      If Nvl (P_Clc_Vat_Price_Typ, 0) = 2 Then
          If NVL(P_CALC_TAX_AUTO_FLG,0)=1 THEN
            V_dis_amt_dtl_vat := Case when nvl(V_dis_amt_dtl_vat,0) =0 Then Nvl (V_dis_amt_dtl, 0) Else Nvl (V_dis_amt_dtl_vat, 0) End;
            V_dis_amt_dtl2_vat := Case when nvl(V_dis_amt_dtl2_vat,0) =0 Then Nvl (V_dis_amt_dtl2, 0) Else Nvl (V_dis_amt_dtl2_vat, 0) End;
            V_dis_amt_dtl3_vat := Case when nvl(V_dis_amt_dtl3_vat,0) =0 Then Nvl (V_dis_amt_dtl3, 0) Else Nvl (V_dis_amt_dtl3_vat, 0) End;            
          End If;
        
      
         V_I_PRICE:= (nvl(V_I_PRICE_VAT,0) /((Nvl(V_Vat_Per,0)/100)+1)) ;     
         V_Dis_Amt_Dtl:= (nvl(V_dis_amt_dtl_vat,0) /((Nvl(V_Vat_Per,0)/100)+1)) ;
         ---------------------------------
         IF nvl(V_Dis_Amt_Dtl2_Vat,0)>0 And (nvl(V_i_price_vat,0)-Nvl(V_Dis_Amt_Dtl_vat,0))>0  AND  Nvl(V_i_price_vat,0) > 0 THEN 
            IF V_Clc_Tax_Dscnt2=1 THEN
              V_Dis_Amt_Dtl2:=NVL(V_Dis_Amt_Dtl2_Vat,0) /((Nvl(V_Vat_Per,0)/100)+1);
            ELSE
              V_Dis_Amt_Dtl2:=V_Dis_Amt_Dtl2_Vat;
            END IF;                
         ELSE
           V_Dis_Amt_Dtl2:=0;
         END IF;
        ---------------------------------
         IF nvl(V_Dis_Amt_Dtl3_Vat,0)>0 And (nvl(V_i_price_Vat,0)-Nvl(V_Dis_Amt_Dtl_Vat,0)-Nvl(V_Dis_Amt_Dtl2_Vat,0))> 0 AND  Nvl(V_i_price_vat,0) > 0 THEN 
            IF V_Clc_Tax_Dscnt3=1 THEN
              V_Dis_Amt_Dtl3:=NVL(V_Dis_Amt_Dtl3_Vat,0) /((Nvl(V_Vat_Per,0)/100)+1);
            ELSE
              V_Dis_Amt_Dtl3:=V_Dis_Amt_Dtl3_Vat;
            END IF;                
         ELSE
           V_Dis_Amt_Dtl3:=0;
         END IF;
                                              
      END IF;
      --====================================================================================--                    
       IF  Nvl(V_i_price,0) > 0 THEN 
         -- V_dis_per:=(nvl(V_dis_amt_dtl,0)/nvl(V_i_price,0))*100;
           
          If nvl(V_dis_per,0)>0 and nvl(V_dis_amt_dtl,0)=0 Then
             V_dis_amt_dtl:=(nvl(V_dis_per,0)/100)*nvl(V_i_price,0);
           ElsIf nvl(V_dis_per,0)=0 and nvl(V_dis_amt_dtl,0)>0 Then   
             V_dis_per:=(nvl(V_dis_amt_dtl,0)/nvl(V_i_price,0))*100;          
          End If;
             
          
          IF (nvl(V_i_price,0)-Nvl(V_dis_amt_dtl,0))>0 THEN
            V_dis_per2:=(nvl(V_dis_amt_dtl2,0)/(nvl(V_i_price,0)-Nvl(V_dis_amt_dtl,0)))*100 ;
          END IF;
          
          IF (nvl(V_i_price,0)-Nvl(V_dis_amt_dtl,0)-Nvl(V_dis_amt_dtl2,0))>0 THEN  
            V_dis_per3:=(nvl(V_dis_amt_dtl3,0)/(nvl(V_i_price,0)-Nvl(V_dis_amt_dtl,0)-Nvl(V_dis_amt_dtl2,0)))*100;
          END IF;
          
           IF ABS( Nvl(V_dis_per,0)-((nvl(V_dis_amt_dtl,0)/nvl(V_i_price,0))*100) )>=V_AMT_DIFF THEN
                  P_Err_No := 20665;
                  P_Msg_Txt := 'DIS_PER IN '|| P_Tbl_Dtl_Nm ||' INCORRECT'
                                           ||chr(10)||'DIS_PER ='||Round(V_dis_per,6)
                                           ||chr(10)||'CORRECT DIS_PER ='||Round(((nvl(V_dis_amt_dtl,0)/nvl(V_i_price,0))*100),6)                                           
                                           ||chr(10)||'I_CODE ='||V_Blk_DISC(I).I_CODE;
                  Goto Rtn_Rslt;           
           END IF;                     
          
        END IF;
         
       --## if calc tax and discont is not auto 
      IF NVL(P_CALC_TAX_AUTO_FLG,0)=0 THEN
         ----------------------------------------------
           --## CHECK FIELD dis_amt_dtl
           IF  Nvl(V_Blk_DISC(I).I_qty,0)=0 Then
              V_dis_amt_dtl:=0;
              V_dis_amt_dtl_Vat:=0;
           ELSIF ABS(Nvl(V_dis_amt_dtl,0)-Nvl(V_Blk_DISC(I).dis_amt_dtl,0))>=V_AMT_DIFF THEN
                  P_Err_No := 20498;
                  P_Msg_Txt := 'DIS_AMT_DTL IN '|| P_Tbl_Dtl_Nm ||' INCORRECT'
                                           ||chr(10)||'DIS_AMT_DTL ='||Round(V_Blk_DISC(I).dis_amt_dtl,6)
                                           ||chr(10)||'CORRECT DIS_AMT_DTL ='||Round(V_dis_amt_dtl,6)
                                           ||chr(10)||'DIFF ='||Round(ABS((NVL(V_dis_amt_dtl,0))-(NVL(V_Blk_DISC(I).dis_amt_dtl,0))),6)
                                           ||chr(10)||'I_CODE ='||V_Blk_DISC(I).I_CODE;
                  Goto Rtn_Rslt;
           ELSE 
             V_dis_amt_dtl:= V_Blk_DISC(I).dis_amt_dtl;  
           END IF;
           ----------------------------------------------
             --## CHECK FIELD I_PRICE
              IF ABS(Nvl(V_I_PRICE,0)-Nvl(V_Blk_DISC(I).I_PRICE,0))>=V_AMT_DIFF THEN
                      P_Err_No := 20499;
                      P_Msg_Txt := 'I_PRICE IN '|| P_Tbl_Dtl_Nm ||' INCORRECT'
                                               ||chr(10)||'I_PRICE ='||Round(V_Blk_DISC(I).I_PRICE,6)
                                               ||chr(10)||'CORRECT I_PRICE ='||Round(V_I_PRICE,6)
                                               ||chr(10)||'DIFF ='||Round(ABS((NVL(V_I_PRICE,0))-(NVL(V_Blk_DISC(I).I_PRICE,0))),6)
                                               ||chr(10)||'I_CODE ='||V_Blk_DISC(I).I_CODE;
                      Goto Rtn_Rslt;
               ELSE 
                 V_I_PRICE:= V_Blk_DISC(I).I_PRICE;  
               END IF;
                 ----------------------------------------------
             --## CHECK FIELD V_dis_per
              IF  Nvl(V_Blk_DISC(I).I_qty,0)=0 Then
                  V_dis_per:=0;                  
              ELSIF ABS(Nvl(V_dis_per,0)-Nvl(V_Blk_DISC(I).dis_per,0))>=V_AMT_DIFF THEN
                      P_Err_No := 20500;
                      P_Msg_Txt := 'DIS_PER IN '|| P_Tbl_Dtl_Nm ||' INCORRECT'
                                               ||chr(10)||'DIS_PER ='||Round(V_Blk_DISC(I).DIS_PER,6)
                                               ||chr(10)||'CORRECT DIS_PER ='||Round(V_DIS_PER,6)
                                               ||chr(10)||'DIFF ='||Round(ABS((NVL(V_DIS_PER,0))-(NVL(V_Blk_DISC(I).DIS_PER,0))),6)
                                               ||chr(10)||'I_CODE ='||V_Blk_DISC(I).I_CODE;
                      Goto Rtn_Rslt;
               ELSE 
                 V_DIS_PER:= V_Blk_DISC(I).DIS_PER;  
               END IF;
      END IF;
      -----------------------------------------------------------------------------
       If Nvl (Ys_Tax_Pkg.Get_Clc_Tax_Typ (P_Clc_Typ_No => P_Clc_Typ_No_Tax), 0) = 0 AND  Nvl(V_i_price,0) > 0 AND Nvl (P_Clc_Vat_Price_Typ, 0) = 2 Then    
             V_Vat_Amt_Dis_Dtl_Vat  := Nvl(V_dis_amt_dtl_Vat,0)-Nvl(V_dis_amt_dtl,0);
             V_Vat_Amt_Dis_Dtl2_Vat := Nvl(V_dis_amt_dtl2_Vat,0)-Nvl(V_dis_amt_dtl2,0);
             V_Vat_Amt_Dis_Dtl3_Vat := Nvl(V_dis_amt_dtl3_Vat,0)-Nvl(V_dis_amt_dtl3,0);
       Else
             V_Vat_Amt_Dis_Dtl_Vat  :=0;
             V_Vat_Amt_Dis_Dtl2_Vat := 0;
             V_Vat_Amt_Dis_Dtl3_Vat := 0;
       END IF;
      -----------------------------------------------------------------------------
       V_SUM_Disc_Amt_Dtl:=NVL(V_SUM_Disc_Amt_Dtl,0)+((NVL(V_DIS_AMT_DTL,0)+NVL(V_DIS_AMT_DTL2,0)+NVL(V_DIS_AMT_DTL3,0))*V_Blk_DISC(I).I_QTY);
       V_SUM_Bill_Amt     :=NVL(V_SUM_Bill_Amt,0)+(NVL(V_I_PRICE,0)*V_Blk_DISC(I).I_QTY);
       V_SUM_Bill_Amt_VAT     :=NVL(V_SUM_Bill_Amt_VAT,0)+(NVL(V_I_PRICE_VAT,0)*V_Blk_DISC(I).I_QTY);
       -----------------------------------------------------------------------------
            BEGIN  
                Execute Immediate ' UPDATE ' || P_Tbl_Dtl_Nm || ' SET 
                                                             i_price              ='||V_i_price||',
                                                             i_price_vat          ='||V_i_price_vat||',
                                                             vat_per              ='||V_vat_per||',
                                                             Dis_Amt_Dtl          ='||V_Dis_Amt_Dtl||',
                                                             Dis_Amt_Dtl2         ='||V_Dis_Amt_Dtl2||',
                                                             Dis_Amt_Dtl3         ='||V_Dis_Amt_Dtl3||',
                                                             Dis_Amt_Dtl_vat      ='||V_Dis_Amt_Dtl_vat||',
                                                             Dis_Amt_Dtl2_vat     ='||V_Dis_Amt_Dtl2_vat||',
                                                             Dis_Amt_Dtl3_vat     ='||V_Dis_Amt_Dtl3_vat||',
                                                             dis_per              ='||V_dis_per||',
                                                             dis_per2             ='||V_dis_per2||',
                                                             dis_per3             ='||V_dis_peR3||',
                                                             Dis_Amt_Mst_Vat      ='||V_Dis_Amt_Mst_Vat||',
                                                             Dis_Amt_Mst          ='||V_Dis_Amt_Mst||',
                                                             Dis_Amt              ='||V_Dis_Amt||',
                                                             Vat_Amt_Dis_Dtl_Vat  ='||V_Vat_Amt_Dis_Dtl_Vat||', 
                                                             Vat_Amt_Dis_Dtl2_Vat ='||V_Vat_Amt_Dis_Dtl2_Vat||',
                                                             Vat_Amt_Dis_Dtl3_Vat ='||V_Vat_Amt_Dis_Dtl3_Vat||',
                                                             Vat_Amt_Dis_Mst_Vat  ='||V_Vat_Amt_Dis_Mst_Vat||',
                                                             Vat_Amt_Bfr_Dis      ='||V_Vat_Amt_Bfr_Dis||',
                                                             Vat_Amt_Aftr_Dis     ='||V_Vat_Amt_Aftr_Dis||'                                                                                
                                                         WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || '
                                                            AND I_CODE='''||V_Blk_DISC(I).I_CODE||'''
                                                            AND ROWID='''||V_Blk_DISC(I).ROW_ID||'''   ';
            Exception
               When No_Data_Found Then
                  Null;
               When Others Then
                  P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20501;
                  Goto Rtn_Rslt;
            End;
  END LOOP;
   V_SUM_Bill_Amt:=ROUND(V_SUM_Bill_Amt,V_No_Of_Decimal);
   ---------------------------------------------------------
   IF NVL(P_CALC_TAX_AUTO_FLG,0)=0 THEN
     --## CHECK FIELD BILL_AMT
      IF ABS(Nvl(V_SUM_Bill_Amt,0)-Nvl(V_BILL_AMT,0))>=V_AMT_DIFF THEN
              P_Err_No := 20502;
              P_Msg_Txt := ''||P_Fld_Mst_Amt||' IN '|| P_Tbl_MST_Nm ||' INCORRECT'
                                       ||chr(10)||' '||P_Fld_Mst_Amt||' ='||Round(V_BILL_AMT,6)
                                       ||chr(10)||'CORRECT '||P_Fld_Mst_Amt||' ='||Round(V_SUM_Bill_Amt,6)
                                       ||chr(10)||'DIFF ='||Round(ABS((NVL(V_BILL_AMT,0))-(NVL(V_SUM_Bill_Amt,0))),6);                                               
              Goto Rtn_Rslt;              
       END IF; 
   ELSE
     V_BILL_AMT:= V_SUM_Bill_Amt;
     V_Bill_Amt_Vat:= V_SUM_Bill_Amt_VAT;           
   END IF;
  ---------------------------------------------------------
      Execute Immediate V_Sql Bulk Collect Into V_Blk_DISC ;                   
      For I In 1..V_Blk_DISC.Count
      Loop
       IF  Nvl (P_Clc_Vat_Price_Typ, 0) = 2 AND NVL(V_Bill_Amt_Vat,0)>0 THEN
         V_Dis_Amt_Mst_Vat := ( Nvl(V_Disc_Amt_Mst_Vat, 0)/ V_Bill_Amt_Vat )*Nvl(V_Blk_DISC(I).i_price_vat,0);
         V_Dis_Amt_Mst     := V_Dis_Amt_Mst_Vat/((Nvl(V_Blk_DISC(I).Vat_Per,0)/100)+1);
         V_Vat_Amt_Dis_Mst_Vat := V_Dis_Amt_Mst_Vat- V_Dis_Amt_Mst;
         V_Dis_Amt := Nvl(V_Dis_Amt_Mst,0)+NVL(V_Blk_DISC(I).Dis_Amt_Dtl,0)+NVL(V_Blk_DISC(I).Dis_Amt_Dtl2,0)+NVL(V_Blk_DISC(I).Dis_Amt_Dtl3,0);
         V_SUM_Disc_Amt_MST:=NVL(V_SUM_Disc_Amt_MST,0)+(NVL(V_Dis_Amt_Mst,0)*V_Blk_DISC(I).I_QTY);
       ELSIF  Nvl (P_Clc_Vat_Price_Typ, 1) = 1 AND NVL(V_Bill_Amt,0)>0 THEN
         V_Dis_Amt_Mst_Vat:=0;
         V_dis_amt_mst := (nvl(V_disc_amt_mst,0)/nvl(V_Bill_Amt,0))*nvl(V_Blk_DISC(I).i_price,0);
         V_Vat_Amt_Dis_Mst_Vat:=0;
         V_Dis_Amt := Nvl(V_Dis_Amt_Mst,0)+NVL(V_Blk_DISC(I).Dis_Amt_Dtl,0)+NVL(V_Blk_DISC(I).Dis_Amt_Dtl2,0)+NVL(V_Blk_DISC(I).Dis_Amt_Dtl3,0);
         V_SUM_Disc_Amt_MST:=V_disc_amt_mst;
       ELSE
         V_Dis_Amt_Mst_Vat:=V_Blk_DISC(I).Dis_Amt_Mst_Vat;
         V_dis_amt_mst := V_Blk_DISC(I).dis_amt_mst;
         V_Vat_Amt_Dis_Mst_Vat:=V_Blk_DISC(I).Vat_Amt_Dis_Mst_Vat;
         V_Dis_Amt := V_Blk_DISC(I).Dis_Amt;
       END IF;       
         ----------------------------------------------
             --## CHECK FIELD Dis_Amt
       IF NVL(P_CALC_TAX_AUTO_FLG,0)=0 THEN       
          IF ABS(Nvl(V_Dis_Amt,0)-Nvl(V_Blk_DISC(I).Dis_Amt,0))>=V_AMT_DIFF THEN
                  P_Err_No := 20503;
                  P_Msg_Txt := 'Dis_Amt IN '|| P_Tbl_Dtl_Nm ||' INCORRECT'
                                           ||chr(10)||'Dis_Amt ='||Round(V_Blk_DISC(I).Dis_Amt,6)
                                           ||chr(10)||'CORRECT Dis_Amt ='||Round(V_Dis_Amt,6)
                                           ||chr(10)||'DIFF ='||Round(ABS((NVL(V_Dis_Amt,0))-(NVL(V_Blk_DISC(I).Dis_Amt,0))),6)
                                           ||chr(10)||'I_CODE ='||V_Blk_DISC(I).I_CODE;
                  Goto Rtn_Rslt;
           ELSE 
             V_Dis_Amt:= V_Blk_DISC(I).Dis_Amt;  
           END IF;
           
           IF ABS(Nvl(V_Dis_Amt_Mst_Vat,0)-Nvl(V_Blk_DISC(I).Dis_Amt_Mst_Vat,0))>=V_AMT_DIFF AND Nvl (P_Clc_Vat_Price_Typ, 0) = 2 THEN
                  P_Err_No := 20645;
                  P_Msg_Txt := 'DIS_AMT_MST_VAT IN '|| P_Tbl_Dtl_Nm ||' INCORRECT'
                                           ||chr(10)||'DIS_AMT_MST_VAT ='||Round(V_Blk_DISC(I).Dis_Amt_Mst_Vat,6)
                                           ||chr(10)||'CORRECT DIS_AMT_MST_VAT ='||Round(V_Dis_Amt_Mst_Vat,6)
                                           ||chr(10)||'DIFF ='||Round(ABS((NVL(V_Dis_Amt_Mst_Vat,0))-(NVL(V_Blk_DISC(I).Dis_Amt_Mst_Vat,0))),6)
                                           ||chr(10)||'I_CODE ='||V_Blk_DISC(I).I_CODE;
                  Goto Rtn_Rslt;
           ELSE 
             V_DIS_AMT_MST_VAT:= V_Blk_DISC(I).Dis_Amt_Mst_Vat;  
           END IF; 
           
           
           IF ABS(Nvl(V_dis_amt_mst,0)-Nvl(V_Blk_DISC(I).dis_amt_mst,0))>=V_AMT_DIFF THEN
                  P_Err_No := 20646;
                  P_Msg_Txt := 'DIS_AMT_MST IN '|| P_Tbl_Dtl_Nm ||' INCORRECT'
                                           ||chr(10)||'DIS_AMT_MST ='||Round(V_Blk_DISC(I).DIS_AMT_MST,6)
                                           ||chr(10)||'CORRECT DIS_AMT_MST ='||Round(V_DIS_AMT_MST,6)
                                           ||chr(10)||'DIFF ='||Round(ABS((NVL(V_DIS_AMT_MST,0))-(NVL(V_Blk_DISC(I).DIS_AMT_MST,0))),6)
                                           ||chr(10)||'I_CODE ='||V_Blk_DISC(I).I_CODE;
                  Goto Rtn_Rslt;
           ELSE 
             V_DIS_AMT_MST:= V_Blk_DISC(I).DIS_AMT_MST;  
           END IF;  
       END IF;    
       
       
       V_Vat_Amt_Bfr_Dis:= (Nvl(V_Blk_DISC(I).i_price,0)*Nvl(V_Blk_DISC(I).vat_per,0))/100;
       V_Vat_Amt_Aftr_Dis := ((Nvl(V_Blk_DISC(I).i_price,0)-(Nvl(V_Blk_DISC(I).Dis_Amt_Dtl,0)+Nvl(V_Blk_DISC(I).Dis_Amt_Dtl2,0)+Nvl(V_Blk_DISC(I).Dis_Amt_Dtl3,0)+Nvl(V_Dis_Amt_Mst,0)))*Nvl(V_Blk_DISC(I).vat_per,0))/100;
       
        BEGIN  
            Execute Immediate ' UPDATE ' || P_Tbl_Dtl_Nm || ' SET                                                             
                                                         Dis_Amt_Mst_Vat      ='||V_Dis_Amt_Mst_Vat||',
                                                         Dis_Amt_Mst          ='||V_Dis_Amt_Mst||',
                                                         Dis_Amt              ='||V_Dis_Amt||',                                                             
                                                         Vat_Amt_Dis_Mst_Vat  ='||V_Vat_Amt_Dis_Mst_Vat||',
                                                         Vat_Amt_Bfr_Dis      ='||V_Vat_Amt_Bfr_Dis||',
                                                         Vat_Amt_Aftr_Dis     ='||V_Vat_Amt_Aftr_Dis||'                                                                                
                                                     WHERE  ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser || '
                                                        AND I_CODE='''||V_Blk_DISC(I).I_CODE||'''
                                                        AND ROWID='''||V_Blk_DISC(I).ROW_ID||'''   ';
        Exception
           When No_Data_Found Then
              Null;
           When Others Then
              P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
              P_Err_No    := 20504;
              Goto Rtn_Rslt;
        End;
        
      END LOOP;
  --##---------------------------------------------------------------------------------------------------------------------------------------##--  
     V_Disc_Amt_M:=NVL(V_SUM_Disc_Amt_MST,0)+NVL(V_SUM_Disc_Amt_Dtl,0);
     V_Disc_Amt_M:=Round(nvl(V_Disc_Amt_M,0),V_No_Of_Decimal) ;
     IF NVL(P_CALC_TAX_AUTO_FLG,0)=0 THEN  
          --## CHECK Disc_Amt_Dtl
          IF ABS(Nvl(V_SUM_Disc_Amt_Dtl,0)-Nvl(V_Disc_Amt_Dtl,0))>=V_AMT_DIFF THEN
                  P_Err_No := 20505;
                  P_Msg_Txt := 'Disc_Amt_Dtl IN '|| P_Tbl_MST_Nm ||' INCORRECT'
                                           ||chr(10)||'Disc_Amt_Dtl ='||Round(V_Disc_Amt_Dtl,6)
                                           ||chr(10)||'CORRECT Disc_Amt_Dtl ='||Round(V_SUM_Disc_Amt_Dtl,6)
                                           ||chr(10)||'DIFF ='||Round(ABS((NVL(V_SUM_Disc_Amt_Dtl,0))-(NVL(V_Disc_Amt_Dtl,0))),6);                                           
                  Goto Rtn_Rslt;
           ELSE 
             V_SUM_Disc_Amt_Dtl:= V_Disc_Amt_Dtl;  
           END IF;
           ----------------------------------------
           --## CHECK DISC_AMT_MST
            IF ABS(Nvl(V_SUM_Disc_Amt_MST,0)-Nvl(V_Disc_Amt_MST,0))>=V_AMT_DIFF THEN
                  P_Err_No := 20506;
                  P_Msg_Txt := 'DISC_AMT_MST IN '|| P_Tbl_MST_Nm ||' INCORRECT'
                                           ||chr(10)||'DISC_AMT_MST ='||Round(V_DISC_AMT_MST,6)
                                           ||chr(10)||'CORRECT DISC_AMT_MST ='||Round(V_SUM_Disc_Amt_MST,6)
                                           ||chr(10)||'DIFF ='||Round(ABS((NVL(V_SUM_Disc_Amt_MST,0))-(NVL(V_DISC_AMT_MST,0))),6);                                           
                  Goto Rtn_Rslt;
           ELSE 
             V_SUM_Disc_Amt_MST:= V_DISC_AMT_MST;  
           END IF;
           ----------------------------------------
           --## CHECK DISC_AMT
            IF ABS(Nvl(V_Disc_Amt_M,0)-Nvl(V_Disc_Amt,0))>=V_AMT_DIFF THEN
                  P_Err_No := 20507;
                  P_Msg_Txt := 'DISC_AMT IN '|| P_Tbl_MST_Nm ||' INCORRECT'
                                           ||chr(10)||'DISC_AMT ='||Round(V_Disc_Amt,6)
                                           ||chr(10)||'CORRECT DISC_AMT ='||Round(V_DISC_AMT_M,6)
                                           ||chr(10)||'DIFF ='||Round(ABS((NVL(V_DISC_AMT_M,0))-(NVL(V_DISC_AMT,0))),6);                                           
                  Goto Rtn_Rslt;
           ELSE 
             V_DISC_AMT_M:= V_DISC_AMT;  
           END IF;           
           
          ---------------------------------------- 
       END IF; 
        Begin
           Execute Immediate ' UPDATE  ' || P_Tbl_Mst_Nm || ' SET 
                                           Disc_Amt_Mst    ='||V_SUM_Disc_Amt_MST||',
                                           Disc_Amt_Mst_VAT='||V_Disc_Amt_Mst_VAT||',
                                           Disc_Amt_Dtl    ='||V_SUM_Disc_Amt_Dtl||',
                                           DISC_AMT        ='||V_DISC_AMT_M||',
                                          '||P_Fld_Mst_Amt||'='||V_BILL_AMT||'
                            WHERE ' || P_Fld_Doc_Ser || '=' || P_Doc_Ser;
        Exception
           When No_Data_Found Then
              Null;
           When Others Then
              P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
              P_Err_No    := 20508;
              Goto Rtn_Rslt;
        End;
   
   --##---------------------------------------------------------------------------------------------------------------------------------------##--
  --####################--
  <<RTN_RSLT>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then      
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := nvl(P_Pkg_Nm,'Ars_Api_Chk_Pkg.Updt_Bill_Disc_Prc_NEW');
      Return;
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;      
   End If;
--####################--

Exception
   When Others Then
      P_Msg_Txt   := 'Errt When Update Disc' ||chr(10) || Sqlerrm;
      P_Err_No    := 20509;
      P_Pkg_Nm    := 'Ars_Api_Chk_Pkg.Updt_Bill_Disc_Prc_NEW';
End Updt_Bill_Disc_Prc;
--##-----------------------------------------------------------------------------------------------------##--
--##-----------------------------------------------------------------------------------------------------##--
    Procedure Chk_Conn_Cst_Col (P_C_Code     In     Customer.C_Code%Type Default Null
                              ,P_Col_No     In     Collerctor.Col_No%Type Default Null
                              ,P_Lng_No     In     Number Default 1
                              ,P_Msg_Txt    Out Varchar2
                              ,P_ERR_NO   Out Varchar2
                              ,P_Pkg_Nm     Out Varchar2)
   Is
      V_Mndtry_Conn_Cst_Col   Number;
      V_Conn_Cst_Multi_Col    Number;
      V_Si_Col_Mandtry        Number;
      V_Cnt                   Number;    
   Begin
      Begin
         Select Nvl (Mndtry_Conn_Cst_Col, 0), Nvl (Conn_Cst_Multi_Col, 0), Nvl (Si_Col_Mandtry, 0)
           Into V_Mndtry_Conn_Cst_Col, V_Conn_Cst_Multi_Col, V_Si_Col_Mandtry
           From Ias_Para_Ar
          Where Rownum <= 1;
      Exception
         When Others Then
            V_Mndtry_Conn_Cst_Col := 0;
      End;
      
      /*
      If V_Mndtry_Conn_Cst_Col = 1 And P_Col_No Is Null And P_C_Code Is Not Null Then
         P_Err_No := 20215;
         P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 1222);
         Goto Rtn_Rslt;
      End If;
      */

      If V_Si_Col_Mandtry = 1 And P_Col_No Is Null Then
         P_Err_No := 20216;
         P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 1222);
         Goto Rtn_Rslt;
      End If;


      If V_Mndtry_Conn_Cst_Col = 1 And P_Col_No Is Not Null And P_C_Code Is Not Null Then
         If V_Conn_Cst_Multi_Col = 0 Then
            Begin
               Select 1
                 Into V_Cnt
                 From Customer
                Where C_Code = P_C_Code And Col_No = P_Col_No And Rownum <= 1;
            Exception
               When Others Then
                  V_Cnt := 0;
            End;
         Elsif V_Conn_Cst_Multi_Col = 1 Then
            Begin
               Select 1
                 Into V_Cnt
                 From Ias_Cst_Col
                Where C_Code = P_C_Code And Col_No = P_Col_No And Rownum <= 1;
            Exception
               When Others Then
                  V_Cnt := 0;
            End;
         End If;

         --------------------------------------------------------------------------------------
         If Nvl (V_Cnt, 0) = 0 Then
            P_Err_No := 20217;
            P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1864) || ' C_CODE=' || P_C_Code || 'Col_No=' || P_Col_No || ' ';
            Goto Rtn_Rslt;
         End If;
      --------------------------------------------------------------------------------------
      End If;
     --####################--
     <<Rtn_Rslt>>
      If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then         
         P_Msg_Txt := NVL(P_Msg_Txt,'Message Number Is Missing');
         P_ERR_NO :=P_Err_No;
         P_Pkg_Nm   :=NVL(P_Pkg_Nm,'Ars_Api_Chk_Pkg.HK_CONN_CST_COL');
         Return;
      End If;
   --####################--
   Exception When Others then
         P_Msg_Txt := 'Error in Chk_Conn_Cst_Col '||sqlerrm;
         P_ERR_NO  := 20403;
         P_Pkg_NM  :='Ars_Api_Chk_Pkg.Chk_Conn_Cst_Col'; 
   End Chk_Conn_Cst_Col;
   --##-----------------------------------------------------------------------------------------------------##--
 Procedure Chk_Sman_Conn_Data (P_Sys_No          In     Number
                             ,P_Doc_Type        In     Number Default Null
                             ,P_Rep_Code        In     Sales_Man.Reprs_Code%Type Default Null
                             ,P_Bill_Doc_Type   In     Number Default Null
                             ,P_W_Code          In     Number Default Null
                             ,P_Cash_No         In     Number Default Null
                             ,P_Cc_Code         In     Varchar2 Default Null
                             ,P_Pj_No           In     Varchar2 Default Null
                             ,P_Actv_No         In     Varchar2 Default Null
                             ,P_Brn_Usr         In     Number   Default Null
                             ,P_Lng_No          In     Number Default 1
                             ,P_Msg_Txt            Out Varchar2
                             ,P_Err_No             Out Varchar2
                             ,P_Pkg_Nm             Out Varchar2)
Is
   V_Cc_Code               Varchar2 (30);
   V_Pj_No                 Varchar2 (30);
   V_Actv_No               Varchar2 (30);
   V_W_Code                Number;
   V_Cash_No               Number;
   V_Cnt                   Number;
   V_Conn_Sman_Wc_Csh_Cc   Number;
   V_Cc_Avail              Number;
   V_Ar_Cst_Type           Number;
   V_Use_Projects          Number;
   V_Ar_Pj_Type            Number;
   V_Use_Actvty            Number;
   V_Ar_Actv_Type          Number;
   V_Si_Rcode_Mandtry      Number;
Begin
   Begin
      Select Nvl (Conn_Sman_Wc_Csh_Cc, 0)
            ,Nvl (Cc_Avail, 0)
            ,Nvl (Ar_Cs_Type, 0)
            ,Nvl (Use_Projects, 0)
            ,Nvl (Ar_Pj_Type, 0)
            ,Nvl (Use_Actvty, 0)
            ,Nvl (Ar_Actv_Type, 0)
            ,Nvl (Si_Rcode_Mandtry, 0)
        Into V_Conn_Sman_Wc_Csh_Cc
            ,V_Cc_Avail
            ,V_Ar_Cst_Type
            ,V_Use_Projects
            ,V_Ar_Pj_Type
            ,V_Use_Actvty
            ,V_Ar_Actv_Type
            ,V_Si_Rcode_Mandtry
        From Ias_Para_Ar, Ias_Para_Gen
       Where Rownum <= 1;
   Exception
      When Others Then
         V_Conn_Sman_Wc_Csh_Cc   := 0;
   End;
   --##-----------------------------------------------------------------------------------------------------------##--
   If P_Rep_Code Is Not Null Then
        Begin
             Select W_Code
                   ,Cash_No
                   ,Cc_Code
                   ,Pj_No
                   ,Actv_No
               Into V_W_Code
                   ,V_Cash_No
                   ,V_Cc_Code
                   ,V_Pj_No
                   ,V_Actv_No
               From Sales_Man
              Where Reprs_Code = P_Rep_Code And Rownum <= 1;
          Exception
             When Others Then
                Null;
          End;
   
    
        If P_W_Code Is Not Null And nvl(P_Doc_type,0) In(4,5)  Then
              If  YS_SYS_GEN_PKG.CHK_ACTV_SYSTEM (P_SYS_NO => 70 , P_Brn_Usr => P_Brn_Usr)=1 and nvl(P_SYS_NO,0)<>70 Then             
                    If Nvl(P_W_CODE,0)=Nvl(V_W_CODE,0)Then
                             P_Err_No    := 20652;
                             P_MSG_TXT := IAS_GEN_PKG.GET_MSG (P_Lng_No, 5145);
                            Goto Rtn_Rslt;                                                      
                    End If;
              End If;
        End If;
        
        If P_Cash_No Is Not Null And nvl(P_Doc_type,0) In(4,5)  Then
              If  YS_SYS_GEN_PKG.CHK_ACTV_SYSTEM (P_SYS_NO => 70 , P_Brn_Usr => P_Brn_Usr)=1 and nvl(P_SYS_NO,0)<>70 Then             
                    If Nvl(P_Cash_No,0)=Nvl(V_Cash_No,0)Then
                             P_Err_No    := 20651;
                             P_MSG_TXT := IAS_GEN_PKG.GET_MSG (P_Lng_No, 4262);
                            Goto Rtn_Rslt;                                                      
                    End If;
              End If;
        End If;              
   End If;
   --##-----------------------------------------------------------------------------------------------------------##--
   If (Nvl (P_Sys_No, 0) = 70 Or Nvl (V_Si_Rcode_Mandtry, 0) = 1) And P_Rep_Code Is Null Then
      P_Err_No    := 20218;
      P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 395);
      Goto Rtn_Rslt;
   End If;
   --##-----------------------------------------------------------------------------------------------------------##--
   If V_Conn_Sman_Wc_Csh_Cc = 1 And P_Rep_Code Is Not Null Then                
      If V_Cash_No Is Not Null And P_Cash_No Is Not Null And P_Cash_No <> V_Cash_No And P_Bill_Doc_Type = 1 Then
         P_Err_No    := 20219;
         P_Msg_Txt   := Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 25) || ' ' || Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1607) || '  ' || ' Cash_No=' || P_Cash_No || 'Rep_Code=' || P_Rep_Code || ' ';
         Goto Rtn_Rslt;
      End If;
      -----------------------------------------------------------------------------------------------------------
      If V_Cc_Avail <> 0 And NVL(V_Ar_Cst_Type,0) =1 And V_Cc_Code Is Not Null And Nvl (P_Cc_Code, '0') <> V_Cc_Code And Nvl (P_Sys_No, 0)<>70 Then
         ------------------------------------------------------------------------------------------------------
         P_Err_No    := 20220;
         P_Msg_Txt   := Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 21) || ' ' || Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1607) || ' CC_CODE=' || P_Cc_Code || 'Rep_Code=' || P_Rep_Code || ' ';
         Goto Rtn_Rslt;
      End If;

      -----------------------------------------------------------------------------------------------------------
    /*  If V_Use_Projects <> 0 And V_Ar_Pj_Type <> 0 And V_Pj_No Is Not Null And Nvl (P_Pj_No, '0') <> V_Pj_No Then
         ------------------------------------------------------------------------------------------------------
         P_Err_No    := 20221;
         P_Msg_Txt   := Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2452) || ' ' || Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1607) || ' Pj_No=' || V_Pj_No || 'Rep_Code=' || P_Rep_Code || ' ';
         Goto Rtn_Rslt;
      End If;

      -----------------------------------------------------------------------------------------------------------
      If V_Use_Actvty <> 0 And V_Ar_Actv_Type <> 0 And V_Actv_No Is Not Null And Nvl (P_Actv_No, '0') <> V_Actv_No Then
         ------------------------------------------------------------------------------------------------------
         P_Err_No    := 20222;
         P_Msg_Txt   := Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2241) || ' ' || Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1607) || ' Actv_No=' || V_Actv_No || 'Rep_Code=' || P_Rep_Code || ' ';
         Goto Rtn_Rslt;
      End If;*/
   -----------------------------------------------------------------------------------------------------------
   End If;
  --##-----------------------------------------------------------------------------------------------------------##--
  --####################--
  <<Rtn_Rslt>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then      
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_Chk_Pkg.CHK_SMAN_CONN_DATA');
      Return;
   End If;
--####################--
Exception
   When Others Then
      P_Msg_Txt   := 'Error in Chk_Sman_Conn_Data ' || Sqlerrm;
      P_Err_No    := 20404;
      P_Pkg_Nm    := 'Ars_Api_Chk_Pkg.Chk_Sman_Conn_Data';
End Chk_Sman_Conn_Data;
   --##-----------------------------------------------------------------------------------------------------##--
   Procedure Chk_Cr_Card_Prc (P_Bill_Doc_Type          In     Ias_Bill_Mst.Bill_Doc_Type%Type
                          ,P_Crdno                  In     Number
                          ,P_W_Code                 In     Ias_Bill_Mst.W_Code%Type
                          ,P_Cur_Code               In     Ex_Rate.Cur_Code%Type
                          ,P_Cr_Card_No             In     Ias_Bill_Mst.Cr_Card_No%Type
                          ,P_Cr_Card_Amt            In     Ias_Bill_Mst.Cr_Card_Amt%Type
                          ,P_Credit_Card            In Out Ias_Bill_Mst.Credit_Card%Type
                          ,P_Cr_A_Code              In Out Account.A_Code%Type
                          ,P_Cr_Card_Comm_Per       In Out Ias_Bill_Mst.Cr_Card_Comm_Per%Type                        
                          ,P_Cr_Card_Max_Comm_Amt   In Out Ias_Bill_Mst.Cr_Card_Max_Comm_Amt%Type                          
                          ,P_Online                 In     Number Default 1
                          ,P_Lng_No                 In     Number Default 1
                          ,P_Msg_Txt                   Out Varchar2
                          ,P_Err_No                    Out Varchar2
                          ,P_Pkg_Nm                    Out Varchar2)
Is
   V_Cnt      Number;
   V_Crd_No   Varchar2 (100);
Begin   
   If P_Crdno = 1 Then
      V_Crd_No   := ' ';
   Elsif P_Crdno = 2 Then
      V_Crd_No   := '_SCND';
   Elsif P_Crdno = 3 Then
      V_Crd_No   := '_THRD';
   End If;

   If P_Cr_Card_No Is Not Null And nvl(P_Cr_Card_Amt,0)=0 Then
      P_Err_No    := 20427;
      P_Msg_Txt   := 'Cr_Card_No' || V_Crd_No || 'IS NOT NULL AND Cr_Card_Amt_' || V_Crd_No || ' IS NULL ';
      Goto Rtn_Rslt;
   End If;

   If P_Cr_Card_No Is Null And nvl(P_Cr_Card_Amt,0)<>0 Then
      P_Err_No    := 20428;
      P_Msg_Txt   := 'Cr_Card_No' || V_Crd_No || 'IS  NULL AND Cr_Card_Amt_' || V_Crd_No || ' IS NOT  NULL ';
      Goto Rtn_Rslt;
   End If;
   
   If P_Cr_Card_No Is Not Null And nvl(P_Cr_Card_Amt,0)<>0 AND NVL(P_Credit_Card,0)=0 and  P_Bill_Doc_Type <> 5  Then
      P_Err_No    := 20446;
      P_Msg_Txt   := 'YOU MUST ENTER Credit_Card=1'||chr(10)
                     ||'Cr_Card_No' || V_Crd_No || '='||P_Cr_Card_No||chr(10)
                     ||'Cr_Card_Amt' || V_Crd_No ||'='||P_Cr_Card_Amt||chr(10)
                     ||'Credit_Card=' ||NVL(P_Credit_Card,0);
      Goto Rtn_Rslt;
   End If;

   If Nvl (P_Credit_Card, 0) = 1 Or P_Bill_Doc_Type = 5 Then
      If P_Cr_Card_No Is Not Null Then
         Begin
            Select Count (1)
              Into V_Cnt
              From Credit_Card_Types
             Where Cr_Card_No = P_Cr_Card_No;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If Nvl (V_Cnt, 0) = 0 Then
            P_Err_No    := 20429;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2194) ||chr(10) || Ias_Gen_Pkg.Get_Msg (P_Lng_No, 312) || ' ' ||chr(10) || 'Cr_Card_No_' || V_Crd_No || '=' || P_Cr_Card_No;
            Goto Rtn_Rslt;
         Else
            Begin
               Select Bank_Ac
                     ,Decode (P_Online, 1, Comm_Per, P_Cr_Card_Comm_Per)
                     ,Decode (P_Online, 1, Max_Comm_Amt, P_Cr_Card_Max_Comm_Amt)                     
                 Into P_Cr_A_Code, P_Cr_Card_Comm_Per, P_Cr_Card_Max_Comm_Amt
                 From Credit_Card_Types
                Where Cr_Card_No = P_Cr_Card_No;
            Exception
               When Others Then
                  P_Err_No    := 20430;
                  P_Msg_Txt   := 'ERROR IN Chk_Cr_Card_Prc' ||chr(10) || Sqlerrm;
                  Goto Rtn_Rslt;
            End;
         End If;

         Begin
            Select Count (1)
              Into V_Cnt
              From Account_Curr
             Where A_Code = P_Cr_A_Code And A_Cy = P_Cur_Code;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If Nvl (V_Cnt, 0) = 0 Then
            P_Err_No    := 20431;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 797) || '=' || P_Cur_Code ||chr(10) || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 129) || '=' || P_Cr_A_Code;
            Goto Rtn_Rslt;
         End If;

         V_Cnt              := 0;

         Begin
            Select 1
              Into V_Cnt
              From Credit_Card_Types
             Where Cr_Card_No = P_Cr_Card_No 
             And Nvl (P_W_Code, 0) <> 0 
             And Nvl (W_Code, 0) <> 0
              And P_W_Code <> W_Code 
              And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If Nvl (V_Cnt, 0) = 1 Then
            P_Err_No    := 20433;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2194) ||chr(10) || Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5842) || ' ' ||chr(10) || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2194) || '=' || P_Cr_Card_No ||chr(10) || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 193) || '=' || P_W_Code;
            Goto Rtn_Rslt;
         End If;

         If P_Bill_Doc_Type = 5 Then
            P_Credit_Card   := 0;
         Else
            P_Credit_Card   := Nvl (P_Credit_Card, 0);
         End If;
                 
      End If;
   End If;

  ---------------------------------------------------------------
  --####################--
  <<RTN_RSLT>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_Chk_Pkg.Chk_Cr_Card_Prc');
      Return;
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;
   End If;
--####################--

Exception
   When Others Then
      P_Msg_Txt   := 'Error When Chk_Cr_Card_Prc , ' ||chr(10) || Sqlerrm;
      P_Err_No    := 20329;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_Chk_Pkg.Chk_Cr_Card_Prc');
End Chk_Cr_Card_Prc;
--##--------------------------------------------------------------------------------------------------------------------------------##--
    Procedure Chk_Amt_And_Itm_Tax(  P_Clc_Typ_No_Tax   In     Gnr_Tax_Itm_Movmnt.Clc_Typ_No%Type Default Null,
                                    P_Use_Vat          In     Number Default Null ,
                                    P_CLC_TAX_FREE_QTY_FLG   In  NUMBER Default Null, 
                                    P_Calc_Vat_Amt_Type IN    NUMBER Default 1  ,
                                    P_CALC_TAX_AUTO_FLG IN    NUMBER Default 0  ,
                                    P_Doc_Typ          In     Gnr_Tax_Itm_Movmnt.Doc_Type%Type,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                                    P_Doc_No           In     Gnr_Tax_Itm_Movmnt.Doc_No%Type,
                                    P_Doc_Ser          In     Gnr_Tax_Itm_Movmnt.Doc_Ser%Type,
                                    P_Fld_Doc_No       In     Varchar2,
                                    P_Fld_Doc_Ser      In     Varchar2,
                                    P_Fld_MST_AMT      In     Varchar2,
                                    P_Tbl_Mvmnt_Nm     In     Varchar2,
                                    P_Tbl_Mst_Nm       In     Varchar2,
                                    P_Tbl_Dtl_Nm       In     Varchar2,
                                    P_No_Of_Decimal    In     Number ,
                                    P_DIFF_AMT         In     Number Default Null,
                                    P_DOC_AMT_XML      OUT    CLOB,
                                    P_Lng_No           In     Number Default 1,
                                    P_Msg_Txt          Out Varchar2,
                                    P_ERR_NO         Out Varchar2,
                                    P_Pkg_Nm           Out Varchar2)
Is   
   V_Use_Vat        Number;  
   V_Cnt        Number;
   V_Mst_Doc_Amt           Number;
   V_Disc_Amt              Number;
   V_Mst_Othr_Amt          Number;
   V_Mst_Vat_Amt           Number;
   V_Doc_Amt_Dtl           Number;
   V_Dis_Amt               Number;
   V_DTL_Othr_Amt          Number;
   V_DTL_VAT_AMT           Number;
   V_DTL_Vat_Amt_CORCT     Number;
   V_DTL_Vat_Per           Number;
   V_Mvt_Vat_Amt           Number;
   V_Mvt_Vat_Per           Number;
   V_DTL_OTHR_AMT_DISC     Number;
   V_QRY                   Varchar2(4000)  ;
   V_CHEQUE_AMT             Number;
   V_Fld_Disc               Varchar2(4000)  ;
   V_Clc_Tax_Dscnt2    Number:=0;
   V_Clc_Tax_Dscnt3    Number:=0;
   V_USE_CLC_TAX_FREE_QTY Number:=0;
   V_AMT_DIFF             number:=NVL(P_DIFF_AMT,0.1);   
   Qry_Ctx      Dbms_Xmlgen.Ctxhandle;    
Begin 

   
     
   Begin
      Select nvl(Use_Vat,0),NVL(Clc_Tax_Dscnt2,0),NVL(Clc_Tax_Dscnt3,0) ,nvl(USE_CLC_TAX_FREE_QTY,0)
      Into V_Use_Vat,V_Clc_Tax_Dscnt2,V_Clc_Tax_Dscnt3 ,V_USE_CLC_TAX_FREE_QTY
      From Ias_Para_Gen,IAS_PARA_AR;
   Exception
      When Others Then
         V_USE_CLC_TAX_FREE_QTY := 0;
   End;
   V_Use_Vat:=nvl(P_Use_Vat,nvl(V_Use_Vat,0));
   V_USE_CLC_TAX_FREE_QTY:=nvl(P_CLC_TAX_FREE_QTY_FLG,nvl(V_USE_CLC_TAX_FREE_QTY,0));
   --##----------------------------------------------------------------------------------------------##--
    V_Fld_Disc := 'NVL(D.DIS_AMT_MST,0)+NVL(D.DIS_AMT_DTL,0)';

   If V_Clc_Tax_Dscnt2 = 1 Then
      V_Fld_Disc := V_Fld_Disc || '+NVL(D.DIS_AMT_DTL2,0)';
   End If;

   If V_Clc_Tax_Dscnt3 = 1 Then
      V_Fld_Disc := V_Fld_Disc || '+NVL(D.DIS_AMT_DTL3,0)';
   End If;

   V_Fld_Disc := '(' || V_Fld_Disc || '+NVL(D.OTHR_AMT_DISC,0))';
   --##----------------------------------------------------------------------------------------------##--
   --## CHECK DATA Between Master And Detail
   Begin
      V_Cnt := Ias_Gen_Pkg.Get_Cnt(' SELECT 1  FROM (
                                             SELECT ' || P_Fld_Doc_No ||','|| P_Fld_Doc_Ser || ' FROM ' || P_Tbl_Mst_Nm || ' WHERE ' || P_Fld_Doc_Ser || ' =' || P_Doc_Ser || '
                                             MINUS
                                             SELECT ' || P_Fld_Doc_No ||', ' || P_Fld_Doc_Ser || ' FROM ' || P_Tbl_Dtl_Nm || ' WHERE ' || P_Fld_Doc_Ser || ' = ' || P_Doc_Ser || ')
                                         WHERE ROWNUM<=1 ');
   Exception
      When No_Data_Found Then
         V_Cnt := 0;
      When Others Then
         P_Err_No := 20223;
         P_Msg_Txt :=  'Check Data Between Master And Detail ' || chr(10) || Sqlerrm;
         Goto Rtn_Rslt;
   End;

   If Nvl(V_Cnt, 0) > 0 Then
      P_Err_No := 20224;
      P_Msg_Txt :=  'Mismatching Data Between Master And Detail ';
      Goto Rtn_Rslt;
   End If;
  --##----------------------------------------------------------------------------------------------##--
   If P_Clc_Typ_No_Tax Is Null And Nvl (V_Use_Vat, 0) = 1 Then
               P_Err_No := 20225;
               P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 12041);
               Goto Rtn_Rslt;
   End If;

   If P_Clc_Typ_No_Tax Is Not Null And Nvl (V_Use_Vat, 0) = 1 Then
       Begin
          V_Cnt := Ias_Gen_Pkg.Get_Cnt (' SELECT 1  FROM ' || P_Tbl_Dtl_Nm || ' D 
                                     WHERE '|| P_Fld_Doc_Ser||' =' || P_Doc_Ser|| '
                                     And (nvl(i_qty,0)+('||V_USE_CLC_TAX_FREE_QTY||'*nvl(free_qty,0)))>0
                                       AND EXISTS ( SELECT 1 FROM  
                                                                   GNR_TAX_ITM TI,
                                                                   GNR_TAX_CODE_MST TM,
                                                                   GNR_TAX_CODE_DTL TD,
                                                                   GNR_TAX_TYP_CLC_DTL TC
                                                               WHERE           TI.TAX_NO = TM.TAX_NO
                                                               AND             TI.TAX_NO = TD.TAX_NO
                                                               AND             TI.AGNCY_NO = TD.AGNCY_NO
                                                               AND             TI.TAX_NO = TC.TAX_NO
                                                               AND             TM.TAX_NO = TD.TAX_NO
                                                               AND             TM.TAX_NO = TC.TAX_NO
                                                               AND             TD.TAX_NO = TC.TAX_NO
                                                               AND             NVL (TM.INACTIVE, 0) = 0 
                                                               AND             I_CODE = D.I_CODE 
                                                               AND             NVL(TI.TAX_PRCNT,0)>0             
                                                               AND             TC.CLC_TYP_NO =' ||P_Clc_Typ_No_Tax || '
                                                               AND ROWNUM<=1)
                                       AND ROWNUM<=1 ');
       Exception
          When No_Data_Found Then
             V_Cnt := 0;
          When Others Then
            P_Err_No := 20226;
            P_Msg_Txt :=  'Check Tax Detail with Tax Define ' || chr(10) || Sqlerrm;
            Goto Rtn_Rslt;                    
       End;

       If Nvl (V_Cnt, 0) > 0 Then
          V_Cnt := 0;

          Begin
             V_Cnt := Ias_Gen_Pkg.Get_Cnt (' SELECT 1  FROM ' || P_Tbl_Mvmnt_Nm || ' WHERE DOC_TYPE =' || P_Doc_Typ || ' AND DOC_SER = ' || P_Doc_Ser || ' AND ROWNUM<=1 ');
          Exception
             When Others Then
                V_Cnt := 0;
          End;

          If Nvl (V_Cnt, 0) = 0 Then
             P_Err_No := 20228;
             P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5804);
             Goto Rtn_Rslt;
          End If;
       End If;
   End If;
  --##----------------------------------------------------------------------------------------------##--                                                  
             --##MST TABLE
              BEGIN
               Execute Immediate '  SELECT     ROUND (NVL ('||P_Fld_MST_AMT||', 0), ' || P_No_Of_Decimal || ' )  ,
                                               ROUND (NVL (DISC_AMT, 0), ' || P_No_Of_Decimal || ')   ,
                                               ROUND (NVL (OTHR_AMT, 0), ' || P_No_Of_Decimal || ')  ,
                                               ROUND (NVL (VAT_AMT, 0),  ' || P_No_Of_Decimal || ')                                                                                                                                    
                                FROM     ' || P_Tbl_Mst_Nm || '  WHERE '|| P_Fld_Doc_Ser||' =' || P_Doc_Ser
                  Into V_Mst_Doc_Amt
                      ,V_Disc_Amt
                      ,V_Mst_Othr_Amt
                      ,V_Mst_Vat_Amt;
              Exception When NO_DATA_FOUND THEN
                       V_Mst_Doc_Amt  :=0;
                       V_Disc_Amt     :=0;
                       V_Mst_Othr_Amt :=0;
                       V_Mst_Vat_Amt :=0;       
              WHEN Others Then
                      P_Err_No := 20229;
                      P_Msg_Txt :='ERROR WHEN CHECK  AMT  IN  '||P_Tbl_MST_Nm||' '||chr(10) || Sqlerrm ;
                      Goto Rtn_Rslt; 
              END;         
               --===============================================================--
              --## DTL TABLE
              BEGIN
              
                                          
               Execute Immediate ' SELECT        ROUND(SUM(NVL(I_PRICE,0) * NVL(I_QTY,0)),' || P_No_Of_Decimal || ')   ,
                                                 ROUND(SUM(NVL(D.DIS_AMT,0)* NVL(I_QTY,0)), ' || P_No_Of_Decimal || ')  ,
                                                 ROUND(SUM(NVL(D.OTHR_AMT,0)* Decode('|| V_Mst_Doc_Amt||',0,NVL(FREE_QTY,0),NVL(I_QTY,0))),' || P_No_Of_Decimal || ') ,
                                                 ROUND(SUM(NVL(D.OTHR_AMT_DISC,0)*Decode('||V_Mst_Doc_Amt||',0,NVL(FREE_QTY,0),NVL(I_QTY,0)) ),' || P_No_Of_Decimal || ') ,
                                                 ROUND(SUM(NVL(D.VAT_AMT,0)* (NVL(I_QTY,0)+(NVL(FREE_QTY,0)*NVL(CLC_TAX_FREE_QTY_FLG,0)))), ' || P_No_Of_Decimal || ') ,
                                                 SUM(NVL(D.VAT_PER,0)) ,
                                                 DECODE('||P_CALC_VAT_AMT_TYPE||',1
                                                                              ,SUM(((NVL(I_PRICE,0)*NVL(VAT_PER,0))/100 )*(NVL(I_QTY,0)+(NVL(FREE_QTY,0)*NVL(CLC_TAX_FREE_QTY_FLG,0))))
                                                                              ,SUM((((NVL(I_PRICE,0)-'||V_Fld_Disc||') *NVL(VAT_PER,0))/100 )* (NVL(I_QTY,0)+(NVL(FREE_QTY,0)*NVL(CLC_TAX_FREE_QTY_FLG,0)))) )                                        
                                   FROM  ' || P_Tbl_MST_Nm || ' M,' || P_Tbl_Dtl_Nm || ' D  
                                   WHERE M.'|| P_Fld_Doc_Ser||' = D.'||P_Fld_Doc_Ser||'
                                   AND M.'|| P_Fld_Doc_Ser||' = ' || P_Doc_Ser
                  Into V_Doc_Amt_Dtl
                      ,V_Dis_Amt
                      ,V_DTL_Othr_Amt
                      ,V_DTL_OTHR_AMT_DISC
                      ,V_DTL_Vat_Amt
                      ,V_DTL_Vat_Per
                      ,V_DTL_Vat_Amt_CORCT;
              Exception When NO_DATA_FOUND THEN
                      V_Doc_Amt_Dtl       :=0;
                      V_Dis_Amt           :=0;
                      V_DTL_Othr_Amt      :=0;
                      V_DTL_Vat_Amt       :=0;
                      V_DTL_Vat_Per       :=0;
                      V_DTL_Vat_Amt_CORCT :=0;      
              WHEN Others Then
                      P_Err_No := 20230;
                      P_Msg_Txt :='ERROR WHEN CHECK  AMT  IN  '||P_Tbl_Dtl_Nm||' '||chr(10) || Sqlerrm ;
                      Goto Rtn_Rslt; 
              END;           
              --===============================================================--
                --## TAX ITM MOVMNT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ---DTL
              BEGIN
                   Execute Immediate ' SELECT  Nvl (Round (Sum (Nvl (Tax_Amt, 0) * (NVL(I_QTY,0)+(NVL(FREE_QTY,0)*NVL(CLC_TAX_FREE_QTY_FLG,0)))), '||P_No_Of_Decimal||'), 0) Vat_Amt
                                              ,NVL(SUM(NVL(TAX_PRCNT,0)),0) VAT_PER
                                        FROM  ' || P_Tbl_Mvmnt_Nm || 
                                         ' WHERE DOC_SER =' || P_Doc_Ser
                                          Into V_Mvt_Vat_Amt,
                                               V_Mvt_Vat_Per;
              Exception When NO_DATA_FOUND THEN
                    V_Mvt_Vat_Amt:=0;
                    V_Mvt_Vat_Per:=0;
              WHEN Others Then
                      P_Err_No := 20231;
                      P_Msg_Txt :='ERROR WHEN CHECK  TAX FROM  '||P_Tbl_Mvmnt_Nm||' '||chr(10) || Sqlerrm ;
                      Goto Rtn_Rslt;
              END; 
            --##------------------------------------------------------------------------------------------------##--       
               --##CHK AMT BETWEEN  Master And Detail  
               If abs(Nvl (V_Mst_Doc_Amt, 0)- Nvl (V_Doc_Amt_Dtl, 0))>=V_AMT_DIFF Then
                  P_Err_No := 20232;
                  P_Msg_Txt := 'Check Data (DOC_AMT) Between Master And Detail '
                                   ||chr(10)|| ' Master DOC_AMT = ' || V_Mst_Doc_Amt 
                                   ||chr(10)|| ' Detail DOC_AMT = ' || V_Doc_Amt_Dtl  
                                   ||chr(10)|| ' Diff= ' || abs(Nvl (V_Mst_Doc_Amt, 0)- Nvl (V_Doc_Amt_Dtl, 0)) || ' ';
                  Goto Rtn_Rslt;
               Elsif abs(Nvl (V_Disc_Amt, 0) - Nvl (V_Dis_Amt, 0))>=V_AMT_DIFF Then
                  P_Err_No := 20233;
                  P_Msg_Txt := 'Check Data (DSCNT_AMT) Between Master And Detail' 
                                        ||chr(10)|| 'MST DISC_AMT = ' || V_Disc_Amt 
                                        ||chr(10)|| 'DTL DISC_AMT = ' || V_Dis_Amt
                                        ||chr(10)|| 'Diff = ' || abs(Nvl (V_Disc_Amt, 0) - Nvl (V_Dis_Amt, 0)) ;
                  Goto Rtn_Rslt;                                  
               ELSIF (Nvl (V_DTL_OTHR_AMT_DISC, 0)+ Nvl (V_Disc_Amt, 0) ) > Nvl (V_Mst_Doc_Amt, 0)  THEN                   
                      P_Err_No := 20639;
                      P_MSG_TXT := IAS_GEN_PKG.GET_MSG (P_LNG_NO, 6129);
                      Goto Rtn_Rslt;                                  
               Elsif abs( Nvl (V_Mst_Othr_Amt, 0) - Nvl (V_DTL_Othr_Amt, 0))>=V_AMT_DIFF Then
                  P_Err_No := 20234;
                  P_Msg_Txt := 'Check Data (OTHR_AMT) Between Master And Detail'            
                                          ||chr(10)|| ' MST OTHR_AMT ='|| V_Mst_Othr_Amt 
                                          ||chr(10)|| ' DTL OTHR_AMT ='|| V_DTL_Othr_AmT
                                          ||chr(10)|| ' Diff = ' || abs( Nvl (V_Mst_Othr_Amt, 0) - Nvl (V_DTL_Othr_Amt, 0)) ;
                  Goto Rtn_Rslt;
               Elsif abs(Nvl (V_Mst_Vat_Amt, 0) - Nvl (V_DTL_Vat_Amt, 0))>=V_AMT_DIFF Then
                  P_Err_No := 20235;
                  P_Msg_Txt := 'Check Data (VAT_AMT) Between Master And Detail'
                                           ||chr(10)||'Master TAX_AMT = ' || V_Mst_Vat_Amt 
                                           ||chr(10)||'Detail TAX_AMT = ' || V_DTL_Vat_Amt
                                           ||chr(10)|| ' Diff = ' || abs(Nvl (V_Mst_Vat_Amt, 0) - Nvl (V_DTL_Vat_Amt, 0)) ;
                  Goto Rtn_Rslt;
               End If;                        
              --##----------------------------------------------------------------------------------------------##--
               If ABS(ROUND(NVL(V_DTL_Vat_Amt_CORCT,0),2)-ROUND(NVL(V_DTL_Vat_Amt,0),2))>=V_AMT_DIFF Then
                  P_Err_No := 20236;
                  P_Msg_Txt := 'TAX_AMT IN '|| P_Tbl_Dtl_Nm ||' INCORRECT'
                                           ||chr(10)||'TAX_AMT ='||Round(V_DTL_Vat_Amt,6)
                                           ||chr(10)||'CORRECT TAX_AMT ='||Round(V_DTL_Vat_Amt_CORCT,6)
                                           ||chr(10)||'DIFF ='||Round(ABS((NVL(V_DTL_Vat_Amt_CORCT,0))-(NVL(V_DTL_Vat_Amt,0))),6);
                  Goto Rtn_Rslt;
                  
               END IF;
              --##----------------------------------------------------------------------------------------------##--
                --## CHK TAX BETWEEN Master And MOVMNT                                                        
               If abs(Nvl (V_Mst_Vat_Amt, 0) - Nvl (V_Mvt_Vat_Amt, 0))>=V_AMT_DIFF Then
                      P_Err_No := 20237;
                      P_Msg_Txt := 'Check Data (TAX_AMT)'
                                       || chr(10)||' Between Master And MOVMNT'
                                       || chr(10)||' Master TAX_AMT = ' || V_Mst_Vat_Amt
                                       || chr(10)||' MOVMNT TAX_AMT = ' || V_Mvt_Vat_Amt
                                       || chr(10)||' Diff = ' || abs(Nvl (V_Mst_Vat_Amt, 0) - Nvl (V_Mvt_Vat_Amt, 0));
                      Goto Rtn_Rslt;
               End If;                                      
              --##----------------------------------------------------------------------------------------------##--
               --##CHK TAX BETWEEN Detail AND MOVMNT 
               If abs(Nvl (V_DTL_VAT_AMT, 0) - Nvl (V_MVT_VAT_AMT, 0))>=V_AMT_DIFF Then
                  P_Err_No := 20238;
                  P_Msg_Txt := 'Check Data (TAX_AMT)' 
                                  || chr(10)||' Between Detail And MOVMNT '
                                  || chr(10)||' DETAIL  TAX_AMT =' || V_DTL_VAT_AMT
                                  || chr(10)||' MOVMNT  TAX_AMT =' || V_Mvt_Vat_Amt
                                  || chr(10)||' Diff =' || abs(Nvl (V_DTL_VAT_AMT, 0) - Nvl (V_MVT_VAT_AMT, 0));
                  Goto Rtn_Rslt;
              /* Elsif Nvl (V_Dtl_Vat_Per, 0) <> Nvl (V_Mvt_Vat_Per, 0) Then
                  P_Err_No := 20239;
                  P_Msg_Txt := ' Check Data (TAX_PRCNT)' 
                                 || chr(10)||'Between Detail And MOVMNT'
                                 || chr(10)||'DETAIL TAX_PER = ' || V_Dtl_Vat_Per
                                 || chr(10)||'MOVMNT TAX_PER = ' || V_Mvt_Vat_Per;
                  Goto Rtn_Rslt;*/
               End If; 
               
               --##----------------------------------------------------------------------------------------------##--
               --##CHK DISCOUNT 
               IF Nvl (V_DTL_OTHR_AMT_DISC, 0)>0 OR Nvl (V_Disc_Amt, 0)>0 THEN 
                   If (Nvl (V_DTL_OTHR_AMT_DISC, 0)+ Nvl (V_Disc_Amt, 0) ) > Nvl (V_Mst_Doc_Amt, 0) Then
                      P_Err_No := 20448;
                      P_MSG_TXT := IAS_GEN_PKG.GET_MSG (P_LNG_NO, 45);
                      Goto Rtn_Rslt;              
                   End If; 
               END IF;                                                  
  --##----------------------------------------------------------------------------------------------##--
          IF P_Doc_Typ in(4,5) THEN
            Declare
               V_Bill_Doc_Type      Number;
               V_Credit_Card        Number (2);
               V_Total              Number;
               V_Cr_Card_Amt        Number;
               V_Cr_Card_Amt_Scnd   Number;
               V_Cr_Card_Amt_Thrd   Number;
               V_Cr_Card_No         Number;
               V_Cr_Card_No_Scnd   Number;
               V_Cr_Card_No_Thrd    Number;
               V_External_Post      Number;
               V_Ac_Amt             NUMBER;
               V_Cr_Card_Comm_Amt   NUMBER;
               V_Fld_Bill_Doc_Type  Varchar2(500);
            Begin
            
              If P_Doc_Typ=5 Then
                 V_Fld_Bill_Doc_Type:='RT_BILL_DOC_TYPE';
               Else
                 V_Fld_Bill_Doc_Type:='BILL_DOC_TYPE';
              End if;
               
              BEGIN
              Execute immediate '
               Select '||V_Fld_Bill_Doc_Type||' Bill_Doc_Type
                     ,NVL(Credit_Card,0)
                     ,Round ( (Nvl (Bill_Amt, 0) + Nvl (Othr_Amt, 0) + Nvl (Vat_Amt_Othr, 0) + Nvl (Vat_Amt, 0)) - (Nvl (Disc_Amt_Mst, 0) + Nvl (Disc_Amt_Dtl, 0) + Nvl (Disc_Amt_Aftr_Vat, 0)),'|| P_No_Of_Decimal ||')
                     ,NVL(CHEQUE_AMT,0)
                     ,Cr_Card_Amt
                     ,Cr_Card_Amt_Scnd
                     ,Cr_Card_Amt_Thrd
                     ,Cr_Card_No
                     ,Cr_Card_No_Scnd
                     ,Cr_Card_No_Thrd
                     ,External_Post
                     ,Ac_Amt
                      FROM     ' || P_Tbl_Mst_Nm || '  WHERE '|| P_Fld_Doc_Ser||' =' || P_Doc_Ser
                 Into V_Bill_Doc_Type
                     ,V_Credit_Card
                     ,V_Total
                     ,V_CHEQUE_AMT
                     ,V_Cr_Card_Amt
                     ,V_Cr_Card_Amt_Scnd
                     ,V_Cr_Card_Amt_Thrd
                     ,V_Cr_Card_No
                     ,V_Cr_Card_No_Scnd
                     ,V_Cr_Card_No_Thrd
                     ,V_External_Post
                     ,V_Ac_Amt;                
              EXCEPTION WHEN OTHERS THEN
                  P_Msg_Txt   := 'Error When Chk_Amt_And_Itm_Tax , ' ||chr(10) || Sqlerrm;
                  P_Err_No    := 20439;
                   Goto Rtn_Rslt;  
              END; 
              --------------------------------------------------------     
               If V_Bill_Doc_Type IN(2,6) Then
                  IF NVL(P_CALC_TAX_AUTO_FLG,0)=0 THEN
                    IF ABS(NVL(V_CHEQUE_AMT,0)-NVL(V_Total,0))>0.1 THEN
                          P_Err_No := 20511;
                          P_Msg_Txt := 'CHEQUE_AMT IN '|| P_Tbl_MST_Nm ||' INCORRECT'
                                                   ||chr(10)||'CHEQUE_AMT ='||Round(V_CHEQUE_AMT,6)
                                                   ||chr(10)||'CORRECT CHEQUE_AMT ='||Round(V_Total,6)
                                                   ||chr(10)||'DIFF ='||Round(ABS((NVL(V_CHEQUE_AMT,0))-(NVL(V_Total,0))),6);
                          Goto Rtn_Rslt;
                  
                    END IF;
                  ELSE
                    Execute immediate ' UPDATE ' || P_Tbl_Mst_Nm || '  SET CHEQUE_AMT='||V_Total||'  WHERE '|| P_Fld_Doc_Ser||' =' || P_Doc_Ser;
                  END IF;                 
               END IF;
              --------------------------------------------------------                                
               If Nvl (V_Credit_Card, 0) = 1 Or V_Bill_Doc_Type = 5 Then
                  If V_Bill_Doc_Type = 5 And (Nvl (V_Cr_Card_Amt, 0) + Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0)) = 0 Then
                     V_Cr_Card_Amt   := Nvl (V_Total, 0);
                  End If;
                       
                  If V_Cr_Card_No Is Null Then
                        P_Err_No    := 20434;
                        P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2194) ;
                        Goto Rtn_Rslt;         
                  End If;
                  --##--------------------------------------------------------------------------------------##--
                  If V_Bill_Doc_Type=5 And V_Cr_Card_No Is Not Null And V_Cr_Card_No_Scnd Is Null And V_Cr_Card_No_Thrd Is  Null Then
                    V_Cr_Card_Amt:=V_Total;
                  END IF;
                   --##--------------------------------------------------------------------------------------##--
                  --V_Cr_Card_Comm_Amt   := (Nvl (V_Total, 0) * (Nvl (V_Cr_Card_Comm_Per, 0) / 100)) + (Nvl (V_Total, 0) * (Nvl (V_Cr_Card_Comm_Per_Scnd, 0) / 100)) + (Nvl (V_Total, 0) * (Nvl (V_Cr_Card_Comm_Per_Thrd, 0) / 100));
                  --##--------------------------------------------------------------------------------------##--
                  If Nvl (V_Cr_Card_Amt, 0) = 0 And V_Bill_Doc_Type = 5 And Nvl (V_Total, 0) > (Nvl (V_Total, 0) - (Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0))) Then
                     V_Cr_Card_Amt   := Nvl (V_Total, 0) - (Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0));
                  End If;
                  --##--------------------------------------------------------------------------------------##--
                  If Nvl (V_Cr_Card_Amt, 0) = 0 Then
                        P_Err_No    := 20435;
                        P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 527) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2167) ;
                        Goto Rtn_Rslt;         
                  End If;
                  --##--------------------------------------------------------------------------------------##--
                   Execute immediate ' UPDATE ' || P_Tbl_Mst_Nm || '  SET Cr_Card_Amt='||V_Cr_Card_Amt||'  WHERE '|| P_Fld_Doc_Ser||' =' || P_Doc_Ser;
                  --##--------------------------------------------------------------------------------------##--
                  If Nvl (V_Credit_Card, 0) = 1 And V_Bill_Doc_Type <> 5 And (Nvl (V_Cr_Card_Amt, 0) + Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0)) >= Nvl (V_Total, 0) Then
                        P_Err_No    := 20436;
                        P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 392) 
                                     ||chr(10)|| Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 900)||'='||Nvl (V_Total, 0)
                                     ||chr(10)|| Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2167)||'='||(Nvl (V_Cr_Card_Amt, 0) + Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0)) ;
                        Goto Rtn_Rslt;        
                  Elsif V_Bill_Doc_Type = 5 Then
                     If V_External_Post <> 87 Then
                        If Round ( (Nvl (V_Cr_Card_Amt, 0) + Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0)), P_No_Of_Decimal) <> Round (Nvl (V_Total, 0), P_No_Of_Decimal) Then
                            P_Err_No    := 20437;
                            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1259) 
                                         ||chr(10)|| Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 900)||'='||Nvl (V_Total, 0)
                                         ||chr(10)|| Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2167)||'='||(Nvl (V_Cr_Card_Amt, 0) + Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0)) ;
                            Goto Rtn_Rslt;               
                        Elsif Round ( (Nvl (V_Cr_Card_Amt, 0) + Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0)) + Nvl (V_Ac_Amt, 0), P_No_Of_Decimal) <> Round (Nvl (V_Total, 0), P_No_Of_Decimal) Then
                            P_Err_No    := 20438;
                            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1259) 
                                         ||chr(10)|| Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 900)||'='||Nvl (V_Total, 0)
                                         ||chr(10)|| Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 1060)||'='||Nvl (V_Ac_Amt, 0)
                                         ||chr(10)|| Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 2167)||'='||(Nvl (V_Cr_Card_Amt, 0) + Nvl (V_Cr_Card_Amt_Scnd, 0) + Nvl (V_Cr_Card_Amt_Thrd, 0)) ;
                            Goto Rtn_Rslt;  
                        End If;
                     End If;
                  End If;
               End If;
            End;
        END IF;
  --##---------------------------------------------------------------------------------------------##--
  BEGIN 
      V_QRY:='SELECT 
                       ROUND(NVL(M.'||P_Fld_MST_AMT||',0),'||P_No_Of_Decimal||') DOC_AMT
                      ,ROUND(NVL(M.DISC_AMT,0),'||P_No_Of_Decimal||') DISC_AMT
                      ,ROUND((NVL(M.VAT_AMT_OTHR,0)+NVL(M.VAT_AMT,0)) ,'||P_No_Of_Decimal||') VAT_AMT
                      ,ROUND(NVL(M.OTHR_AMT,0),'||P_No_Of_Decimal||') OTHR_AMT
                      ,ROUND(( (NVL(M.'||P_Fld_MST_AMT||',0)+ NVL(M.OTHR_AMT,0)+ NVL(M.VAT_AMT_OTHR,0)+NVL(M.VAT_AMT,0))-NVL(M.DISC_AMT,0)),'||P_No_Of_Decimal||') NET_AMT
                    FROM '||P_Tbl_Mst_Nm||' M
                     WHERE  M.'||P_Fld_Doc_Ser||'='||P_Doc_Ser||' ';
       Qry_Ctx := Dbms_Xmlgen.Newcontext( V_QRY);      
       P_DOC_AMT_XML := Dbms_Xmlgen.Getxml( Qry_Ctx);                    
  EXCEPTION WHEN OTHERS THEN
     P_DOC_AMT_XML:=NULL;
     P_Err_No := 20240;
     P_Msg_Txt :='Err IN Chk_Amt_And_Itm_Tax'|| Sqlerrm;
     Goto Rtn_Rslt;
  END ;                      
  --##---------------------------------------------------------------------------------------------##--
     --####################--
  <<Rtn_Rslt>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then     
      P_Msg_Txt:= NVL(P_Msg_Txt,'Message Number Is Missing');
      P_ERR_NO := P_Err_No;
      P_Pkg_Nm := NVL(P_Pkg_Nm,'Ars_Api_Chk_Pkg.Chk_Amt_And_Itm_Tax');
      Return;
   Else
      P_Msg_Txt:=  Null;
      P_ERR_NO :=  Null;
      P_Pkg_Nm :=  Null;         
   End If;
--####################--
Exception When Others then      
         P_Msg_Txt := 'Error in Chk_Amt_And_Itm_Tax '||sqlerrm;
         P_ERR_NO  := 20406;
         P_Pkg_NM  :='Ars_Api_Chk_Pkg.Chk_Amt_And_Itm_Tax';  
End Chk_Amt_And_Itm_Tax;
--##-----------------------------------------------------------------------------------------------------##--
Procedure CHK_MNDTRY_FLIDS (P_Doc_Typ           IN  IAS_POST_DTL.DOC_TYPE%TYPE,
                            P_REP_CODE          IN  SALES_MAN.REPRS_CODE %Type  Default Null,
                            P_DOC_Desc          IN  IAS_POST_DTL.DOC_DESC %Type Default Null,
                            P_Use_Vat           In  Number Default Null , 
                            P_REF_NO            IN  Varchar2                    Default Null,
                            P_C_Code            IN  CUSTOMER.C_CODE %Type       Default Null,
                            P_Bill_Doc_Type     IN  CUSTOMER.C_CODE %Type       Default Null,
                            P_Lng_No            In     Number Default 1,
                            P_Msg_Txt           Out Varchar2,
                            P_ERR_NO          Out Varchar2,
                            P_Pkg_Nm            Out Varchar2     ) IS
      V_Cnt                      Number;
      V_Fnd                      Number := 0;
      V_Amt                      Number := 0;
      V_Msg_No                   Number;
      V_FORM_NO                  Number;
      V_Doc_Amt                  Number;
      V_Use_Vat                  Number;      
      V_Request_Refno_Ar         Number;
      V_Request_Desc_Ar          Number;
      V_Si_Repcode_Mandtry       Number;     
      V_Si_Pay_Csh_Cst_Mandtry   Number;     
BEGIN

 V_FORM_NO:= CASE WHEN P_Doc_Typ=4 Then 158 
                  when P_Doc_Typ=5 then 160
                  WHEN P_Doc_Typ=53 Then 156
                  WHEN P_Doc_Typ=52 Then 155
                  WHEN P_Doc_Typ=136 Then 821
                 else 0 end;
                 
                                         
  
      Begin
         Select Nvl (Use_Vat, 0)               
               ,IAS_GEN_PKG.GET_CNT('select 1  from IAS_MNDTRY_SCR_FIELDS where form_no='||V_FORM_NO||' and fld_nm=''REF_NO'' and nvl(FLD_ST,0)=1  and rownum<=1')
               ,IAS_GEN_PKG.GET_CNT('select 1  from IAS_MNDTRY_SCR_FIELDS where form_no='||V_FORM_NO||' and fld_nm=''A_DESC'' and nvl(FLD_ST,0)=1 and rownum<=1')
               ,IAS_GEN_PKG.GET_CNT('select 1  from IAS_MNDTRY_SCR_FIELDS where form_no='||V_FORM_NO||' and fld_nm=''REP_CODE'' and nvl(FLD_ST,0)=1 and rownum<=1')
               ,Nvl (Si_Pay_Csh_Cst_Mandtry, 0)               
           Into V_Use_Vat               
               ,V_Request_Refno_Ar
               ,V_Request_Desc_Ar
               ,V_Si_Repcode_Mandtry
               ,V_Si_Pay_Csh_Cst_Mandtry               
           From Ias_Para_Gen, Ias_Para_Ar;
      Exception
         When Others Then
             P_Err_No := 20241;
             P_Msg_Txt :=  'ERROR WHEN GET PARAMETER' ||chr(10) || Sqlerrm;
             Goto Rtn_Rslt;           
      End;
      V_Use_Vat:=nvl(P_Use_Vat,nvl(V_Use_Vat,0));
      --------------------------------------------------------------------------------------
        If nvl(V_Request_Refno_Ar,0) = 1 And P_Ref_No Is Null AND P_DOC_TYP IN(4,5)  Then
           P_Err_No := 20242;
           P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 143);
           Goto Rtn_Rslt;
        End If;

        --------------------------------------------------------------------------------------
        If nvl(V_Request_Desc_Ar,0) = 1 And P_DOC_Desc Is Null AND P_DOC_TYP IN(4,5)  Then
           P_Err_No := 20243;
           P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 146);
           Goto Rtn_Rslt;
        End If;

        --------------------------------------------------------------------------------------
        If nvl(V_Si_Repcode_Mandtry,0) = 1 And P_Rep_Code Is Null AND P_DOC_TYP IN(4,5) Then
           P_Err_No := 20244;
           P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 395);
           Goto Rtn_Rslt;
        End If;

        --------------------------------------------------------------------------------------
        If V_Si_Pay_Csh_Cst_Mandtry = 1 And P_Bill_Doc_Type = 1 And P_C_Code Is Null AND P_DOC_TYP=4  Then
           P_Err_No := 20245;
           P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 388);
           Goto Rtn_Rslt;
        End If;
      --------------------------------------------------------------------------------------
      --------------------------------------------------------------------------------------
      --------------------------------------------------------------------------------------
                                    
   --####################--
  <<Rtn_Rslt>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then    
      P_Msg_Txt :=  NVL(P_Msg_Txt,'Message Number Is Missing');
      P_ERR_NO := P_Err_No;
      P_Pkg_Nm :=   NVL(P_Pkg_Nm,'Ars_Api_Chk_Pkg.CHK_MNDTRY_FLIDS');
      Return;
   Else
      P_Msg_Txt:=  Null;
      P_ERR_NO :=  Null;
      P_Pkg_Nm :=  Null;   
   End If;
--####################-- 
Exception When Others then
         P_Msg_Txt := 'Error in CHK_MNDTRY_FLIDS '||sqlerrm;
         P_ERR_NO  := 20407;
         P_Pkg_NM  :='Ars_Api_Chk_Pkg.CHK_MNDTRY_FLIDS';                            
END CHK_MNDTRY_FLIDS;                           
--##-----------------------------------------------------------------------------------------------------##--
 Procedure Chk_Credit_Period (  P_CHK_CRDT_PRD    In     Number   --## 0-UNCHECK Credit_Period 1-CHECK_Credit_Period
                               ,P_C_Code          In     Customer.C_Code%Type
                               ,P_Doc_Ser         In     Ias_Post_Mst.Doc_Ser%Type Default Null
                               ,P_Doc_Date        In     Ias_Bill_Mst.Bill_Date%Type Default Null
                               ,P_Bill_Doc_Type   In     Ias_Bill_Mst.Bill_Doc_Type%Type
                               ,P_Stand_By        In     Ias_Bill_Mst.Stand_By%Type Default 0
                               ,P_Usr_No          In     User_R.U_Id%Type
                               ,P_Lng_No          In     Number Default 1
                               ,P_Msg_No           Out Number)
   Is
      V_Min_Idate                 Date;
      V_Min_Doc_Date              Date;
      V_Credit_Period             Number;     
      V_Ar_Allow_Sales_Prv_Dr     Number;
      V_CST_ALLOW_SALES_PRV_DR Number(1) := 0;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                --  ??C??E C???C? EC?E?? ?????C? E???I ?I????E ?CE?E U?? ??II?
      V_Ar_Chk_Prd_Aftr_Due       Number;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           --  EO??? ?E?E C???C? E?I C?C?E??C?
      V_Check_Credit_Period       Number;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              -- ?E?E C?C?E?C?
      V_Allow_Prd_Aftr_Due        Number;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  -- ?E?E C???C? E?I C?C?E??C?
      --V_Prnt_Rprt             Number:=0;
      V_Cnt_Acy                   Number := 0;
      V_F_Actv_Date               Date;
      V_T_Actv_Date               Date;
      V_Allw                      Number := 0;
      V_Paid_Instllmnt_Man        Number;
      V_No_Of_Decimal             Number;
      V_Allw_Excd_Credit_Period   Number := 0;
      V_Aralt                     Number;
      V_Lang_No                   Number := Nvl (P_Lng_No, 1);
      V_Msg_No                    Number;
      V_Crdt_St                   Number := 0;
      P_Msg_Txt    Varchar2(4000) := Null;
      P_Pkg_Nm     Varchar2(4000) := Null;
      P_Err_No   Int := Null;
   Begin
   
     If Nvl (P_CHK_CRDT_PRD, 0) = 0 Then
            P_Msg_Txt := NULL;
            P_Err_No :=NULL;
            V_Msg_No   :=Null;
            Return;
      End If; 
      --##------------------------------------------------------------------------------------------------------##--  
      Begin
         Select Nvl (Paid_Instllmnt_Man, 0), Nvl (No_Of_Decimal_Ar, 2), Nvl (Ar_Ac_Link_Type, 0)
           Into V_Paid_Instllmnt_Man, V_No_Of_Decimal, V_Aralt
           From Ias_Para_Ar;
      Exception
         When Others Then
            Null;
      End;

      --##------------------------------------------------------------------------------------------------------##--
      If Nvl (P_Stand_By, 0) = 0 Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           --- (1)
         ---------------------------------------------------------------------------------------------
         Begin
            Select Nvl (Ar_Allow_Sales_Prv_Dr, 0), Nvl (Ar_Chk_Prd_Aftr_Due, 0), Nvl (Check_Credit_Period, 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         --,NVL(Allw_Excd_Credit_Period,0)
              Into V_Ar_Allow_Sales_Prv_Dr, V_Ar_Chk_Prd_Aftr_Due, V_Check_Credit_Period                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   --,V_Allw_Excd_Credit_Period
              From Privilege_Fixed
             Where U_Id = P_Usr_No;
         Exception
            When Others Then
               V_Msg_No := 670;
               Goto Rtn_Rslt;
         End;

         ---------------------------------------------------------------------------------------------
         Begin
            Select Credit_Period
                  ,Decode (Nvl (V_Ar_Chk_Prd_Aftr_Due, 0), 1, Allow_Prd_Aftr_Due, 0)
                  ,F_Actv_Date
                  ,T_Actv_Date
                  ,NVL(CST_ALLOW_SALES_PRV_DR,0)
              Into V_Credit_Period
                  ,V_Allow_Prd_Aftr_Due
                  ,V_F_Actv_Date
                  ,V_T_Actv_Date
                  ,V_CST_ALLOW_SALES_PRV_DR
              From Customer
             Where C_Code = P_C_Code;
         Exception
            When Others Then
               V_Credit_Period := Null;
         End;

         ---------------------------------------------------------------------------------------------
         --## Check Inactive Custumer
         If V_F_Actv_Date Is Not Null Then
            If P_Doc_Date < V_F_Actv_Date Or P_Doc_Date > V_T_Actv_Date Then
               V_Msg_No := 1786;
               Goto Rtn_Rslt;
            End If;
         End If;

         ---------------------------------------------------------------------------------------------
         If nvl(V_Cst_Allow_Sales_Prv_Dr,0)=0 And nvl(V_Ar_Allow_Sales_Prv_Dr,0)=1 Then
             V_Ar_Allow_Sales_Prv_Dr :=0;
         ElsIf nvl(V_Cst_Allow_Sales_Prv_Dr,0)=1 And nvl(V_Ar_Allow_Sales_Prv_Dr,0)=0 Then
            V_Ar_Allow_Sales_Prv_Dr :=0;
         ElsIf nvl(V_Cst_Allow_Sales_Prv_Dr,0)=0 And nvl(V_Ar_Allow_Sales_Prv_Dr,0)=0 Then
            V_Ar_Allow_Sales_Prv_Dr :=0;
         ElsIf nvl(V_Cst_Allow_Sales_Prv_Dr,0)=1 And nvl(V_Ar_Allow_Sales_Prv_Dr,0)=1 Then
            V_Ar_Allow_Sales_Prv_Dr :=1;          
         End If; 
         ---------------------------------------------------------------------------------------------
         If Nvl (P_Bill_Doc_Type, 0) = 4 And ( (V_Check_Credit_Period = 1 And V_Credit_Period Is Not Null) Or V_Ar_Allow_Sales_Prv_Dr = 0) Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --- (2)
            If Nvl (V_Paid_Instllmnt_Man, 0) = 1 Then
               Begin
                  Select Min (I_Date)
                    Into V_Min_Idate
                    From Installment
                   Where C_Code = P_C_Code 
                   And Bill_Ser <> Nvl (P_Doc_Ser, -1)
                    And Trunc (Nvl (I_Amt, 0)) > (Trunc (Nvl (Paid_Amt, 0) + Nvl (Adj_Amt, 0)) + 1)
                     And Dr_No Is Null;
               Exception
                  When Others Then
                     V_Min_Idate := Null;
               End;
            Else
               Begin
                  Select Count (Distinct A_Cy)
                    Into V_Cnt_Acy
                    From Ias_Post_Dtl
                   Where C_Code = P_C_Code;
               Exception
                  When Others Then
                     V_Cnt_Acy := 1;
               End;

               Begin
                  Delete From Ias_Dr_Det_Tmp;
               Exception
                  When Others Then
                     Null;
               End;


               If V_Cnt_Acy = 1 Then
                  --Ias_Dstr_Cst_Dr_Amt_Acy;
                  Ias_Dstr_Cst_Dr_Pkg.Ias_Dstr_Cst_Dr_Amt_Acy_Prc (P_C_Code          => P_C_Code
                                                                  ,P_Doc_Date        => Null                                                                  
                                                                  ,P_Local_Cur       => Ias_Gen_Pkg.Get_Local_Cur
                                                                  ,P_Aralt           => V_Aralt
                                                                  ,P_User_No         => P_Usr_No
                                                                  ,P_No_Of_Decimal   => V_No_Of_Decimal);
               Else
                  --Ias_Dstr_Cst_Dr_Amt;
                  Ias_Dstr_Cst_Dr_Pkg.Ias_Dstr_Cst_Dr_Amt_Prc (P_C_Code          => P_C_Code
                                                              ,P_Doc_Date        => Null 
                                                              ,P_Local_Cur       => Ias_Gen_Pkg.Get_Local_Cur
                                                              ,P_Aralt           => V_Aralt
                                                              ,P_User_No         => P_Usr_No
                                                              ,P_No_Of_Decimal   => V_No_Of_Decimal);
               End If;

               Begin
                  --Select Min(To_Date(Doc_Date)+Decode(Doc_Type,0,Nvl(v_Credit_Period,0),0)) Into V_Min_Idate
                  Select Min (Doc_Date)
                    Into V_Min_Idate
                    From Ias_Si_Dr_Dtl_Tmp
                   Where C_Code = P_C_Code 
                   And Doc_Ser <> Nvl (P_Doc_Ser, -1)
                    And Trunc (Nvl (I_Amt, 0)) > (Trunc (Nvl (Paid_Amt, 0)) + 1);
               Exception
                  When Others Then
                     V_Min_Idate := Null;
               End;
            End If;

            Begin
               Delete From Ias_Si_Dr_Dtl_Tmp;
            Exception
               When Others Then
                  Null;
            End;

            -- gen_pkg.msgbox(null,V_Min_Idate+Nvl(V_Allow_Prd_Aftr_Due,0));
            ---------------------------------------------------------------------------------------------
            If V_Check_Credit_Period = 1 And (P_Doc_Date Between V_Min_Idate And V_Min_Idate + Nvl (V_Allow_Prd_Aftr_Due, 0) Or V_Allw_Excd_Credit_Period = 3) Then
               V_Allw := 3;
            Else
               V_Allw := V_Allw_Excd_Credit_Period;
            End If;

            ---------------------------------------------------------------------------------------------
            If P_Doc_Date >= V_Min_Idate + Nvl (V_Allow_Prd_Aftr_Due, 0) And V_Check_Credit_Period = 1 Then
               V_Msg_No := 1536;
               V_Crdt_St := 1;
            -- GOTO RTN_RSLT;
            Elsif V_Min_Idate Is Not Null And V_Ar_Allow_Sales_Prv_Dr = 0 Then
               V_Msg_No := 1537;
               V_Crdt_St := 1;
            -- GOTO RTN_RSLT;
            End If;

            ---------------------------------------------------------------------------------------------
            If (Nvl (V_Crdt_St, 0) = 1 And V_Allw = 1) Or V_Allw = 3 Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       --- (3)
               If Nvl (P_Stand_By, 0) = 0 And V_Allw = 1 Then
                  Goto Rtn_Rslt;
               End If;
            End If;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             --- (3)
         End If;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                --- (2)
      End If;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   --- (1)

     --##---------------------------------------------------------------------------------------------------------------------------------------##--
     <<Rtn_Rslt>>
      P_Msg_No := V_Msg_No;
   Exception
      When Others Then
         Raise_Application_Error (-20386, ' ERR WHEN Chk_Credit_Period' || Chr (10) || Sqlerrm);
   End Chk_Credit_Period;
--##-----------------------------------------------------------------------------------------------------##--
 Procedure Chk_Credit_Limit (  P_Chk_CrDT_LMIT  In    NUMBER --## 0 UNCHECKCredit_Limit  1- CHECK Credit_Limit
                              ,P_Doc_Date       In    Ias_Bill_Mst.Bill_Date%Type Default Null
                              ,P_Doc_Ser        In    Ias_Bill_Mst.BILL_Ser%Type
                              ,P_Bill_Doc_Type  In     Ias_Bill_Mst.BILL_Ser%Type                            
                              ,P_Ac_Code        In     Account.A_Code%Type Default Null
                              ,P_Ac_Code_Dtl    In     Ias_Bill_Mst.Ac_Code_Dtl%Type Default Null
                              ,P_C_CODE         In     Ias_Bill_Mst.C_CODE%Type Default Null
                              ,P_Cash_No        In     Ias_Bill_Mst.Cash_No%Type Default Null                              
                              ,P_Brn_No         In     Ias_Bill_Mst.Brn_No%Type Default Null
                              ,P_User_No        In     User_R.U_Id%Type Default Null
                              ,P_Cur_Code       In     Ias_Bill_Mst.Bill_Currency%Type Default Null
                              ,P_CUR_RATE       In     NUMBER
                              ,P_Frc_No         In     Number Default 2
                              ,P_Stand_By       In     Number Default 0                              
                              ,P_Fld_Doc_Ser    In     Varchar2
                              ,P_Fld_MST_AMT    In     Varchar2
                              ,P_Tbl_Mst_Nm     In     Varchar2
                              ,P_Tbl_Dtl_Nm     In     Varchar2   Default Null
                              ,P_Lng_No         In     Number Default 1
                              ,P_Msg_Txt        Out Varchar2
                              ,P_ERR_NO         Out Varchar2
                              ,P_Pkg_Nm         Out Varchar2)
   Is
   
       V_Net_Amt        Number;
       V_Amt            Number := 0;
       V_Amtf           Number := 0;
       V_Trns_Amt       Number := 0;
       V_Trns_Amtf      Number := 0;
       V_Ac_Code_Dtl    Ias_Bill_Mst.Ac_Code_Dtl%Type;
       V_Disc_Amt_Mst   Number;
       V_Disc_Amt_Dtl   Number;
       V_Doc_Amt        NUMBER:=0;
       V_Cc_Code      Ias_Bill_Mst.Cc_Code%Type;
       V_Pj_No         Ias_Bill_Mst.Pj_No%Type;
       V_Actv_No       Ias_Bill_Mst.Actv_No%Type; 
       V_QT_PRM_SER_MST       Ias_Bill_Mst.QT_PRM_SER%Type; 
       V_Is_Mst_Prm_Disc     NUMBER:=0;
       V_QT_PRM_DISC_DTL       Number;
                                     
       
      --------------------------------------------------
      V_Billamt             Number := 0;
      V_Inv_Dis_Limit       Number := 0;
      V_Inv_Dis_Limit_Itm   Number := 0;
      V_Dis_Per_Itm         Number := 0;
      V_Dis_Per             Number := 0;

      ----------------------------
      V_Min_Lmt             Number := 0;
      V_Max_Lmt             Number := 0;
      V_Min_Trns_Lmt        Number := 0;
      V_Max_Trns_Lmt        Number := 0;
      V_Pass                Number := 0;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           --## Pass 1=not allow ,2=allow ,3=allow with worning
      V_Pass_Prv            Number := 0;
      V_No_Chk_Prv          Number := 0;     
   Begin
      --------------------------------------------------------------------------------
      If Nvl (P_CHK_CRDT_LMIT, 0) = 0 Then
            P_Msg_Txt := NULL;
            P_Err_No :=NULL;
            Goto Rtn_Rslt;
      End If;
      --------------------------------------------------------------------------------
      /*If Nvl (P_Stand_By, 0) = 0 Then
            P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 670) || V_Inv_Dis_Limit || ' %';
            P_Err_No := 20246;
            Goto Rtn_Rslt;
      End If;*/
        BEGIN
               Execute Immediate '  SELECT (Nvl ('||P_Fld_MST_AMT||', 0) - Nvl (Disc_Amt, 0) + Nvl (Othr_Amt, 0) + Nvl (Vat_Amt, 0))
                                            ,Nvl ('||P_Fld_MST_AMT||', 0)
                                            ,Disc_Amt_Mst
                                           , Disc_Amt_Dtl 
                                            ,Cc_Code
                                            ,Pj_No 
                                            ,Actv_No 
                                            ,QT_PRM_SER                                
                                   FROM ' || P_Tbl_Mst_Nm || '  WHERE '|| P_Fld_Doc_Ser||' =' || P_Doc_Ser||' AND ROWNUM<=1'
                                        Into V_Net_Amt
                                            ,V_Doc_Amt
                                            ,V_Disc_Amt_Mst
                                            ,V_Disc_Amt_Dtl
                                            ,V_Cc_Code
                                            ,V_Pj_No 
                                            ,V_Actv_No
                                            ,V_QT_PRM_SER_MST;
        Exception When NO_DATA_FOUND THEN
                   V_Net_Amt      :=0;
                   V_Disc_Amt_Mst :=0;
                   V_Disc_Amt_Dtl :=0;                         
        WHEN Others Then
              P_Err_No := 20247;
              P_Msg_Txt :='ERROR WHEN CHECK  AMT  FROM   '||P_Tbl_MST_Nm||' '||chr(10) || Sqlerrm ;
              Goto Rtn_Rslt; 
        END;
    --------------------------------------------------------------------------------
       BEGIN
               Execute Immediate '  SELECT QT_PRM_SER                                
                                   FROM ' || P_Tbl_Mst_Nm || '  WHERE '|| P_Fld_Doc_Ser||' =' || P_Doc_Ser||' AND ROWNUM<=1'
                                        Into V_QT_PRM_SER_MST;
        Exception When  Others Then
            Null;
        END;
        
        BEGIN
               Execute Immediate '  SELECT sum((NVL(DIS_AMT_DTL,0)+NVL(DIS_AMT_DTL2,0)+NVL(DIS_AMT_DTL3,0))*nvl(I_QTY,0))                                 
                                     FROM ' || P_Tbl_Dtl_Nm || '  
                                   WHERE '|| P_Fld_Doc_Ser||' =' || P_Doc_Ser||'
                                   and QT_PRM_SER Is Not Null
                                   and  nvl(Ias_Qt_Prm_Pkg.Chk_Qt_Prm_Disc (QT_PRM_SER),0)=1'
                                        Into V_QT_PRM_DISC_DTL;
        Exception When  Others Then
            Null;
        END;
        
        If V_QT_PRM_SER_MST Is Not Null Then
            Begin
              V_Is_Mst_Prm_Disc:=Ias_Qt_Prm_Pkg.Chk_Qt_Prm_Disc (V_QT_PRM_SER_MST);
            Exception When  Others Then
                Null;
            END;
       End If;  
    --------------------------------------------------------------------------------
       If P_Cur_Code = Ias_Gen_Pkg.Get_Local_Cur Then
          V_Amt := Nvl (V_Net_Amt, 0);
          V_Amtf := 0;
          V_Trns_Amt := Nvl (V_Net_Amt, 0);
          V_Trns_Amtf := 0;
       Else
          V_Amt := (Nvl (V_Net_Amt, 0)) * Nvl (P_CUR_RATE, 1);
          V_Amtf := Nvl (V_Net_Amt, 0);
          V_Trns_Amt := Nvl (V_Net_Amt, 0) * Nvl (P_CUR_RATE, 1);
          V_Trns_Amtf := Nvl (V_Net_Amt, 0);
       End If;

       If P_Bill_Doc_Type In (1, 2, 3) Then
          V_Ac_Code_Dtl := P_Cash_No;
       Elsif P_Bill_Doc_Type = 4 Then
          V_Ac_Code_Dtl := P_C_Code;
       Elsif P_Bill_Doc_Type = 8 Then
          V_Ac_Code_Dtl := P_Ac_Code_Dtl;
       End If;
    --------------------------------------------------------------------------------       
      
     BEGIN
      Gls_Lmt_Pkg.Chk_Ac_Lmt (P_Dr_Cr          => 1
                             ,P_Doc_Date       => P_Doc_Date
                             ,P_Amt            => V_Amt
                             ,P_Amtf           => V_Amtf
                             ,P_Amt_Trns       => V_Trns_Amt
                             ,P_Amtf_Trns      => V_Trns_Amtf
                             ,P_Ac_Code        => P_Ac_Code
                             ,P_Ac_Code_Dtl    => V_Ac_Code_Dtl
                             ,P_Cc_Code        => V_Cc_Code
                             ,P_Pj_No          => V_Pj_No
                             ,P_Actv_No        => V_Actv_No
                             ,P_Brn_No         => P_Brn_No
                             ,P_User_No        => P_User_No
                             ,P_Cur_Code       => P_Cur_Code
                             ,P_Frc_No         => P_Frc_No
                             ,P_Min_Lmt        => V_Min_Lmt
                             ,P_Max_Lmt        => V_Max_Lmt
                             ,P_Min_Trns_Lmt   => V_Min_Trns_Lmt
                             ,P_Max_Trns_Lmt   => V_Max_Trns_Lmt
                             ,P_Pass           => V_Pass
                             ,P_Pass_Prv       => V_Pass_Prv
                             ,P_No_Chk_Prv     => V_No_Chk_Prv
                             ,P_Upd_Flg        => 0
                             ,P_Msg            => P_Msg_Txt
                             ,P_Lng            => P_Lng_No);
    Exception  When Others Then 
      P_Err_No := 20248;
      P_Msg_Txt :=  'ERR WHEN Chk_Credit_Limit ' ||chr(10) || Sqlerrm;
      Goto Rtn_Rslt; 
    END;                         

      --##----------------------------------------------------------------------------------------------------------##--
      If P_Msg_Txt Is Not Null Then
         If V_No_Chk_Prv = 1 Then
            If Nvl (P_Stand_By, 0) = 0 Then
               P_Err_No := 20249;
               Goto Rtn_Rslt;
            End If;
         End If;


         If V_Pass = 1 Or (V_Pass In (2, 3) And V_Pass_Prv = 1) Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --mm
            If Nvl (P_Stand_By, 0) = 0 Then
               P_Err_No := 20250;
               Goto Rtn_Rslt;
            End If;
         Elsif V_Pass In (2, 3) And V_Pass_Prv = 3 Then
            Ars_Api_Trns_Pkg.G_ALRT_MSG_TXT:=P_Msg_Txt;
            P_Msg_Txt := Null;
         End If;
      End If;

      --##----------------------------------------------------------------------------------------------------------##--
      Begin
         Select Inv_Dis_Lmt, Inv_Dis_Lmt_Itm
           Into V_Inv_Dis_Limit, V_Inv_Dis_Limit_Itm
           From Privilege_Fixed
          Where U_Id = P_User_No;
      Exception
         When Others Then
            P_Msg_Txt :='Privilege_Fixed '|| sqlerrm;--Ias_Gen_Pkg.Get_Msg (P_Lng_No, 670);
            P_Err_No := 20251;
            V_Inv_Dis_Limit := Null;
            Goto Rtn_Rslt;
      End;

      If Nvl (V_Doc_Amt, 0) > 0 Then
         V_Disc_Amt_Dtl:=Nvl(V_Disc_Amt_Dtl,0)- Nvl(V_QT_PRM_DISC_DTL,0);
         
         If Nvl(V_Is_Mst_Prm_Disc,0)>0 Then
           V_Disc_Amt_Mst:=0;
         End If;  
         
         V_Dis_Per := (100 * Nvl (V_Disc_Amt_Mst, 0)) / V_Doc_Amt;
         V_Dis_Per_Itm := (100 * (Nvl (V_Disc_Amt_Mst, 0) + Nvl (V_Disc_Amt_Dtl, 0))) / V_Doc_Amt;
      End If;
      V_Dis_Per:=round(V_Dis_Per,P_Frc_No);
      V_Dis_Per_Itm:=round(V_Dis_Per_Itm,P_Frc_No);

      If ( (Nvl (V_Dis_Per, 0) > NVL(V_Inv_Dis_Limit,0) AND V_Inv_Dis_Limit Is Not Null ) 
      Or (Nvl (V_Dis_Per_Itm, 0) > nvl(V_Inv_Dis_Limit_Itm,0) and V_Inv_Dis_Limit_Itm Is Not Null )) And (Nvl (V_Disc_Amt_Mst, 0) + Nvl (V_Disc_Amt_Dtl, 0)) > 0 Then
         If Nvl (P_Stand_By, 0) = 0 Then
            P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 919) || V_Inv_Dis_Limit || ' %';
            P_Err_No := 20252;
            Goto Rtn_Rslt;
         End If;
      End If;

     --##----------------------------------------------------------------------------------------------------------##--
     --####################--
     <<Rtn_Rslt>>
      If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then         
         P_Msg_Txt := NVL(P_Msg_Txt,'Message Number Is Missing');
         P_ERR_NO := P_Err_No;
         P_Pkg_NM   :=NVL(P_Pkg_Nm,'Ars_Api_Chk_Pkg.Chk_Credit_Limit');
         Return;
      ELSE
       P_Msg_Txt := NULL;
       P_Err_No :=NULL;
       P_Pkg_NM   :=NULL; 
      End If;
   --####################--  
   Exception When Others then
         P_Msg_Txt := 'Error in Chk_Credit_Limit '||sqlerrm;
         P_ERR_NO  := 20057;
         P_Pkg_NM  :='Ars_Api_Chk_Pkg.Chk_Credit_Limit';                          
   End Chk_Credit_Limit;
--##-----------------------------------------------------------------------------------------------------##--

Procedure Update_Other_Charges_OLD (P_Doc_Typ          In     Number
                               ,P_Doc_Ser          In     Number
                               ,P_Clc_Typ_No_Tax   In     Number
                               ,P_No_Of_Decimal    In     Number
                               ,P_Lng_No           In     Number Default 1
                               ,P_Msg_Txt             Out Varchar2
                               ,P_Err_No              Out Varchar2
                               ,P_Pkg_Nm              Out Varchar2)
Is
   V_Cnt         Number := 0;
   V_Cntf        Number := 0;
   V_Billamt     Number;
   V_Fbillamt    Number;
   V_Bill_Type   Number := 0;
Begin
   If P_Doc_Typ = 4 Then
      Begin
         Begin
            Update Ias_Bill_Dtl
               Set Othr_Amt        = 0
                  ,Othr_Amt_Itm    = 0
                  ,Othr_Amt_Disc   = 0
                  ,Vat_Amt_Othr    = 0
             Where Bill_Ser = P_Doc_Ser;
         Exception
            When Others Then
               Null;
         End;

         Begin
            Execute Immediate 'Select 1 From Other_Charges 
                                          Where Bill_Ser = ' || P_Doc_Ser || '
                                            And Bill_Type=1
                                            And Nvl(Inv_Item,0)=1            
                                            And RowNum <= 1' Into V_Cnt;
         Exception
            When No_Data_Found Then
               V_Cnt   := 0;
            When Others Then
               P_Err_No    := 20442;
               P_Msg_Txt   := 'error when get Other_Charges  ' ||chr(10) || Sqlerrm;
               Goto Rtn_Rslt;
         End;

         Begin
            Execute Immediate 'Select 1 From Sales_Charges 
                                                          Where Nvl(Inv_Item,0)=1    
                                                            And Nvl(Sc_Qty_Type,0)=2        
                                                            And RowNum <= 1' Into V_Cntf;
         Exception
            When No_Data_Found Then
               V_Cnt   := 0;
            When Others Then
               P_Err_No    := 20443;
               P_Msg_Txt   := 'error when get Sales_Charges  ' ||chr(10) || Sqlerrm;
               Goto Rtn_Rslt;
         End;

         If (Nvl (V_Cnt, 0) = 1) Then --And ( Nvl(:Ias_Bill_Dtl.amt,0)> 0 )
            Begin
               If Nvl (V_Cntf, 0) = 0 Then
                  Update Ias_Bill_Dtl A
                     Set Othr_Amt      =
                            (Select Sum (Decode (Nvl (Unit_Amt, 0), 0, (Nvl (Other_Charges_Items.Amt, 0) / Decode (Nvl (A.I_Qty, 0), 0, Decode (Nvl (A.Free_Qty, 0), 0, 1, A.Free_Qty), A.I_Qty)), Unit_Amt))
                               From Other_Charges_Items
                              Where Other_Charges_Items.Bill_Ser = A.Bill_Ser And Other_Charges_Items.Bill_Ser = P_Doc_Ser And Other_Charges_Items.I_Code = A.I_Code And Other_Charges_Items.Rcrd_No = A.Rcrd_No)
                        ,Othr_Amt_Itm      =
                            (Select Sum (Decode (Nvl (Unit_Amt, 0), 0, (Nvl (Other_Charges_Items.Amt, 0) / Decode (Nvl (A.I_Qty, 0), 0, Decode (Nvl (A.Free_Qty, 0), 0, 1, A.Free_Qty), A.I_Qty)), Unit_Amt))
                               From Other_Charges_Items
                              Where Other_Charges_Items.Bill_Ser = A.Bill_Ser And Other_Charges_Items.Bill_Ser = P_Doc_Ser And Other_Charges_Items.I_Code = A.I_Code And Other_Charges_Items.Rcrd_No = A.Rcrd_No)
                        ,Othr_Amt_Disc      =
                            (Select Abs (Sum (Decode (Nvl (Unit_Amt, 0), 0, (Nvl (Other_Charges_Items.Amt, 0) / Decode (Nvl (A.I_Qty, 0), 0, Decode (Nvl (A.Free_Qty, 0), 0, 1, A.Free_Qty), A.I_Qty)), Unit_Amt)))
                               From Other_Charges_Items
                              Where     Other_Charges_Items.Bill_Ser = A.Bill_Ser
                                    And Other_Charges_Items.Bill_Ser = P_Doc_Ser
                                    And Other_Charges_Items.I_Code = A.I_Code
                                    And Other_Charges_Items.Rcrd_No = A.Rcrd_No
                                    And Nvl (Other_Charges_Items.Amt, 0) < 0
                                    And Exists
                                           (Select 1
                                              From Sales_Charges
                                             Where Sc_No = Other_Charges_Items.Sc_No And Nvl (Use_Vat, 0) = 1 And Rownum <= 1))
                   Where Bill_Ser = P_Doc_Ser;

                  Update Item_Movement A
                     Set Othr_Amt      =
                            (Select Sum (Decode (Nvl (Unit_Amt, 0), 0, (Nvl (Other_Charges_Items.Amt, 0) / Decode (Nvl (A.I_Qty, 0), 0, Decode (Nvl (A.Free_Qty, 0), 0, 1, A.Free_Qty), A.I_Qty)), Unit_Amt))
                               From Other_Charges_Items
                              Where Other_Charges_Items.Bill_Ser = A.Doc_Ser And Other_Charges_Items.Bill_Ser = P_Doc_Ser And Other_Charges_Items.I_Code = A.I_Code And Other_Charges_Items.Rcrd_No = A.Rcrd_No)
                   Where Doc_Type = 1 And Doc_Ser = P_Doc_Ser;
               Else
                  Update Ias_Bill_Dtl A
                     Set Othr_Amt      =
                            (Select Sum (Nvl (Other_Charges_Items.Amt, 0) / Decode (Nvl (A.I_Qty, 0), 0, Decode (Nvl (A.Free_Qty, 0), 0, 1, A.Free_Qty), A.I_Qty))
                               From Other_Charges_Items
                              Where Other_Charges_Items.Bill_Ser = A.Bill_Ser And Other_Charges_Items.Bill_Ser = P_Doc_Ser And Other_Charges_Items.I_Code = A.I_Code And Other_Charges_Items.Rcrd_No = A.Rcrd_No)
                        ,Othr_Amt_Itm      =
                            (Select Sum (Nvl (Other_Charges_Items.Amt, 0) / Decode (Nvl (A.I_Qty, 0), 0, Decode (Nvl (A.Free_Qty, 0), 0, 1, A.Free_Qty), A.I_Qty))
                               From Other_Charges_Items
                              Where Other_Charges_Items.Bill_Ser = A.Bill_Ser And Other_Charges_Items.Bill_Ser = P_Doc_Ser And Other_Charges_Items.I_Code = A.I_Code And Other_Charges_Items.Rcrd_No = A.Rcrd_No)
                        ,Othr_Amt_Disc      =
                            (Select Abs (Sum (Nvl (Other_Charges_Items.Amt, 0) / Decode (Nvl (A.I_Qty, 0), 0, Decode (Nvl (A.Free_Qty, 0), 0, 1, A.Free_Qty), A.I_Qty)))
                               From Other_Charges_Items
                              Where     Other_Charges_Items.Bill_Ser = A.Bill_Ser
                                    And Other_Charges_Items.Bill_Ser = P_Doc_Ser
                                    And Other_Charges_Items.I_Code = A.I_Code
                                    And Other_Charges_Items.Rcrd_No = A.Rcrd_No
                                    And Nvl (Other_Charges_Items.Amt, 0) < 0
                                    And Exists
                                           (Select 1
                                              From Sales_Charges
                                             Where Sc_No = Other_Charges_Items.Sc_No And Nvl (Use_Vat, 0) = 1 And Rownum <= 1))
                   Where Bill_Ser = P_Doc_Ser;
               End If;
            Exception
               When Others Then
                  Null;
            End;
         End If;

         Begin
            Select Bill_Amt
              Into V_Billamt
              From Ias_Bill_Mst
             Where Bill_Ser = P_Doc_Ser And Rownum <= 1;

            If V_Billamt = 0 Then
               Begin
                  Select 1
                    Into V_Cnt
                    From Ias_Bill_Dtl
                   Where Bill_Ser = P_Doc_Ser And I_Qty > 0 And Rownum <= 1;
               Exception
                  When Others Then
                     Select Sum (Nvl (Free_Qty, 0) * Nvl (I_Price, 0))
                       Into V_Fbillamt
                       From Ias_Bill_Dtl
                      Where Bill_Ser = P_Doc_Ser;
               End;
            End If;
         Exception
            When Others Then
               Null;
         End;

         V_Cnt   := Ias_Gen_Pkg.Get_Cnt ('Select 1 From Other_Charges 
                                                          Where Bill_Ser =' || P_Doc_Ser || '
                                                            And Bill_Type=1
                                                            And Nvl(Inv_Item,0)=0                
                                                            And RowNum <= 1');

         If (Nvl (V_Cnt, 0) = 1) Then 
            Begin
               If Nvl (V_Fbillamt, 0) = 0 Then
                  Update Ias_Bill_Dtl A
                     Set Othr_Amt      =
                            (Select Nvl (A.Othr_Amt, 0) + (Sum (Nvl (Other_Charges.Amt, 0)) / Nvl (V_Billamt, 0)) * Nvl (A.I_Price, 0)
                               From Other_Charges
                              Where Other_Charges.Bill_Ser = A.Bill_Ser And Nvl (Other_Charges.Inv_Item, 0) = 0 And Other_Charges.Bill_Ser = P_Doc_Ser)
                        ,Othr_Amt_Disc      =
                            (Select Nvl (A.Othr_Amt_Disc, 0) + Abs (Sum (Nvl (Other_Charges.Amt, 0)) / Nvl (V_Billamt, 0)) * Nvl (A.I_Price, 0)
                               From Other_Charges
                              Where     Other_Charges.Bill_Ser = A.Bill_Ser
                                    And Nvl (Other_Charges.Inv_Item, 0) = 0
                                    And Other_Charges.Bill_Ser = P_Doc_Ser
                                    And Nvl (Other_Charges.Amt, 0) < 0
                                    And Exists
                                           (Select 1
                                              From Sales_Charges
                                             Where Sc_No = Other_Charges.Sc_No And Nvl (Use_Vat, 0) = 1 And Rownum <= 1))
                   Where Bill_Ser = P_Doc_Ser And Nvl (I_Qty, 0) > 0;


                  Update Item_Movement A
                     Set Othr_Amt      =
                            (Select Nvl (A.Othr_Amt, 0) + (Sum (Nvl (Other_Charges.Amt, 0)) / Nvl (V_Billamt, 0)) * Nvl (A.I_Cost, 0)
                               From Other_Charges
                              Where Other_Charges.Bill_Ser = A.Doc_Ser And Nvl (Other_Charges.Inv_Item, 0) = 0 And Other_Charges.Bill_Ser = P_Doc_Ser)
                   Where Doc_Type = 1 And Doc_Ser = P_Doc_Ser And Nvl (I_Qty, 0) > 0;
               Else
                  Update Ias_Bill_Dtl A
                     Set Othr_Amt      =
                            (Select Nvl (A.Othr_Amt, 0) + (Sum (Nvl (Other_Charges.Amt, 0)) / Nvl (V_Fbillamt, 0)) * Nvl (A.I_Price, 0)
                               From Other_Charges
                              Where Other_Charges.Bill_Ser = A.Bill_Ser And Nvl (Other_Charges.Inv_Item, 0) = 0 And Other_Charges.Bill_Ser = P_Doc_Ser)
                        ,Othr_Amt_Disc      =
                            (Select Nvl (A.Othr_Amt_Disc, 0) + Abs (Sum (Nvl (Other_Charges.Amt, 0)) / Nvl (V_Fbillamt, 0)) * Nvl (A.I_Price, 0)
                               From Other_Charges
                              Where     Other_Charges.Bill_Ser = A.Bill_Ser
                                    And Nvl (Other_Charges.Inv_Item, 0) = 0
                                    And Other_Charges.Bill_Ser = P_Doc_Ser
                                    And Nvl (Other_Charges.Amt, 0) < 0
                                    And Exists
                                           (Select 1
                                              From Sales_Charges
                                             Where Sc_No = Other_Charges.Sc_No And Nvl (Use_Vat, 0) = 1 And Rownum <= 1))
                   Where Bill_Ser = P_Doc_Ser;

                  Update Item_Movement A
                     Set Othr_Amt      =
                            (Select Nvl (A.Othr_Amt, 0) + (Sum (Nvl (Other_Charges.Amt, 0)) / Nvl (V_Fbillamt, 0)) * Nvl (A.I_Cost, 0)
                               From Other_Charges
                              Where Other_Charges.Bill_Ser = A.Doc_Ser And Nvl (Other_Charges.Inv_Item, 0) = 0 And Other_Charges.Bill_Ser = P_Doc_Ser)
                   Where Doc_Type = 1 And Doc_Ser = P_Doc_Ser;
               End If;
            Exception
               When Others Then
                  Null;
            End;
         End If;

         --##-------------------------------------------------------------------------------------##--
         Begin
            Update Ias_Bill_Mst
               Set Othr_Amt      =
                      (Select Round (Nvl (Sum (Amt), 0), P_No_Of_Decimal)
                         From Other_Charges
                        Where Bill_Type = 1 And Bill_Ser = P_Doc_Ser)
                  ,Othr_Amt_Disc      =
                      (Select Abs (Round (Nvl (Sum (Amt), 0), P_No_Of_Decimal))
                         From Other_Charges
                        Where     Bill_Type = 1
                              And Bill_Ser = P_Doc_Ser
                              And Nvl (Other_Charges.Amt, 0) < 0
                              And Exists
                                     (Select 1
                                        From Sales_Charges
                                       Where Sc_No = Other_Charges.Sc_No And Nvl (Use_Vat, 0) = 1 And Rownum <= 1))
             Where Bill_Ser = P_Doc_Ser;
         Exception
            When Others Then
               Null;
         End;

         --##-------------------------------------------------------------------------------------##--
         If Nvl (Ys_Tax_Pkg.Get_Clc_Tax_Typ (P_Clc_Typ_No_Tax), 0) = 0 Then
            Begin
               Update Ias_Bill_Mst A
                  Set Vat_Amt_Othr      =
                         (Select Sum (Nvl (Vat_Amt, 0))
                            From Other_Charges
                           Where Bill_Ser = A.Bill_Ser And Bill_Ser = P_Doc_Ser)
                Where Bill_Ser = P_Doc_Ser;

               Update Ias_Bill_Dtl A
                  Set Vat_Amt_Othr      =
                         (Select (Nvl (Ias_Bill_Mst.Vat_Amt_Othr, 0) / Nvl (Ias_Bill_Mst.Bill_Amt, 0)) * Nvl (A.I_Price, 0)
                            From Ias_Bill_Mst
                           Where Bill_Ser = A.Bill_Ser And Bill_Ser = P_Doc_Ser)
                Where Bill_Ser = P_Doc_Ser;

               Update Item_Movement A
                  Set Vat_Amt_Othr      =
                         (Select (Nvl (Ias_Bill_Mst.Vat_Amt_Othr, 0) / Nvl (Ias_Bill_Mst.Bill_Amt, 0)) * Nvl (A.I_Cost, 0)
                            From Ias_Bill_Mst
                           Where Bill_Ser = A.Doc_Ser And Bill_Ser = P_Doc_Ser)
                Where Doc_Type = 1 And Doc_Ser = P_Doc_Ser;
            Exception
               When Others Then
                  Null;
            End;
         Else
            Begin
               Update Ias_Bill_Mst A
                  Set Vat_Amt_Othr   = 0
                Where Bill_Ser = P_Doc_Ser;

               Update Ias_Bill_Dtl A
                  Set Vat_Amt_Othr   = 0
                Where Bill_Ser = P_Doc_Ser;

               Update Other_Charges A
                  Set Vat_Per = 0, Vat_Amt = 0
                Where Bill_Type = 1 And Bill_Ser = P_Doc_Ser;

               Update Item_Movement
                  Set Vat_Amt_Othr   = 0
                Where Doc_Type = 1 And Doc_Ser = P_Doc_Ser;
            Exception
               When Others Then
                  Null;
            End;
         End If;
      Exception
         When Others Then
            Null;
      End;
   Elsif P_Doc_Typ = 5 Then
      Null;
   End If;

  --####################--
  <<RTN_RSLT>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then      
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_Chk_Pkg.Update_Other_Charges');
      Return;
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;
   End If;
--####################--
Exception
   When Others Then
      P_Msg_Txt   := 'ERROR WHEN Update_Other_Charges' || Sqlerrm;
      P_Err_No    := 20444;
      P_Pkg_Nm    := 'Ars_Api_Chk_Pkg.Update_Other_Charges';
End Update_Other_Charges_OLD;
--##-----------------------------------------------------------------------------------------------------##--
Procedure Update_Other_Charges (P_Doc_Typ             In     Number
                                   ,P_Doc_Ser          In     Number
                                   ,P_Use_Vat          In     Number Default Null
                                   ,P_Clc_Typ_No_Tax      In     Number
                                   ,P_No_Of_Decimal       In     Number
                                   ,P_Bill_Type        In     Number
                                   ,P_CALC_TAX_AUTO_FLG   In     Number Default 0
                                   ,P_Fld_Doc_Ser         In     Varchar2
                                   ,P_TBL_OTHER_CHRG_NM   In     Varchar2
                                   ,P_Tbl_INPT_Mvmnt_Nm   In     Varchar2
                                   ,P_Tbl_Mst_Nm          In     Varchar2
                                   ,P_Tbl_Dtl_Nm          In     Varchar2
                                   ,P_Fld_Mst_Amt         In     Varchar2
                                   ,P_DIFF_AMT            In     Number Default Null
                                   ,P_Lng_No              In     Number Default 1
                                   ,P_Msg_Txt             Out Varchar2
                                   ,P_Err_No              Out Varchar2
                                   ,P_Pkg_Nm              Out Varchar2)
Is
   V_Cnt         Number := 0;
   V_Cntf        Number := 0;
   V_Billamt     Number:= 0;
   V_Fbillamt    Number:= 0;
   V_Bill_Type   Number := 0;
   V_Net_Billamt Number:= 0;
   V_Othr_Amt_Disc_MST NUMBER:= 0;
   V_OTHR_AMT_MST NUMBER:= 0;
   V_Othr_Amt_Disc_OTH NUMBER:= 0;
   V_Othr_Amt_OTH NUMBER:= 0;
   V_Othr_PER  NUMBER:= 0;
   V_Othr_DISC_PER  NUMBER:= 0;
   V_Vat_Amt       NUMBER:= 0;
   V_INPT_TAX_Amt  NUMBER:= 0;
   V_VAT_AMT_OTHR_MST  NUMBER:= 0;
   V_AMT_DIFF          NUMBER:=NVL(P_DIFF_AMT,0.1);
Begin
  ---------------------------------------------------------------------------------
--If P_Doc_Typ IN( 4,5) Then 
      BEGIN
        EXECUTE IMMEDIATE ' Select Nvl ('||P_Fld_Mst_Amt||', 0)
                                  ,Nvl ('||P_Fld_Mst_Amt||', 0) - Nvl (Disc_Amt_Dtl, 0) 
                                  ,NVL(Othr_Amt,0) 
                                  ,NVL(Othr_Amt_Disc,0)
                                  ,NVL(Vat_Amt_Othr,0)       
                            From '||P_Tbl_Mst_Nm||'
                               Where '||P_Fld_Doc_Ser||' = '||P_Doc_Ser||'
                               And Rownum <= 1'
                                Into V_Billamt
                                    ,V_Net_Billamt
                                    ,V_OTHR_AMT_MST
                                    ,V_OTHR_AMT_DISC_MST
                                    ,V_VAT_AMT_OTHR_MST;
      Exception
                When No_Data_Found Then
                   V_Cnt              := 0;
                   V_Billamt          := 0;
                   V_Net_Billamt      := 0;
                   V_OTHR_AMT_MST     := 0;
                   V_OTHR_AMT_DISC_MST:= 0;
                   V_VAT_AMT_OTHR_MST := 0;
                When Others Then
                   P_Err_No    := 20536;
                   P_Msg_Txt   := 'error when get Other_Charges  ' ||chr(10) || Sqlerrm;
                   Goto Rtn_Rslt;
      End;
       ---------------------------------------------------------------------------------  
       BEGIN
            EXECUTE IMMEDIATE ' Select  Sum (Nvl (Amt, 0)),Sum (Nvl (Vat_Amt, 0)) 
                                     From '||P_TBL_OTHER_CHRG_NM||' 
                                    Where Bill_Ser = '||P_DOC_SER||'
                                    And   Bill_Type='||P_Bill_Type||'
                                    And Nvl (Inv_Item, 0) = 0  '
                                    INTO V_Othr_Amt_OTH,V_Vat_Amt;
         Exception
                    When No_Data_Found Then
                       V_Othr_Amt_OTH   := 0;
                       V_Vat_Amt   := 0;
                    When Others Then
                       P_Err_No    := 20537;
                       P_Msg_Txt   := 'error when get Other_Charges  ' ||chr(10) || Sqlerrm;
                       Goto Rtn_Rslt;
         End;
      ---------------------------------------------------------------------------------  
       BEGIN
            EXECUTE IMMEDIATE ' Select  Sum (Nvl (TAX_AMT, 0))
                                     From '||P_Tbl_INPT_Mvmnt_Nm||' 
                                    Where DOC_SER = '||P_DOC_SER||'
                                    And   DOC_TYPE='||P_Doc_Typ||' '                                     
                                    INTO V_INPT_TAX_Amt;
         Exception
                    When No_Data_Found Then
                       V_INPT_TAX_Amt   := 0;
                    When Others Then
                       P_Err_No    := 20537;
                       P_Msg_Txt   := 'error when get '||P_Tbl_INPT_Mvmnt_Nm||'  ' ||chr(10) || Sqlerrm;
                       Goto Rtn_Rslt;
         End;
      ---------------------------------------------------------------------------------     
         BEGIN
            EXECUTE IMMEDIATE ' Select  Abs (Sum (Nvl (OTH.Amt, 0))) 
                                     From '||P_TBL_OTHER_CHRG_NM||'  OTH
                                    Where OTH.Bill_Ser = '||P_DOC_SER||'
                                          And OTH.Bill_Type='||P_Bill_Type||'
                                          And Nvl (OTH.Inv_Item, 0) = 0                                                                    
                                          And Nvl (OTH.Amt, 0) < 0
                                          And Exists
                                                 (Select 1
                                                    From Sales_Charges
                                                   Where Sc_No = OTH.Sc_No 
                                                   And Nvl (Use_Vat, 0) = 1 
                                                   And Nvl (Sc_Comm_Flg, 0) = 0 
                                                   And Rownum <= 1) '
                                    INTO V_Othr_Amt_Disc_OTH;
         Exception
                    When No_Data_Found Then
                       V_Othr_Amt_Disc_OTH   := 0;
                    When Others Then
                       P_Err_No    := 20538;
                       P_Msg_Txt   := 'error when get Other_Charges  ' ||chr(10) || Sqlerrm;
                       Goto Rtn_Rslt;
         End;
         ---------------------------------------------------------------------------------          
          IF NVL(V_Othr_Amt_mst,0)<>0 OR NVL(V_Othr_Amt_Disc_mst,0)<>0 THEN
            IF NVL(V_Othr_Amt_OTH,0)=0 AND NVL(V_Othr_Amt_Disc_OTH,0)=0 THEN  
                 P_Err_No    := 20539;
                 P_Msg_Txt   := ' Not Calculated Other_Charges For this Document ';
                 Goto Rtn_Rslt;
            END IF; 
          END IF; 
              
        IF NVL(V_Othr_Amt_OTH,0)<>0 OR NVL(V_Othr_Amt_Disc_OTH,0)<>0 THEN        
               If V_Billamt = 0 Then
                         Begin
                             EXECUTE IMMEDIATE 'Select 1             
                                                  From '||P_Tbl_DTL_Nm||'
                                                  Where '||P_Fld_Doc_Ser||' = '||P_Doc_Ser||' 
                                                 And nvl(I_Qty,0) > 0 And Rownum <= 1 ' 
                             Into V_Cnt;
                         Exception
                            When Others Then
                               EXECUTE IMMEDIATE ' Select Sum (Nvl (Free_Qty, 0) * Nvl (I_Price, 0))                 
                                                   From '||P_Tbl_DTL_Nm||'
                                                  Where '||P_Fld_Doc_Ser||' = '||P_Doc_Ser||' ' 
                                                         Into V_Fbillamt;
                        End;
               END IF;         
                
               If Nvl (V_Fbillamt, 0) = 0 Then               
                    
                      
                       IF Nvl (V_Billamt, 0)>0 THEN
                         V_Othr_PER        := Nvl(V_Othr_Amt_OTH, 0) / Nvl (V_Billamt, 0);
                       END IF;
                       
                       IF Nvl (V_Net_Billamt, 0)>0 THEN 
                         V_Othr_DISC_PER   := ABS(Nvl(V_Othr_Amt_Disc_OTH, 0) / Nvl (V_Net_Billamt, 0));
                       END IF;  
                   IF NVL(P_CALC_TAX_AUTO_FLG,0)=1 THEN
                            BEGIN        
                              EXECUTE IMMEDIATE '  Update '||P_Tbl_DTL_Nm||' A
                                                   Set Othr_Amt   ='||NVL(V_Othr_PER,0)||' * Nvl (A.I_Price, 0)
                                                      ,Othr_Amt_Disc ='||NVL(V_Othr_DISC_PER,0)||' * (Nvl (A.I_Price, 0) - Nvl (A.Dis_Amt_Dtl, 0) - Nvl (A.Dis_Amt_Dtl2, 0) - Nvl (A.Dis_Amt_Dtl3, 0))
                                                    Where '||P_Fld_Doc_Ser||' = '||P_Doc_Ser||'  
                                                      And Nvl (I_Qty, 0) > 0 ';
                            Exception
                                When No_Data_Found Then
                                  NULL;
                                When Others Then
                                   P_Err_No    := 20540;
                                   P_Msg_Txt   := 'error when get Other_Charges  ' ||chr(10) || Sqlerrm;
                                   Goto Rtn_Rslt;
                            End;
                    END IF;         
                    BEGIN
                      Update Item_Movement A
                               Set Othr_Amt      = NVL(V_Othr_PER,0) * Nvl (A.I_Cost, 0)                                    
                             Where Doc_Type = DECODE(P_DOC_TYP,4,1,5,3,NULL) And Doc_Ser = P_DOC_SER And Nvl (I_Qty, 0) > 0;
                       Exception When No_Data_Found Then
                          NULL;                        
                    End;                             
               ELSE
                   
                    IF Nvl (V_Fbillamt, 0)>0 THEN
                       V_Othr_PER        := Nvl(V_Othr_Amt_OTH, 0) / Nvl (V_Fbillamt, 0);                      
                       V_Othr_DISC_PER   := ABS(Nvl(V_Othr_Amt_Disc_OTH, 0) / Nvl (V_Fbillamt, 0));
                    END IF;   
                    
                   IF NVL(P_CALC_TAX_AUTO_FLG,0)=1 THEN 
                                BEGIN                
                                EXECUTE IMMEDIATE '  Update '||P_Tbl_DTL_Nm||' A
                                                       Set Othr_Amt   ='||NVL(V_Othr_PER,0)||' * Nvl (A.I_Price, 0)
                                                          ,Othr_Amt_Disc ='||NVL(V_Othr_DISC_PER,0)||' * Nvl (A.I_Price, 0)
                                                        Where '||P_Fld_Doc_Ser||' = '||P_Doc_Ser||'  
                                                           ';
                                Exception
                                    When No_Data_Found Then
                                      NULL;
                                    When Others Then
                                       P_Err_No    := 20541;
                                       P_Msg_Txt   := 'error when get Other_Charges  ' ||chr(10) || Sqlerrm;
                                       Goto Rtn_Rslt;
                                End;
                   END IF;  
                    
                     BEGIN
                      Update Item_Movement A
                               Set Othr_Amt      = NVL(V_Othr_PER,0) * Nvl (A.I_Cost, 0)                                    
                             Where Doc_Type =  DECODE(P_DOC_TYP,4,1,5,3,NULL) And Doc_Ser = P_DOC_SER ;                                    
                       Exception When No_Data_Found Then
                          NULL;                        
                    End;        
                 
               End If;       
         --##-------------------------------------------------------------------------------------##--
              IF NVL(P_CALC_TAX_AUTO_FLG,0)=1 THEN
                        BEGIN
                        EXECUTE IMMEDIATE 'Update '||P_Tbl_MST_Nm||'
                                      Set Othr_Amt      =Round ('||NVL(V_Othr_Amt_OTH,0)||','|| P_No_Of_Decimal||')                      
                                        ,Othr_Amt_Disc  =Abs (Round ('||NVL(V_Othr_Amt_Disc_OTH,0)||', '||P_No_Of_Decimal||'))                         
                              Where '||P_Fld_Doc_Ser||' = '||P_Doc_Ser||'  ';
                        EXCEPTION 
                          When No_Data_Found Then
                              NULL;
                            When Others Then
                               P_Err_No    := 20640;
                               P_Msg_Txt   := 'error when ON  Other_Charges  ' ||chr(10) || Sqlerrm;
                               Goto Rtn_Rslt;
                            END;   
                        If Nvl (Ys_Tax_Pkg.Get_Clc_Tax_Typ (P_Clc_Typ_No_Tax), 0) = 0 Then                    
                                BEGIN
                                EXECUTE IMMEDIATE 'Update '||P_Tbl_MST_Nm||'
                                                    Set Vat_Amt_Othr      ='||NVL(V_VAT_AMT,0)||'                                                                                      
                                                    Where '||P_Fld_Doc_Ser||' = '||P_Doc_Ser||'  ';
                                EXCEPTION 
                                  When No_Data_Found Then
                                      NULL;
                                    When Others Then
                                       P_Err_No    := 20641;
                                       P_Msg_Txt   := 'error when ON  Other_Charges  ' ||chr(10) || Sqlerrm;
                                       Goto Rtn_Rslt;
                                END; 
                                IF NVL(V_BILLAMT,0)>0 THEN
                                    BEGIN
                                        EXECUTE IMMEDIATE 'Update '||P_Tbl_DTL_Nm||'
                                                            Set Vat_Amt_Othr      =('||NVL(V_VAT_AMT,0)||' / '||NVL(V_BILLAMT,0)||') * Nvl (I_Price, 0)                                                                                     
                                                            Where '||P_Fld_Doc_Ser||' = '||P_Doc_Ser||'  ';
                                    EXCEPTION 
                                    When No_Data_Found Then
                                      NULL;
                                    When Others Then
                                       P_Err_No    := 20642;
                                       P_Msg_Txt   := 'error when ON  Other_Charges  ' ||chr(10) || Sqlerrm;
                                       Goto Rtn_Rslt;
                                    END;
                                END IF;    
                                                          
                          END IF;
              ELSE
                   -------------------
                  --## CHK Othr_Amt BETWEEN Master And Other_Charges                                                        
                   If round(Nvl (V_Othr_Amt_mst, 0),P_No_Of_Decimal)-round(Nvl (V_Othr_Amt_OTH, 0),P_No_Of_Decimal)>=V_AMT_DIFF Then
                          P_Err_No := 20542;
                          P_Msg_Txt := 'Check Data (Othr_Amt)'
                                           || chr(10)||' Between Master And '||P_TBL_OTHER_CHRG_NM||' '
                                           || chr(10)||' Master        Othr_Amt = ' || V_Othr_Amt_mst
                                           || chr(10)||' Other_Charges Othr_Amt = ' || V_Othr_Amt_OTH
                                           || chr(10)||'  diff = ' || abs(round((nvl(V_Othr_Amt_OTH,0)-nvl(V_Othr_Amt_mst,0)),4));
                          Goto Rtn_Rslt;
                   End If;                
                   -------------------              
                   --## CHK Othr_Amt_Disc BETWEEN Master And Other_Charges                                                        
                   If round(Nvl (V_Othr_Amt_Disc_mst, 0) ,P_No_Of_Decimal)- round(Nvl (V_Othr_Amt_Disc_OTH, 0),P_No_Of_Decimal)>=V_AMT_DIFF Then
                          P_Err_No := 20543;
                          P_Msg_Txt := 'Check Data (Othr_Amt_Disc)'
                                           || chr(10)||' Between Master And '||P_TBL_OTHER_CHRG_NM||' '
                                           || chr(10)||' Master        Othr_Amt_Disc = ' || V_Othr_Amt_Disc_mst
                                           || chr(10)||' Other_Charges Othr_Amt_Disc = ' || V_Othr_Amt_Disc_OTH
                                           || chr(10)||'  diff = ' || abs(round((nvl(V_Othr_Amt_Disc_mst,0)-nvl(V_Othr_Amt_Disc_OTH,0)),4));
                          Goto Rtn_Rslt;
                   End If;
                   -------------------------
                   --## CHK Vat_Amt_Othr BETWEEN Master And Other_Charges                                                        
                   If round(Nvl (V_VAT_AMT, 0),P_No_Of_Decimal) - round(Nvl (V_Vat_Amt_Othr_mst, 0),P_No_Of_Decimal) >=V_AMT_DIFF Then
                          P_Err_No := 20544;
                          P_Msg_Txt := 'Check Data (Vat_Amt_Othr)'
                                           || chr(10)||' Between Master And '||P_TBL_OTHER_CHRG_NM||' '
                                           || chr(10)||' Master        Vat_Amt_Othr = ' || V_Vat_Amt_Othr_mst
                                           || chr(10)||' Other_Charges Vat_Amt_Othr = ' || V_VAT_AMT
                                           || chr(10)||'  diff = ' || abs(round((nvl(V_Vat_Amt_Othr_mst,0)-nvl(V_VAT_AMT,0)),4));
                          Goto Rtn_Rslt;
                   End If;  
              END IF;        
        END IF;
        ----------------------------------------------------------------
        IF NVL(V_VAT_AMT,0)>0 AND  NVL(V_INPT_TAX_Amt,0)=0 THEN
                 IF NVL(P_CALC_TAX_AUTO_FLG,0)=1 And trim(upper(P_TBL_INPT_MVMNT_NM))=trim(upper('GNR_TAX_INPT_MOVMNT_BR')) THEN
                   Null;
                 Else               
                     P_Err_No    := 20550;
                     P_Msg_Txt   := ' Not Calculated TAX_INPT_MOVMNT For this Document ';                 
                     Goto Rtn_Rslt;
                End If;     
        END IF; 
        ----------------------------------------------------------------
         --## CHK Vat_Amt_Othr BETWEEN OTHER_CHRG And GNR_TAX_INPT_MOVMNT                                                        
           If round(Nvl (V_VAT_AMT, 0),P_No_Of_Decimal) - round(Nvl (V_INPT_TAX_Amt, 0),P_No_Of_Decimal)>=V_AMT_DIFF Then
              IF NVL(P_CALC_TAX_AUTO_FLG,0)=1 And trim(upper(P_TBL_INPT_MVMNT_NM))=trim(upper('GNR_TAX_INPT_MOVMNT_BR')) THEN
                   Null;
              Else  
                  P_Err_No := 20551;
                  P_Msg_Txt := 'Check Data (INPT_TAX_AMT)'
                                   || chr(10)||' Between '||P_TBL_OTHER_CHRG_NM||' And '||P_Tbl_INPT_Mvmnt_Nm||' '
                                   || chr(10)||' OTHER_CHRG        TAX_AMT = ' || Nvl (V_VAT_AMT, 0)
                                   || chr(10)||' TAX_INPT_MOVMNT   TAX_AMT = ' || Nvl (V_INPT_TAX_Amt, 0)
                                   || chr(10)||'  diff = ' || abs(round((nvl(V_VAT_AMT,0)-nvl(V_INPT_TAX_Amt,0)),4));
                  Goto Rtn_Rslt;
             End If;     
           End If; 
        ----------------------------------------------------------------
         BEGIN 
            Update Item_Movement A Set Vat_Amt_Othr =DECODE( Nvl (V_BILLAMT, 0),0,0,(Nvl (V_VAT_AMT, 0) / Nvl (V_BILLAMT, 0)) * Nvl (A.I_Cost, 0))                                         
                Where Doc_Type = DECODE(P_DOC_TYP,4,1,5,3,NULL) And Doc_Ser = P_Doc_Ser;
            Exception When Others Then
                  Null;
            End; 
   --Elsif P_Doc_Typ = 53 Then
      Null;
  -- End If;

  --####################--
  <<RTN_RSLT>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then      
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_Chk_Pkg.Update_Other_Charges');
      Return;
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;
   End If;
--####################--
Exception
   When Others Then
      P_Msg_Txt   := 'ERROR WHEN Update_Other_Charges' || Sqlerrm;
      P_Err_No    := 20545;
      P_Pkg_Nm    := 'Ars_Api_Chk_Pkg.Update_Other_Charges';
End Update_Other_Charges;
--##-----------------------------------------------------------------------------------------------------##--
Procedure Chk_Rt_Bill_Info (P_Rt_Bill_Ser       In     Ias_Rt_Bill_Mst.Rt_Bill_Ser%Type Default Null
                           ,P_RT_Bill_No        In     Ias_Rt_Bill_Mst.Rt_Bill_no%Type Default Null
                           ,P_P_Year            In     Number Default Null
                           ,P_Pst_Typ           In     Number Default Null
                           ,P_Bill_No           In     Ias_Bill_Mst.Bill_No%Type Default Null
                           ,P_Bill_Ser          In     Ias_Bill_Mst.Bill_Ser%Type Default Null
                           ,P_I_Code            In     Ias_Bill_Dtl.I_Code%Type Default Null
                           ,P_P_Size            In     Ias_Bill_Dtl.P_Size%Type Default Null
                           ,P_I_Qty             In     Ias_Bill_Dtl.I_Qty%Type Default Null
                           ,P_Free_Qty          In     Ias_Bill_Dtl.I_Qty%Type Default Null
                           ,P_Expiredate        In     Ias_Bill_Dtl.Expire_Date%Type Default Null
                           ,P_Batchno           In     Ias_Bill_Dtl.Batch_No%Type Default Null
                           ,P_Doc_Sequence_Si   In Out Number
                           ,P_Si_Rcrd_No        In Out Number
                           ,P_Lng_No            In     Number Default 1
                           ,P_Msg_Txt              Out Varchar2
                           ,P_Err_No               Out Varchar2
                           ,P_Pkg_Nm               Out Varchar2)
Is
   V_Cnt               Number := 0;
   V_Doc_Sequence_Si   Number;
   V_Si_Rcrd_No        Number;
   V_I_Qty             Number := 0;
   V_Free_Qty          Number := 0;
   V_Psize             Number;
   V_Out_Qty           Number := 0;
   V_Out_Fqty          Number := 0;
   V_Bill_Rtqty        Number := 0;
   V_Bill_Frtqty       Number := 0;
   V_Diff_Iqty         Number := 0;
   V_Diff_Fqty         Number := 0;
   V_Bill_Rtqty_Br     Number := 0;
   V_Bill_Frtqty_Br    Number := 0;
Begin
   If Nvl (P_P_Year, 0) In (0, 3) And P_P_Year Is Not Null Then
      If P_Bill_No Is Null Then
         P_Err_No    := 20472;
         P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 6136) || Chr (13) || 'I_CODE = ' || P_I_Code;
         Goto Rtn_Rslt;
      End If;

      If P_Bill_Ser Is Null Then
         P_Err_No    := 20473;
         P_Msg_Txt   := 'Err. You Send P_BILL_SER Is Null ' || Chr (13) || ' BILL_NO=' || P_Bill_No || Chr (13) || 'I_CODE = ' || P_I_Code;
         Goto Rtn_Rslt;
      End If;

      If Nvl (P_Pst_Typ, 0) = 2 Then
         -----------------------------------------------------------------
         Begin
            Select 1
              Into V_Cnt
              From Ias_Bill_Mst
             Where Bill_Ser = P_Bill_Ser And Bill_No = P_Bill_No And Rownum <= 1;
         Exception
            When No_Data_Found Then
               Begin
                  Select 1
                    Into V_Cnt
                    From Ias_Bill_Mst_Br
                   Where Bill_Ser = P_Bill_Ser And Bill_No = P_Bill_No And Rownum <= 1;
               Exception
                  When No_Data_Found Then
                     P_Err_No    := 20474;
                     P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5980) || Chr (13) || 'BILL_NO=' || P_Bill_No;
                     Goto Rtn_Rslt;
                  When Others Then
                     V_Cnt   := 0;
               End;

               If Nvl (V_Cnt, 0) = 1 Then
                  P_Err_No    := 20475;
                  P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5981) || Chr (13) || 'BILL_NO=' || P_Bill_No;
                  Goto Rtn_Rslt;
               End If;
            When Others Then
               V_Cnt   := 0;
         End;

         If Nvl (V_Cnt, 0) = 0 Then
            P_Err_No    := 20476;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 6136) || Chr (13) || 'I_CODE = ' || P_I_Code;
            Goto Rtn_Rslt;
         End If;
      -----------------------------------------------------------------
      Else
         Begin
            Select 1
              Into V_Cnt
              From (Select Bill_Ser
                      From Ias_Bill_Mst
                     Where Bill_Ser = P_Bill_Ser And Bill_No = P_Bill_No And Rownum <= 1
                    Union All
                    Select Bill_Ser
                      From Ias_Bill_Mst_Br
                     Where Bill_Ser = P_Bill_Ser And Bill_No = P_Bill_No And Rownum <= 1)
                     where Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If Nvl (V_Cnt, 0) = 0 Then
            P_Err_No    := 20477;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5980) || Chr (13) || 'BILL_NO=' || P_Bill_No;
            Goto Rtn_Rslt;
         End If;
      End If;

      -----------------------------------------------------------------
      Begin
         Select Count (*)
           Into V_Cnt
           From (Select Bill_No, Bill_Ser
                   From Ias_Bill_Dtl
                  Where Bill_Ser = P_Bill_Ser 
                  And Bill_No = P_Bill_No 
                  And I_Code = P_I_Code 
                  And Nvl (Expire_Date, '01/01/1900') = Nvl (P_Expiredate, '01/01/1900') 
                  And Nvl (Batch_No, '0') = Nvl (P_Batchno, '0')
                 Union All
                 Select M.Bill_No, M.Bill_Ser
                   From Ias_Bill_Mst_Br M, Ias_Bill_Dtl_Br D
                  Where     M.Bill_Ser = D.Bill_Ser
                        And M.Bill_Ser = P_Bill_Ser
                        And Nvl (M.Bill_Post, 0) = 0
                        And Nvl (M.Cncl_Flg, 0) = 0
                        And M.Bill_No = P_Bill_No
                        And I_Code = P_I_Code
                        And Nvl (Expire_Date, '01/01/1900') = Nvl (P_Expiredate, '01/01/1900')
                        And Nvl (Batch_No, '0') = Nvl (P_Batchno, '0')
                        And Not Exists
                               (Select 1
                                  From Ias_Bill_Mst
                                 Where Ias_Bill_Mst.Bill_Ser = M.Bill_Ser And Rownum <= 1));
      Exception
         When Others Then
            V_Cnt   := 0;
      End;


      If Nvl (V_Cnt, 0) = 0 Then
         P_Err_No    := 20478;
         P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5982) || Chr (13) || 'I_CODE =' || P_I_Code || Chr (13) || 'BILL_NO=' || P_Bill_No;
         Goto Rtn_Rslt;
      Elsif Nvl (V_Cnt, 0) = 1 Then
         Begin
            Select Doc_Sequence
                  ,Rcrd_No
                  ,I_Qty
                  ,Free_Qty
                  ,P_Size
              Into P_Doc_Sequence_Si
                  ,P_Si_Rcrd_No
                  ,V_I_Qty
                  ,V_Free_Qty
                  ,V_Psize
              From (Select Bill_No
                          ,Bill_Ser
                          ,Doc_Sequence
                          ,Rcrd_No
                          ,I_Qty
                          ,Free_Qty
                          ,P_Size
                      From Ias_Bill_Dtl
                     Where Bill_Ser = P_Bill_Ser And Bill_No = P_Bill_No And I_Code = P_I_Code And Nvl (Expire_Date, '01/01/1900') = Nvl (P_Expiredate, '01/01/1900') And Nvl (Batch_No, '0') = Nvl (P_Batchno, '0')
                    Union All
                    Select M.Bill_No
                          ,M.Bill_Ser
                          ,Doc_Sequence
                          ,Rcrd_No
                          ,I_Qty
                          ,Free_Qty
                          ,P_Size
                      From Ias_Bill_Mst_Br M, Ias_Bill_Dtl_Br D
                     Where     M.Bill_Ser = D.Bill_Ser
                           And M.Bill_Ser = P_Bill_Ser
                           And Nvl (M.Bill_Post, 0) = 0
                           And Nvl (M.Cncl_Flg, 0) = 0
                           And M.Bill_No = P_Bill_No
                           And I_Code = P_I_Code
                           And Nvl (Expire_Date, '01/01/1900') = Nvl (P_Expiredate, '01/01/1900')
                           And Nvl (Batch_No, '0') = Nvl (P_Batchno, '0')
                           And Not Exists
                                  (Select 1
                                     From Ias_Bill_Mst
                                    Where Ias_Bill_Mst.Bill_Ser = M.Bill_Ser And Rownum <= 1));
         Exception
            When Others Then
               Null;
         End;
      Elsif Nvl (V_Cnt, 0) > 1 Then
         If P_Si_Rcrd_No Is Null Then
            P_Err_No    := 20479;
            P_Msg_Txt   := ' P_Si_Rcrd_No Is Null ' || Chr (13) || 'I_CODE =' || P_I_Code || Chr (13) || 'BILL_NO=' || P_Bill_No;
            Goto Rtn_Rslt;
         End If;

         Begin
            Select Doc_Sequence
                  ,Rcrd_No
                  ,I_Qty
                  ,Free_Qty
                  ,P_Size
              Into P_Doc_Sequence_Si
                  ,P_Si_Rcrd_No
                  ,V_I_Qty
                  ,V_Free_Qty
                  ,V_Psize
              From (Select Bill_No
                          ,Bill_Ser
                          ,Doc_Sequence
                          ,Rcrd_No
                          ,I_Qty
                          ,Free_Qty
                          ,P_Size
                      From Ias_Bill_Dtl
                     Where Bill_Ser = P_Bill_Ser And Bill_No = P_Bill_No And I_Code = P_I_Code 
                     And Nvl (Expire_Date, '01/01/1900') = Nvl (P_Expiredate, '01/01/1900') 
                     And Nvl (Batch_No, '0') = Nvl (P_Batchno, '0') 
                     And (Nvl (Rcrd_No, 0) = Nvl (P_Si_Rcrd_No, 0) Or Nvl (Rcrd_No_Br, 0) = Nvl (P_Si_Rcrd_No, 0))
                    Union All
                    Select M.Bill_No
                          ,M.Bill_Ser
                          ,Doc_Sequence
                          ,Rcrd_No
                          ,I_Qty
                          ,Free_Qty
                          ,P_Size
                      From Ias_Bill_Mst_Br M, Ias_Bill_Dtl_Br D
                     Where     M.Bill_Ser = D.Bill_Ser
                           And M.Bill_Ser = P_Bill_Ser
                           And Nvl (M.Bill_Post, 0) = 0
                           And Nvl (M.Cncl_Flg, 0) = 0
                           And M.Bill_No = P_Bill_No
                           And I_Code = P_I_Code
                           And Nvl (Expire_Date, '01/01/1900') = Nvl (P_Expiredate, '01/01/1900')
                           And Nvl (Batch_No, '0') = Nvl (P_Batchno, '0')
                           And Nvl (Rcrd_No, 0) = Nvl (P_Si_Rcrd_No, 0)
                           And Not Exists
                                  (Select 1
                                     From Ias_Bill_Mst
                                    Where Ias_Bill_Mst.Bill_Ser = M.Bill_Ser And Rownum <= 1))
             Where Rownum <= 1;
         Exception
            When Others Then
               P_Err_No    := 20480;
               P_Msg_Txt   := ' Error when Get Bill data for P_Si_Rcrd_No' || P_Si_Rcrd_No || Chr (13) || 'I_CODE =' || P_I_Code || Chr (13) || 'BILL_NO=' || P_Bill_No;
               Goto Rtn_Rslt;
         End;
      End If;

      -----------------------------------------------------------------
      Begin
         Select Nvl (Sum (B.P_Qty), 0), Nvl (Sum (NVL(B.Free_Qty,0)* Nvl (B.P_Size, 1)) , 0)
           Into V_Bill_Rtqty, V_Bill_Frtqty
           From Ias_Rt_Bill_Mst A, Ias_Rt_Bill_Dtl B
          Where A.Rt_Bill_Ser = B.Rt_Bill_Ser And B.Bill_Ser = P_Bill_Ser 
           And B.I_Code = P_I_Code And Nvl (B.Si_Rcrd_No, 0) = Nvl (P_Si_Rcrd_No, 0) And A.P_Year In (0, 3);
      Exception
         When Others Then
            V_Bill_Rtqty    := 0;
            V_Bill_Frtqty   := 0;
      End;

      Begin
         Select Nvl (Sum (B.P_Qty), 0), Nvl (Sum (NVL(B.Free_Qty,0)* Nvl (B.P_Size, 1)) , 0)
           Into V_Bill_Rtqty_Br, V_Bill_Frtqty_Br
           From Ias_Rt_Bill_Mst_Br A, Ias_Rt_Bill_Dtl_Br B
          Where     A.Rt_Bill_Ser = B.Rt_Bill_Ser
                And B.Bill_Ser = P_Bill_Ser
                And A.Rt_Bill_Ser <> Nvl (P_Rt_Bill_Ser, 0)
                And B.I_Code = P_I_Code
                And Nvl (B.Si_Rcrd_No, 0) = Nvl (P_Si_Rcrd_No, 0)
                And A.P_Year In (0, 3)
                And Nvl (A.Rt_Bill_Post, 0) = 0
                And Nvl (A.Cncl_Flg, 0) = 0
                And Not Exists
                       (Select 1
                          From Ias_Rt_Bill_Mst
                         Where Ias_Rt_Bill_Mst.Rt_Bill_Ser = A.Rt_Bill_Ser And Rownum <= 1);
      Exception
         When Others Then
            V_Bill_Rtqty_Br    := 0;
            V_Bill_Frtqty_Br   := 0;
      End;

      If Nvl (P_P_Year, 0) = 3 Then
         Begin
            Select Nvl (Sum (P_Qty), 0), Nvl (Sum (NVL(Free_Qty,0)* Nvl (P_Size, 1)) , 0)
              Into V_Out_Qty, V_Out_Fqty
              From Detail_Out_Bills
             Where Bill_Ser = P_Bill_Ser And I_Code = P_I_Code And Nvl (Rcrd_No, 0) = Nvl (P_Si_Rcrd_No, 0);
         Exception
            When Others Then
               V_Out_Qty    := 0;
               V_Out_Fqty   := 0;
         End;
      End If;

      V_Diff_Iqty   := ( (Nvl (V_I_Qty, 0) * Nvl (V_Psize, 1)) - (Nvl (V_Bill_Rtqty, 0) + Nvl (V_Bill_Rtqty_Br, 0) + Nvl (V_Out_Qty, 0))) / Nvl (P_P_Size, 1);
      V_Diff_Fqty   := ( (Nvl (V_Free_Qty, 0) * Nvl (V_Psize, 1)) - (Nvl (V_Bill_Frtqty, 0) + Nvl (V_Bill_Frtqty_Br, 0) + Nvl (V_Out_Fqty, 0))) / Nvl (P_P_Size, 1);

      If Nvl (P_I_Qty, 0) > V_Diff_Iqty Then
         If (Nvl (V_Bill_Rtqty, 0) + Nvl (V_Bill_Rtqty_Br, 0)) <> 0 Then
            P_Err_No    := 20145;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 907) || V_I_Qty || Chr (13) 
                          || Ias_Gen_Pkg.Get_Msg (P_Lng_No, 908) || (Nvl (V_Bill_Rtqty, 0) + Nvl (V_Bill_Rtqty_Br, 0)) / Nvl (P_P_Size, 1) || Chr (13) 
                          || Ias_Gen_Pkg.Get_Msg (P_Lng_No, 909) || V_Diff_Iqty || Chr (13)
                          || 'I_CODE =' || P_I_Code || Chr (13) 
                          || 'RT_BILL_NO=' || P_RT_Bill_No 
                          || 'BILL_NO=' || P_Bill_No;
            Goto Rtn_Rslt;
         Else
            P_Err_No    := 20481;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 910) || V_Diff_Iqty  || Chr (13) 
                            || 'I_CODE =' || P_I_Code|| Chr (13) 
                            || 'RT_BILL_NO='|| P_RT_Bill_No || Chr (13) 
                            || 'BILL_NO=' || P_Bill_No;
           Goto Rtn_Rslt;                            
         End If;
      End If;
      
      If Nvl (P_free_Qty, 0) > nvl(V_Diff_Fqty,0) Then
            P_Err_No    := 20482;
            P_Msg_Txt   :=   Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 433)|| Chr (13)  
                            ||Ias_Gen_Pkg.Get_Msg (P_Lng_No, 910) || V_Diff_fqty || Chr (13) 
                            || 'I_CODE =' || P_I_Code|| Chr (13) 
                            || 'RT_BILL_NO=' || P_RT_Bill_No || Chr (13) 
                            || 'BILL_NO=' || P_Bill_No;
           Goto Rtn_Rslt;
      End if;
      
            
   End If;

  --##---------------------------------------------------------------------------------------------##--
  --####################--
  <<Rtn_Rslt>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_Chk_Pkg.Chk_Rt_Bill_Info');
      Return;
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;
   End If;
--####################--
Exception
   When Others Then
      P_Msg_Txt   := 'Error in Chk_Rt_Bill_Info ' || Sqlerrm;
      P_Err_No    := 20483;
      P_Pkg_Nm    := 'Ars_Api_Chk_Pkg.Chk_Rt_Bill_Info';
End Chk_Rt_Bill_Info;                         
--##-----------------------------------------------------------------------------------------------------##-- 
Procedure CHK_RETRN_BILL_INSTLL(P_SYS_NO            In NUMBER                               
                               ,P_rep_code          In Varchar2 Default Null 
                               ,P_c_code            In Varchar2 Default Null 
                               ,P_RT_BILL_DOC_TYPE  In ias_rt_bill_mst.RT_BILL_DOC_TYPE%TYPE 
                               ,P_Bill_Currency     In ias_bill_mst.Bill_Currency%TYPE
                               ,P_W_code            In ias_rt_bill_mst.w_code%TYPE       Default Null
                               ,P_RT_BILL_DATE      In ias_rt_bill_mst.RT_BILL_DATE%TYPE Default Null
                               ,P_Use_Vat           In     Number Default Null
                               ,P_CLC_TYP_NO_TAX    in number Default Null
                               ,P_p_year            In ias_rt_bill_mst.P_year%TYPE
                               ,P_Prev_Year         In Number
                               ,P_Brn_No            In S_brn.Brn_no%TYPE Default Null
                               ,P_Brn_Usr           In Number                                                                                        
                               ,P_Rt_Bill_Ser       In     Ias_Rt_Bill_Mst.Rt_Bill_Ser%Type Default Null
                               ,P_RT_Bill_No        In     Ias_Rt_Bill_Mst.Rt_Bill_no%Type Default Null                               
                               ,P_Pst_Typ           In     Number Default Null
                               ,P_Bill_No           In     Ias_Bill_Mst.Bill_No%Type Default Null
                               ,P_Bill_Ser          In     Ias_Bill_Mst.Bill_Ser%Type Default Null
                               ,P_I_Code            In     Ias_Bill_Dtl.I_Code%Type Default Null
                               ,P_P_Size            In     Ias_Bill_Dtl.P_Size%Type Default Null
                               ,P_I_Qty             In     Ias_Bill_Dtl.I_Qty%Type Default Null
                               ,P_Free_Qty          In     Ias_Bill_Dtl.I_Qty%Type Default Null
                               ,P_Expiredate        In     Ias_Bill_Dtl.Expire_Date%Type Default Null
                               ,P_Batchno           In     Ias_Bill_Dtl.Batch_No%Type Default Null
                               ,P_Doc_Sequence_Si   In Out Number
                               ,P_Si_Rcrd_No        In Out Number
                               ,P_Rtrn_From_Othr_Sman       In Number Default 0   --## 0 same sman-1 other sman                                 
                               ,P_Usr_no            In Number 
                               ,P_Lng_No            In     Number Default 1
                               ,P_Msg_Txt              Out Varchar2
                               ,P_Err_No               Out Varchar2
                               ,P_Pkg_Nm               Out Varchar2)
Is
   V_Cnt               Number := 0;
   V_Doc_Sequence_Si   Number;
   V_Si_Rcrd_No        Number;  
   V_MUST_RET_SAME_WCODE   Number(1) := 0;
   V_AR_WC_TYPE    Number(1) := 0;
   V_use_vat    Number(1) := 0;
   v_found    Number(1) := 0;
   V_YR      Varchar2(500);
   V_w_code_bill ias_rt_bill_mst.w_code%TYPE;
   V_Rep_code_bill ias_rt_bill_mst.Rep_code%TYPE;
   V_Ar_Return_Period  NUMBER;
   V_Check_Ret_Per    Number;
Begin
   If Nvl (P_P_Year, 0)=2 then
     Return;
   End if;
   
   If Nvl (P_P_Year, 0) In (0,1, 3) And P_P_Year Is Not Null Then
      If P_Bill_No Is Null Then
         P_Err_No    := 20456;
         P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 6136) || Chr (13) || 'I_CODE = ' || P_I_Code;
         Goto Rtn_Rslt;
      End If;
     ---------------------------------------------------------------------------
      If P_Bill_Ser Is Null Then
         P_Err_No    := 20457;
         P_Msg_Txt   := 'Err. You Send P_BILL_SER Is Null ' || Chr (13) || ' BILL_NO=' || P_Bill_No || Chr (13) || 'I_CODE = ' || P_I_Code;
         Goto Rtn_Rslt;
      End If;
      ---------------------------------------------------------------------------
      BEGIN
        SELECT NVL(MUST_RET_SAME_WCODE,0),NVL(AR_WC_TYPE,0),nvl(use_vat,0),Return_Period   
        INTO V_MUST_RET_SAME_WCODE,V_AR_WC_TYPE,V_use_vat,V_Ar_Return_Period
        FROM IAS_PARA_AR,IAS_PARA_gen;
      EXCEPTION WHEN OTHERS THEN 
        NULL;
      END;          
      ---------------------------------------------------------------------------
      Begin
         Select Nvl(Check_Ret_Per,0)
           Into V_Check_Ret_Per 
           From Privilege_Fixed
          Where U_id=P_Usr_no
            And RowNum<=1;
      Exception When Others Then 
          V_Check_Ret_Per:=0;
      End;
      ---------------------------------------------------------------------------
        V_use_vat:=nvl(P_use_vat,nvl(V_use_vat,0));
      ---------------------------------------------------------------------------      
       V_YR:= 'IAS'||P_PREV_YEAR||P_BRN_USR;
      ---------------------------------------------------------------------------
      Begin
        Execute Immediate '
                select w_code,rep_code 
                from (
                select w_code,rep_code  FROM '||V_YR||'.Ias_Bill_Mst
                where bill_ser='||P_Bill_Ser||' 
                union all
                select w_code,rep_code  FROM '||V_YR||'.Ias_Bill_Mst_BR
                where bill_ser='||P_Bill_Ser||' 
                ) where rownum<=1 ' 
       Into  V_w_code_bill,V_Rep_code_bill;
       EXCEPTION WHEN OTHERS THEN 
        NULL;
      END;  
      ---------------------------------------------------------------------------
       If nvl(P_SYS_NO,0)=70 And V_Rep_code_bill Is Null Then
          P_Err_No    := 20689;
          P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 899) 
                             || Chr (13) || 'BILL_NO=' || P_Bill_No
                             || Chr (13) || 'PREV_YEAR=' || P_PREV_YEAR;
          Goto Rtn_Rslt;
       End if;
      ---------------------------------------------------------------------------
        If P_W_code is null And Nvl (V_MUST_RET_SAME_WCODE, 0) = 1 and  nvl(P_SYS_NO,0)<>70 Then 
          P_Err_No    := 20458;
          P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 100) || Chr (13) || 'BILL_NO=' || P_Bill_No;
          Goto Rtn_Rslt;
        End If;
      ---------------------------------------------------------------------------
       If P_Bill_Currency is null Then
          P_Err_No    := 20459;
          P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 921) || Chr (13) || 'BILL_NO=' || P_Bill_No;
          Goto Rtn_Rslt;
        End If;
      ---------------------------------------------------------------------------
       If nvl(V_use_vat,0)=1 and P_CLC_TYP_NO_TAX is null Then
          P_Err_No    := 20460;
          P_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => p_Lng_No, P_Msg_No => 1601) || ' ' || Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 12526) || ' ,CLC_TYP_NO_TAX IS NULL ';          
          Goto Rtn_Rslt;
        End If;
      ---------------------------------------------------------------------------
       
         FOR J IN(select  * 
                     from table( Ars_Api_Instll_Doc_Pkg.GET_BILL_MST (  P_SYS_NO            =>P_SYS_NO,
                                                                        P_rep_code          =>V_Rep_code_bill,
                                                                        p_Bill_ser          =>p_Bill_ser,
                                                                        P_c_code            =>P_c_code,
                                                                        P_RT_BILL_DOC_TYPE  => P_RT_BILL_DOC_TYPE,
                                                                        P_Bill_Currency     =>P_Bill_Currency,
                                                                        P_W_code            =>V_w_code_bill,
                                                                        P_RT_BILL_DATE      => P_RT_BILL_DATE,
                                                                        P_p_year            =>P_p_year, 
                                                                        P_Prev_Year         =>P_Prev_Year,                                                                        
                                                                        P_Brn_Usr           =>P_Brn_Usr,
                                                                        P_shw_all_qty       =>1    ,
                                                                        P_Rtrn_From_Othr_Sman=>0,
                                                                        P_Usr_no            =>P_Usr_no,
                                                                        P_lng_no            =>P_lng_no  ))  )
     lOOP

               v_found:=1;
               If J.Bill_Currency <> P_Bill_Currency Then
                  P_Err_No    := 20461;
                  P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 903) ||J.Bill_Currency|| Chr (13) 
                                    ||Ias_Gen_Pkg.Get_Msg (P_Lng_No, 904) ||P_Bill_Currency|| Chr (13) || 'BILL_NO=' || P_Bill_No;
                  Goto Rtn_Rslt;                  
               End If;
               --------------------------------------
               If nvl(P_RT_BILL_DOC_TYPE,0)= 4 Then
                 If nvl(j.C_Code,'0') <> nvl(P_c_code,'0') Then   
                    P_Err_No    := 20462;
                    P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 905) ||j.C_Code|| Chr (13) 
                                    ||Ias_Gen_Pkg.Get_Msg (P_Lng_No, 906) ||P_c_code|| Chr (13) || 'BILL_NO=' || P_Bill_No;
                  Goto Rtn_Rslt;                  
                 End If;
               end if;                             
               --------------------------------------
                If Nvl (V_use_vat, 0) = 1  and nvl(j.CLC_TYP_NO_TAX,0)<>nvl(P_CLC_TYP_NO_TAX,0) Then
                  P_Err_No    := 20464;
                  P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 4778) || Chr (13) || 'BILL_NO=' || P_Bill_No;
                  Goto Rtn_Rslt;
               End If;
               --------------------------------------
                If Nvl (P_Pst_Typ, 0) = 2  and nvl(j.BILL_POST,0)=0  Then
                  P_Err_No    := 20465;
                  P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5981) || Chr (13) || 'BILL_NO=' || P_Bill_No;
                  Goto Rtn_Rslt;
               End If;
      
       --=========================================================--- 
       --=========================================================---
        Begin          
           select count(*) into v_cnt from table( Ars_Api_Instll_Doc_Pkg.GET_BILL_dtl( P_BILL_SER    =>J.BILL_SER,
                                                                      P_p_year      =>P_p_year, 
                                                                      P_Prev_Year   =>P_Prev_Year,
                                                                      P_Brn_Usr     =>P_Brn_Usr,
                                                                      P_shw_all_qty =>1   ,
                                                                      P_Usr_no      =>P_Usr_no,
                                                                      P_lng_no      =>P_lng_no  )) 
                         Where i_code=p_i_code
                          And Nvl (Expire_Date, '01/01/1900') = Nvl (P_Expiredate, '01/01/1900') 
                          And Nvl (Batch_No, '0') = Nvl (P_Batchno, '0');
                                                     
        Exception when others then
          v_cnt:=0;
        End;
        
        If nvl(V_Cnt,0)=0 then
              P_Err_No    := 20466;
             P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5982) || Chr (13) || 'I_CODE =' || P_I_Code || Chr (13) || 'BILL_NO=' || P_Bill_No;
             Goto Rtn_Rslt;             
        Elsif Nvl (V_Cnt, 0) > 1 Then
             If P_Si_Rcrd_No Is Null Then
                P_Err_No    := 20467;
                P_Msg_Txt   := ' P_Si_Rcrd_No Is Null ' || Chr (13) || 'I_CODE =' || P_I_Code || Chr (13) || 'BILL_NO=' || P_Bill_No;
                Goto Rtn_Rslt;
             End If;
        End If;
        ------------------------------------------------------------------------------          
         Declare
               v_I_Qty number;
               v_free_Qty number;           
           cursor bill_dtl is select * from table( Ars_Api_Instll_Doc_Pkg.GET_BILL_dtl( P_BILL_SER    =>J.BILL_SER,
                                                                      P_p_year      =>P_p_year, 
                                                                      P_Prev_Year   =>P_Prev_Year,
                                                                      P_Brn_Usr     =>P_Brn_Usr,
                                                                      P_shw_all_qty =>1   ,
                                                                      P_Usr_no      =>P_Usr_no,
                                                                      P_lng_no      =>P_lng_no  )) D 
                         Where i_code=p_i_code
                          And Nvl (Expire_Date, '01/01/1900') = Nvl (P_Expiredate, '01/01/1900') 
                          And Nvl (Batch_No, '0') = Nvl (P_Batchno, '0')
                          And Nvl (Rcrd_No, 0) = Nvl (P_Si_Rcrd_No, Nvl (Rcrd_No, 0))
                          AND NOT EXISTS(SELECT 1 FROM IAS_RT_BILL_DTL_BR
                                             WHERE RT_BILL_SER=P_RT_BILL_SER
                                                  AND I_CODE=D.I_CODE
                                                  AND NVL(SI_RCRD_NO,0)=D.RCRD_NO
                                                  AND ROWNUM<=1 );
                                                    
       
             
            Begin
                 For I in bill_dtl loop
                 
                           If Nvl (V_MUST_RET_SAME_WCODE, 0) = 1 and nvl(I.w_code,0)<>nvl(p_w_code,0) and nvl(P_SYS_NO,0)<>70 Then                              
                              P_Err_No    := 20463;
                              P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 6140) ||'w_code='||p_w_code || Chr (13) || 'BILL_NO=' || P_Bill_No;
                              Goto Rtn_Rslt;
                           End If;
                        v_I_Qty:=(nvl(i.I_Qty,0)*nvl(i.p_size,1) )/nvl(p_p_size,1);
                        v_free_Qty:=(nvl(i.free_Qty,0)*nvl(i.p_size,1) )/nvl(p_p_size,1);                   
                         If nvl(p_i_qty,0)>nvl(v_I_Qty,0)  Then
                              P_Err_No    := 20468;
                              P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 910) || v_I_Qty || Chr (13) 
                                      || Ias_Gen_Pkg.Get_Prompt  (P_Lng_No, 2745) || nvl(p_i_qty,0)|| Chr (13)                           
                                      || 'I_CODE =' || P_I_Code || Chr (13) 
                                      || 'RT_BILL_NO=' || P_RT_Bill_No 
                                      || 'BILL_NO=' || P_Bill_No;
                              Goto Rtn_Rslt;
                         End if;
                         
                         If nvl(p_free_Qty,0)>nvl(v_free_Qty,0)  Then
                              P_Err_No    := 20469;
                              P_Msg_Txt   := Ias_Gen_Pkg.Get_Prompt (P_Lng_No, 433)||Chr (13) 
                                      ||Ias_Gen_Pkg.Get_Msg (P_Lng_No, 910) || v_free_Qty || Chr (13) 
                                      || Ias_Gen_Pkg.Get_Prompt  (P_Lng_No, 2745) || nvl(p_free_Qty,0)|| Chr (13)                           
                                      || 'I_CODE =' || P_I_Code || Chr (13) 
                                      || 'RT_BILL_NO=' || P_RT_Bill_No 
                                      || 'BILL_NO=' || P_Bill_No;
                              Goto Rtn_Rslt;
                         End if;
                P_Doc_Sequence_Si:=I.DOC_SEQUENCE_SI;
                P_Si_Rcrd_No:=I.Rcrd_No;
                -------------------------------------------------------------------
                --## Check_Ret_Per
                If Nvl(V_Check_Ret_Per,0) =0 Then
                
                   If J.Bill_Date Is Not Null And V_Ar_Return_Period Is Not Null And P_Rt_Bill_Date Is Not Null Then
                      If To_date(P_Rt_Bill_Date,'DD/MM/YYYY') -To_date(J.Bill_Date,'DD/MM/YYYY') > V_Ar_Return_Period Then
                           P_Err_No    := 20679;
                           P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1251) ;
                           Goto Rtn_Rslt;                                        
                      End If ;
                   End If;
                   
                    If I.Return_Period Is Not Null And J.Bill_Date Is Not Null And P_Rt_Bill_Date Is Not Null Then
                        If To_date(P_Rt_Bill_Date,'DD/MM/YYYY') -To_date(J.Bill_Date,'DD/MM/YYYY') > I.Return_Period Then
                           P_Err_No    := 20680;
                           P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 1205)||Chr(13)|| 'I_CODE =' || P_I_Code || Chr (13)|| 'RT_BILL_NO=' || P_RT_Bill_No  ;
                           Goto Rtn_Rslt;                                        
                      End If ;
                    End If;
                   
                   
                
                End If;
                -------------------------------------------------------------------               
               End Loop;        
            End;   
     End Loop; 
     
     If Nvl (v_found, 0) = 0 Then
          P_Err_No    := 20470;
          P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No, 5980) || Chr (13) || 'BILL_NO=' || P_Bill_No;
          Goto Rtn_Rslt;
     End If;                                                                  
     ---------------------------------------------------------------------------
   End If;
    
    

  --##---------------------------------------------------------------------------------------------##--
  --####################--
  <<Rtn_Rslt>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_Chk_Pkg.CHK_RETRN_BILL_INSTLL');
      Return;
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;
   End If;
--####################--
Exception
   When Others Then
      P_Msg_Txt   := 'Error in CHK_RETRN_BILL_INSTLL ' || Sqlerrm;
      P_Err_No    := 20471;
      P_Pkg_Nm    := 'Ars_Api_Chk_Pkg.CHK_RETRN_BILL_INSTLL';
End CHK_RETRN_BILL_INSTLL;                         
--##-----------------------------------------------------------------------------------------------------##--
Procedure INSRT_DOC_BY_XML (   P_Doc_Typ          In       Ias_Post_Mst.Doc_Type%Type
                              ,P_Xml              In OUT   Clob
                              ,P_COMMIT_FLG       In       NUMBER  --## 0 ROLLBACK ,1 COMMIT ,2 ,MANUAL COMMIT
                              ,P_CLC_TAX_METHOD   In       NUMBER  --## 0 CALC TAX IN EXTRNAL ,1-AOUTO CALC TAX                                                        
                              ,P_Pst_Typ          In       Number --## 1 to br tables ,2 to onyx tables
                              ,P_Pst_FROM_BR      In       Number  --## 1- POSTING FORM BR TABLE  0- NOT FROM BR
                              ,P_DTS_ONLINE       In     NUMBER DEFAULT 0 --## 0 OFFLINE ,1-ONLINE
                              ,P_Lng_No           In       Number Default 1                          
                              ,P_Msg_Txt          Out   Varchar2
                              ,P_ERR_NO           Out   Varchar2
                              ,P_Pkg_Nm           Out   Varchar2)
   Is
      V_Doc_No        Sales_Order.Order_No%Type;
      V_Json_Rslt     Varchar2 (4000);
      V_Xml_Type      Xmltype;
      V_Doc_Srl       Sales_Order.Order_Ser%Type;
      V_Doc_Typ       Number;
      V_Doc_Seq       Order_Detail.Doc_Seq%Type;
      V_Rcrd_No       Number; 
      V_dis_per_qt_prm         Number;
      V_dis_amt_dtl_qt_prm     Number;
      V_dis_amt_dtl_qt_prm_vat Number;  
      V_Icode                  ias_itm_mst.i_code%Type;
      V_Itm_Unt                Ias_itm_Dtl.Itm_Unt%Type;
      V_Barcode                Ias_itm_Dtl.Barcode%Type;
   --PRAGMA AUTONOMOUS_TRANSACTION;
   Begin
      If P_Doc_Typ Is Null Then
         P_Err_No := 20020;
         P_Msg_Txt := ' App DOC_TYP IS NULL ';
         Goto Rtn_Rslt;
      End If;

      If P_Doc_Typ Not In (4, 5, 53,52,136) Then
         P_Err_No := 20021;
         P_Msg_Txt := ' DOC_TYPE=' || P_Doc_Typ || ' This Doc_Typ Is Not Idientified ';
         Goto Rtn_Rslt;
      End If;

      If P_Xml Is Null Then
         P_Err_No := 20022;
         P_Msg_Txt := 'App XML FILE  IS NULL  ';
         Goto Rtn_Rslt;
      End If;
      V_Xml_Type := Xmltype.Createxml (P_Xml);

      If P_Doc_Typ = 53 Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             -- SALES ORDER
         For M_Cv In (Select Extractvalue (Value (Xmlmstdmy), '*/SYS_NO              ') As Sys_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_NO               ') As Doc_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER               ') As Doc_Ser
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DATE               ') As Doc_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/CUR_CODE               ') As Cur_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/CUR_RATE               ') As Cur_Rate
                            ,Extractvalue (Value (Xmlmstdmy), '*/SO_TYPE               ') As So_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE               ') As C_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_NAME               ') As C_Name
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_TAX_CODE          ') As C_TAX_CODE
                            ,Extractvalue (Value (Xmlmstdmy), '*/A_DESC               ') As A_Desc
                            ,Extractvalue (Value (Xmlmstdmy), '*/CC_CODE               ') As Cc_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/PJ_NO               ') As Pj_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/ACTV_NO               ') As Actv_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/W_CODE               ') As W_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/REP_CODE               ') As Rep_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/EMP_NO               ') As Emp_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT               ') As Vat_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/ORDER_AMT               ') As Order_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT               ') As Disc_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_DTL               ') As Disc_Amt_Dtl
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST               ') As Disc_Amt_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT               ') As Othr_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_OTHR               ') As Vat_Amt_Othr
                            ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT_DISC               ') As OTHR_AMT_DISC  
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST_VAT               ') As Disc_Amt_Mst_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_DISC_MST               ') As Vat_Amt_Disc_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_AFTR_VAT               ') As Disc_Amt_Aftr_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/CASH_NO               ') As Cash_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TYP_NO_TAX               ') As Clc_Typ_No_Tax
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_VAT_PRICE_TYP               ') As Clc_Vat_Price_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/REF_DOC_NO               ') As Ref_Doc_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/REF_NO               ') As REF_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/REF_DOC_DATE               ') As Ref_Doc_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/PREPARE_DATE               ') As Prepare_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/REC_DEALER_DATE               ') As Rec_Dealer_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/DELIVERY_DATE               ') As Delivery_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/R_CODE               ') As R_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/DRIVER_NO               ') As Driver_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_DOC_TYPE               ') As Bill_Doc_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_DUE_DATE               ') As Bill_Due_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/ORDER_EXPIRE_DATE               ') As Order_Expire_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_DUE_DATE               ') As Cheque_Due_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE_CSH               ') As C_Code_Csh
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_ADDRESS               ') As C_Address
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_MOBILE               ') As C_Mobile
                            ,Extractvalue (Value (Xmlmstdmy), '*/LATITUDE               ') As Latitude
                            ,Extractvalue (Value (Xmlmstdmy), '*/LONGITUDE               ') As Longitude
                            ,Extractvalue (Value (Xmlmstdmy), '*/SI_TYPE                     ') As Si_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/EXTERNAL_POST               ') As External_Post
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD1                      ') As Field1
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD2               ') As Field2
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD3               ') As Field3
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD4               ') As Field4
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD5               ') As Field5
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD6               ') As Field6
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD7               ') As Field7
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD8               ') As Field8
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD9               ') As Field9
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD10               ') As Field10
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TAX_FREE_QTY_FLG  ') As CLC_TAX_FREE_QTY_FLG
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER_EXTRNL        ') As DOC_SER_EXTRNL
                            ,Extractvalue (Value (Xmlmstdmy), '*/QT_PRM_NO               ') As QT_PRM_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/QT_PRM_RCRD_NO           ') As QT_PRM_RCRD_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/QT_PRM_SER               ') As QT_PRM_SER
                            ,Extractvalue (Value (Xmlmstdmy), '*/TYP_NO         ') As TYP_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_AMT        ') As DOC_AMT
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DUE_DATE   ') As DOC_DUE_DATE
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_EXPIRE_DATE ')As DOC_EXPIRE_DATE
                            ,Extractvalue (Value (Xmlmstdmy), '*/TYP_NO_REF     ') As TYP_NO_REF 
                            ,Extractvalue (Value (Xmlmstdmy), '*/STAND_BY       ') As STAND_BY 
                            ,Extractvalue (Value (Xmlmstdmy), '*/TRNS_TYP        ') As TRNS_TYP                                                       
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_NO               ') As Brn_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_YEAR             ') As Brn_Year
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_USR              ') As Brn_Usr
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_TRMNL_NM           ') As Ad_Trmnl_Nm
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_U_ID               ') As Ad_U_Id
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_DATE               ') As Ad_Date
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/SAL_ORDR/SALES_ORDER'))) Xmlmstdmy)
         Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    --(11)
            --------------------------------------------------------------------------------          
            V_Doc_Typ := P_Doc_Typ;
            ---------------------------------------------------------------------------------
            Chk_Prmtr (   P_Sys_No            =>M_Cv.Sys_No
                          ,P_Doc_Typ          =>P_Doc_Typ                           
                          ,P_COMMIT_FLG       =>P_COMMIT_FLG
                          ,P_CLC_TAX_METHOD   =>P_CLC_TAX_METHOD                                                      
                          ,P_Pst_Typ          =>P_Pst_Typ
                          ,P_Pst_FROM_BR      =>P_Pst_FROM_BR
                          ,P_DTS_ONLINE       =>P_DTS_ONLINE
                          ,P_Lng_No           =>P_Lng_No                          
                          ,P_Msg_Txt          =>P_Msg_Txt
                          ,P_ERR_NO           =>P_ERR_NO
                          ,P_Pkg_Nm           =>P_Pkg_Nm);
                          If  P_Msg_Txt Is Not Null Then
                              Goto Rtn_Rslt;
                          End If;
          ---------------------------------------------------------------------------------                          
            Begin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(1)
               Ars_Api_Trns_Pkg.Insrt_Sales_Order (P_Sys_No              => M_Cv.Sys_No
                                 ,P_Doc_No              => M_Cv.Doc_No
                                 ,P_Doc_Type            => P_Doc_Typ
                                 ,P_Doc_Ser             => M_Cv.Doc_SER
                                 ,P_Doc_Date            => TO_DATE(M_Cv.Doc_Date,'DD/MM/RRRR')
                                 ,P_Cur_Code            => M_Cv.Cur_Code
                                 ,P_Cur_Rate            => M_Cv.Cur_Rate
                                 ,P_So_Type             => NVL(M_Cv.TYP_NO,M_Cv.So_Type)
                                 ,P_C_Code              => M_Cv.C_Code
                                 ,P_C_Name              => M_Cv.C_Name
                                 ,P_C_TAX_CODE          => M_Cv.C_TAX_CODE
                                 ,P_A_Desc              => M_Cv.A_Desc
                                 ,P_Cc_Code             => M_Cv.Cc_Code
                                 ,P_Pj_No               => M_Cv.Pj_No
                                 ,P_Actv_No             => M_Cv.Actv_No
                                 ,P_W_Code              => M_Cv.W_Code
                                 ,P_Rep_Code            => M_Cv.Rep_Code
                                 ,P_Emp_No              => M_Cv.Emp_No
                                 ,P_Vat_Amt             => M_Cv.Vat_Amt
                                 ,P_Order_Amt           => NVL(M_Cv.DOC_Amt,M_Cv.Order_Amt)
                                 ,P_Disc_Amt            => M_Cv.Disc_Amt
                                 ,P_Disc_Amt_Dtl        => M_Cv.Disc_Amt_Dtl
                                 ,P_Disc_Amt_Mst        => M_Cv.Disc_Amt_Mst
                                 ,P_Othr_Amt            => M_Cv.Othr_Amt
                                 ,P_Vat_Amt_Othr        => M_Cv.Vat_Amt_Othr
                                 ,P_OTHR_AMT_DISC       =>M_CV.OTHR_AMT_DISC
                                 ,P_Disc_Amt_Mst_Vat    => M_Cv.Disc_Amt_Mst_Vat
                                 ,P_Vat_Amt_Disc_Mst    => M_Cv.Vat_Amt_Disc_Mst
                                 ,P_Disc_Amt_Aftr_Vat   => M_Cv.Disc_Amt_Aftr_Vat
                                 ,P_Cash_No             => M_Cv.Cash_No
                                 ,P_Clc_Typ_No_Tax      => M_Cv.Clc_Typ_No_Tax
                                 ,P_Clc_Vat_Price_Typ   => M_Cv.Clc_Vat_Price_Typ
                                 ,P_Ref_Doc_No          => nvl(M_Cv.Ref_Doc_No,M_Cv.Ref_No)
                                 ,P_Ref_Doc_Date        => TO_DATE(M_Cv.Ref_Doc_Date,'DD/MM/RRRR')
                                 ,P_Prepare_Date        => TO_DATE(M_Cv.Prepare_Date,'DD/MM/RRRR')
                                 ,P_Rec_Dealer_Date     => TO_DATE(M_Cv.Rec_Dealer_Date,'DD/MM/RRRR')
                                 ,P_Delivery_Date       => TO_DATE(M_Cv.Delivery_Date,'DD/MM/RRRR')
                                 ,P_R_Code              => M_Cv.R_Code
                                 ,P_Driver_No           => M_Cv.Driver_No
                                 ,P_Bill_Doc_Type       => M_Cv.Bill_Doc_Type
                                 ,P_Bill_Due_Date       => NVL(TO_DATE(M_Cv.DOC_Due_Date,'DD/MM/RRRR'),TO_DATE(M_Cv.Bill_Due_Date,'DD/MM/RRRR'))
                                 ,P_Order_Expire_Date   => NVL(TO_DATE(M_Cv.DOC_Expire_Date,'DD/MM/RRRR'),TO_DATE(M_Cv.Order_Expire_Date,'DD/MM/RRRR'))
                                 ,P_Cheque_Due_Date     => TO_DATE(M_Cv.Cheque_Due_Date,'DD/MM/RRRR')
                                 ,P_C_Code_Csh          => M_Cv.C_Code_Csh
                                 ,P_C_Address           => M_Cv.C_Address
                                 ,P_C_Mobile            => M_Cv.C_Mobile
                                 ,P_Latitude            => M_Cv.Latitude
                                 ,P_Longitude           => M_Cv.Longitude
                                 ,P_Si_Type             => NVL(M_Cv.TYP_NO_REF,M_Cv.Si_Type)
                                 ,P_External_Post       => M_Cv.External_Post
                                 ,P_Field1              => M_Cv.Field1
                                 ,P_Field2              => M_Cv.Field2
                                 ,P_Field3              => M_Cv.Field3
                                 ,P_Field4              => M_Cv.Field4
                                 ,P_Field5              => M_Cv.Field5
                                 ,P_Field6              => M_Cv.Field6
                                 ,P_Field7              => M_Cv.Field7
                                 ,P_Field8              => M_Cv.Field8
                                 ,P_Field9              => M_Cv.Field9
                                 ,P_Field10             => M_Cv.Field10
                                 ,P_CLC_TAX_FREE_QTY_FLG =>M_Cv.CLC_TAX_FREE_QTY_FLG
                                 ,P_Doc_Ser_Extrnl      =>M_Cv.DOC_SER_EXTRNL
                                 ,P_Qt_Prm_No          => M_Cv.Qt_Prm_No                               
                                 ,P_QT_PRM_RCRD_NO      => M_Cv.QT_PRM_RCRD_NO
                                 ,P_QT_PRM_SER          => M_Cv.QT_PRM_SER
                                 ,P_STAND_BY            => M_Cv.STAND_BY
                                 ,P_Brn_No              => M_Cv.Brn_No
                                 ,P_Brn_Year            => M_Cv.Brn_Year
                                 ,P_BRN_USR             => M_Cv.BRN_USR
                                 ,P_Ad_Trmnl_Nm         => M_Cv.Ad_Trmnl_Nm
                                 ,P_Ad_U_Id             => M_Cv.Ad_U_Id
                                 ,P_Ad_Date             => TO_DATE(TO_CHAR(M_CV.AD_DATE),'DD/MM/RRRR HH24:MI:SS')
                                 ,P_TRNS_TYP            => M_Cv.TRNS_TYP
                                 ,P_CLC_TAX_METHOD      => P_CLC_TAX_METHOD
                                 ,P_DTS_ONLINE          => P_DTS_ONLINE
                                 ,P_Lng_No              => P_Lng_No 
                                 ,P_Msg_Txt             => P_Msg_Txt
                                 ,P_ERR_NO              => P_Err_No
                                 ,P_Pkg_NM              => P_Pkg_Nm);                                   
                If P_Msg_Txt Is Not Null Then                
                  Goto Rtn_Rslt;
                End If ;
            Exception
               When Others Then               
                  Raise_Application_Error (-20302, 'Err when insert SALES_ORDER DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);            
            End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  --(1)
            -------------------------------------------------------------------------------------------
            For D_Cv In (Select Extractvalue (Value (Xmldtldmy), '*/I_CODE               ') As I_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/ITM_UNT               ') As Itm_Unt
                               ,Extractvalue (Value (Xmldtldmy), '*/I_QTY               ') As I_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/P_QTY               ') As P_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/P_SIZE               ') As P_Size
                               ,Extractvalue (Value (Xmldtldmy), '*/FREE_QTY               ') As Free_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/BARCODE               ') As Barcode
                               ,Extractvalue (Value (Xmldtldmy), '*/BATCH_NO               ') As Batch_No
                               ,Extractvalue (Value (Xmldtldmy), '*/EXPIRE_DATE               ') As Expire_Date
                               ,Extractvalue (Value (Xmldtldmy), '*/W_CODE               ') As W_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/CC_CODE               ') As Cc_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/ACTV_NO               ') As Actv_No
                               ,Extractvalue (Value (Xmldtldmy), '*/PJ_NO               ') As Pj_No
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE               ') As I_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE_VAT               ') As I_Price_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/MEASUR_PRICE               ') As Measur_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT               ') As Othr_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT_DISC               ') As Othr_Amt_Disc
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT               ') As Vat_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_AFTR_DIS               ') As Vat_Amt_Aftr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_BFR_DIS               ') As Vat_Amt_Bfr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL2_VAT               ') As Vat_Amt_Dis_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL3_VAT               ') As Vat_Amt_Dis_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL_VAT               ') As Vat_Amt_Dis_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_MST_VAT               ') As Vat_Amt_Dis_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_OTHR               ') As Vat_Amt_Othr
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_PER               ') As Vat_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT               ') As Dis_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_AFTR_VAT               ') As Dis_Amt_Aftr_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL               ') As Dis_Amt_Dtl
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2               ') As Dis_Amt_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2_VAT               ') As Dis_Amt_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3               ') As Dis_Amt_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3_VAT               ') As Dis_Amt_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_VAT               ') As Dis_Amt_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST               ') As Dis_Amt_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST_VAT               ') As Dis_Amt_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER               ') As Dis_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER2               ') As Dis_Per2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER3               ') As Dis_Per3                               
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO               ') As RCRD_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE          ') As DOC_SEQUENCE                                                              
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_TYPE_REF          ') As Doc_Type_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SER_REF           ') As Doc_Ser_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_NO_REF            ') As Doc_No_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE_REF     ') As Doc_Sequence_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO_REF          ') As RCRD_NO_REF
                               ,Extractvalue (Value (Xmldtldmy), '*/EMP_NO               ') As Emp_No
                               ,Extractvalue (Value (Xmldtldmy), '*/EXTERNAL_POST               ') As External_Post
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL1               ') As Field_Dtl1
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL2               ') As Field_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL3               ') As Field_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/F_TIME               ') As F_Time
                               ,Extractvalue (Value (Xmldtldmy), '*/T_TIME               ') As T_Time
                               ,Extractvalue (Value (Xmldtldmy), '*/ITEM_DESC               ') As Item_Desc
                               ,Extractvalue (Value (Xmldtldmy), '*/I_WIDTH               ') As I_Width
                               ,Extractvalue (Value (Xmldtldmy), '*/I_HEIGHT               ') As I_Height
                               ,Extractvalue (Value (Xmldtldmy), '*/I_LENGTH               ') As I_Length
                               ,Extractvalue (Value (Xmldtldmy), '*/I_NUMBER               ') As I_Number
                               ,Extractvalue (Value (Xmldtldmy), '*/ARGMNT_NO               ') As Argmnt_No 
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_QTY                  ') As WT_QTY 
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_UNT                 ') As  WT_UNT                              
                               ,Extractvalue (Value (Xmldtldmy), '*/REC_ATTCH               ') As Rec_Attch
                               ,Extractvalue (Value (Xmldtldmy), '*/RESERVED               ') As Reserved
                               ,Extractvalue (Value (Xmldtldmy), '*/RES_DATE               ') As Res_Date
                               ,Extractvalue (Value (Xmldtldmy), '*/RES_QTY               ') As Res_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/LEV_NO               ') As Lev_No
                               ,Extractvalue (Value (Xmldtldmy), '*/PRM_GRP_NO               ') As PRM_GRP_No
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_NO               ') As QT_PRM_NO
                                ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_RCRD_NO           ') As QT_PRM_RCRD_NO
                                ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_SER               ') As QT_PRM_SER
                                ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_QT_PRM       ') As Dis_Amt_Dtl_Qt_Prm
                                ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_QT_PRM_VAT   ') As Dis_Amt_Dtl_Qt_Prm_Vat
                                ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER_QT_PRM          ') As Dis_Per_Qt_Prm
                           From Table (Xmlsequence (Extract (V_Xml_Type, '/SAL_ORDR/ORDER_DETAIL'))) Xmldtldmy)
            Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(12)
               ---------------------
               V_DOC_SEQ:=NULL;
               V_Rcrd_No:=Null;
               V_Icode  :=Null;
               V_Itm_Unt:=Null;
               V_Barcode:=Null;
               
                Ias_Itm_Pkg.Get_I_Code (P_Barcode => D_Cv.I_Code, P_I_Code => V_Icode, P_Itm_Unt => V_Itm_Unt);
                If V_Icode Is  Null  Or nvl(V_Icode,'0')=Nvl(D_Cv.I_Code,'0') Then                                  
                  V_Icode  := D_Cv.I_Code;
                  V_Itm_Unt:=D_Cv.Itm_Unt;
                  V_Barcode:=D_Cv.Barcode;
                Else
                    V_Barcode:=D_Cv.I_Code;  
                End If;   
               
               If D_cv.Qt_prm_ser Is Not Null And Ias_qt_prm_pkg.Ias_get_qt_prm_type ( P_qt_ser=>D_cv.Qt_prm_ser) =3 Then
                   V_dis_per_qt_prm         := D_cv.Dis_per_qt_prm;
                   V_dis_amt_dtl_qt_prm     := D_cv.Dis_amt_dtl_qt_prm;
                   V_dis_amt_dtl_qt_prm_vat := D_cv.Dis_amt_dtl_qt_prm_vat;
               End If;
               
               Begin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              --(2)
                  Ars_Api_Trns_Pkg.Insrt_Order_Detail (P_I_Code                 => V_Icode
                                     ,P_Itm_Unt                => V_Itm_Unt
                                     ,P_I_Qty                  => D_Cv.I_Qty
                                     ,P_P_Qty                  => D_Cv.P_Qty
                                     ,P_P_Size                 => D_Cv.P_Size
                                     ,P_Free_Qty               => D_Cv.Free_Qty
                                     ,P_Barcode                => V_Barcode
                                     ,P_Batch_No               => D_Cv.Batch_No
                                     ,P_Expire_Date            => TO_DATE(D_Cv.Expire_Date,'DD/MM/RRRR') 
                                     ,P_W_Code                 => D_Cv.W_Code
                                     ,P_Cc_Code                => D_Cv.Cc_Code
                                     ,P_Actv_No                => D_Cv.Actv_No
                                     ,P_Pj_No                  => D_Cv.Pj_No
                                     ,P_I_Price                => D_Cv.I_Price
                                     ,P_I_Price_Vat            => D_Cv.I_Price_Vat
                                     ,P_Measur_Price           => D_Cv.Measur_Price
                                     ,P_Othr_Amt               => D_Cv.Othr_Amt
                                     ,P_Othr_Amt_Disc          => D_Cv.Othr_Amt_Disc
                                     ,P_Vat_Amt                => D_Cv.Vat_Amt
                                     ,P_Vat_Amt_Aftr_Dis       => D_Cv.Vat_Amt_Aftr_Dis
                                     ,P_Vat_Amt_Bfr_Dis        => D_Cv.Vat_Amt_Bfr_Dis
                                     ,P_Vat_Amt_Dis_Dtl2_Vat   => D_Cv.Vat_Amt_Dis_Dtl2_Vat
                                     ,P_Vat_Amt_Dis_Dtl3_Vat   => D_Cv.Vat_Amt_Dis_Dtl3_Vat
                                     ,P_Vat_Amt_Dis_Dtl_Vat    => D_Cv.Vat_Amt_Dis_Dtl_Vat
                                     ,P_Vat_Amt_Dis_Mst_Vat    => D_Cv.Vat_Amt_Dis_Mst_Vat
                                     ,P_Vat_Amt_Othr           => D_Cv.Vat_Amt_Othr
                                     ,P_Vat_Per                => D_Cv.Vat_Per
                                     ,P_Dis_Amt                => D_Cv.Dis_Amt
                                     ,P_Dis_Amt_Aftr_Vat       => D_Cv.Dis_Amt_Aftr_Vat
                                     ,P_Dis_Amt_Dtl            => D_Cv.Dis_Amt_Dtl
                                     ,P_Dis_Amt_Dtl2           => D_Cv.Dis_Amt_Dtl2
                                     ,P_Dis_Amt_Dtl2_Vat       => D_Cv.Dis_Amt_Dtl2_Vat
                                     ,P_Dis_Amt_Dtl3           => D_Cv.Dis_Amt_Dtl3
                                     ,P_Dis_Amt_Dtl3_Vat       => D_Cv.Dis_Amt_Dtl3_Vat
                                     ,P_Dis_Amt_Dtl_Vat        => D_Cv.Dis_Amt_Dtl_Vat
                                     ,P_Dis_Amt_Mst            => D_Cv.Dis_Amt_Mst
                                     ,P_Dis_Amt_Mst_Vat        => D_Cv.Dis_Amt_Mst_Vat
                                     ,P_Dis_Per                => D_Cv.Dis_Per
                                     ,P_Dis_Per2               => D_Cv.Dis_Per2
                                     ,P_Dis_Per3               => D_Cv.Dis_Per3                                     
                                     ,P_Doc_Seq                => V_DOC_SEQ
                                     ,P_Rcrd_No                => V_Rcrd_No
                                     ,P_Doc_Sequence_Ref       => case when nvl(D_Cv.Doc_Sequence_Ref,0)=0 then null else D_Cv.Doc_Sequence_Ref end                                        
                                     ,P_Doc_Type_Ref           => case when nvl(D_Cv.Doc_Type_Ref,0)=0 then null else D_Cv.Doc_Type_Ref end
                                     ,P_Doc_Ser_Ref            => case when nvl(D_Cv.Doc_Ser_Ref,0)=0 then null else D_Cv.Doc_Ser_Ref end
                                     ,P_Doc_No_Ref             => case when nvl(D_Cv.Doc_No_Ref,0)=0 then null else D_Cv.Doc_No_Ref end  
                                     ,P_Rcrd_No_Ref            => case when nvl(D_Cv.Rcrd_No_Ref,0)=0 then null else D_Cv.Rcrd_No_Ref end  
                                     ,P_Emp_No                 => D_Cv.Emp_No
                                     ,P_Field_Dtl1             => D_Cv.Field_Dtl1
                                     ,P_Field_Dtl2             => D_Cv.Field_Dtl2
                                     ,P_Field_Dtl3             => D_Cv.Field_Dtl3
                                     ,P_F_Time                 => D_Cv.F_Time
                                     ,P_T_Time                 => D_Cv.T_Time
                                     ,P_Item_Desc              => D_Cv.Item_Desc
                                     ,P_I_Width                => D_Cv.I_Width
                                     ,P_I_Height               => D_Cv.I_Height
                                     ,P_I_Length               => D_Cv.I_Length
                                     ,P_I_Number               => D_Cv.I_Number
                                     ,P_Argmnt_No              => D_Cv.Argmnt_No
                                     ,P_WT_QTY                 => D_Cv.WT_QTY
                                     ,P_WT_UNT                 => D_Cv.WT_UNT                                     
                                     ,P_Rec_Attch              => D_Cv.Rec_Attch
                                     ,P_Reserved               => D_Cv.Reserved
                                     ,P_Res_Date               => D_Cv.Res_Date
                                     ,P_Res_Qty                => D_Cv.Res_Qty
                                     ,P_Lev_No                 =>D_cv.Lev_No
                                     ,P_PRM_GRP_NO             => Case When nvl(D_Cv.PRM_GRP_NO,0)=0 Then Null Else  D_Cv.PRM_GRP_NO end 
                                     ,P_QT_PRM_NO              => Case When nvl(D_cv.QT_PRM_NO,0)=0 Then Null Else D_cv.QT_PRM_NO end 
                                     ,P_QT_PRM_RCRD_NO         =>Case When nvl(D_Cv.QT_PRM_RCRD_NO,0)=0 Then Null Else D_Cv.QT_PRM_RCRD_NO end 
                                     ,P_QT_PRM_SER             =>Case When nvl(D_Cv.QT_PRM_SER,0)=0 Then Null Else D_Cv.QT_PRM_SER end
                                      ,P_Dis_Amt_Dtl_Qt_Prm       => V_Dis_Amt_Dtl_Qt_Prm
                                      ,P_Dis_Amt_Dtl_Qt_Prm_Vat   => V_Dis_Amt_Dtl_Qt_Prm_Vat
                                      ,P_Dis_Per_Qt_Prm            => V_Dis_Per_Qt_Prm
                                     ,P_Msg_Txt                => P_Msg_Txt
                                     ,P_ERR_NO               => P_Err_No
                                     ,P_Pkg_NM                 => P_Pkg_Nm);
                    If P_Msg_Txt Is Not Null Then                  
                      Goto Rtn_Rslt;
                    End If ;              
               Exception
                  When Others Then                   
                     Raise_Application_Error (-20303, 'Err. When Insert ORDER_DETAIL DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);
               End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --(2)
            --##------------------------------------------------------------------------------------------------------------------------------##--
             for Tax_Mvmnt_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As Bill_Doc_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As Doc_Jv_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As Tax_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As Clc_Typ_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As Agncy_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                      ') As I_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                     ') As Itm_Unt
                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                      ') As P_Size
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_PRICE                     ') As I_Price
                                      ,Extractvalue( Value( Xmldtldmy), '*/DISC_AMT                    ') As Disc_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                    ') As A_Cy
                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As Ac_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As Tax_Prcnt
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As Tax_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                      ') As W_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As Cc_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As Pj_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As Actv_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As Rcrd_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As Doc_Sequence
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As Tax_Amt_L
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_QTY                       ') As I_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/FREE_QTY                    ') As Free_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As Ref_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_COST                    ') As Stk_Cost
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_RATE                    ') As Stk_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TAX_FREE_QTY_FLG        ') As Clc_Tax_Free_Qty_Flg
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/SAL_ORDR/GNR_TAX_ITM_MOVMNT'))) Xmldtldmy                                                                      
                                   )                              
               Loop
                   IF NVL(Tax_Mvmnt_Cv.I_CODE,'0')=NVL(D_CV.I_CODE,'0')  AND NVL(Tax_Mvmnt_Cv.ITM_UNT,'0')=NVL(D_CV.ITM_UNT,'0')
                     AND NVL(Tax_Mvmnt_Cv.RCRD_NO,0)=NVL(D_CV.RCRD_NO,0) THEN    
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Gnr_Tax_Itm_Movmnt(P_Doc_Typ                => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Bill_Doc_Type          => Ars_Api_Trns_Pkg.G_Bill_Doc_Type
                                                     ,P_Doc_Jv_Type            => Ars_Api_Trns_Pkg.G_SO_TYPE--.Tax_Mvmnt_Cv.Doc_Jv_Type
                                                     ,P_Tax_No                 => Tax_Mvmnt_Cv.Tax_No
                                                     ,P_Clc_Typ_No             => Tax_Mvmnt_Cv.Clc_Typ_No
                                                     ,P_Agncy_No               => Tax_Mvmnt_Cv.Agncy_No
                                                     ,P_I_Code                 => V_Icode
                                                     ,P_Itm_Unt                => V_Itm_Unt
                                                     ,P_P_Size                 => Tax_Mvmnt_Cv.P_Size
                                                     ,P_I_Price                => Tax_Mvmnt_Cv.I_Price
                                                     ,P_Disc_Amt               => Tax_Mvmnt_Cv.Disc_Amt
                                                     ,P_A_Code                 => Tax_Mvmnt_Cv.A_Code
                                                     ,P_Cur_Code               => Tax_Mvmnt_Cv.A_Cy
                                                     ,P_Ac_Rate                => Tax_Mvmnt_Cv.Ac_Rate
                                                     ,P_Tax_Prcnt              => Tax_Mvmnt_Cv.Tax_Prcnt
                                                     ,P_Tax_Amt                => Tax_Mvmnt_Cv.Tax_Amt
                                                     ,P_W_Code                 => Ars_Api_Trns_Pkg.G_W_Code
                                                     ,P_Cc_Code                => Ars_Api_Trns_Pkg.G_Dtl_Cc_Code
                                                     ,P_Pj_No                  => Ars_Api_Trns_Pkg.G_Dtl_Pj_No
                                                     ,P_Actv_No                => Ars_Api_Trns_Pkg.G_Dtl_Actv_No
                                                     ,P_Rcrd_No                => V_Rcrd_No
                                                     ,P_Doc_Sequence           => V_Doc_Seq
                                                     ,P_Tax_Amt_L              => Tax_Mvmnt_Cv.Tax_Amt_L
                                                     ,P_I_Qty                  => Tax_Mvmnt_Cv.I_Qty
                                                     ,P_Free_Qty               => Tax_Mvmnt_Cv.Free_Qty
                                                     ,P_Ref_No                 => Tax_Mvmnt_Cv.Ref_No
                                                     ,P_Stk_Cost               => Tax_Mvmnt_Cv.Stk_Cost
                                                     ,P_Stk_Rate               => Tax_Mvmnt_Cv.Stk_Rate
                                                     ,P_Clc_Tax_Free_Qty_Flg   => M_CV.Clc_Tax_Free_Qty_Flg
                                                     ,P_Msg_Txt                => P_Msg_Txt
                                                     ,P_ERR_NO               => P_Err_No
                                                     ,P_Pkg_Nm                 => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then
                       -- ---Rollback;
                        Raise_Application_Error( -20304, 'ERR WHEN INSERT INSRT_GNR_TAX_ITM_MOVMNT DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                    End;
                 END IF; 
               End Loop;            
            --##---------------------------------------------------------------------------------------------------------------------------##--             
            End Loop;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            --(12)          
            --##---------------------------------------------------------------------------------------------------------------------------##--
            --##INSERT OTHER CHARGE
               For Othr_Chrg_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                        ') As Sc_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                       ') As A_Code
                                          ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                     ') As A_Cy
                                          ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                      ') As Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/PER                          ') As Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/AMT                          ') As Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/INV_ITEM                     ') As Inv_Item
                                          ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                      ') As Rcrd_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                      ') As Bill_Py
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_AMT                      ') As Vat_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_PER                      ') As Vat_Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AMT                       ') As Sc_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AC_RATE                   ') As Sc_Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_A_CY                      ') As Sc_A_Cy
                                      From Table( Xmlsequence( Extract( V_Xml_Type, '/SAL_ORDR/OTHER_CHARGES'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Other_Charges(P_Doc_Typ      => Ars_Api_Trns_Pkg.G_Doc_Typ
                                        ,P_Bill_Doc_Type       => Ars_Api_Trns_Pkg.G_Bill_Doc_Type
                                        ,P_BILL_TYPE    =>53
                                        ,P_Sc_No        => Othr_Chrg_Cv.Sc_No
                                        ,P_A_Code       => Othr_Chrg_Cv.A_Code
                                        ,P_Cur_Code     => Othr_Chrg_Cv.A_Cy
                                        ,P_Ac_Rate      => Othr_Chrg_Cv.Ac_Rate
                                        ,P_Per          => Othr_Chrg_Cv.Per
                                        ,P_Amt          => Othr_Chrg_Cv.Amt
                                        ,P_Inv_Item     => Othr_Chrg_Cv.Inv_Item
                                        ,P_Rcrd_No      => Othr_Chrg_Cv.Rcrd_No
                                        ,P_Bill_Py      => Othr_Chrg_Cv.Bill_Py
                                        ,P_Vat_Amt      => Othr_Chrg_Cv.Vat_Amt
                                        ,P_Vat_Per      => Othr_Chrg_Cv.Vat_Per
                                        ,P_Sc_Amt       => Othr_Chrg_Cv.Sc_Amt
                                        ,P_Sc_Ac_Rate   => Othr_Chrg_Cv.Sc_Ac_Rate
                                        ,P_Sc_A_Cy      => Othr_Chrg_Cv.Sc_A_Cy
                                        ,P_Msg_Txt      => P_Msg_Txt
                                        ,P_ERR_NO     => P_Err_No
                                        ,P_Pkg_Nm       => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                      ---  ---Rollback;
                        Raise_Application_Error( -20305, 'ERR WHEN INSERT OTHER_CHARGES DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
         --##INSERT OTHER CHARGE ITEMS
               For Othr_Chrg_Itm_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                    ') As Doc_Typ
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                      ') As Sc_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                     ') As A_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                   ') As A_Cy
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                    ') As Ac_Rate
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PER                        ') As Per
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AMT                        ') As Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                     ') As W_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                    ') As Cc_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                      ') As Pj_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                    ') As Actv_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                    ') As Rcrd_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SI_TYPE                    ') As Si_Type
                                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                     ') As I_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                    ') As Itm_Unt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                     ') As P_Size
                                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                    ') As Bill_Py
                                                      ,Extractvalue( Value( Xmldtldmy), '*/UNIT_AMT                   ') As Unit_Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/POST_CODE                  ') As Post_Code
                                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/SAL_ORDR/OTHER_CHARGES_ITEMS'))) Xmldtldmy)
                       Loop
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Other_Charges_Items(P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                      ,P_Sc_No       => Othr_Chrg_Itm_Cv.Sc_No
                                                      ,P_A_Code      => Othr_Chrg_Itm_Cv.A_Code
                                                      ,P_Cur_Code    => Othr_Chrg_Itm_Cv.A_Cy
                                                      ,P_Ac_Rate     => Othr_Chrg_Itm_Cv.Ac_Rate
                                                      ,P_Per         => Othr_Chrg_Itm_Cv.Per
                                                      ,P_Amt         => Othr_Chrg_Itm_Cv.Amt
                                                      ,P_W_Code      => Othr_Chrg_Itm_Cv.W_Code
                                                      ,P_Cc_Code     => Othr_Chrg_Itm_Cv.Cc_Code
                                                      ,P_Pj_No       => Othr_Chrg_Itm_Cv.Pj_No
                                                      ,P_Actv_No     => Othr_Chrg_Itm_Cv.Actv_No
                                                      ,P_Rcrd_No     => Othr_Chrg_Itm_Cv.Rcrd_No
                                                      ,P_Si_Type     => Othr_Chrg_Itm_Cv.Si_Type
                                                      ,P_I_Code      => Othr_Chrg_Itm_Cv.I_Code
                                                      ,P_Itm_Unt     => Othr_Chrg_Itm_Cv.Itm_Unt
                                                      ,P_P_Size      => Othr_Chrg_Itm_Cv.P_Size
                                                      ,P_Bill_Py     => Othr_Chrg_Itm_Cv.Bill_Py
                                                      ,P_Unit_Amt    => Othr_Chrg_Itm_Cv.Unit_Amt
                                                      ,P_Post_Code   => Othr_Chrg_Itm_Cv.Post_Code
                                                      ,P_Msg_Txt     => P_Msg_Txt
                                                      ,P_ERR_NO    => P_Err_No
                                                      ,P_Pkg_Nm      => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                          Exception
                             When Others Then
                               -- ---Rollback;
                                Raise_Application_Error( -20306, 'ERR WHEN INSERT OTHER_CHARGES_ITEMS DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                          End;
                       End Loop; 
         --##---------------------------------------------------------------------------------------------------------------------------##--
         For Tax_INPT_Mvmnt_Cv In (SELECT    Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As DOC_TYP              
                                            ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As BILL_DOC_TYPE         
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As DOC_JV_TYPE                                                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As TAX_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As CLC_TYP_NO           
                                            ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As AGNCY_NO                                        
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_CODE                   ') As INPT_CODE            
                                            ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_CODE               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                    ') As CUR_CODE                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As AC_RATE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_AMT                    ') As INPT_AMT             
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As TAX_PRCNT            
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As TAX_AMT              
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As TAX_AMT_L            
                                            ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As CC_CODE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As PJ_NO                
                                            ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As ACTV_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As REF_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As RCRD_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As DOC_SEQUENCE
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/SAL_ORDR/GNR_TAX_INPT_MOVMNT'))) Xmldtldmy                                  
                                   )                              
               Loop                    
                    Begin
                          Ars_Api_Trns_Pkg.INSRT_GNR_TAX_INPT_MOVMNT(
                                            P_DOC_TYP                    =>53
                                           ,P_BILL_DOC_TYPE              =>Ars_Api_Trns_Pkg.G_BILL_DOC_TYPE
                                           ,P_DOC_JV_TYPE                =>Ars_Api_Trns_Pkg.G_SO_TYPE                                       
                                           ,P_TAX_NO                     =>Tax_INPT_Mvmnt_Cv.TAX_NO
                                          , P_CLC_TYP_NO                 =>Tax_INPT_Mvmnt_Cv.CLC_TYP_NO 
                                          , P_AGNCY_NO                   =>Tax_INPT_Mvmnt_Cv.AGNCY_NO                            
                                          , P_INPT_CODE                  =>Tax_INPT_Mvmnt_Cv.INPT_CODE 
                                           ,P_A_CODE                     =>Tax_INPT_Mvmnt_Cv.A_CODE 
                                          , P_A_CY                       =>Tax_INPT_Mvmnt_Cv.CUR_CODE
                                          , P_AC_RATE                    =>Tax_INPT_Mvmnt_Cv.AC_RATE 
                                          , P_INPT_AMT                   =>Tax_INPT_Mvmnt_Cv.INPT_AMT 
                                          , P_TAX_PRCNT                  =>Tax_INPT_Mvmnt_Cv.TAX_PRCNT 
                                          , P_TAX_AMT                    =>Tax_INPT_Mvmnt_Cv.TAX_AMT
                                          , P_TAX_AMT_L                  =>Tax_INPT_Mvmnt_Cv.TAX_AMT_L 
                                           ,P_CC_CODE                    =>Tax_INPT_Mvmnt_Cv.CC_CODE 
                                          , P_PJ_NO                      =>Tax_INPT_Mvmnt_Cv.PJ_NO 
                                          , P_ACTV_NO                    =>Tax_INPT_Mvmnt_Cv.ACTV_NO 
                                          , P_REF_NO                     =>Tax_INPT_Mvmnt_Cv.REF_NO 
                                          , P_RCRD_NO                    =>Tax_INPT_Mvmnt_Cv.RCRD_NO 
                                          , P_DOC_SEQUENCE               =>Tax_INPT_Mvmnt_Cv.DOC_SEQUENCE
                                          ,P_Msg_Txt                     =>P_Msg_Txt
                                          ,P_ERR_NO                     =>P_ERR_NO
                                          ,P_Pkg_NM                     =>P_Pkg_NM); 

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then
                       -- ---Rollback;
                        Raise_Application_Error( -20547, 'ERR WHEN INSERT INSRT_GNR_TAX_INPT_MOVMNT DOC_NO= ' || V_DOC_NO || ' ' || Chr( 10) || Sqlerrm);
                    End;                 
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
            For Attach_Cv
                  In (Select Extractvalue (Value (Xmldtldmy), '*/FILE_NAME         ') As File_Name
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/SAL_ORDR/ATTACH'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Archives (P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Doc_Ser     => Ars_Api_Trns_Pkg.G_Doc_Ser
                                                     ,P_File_Name   => Attach_Cv.File_Name
                                                     ,P_Msg_Txt     => P_Msg_Txt
                                                     ,P_Err_No      => P_Err_No
                                                     ,P_Pkg_Nm      => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                        Raise_Application_Error (-20719,'Err.in Ars_Api_Trns_Pkg.INSRT_ARCHIVES= '|| V_Doc_No|| ' '|| Chr (10)|| Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--               
            --## CHK INSERT DATA
            Ars_Api_Trns_Pkg.Chk_Insrt_Data (P_Doc_Typ    => Ars_Api_Trns_Pkg.G_Doc_Typ
                           ,P_Doc_Ser    => Ars_Api_Trns_Pkg.G_Doc_Ser
                           ,P_Msg_Txt    => P_Msg_Txt
                           ,P_ERR_NO   => P_Err_No
                            ,P_Pkg_NM   => P_Pkg_Nm);
              If P_Msg_Txt Is Not Null Then                 
                  Goto Rtn_Rslt;
              End If ;                                    
         ----------------------------------------------------------------------------------------------------------
         End Loop;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --(11)
      Elsif P_Doc_Typ = 4 Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            -- BILL SALES
         For M_Cv In (Select Extractvalue (Value (Xmlmstdmy), '*/SYS_NO                                   ') As Sys_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_TYPE                                 ') As Doc_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_DOC_TYPE                            ') As Bill_Doc_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_NO                                   ') As Doc_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER                                  ') As Doc_Ser
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DATE                                 ') As Doc_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/CUR_CODE                                 ') As Cur_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/CUR_RATE                                 ') As Cur_Rate
                            ,Extractvalue (Value (Xmlmstdmy), '*/STOCK_RATE                               ') As Stock_Rate
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE                                   ') As C_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_NAME                                   ') As C_Name
                            ,Extractvalue (Value (Xmlmstdmy), '*/A_CODE                                   ') As A_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_NO                                ') As Cheque_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/NOTE_NO                                  ') As Note_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_DUE_DATE                          ') As Cheque_Due_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_DUE_DATE                            ') As Bill_Due_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/W_CODE                                   ') As W_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/R_CODE                                   ') As R_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/REP_CODE                                 ') As Rep_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/EMP_NO                                   ') As Emp_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/REF_NO                                   ') As Ref_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CASH_NO                                  ') As Cash_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CC_CODE                                  ') As Cc_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/PJ_NO                                    ') As Pj_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/ACTV_NO                                  ') As Actv_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/SI_TYPE                                  ') As Si_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/STAND_BY                                 ') As Stand_By
                            ,Extractvalue (Value (Xmlmstdmy), '*/COL_NO                                   ') As Col_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CASH_AC_FCC                              ') As Cash_Ac_Fcc
                            ,Extractvalue (Value (Xmlmstdmy), '*/BANK_NO                                  ') As Bank_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/A_DESC                                   ') As A_Desc
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_PY                                  ') As Bill_Py
                            ,Extractvalue (Value (Xmlmstdmy), '*/EXTERNAL_POST                            ') As External_Post
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD1                                   ') As Field1
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD2                                   ') As Field2
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD3                                   ') As Field3
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD4                                   ') As Field4
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD5                                   ') As Field5
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD6                                   ') As Field6
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD7                                   ') As Field7
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD8                                   ') As Field8
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD9                                   ') As Field9
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD10                                  ') As Field10
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_TEL                                    ') As C_Tel
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_ADDRESS                                ') As C_Address
                            ,Extractvalue (Value (Xmlmstdmy), '*/DRIVER_NO                                ') As Driver_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_VALUED                              ') As Bill_Valued
                            ,Extractvalue (Value (Xmlmstdmy), '*/VALUE_DATE                               ') As Value_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_WITHOUT_AUTO_OTHR_AMT               ') As Bill_Without_Auto_Othr_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/QT_PRM_NO                                ') As Qt_Prm_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/QT_PRM_SER                               ') As Qt_Prm_Ser                            
                            ,Extractvalue (Value (Xmlmstdmy), '*/QT_PRM_RCRD_NO                           ') As Qt_Prm_Rcrd_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/PRM_CODE                                 ') As Prm_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_BRN_NO                               ') As Doc_Brn_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CMPNY_NO                                 ') As Cmpny_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/MOBILE_NO                                ') As Mobile_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/NOT_USE_QUT_PRM                          ') As Not_Use_Qut_Prm
                            ,Extractvalue (Value (Xmlmstdmy), '*/RECEIVE_NM                               ') As Receive_Nm
                            ,Extractvalue (Value (Xmlmstdmy), '*/CONN_SI_WITH_OUTGONG                     ') As Conn_Si_With_Outgong
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE_CSH                               ') As C_Code_Csh
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_TAX_CODE                               ') As C_Tax_Code                           
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_NO_RES                               ') As Doc_No_Res
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SRL_RES                              ') As Doc_Srl_Res
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_CODE                                  ') As Ac_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_CODE_DTL                              ') As Ac_Code_Dtl
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_DTL_TYP                               ') As Ac_Dtl_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/PYMNT_AC                                 ') As Pymnt_Ac
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TYP_NO_TAX                           ') As Clc_Typ_No_Tax
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER_EXTRNL                           ') As Doc_Ser_Extrnl
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_NO_EXTRNL                            ') As DOC_NO_EXTRNL             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CNCL_FLG                                 ') As Cncl_Flg
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_VAT_PRICE_TYP                        ') As Clc_Vat_Price_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_AMT                                 ') As Bill_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT                                  ') As Vat_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_AFTR_VAT                        ') As Disc_Amt_Aftr_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST_VAT                         ') As Disc_Amt_Mst_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_DISC_MST                         ') As Vat_Amt_Disc_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_OTHR                             ') As Vat_Amt_Othr
                            ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT                                 ') As Othr_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT                                 ') As Disc_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST                             ') As Disc_Amt_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_DTL                             ') As Disc_Amt_Dtl
                            ,Extractvalue (Value (Xmlmstdmy), '*/ADD_DISC_AMT_MST                         ') As Add_Disc_Amt_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/ADD_DISC_AMT_DTL                         ') As Add_Disc_Amt_Dtl
                            ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT_DISC                            ') As Othr_Amt_Disc
                            ,Extractvalue (Value (Xmlmstdmy), '*/OUT_BILL_TYP                         ') As  OUT_BILL_TYP                 
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_STAT_TYP                        ') As  BILL_STAT_TYP                                                       
                            ,Extractvalue (Value (Xmlmstdmy), '*/CRD_DISC_PER                         ') As  CRD_DISC_PER                 
                            ,Extractvalue (Value (Xmlmstdmy), '*/CRD_NO_DISC                          ') As  CRD_NO_DISC                  
                            ,Extractvalue (Value (Xmlmstdmy), '*/CREDIT_CARD                          ') As  CREDIT_CARD                  
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_AMT                          ') As  CR_CARD_AMT                  
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_AMT_SCND                     ') As  CR_CARD_AMT_SCND             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_AMT_THRD                     ') As  CR_CARD_AMT_THRD             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_COMM_PER                     ') As  CR_CARD_COMM_PER             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_COMM_PER_SCND                ') As  CR_CARD_COMM_PER_SCND        
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_COMM_PER_THRD                ') As  CR_CARD_COMM_PER_THRD        
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_CST_NO                       ') As  CR_CARD_CST_NO               
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_CST_NO_SCND                  ') As  CR_CARD_CST_NO_SCND          
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_CST_NO_THRD                  ') As  CR_CARD_CST_NO_THRD          
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DOC_NO_REF                   ') As  CR_CARD_DOC_NO_REF           
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DOC_NO_REF_SCND              ') As  CR_CARD_DOC_NO_REF_SCND      
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DOC_NO_REF_THRD              ') As  CR_CARD_DOC_NO_REF_THRD      
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DSC                          ') As  CR_CARD_DSC                  
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DSC_SCND                     ') As  CR_CARD_DSC_SCND             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DSC_THRD                     ') As  CR_CARD_DSC_THRD             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_MAX_COMM_AMT                 ') As  CR_CARD_MAX_COMM_AMT         
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_MAX_COMM_AMT_SCND            ') As  CR_CARD_MAX_COMM_AMT_SCND    
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_MAX_COMM_AMT_THRD            ') As  CR_CARD_MAX_COMM_AMT_THRD    
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_NO                           ') As  CR_CARD_NO                   
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_NO_SCND                      ') As  CR_CARD_NO_SCND              
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_NO_THRD                      ') As  CR_CARD_NO_THRD              
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_DOC_NO_REF                        ') As  CR_DOC_NO_REF                
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_DOC_NO_REF_SCND                   ') As  CR_DOC_NO_REF_SCND           
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_DOC_NO_REF_THRD                   ') As  CR_DOC_NO_REF_THRD           
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUED                            ') As  CR_VALUED                    
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUED_SCND                       ') As  CR_VALUED_SCND               
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUED_THRD                       ') As  CR_VALUED_THRD               
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUE_DATE                        ') As  CR_VALUE_DATE                
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUE_DATE_SCND                   ') As  CR_VALUE_DATE_SCND           
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUE_DATE_THRD                   ') As  CR_VALUE_DATE_THRD 
                            ,Extractvalue (Value (Xmlmstdmy), '*/CPN_AMT                                  ') As Cpn_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_AMT                               ') As Cheque_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/PRCNT_AMT                                ') As Prcnt_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_AMT                                   ') As Ac_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TAX_FREE_QTY_FLG                     ') As CLC_TAX_FREE_QTY_FLG 
                            ,Extractvalue (Value (Xmlmstdmy), '*/E_INVC_MTHD_NO                           ') As E_INVC_MTHD_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/TAX_BILL_TYP                            ') As TAX_BILL_TYP
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DUE_DATE                            ') As DOC_DUE_DATE
                            ,Extractvalue (Value (Xmlmstdmy), '*/TYP_NO                                  ') As TYP_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_AMT                                 ') As DOC_AMT
                            ,Extractvalue (Value (Xmlmstdmy), '*/CMP_NO                                   ') As Cmp_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_NO                                   ') As Brn_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_YEAR                                 ') As Brn_Year
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_USR                                  ') As Brn_Usr
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_U_ID                                  ') As Ad_U_Id
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_DATE                                  ') As Ad_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_TRMNL_NM                              ') As Ad_Trmnl_Nm
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/BILL/IAS_BILL_MST'))) Xmlmstdmy)
         Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    --(11)
            --------------------------------------------------------------------------------
             V_Doc_No := M_Cv.Doc_No;            
            V_Doc_Typ := P_Doc_Typ;
            ---------------------------------------------------------------------------------
            Chk_Prmtr (   P_Sys_No            =>M_Cv.Sys_No
                          ,P_Doc_Typ          =>P_Doc_Typ                           
                          ,P_COMMIT_FLG       =>P_COMMIT_FLG
                          ,P_CLC_TAX_METHOD   =>P_CLC_TAX_METHOD                                                      
                          ,P_Pst_Typ          =>P_Pst_Typ
                          ,P_Pst_FROM_BR      =>P_Pst_FROM_BR
                          ,P_DTS_ONLINE       =>P_DTS_ONLINE
                          ,P_Lng_No           =>P_Lng_No                          
                          ,P_Msg_Txt          =>P_Msg_Txt
                          ,P_ERR_NO           =>P_ERR_NO
                          ,P_Pkg_Nm           =>P_Pkg_Nm);
                          If  P_Msg_Txt Is Not Null Then
                              Goto Rtn_Rslt;
                          End If;
          --------------------------------------------------------------------------------- 
            Begin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(1)
               Ars_Api_Trns_Pkg.Insrt_Ias_Bill_Mst (P_Sys_No                       => M_Cv.Sys_No
                                  ,P_Doc_Type                     => M_Cv.Doc_Type
                                  ,P_Bill_Doc_Type                => M_Cv.Bill_Doc_Type
                                  ,P_Doc_No                       => M_Cv.Doc_No
                                  ,P_Doc_Ser                      => NULL
                                  ,P_Doc_Date                     => TO_DATE(M_Cv.Doc_Date,'DD/MM/RRRR')
                                  ,P_Cur_Code                     => M_Cv.Cur_Code
                                  ,P_Cur_Rate                     => M_Cv.Cur_Rate
                                  ,P_Stock_Rate                   => M_Cv.Stock_Rate
                                  ,P_C_Code                       => M_Cv.C_Code
                                  ,P_C_Name                       => M_Cv.C_Name
                                  ,P_A_Code                       => M_Cv.A_Code
                                  ,P_Cheque_No                    => M_Cv.Cheque_No
                                  ,P_Note_No                      => M_Cv.Note_No
                                  ,P_Cheque_Due_Date              => TO_DATE(M_Cv.Cheque_Due_Date,'DD/MM/RRRR')
                                  ,P_Bill_Due_Date                => NVL(TO_DATE(M_Cv.DOC_Due_Date,'DD/MM/RRRR'),TO_DATE(M_Cv.Bill_Due_Date,'DD/MM/RRRR'))
                                  ,P_W_Code                       => M_Cv.W_Code
                                  ,P_R_Code                       => M_Cv.R_Code
                                  ,P_Rep_Code                     => M_Cv.Rep_Code
                                  ,P_Emp_No                       => M_Cv.Emp_No
                                  ,P_Ref_No                       => M_Cv.Ref_No
                                  ,P_Cash_No                      => M_Cv.Cash_No
                                  ,P_Cc_Code                      => M_Cv.Cc_Code
                                  ,P_Pj_No                        => M_Cv.Pj_No
                                  ,P_Actv_No                      => M_Cv.Actv_No
                                  ,P_Si_Type                      => NVL(M_Cv.TYP_NO,M_Cv.Si_Type)
                                  ,P_Stand_By                     => M_Cv.Stand_By
                                  ,P_Col_No                       => M_Cv.Col_No
                                  ,P_Cash_Ac_Fcc                  => M_Cv.Cash_Ac_Fcc
                                  ,P_Bank_No                      => M_Cv.Bank_No
                                  ,P_A_Desc                       => M_Cv.A_Desc
                                  ,P_Bill_Py                      => M_Cv.Bill_Py
                                  ,P_External_Post                => M_Cv.External_Post
                                  ,P_Field1                       => M_Cv.Field1
                                  ,P_Field2                       => M_Cv.Field2
                                  ,P_Field3                       => M_Cv.Field3
                                  ,P_Field4                       => M_Cv.Field4
                                  ,P_Field5                       => M_Cv.Field5
                                  ,P_Field6                       => M_Cv.Field6
                                  ,P_Field7                       => M_Cv.Field7
                                  ,P_Field8                       => M_Cv.Field8
                                  ,P_Field9                       => M_Cv.Field9
                                  ,P_Field10                      => M_Cv.Field10
                                  ,P_C_Tel                        => M_Cv.C_Tel
                                  ,P_C_Address                    => M_Cv.C_Address
                                  ,P_Driver_No                    => M_Cv.Driver_No
                                  ,P_Bill_Valued                  => M_Cv.Bill_Valued
                                  ,P_Value_Date                   =>TO_DATE(M_Cv.Value_Date,'DD/MM/RRRR')
                                  ,P_Bill_Without_Auto_Othr_Amt   => M_Cv.Bill_Without_Auto_Othr_Amt
                                  ,P_Qt_Prm_No                    => M_Cv.Qt_Prm_No
                                  ,P_Qt_Prm_Ser                   => M_Cv.Qt_Prm_Ser
                                  ,P_Qt_Prm_Rcrd_No               => M_Cv.Qt_Prm_Rcrd_No
                                  ,P_Prm_Code                     => M_Cv.Prm_Code
                                  ,P_Doc_Brn_No                   => M_Cv.Doc_Brn_No
                                  ,P_Cmpny_No                     => M_Cv.Cmpny_No
                                  ,P_Mobile_No                    => M_Cv.Mobile_No
                                  ,P_Not_Use_Qut_Prm              => M_Cv.Not_Use_Qut_Prm
                                  ,P_Receive_Nm                   => M_Cv.Receive_Nm
                                  ,P_Conn_Si_With_Outgong         => M_Cv.Conn_Si_With_Outgong
                                  ,P_C_Code_Csh                   => M_Cv.C_Code_Csh
                                  ,P_C_Tax_Code                   => M_Cv.C_Tax_Code                                
                                  ,P_Doc_No_Res                   => M_Cv.Doc_No_Res
                                  ,P_Doc_Srl_Res                  => M_Cv.Doc_Srl_Res
                                  ,P_Ac_Code                      => M_Cv.Ac_Code
                                  ,P_Ac_Code_Dtl                  => M_Cv.Ac_Code_Dtl
                                  ,P_Ac_Dtl_Typ                   => M_Cv.Ac_Dtl_Typ
                                  ,P_Pymnt_Ac                     => M_Cv.Pymnt_Ac
                                  ,P_Clc_Typ_No_Tax               => M_Cv.Clc_Typ_No_Tax
                                  ,P_Doc_Ser_Extrnl               => M_Cv.Doc_Ser_Extrnl
                                  ,P_DOC_NO_EXTRNL                => M_Cv.DOC_NO_EXTRNL 
                                  ,P_Cncl_Flg                     => M_Cv.Cncl_Flg
                                  ,P_Clc_Vat_Price_Typ            => M_Cv.Clc_Vat_Price_Typ
                                  ,P_Bill_Amt                     => NVL(M_Cv.DOC_Amt,M_Cv.Bill_Amt)
                                  ,P_Vat_Amt                      => M_Cv.Vat_Amt
                                  ,P_Disc_Amt_Aftr_Vat            => M_Cv.Disc_Amt_Aftr_Vat
                                  ,P_Disc_Amt_Mst_Vat             => M_Cv.Disc_Amt_Mst_Vat
                                  ,P_Vat_Amt_Disc_Mst             => M_Cv.Vat_Amt_Disc_Mst
                                  ,P_Vat_Amt_Othr                 => M_Cv.Vat_Amt_Othr
                                  ,P_Othr_Amt                     => M_Cv.Othr_Amt
                                  ,P_Disc_Amt                     => M_Cv.Disc_Amt
                                  ,P_Disc_Amt_Mst                 => M_Cv.Disc_Amt_Mst
                                  ,P_Disc_Amt_Dtl                 => M_Cv.Disc_Amt_Dtl
                                  ,P_Add_Disc_Amt_Mst             => M_Cv.Add_Disc_Amt_Mst
                                  ,P_Add_Disc_Amt_Dtl             => M_Cv.Add_Disc_Amt_Dtl
                                  ,P_Othr_Amt_Disc                => M_Cv.Othr_Amt_Disc
                                    ,P_OUT_BILL_TYP                =>M_CV.OUT_BILL_TYP                 
                                    ,P_BILL_STAT_TYP              =>M_CV.BILL_STAT_TYP                                                              
                                    ,P_CRD_DISC_PER               =>M_CV.CRD_DISC_PER                 
                                    ,P_CRD_NO_DISC                =>M_CV.CRD_NO_DISC                  
                                    ,P_CREDIT_CARD                =>M_CV.CREDIT_CARD                  
                                    ,P_CR_CARD_AMT                =>M_CV.CR_CARD_AMT                  
                                    ,P_CR_CARD_AMT_SCND           =>M_CV.CR_CARD_AMT_SCND             
                                    ,P_CR_CARD_AMT_THRD           =>M_CV.CR_CARD_AMT_THRD             
                                    ,P_CR_CARD_COMM_PER           =>M_CV.CR_CARD_COMM_PER             
                                    ,P_CR_CARD_COMM_PER_SCND      =>M_CV.CR_CARD_COMM_PER_SCND        
                                    ,P_CR_CARD_COMM_PER_THRD      =>M_CV.CR_CARD_COMM_PER_THRD        
                                    ,P_CR_CARD_CST_NO             =>M_CV.CR_CARD_CST_NO               
                                    ,P_CR_CARD_CST_NO_SCND        =>M_CV.CR_CARD_CST_NO_SCND          
                                    ,P_CR_CARD_CST_NO_THRD        =>M_CV.CR_CARD_CST_NO_THRD          
                                    ,P_CR_CARD_DOC_NO_REF         =>M_CV.CR_CARD_DOC_NO_REF           
                                    ,P_CR_CARD_DOC_NO_REF_SCND    =>M_CV.CR_CARD_DOC_NO_REF_SCND      
                                    ,P_CR_CARD_DOC_NO_REF_THRD    =>M_CV.CR_CARD_DOC_NO_REF_THRD      
                                    ,P_CR_CARD_DSC                =>M_CV.CR_CARD_DSC                  
                                    ,P_CR_CARD_DSC_SCND           =>M_CV.CR_CARD_DSC_SCND             
                                    ,P_CR_CARD_DSC_THRD           =>M_CV.CR_CARD_DSC_THRD             
                                    ,P_CR_CARD_MAX_COMM_AMT       =>M_CV.CR_CARD_MAX_COMM_AMT         
                                    ,P_CR_CARD_MAX_COMM_AMT_SCND  =>M_CV.CR_CARD_MAX_COMM_AMT_SCND    
                                    ,P_CR_CARD_MAX_COMM_AMT_THRD  =>M_CV.CR_CARD_MAX_COMM_AMT_THRD    
                                    ,P_CR_CARD_NO                 =>M_CV.CR_CARD_NO                   
                                    ,P_CR_CARD_NO_SCND            =>M_CV.CR_CARD_NO_SCND              
                                    ,P_CR_CARD_NO_THRD            =>M_CV.CR_CARD_NO_THRD              
                                    ,P_CR_DOC_NO_REF              =>M_CV.CR_DOC_NO_REF                
                                    ,P_CR_DOC_NO_REF_SCND         =>M_CV.CR_DOC_NO_REF_SCND           
                                    ,P_CR_DOC_NO_REF_THRD         =>M_CV.CR_DOC_NO_REF_THRD           
                                    ,P_CR_VALUED                  =>M_CV.CR_VALUED                    
                                    ,P_CR_VALUED_SCND             =>M_CV.CR_VALUED_SCND               
                                    ,P_CR_VALUED_THRD             =>M_CV.CR_VALUED_THRD               
                                    ,P_CR_VALUE_DATE              =>M_CV.CR_VALUE_DATE                
                                    ,P_CR_VALUE_DATE_SCND         =>M_CV.CR_VALUE_DATE_SCND           
                                    ,P_CR_VALUE_DATE_THRD         =>M_CV.CR_VALUE_DATE_THRD 
                                  ,P_Cpn_Amt                      => M_Cv.Cpn_Amt
                                  ,P_Cheque_Amt                   => M_Cv.Cheque_Amt
                                  ,P_Prcnt_Amt                    => M_Cv.Prcnt_Amt
                                  ,P_Ac_Amt                       => M_Cv.Ac_Amt
                                  ,P_CLC_TAX_FREE_QTY_FLG         =>M_Cv.CLC_TAX_FREE_QTY_FLG
                                  ,P_E_INVC_MTHD_NO               =>M_CV.E_INVC_MTHD_NO
                                  ,p_TAX_BILL_TYP                 =>M_CV.TAX_BILL_TYP 
                                  ,P_Cmp_No                       => M_Cv.Cmp_No
                                  ,P_Brn_No                       => M_Cv.Brn_No
                                  ,P_Brn_Year                     => M_Cv.Brn_Year
                                  ,P_Brn_Usr                      => M_Cv.Brn_Usr
                                  ,P_Ad_U_Id                      => M_Cv.Ad_U_Id
                                  ,P_Ad_Date                      => TO_DATE(TO_CHAR(M_CV.AD_DATE),'DD/MM/RRRR HH24:MI:SS') 
                                  ,P_Ad_Trmnl_Nm                  => M_Cv.Ad_Trmnl_Nm
                                  ,P_Pst_Typ                      => P_Pst_Typ
                                  ,P_CLC_TAX_METHOD               =>P_CLC_TAX_METHOD
                                  ,P_Pst_FROM_BR                  =>P_Pst_FROM_BR
                                  ,P_DTS_ONLINE                   =>P_DTS_ONLINE
                                  ,P_Lng_No                       =>P_Lng_No 
                                  ,P_Msg_Txt                      => P_Msg_Txt
                                  ,P_ERR_NO                     => P_Err_No
                                  ,P_Pkg_NM                       => P_Pkg_Nm);             
               If P_Msg_Txt Is Not Null Then                 
                  Goto Rtn_Rslt;
               End If;
            Exception
               When Others Then               
                  Raise_Application_Error (-20307, 'Err when insert IAS_BILL_MST DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);            
            End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            -------------------------------------------------------------------------------------------
            For D_Cv In (Select Extractvalue (Value (Xmldtldmy), '*/I_CODE                                           ') As I_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/I_QTY                                            ') As I_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/P_SIZE                                           ') As P_Size
                               ,Extractvalue (Value (Xmldtldmy), '*/P_QTY                                            ') As P_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE                                          ') As I_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE_VAT                                      ') As I_Price_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/STK_COST                                         ') As Stk_Cost
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO                                          ') As RCRD_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE                                     ') As Doc_Sequence
                               ,Extractvalue (Value (Xmldtldmy), '*/W_CODE                                           ') As W_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/CC_CODE                                          ') As Cc_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/PJ_NO                                            ') As Pj_No
                               ,Extractvalue (Value (Xmldtldmy), '*/ACTV_NO                                          ') As Actv_No
                               ,Extractvalue (Value (Xmldtldmy), '*/EXPIRE_DATE                                      ') As Expire_Date
                               ,Extractvalue (Value (Xmldtldmy), '*/BATCH_NO                                         ') As Batch_No
                               ,Extractvalue (Value (Xmldtldmy), '*/FREE_QTY                                         ') As Free_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_PER                                          ') As Vat_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT                                          ') As Vat_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT                                         ') As Othr_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/ITEM_DESC                                        ') As Item_Desc
                               ,Extractvalue (Value (Xmldtldmy), '*/BARCODE                                          ') As Barcode
                               ,Extractvalue (Value (Xmldtldmy), '*/SO_NO                                            ') As So_No
                               ,Extractvalue (Value (Xmldtldmy), '*/SO_SER                                           ') As So_Ser
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_TYPE_REF                                     ') As Doc_Type_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_NO_REF                                       ') As Doc_No_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SER_REF                                      ') As Doc_Ser_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO_REF                                      ') As RCRD_NO_REF
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER                                          ') As Dis_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT                                          ') As Dis_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST                                      ') As Dis_Amt_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL                                      ') As Dis_Amt_Dtl
                               ,Extractvalue (Value (Xmldtldmy), '*/ADD_DIS_AMT_MST                                  ') As Add_Dis_Amt_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/ADD_DIS_AMT_DTL                                  ') As Add_Dis_Amt_Dtl
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER2                                         ') As Dis_Per2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2                                     ') As Dis_Amt_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER3                                         ') As Dis_Per3
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3                                     ') As Dis_Amt_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_OTHR                                     ') As Vat_Amt_Othr
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT_DISC                                    ') As Othr_Amt_Disc
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AFTR_VAT_MST                                 ') As Dis_Aftr_Vat_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_VAT                                  ') As Dis_Amt_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2_VAT                                 ') As Dis_Amt_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL_VAT                              ') As Vat_Amt_Dis_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL3_VAT                             ') As Vat_Amt_Dis_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL2_VAT                             ') As Vat_Amt_Dis_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST_VAT                                  ') As Dis_Amt_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_MST_VAT                              ') As Vat_Amt_Dis_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_BFR_DIS                                  ') As Vat_Amt_Bfr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_AFTR_DIS                                 ') As Vat_Amt_Aftr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_AFTR_VAT                                 ') As Dis_Amt_Aftr_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_QT_PRM                               ') As Dis_Amt_Dtl_Qt_Prm
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_QT_PRM_VAT                            ') As Dis_Amt_Dtl_Qt_Prm_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER_QT_PRM                                   ') As Dis_Per_Qt_Prm
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3_VAT                                 ') As Dis_Amt_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/LEV_NO                                           ') As Lev_No
                               ,Extractvalue (Value (Xmldtldmy), '*/PRM_GRP_NO                                       ') As PRM_GRP_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_NO                                       ') As QT_PRM_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_RCRD_NO                                   ') As QT_PRM_RCRD_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_SER                                       ') As QT_PRM_SER                               
                               ,Extractvalue (Value (Xmldtldmy), '*/I_LENGTH                                         ') As I_Length
                               ,Extractvalue (Value (Xmldtldmy), '*/I_WIDTH                                          ') As I_Width
                               ,Extractvalue (Value (Xmldtldmy), '*/I_HEIGHT                                         ') As I_Height
                               ,Extractvalue (Value (Xmldtldmy), '*/I_NUMBER                                         ') As I_Number
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL1                                       ') As Field_Dtl1
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL2                                       ') As Field_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL3                                       ') As Field_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL4                                       ') As Field_Dtl4
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL5                                       ') As Field_Dtl5
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL6                                       ') As Field_Dtl6
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL7                                       ') As Field_Dtl7
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL8                                       ') As Field_Dtl8
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL9                                       ') As Field_Dtl9
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL10                                       ') As Field_Dtl10
                               ,Extractvalue (Value (Xmldtldmy), '*/UP_CNT                                           ') As Up_Cnt
                               ,Extractvalue (Value (Xmldtldmy), '*/ITM_UNT                                          ') As Itm_Unt
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_QTY                                           ') As Wt_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_UNT                                           ') As Wt_Unt
                               ,Extractvalue (Value (Xmldtldmy), '*/EMP_NO                                           ') As Emp_No
                               ,Extractvalue (Value (Xmldtldmy), '*/MEASUR_PRICE                                     ') As Measur_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/ARGMNT_NO                                        ') As Argmnt_No
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE_REF                                 ') As Doc_Sequence_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/SERIALNO_N                                      ')  As SERIALNO_N
                           From Table (Xmlsequence (Extract (V_Xml_Type, '/BILL/IAS_BILL_DTL'))) Xmldtldmy)
            Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(12)
               ---------------------
              V_Doc_Seq:=NULL;
              V_Rcrd_No:=null;
              V_Icode  :=Null;
              V_Itm_Unt:=Null;
              V_Barcode:=Null;
               
               Ias_Itm_Pkg.Get_I_Code (P_Barcode => D_Cv.I_Code, P_I_Code => V_Icode, P_Itm_Unt => V_Itm_Unt);
               If V_Icode Is  Null  Or nvl(V_Icode,'0')=Nvl(D_Cv.I_Code,'0') Then                                  
                  V_Icode  :=D_Cv.I_Code;
                  V_Itm_Unt:=D_Cv.Itm_Unt;
                  V_Barcode:=D_Cv.Barcode;
               Else
                    V_Barcode:=D_Cv.I_Code;  
               End If;            
     
               Begin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              --(2)                
                  Ars_Api_Trns_Pkg.Insrt_Ias_Bill_Dtl (P_I_Code                   => V_Icode
                                     ,P_I_Qty                    => D_Cv.I_Qty
                                     ,P_P_Size                   => D_Cv.P_Size
                                     ,P_P_Qty                    => D_Cv.P_Qty
                                     ,P_I_Price                  => D_Cv.I_Price
                                     ,P_I_Price_Vat              => D_Cv.I_Price_Vat
                                     ,P_Stk_Cost                 => D_Cv.Stk_Cost
                                     ,P_Doc_Sequence             => V_Doc_Seq
                                     ,P_Rcrd_No                  => V_Rcrd_No
                                     ,P_W_Code                   => D_Cv.W_Code
                                     ,P_Cc_Code                  => nvl(D_Cv.Cc_Code,Ars_Api_Trns_Pkg.G_Mst_Cc_Code)
                                     ,P_Pj_No                    => nvl(D_Cv.Pj_No,Ars_Api_Trns_Pkg.G_Mst_Pj_No)
                                     ,P_Actv_No                  => nvl(D_Cv.Actv_No,Ars_Api_Trns_Pkg.G_Mst_Actv_No)
                                     ,P_Expire_Date              => TO_DATE(D_Cv.Expire_Date,'DD/MM/RRRR')
                                     ,P_Batch_No                 => D_Cv.Batch_No
                                     ,P_Free_Qty                 => D_Cv.Free_Qty
                                     ,P_Vat_Per                  => D_Cv.Vat_Per
                                     ,P_Vat_Amt                  => D_Cv.Vat_Amt
                                     ,P_Othr_Amt                 => D_Cv.Othr_Amt
                                     ,P_Item_Desc                => D_Cv.Item_Desc
                                     ,P_Barcode                  => V_Barcode
                                     ,P_So_No                    => D_Cv.So_No
                                     ,P_So_Ser                   => D_Cv.So_Ser
                                     ,P_Doc_Type_Ref             => case when nvl(D_Cv.Doc_Type_Ref,0)=0 then null else D_Cv.Doc_Type_Ref end
                                     ,P_Doc_Ser_Ref              => case when nvl(D_Cv.Doc_Ser_Ref,0)=0 then null else D_Cv.Doc_Ser_Ref end
                                     ,P_Doc_No_Ref               => case when nvl(D_Cv.Doc_No_Ref,0)=0 then null else D_Cv.Doc_No_Ref end  
                                     ,P_Rcrd_No_Ref              => case when nvl(D_Cv.Rcrd_No_Ref,0)=0 then null else D_Cv.Rcrd_No_Ref end
                                     ,P_Dis_Per                  => D_Cv.Dis_Per
                                     ,P_Dis_Amt                  => D_Cv.Dis_Amt
                                     ,P_Dis_Amt_Mst              => D_Cv.Dis_Amt_Mst
                                     ,P_Dis_Amt_Dtl              => D_Cv.Dis_Amt_Dtl
                                     ,P_Add_Dis_Amt_Mst          => D_Cv.Add_Dis_Amt_Mst
                                     ,P_Add_Dis_Amt_Dtl          => D_Cv.Add_Dis_Amt_Dtl
                                     ,P_Dis_Per2                 => D_Cv.Dis_Per2
                                     ,P_Dis_Amt_Dtl2             => D_Cv.Dis_Amt_Dtl2
                                     ,P_Dis_Per3                 => D_Cv.Dis_Per3
                                     ,P_Dis_Amt_Dtl3             => D_Cv.Dis_Amt_Dtl3
                                     ,P_Vat_Amt_Othr             => D_Cv.Vat_Amt_Othr
                                     ,P_Othr_Amt_Disc            => D_Cv.Othr_Amt_Disc
                                     ,P_Dis_Aftr_Vat_Mst         => D_Cv.Dis_Aftr_Vat_Mst
                                     ,P_Dis_Amt_Dtl_Vat          => D_Cv.Dis_Amt_Dtl_Vat
                                     ,P_Dis_Amt_Dtl2_Vat         => D_Cv.Dis_Amt_Dtl2_Vat
                                     ,P_Vat_Amt_Dis_Dtl_Vat      => D_Cv.Vat_Amt_Dis_Dtl_Vat
                                     ,P_Vat_Amt_Dis_Dtl3_Vat     => D_Cv.Vat_Amt_Dis_Dtl3_Vat
                                     ,P_Vat_Amt_Dis_Dtl2_Vat     => D_Cv.Vat_Amt_Dis_Dtl2_Vat
                                     ,P_Dis_Amt_Mst_Vat          => D_Cv.Dis_Amt_Mst_Vat
                                     ,P_Vat_Amt_Dis_Mst_Vat      => D_Cv.Vat_Amt_Dis_Mst_Vat
                                     ,P_Vat_Amt_Bfr_Dis          => D_Cv.Vat_Amt_Bfr_Dis
                                     ,P_Vat_Amt_Aftr_Dis         => D_Cv.Vat_Amt_Aftr_Dis
                                     ,P_Dis_Amt_Aftr_Vat         => D_Cv.Dis_Amt_Aftr_Vat
                                     ,P_Dis_Amt_Dtl_Qt_Prm       => D_Cv.Dis_Amt_Dtl_Qt_Prm
                                     ,P_Dis_Amt_Dtl_Qt_Prm_Vat   => D_Cv.Dis_Amt_Dtl_Qt_Prm_Vat
                                     ,P_Dis_Per_Qt_Prm           => D_Cv.Dis_Per_Qt_Prm
                                     ,P_Dis_Amt_Dtl3_Vat         => D_Cv.Dis_Amt_Dtl3_Vat
                                     ,P_Lev_No                   => D_Cv.Lev_No
                                     ,P_PRM_GRP_NO               => Case When nvl(D_Cv.PRM_GRP_NO,0)=0 Then Null Else  D_Cv.PRM_GRP_NO end 
                                     ,P_QT_PRM_NO                => Case When nvl(D_cv.QT_PRM_NO,0)=0 Then Null Else D_cv.QT_PRM_NO end 
                                     ,P_QT_PRM_RCRD_NO           =>Case When nvl(D_Cv.QT_PRM_RCRD_NO,0)=0 Then Null Else D_Cv.QT_PRM_RCRD_NO end 
                                     ,P_QT_PRM_SER               =>Case When nvl(D_Cv.QT_PRM_SER,0)=0 Then Null Else D_Cv.QT_PRM_SER end                                    
                                     ,P_I_Length                 => D_Cv.I_Length
                                     ,P_I_Width                  => D_Cv.I_Width
                                     ,P_I_Height                 => D_Cv.I_Height
                                     ,P_I_Number                 => D_Cv.I_Number
                                     ,P_Field_Dtl1               => D_Cv.Field_Dtl1
                                     ,P_Field_Dtl2               => D_Cv.Field_Dtl2
                                     ,P_Field_Dtl3               => D_Cv.Field_Dtl3
                                     ,P_Field_Dtl4               => D_Cv.Field_Dtl4
                                     ,P_Field_Dtl5               => D_Cv.Field_Dtl5
                                     ,P_Field_Dtl6               => D_Cv.Field_Dtl6
                                     ,P_Field_Dtl7               => D_Cv.Field_Dtl7
                                     ,P_Field_Dtl8               => D_Cv.Field_Dtl8
                                     ,P_Field_Dtl9               => D_Cv.Field_Dtl9
                                     ,P_Field_Dtl10               => D_Cv.Field_Dtl10                                    
                                     ,P_Up_Cnt                   => D_Cv.Up_Cnt
                                     ,P_Itm_Unt                  => V_Itm_Unt
                                     ,P_Wt_Qty                   => D_Cv.Wt_Qty
                                     ,P_Wt_Unt                   => D_Cv.Wt_Unt
                                     ,P_Emp_No                   => D_Cv.Emp_No
                                     ,P_Measur_Price             => D_Cv.Measur_Price
                                     ,P_Argmnt_No                => D_Cv.Argmnt_No
                                     ,P_Doc_Sequence_Ref         => D_Cv.Doc_Sequence_Ref
                                     ,P_SERIALNO_N               =>D_CV.SERIALNO_N
                                     ,P_Msg_Txt                  => P_Msg_Txt
                                     ,P_ERR_NO                 => P_Err_No
                                     ,P_Pkg_NM                   => P_Pkg_Nm);

                  If P_Msg_Txt Is Not Null Then                   
                     Goto Rtn_Rslt;
                  End If;
               Exception
                  When Others Then
                    -- ---Rollback;
                     Raise_Application_Error (-20308, 'Err when insert IAS_BILL_DTL DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);
               End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --(2)
            --##------------------------------------------------------------------------------------------------------------------------------##--
             For Tax_Mvmnt_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As Bill_Doc_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As Doc_Jv_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As Tax_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As Clc_Typ_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As Agncy_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                      ') As I_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                     ') As Itm_Unt
                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                      ') As P_Size
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_PRICE                     ') As I_Price
                                      ,Extractvalue( Value( Xmldtldmy), '*/DISC_AMT                    ') As Disc_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                    ') As A_Cy
                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As Ac_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As Tax_Prcnt
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As Tax_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                      ') As W_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As Cc_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As Pj_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As Actv_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As Rcrd_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As Doc_Sequence
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As Tax_Amt_L
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_QTY                       ') As I_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/FREE_QTY                    ') As Free_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As Ref_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_COST                    ') As Stk_Cost
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_RATE                    ') As Stk_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TAX_FREE_QTY_FLG        ') As Clc_Tax_Free_Qty_Flg
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/BILL/GNR_TAX_ITM_MOVMNT'))) Xmldtldmy                                  
                                   )                              
               Loop
                   IF NVL(Tax_Mvmnt_Cv.I_CODE,'0')=NVL(D_CV.I_CODE,'0')  AND NVL(Tax_Mvmnt_Cv.ITM_UNT,'0')=NVL(D_CV.ITM_UNT,'0')
                     AND NVL(Tax_Mvmnt_Cv.RCRD_NO,0)=NVL(D_CV.RCRD_NO,0) THEN    
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Gnr_Tax_Itm_Movmnt(P_Doc_Typ               => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Bill_Doc_Type          => Ars_Api_Trns_Pkg.G_Bill_Doc_Type
                                                     ,P_Doc_Jv_Type            => Ars_Api_Trns_Pkg.G_SI_TYPE
                                                     ,P_Tax_No                 => Tax_Mvmnt_Cv.Tax_No
                                                     ,P_Clc_Typ_No             => Tax_Mvmnt_Cv.Clc_Typ_No
                                                     ,P_Agncy_No               => Tax_Mvmnt_Cv.Agncy_No
                                                     ,P_I_Code                 => V_Icode
                                                     ,P_Itm_Unt                => V_Itm_Unt
                                                     ,P_P_Size                 => Tax_Mvmnt_Cv.P_Size
                                                     ,P_I_Price                => Tax_Mvmnt_Cv.I_Price
                                                     ,P_Disc_Amt               => Tax_Mvmnt_Cv.Disc_Amt
                                                     ,P_A_Code                 => Tax_Mvmnt_Cv.A_Code
                                                     ,P_Cur_Code               => Tax_Mvmnt_Cv.A_Cy
                                                     ,P_Ac_Rate                => Tax_Mvmnt_Cv.Ac_Rate
                                                     ,P_Tax_Prcnt              => Tax_Mvmnt_Cv.Tax_Prcnt
                                                     ,P_Tax_Amt                => Tax_Mvmnt_Cv.Tax_Amt
                                                     ,P_W_Code                 => Ars_Api_Trns_Pkg.G_W_Code
                                                     ,P_Cc_Code                => Ars_Api_Trns_Pkg.G_Dtl_Cc_Code
                                                     ,P_Pj_No                  => Ars_Api_Trns_Pkg.G_Dtl_Pj_No
                                                     ,P_Actv_No                => Ars_Api_Trns_Pkg.G_Dtl_Actv_No                                                     
                                                     ,P_Doc_Sequence           => V_Doc_Seq
                                                     ,P_Rcrd_No                => V_Rcrd_No
                                                     ,P_Tax_Amt_L              => Tax_Mvmnt_Cv.Tax_Amt_L
                                                     ,P_I_Qty                  => Tax_Mvmnt_Cv.I_Qty
                                                     ,P_Free_Qty               => Tax_Mvmnt_Cv.Free_Qty
                                                     ,P_Ref_No                 => Tax_Mvmnt_Cv.Ref_No
                                                     ,P_Stk_Cost               => Tax_Mvmnt_Cv.Stk_Cost
                                                     ,P_Stk_Rate               => Tax_Mvmnt_Cv.Stk_Rate
                                                     ,P_Clc_Tax_Free_Qty_Flg   => M_CV.Clc_Tax_Free_Qty_Flg
                                                     ,P_Msg_Txt                => P_Msg_Txt
                                                     ,P_ERR_NO                 => P_Err_No
                                                     ,P_Pkg_Nm                 => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then
                       -- ---Rollback;
                        Raise_Application_Error( -20309, 'ERR WHEN INSERT INSRT_GNR_TAX_ITM_MOVMNT DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                    End;
                 END IF; 
               End Loop;            
             --##---------------------------------------------------------------------------------------------------------------------------##--
            End Loop;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
            --##---------------------------------------------------------------------------------------------------------------------------##--
            --##INSERT OTHER CHARGE
                         For Othr_Chrg_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                        ') As Sc_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                       ') As A_Code
                                          ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                     ') As A_Cy
                                          ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                      ') As Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/PER                          ') As Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/AMT                          ') As Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/INV_ITEM                     ') As Inv_Item
                                          ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                      ') As Rcrd_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                      ') As Bill_Py
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_AMT                      ') As Vat_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_PER                      ') As Vat_Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AMT                       ') As Sc_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AC_RATE                   ') As Sc_Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_A_CY                      ') As Sc_A_Cy
                                      From Table( Xmlsequence( Extract( V_Xml_Type, '/BILL/OTHER_CHARGES'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Other_Charges(P_Doc_Typ      => Ars_Api_Trns_Pkg.G_Doc_Typ
                                        ,P_Bill_Doc_Type  => Ars_Api_Trns_Pkg.G_Bill_Doc_Type
                                        ,P_BILL_TYPE      =>1
                                        ,P_Sc_No        => Othr_Chrg_Cv.Sc_No
                                        ,P_A_Code       => Othr_Chrg_Cv.A_Code
                                        ,P_Cur_Code     => Othr_Chrg_Cv.A_Cy
                                        ,P_Ac_Rate      => Othr_Chrg_Cv.Ac_Rate
                                        ,P_Per          => Othr_Chrg_Cv.Per
                                        ,P_Amt          => Othr_Chrg_Cv.Amt
                                        ,P_Inv_Item     => Othr_Chrg_Cv.Inv_Item
                                        ,P_Rcrd_No      => Othr_Chrg_Cv.Rcrd_No
                                        ,P_Bill_Py      => Othr_Chrg_Cv.Bill_Py
                                        ,P_Vat_Amt      => Othr_Chrg_Cv.Vat_Amt
                                        ,P_Vat_Per      => Othr_Chrg_Cv.Vat_Per
                                        ,P_Sc_Amt       => Othr_Chrg_Cv.Sc_Amt
                                        ,P_Sc_Ac_Rate   => Othr_Chrg_Cv.Sc_Ac_Rate
                                        ,P_Sc_A_Cy      => Othr_Chrg_Cv.Sc_A_Cy
                                        ,P_Msg_Txt      => P_Msg_Txt
                                        ,P_ERR_NO     => P_Err_No
                                        ,P_Pkg_Nm       => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                      --  ---Rollback;
                        Raise_Application_Error( -20310, 'ERR WHEN INSERT OTHER_CHARGES DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
         --##INSERT OTHER CHARGE ITEMS
               For Othr_Chrg_Itm_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                    ') As Doc_Typ
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                      ') As Sc_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                     ') As A_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                   ') As A_Cy
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                    ') As Ac_Rate
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PER                        ') As Per
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AMT                        ') As Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                     ') As W_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                    ') As Cc_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                      ') As Pj_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                    ') As Actv_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                    ') As Rcrd_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SI_TYPE                    ') As Si_Type
                                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                     ') As I_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                    ') As Itm_Unt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                     ') As P_Size
                                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                    ') As Bill_Py
                                                      ,Extractvalue( Value( Xmldtldmy), '*/UNIT_AMT                   ') As Unit_Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/POST_CODE                  ') As Post_Code
                                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/BILL/OTHER_CHARGES_ITEMS'))) Xmldtldmy)
                       Loop
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Other_Charges_Items(P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                      ,P_Sc_No       => Othr_Chrg_Itm_Cv.Sc_No
                                                      ,P_A_Code      => Othr_Chrg_Itm_Cv.A_Code
                                                      ,P_Cur_Code    => Othr_Chrg_Itm_Cv.A_Cy
                                                      ,P_Ac_Rate     => Othr_Chrg_Itm_Cv.Ac_Rate
                                                      ,P_Per         => Othr_Chrg_Itm_Cv.Per
                                                      ,P_Amt         => Othr_Chrg_Itm_Cv.Amt
                                                      ,P_W_Code      => Othr_Chrg_Itm_Cv.W_Code
                                                      ,P_Cc_Code     => Ars_Api_Trns_Pkg.G_Dtl_Cc_Code
                                                      ,P_Pj_No       => Ars_Api_Trns_Pkg.G_Dtl_Pj_No
                                                      ,P_Actv_No     => Ars_Api_Trns_Pkg.G_Dtl_Actv_No 
                                                      ,P_Rcrd_No     => Othr_Chrg_Itm_Cv.Rcrd_No
                                                      ,P_Si_Type     => Othr_Chrg_Itm_Cv.Si_Type
                                                      ,P_I_Code      => Othr_Chrg_Itm_Cv.I_Code
                                                      ,P_Itm_Unt     => Othr_Chrg_Itm_Cv.Itm_Unt
                                                      ,P_P_Size      => Othr_Chrg_Itm_Cv.P_Size
                                                      ,P_Bill_Py     => Othr_Chrg_Itm_Cv.Bill_Py
                                                      ,P_Unit_Amt    => Othr_Chrg_Itm_Cv.Unit_Amt
                                                      ,P_Post_Code   => Othr_Chrg_Itm_Cv.Post_Code
                                                      ,P_Msg_Txt     => P_Msg_Txt
                                                      ,P_ERR_NO    => P_Err_No
                                                      ,P_Pkg_Nm      => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                          Exception
                             When Others Then
                              --  ---Rollback;
                                Raise_Application_Error( -20311, 'ERR WHEN INSERT OTHER_CHARGES_ITEMS DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                          End;
                       End Loop; 
         --##---------------------------------------------------------------------------------------------------------------------------##--
         For Tax_INPT_Mvmnt_Cv In (SELECT    Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As DOC_TYP              
                                            ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As BILL_DOC_TYPE         
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As DOC_JV_TYPE                                                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As TAX_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As CLC_TYP_NO           
                                            ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As AGNCY_NO                                        
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_CODE                   ') As INPT_CODE            
                                            ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_CODE               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                    ') As CUR_CODE                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As AC_RATE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_AMT                    ') As INPT_AMT             
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As TAX_PRCNT            
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As TAX_AMT              
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As TAX_AMT_L            
                                            ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As CC_CODE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As PJ_NO                
                                            ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As ACTV_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As REF_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As RCRD_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As DOC_SEQUENCE
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/BILL/GNR_TAX_INPT_MOVMNT'))) Xmldtldmy                                  
                                   )                              
               Loop                    
                    Begin
                          Ars_Api_Trns_Pkg.INSRT_GNR_TAX_INPT_MOVMNT(
                                            P_DOC_TYP                    =>Ars_Api_Trns_Pkg.G_DOC_TYP
                                           ,P_BILL_DOC_TYPE              =>Ars_Api_Trns_Pkg.G_BILL_DOC_TYPE
                                           ,P_DOC_JV_TYPE                =>Ars_Api_Trns_Pkg.G_SI_TYPE                                      
                                           ,P_TAX_NO                     =>Tax_INPT_Mvmnt_Cv.TAX_NO
                                          , P_CLC_TYP_NO                 =>Tax_INPT_Mvmnt_Cv.CLC_TYP_NO 
                                          , P_AGNCY_NO                   =>Tax_INPT_Mvmnt_Cv.AGNCY_NO                            
                                          , P_INPT_CODE                  =>Tax_INPT_Mvmnt_Cv.INPT_CODE 
                                           ,P_A_CODE                     =>Tax_INPT_Mvmnt_Cv.A_CODE 
                                          , P_A_CY                       =>Tax_INPT_Mvmnt_Cv.CUR_CODE
                                          , P_AC_RATE                    =>Tax_INPT_Mvmnt_Cv.AC_RATE 
                                          , P_INPT_AMT                   =>Tax_INPT_Mvmnt_Cv.INPT_AMT 
                                          , P_TAX_PRCNT                  =>Tax_INPT_Mvmnt_Cv.TAX_PRCNT 
                                          , P_TAX_AMT                    =>Tax_INPT_Mvmnt_Cv.TAX_AMT
                                          , P_TAX_AMT_L                  =>Tax_INPT_Mvmnt_Cv.TAX_AMT_L 
                                           ,P_CC_CODE                    =>Ars_Api_Trns_Pkg.G_Mst_CC_CODE 
                                          , P_PJ_NO                      =>Ars_Api_Trns_Pkg.G_Mst_PJ_NO 
                                          , P_ACTV_NO                    =>Ars_Api_Trns_Pkg.G_Mst_ACTV_NO 
                                          , P_REF_NO                     =>Tax_INPT_Mvmnt_Cv.REF_NO 
                                          , P_RCRD_NO                    =>Tax_INPT_Mvmnt_Cv.RCRD_NO 
                                          , P_DOC_SEQUENCE               =>Tax_INPT_Mvmnt_Cv.DOC_SEQUENCE
                                          ,P_Msg_Txt                     =>P_Msg_Txt
                                          ,P_ERR_NO                     =>P_ERR_NO
                                          ,P_Pkg_NM                     =>P_Pkg_NM); 

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then
                       -- ---Rollback;
                        Raise_Application_Error( -20546, 'ERR WHEN INSERT INSRT_GNR_TAX_INPT_MOVMNT DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                    End;                 
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
            For Attach_Cv
                  In (Select Extractvalue (Value (Xmldtldmy), '*/FILE_NAME         ') As File_Name
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/BILL/ATTACH'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Archives (P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Doc_Ser     => Ars_Api_Trns_Pkg.G_Doc_Ser
                                                     ,P_File_Name   => Attach_Cv.File_Name
                                                     ,P_Msg_Txt     => P_Msg_Txt
                                                     ,P_Err_No      => P_Err_No
                                                     ,P_Pkg_Nm      => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                        Raise_Application_Error (-20719,'Err.in Ars_Api_Trns_Pkg.INSRT_ARCHIVES= '|| V_Doc_No|| ' '|| Chr (10)|| Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--                                       
            --## CHK INSERT DATA
            Ars_Api_Trns_Pkg.Chk_Insrt_Data (P_Doc_Typ    => 4
                           ,P_Doc_Ser    => Ars_Api_Trns_Pkg.G_Doc_Ser
                           ,P_Msg_Txt    => P_Msg_Txt
                           ,P_ERR_NO   => P_Err_No
                           ,P_Pkg_NM   => P_Pkg_Nm);

             If P_Msg_Txt Is Not Null Then             
               Rollback;
               Goto Rtn_Rslt;
             End If;                          
               --------------------------------------------
             --## POST INTO ONYX IF SYSTEM IS DISTRBUTED AND ONLINE
                IF NVL(Ars_Api_Trns_Pkg.G_SYS_NO,0)=70 AND NVL(P_DTS_ONLINE,0)=1 THEN
                 Ars_Api_Trns_Pkg.Post_From_Br_Prc (P_Sys_No    =>Ars_Api_Trns_Pkg.G_SYS_NO
                                  ,P_Doc_Typ    =>4
                                  ,P_Doc_Ser    =>Ars_Api_Trns_Pkg.G_Doc_Ser
                                  ,P_Lng_No     =>Ars_Api_Trns_Pkg.G_LNG_NO                             
                                  ,P_Msg_Txt    =>P_Msg_Txt
                                  ,P_ERR_NO     =>P_ERR_NO
                                  ,P_Pkg_Nm     =>P_Pkg_Nm) ; 
                    If P_Msg_Txt Is Not Null Then                                   
                      Goto Rtn_Rslt;
                    End If;
                END IF;               
         ----------------------------------------------------------------------------------------------------------
         End Loop;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --(11)
      Elsif P_Doc_Typ = 5 Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         -- RT BILL SALES
         For M_Cv In (Select Extractvalue (Value (Xmlmstdmy), '*/SYS_NO                          ') As Sys_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_TYPE                        ') As Doc_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_NO                          ') As Doc_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER                         ') As Doc_Ser
                            ,Extractvalue (Value (Xmlmstdmy), '*/RT_BILL_DOC_TYPE                ') As Rt_Bill_Doc_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DATE                        ') As Doc_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/CUR_CODE                        ') As Cur_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/CUR_RATE                        ') As Cur_Rate
                            ,Extractvalue (Value (Xmlmstdmy), '*/STOCK_RATE                      ') As Stock_Rate
                            ,Extractvalue (Value (Xmlmstdmy), '*/P_YEAR                          ') As P_Year
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE                          ') As C_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_NAME                          ') As C_Name
                            ,Extractvalue (Value (Xmlmstdmy), '*/A_CODE                          ') As A_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_NO_MNL                     ') As BILL_NO_MNL                            
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_NO                       ') As Cheque_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_AMT                      ') As Cheque_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_DUE_DATE                 ') As Cheque_Due_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/RT_BILL_DUE_DATE                ') As Rt_Bill_Due_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/W_CODE                          ') As W_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/R_CODE                          ') As R_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/CASH_NO                         ') As Cash_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CC_CODE                         ') As Cc_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/PJ_NO                           ') As Pj_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/ACTV_NO                         ') As Actv_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CASH_AC_FCC                     ') As Cash_Ac_Fcc
                            ,Extractvalue (Value (Xmlmstdmy), '*/BANK_NO                         ') As Bank_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TYP_NO_TAX                  ') As Clc_Typ_No_Tax
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_CODE                         ') As Ac_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_CODE_DTL                     ') As Ac_Code_Dtl
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_DTL_TYP                      ') As Ac_Dtl_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/REP_CODE                        ') As Rep_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/EMP_NO                          ') As Emp_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/SR_TYPE                         ') As Sr_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/REF_NO                          ') As Ref_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/A_DESC                          ') As A_Desc
                            ,Extractvalue (Value (Xmlmstdmy), '*/RETURN_RES                      ') As Return_Res
                            ,Extractvalue (Value (Xmlmstdmy), '*/PREV_YEAR                       ') As Prev_Year
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLASSIFY_NO                     ') As Classify_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLASSIFY_SER                    ') As Classify_Ser
                            ,Extractvalue (Value (Xmlmstdmy), '*/W_CODE_BILL                     ') As W_Code_Bill
                            ,Extractvalue (Value (Xmlmstdmy), '*/CC_CODE_BILL                    ') As Cc_Code_Bill
                            ,Extractvalue (Value (Xmlmstdmy), '*/REP_CODE_BILL                   ') As Rep_Code_Bill
                            ,Extractvalue (Value (Xmlmstdmy), '*/STAND_BY                        ') As Stand_By
                            ,Extractvalue (Value (Xmlmstdmy), '*/NOTE_NO                         ') As Note_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DRIVER_NO                       ') As Driver_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_BRN_NO                      ') As Doc_Brn_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/RES_TYP                         ') As Res_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/WITHOUT_VAT                     ') As Without_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/RT_VAT_PRD_TYP                  ') As Rt_Vat_Prd_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE_CSH                      ') As C_Code_Csh
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_TEL                           ') As C_Tel
                            ,Extractvalue (Value (Xmlmstdmy), '*/PYMNT_AC                        ') As Pymnt_Ac
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_AMT                          ') As Ac_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER_EXTRNL                  ') As Doc_Ser_Extrnl
                            ,Extractvalue (Value (Xmlmstdmy), '*/CNCL_FLG                        ') As Cncl_Flg
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_VAT_PRICE_TYP               ') As Clc_Vat_Price_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/COL_NO                          ') As Col_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD1                          ') As Field1
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD2                          ') As Field2
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD3                          ') As Field3
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD4                          ') As Field4
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD5                          ') As Field5
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD6                          ') As Field6
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD7                          ') As Field7
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD8                          ') As Field8
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD9                          ') As Field9
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD10                         ') As Field10
                            ,Extractvalue (Value (Xmlmstdmy), '*/PRM_CODE                        ') As Prm_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_AMT                        ') As Bill_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT                        ') As Disc_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST                    ') As Disc_Amt_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_DTL                    ') As Disc_Amt_Dtl
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT                         ') As Vat_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT                        ') As Othr_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT_DISC                   ') As Othr_Amt_Disc
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_OTHR                    ') As Vat_Amt_Othr
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_AFTR_VAT               ') As Disc_Amt_Aftr_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST_VAT                ') As Disc_Amt_Mst_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_DISC_MST                ') As Vat_Amt_Disc_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TAX_FREE_QTY_FLG            ') As CLC_TAX_FREE_QTY_FLG
                            ,Extractvalue (Value (Xmlmstdmy), '*/E_INVC_MTHD_NO                  ') As E_INVC_MTHD_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_DOC_TYPE                   ') As BILL_DOC_TYPE
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DUE_DATE                    ') As DOC_DUE_DATE
                            ,Extractvalue (Value (Xmlmstdmy), '*/TYP_NO                          ') As TYP_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_AMT                         ') As DOC_AMT
                             ,Extractvalue (Value (Xmlmstdmy), '*/CRD_DISC_PER                         ') As  CRD_DISC_PER                 
                            ,Extractvalue (Value (Xmlmstdmy), '*/CRD_NO_DISC                          ') As  CRD_NO_DISC                  
                            ,Extractvalue (Value (Xmlmstdmy), '*/CREDIT_CARD                          ') As  CREDIT_CARD                  
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_AMT                          ') As  CR_CARD_AMT                  
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_AMT_SCND                     ') As  CR_CARD_AMT_SCND             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_AMT_THRD                     ') As  CR_CARD_AMT_THRD             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_COMM_PER                     ') As  CR_CARD_COMM_PER             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_COMM_PER_SCND                ') As  CR_CARD_COMM_PER_SCND        
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_COMM_PER_THRD                ') As  CR_CARD_COMM_PER_THRD        
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_CST_NO                       ') As  CR_CARD_CST_NO               
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_CST_NO_SCND                  ') As  CR_CARD_CST_NO_SCND          
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_CST_NO_THRD                  ') As  CR_CARD_CST_NO_THRD          
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DOC_NO_REF                   ') As  CR_CARD_DOC_NO_REF           
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DOC_NO_REF_SCND              ') As  CR_CARD_DOC_NO_REF_SCND      
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DOC_NO_REF_THRD              ') As  CR_CARD_DOC_NO_REF_THRD      
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DSC                          ') As  CR_CARD_DSC                  
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DSC_SCND                     ') As  CR_CARD_DSC_SCND             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_DSC_THRD                     ') As  CR_CARD_DSC_THRD             
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_MAX_COMM_AMT                 ') As  CR_CARD_MAX_COMM_AMT         
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_MAX_COMM_AMT_SCND            ') As  CR_CARD_MAX_COMM_AMT_SCND    
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_MAX_COMM_AMT_THRD            ') As  CR_CARD_MAX_COMM_AMT_THRD    
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_NO                           ') As  CR_CARD_NO                   
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_NO_SCND                      ') As  CR_CARD_NO_SCND              
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_CARD_NO_THRD                      ') As  CR_CARD_NO_THRD              
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_DOC_NO_REF                        ') As  CR_DOC_NO_REF                
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_DOC_NO_REF_SCND                   ') As  CR_DOC_NO_REF_SCND           
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_DOC_NO_REF_THRD                   ') As  CR_DOC_NO_REF_THRD           
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUED                            ') As  CR_VALUED                    
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUED_SCND                       ') As  CR_VALUED_SCND               
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUED_THRD                       ') As  CR_VALUED_THRD               
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUE_DATE                        ') As  CR_VALUE_DATE                
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUE_DATE_SCND                   ') As  CR_VALUE_DATE_SCND           
                            ,Extractvalue (Value (Xmlmstdmy), '*/CR_VALUE_DATE_THRD                   ') As  CR_VALUE_DATE_THRD
                            ,Extractvalue (Value (Xmlmstdmy), '*/RTRN_FROM_OTHR_SMAN             ') As RTRN_FROM_OTHR_SMAN
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_TAX_CODE                      ') As C_TAX_CODE
                            ,Extractvalue (Value (Xmlmstdmy), '*/MOBILE_NO                       ') As MOBILE_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_ADDRESS                       ') As C_ADDRESS
                            ,Extractvalue (Value (Xmlmstdmy), '*/CMP_NO                          ') As Cmp_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_NO                          ') As Brn_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_YEAR                        ') As Brn_Year
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_USR                         ') As Brn_Usr
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_U_ID                         ') As Ad_U_Id
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_DATE                         ') As Ad_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_TRMNL_NM                     ') As Ad_Trmnl_Nm
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/RT_BILL/IAS_RT_BILL_MST'))) Xmlmstdmy)
         Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    --(11)
            --------------------------------------------------------------------------------           
            V_Doc_No := M_Cv.Doc_No;            
            V_Doc_Typ := P_Doc_Typ;

            ---------------------------------------------------------------------------------
            Chk_Prmtr (   P_Sys_No            =>M_Cv.Sys_No
                          ,P_Doc_Typ          =>P_Doc_Typ                           
                          ,P_COMMIT_FLG       =>P_COMMIT_FLG
                          ,P_CLC_TAX_METHOD   =>P_CLC_TAX_METHOD                                                      
                          ,P_Pst_Typ          =>P_Pst_Typ
                          ,P_Pst_FROM_BR      =>P_Pst_FROM_BR
                          ,P_DTS_ONLINE       =>P_DTS_ONLINE
                          ,P_Lng_No           =>P_Lng_No                          
                          ,P_Msg_Txt          =>P_Msg_Txt
                          ,P_ERR_NO           =>P_ERR_NO
                          ,P_Pkg_Nm           =>P_Pkg_Nm);
                          If  P_Msg_Txt Is Not Null Then
                              Goto Rtn_Rslt;
                          End If;
          --------------------------------------------------------------------------------- 
            Begin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(1)
               Ars_Api_Trns_Pkg.Insrt_Ias_Rt_Bill_Mst (P_Sys_No              => M_Cv.Sys_No
                                     ,P_Doc_Type            => M_Cv.Doc_Type
                                     ,P_Doc_No              => M_Cv.Doc_No
                                     ,P_Doc_Ser             => NULL
                                     ,P_Rt_Bill_Doc_Type    => NVL(M_Cv.Bill_Doc_Type,M_Cv.Rt_Bill_Doc_Type)
                                     ,P_Doc_Date            => TO_DATE(M_Cv.Doc_Date,'DD/MM/RRRR')
                                     ,P_Cur_Code            => M_Cv.Cur_Code
                                     ,P_Cur_Rate            => M_Cv.Cur_Rate
                                     ,P_Stock_Rate          => M_Cv.Stock_Rate
                                     ,P_P_Year              => M_Cv.P_Year
                                     ,P_C_Code              => M_Cv.C_Code
                                     ,P_C_Name              => M_Cv.C_Name
                                     ,P_A_Code              => M_Cv.A_Code
                                     ,P_BILL_NO_MNL         =>M_Cv.BILL_NO_MNL
                                     ,P_Cheque_No           => M_Cv.Cheque_No
                                     ,P_Cheque_Amt          => M_Cv.Cheque_Amt
                                     ,P_Cheque_Due_Date     => TO_DATE(M_Cv.Cheque_Due_Date,'DD/MM/RRRR')
                                     ,P_Rt_Bill_Due_Date    => NVL(TO_DATE(M_Cv.DOC_DUE_DATE,'DD/MM/RRRR'),TO_DATE(M_Cv.Rt_Bill_Due_Date,'DD/MM/RRRR'))
                                     ,P_W_Code              => M_Cv.W_Code
                                     ,P_R_Code              => M_Cv.R_Code
                                     ,P_Cash_No             => M_Cv.Cash_No
                                     ,P_Cc_Code             => M_Cv.Cc_Code
                                     ,P_Pj_No               => M_Cv.Pj_No
                                     ,P_Actv_No             => M_Cv.Actv_No
                                     ,P_Cash_Ac_Fcc         => M_Cv.Cash_Ac_Fcc
                                     ,P_Bank_No             => M_Cv.Bank_No
                                     ,P_Clc_Typ_No_Tax      => M_Cv.Clc_Typ_No_Tax
                                     ,P_Ac_Code             => M_Cv.Ac_Code
                                     ,P_Ac_Code_Dtl         => M_Cv.Ac_Code_Dtl
                                     ,P_Ac_Dtl_Typ          => M_Cv.Ac_Dtl_Typ
                                     ,P_Rep_Code            => M_Cv.Rep_Code
                                     ,P_Emp_No              => M_Cv.Emp_No
                                     ,P_Sr_Type             => NVL(M_Cv.TYP_NO,M_Cv.Sr_Type)
                                     ,P_Ref_No              => M_Cv.Ref_No
                                     ,P_A_Desc              => M_Cv.A_Desc
                                     ,P_Return_Res          => M_Cv.Return_Res
                                     ,P_Prev_Year           => M_Cv.Prev_Year
                                     ,P_Classify_No         => M_Cv.Classify_No
                                     ,P_Classify_Ser        => M_Cv.Classify_Ser
                                     ,P_W_Code_Bill         => M_Cv.W_Code_Bill
                                     ,P_Cc_Code_Bill        => M_Cv.Cc_Code_Bill
                                     ,P_Rep_Code_Bill       => M_Cv.Rep_Code_Bill
                                     ,P_Stand_By            => M_Cv.Stand_By
                                     ,P_Note_No             => M_Cv.Note_No
                                     ,P_Driver_No           => M_Cv.Driver_No
                                     ,P_Doc_Brn_No          => M_Cv.Doc_Brn_No
                                     ,P_Res_Typ             => M_Cv.Res_Typ
                                     ,P_Without_Vat         => M_Cv.Without_Vat
                                     ,P_Rt_Vat_Prd_Typ      => M_Cv.Rt_Vat_Prd_Typ
                                     ,P_C_Code_Csh          => M_Cv.C_Code_Csh
                                     ,P_C_Tel               => M_Cv.C_Tel
                                     ,P_Pymnt_Ac            => M_Cv.Pymnt_Ac
                                     ,P_Ac_Amt              => M_Cv.Ac_Amt
                                     ,P_Doc_Ser_Extrnl      => M_Cv.Doc_Ser_Extrnl
                                     ,P_Cncl_Flg            => M_Cv.Cncl_Flg
                                     ,P_Clc_Vat_Price_Typ   => M_Cv.Clc_Vat_Price_Typ
                                     ,P_Col_No              => M_Cv.Col_No
                                     ,P_Field1              => M_Cv.Field1
                                     ,P_Field2              => M_Cv.Field2
                                     ,P_Field3              => M_Cv.Field3
                                     ,P_Field4              => M_Cv.Field4
                                     ,P_Field5              => M_Cv.Field5
                                     ,P_Field6              => M_Cv.Field6
                                     ,P_Field7              => M_Cv.Field7
                                     ,P_Field8              => M_Cv.Field8
                                     ,P_Field9              => M_Cv.Field9
                                     ,P_Field10             => M_Cv.Field10
                                     ,P_Prm_Code            => M_Cv.Prm_Code
                                     ,P_Bill_Amt            => NVL(M_Cv.DOC_Amt,M_Cv.Bill_Amt)
                                     ,P_Disc_Amt            => M_Cv.Disc_Amt
                                     ,P_Disc_Amt_Mst        => M_Cv.Disc_Amt_Mst
                                     ,P_Disc_Amt_Dtl        => M_Cv.Disc_Amt_Dtl
                                     ,P_Vat_Amt             => M_Cv.Vat_Amt
                                     ,P_Othr_Amt            => M_Cv.Othr_Amt
                                     ,P_Othr_Amt_Disc       => M_Cv.Othr_Amt_Disc
                                     ,P_Vat_Amt_Othr        => M_Cv.Vat_Amt_Othr
                                     ,P_Disc_Amt_Aftr_Vat   => M_Cv.Disc_Amt_Aftr_Vat
                                     ,P_Disc_Amt_Mst_Vat    => M_Cv.Disc_Amt_Mst_Vat
                                     ,P_Vat_Amt_Disc_Mst    => M_Cv.Vat_Amt_Disc_Mst
                                     ,P_CLC_TAX_FREE_QTY_FLG =>M_Cv.CLC_TAX_FREE_QTY_FLG 
                                     ,P_E_INVC_MTHD_NO       =>M_CV.E_INVC_MTHD_NO
                                    ,P_CRD_DISC_PER               =>M_CV.CRD_DISC_PER                 
                                    ,P_CRD_NO_DISC                =>M_CV.CRD_NO_DISC                  
                                    ,P_CREDIT_CARD                =>M_CV.CREDIT_CARD                  
                                    ,P_CR_CARD_AMT                =>M_CV.CR_CARD_AMT                  
                                    ,P_CR_CARD_AMT_SCND           =>M_CV.CR_CARD_AMT_SCND             
                                    ,P_CR_CARD_AMT_THRD           =>M_CV.CR_CARD_AMT_THRD             
                                    ,P_CR_CARD_COMM_PER           =>M_CV.CR_CARD_COMM_PER             
                                    ,P_CR_CARD_COMM_PER_SCND      =>M_CV.CR_CARD_COMM_PER_SCND        
                                    ,P_CR_CARD_COMM_PER_THRD      =>M_CV.CR_CARD_COMM_PER_THRD        
                                    ,P_CR_CARD_CST_NO             =>M_CV.CR_CARD_CST_NO               
                                    ,P_CR_CARD_CST_NO_SCND        =>M_CV.CR_CARD_CST_NO_SCND          
                                    ,P_CR_CARD_CST_NO_THRD        =>M_CV.CR_CARD_CST_NO_THRD          
                                    ,P_CR_CARD_DOC_NO_REF         =>M_CV.CR_CARD_DOC_NO_REF           
                                    ,P_CR_CARD_DOC_NO_REF_SCND    =>M_CV.CR_CARD_DOC_NO_REF_SCND      
                                    ,P_CR_CARD_DOC_NO_REF_THRD    =>M_CV.CR_CARD_DOC_NO_REF_THRD      
                                    ,P_CR_CARD_DSC                =>M_CV.CR_CARD_DSC                  
                                    ,P_CR_CARD_DSC_SCND           =>M_CV.CR_CARD_DSC_SCND             
                                    ,P_CR_CARD_DSC_THRD           =>M_CV.CR_CARD_DSC_THRD             
                                    ,P_CR_CARD_MAX_COMM_AMT       =>M_CV.CR_CARD_MAX_COMM_AMT         
                                    ,P_CR_CARD_MAX_COMM_AMT_SCND  =>M_CV.CR_CARD_MAX_COMM_AMT_SCND    
                                    ,P_CR_CARD_MAX_COMM_AMT_THRD  =>M_CV.CR_CARD_MAX_COMM_AMT_THRD    
                                    ,P_CR_CARD_NO                 =>M_CV.CR_CARD_NO                   
                                    ,P_CR_CARD_NO_SCND            =>M_CV.CR_CARD_NO_SCND              
                                    ,P_CR_CARD_NO_THRD            =>M_CV.CR_CARD_NO_THRD              
                                    ,P_CR_DOC_NO_REF              =>M_CV.CR_DOC_NO_REF                
                                    ,P_CR_DOC_NO_REF_SCND         =>M_CV.CR_DOC_NO_REF_SCND           
                                    ,P_CR_DOC_NO_REF_THRD         =>M_CV.CR_DOC_NO_REF_THRD           
                                    ,P_CR_VALUED                  =>M_CV.CR_VALUED                    
                                    ,P_CR_VALUED_SCND             =>M_CV.CR_VALUED_SCND               
                                    ,P_CR_VALUED_THRD             =>M_CV.CR_VALUED_THRD               
                                    ,P_CR_VALUE_DATE              =>M_CV.CR_VALUE_DATE                
                                    ,P_CR_VALUE_DATE_SCND         =>M_CV.CR_VALUE_DATE_SCND           
                                    ,P_CR_VALUE_DATE_THRD         =>M_CV.CR_VALUE_DATE_THRD 
                                     ,P_Rtrn_From_Othr_Sman  =>M_CV.Rtrn_From_Othr_Sman
                                     ,P_C_Tax_Code           =>M_CV.C_Tax_Code
                                     ,P_Mobile_No            =>M_CV.Mobile_No
                                     ,P_C_Address            =>M_CV.C_Address
                                     ,P_Cmp_No              => M_Cv.Cmp_No
                                     ,P_Brn_No              => M_Cv.Brn_No
                                     ,P_Brn_Year            => M_Cv.Brn_Year
                                     ,P_Brn_Usr             => M_Cv.Brn_Usr
                                     ,P_Ad_U_Id             => M_Cv.Ad_U_Id
                                     ,P_Ad_Date             => TO_DATE(TO_CHAR(M_CV.AD_DATE),'DD/MM/RRRR HH24:MI:SS')  
                                     ,P_Ad_Trmnl_Nm         => M_Cv.Ad_Trmnl_Nm
                                     ,P_Pst_Typ             => P_Pst_Typ
                                     ,P_CLC_TAX_METHOD      =>P_CLC_TAX_METHOD
                                     ,P_Pst_FROM_BR         =>P_Pst_FROM_BR
                                     ,P_DTS_ONLINE          =>P_DTS_ONLINE
                                     ,P_Lng_No              =>P_Lng_No 
                                     ,P_Msg_Txt             => P_Msg_Txt                                     
                                     ,P_ERR_NO              => P_Err_No
                                     ,P_Pkg_NM              => P_Pkg_Nm);
               If P_Msg_Txt Is Not Null Then              
                  Goto Rtn_Rslt;
               End If;
            Exception
               When Others Then               
                  Raise_Application_Error (-20312, 'Err when insert IAS_RT_BILL_MST DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);           
            End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            -------------------------------------------------------------------------------------------
            For D_Cv In (Select Extractvalue (Value (Xmldtldmy), '*/I_CODE                          ') As I_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/I_QTY                           ') As I_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/P_SIZE                          ') As P_Size
                               ,Extractvalue (Value (Xmldtldmy), '*/ITM_UNT                         ') As Itm_Unt
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE                         ') As I_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE_VAT                     ') As I_Price_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO                         ') As RCRD_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE                    ') As DOC_SEQUENCE
                               ,Extractvalue (Value (Xmldtldmy), '*/W_CODE                          ') As W_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/BILL_NO                         ') As Bill_No
                               ,Extractvalue (Value (Xmldtldmy), '*/BILL_DOC_TYPE                   ') As Bill_Doc_Type
                               ,Extractvalue (Value (Xmldtldmy), '*/BILL_SER                        ') As Bill_Ser
                               ,Extractvalue (Value (Xmldtldmy), '*/CC_CODE                         ') As Cc_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/PJ_NO                           ') As Pj_No
                               ,Extractvalue (Value (Xmldtldmy), '*/ACTV_NO                         ') As Actv_No
                               ,Extractvalue (Value (Xmldtldmy), '*/EXPIRE_DATE                     ') As Expire_Date
                               ,Extractvalue (Value (Xmldtldmy), '*/BATCH_NO                        ') As Batch_No
                               ,Extractvalue (Value (Xmldtldmy), '*/FREE_QTY                        ') As Free_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE_SI                 ') As DOC_SEQUENCE_SI
                               ,Extractvalue (Value (Xmldtldmy), '*/SI_RCRD_NO                     ') As SI_RCRD_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER                         ') As Dis_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER2                        ') As Dis_Per2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER3                        ') As Dis_Per3
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT                         ') As Dis_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST                     ') As Dis_Amt_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL                     ') As Dis_Amt_Dtl
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2                    ') As Dis_Amt_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3                    ') As Dis_Amt_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_PER                         ') As Vat_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT                         ') As Vat_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT                        ') As Othr_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_OTHR                    ') As Vat_Amt_Othr
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT_DISC                   ') As Othr_Amt_Disc
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AFTR_VAT_MST                ') As Dis_Aftr_Vat_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST_VAT                 ') As Dis_Amt_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL_VAT             ') As Vat_Amt_Dis_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_AFTR_DIS                ') As Vat_Amt_Aftr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_BFR_DIS                 ') As Vat_Amt_Bfr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_VAT                 ') As Dis_Amt_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2_VAT                ') As Dis_Amt_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3_VAT                ') As Dis_Amt_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_MST_VAT             ') As Vat_Amt_Dis_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL2_VAT            ') As Vat_Amt_Dis_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL3_VAT            ') As Vat_Amt_Dis_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_AFTR_VAT                ') As Dis_Amt_Aftr_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/LEV_NO                          ') As Lev_No
                               ,Extractvalue (Value (Xmldtldmy), '*/ITEM_DESC                       ') As Item_Desc
                               ,Extractvalue (Value (Xmldtldmy), '*/BARCODE                         ') As Barcode
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL1                      ') As Field_Dtl1
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL2                      ') As Field_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL3                      ') As Field_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/EMP_NO                          ') As Emp_No
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_TYPE_REF                    ') As Doc_Type_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_NO_REF                      ') As Doc_No_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SER_REF                     ') As Doc_Ser_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/SUB_C_CODE                      ') As Sub_C_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO_REF                     ') As Rcrd_No_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_NO                       ') As Qt_Prm_No
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_SER                      ') As Qt_Prm_Ser
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_RCRD_NO                  ') As Qt_Prm_Rcrd_No
                               ,Extractvalue (Value (Xmldtldmy), '*/I_LENGTH                        ') As I_Length
                               ,Extractvalue (Value (Xmldtldmy), '*/I_WIDTH                         ') As I_Width
                               ,Extractvalue (Value (Xmldtldmy), '*/I_HEIGHT                        ') As I_Height
                               ,Extractvalue (Value (Xmldtldmy), '*/I_NUMBER                        ') As I_Number
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_QTY                          ') As Wt_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_UNT                          ') As Wt_Unt
                               ,Extractvalue (Value (Xmldtldmy), '*/MEASUR_PRICE                    ') As Measur_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/ARGMNT_NO                       ') As Argmnt_No
                               ,Extractvalue (Value (Xmldtldmy), '*/SERIALNO_N                      ') As SERIALNO_N                                   
                           From Table (Xmlsequence (Extract (V_Xml_Type, '/RT_BILL/IAS_RT_BILL_DTL'))) Xmldtldmy)
            Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(12)
               ------------------------------------------
               V_DOC_SEQ:=NULL;
               V_Rcrd_No :=null;
               V_Icode  :=Null;
               V_Itm_Unt:=Null;
               V_Barcode:=Null;
               
                Ias_Itm_Pkg.Get_I_Code (P_Barcode => D_Cv.I_Code, P_I_Code => V_Icode, P_Itm_Unt => V_Itm_Unt);
                If V_Icode Is  Null  Or nvl(V_Icode,'0')=Nvl(D_Cv.I_Code,'0') Then                                  
                  V_Icode  := D_Cv.I_Code;
                  V_Itm_Unt:=D_Cv.Itm_Unt;
                  V_Barcode:=D_Cv.Barcode;
                Else
                    V_Barcode:=D_Cv.I_Code;  
                End If;
               Begin
                  Ars_Api_Trns_Pkg.Insrt_Ias_Rt_Bill_Dtl (P_I_Code                 => V_Icode
                                        ,P_I_Qty                  => D_Cv.I_Qty
                                        ,P_P_Size                 => D_Cv.P_Size
                                        ,P_Itm_Unt                => V_Itm_Unt
                                        ,P_I_Price                => D_Cv.I_Price
                                        ,P_I_Price_Vat            => D_Cv.I_Price_Vat
                                        ,P_DOC_SEQUENCE           => V_Doc_Seq
                                        ,P_Rcrd_No                => V_Rcrd_No
                                        ,P_W_Code                 => D_Cv.W_Code
                                        ,P_Bill_No                => case when nvl(D_Cv.Bill_No,0)=0  then null else D_Cv.Bill_No end 
                                        ,P_Bill_Doc_Type          => case when nvl(D_Cv.Bill_Doc_Type,0)=0 then null else D_Cv.Bill_Doc_Type end  
                                        ,P_Bill_Ser               => case when nvl(D_Cv.Bill_Ser,0)=0 then null else D_Cv.Bill_Ser end  
                                        ,P_Cc_Code                => nvl(D_Cv.Cc_Code,Ars_Api_Trns_Pkg.G_Mst_Cc_Code)
                                        ,P_Pj_No                  => nvl(D_Cv.Pj_No,Ars_Api_Trns_Pkg.G_Mst_Pj_No)
                                        ,P_Actv_No                => nvl(D_Cv.Actv_No,Ars_Api_Trns_Pkg.G_Mst_Actv_No)
                                        ,P_Expire_Date            => TO_DATE(D_Cv.Expire_Date,'DD/MM/RRRR')
                                        ,P_Batch_No               => D_Cv.Batch_No
                                        ,P_Free_Qty               => D_Cv.Free_Qty
                                        ,P_DOC_SEQUENCE_SI        => case when nvl(D_Cv.DOC_SEQUENCE_SI,0)=0 then null else D_Cv.DOC_SEQUENCE_SI end  
                                        ,P_SI_RCRD_NO             => case when nvl(D_Cv.SI_RCRD_NO,0)=0 then null else D_Cv.SI_RCRD_NO end  
                                        ,P_Dis_Per                => D_Cv.Dis_Per
                                        ,P_Dis_Per2               => D_Cv.Dis_Per2
                                        ,P_Dis_Per3               => D_Cv.Dis_Per3
                                        ,P_Dis_Amt                => D_Cv.Dis_Amt
                                        ,P_Dis_Amt_Mst            => D_Cv.Dis_Amt_Mst
                                        ,P_Dis_Amt_Dtl            => D_Cv.Dis_Amt_Dtl
                                        ,P_Dis_Amt_Dtl2           => D_Cv.Dis_Amt_Dtl2
                                        ,P_Dis_Amt_Dtl3           => D_Cv.Dis_Amt_Dtl3
                                        ,P_Vat_Per                => D_Cv.Vat_Per
                                        ,P_Vat_Amt                => D_Cv.Vat_Amt
                                        ,P_Othr_Amt               => D_Cv.Othr_Amt
                                        ,P_Vat_Amt_Othr           => D_Cv.Vat_Amt_Othr
                                        ,P_Othr_Amt_Disc          => D_Cv.Othr_Amt_Disc
                                        ,P_Dis_Aftr_Vat_Mst       => D_Cv.Dis_Aftr_Vat_Mst
                                        ,P_Dis_Amt_Mst_Vat        => D_Cv.Dis_Amt_Mst_Vat
                                        ,P_Vat_Amt_Dis_Dtl_Vat    => D_Cv.Vat_Amt_Dis_Dtl_Vat
                                        ,P_Vat_Amt_Aftr_Dis       => D_Cv.Vat_Amt_Aftr_Dis
                                        ,P_Vat_Amt_Bfr_Dis        => D_Cv.Vat_Amt_Bfr_Dis
                                        ,P_Dis_Amt_Dtl_Vat        => D_Cv.Dis_Amt_Dtl_Vat
                                        ,P_Dis_Amt_Dtl2_Vat       => D_Cv.Dis_Amt_Dtl2_Vat
                                        ,P_Dis_Amt_Dtl3_Vat       => D_Cv.Dis_Amt_Dtl3_Vat
                                        ,P_Vat_Amt_Dis_Mst_Vat    => D_Cv.Vat_Amt_Dis_Mst_Vat
                                        ,P_Vat_Amt_Dis_Dtl2_Vat   => D_Cv.Vat_Amt_Dis_Dtl2_Vat
                                        ,P_Vat_Amt_Dis_Dtl3_Vat   => D_Cv.Vat_Amt_Dis_Dtl3_Vat
                                        ,P_Dis_Amt_Aftr_Vat       => D_Cv.Dis_Amt_Aftr_Vat
                                        ,P_Lev_No                 => D_Cv.Lev_No
                                        ,P_Item_Desc              => D_Cv.Item_Desc
                                        ,P_Barcode                => V_Barcode
                                        ,P_Field_Dtl1             => D_Cv.Field_Dtl1
                                        ,P_Field_Dtl2             => D_Cv.Field_Dtl2
                                        ,P_Field_Dtl3             => D_Cv.Field_Dtl3
                                        ,P_Emp_No                 => D_Cv.Emp_No
                                        ,P_Doc_Type_Ref           => case when nvl(D_Cv.Doc_Type_Ref,0)=0 then null else D_Cv.Doc_Type_Ref end
                                        ,P_Doc_Ser_Ref            => case when nvl(D_Cv.Doc_Ser_Ref,0)=0 then null else D_Cv.Doc_Ser_Ref end
                                        ,P_Doc_No_Ref             => case when nvl(D_Cv.Doc_No_Ref,0)=0 then null else D_Cv.Doc_No_Ref end  
                                        ,P_Rcrd_No_Ref            => case when nvl(D_Cv.Rcrd_No_Ref,0)=0 then null else D_Cv.Rcrd_No_Ref end
                                        ,P_Sub_C_Code             => D_Cv.Sub_C_Code                                        
                                        ,P_QT_PRM_NO              => Case When nvl(D_cv.QT_PRM_NO,0)=0 Then Null Else D_cv.QT_PRM_NO end 
                                        ,P_QT_PRM_RCRD_NO         =>Case When nvl(D_Cv.QT_PRM_RCRD_NO,0)=0 Then Null Else D_Cv.QT_PRM_RCRD_NO end 
                                        ,P_QT_PRM_SER             =>Case When nvl(D_Cv.QT_PRM_SER,0)=0 Then Null Else D_Cv.QT_PRM_SER end
                                        ,P_I_Length               => D_Cv.I_Length
                                        ,P_I_Width                => D_Cv.I_Width
                                        ,P_I_Height               => D_Cv.I_Height
                                        ,P_I_Number               => D_Cv.I_Number
                                        ,P_Wt_Qty                 => D_Cv.Wt_Qty
                                        ,P_Wt_Unt                 => D_Cv.Wt_Unt
                                        ,P_Argmnt_No              => D_Cv.Argmnt_No
                                        ,P_SERIALNO_N             => D_Cv.SERIALNO_N
                                        ,P_Msg_Txt                => P_Msg_Txt
                                        ,P_ERR_NO               => P_Err_No
                                        ,P_Pkg_NM                 => P_Pkg_Nm);

                  If P_Msg_Txt Is Not Null Then                 
                     Goto Rtn_Rslt;
                  End If;
               Exception
                  When Others Then                 
                     Raise_Application_Error (-20313, 'Err when insert IAS_RT_BILL_DTL DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);
               End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --(2)
            --##------------------------------------------------------------------------------------------------------------------------------##--
            For Tax_Mvmnt_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As Bill_Doc_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As Doc_Jv_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As Tax_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As Clc_Typ_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As Agncy_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                      ') As I_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                     ') As Itm_Unt
                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                      ') As P_Size
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_PRICE                     ') As I_Price
                                      ,Extractvalue( Value( Xmldtldmy), '*/DISC_AMT                    ') As Disc_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                    ') As A_Cy
                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As Ac_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As Tax_Prcnt
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As Tax_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                      ') As W_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As Cc_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As Pj_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As Actv_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As Rcrd_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As Doc_Sequence
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As Tax_Amt_L
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_QTY                       ') As I_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/FREE_QTY                    ') As Free_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As Ref_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_COST                    ') As Stk_Cost
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_RATE                    ') As Stk_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TAX_FREE_QTY_FLG        ') As Clc_Tax_Free_Qty_Flg
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/RT_BILL/GNR_TAX_ITM_MOVMNT'))) Xmldtldmy                                  
                                   )                              
               Loop
                   IF NVL(Tax_Mvmnt_Cv.I_CODE,'0')=NVL(D_CV.I_CODE,'0')  AND NVL(Tax_Mvmnt_Cv.ITM_UNT,'0')=NVL(D_CV.ITM_UNT,'0')
                     AND NVL(Tax_Mvmnt_Cv.RCRD_NO,0)=NVL(D_CV.RCRD_NO,0) THEN    
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Gnr_Tax_Itm_Movmnt(P_Doc_Typ                => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Bill_Doc_Type          => Ars_Api_Trns_Pkg.G_RT_Bill_Doc_Type
                                                     ,P_Doc_Jv_Type            => Ars_Api_Trns_Pkg.G_SR_TYPE
                                                     ,P_Tax_No                 => Tax_Mvmnt_Cv.Tax_No
                                                     ,P_Clc_Typ_No             => Tax_Mvmnt_Cv.Clc_Typ_No
                                                     ,P_Agncy_No               => Tax_Mvmnt_Cv.Agncy_No
                                                     ,P_I_Code                 => V_Icode
                                                     ,P_Itm_Unt                => V_Itm_Unt
                                                     ,P_P_Size                 => Tax_Mvmnt_Cv.P_Size
                                                     ,P_I_Price                => Tax_Mvmnt_Cv.I_Price
                                                     ,P_Disc_Amt               => Tax_Mvmnt_Cv.Disc_Amt
                                                     ,P_A_Code                 => Tax_Mvmnt_Cv.A_Code
                                                     ,P_Cur_Code               => Tax_Mvmnt_Cv.A_Cy
                                                     ,P_Ac_Rate                => Tax_Mvmnt_Cv.Ac_Rate
                                                     ,P_Tax_Prcnt              => Tax_Mvmnt_Cv.Tax_Prcnt
                                                     ,P_Tax_Amt                => Tax_Mvmnt_Cv.Tax_Amt
                                                     ,P_W_Code                 => Ars_Api_Trns_Pkg.G_W_Code
                                                     ,P_Cc_Code                => Ars_Api_Trns_Pkg.G_Dtl_Cc_Code
                                                     ,P_Pj_No                  => Ars_Api_Trns_Pkg.G_Dtl_Pj_No
                                                     ,P_Actv_No                => Ars_Api_Trns_Pkg.G_Dtl_Actv_No                                                      
                                                     ,P_Doc_Sequence           => V_Doc_Seq
                                                     ,P_Rcrd_No                => V_Rcrd_No
                                                     ,P_Tax_Amt_L              => Tax_Mvmnt_Cv.Tax_Amt_L
                                                     ,P_I_Qty                  => Tax_Mvmnt_Cv.I_Qty
                                                     ,P_Free_Qty               => Tax_Mvmnt_Cv.Free_Qty
                                                     ,P_Ref_No                 => Tax_Mvmnt_Cv.Ref_No
                                                     ,P_Stk_Cost               => Tax_Mvmnt_Cv.Stk_Cost
                                                     ,P_Stk_Rate               => Tax_Mvmnt_Cv.Stk_Rate
                                                     ,P_Clc_Tax_Free_Qty_Flg   => M_CV.Clc_Tax_Free_Qty_Flg
                                                     ,P_Msg_Txt                => P_Msg_Txt
                                                     ,P_ERR_NO               => P_Err_No
                                                     ,P_Pkg_Nm                 => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then                    
                        Raise_Application_Error( -20314, 'ERR WHEN INSERT INSRT_GNR_TAX_ITM_MOVMNT DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                    End;
                 END IF; 
               End Loop;            
            --##---------------------------------------------------------------------------------------------------------------------------##--
            End Loop;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            --(12)
            -----------------------------------------------------------------------------------------------------------------------------
            --##---------------------------------------------------------------------------------------------------------------------------##--
            --##INSERT OTHER CHARGE
                         For Othr_Chrg_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                        ') As Sc_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                       ') As A_Code
                                          ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                     ') As A_Cy
                                          ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                      ') As Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/PER                          ') As Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/AMT                          ') As Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/INV_ITEM                     ') As Inv_Item
                                          ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                      ') As Rcrd_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                      ') As Bill_Py
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_AMT                      ') As Vat_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_PER                      ') As Vat_Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AMT                       ') As Sc_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AC_RATE                   ') As Sc_Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_A_CY                      ') As Sc_A_Cy
                                      From Table( Xmlsequence( Extract( V_Xml_Type, '/RT_BILL/OTHER_CHARGES'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Other_Charges(P_Doc_Typ      => Ars_Api_Trns_Pkg.G_Doc_Typ
                                        ,P_Bill_Doc_Type   =>Ars_Api_Trns_Pkg.G_RT_Bill_Doc_Type
                                        ,P_BILL_TYPE      =>3
                                        ,P_Sc_No        => Othr_Chrg_Cv.Sc_No
                                        ,P_A_Code       => Othr_Chrg_Cv.A_Code
                                        ,P_Cur_Code     => Othr_Chrg_Cv.A_Cy
                                        ,P_Ac_Rate      => Othr_Chrg_Cv.Ac_Rate
                                        ,P_Per          => Othr_Chrg_Cv.Per
                                        ,P_Amt          => Othr_Chrg_Cv.Amt
                                        ,P_Inv_Item     => Othr_Chrg_Cv.Inv_Item
                                        ,P_Rcrd_No      => Othr_Chrg_Cv.Rcrd_No
                                        ,P_Bill_Py      => Othr_Chrg_Cv.Bill_Py
                                        ,P_Vat_Amt      => Othr_Chrg_Cv.Vat_Amt
                                        ,P_Vat_Per      => Othr_Chrg_Cv.Vat_Per
                                        ,P_Sc_Amt       => Othr_Chrg_Cv.Sc_Amt
                                        ,P_Sc_Ac_Rate   => Othr_Chrg_Cv.Sc_Ac_Rate
                                        ,P_Sc_A_Cy      => Othr_Chrg_Cv.Sc_A_Cy
                                        ,P_Msg_Txt      => P_Msg_Txt
                                        ,P_ERR_NO     => P_Err_No
                                        ,P_Pkg_Nm       => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                      --  ---Rollback;
                        Raise_Application_Error( -20315, 'ERR WHEN INSERT OTHER_CHARGES DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
         --##INSERT OTHER CHARGE ITEMS
               For Othr_Chrg_Itm_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                    ') As Doc_Typ
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                      ') As Sc_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                     ') As A_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                   ') As A_Cy
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                    ') As Ac_Rate
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PER                        ') As Per
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AMT                        ') As Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                     ') As W_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                    ') As Cc_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                      ') As Pj_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                    ') As Actv_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                    ') As Rcrd_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SI_TYPE                    ') As Si_Type
                                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                     ') As I_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                    ') As Itm_Unt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                     ') As P_Size
                                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                    ') As Bill_Py
                                                      ,Extractvalue( Value( Xmldtldmy), '*/UNIT_AMT                   ') As Unit_Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/POST_CODE                  ') As Post_Code
                                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/RT_BILL/OTHER_CHARGES_ITEMS'))) Xmldtldmy)
                       Loop
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Other_Charges_Items(P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                      ,P_Sc_No       => Othr_Chrg_Itm_Cv.Sc_No
                                                      ,P_A_Code      => Othr_Chrg_Itm_Cv.A_Code
                                                      ,P_Cur_Code    => Othr_Chrg_Itm_Cv.A_Cy
                                                      ,P_Ac_Rate     => Othr_Chrg_Itm_Cv.Ac_Rate
                                                      ,P_Per         => Othr_Chrg_Itm_Cv.Per
                                                      ,P_Amt         => Othr_Chrg_Itm_Cv.Amt
                                                      ,P_W_Code      => Othr_Chrg_Itm_Cv.W_Code
                                                      ,P_Cc_Code     => Ars_Api_Trns_Pkg.G_Dtl_Cc_Code
                                                      ,P_Pj_No       => Ars_Api_Trns_Pkg.G_Dtl_Pj_No
                                                      ,P_Actv_No     => Ars_Api_Trns_Pkg.G_Dtl_Actv_No   
                                                      ,P_Rcrd_No     => Othr_Chrg_Itm_Cv.Rcrd_No
                                                      ,P_Si_Type     => Othr_Chrg_Itm_Cv.Si_Type
                                                      ,P_I_Code      => Othr_Chrg_Itm_Cv.I_Code
                                                      ,P_Itm_Unt     => Othr_Chrg_Itm_Cv.Itm_Unt
                                                      ,P_P_Size      => Othr_Chrg_Itm_Cv.P_Size
                                                      ,P_Bill_Py     => Othr_Chrg_Itm_Cv.Bill_Py
                                                      ,P_Unit_Amt    => Othr_Chrg_Itm_Cv.Unit_Amt
                                                      ,P_Post_Code   => Othr_Chrg_Itm_Cv.Post_Code
                                                      ,P_Msg_Txt     => P_Msg_Txt
                                                      ,P_ERR_NO    => P_Err_No
                                                      ,P_Pkg_Nm      => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                          Exception
                             When Others Then
                                ---Rollback;
                                Raise_Application_Error( -20316, 'ERR WHEN INSERT OTHER_CHARGES_ITEMS DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                          End;
                       End Loop; 
         --##---------------------------------------------------------------------------------------------------------------------------##--
                  For Tax_INPT_Mvmnt_Cv In (SELECT    Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As DOC_TYP              
                                            ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As BILL_DOC_TYPE         
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As DOC_JV_TYPE                                                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As TAX_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As CLC_TYP_NO           
                                            ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As AGNCY_NO                                        
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_CODE                   ') As INPT_CODE            
                                            ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_CODE               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                     ') As CUR_CODE                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As AC_RATE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_AMT                    ') As INPT_AMT             
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As TAX_PRCNT            
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As TAX_AMT              
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As TAX_AMT_L            
                                            ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As CC_CODE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As PJ_NO                
                                            ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As ACTV_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As REF_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As RCRD_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As DOC_SEQUENCE
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/RT_BILL/GNR_TAX_INPT_MOVMNT'))) Xmldtldmy                                  
                                   )                              
               Loop                    
                    Begin
                          Ars_Api_Trns_Pkg.INSRT_GNR_TAX_INPT_MOVMNT(
                                            P_DOC_TYP                    =>Ars_Api_Trns_Pkg.G_DOC_TYP
                                           ,P_BILL_DOC_TYPE              =>Ars_Api_Trns_Pkg.G_RT_BILL_DOC_TYPE
                                           ,P_DOC_JV_TYPE                =>Ars_Api_Trns_Pkg.G_SR_TYPE                                      
                                           ,P_TAX_NO                     =>Tax_INPT_Mvmnt_Cv.TAX_NO
                                          , P_CLC_TYP_NO                 =>Tax_INPT_Mvmnt_Cv.CLC_TYP_NO 
                                          , P_AGNCY_NO                   =>Tax_INPT_Mvmnt_Cv.AGNCY_NO                            
                                          , P_INPT_CODE                  =>Tax_INPT_Mvmnt_Cv.INPT_CODE 
                                           ,P_A_CODE                     =>Tax_INPT_Mvmnt_Cv.A_CODE 
                                          , P_A_CY                       =>Tax_INPT_Mvmnt_Cv.CUR_CODE
                                          , P_AC_RATE                    =>Tax_INPT_Mvmnt_Cv.AC_RATE 
                                          , P_INPT_AMT                   =>Tax_INPT_Mvmnt_Cv.INPT_AMT 
                                          , P_TAX_PRCNT                  =>Tax_INPT_Mvmnt_Cv.TAX_PRCNT 
                                          , P_TAX_AMT                    =>Tax_INPT_Mvmnt_Cv.TAX_AMT
                                          , P_TAX_AMT_L                  =>Tax_INPT_Mvmnt_Cv.TAX_AMT_L 
                                          , P_Cc_Code                    =>Ars_Api_Trns_Pkg.G_Mst_Cc_Code
                                          , P_Pj_No                      =>Ars_Api_Trns_Pkg.G_Mst_Pj_No
                                          , P_Actv_No                    =>Ars_Api_Trns_Pkg.G_Mst_Actv_No  
                                          , P_REF_NO                     =>Tax_INPT_Mvmnt_Cv.REF_NO 
                                          , P_RCRD_NO                    =>Tax_INPT_Mvmnt_Cv.RCRD_NO 
                                          , P_DOC_SEQUENCE               =>Tax_INPT_Mvmnt_Cv.DOC_SEQUENCE
                                          ,P_Msg_Txt                     =>P_Msg_Txt
                                          ,P_ERR_NO                     =>P_ERR_NO
                                          ,P_Pkg_NM                     =>P_Pkg_NM); 

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then
                       -- ---Rollback;
                        Raise_Application_Error( -20547, 'ERR WHEN INSERT INSRT_GNR_TAX_INPT_MOVMNT DOC_NO= ' || V_DOC_NO || ' ' || Chr( 10) || Sqlerrm);
                    End;                 
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
            For Attach_Cv
                  In (Select Extractvalue (Value (Xmldtldmy), '*/FILE_NAME         ') As File_Name
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/RT_BILL/ATTACH'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Archives (P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Doc_Ser     => Ars_Api_Trns_Pkg.G_Doc_Ser
                                                     ,P_File_Name   => Attach_Cv.File_Name
                                                     ,P_Msg_Txt     => P_Msg_Txt
                                                     ,P_Err_No      => P_Err_No
                                                     ,P_Pkg_Nm      => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                        Raise_Application_Error (-20719,'Err.in Ars_Api_Trns_Pkg.INSRT_ARCHIVES= '|| V_Doc_No|| ' '|| Chr (10)|| Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
            --## CHK INSERT DATA
            Ars_Api_Trns_Pkg.Chk_Insrt_Data (P_Doc_Typ    => 5
                           ,P_Doc_Ser    => Ars_Api_Trns_Pkg.G_Doc_Ser
                           ,P_Msg_Txt    => P_Msg_Txt
                           ,P_ERR_NO   => P_Err_No
                           ,P_Pkg_NM   => P_Pkg_Nm);

            If P_Msg_Txt Is Not Null Then             
               ---Rollback;
               Goto Rtn_Rslt;
            End If;            
            -------------------------------------------- 
            --## POST INTO ONYX IF SYSTEM IS DISTRBUTED AND ONLINE
                IF NVL(Ars_Api_Trns_Pkg.G_SYS_NO,0)=70 AND NVL(P_DTS_ONLINE,0)=1 THEN
                 Ars_Api_Trns_Pkg.Post_From_Br_Prc (P_Sys_No    =>Ars_Api_Trns_Pkg.G_SYS_NO
                                  ,P_Doc_Typ    =>5
                                  ,P_Doc_Ser    =>Ars_Api_Trns_Pkg.G_Doc_Ser
                                  ,P_Lng_No     =>Ars_Api_Trns_Pkg.G_LNG_NO                             
                                  ,P_Msg_Txt    =>P_Msg_Txt
                                  ,P_ERR_NO     =>P_ERR_NO
                                  ,P_Pkg_Nm     =>P_Pkg_Nm) ; 
                    If P_Msg_Txt Is Not Null Then                                    
                      Goto Rtn_Rslt;
                    End If;
                END IF;                                
         ----------------------------------------------------------------------------------------------------------
         End Loop; 
      Elsif P_Doc_Typ = 136 Then                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         -- RT BILL SALES
         For M_Cv In (Select Extractvalue (Value (Xmlmstdmy), '*/SYS_NO                          ') As Sys_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_TYPE                        ') As Doc_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_NO                          ') As Doc_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER                         ') As Doc_Ser
                            ,Extractvalue (Value (Xmlmstdmy), '*/RT_BILL_DOC_TYPE                ') As Rt_Bill_Doc_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DATE                        ') As Doc_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/CUR_CODE                        ') As Cur_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/CUR_RATE                        ') As Cur_Rate
                            ,Extractvalue (Value (Xmlmstdmy), '*/STOCK_RATE                      ') As Stock_Rate
                            ,Extractvalue (Value (Xmlmstdmy), '*/P_YEAR                          ') As P_Year
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE                          ') As C_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_NAME                          ') As C_Name
                            ,Extractvalue (Value (Xmlmstdmy), '*/A_CODE                          ') As A_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_NO_MNL                     ') As BILL_NO_MNL
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_NO                       ') As Cheque_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_AMT                      ') As Cheque_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_DUE_DATE                 ') As Cheque_Due_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/RT_BILL_DUE_DATE                ') As Rt_Bill_Due_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/W_CODE                          ') As W_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/R_CODE                          ') As R_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/CASH_NO                         ') As Cash_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CC_CODE                         ') As Cc_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/PJ_NO                           ') As Pj_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/ACTV_NO                         ') As Actv_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CASH_AC_FCC                     ') As Cash_Ac_Fcc
                            ,Extractvalue (Value (Xmlmstdmy), '*/BANK_NO                         ') As Bank_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TYP_NO_TAX                  ') As Clc_Typ_No_Tax
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_CODE                         ') As Ac_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_CODE_DTL                     ') As Ac_Code_Dtl
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_DTL_TYP                      ') As Ac_Dtl_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/REP_CODE                        ') As Rep_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/EMP_NO                          ') As Emp_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/SR_TYPE                         ') As Sr_Type
                            ,Extractvalue (Value (Xmlmstdmy), '*/REF_NO                          ') As Ref_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/A_DESC                          ') As A_Desc
                            ,Extractvalue (Value (Xmlmstdmy), '*/RETURN_RES                      ') As Return_Res
                            ,Extractvalue (Value (Xmlmstdmy), '*/PREV_YEAR                       ') As Prev_Year
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLASSIFY_NO                     ') As Classify_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLASSIFY_SER                    ') As Classify_Ser
                            ,Extractvalue (Value (Xmlmstdmy), '*/W_CODE_BILL                     ') As W_Code_Bill
                            ,Extractvalue (Value (Xmlmstdmy), '*/CC_CODE_BILL                    ') As Cc_Code_Bill
                            ,Extractvalue (Value (Xmlmstdmy), '*/REP_CODE_BILL                   ') As Rep_Code_Bill
                            ,Extractvalue (Value (Xmlmstdmy), '*/STAND_BY                        ') As Stand_By
                            ,Extractvalue (Value (Xmlmstdmy), '*/NOTE_NO                         ') As Note_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DRIVER_NO                       ') As Driver_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_BRN_NO                      ') As Doc_Brn_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/RES_TYP                         ') As Res_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/WITHOUT_VAT                     ') As Without_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/RT_VAT_PRD_TYP                  ') As Rt_Vat_Prd_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE_CSH                      ') As C_Code_Csh
                            ,Extractvalue (Value (Xmlmstdmy), '*/C_TEL                           ') As C_Tel
                            ,Extractvalue (Value (Xmlmstdmy), '*/PYMNT_AC                        ') As Pymnt_Ac
                            ,Extractvalue (Value (Xmlmstdmy), '*/AC_AMT                          ') As Ac_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER_EXTRNL                  ') As Doc_Ser_Extrnl
                            ,Extractvalue (Value (Xmlmstdmy), '*/CNCL_FLG                        ') As Cncl_Flg
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_VAT_PRICE_TYP               ') As Clc_Vat_Price_Typ
                            ,Extractvalue (Value (Xmlmstdmy), '*/COL_NO                          ') As Col_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD1                          ') As Field1
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD2                          ') As Field2
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD3                          ') As Field3
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD4                          ') As Field4
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD5                          ') As Field5
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD6                          ') As Field6
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD7                          ') As Field7
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD8                          ') As Field8
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD9                          ') As Field9
                            ,Extractvalue (Value (Xmlmstdmy), '*/FIELD10                         ') As Field10
                            ,Extractvalue (Value (Xmlmstdmy), '*/PRM_CODE                        ') As Prm_Code
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_AMT                        ') As Bill_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT                        ') As Disc_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST                    ') As Disc_Amt_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_DTL                    ') As Disc_Amt_Dtl
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT                         ') As Vat_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT                        ') As Othr_Amt
                            ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT_DISC                   ') As Othr_Amt_Disc
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_OTHR                    ') As Vat_Amt_Othr
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_AFTR_VAT               ') As Disc_Amt_Aftr_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST_VAT                ') As Disc_Amt_Mst_Vat
                            ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_DISC_MST                ') As Vat_Amt_Disc_Mst
                            ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TAX_FREE_QTY_FLG           ') As CLC_TAX_FREE_QTY_FLG
                            ,Extractvalue (Value (Xmlmstdmy), '*/E_INVC_MTHD_NO                 ') As E_INVC_MTHD_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/BILL_DOC_TYPE                  ') As BILL_DOC_TYPE
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DUE_DATE                   ') As DOC_DUE_DATE
                            ,Extractvalue (Value (Xmlmstdmy), '*/TYP_NO                         ') As TYP_NO
                            ,Extractvalue (Value (Xmlmstdmy), '*/DOC_AMT                        ') As DOC_AMT
                            ,Extractvalue (Value (Xmlmstdmy), '*/RTRN_FROM_OTHR_SMAN             ') As RTRN_FROM_OTHR_SMAN
                            ,Extractvalue (Value (Xmlmstdmy), '*/CMP_NO                          ') As Cmp_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_NO                          ') As Brn_No
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_YEAR                        ') As Brn_Year
                            ,Extractvalue (Value (Xmlmstdmy), '*/BRN_USR                         ') As Brn_Usr
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_U_ID                         ') As Ad_U_Id
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_DATE                         ') As Ad_Date
                            ,Extractvalue (Value (Xmlmstdmy), '*/AD_TRMNL_NM                     ') As Ad_Trmnl_Nm
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/RT_BILL/IAS_RT_BILL_MST'))) Xmlmstdmy)
         Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    --(11)
            --------------------------------------------------------------------------------           
            V_Doc_No := M_Cv.Doc_No;            
            V_Doc_Typ := P_Doc_Typ;
            ---------------------------------------------------------------------------------
            Chk_Prmtr (   P_Sys_No            =>M_Cv.Sys_No
                          ,P_Doc_Typ          =>P_Doc_Typ                           
                          ,P_COMMIT_FLG       =>P_COMMIT_FLG
                          ,P_CLC_TAX_METHOD   =>P_CLC_TAX_METHOD                                                      
                          ,P_Pst_Typ          =>P_Pst_Typ
                          ,P_Pst_FROM_BR      =>P_Pst_FROM_BR
                          ,P_DTS_ONLINE       =>P_DTS_ONLINE
                          ,P_Lng_No           =>P_Lng_No                          
                          ,P_Msg_Txt          =>P_Msg_Txt
                          ,P_ERR_NO           =>P_ERR_NO
                          ,P_Pkg_Nm           =>P_Pkg_Nm);
                          If  P_Msg_Txt Is Not Null Then
                              Goto Rtn_Rslt;
                          End If;
          --------------------------------------------------------------------------------- 
            Begin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(1)
               Ars_Api_Trns_Pkg.Insrt_Ias_Rt_Bill_Mst_RQ (P_Sys_No              => M_Cv.Sys_No
                                     ,P_Doc_Type            => M_Cv.Doc_Type
                                     ,P_Doc_No              => M_Cv.Doc_No
                                     ,P_Doc_Ser             => NULL
                                     ,P_Rt_Bill_Doc_Type    =>NVL(M_Cv.Bill_Doc_Type,M_Cv.Rt_Bill_Doc_Type)
                                     ,P_Doc_Date            => TO_DATE(M_Cv.Doc_Date,'DD/MM/RRRR')
                                     ,P_Cur_Code            => M_Cv.Cur_Code
                                     ,P_Cur_Rate            => M_Cv.Cur_Rate
                                     ,P_Stock_Rate          => M_Cv.Stock_Rate
                                     ,P_P_Year              => M_Cv.P_Year
                                     ,P_C_Code              => M_Cv.C_Code
                                     ,P_C_Name              => M_Cv.C_Name
                                     ,P_A_Code              => M_Cv.A_Code
                                     ,P_BILL_NO_MNL          =>M_Cv.BILL_NO_MNL
                                     ,P_Cheque_No           => M_Cv.Cheque_No
                                     ,P_Cheque_Amt          => M_Cv.Cheque_Amt
                                     ,P_Cheque_Due_Date     => TO_DATE(M_Cv.Cheque_Due_Date,'DD/MM/RRRR')
                                     ,P_Rt_Bill_Due_Date    => NVL(TO_DATE(M_Cv.DOC_Due_Date,'DD/MM/RRRR'),TO_DATE(M_Cv.Rt_Bill_Due_Date,'DD/MM/RRRR'))
                                     ,P_W_Code              => M_Cv.W_Code
                                     ,P_R_Code              => M_Cv.R_Code
                                     ,P_Cash_No             => M_Cv.Cash_No
                                     ,P_Cc_Code             => M_Cv.Cc_Code
                                     ,P_Pj_No               => M_Cv.Pj_No
                                     ,P_Actv_No             => M_Cv.Actv_No
                                     ,P_Cash_Ac_Fcc         => M_Cv.Cash_Ac_Fcc
                                     ,P_Bank_No             => M_Cv.Bank_No
                                     ,P_Clc_Typ_No_Tax      => M_Cv.Clc_Typ_No_Tax
                                     ,P_Ac_Code             => M_Cv.Ac_Code
                                     ,P_Ac_Code_Dtl         => M_Cv.Ac_Code_Dtl
                                     ,P_Ac_Dtl_Typ          => M_Cv.Ac_Dtl_Typ
                                     ,P_Rep_Code            => M_Cv.Rep_Code
                                     ,P_Emp_No              => M_Cv.Emp_No
                                     ,P_Sr_Type             => NVL(M_Cv.TYP_NO,M_Cv.Sr_Type)
                                     ,P_Ref_No              => M_Cv.Ref_No
                                     ,P_A_Desc              => M_Cv.A_Desc
                                     ,P_Return_Res          => M_Cv.Return_Res
                                     ,P_Prev_Year           => M_Cv.Prev_Year
                                     ,P_Classify_No         => M_Cv.Classify_No
                                     ,P_Classify_Ser        => M_Cv.Classify_Ser
                                     ,P_W_Code_Bill         => M_Cv.W_Code_Bill
                                     ,P_Cc_Code_Bill        => M_Cv.Cc_Code_Bill
                                     ,P_Rep_Code_Bill       => M_Cv.Rep_Code_Bill
                                     ,P_Stand_By            => M_Cv.Stand_By
                                     ,P_Note_No             => M_Cv.Note_No
                                     ,P_Driver_No           => M_Cv.Driver_No
                                     ,P_Doc_Brn_No          => M_Cv.Doc_Brn_No
                                     ,P_Res_Typ             => M_Cv.Res_Typ
                                     ,P_Without_Vat         => M_Cv.Without_Vat
                                     ,P_Rt_Vat_Prd_Typ      => M_Cv.Rt_Vat_Prd_Typ
                                     ,P_C_Code_Csh          => M_Cv.C_Code_Csh
                                     ,P_C_Tel               => M_Cv.C_Tel
                                     ,P_Pymnt_Ac            => M_Cv.Pymnt_Ac
                                     ,P_Ac_Amt              => M_Cv.Ac_Amt
                                     ,P_Doc_Ser_Extrnl      => M_Cv.Doc_Ser_Extrnl
                                     ,P_Cncl_Flg            => M_Cv.Cncl_Flg
                                     ,P_Clc_Vat_Price_Typ   => M_Cv.Clc_Vat_Price_Typ
                                     ,P_Col_No              => M_Cv.Col_No
                                     ,P_Field1              => M_Cv.Field1
                                     ,P_Field2              => M_Cv.Field2
                                     ,P_Field3              => M_Cv.Field3
                                     ,P_Field4              => M_Cv.Field4
                                     ,P_Field5              => M_Cv.Field5
                                     ,P_Field6              => M_Cv.Field6
                                     ,P_Field7              => M_Cv.Field7
                                     ,P_Field8              => M_Cv.Field8
                                     ,P_Field9              => M_Cv.Field9
                                     ,P_Field10             => M_Cv.Field10
                                     ,P_Prm_Code            => M_Cv.Prm_Code
                                     ,P_Bill_Amt            => NVL(M_Cv.DOC_Amt,M_Cv.Bill_Amt)
                                     ,P_Disc_Amt            => M_Cv.Disc_Amt
                                     ,P_Disc_Amt_Mst        => M_Cv.Disc_Amt_Mst
                                     ,P_Disc_Amt_Dtl        => M_Cv.Disc_Amt_Dtl
                                     ,P_Vat_Amt             => M_Cv.Vat_Amt
                                     ,P_Othr_Amt            => M_Cv.Othr_Amt
                                     ,P_Othr_Amt_Disc       => M_Cv.Othr_Amt_Disc
                                     ,P_Vat_Amt_Othr        => M_Cv.Vat_Amt_Othr
                                     ,P_Disc_Amt_Aftr_Vat   => M_Cv.Disc_Amt_Aftr_Vat
                                     ,P_Disc_Amt_Mst_Vat    => M_Cv.Disc_Amt_Mst_Vat
                                     ,P_Vat_Amt_Disc_Mst    => M_Cv.Vat_Amt_Disc_Mst
                                     ,P_CLC_TAX_FREE_QTY_FLG =>M_Cv.CLC_TAX_FREE_QTY_FLG 
                                     ,P_E_INVC_MTHD_NO       =>M_CV.E_INVC_MTHD_NO
                                     ,P_Rtrn_From_Othr_Sman  =>M_CV.Rtrn_From_Othr_Sman
                                     ,P_Cmp_No              => M_Cv.Cmp_No
                                     ,P_Brn_No              => M_Cv.Brn_No
                                     ,P_Brn_Year            => M_Cv.Brn_Year
                                     ,P_Brn_Usr             => M_Cv.Brn_Usr
                                     ,P_Ad_U_Id             => M_Cv.Ad_U_Id
                                     ,P_Ad_Date             => TO_DATE(TO_CHAR(M_CV.AD_DATE),'DD/MM/RRRR HH24:MI:SS')  
                                     ,P_Ad_Trmnl_Nm         => M_Cv.Ad_Trmnl_Nm
                                     ,P_Pst_Typ             => P_Pst_Typ
                                     ,P_CLC_TAX_METHOD      =>P_CLC_TAX_METHOD
                                     ,P_Pst_FROM_BR         =>P_Pst_FROM_BR
                                     ,P_DTS_ONLINE          =>P_DTS_ONLINE
                                     ,P_Lng_No              =>P_Lng_No 
                                     ,P_Msg_Txt             => P_Msg_Txt                                     
                                     ,P_ERR_NO            => P_Err_No
                                     ,P_Pkg_NM              => P_Pkg_Nm);
               If P_Msg_Txt Is Not Null Then              
                  Goto Rtn_Rslt;
               End If;
            Exception
               When Others Then               
                  Raise_Application_Error (-20555, 'Err when insert IAS_RT_BILL_MST_RQ DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);           
            End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            -------------------------------------------------------------------------------------------
            For D_Cv In (Select Extractvalue (Value (Xmldtldmy), '*/I_CODE                          ') As I_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/I_QTY                           ') As I_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/P_SIZE                          ') As P_Size
                               ,Extractvalue (Value (Xmldtldmy), '*/ITM_UNT                         ') As Itm_Unt
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE                         ') As I_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE_VAT                     ') As I_Price_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO                         ') As RCRD_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE                    ') As DOC_SEQUENCE
                               ,Extractvalue (Value (Xmldtldmy), '*/W_CODE                          ') As W_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/BILL_NO                         ') As Bill_No
                               ,Extractvalue (Value (Xmldtldmy), '*/BILL_DOC_TYPE                   ') As Bill_Doc_Type
                               ,Extractvalue (Value (Xmldtldmy), '*/BILL_SER                        ') As Bill_Ser
                               ,Extractvalue (Value (Xmldtldmy), '*/CC_CODE                         ') As Cc_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/PJ_NO                           ') As Pj_No
                               ,Extractvalue (Value (Xmldtldmy), '*/ACTV_NO                         ') As Actv_No
                               ,Extractvalue (Value (Xmldtldmy), '*/EXPIRE_DATE                     ') As Expire_Date
                               ,Extractvalue (Value (Xmldtldmy), '*/BATCH_NO                        ') As Batch_No
                               ,Extractvalue (Value (Xmldtldmy), '*/FREE_QTY                        ') As Free_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE_SI                 ') As DOC_SEQUENCE_SI
                               ,Extractvalue (Value (Xmldtldmy), '*/SI_RCRD_NO                     ') As SI_RCRD_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER                         ') As Dis_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER2                        ') As Dis_Per2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER3                        ') As Dis_Per3
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT                         ') As Dis_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST                     ') As Dis_Amt_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL                     ') As Dis_Amt_Dtl
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2                    ') As Dis_Amt_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3                    ') As Dis_Amt_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_PER                         ') As Vat_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT                         ') As Vat_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT                        ') As Othr_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_OTHR                    ') As Vat_Amt_Othr
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT_DISC                   ') As Othr_Amt_Disc
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AFTR_VAT_MST                ') As Dis_Aftr_Vat_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST_VAT                 ') As Dis_Amt_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL_VAT             ') As Vat_Amt_Dis_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_AFTR_DIS                ') As Vat_Amt_Aftr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_BFR_DIS                 ') As Vat_Amt_Bfr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_VAT                 ') As Dis_Amt_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2_VAT                ') As Dis_Amt_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3_VAT                ') As Dis_Amt_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_MST_VAT             ') As Vat_Amt_Dis_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL2_VAT            ') As Vat_Amt_Dis_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL3_VAT            ') As Vat_Amt_Dis_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_AFTR_VAT                ') As Dis_Amt_Aftr_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/LEV_NO                          ') As Lev_No
                               ,Extractvalue (Value (Xmldtldmy), '*/ITEM_DESC                       ') As Item_Desc
                               ,Extractvalue (Value (Xmldtldmy), '*/BARCODE                         ') As Barcode
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL1                      ') As Field_Dtl1
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL2                      ') As Field_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL3                      ') As Field_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/EMP_NO                          ') As Emp_No
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_TYPE_REF                    ') As Doc_Type_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_NO_REF                      ') As Doc_No_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SER_REF                     ') As Doc_Ser_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/SUB_C_CODE                      ') As Sub_C_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO_REF                     ') As Rcrd_No_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_NO                       ') As Qt_Prm_No
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_SER                      ') As Qt_Prm_Ser
                               ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_RCRD_NO                  ') As Qt_Prm_Rcrd_No
                               ,Extractvalue (Value (Xmldtldmy), '*/I_LENGTH                        ') As I_Length
                               ,Extractvalue (Value (Xmldtldmy), '*/I_WIDTH                         ') As I_Width
                               ,Extractvalue (Value (Xmldtldmy), '*/I_HEIGHT                        ') As I_Height
                               ,Extractvalue (Value (Xmldtldmy), '*/I_NUMBER                        ') As I_Number
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_QTY                          ') As Wt_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_UNT                          ') As Wt_Unt
                               ,Extractvalue (Value (Xmldtldmy), '*/MEASUR_PRICE                    ') As Measur_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/ARGMNT_NO                       ') As Argmnt_No
                               ,Extractvalue (Value (Xmldtldmy), '*/SERIALNO_N                      ') As SERIALNO_N                                   
                           From Table (Xmlsequence (Extract (V_Xml_Type, '/RT_BILL/IAS_RT_BILL_DTL'))) Xmldtldmy)
            Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(12)
               ------------------------------------------
               V_DOC_SEQ:=NULL;
               V_Rcrd_No :=null;
               V_Icode  :=Null;
               V_Itm_Unt:=Null;
               V_Barcode:=Null;
               
                Ias_Itm_Pkg.Get_I_Code (P_Barcode => D_Cv.I_Code, P_I_Code => V_Icode, P_Itm_Unt => V_Itm_Unt);
                If V_Icode Is  Null  Or nvl(V_Icode,'0')=Nvl(D_Cv.I_Code,'0') Then                                  
                  V_Icode  := D_Cv.I_Code;
                  V_Itm_Unt:=D_Cv.Itm_Unt;
                  V_Barcode:=D_Cv.Barcode;
                Else
                    V_Barcode:=D_Cv.I_Code;  
                End If;
               Begin
                  Ars_Api_Trns_Pkg.Insrt_Ias_Rt_Bill_Dtl_RQ (P_I_Code => V_Icode
                                        ,P_I_Qty                  => D_Cv.I_Qty
                                        ,P_P_Size                 => D_Cv.P_Size
                                        ,P_Itm_Unt                => V_Itm_Unt
                                        ,P_I_Price                => D_Cv.I_Price
                                        ,P_I_Price_Vat            => D_Cv.I_Price_Vat
                                        ,P_DOC_SEQUENCE           => V_Doc_Seq
                                        ,P_Rcrd_No                => V_Rcrd_No
                                        ,P_W_Code                 => D_Cv.W_Code
                                        ,P_Bill_No                => D_Cv.Bill_No
                                        ,P_Bill_Doc_Type          => D_Cv.Bill_Doc_Type
                                        ,P_Bill_Ser               => D_Cv.Bill_Ser
                                        ,P_Cc_Code                => D_Cv.Cc_Code
                                        ,P_Pj_No                  => D_Cv.Pj_No
                                        ,P_Actv_No                => D_Cv.Actv_No
                                        ,P_Expire_Date            => TO_DATE(D_Cv.Expire_Date,'DD/MM/RRRR')
                                        ,P_Batch_No               => D_Cv.Batch_No
                                        ,P_Free_Qty               => D_Cv.Free_Qty
                                        ,P_DOC_SEQUENCE_SI        => case when nvl(D_Cv.DOC_SEQUENCE_SI,0)=0 then null else D_Cv.DOC_SEQUENCE_SI end 
                                        ,P_SI_RCRD_NO             => case when nvl(D_Cv.SI_RCRD_NO,0)=0 then null else D_Cv.SI_RCRD_NO end  
                                        ,P_Dis_Per                => D_Cv.Dis_Per
                                        ,P_Dis_Per2               => D_Cv.Dis_Per2
                                        ,P_Dis_Per3               => D_Cv.Dis_Per3
                                        ,P_Dis_Amt                => D_Cv.Dis_Amt
                                        ,P_Dis_Amt_Mst            => D_Cv.Dis_Amt_Mst
                                        ,P_Dis_Amt_Dtl            => D_Cv.Dis_Amt_Dtl
                                        ,P_Dis_Amt_Dtl2           => D_Cv.Dis_Amt_Dtl2
                                        ,P_Dis_Amt_Dtl3           => D_Cv.Dis_Amt_Dtl3
                                        ,P_Vat_Per                => D_Cv.Vat_Per
                                        ,P_Vat_Amt                => D_Cv.Vat_Amt
                                        ,P_Othr_Amt               => D_Cv.Othr_Amt
                                        ,P_Vat_Amt_Othr           => D_Cv.Vat_Amt_Othr
                                        ,P_Othr_Amt_Disc          => D_Cv.Othr_Amt_Disc
                                        ,P_Dis_Aftr_Vat_Mst       => D_Cv.Dis_Aftr_Vat_Mst
                                        ,P_Dis_Amt_Mst_Vat        => D_Cv.Dis_Amt_Mst_Vat
                                        ,P_Vat_Amt_Dis_Dtl_Vat    => D_Cv.Vat_Amt_Dis_Dtl_Vat
                                        ,P_Vat_Amt_Aftr_Dis       => D_Cv.Vat_Amt_Aftr_Dis
                                        ,P_Vat_Amt_Bfr_Dis        => D_Cv.Vat_Amt_Bfr_Dis
                                        ,P_Dis_Amt_Dtl_Vat        => D_Cv.Dis_Amt_Dtl_Vat
                                        ,P_Dis_Amt_Dtl2_Vat       => D_Cv.Dis_Amt_Dtl2_Vat
                                        ,P_Dis_Amt_Dtl3_Vat       => D_Cv.Dis_Amt_Dtl3_Vat
                                        ,P_Vat_Amt_Dis_Mst_Vat    => D_Cv.Vat_Amt_Dis_Mst_Vat
                                        ,P_Vat_Amt_Dis_Dtl2_Vat   => D_Cv.Vat_Amt_Dis_Dtl2_Vat
                                        ,P_Vat_Amt_Dis_Dtl3_Vat   => D_Cv.Vat_Amt_Dis_Dtl3_Vat
                                        ,P_Dis_Amt_Aftr_Vat       => D_Cv.Dis_Amt_Aftr_Vat
                                        ,P_Lev_No                 => D_Cv.Lev_No
                                        ,P_Item_Desc              => D_Cv.Item_Desc
                                        ,P_Barcode                => V_Barcode
                                        ,P_Field_Dtl1             => D_Cv.Field_Dtl1
                                        ,P_Field_Dtl2             => D_Cv.Field_Dtl2
                                        ,P_Field_Dtl3             => D_Cv.Field_Dtl3
                                        ,P_Emp_No                 => D_Cv.Emp_No
                                        ,P_Doc_Type_Ref           => case when nvl(D_Cv.Doc_Type_Ref,0)=0 then null else D_Cv.Doc_Type_Ref end
                                        ,P_Doc_Ser_Ref            => case when nvl(D_Cv.Doc_Ser_Ref,0)=0 then null else D_Cv.Doc_Ser_Ref end
                                        ,P_Doc_No_Ref             => case when nvl(D_Cv.Doc_No_Ref,0)=0 then null else D_Cv.Doc_No_Ref end  
                                        ,P_Rcrd_No_Ref            => case when nvl(D_Cv.Rcrd_No_Ref,0)=0 then null else D_Cv.Rcrd_No_Ref end
                                        ,P_Sub_C_Code             => D_Cv.Sub_C_Code                                        
                                        ,P_Qt_Prm_No              => D_Cv.Qt_Prm_No
                                        ,P_Qt_Prm_Ser             => D_Cv.Qt_Prm_Ser
                                        ,P_Qt_Prm_Rcrd_No         => D_Cv.Qt_Prm_Rcrd_No
                                        ,P_I_Length               => D_Cv.I_Length
                                        ,P_I_Width                => D_Cv.I_Width
                                        ,P_I_Height               => D_Cv.I_Height
                                        ,P_I_Number               => D_Cv.I_Number
                                        ,P_Wt_Qty                 => D_Cv.Wt_Qty
                                        ,P_Wt_Unt                 => D_Cv.Wt_Unt
                                        ,P_Argmnt_No              => D_Cv.Argmnt_No
                                        ,P_SERIALNO_N             => D_Cv.SERIALNO_N
                                        ,P_Msg_Txt                => P_Msg_Txt
                                        ,P_ERR_NO               => P_Err_No
                                        ,P_Pkg_NM                 => P_Pkg_Nm);

                  If P_Msg_Txt Is Not Null Then                 
                     Goto Rtn_Rslt;
                  End If;
               Exception
                  When Others Then                 
                     Raise_Application_Error (-20556, 'Err when insert IAS_RT_BILL_DTL DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);
               End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --(2)
            --##------------------------------------------------------------------------------------------------------------------------------##--
            For Tax_Mvmnt_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As Bill_Doc_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As Doc_Jv_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As Tax_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As Clc_Typ_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As Agncy_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                      ') As I_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                     ') As Itm_Unt
                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                      ') As P_Size
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_PRICE                     ') As I_Price
                                      ,Extractvalue( Value( Xmldtldmy), '*/DISC_AMT                    ') As Disc_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                    ') As A_Cy
                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As Ac_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As Tax_Prcnt
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As Tax_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                      ') As W_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As Cc_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As Pj_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As Actv_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As Rcrd_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As Doc_Sequence
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As Tax_Amt_L
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_QTY                       ') As I_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/FREE_QTY                    ') As Free_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As Ref_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_COST                    ') As Stk_Cost
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_RATE                    ') As Stk_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TAX_FREE_QTY_FLG        ') As Clc_Tax_Free_Qty_Flg
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/RT_BILL/GNR_TAX_ITM_MOVMNT'))) Xmldtldmy                                  
                                   )                              
               Loop
                   IF NVL(Tax_Mvmnt_Cv.I_CODE,'0')=NVL(D_CV.I_CODE,'0')  AND NVL(Tax_Mvmnt_Cv.ITM_UNT,'0')=NVL(D_CV.ITM_UNT,'0')
                     AND NVL(Tax_Mvmnt_Cv.RCRD_NO,0)=NVL(D_CV.RCRD_NO,0) THEN    
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Gnr_Tax_Itm_Movmnt(P_Doc_Typ                => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Bill_Doc_Type          => Ars_Api_Trns_Pkg.G_RT_Bill_Doc_Type
                                                     ,P_Doc_Jv_Type            =>Ars_Api_Trns_Pkg.G_SR_TYPE-- Tax_Mvmnt_Cv.Doc_Jv_Type
                                                     ,P_Tax_No                 => Tax_Mvmnt_Cv.Tax_No
                                                     ,P_Clc_Typ_No             => Tax_Mvmnt_Cv.Clc_Typ_No
                                                     ,P_Agncy_No               => Tax_Mvmnt_Cv.Agncy_No
                                                     ,P_I_Code                 => V_Icode
                                                     ,P_Itm_Unt                => V_Itm_Unt
                                                     ,P_P_Size                 => Tax_Mvmnt_Cv.P_Size
                                                     ,P_I_Price                => Tax_Mvmnt_Cv.I_Price
                                                     ,P_Disc_Amt               => Tax_Mvmnt_Cv.Disc_Amt
                                                     ,P_A_Code                 => Tax_Mvmnt_Cv.A_Code
                                                     ,P_Cur_Code               => Tax_Mvmnt_Cv.A_Cy
                                                     ,P_Ac_Rate                => Tax_Mvmnt_Cv.Ac_Rate
                                                     ,P_Tax_Prcnt              => Tax_Mvmnt_Cv.Tax_Prcnt
                                                     ,P_Tax_Amt                => Tax_Mvmnt_Cv.Tax_Amt
                                                     ,P_W_Code                 => Ars_Api_Trns_Pkg.G_W_Code
                                                     ,P_Cc_Code                => Ars_Api_Trns_Pkg.G_Cc_Code
                                                     ,P_Pj_No                  => Ars_Api_Trns_Pkg.G_Pj_No
                                                     ,P_Actv_No                => Ars_Api_Trns_Pkg.G_Actv_No                                                     
                                                     ,P_Doc_Sequence           => V_Doc_Seq
                                                     ,P_Rcrd_No                => V_Rcrd_No
                                                     ,P_Tax_Amt_L              => Tax_Mvmnt_Cv.Tax_Amt_L
                                                     ,P_I_Qty                  => Tax_Mvmnt_Cv.I_Qty
                                                     ,P_Free_Qty               => Tax_Mvmnt_Cv.Free_Qty
                                                     ,P_Ref_No                 => Tax_Mvmnt_Cv.Ref_No
                                                     ,P_Stk_Cost               => Tax_Mvmnt_Cv.Stk_Cost
                                                     ,P_Stk_Rate               => Tax_Mvmnt_Cv.Stk_Rate
                                                     ,P_Clc_Tax_Free_Qty_Flg   => M_CV.Clc_Tax_Free_Qty_Flg
                                                     ,P_Msg_Txt                => P_Msg_Txt
                                                     ,P_ERR_NO               => P_Err_No
                                                     ,P_Pkg_Nm                 => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then                    
                        Raise_Application_Error( -20557, 'ERR WHEN INSERT INSRT_GNR_TAX_ITM_MOVMNT DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                    End;
                 END IF; 
               End Loop;            
            --##---------------------------------------------------------------------------------------------------------------------------##--
            End Loop;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            --(12)
            -----------------------------------------------------------------------------------------------------------------------------
            --##---------------------------------------------------------------------------------------------------------------------------##--
            --##INSERT OTHER CHARGE
                         For Othr_Chrg_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                        ') As Sc_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                       ') As A_Code
                                          ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                     ') As A_Cy
                                          ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                      ') As Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/PER                          ') As Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/AMT                          ') As Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/INV_ITEM                     ') As Inv_Item
                                          ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                      ') As Rcrd_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                      ') As Bill_Py
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_AMT                      ') As Vat_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_PER                      ') As Vat_Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AMT                       ') As Sc_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AC_RATE                   ') As Sc_Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_A_CY                      ') As Sc_A_Cy
                                      From Table( Xmlsequence( Extract( V_Xml_Type, '/RT_BILL/OTHER_CHARGES'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Other_Charges(P_Doc_Typ      => Ars_Api_Trns_Pkg.G_Doc_Typ
                                        ,P_Bill_Doc_Type   =>Ars_Api_Trns_Pkg.G_RT_Bill_Doc_Type
                                        ,P_BILL_TYPE      =>136
                                        ,P_Sc_No        => Othr_Chrg_Cv.Sc_No
                                        ,P_A_Code       => Othr_Chrg_Cv.A_Code
                                        ,P_Cur_Code     => Othr_Chrg_Cv.A_Cy
                                        ,P_Ac_Rate      => Othr_Chrg_Cv.Ac_Rate
                                        ,P_Per          => Othr_Chrg_Cv.Per
                                        ,P_Amt          => Othr_Chrg_Cv.Amt
                                        ,P_Inv_Item     => Othr_Chrg_Cv.Inv_Item
                                        ,P_Rcrd_No      => Othr_Chrg_Cv.Rcrd_No
                                        ,P_Bill_Py      => Othr_Chrg_Cv.Bill_Py
                                        ,P_Vat_Amt      => Othr_Chrg_Cv.Vat_Amt
                                        ,P_Vat_Per      => Othr_Chrg_Cv.Vat_Per
                                        ,P_Sc_Amt       => Othr_Chrg_Cv.Sc_Amt
                                        ,P_Sc_Ac_Rate   => Othr_Chrg_Cv.Sc_Ac_Rate
                                        ,P_Sc_A_Cy      => Othr_Chrg_Cv.Sc_A_Cy
                                        ,P_Msg_Txt      => P_Msg_Txt
                                        ,P_ERR_NO     => P_Err_No
                                        ,P_Pkg_Nm       => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                      --  ---Rollback;
                        Raise_Application_Error( -20558, 'ERR WHEN INSERT OTHER_CHARGES DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
         --##INSERT OTHER CHARGE ITEMS
               For Othr_Chrg_Itm_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                    ') As Doc_Typ
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                      ') As Sc_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                     ') As A_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                   ') As A_Cy
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                    ') As Ac_Rate
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PER                        ') As Per
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AMT                        ') As Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                     ') As W_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                    ') As Cc_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                      ') As Pj_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                    ') As Actv_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                    ') As Rcrd_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SI_TYPE                    ') As Si_Type
                                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                     ') As I_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                    ') As Itm_Unt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                     ') As P_Size
                                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                    ') As Bill_Py
                                                      ,Extractvalue( Value( Xmldtldmy), '*/UNIT_AMT                   ') As Unit_Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/POST_CODE                  ') As Post_Code
                                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/RT_BILL/OTHER_CHARGES_ITEMS'))) Xmldtldmy)
                       Loop
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Other_Charges_Items(P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                      ,P_Sc_No       => Othr_Chrg_Itm_Cv.Sc_No
                                                      ,P_A_Code      => Othr_Chrg_Itm_Cv.A_Code
                                                      ,P_Cur_Code    => Othr_Chrg_Itm_Cv.A_Cy
                                                      ,P_Ac_Rate     => Othr_Chrg_Itm_Cv.Ac_Rate
                                                      ,P_Per         => Othr_Chrg_Itm_Cv.Per
                                                      ,P_Amt         => Othr_Chrg_Itm_Cv.Amt
                                                      ,P_W_Code      => Othr_Chrg_Itm_Cv.W_Code
                                                      ,P_Cc_Code     => Othr_Chrg_Itm_Cv.Cc_Code
                                                      ,P_Pj_No       => Othr_Chrg_Itm_Cv.Pj_No
                                                      ,P_Actv_No     => Othr_Chrg_Itm_Cv.Actv_No
                                                      ,P_Rcrd_No     => Othr_Chrg_Itm_Cv.Rcrd_No
                                                      ,P_Si_Type     => Othr_Chrg_Itm_Cv.Si_Type
                                                      ,P_I_Code      => Othr_Chrg_Itm_Cv.I_Code
                                                      ,P_Itm_Unt     => Othr_Chrg_Itm_Cv.Itm_Unt
                                                      ,P_P_Size      => Othr_Chrg_Itm_Cv.P_Size
                                                      ,P_Bill_Py     => Othr_Chrg_Itm_Cv.Bill_Py
                                                      ,P_Unit_Amt    => Othr_Chrg_Itm_Cv.Unit_Amt
                                                      ,P_Post_Code   => Othr_Chrg_Itm_Cv.Post_Code
                                                      ,P_Msg_Txt     => P_Msg_Txt
                                                      ,P_ERR_NO    => P_Err_No
                                                      ,P_Pkg_Nm      => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                          Exception
                             When Others Then
                                ---Rollback;
                                Raise_Application_Error( -20559, 'ERR WHEN INSERT OTHER_CHARGES_ITEMS DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                          End;
                       End Loop; 
         --##---------------------------------------------------------------------------------------------------------------------------##--
                  For Tax_INPT_Mvmnt_Cv In (SELECT    Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As DOC_TYP              
                                            ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As BILL_DOC_TYPE         
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As DOC_JV_TYPE                                                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As TAX_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As CLC_TYP_NO           
                                            ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As AGNCY_NO                                        
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_CODE                   ') As INPT_CODE            
                                            ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_CODE               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                     ') As CUR_CODE                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As AC_RATE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_AMT                    ') As INPT_AMT             
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As TAX_PRCNT            
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As TAX_AMT              
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As TAX_AMT_L            
                                            ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As CC_CODE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As PJ_NO                
                                            ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As ACTV_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As REF_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As RCRD_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As DOC_SEQUENCE
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/RT_BILL/GNR_TAX_INPT_MOVMNT'))) Xmldtldmy                                  
                                   )                              
               Loop                    
                    Begin
                          Ars_Api_Trns_Pkg.INSRT_GNR_TAX_INPT_MOVMNT(
                                            P_DOC_TYP                    =>Ars_Api_Trns_Pkg.G_DOC_TYP
                                           ,P_BILL_DOC_TYPE              =>Ars_Api_Trns_Pkg.G_RT_BILL_DOC_TYPE
                                           ,P_DOC_JV_TYPE                =>Ars_Api_Trns_Pkg.G_SR_TYPE--Tax_INPT_Mvmnt_Cv.DOC_JV_TYPE                                       
                                           ,P_TAX_NO                     =>Tax_INPT_Mvmnt_Cv.TAX_NO
                                          , P_CLC_TYP_NO                 =>Tax_INPT_Mvmnt_Cv.CLC_TYP_NO 
                                          , P_AGNCY_NO                   =>Tax_INPT_Mvmnt_Cv.AGNCY_NO                            
                                          , P_INPT_CODE                  =>Tax_INPT_Mvmnt_Cv.INPT_CODE 
                                           ,P_A_CODE                     =>Tax_INPT_Mvmnt_Cv.A_CODE 
                                          , P_A_CY                       =>Tax_INPT_Mvmnt_Cv.CUR_CODE
                                          , P_AC_RATE                    =>Tax_INPT_Mvmnt_Cv.AC_RATE 
                                          , P_INPT_AMT                   =>Tax_INPT_Mvmnt_Cv.INPT_AMT 
                                          , P_TAX_PRCNT                  =>Tax_INPT_Mvmnt_Cv.TAX_PRCNT 
                                          , P_TAX_AMT                    =>Tax_INPT_Mvmnt_Cv.TAX_AMT
                                          , P_TAX_AMT_L                  =>Tax_INPT_Mvmnt_Cv.TAX_AMT_L 
                                           ,P_CC_CODE                    =>Ars_Api_Trns_Pkg.G_CC_CODE 
                                          , P_PJ_NO                      =>Ars_Api_Trns_Pkg.G_PJ_NO 
                                          , P_ACTV_NO                    =>Ars_Api_Trns_Pkg.G_ACTV_NO 
                                          , P_REF_NO                     =>Tax_INPT_Mvmnt_Cv.REF_NO 
                                          , P_RCRD_NO                    =>Tax_INPT_Mvmnt_Cv.RCRD_NO 
                                          , P_DOC_SEQUENCE               =>Tax_INPT_Mvmnt_Cv.DOC_SEQUENCE
                                          ,P_Msg_Txt                     =>P_Msg_Txt
                                          ,P_ERR_NO                     =>P_ERR_NO
                                          ,P_Pkg_NM                     =>P_Pkg_NM); 

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then
                       -- ---Rollback;
                        Raise_Application_Error( -20560, 'ERR WHEN INSERT INSRT_GNR_TAX_INPT_MOVMNT DOC_NO= ' || V_DOC_NO || ' ' || Chr( 10) || Sqlerrm);
                    End;                 
               End Loop;
          --##---------------------------------------------------------------------------------------------------------------------------##--
            For Attach_Cv
                  In (Select Extractvalue (Value (Xmldtldmy), '*/FILE_NAME         ') As File_Name
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/RT_BILL/ATTACH'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Archives (P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Doc_Ser     => Ars_Api_Trns_Pkg.G_Doc_Ser
                                                     ,P_File_Name   => Attach_Cv.File_Name
                                                     ,P_Msg_Txt     => P_Msg_Txt
                                                     ,P_Err_No      => P_Err_No
                                                     ,P_Pkg_Nm      => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                        Raise_Application_Error (-20719,'Err.in Ars_Api_Trns_Pkg.INSRT_ARCHIVES= '|| V_Doc_No|| ' '|| Chr (10)|| Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
            --## CHK INSERT DATA
            Ars_Api_Trns_Pkg.Chk_Insrt_Data (P_Doc_Typ    => 136
                           ,P_Doc_Ser    => Ars_Api_Trns_Pkg.G_Doc_Ser
                           ,P_Msg_Txt    => P_Msg_Txt
                           ,P_ERR_NO   => P_Err_No
                           ,P_Pkg_NM   => P_Pkg_Nm);

            If P_Msg_Txt Is Not Null Then              
               Goto Rtn_Rslt;
            End If;                                          
         ----------------------------------------------------------------------------------------------------------
         End Loop; 
      ---################################################################################################---   
      ELSIf P_Doc_Typ = 52 Then 
       --QUOTATION
       For M_Cv In (Select Extractvalue (Value (Xmlmstdmy),'*/SYS_NO         ') As Sys_No
                      ,Extractvalue (Value (Xmlmstdmy), '*/DOC_NO              ') As Doc_No
                      ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER             ') As Doc_Ser
                      ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DATE             ') As Doc_Date
                      ,Extractvalue (Value (Xmlmstdmy), '*/CUR_CODE             ') As Cur_Code
                      ,Extractvalue (Value (Xmlmstdmy), '*/CUR_RATE             ') As Cur_Rate
                      ,Extractvalue (Value (Xmlmstdmy), '*/QT_TYPE              ') As QT_Type
                      ,Extractvalue (Value (Xmlmstdmy), '*/C_CODE               ') As C_Code
                      ,Extractvalue (Value (Xmlmstdmy), '*/C_NAME               ') As C_Name
                      ,Extractvalue (Value (Xmlmstdmy), '*/C_TAX_CODE           ') As C_TAX_CODE
                      ,Extractvalue (Value (Xmlmstdmy), '*/A_DESC               ') As A_Desc
                      ,Extractvalue (Value (Xmlmstdmy), '*/CC_CODE              ') As Cc_Code
                      ,Extractvalue (Value (Xmlmstdmy), '*/PJ_NO                ') As Pj_No
                      ,Extractvalue (Value (Xmlmstdmy), '*/ACTV_NO              ') As Actv_No
                      ,Extractvalue (Value (Xmlmstdmy), '*/W_CODE               ') As W_Code
                      ,Extractvalue (Value (Xmlmstdmy), '*/REP_CODE             ') As Rep_Code
                      ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT              ') As Vat_Amt
                      ,Extractvalue (Value (Xmlmstdmy), '*/DOC_AMT              ') As DOC_Amt
                      ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT             ') As Disc_Amt
                      ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_DTL         ') As Disc_Amt_Dtl
                      ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST         ') As Disc_Amt_Mst
                      ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT             ') As Othr_Amt
                      ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_OTHR         ') As Vat_Amt_Othr
                      ,Extractvalue (Value (Xmlmstdmy), '*/OTHR_AMT_DISC         ') As OTHR_AMT_DISC
                      ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_MST_VAT     ') As Disc_Amt_Mst_Vat
                      ,Extractvalue (Value (Xmlmstdmy), '*/VAT_AMT_DISC_MST     ') As Vat_Amt_Disc_Mst
                      ,Extractvalue (Value (Xmlmstdmy), '*/DISC_AMT_AFTR_VAT    ') As Disc_Amt_Aftr_Vat
                      ,Extractvalue (Value (Xmlmstdmy), '*/CASH_NO              ') As Cash_No
                      ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TYP_NO_TAX       ') As Clc_Typ_No_Tax
                      ,Extractvalue (Value (Xmlmstdmy), '*/CLC_VAT_PRICE_TYP    ') As Clc_Vat_Price_Typ
                      ,Extractvalue (Value (Xmlmstdmy), '*/PAY_TERMS            ') As Pay_Terms
                      ,Extractvalue (Value (Xmlmstdmy), '*/REQ_DAYS             ') As Req_Days
                      ,Extractvalue (Value (Xmlmstdmy), '*/REF_NO               ') As Ref_No
                      ,Extractvalue (Value (Xmlmstdmy), '*/REF_DATE             ') As Ref_Date
                      ,Extractvalue (Value (Xmlmstdmy), '*/QUOT_TEND            ') As Quot_Tend
                      ,Extractvalue (Value (Xmlmstdmy), '*/QUOT_TEND_DATE       ') As Quot_Tend_Date
                      ,Extractvalue (Value (Xmlmstdmy), '*/PORT_OF_DEP          ') As Port_Of_Dep
                      ,Extractvalue (Value (Xmlmstdmy), '*/BILL_DOC_TYPE        ') As Bill_Doc_Type
                      ,Extractvalue (Value (Xmlmstdmy), '*/QUOT_DUE_DATE        ') As Quot_Due_Date
                      ,Extractvalue (Value (Xmlmstdmy), '*/QUOT_EXPIRE_DATE     ') As Quot_Expire_Date
                      ,Extractvalue (Value (Xmlmstdmy), '*/CHEQUE_DUE_DATE      ') As Cheque_Due_Date
                      ,Extractvalue (Value (Xmlmstdmy), '*/SI_TYPE              ') As Si_Type
                      ,Extractvalue (Value (Xmlmstdmy), '*/EXTERNAL_POST        ') As External_Post
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD1               ') As Field1
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD2               ') As Field2
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD3               ') As Field3
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD4               ') As Field4
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD5               ') As Field5
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD6               ') As Field6
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD7               ') As Field7
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD8               ') As Field8
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD9               ') As Field9
                      ,Extractvalue (Value (Xmlmstdmy), '*/FIELD10              ') As Field10
                      ,Extractvalue (Value (Xmlmstdmy), '*/CLC_TAX_FREE_QTY_FLG ') As Clc_Tax_Free_Qty_Flg
                      ,Extractvalue (Value (Xmlmstdmy), '*/DOC_SER_EXTRNL       ') As Doc_Ser_Extrnl
                      ,Extractvalue (Value (Xmlmstdmy), '*/TYP_NO              ') As TYP_NO
                      ,Extractvalue (Value (Xmlmstdmy), '*/DOC_DUE_DATE         ') As DOC_DUE_DATE
                      ,Extractvalue (Value (Xmlmstdmy), '*/TYP_NO_REF          ') As TYP_NO_REF
                      ,Extractvalue (Value (Xmlmstdmy), '*/DOC_EXPIRE_DATE     ') As DOC_EXPIRE_DATE
                      ,Extractvalue (Value (Xmlmstdmy), '*/BRN_NO               ') As Brn_No
                      ,Extractvalue (Value (Xmlmstdmy), '*/BRN_YEAR             ') As Brn_Year
                      ,Extractvalue (Value (Xmlmstdmy), '*/BRN_USR              ') As Brn_Usr
                      ,Extractvalue (Value (Xmlmstdmy), '*/AD_TRMNL_NM           ') As Ad_Trmnl_Nm
                      ,Extractvalue (Value (Xmlmstdmy), '*/AD_U_ID               ') As Ad_U_Id
                      ,Extractvalue (Value (Xmlmstdmy), '*/AD_DATE               ') As Ad_Date
                  From Table (Xmlsequence (Extract (V_Xml_Type, '/QUOT/QUOTATION'))) Xmlmstdmy)
   Loop --(11)
      --------------------------------------------------------------------------------
      V_Doc_Typ   := P_Doc_Typ;
      ---------------------------------------------------------------------------------
            Chk_Prmtr (   P_Sys_No            =>M_Cv.Sys_No
                          ,P_Doc_Typ          =>P_Doc_Typ                           
                          ,P_COMMIT_FLG       =>P_COMMIT_FLG
                          ,P_CLC_TAX_METHOD   =>P_CLC_TAX_METHOD                                                      
                          ,P_Pst_Typ          =>P_Pst_Typ
                          ,P_Pst_FROM_BR      =>P_Pst_FROM_BR
                          ,P_DTS_ONLINE       =>P_DTS_ONLINE
                          ,P_Lng_No           =>P_Lng_No                          
                          ,P_Msg_Txt          =>P_Msg_Txt
                          ,P_ERR_NO           =>P_ERR_NO
                          ,P_Pkg_Nm           =>P_Pkg_Nm);
                          If  P_Msg_Txt Is Not Null Then
                              Goto Rtn_Rslt;
                          End If;
          ---------------------------------------------------------------------------------            
            Begin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(1)
               Ars_Api_Trns_Pkg.Insrt_QUOTATION   (P_Sys_No              => M_Cv.Sys_No
                                 ,P_Doc_No              => M_Cv.Doc_No
                                 ,P_Doc_Type            => 52
                                 ,P_Doc_Ser             => Null
                                 ,P_Doc_Date            => TO_DATE(M_Cv.Doc_Date,'DD/MM/RRRR')
                                 ,P_Cur_Code            => M_Cv.Cur_Code
                                 ,P_Cur_Rate            => M_Cv.Cur_Rate
                                 ,P_QT_Type             => NVL(M_Cv.TYP_NO,M_Cv.QT_Type)
                                 ,P_C_Code              => M_Cv.C_Code
                                 ,P_C_Name              => M_Cv.C_Name
                                 ,P_C_TAX_CODE          => M_Cv.C_TAX_CODE
                                 ,P_A_Desc              => M_Cv.A_Desc
                                 ,P_Cc_Code             => M_Cv.Cc_Code
                                 ,P_Pj_No               => M_Cv.Pj_No
                                 ,P_Actv_No             => M_Cv.Actv_No
                                 ,P_W_Code              => M_Cv.W_Code
                                 ,P_Rep_Code            => M_Cv.Rep_Code                                
                                 ,P_Vat_Amt             => M_Cv.Vat_Amt
                                 ,P_DOC_Amt             => M_Cv.DOC_Amt
                                 ,P_Disc_Amt            => M_Cv.Disc_Amt
                                 ,P_Disc_Amt_Dtl        => M_Cv.Disc_Amt_Dtl
                                 ,P_Disc_Amt_Mst        => M_Cv.Disc_Amt_Mst
                                 ,P_Othr_Amt            => M_Cv.Othr_Amt
                                 ,P_Vat_Amt_Othr        => M_Cv.Vat_Amt_Othr
                                 ,P_OTHR_AMT_DISC       => M_Cv.OTHR_AMT_DISC
                                 ,P_Disc_Amt_Mst_Vat    => M_Cv.Disc_Amt_Mst_Vat
                                 ,P_Vat_Amt_Disc_Mst    => M_Cv.Vat_Amt_Disc_Mst
                                 ,P_Disc_Amt_Aftr_Vat   => M_Cv.Disc_Amt_Aftr_Vat
                                 ,P_Cash_No             => M_Cv.Cash_No
                                 ,P_Clc_Typ_No_Tax      => M_Cv.Clc_Typ_No_Tax
                                 ,P_Clc_Vat_Price_Typ   => M_Cv.Clc_Vat_Price_Typ
                                 ,P_PAY_TERMS           => M_Cv.PAY_TERMS
                                 ,P_REF_NO              => M_CV.REF_NO
                                 ,P_REF_DATE            => TO_DATE(M_Cv.REF_DATE,'DD/MM/RRRR')
                                 ,P_QUOT_TEND           => M_CV.QUOT_TEND
                                 ,P_QUOT_TEND_DATE      => TO_DATE(M_Cv.QUOT_TEND_DATE,'DD/MM/RRRR')                                 
                                 ,P_PORT_OF_DEP         =>M_CV.PORT_OF_DEP                                                            
                                 ,P_Bill_Doc_Type       => M_Cv.Bill_Doc_Type
                                 ,P_QUOT_Due_Date       => NVL(TO_DATE(M_Cv.DOC_Due_Date,'DD/MM/RRRR'),TO_DATE(M_Cv.QUOT_Due_Date,'DD/MM/RRRR'))
                                 ,P_QUOT_Expire_Date   => NVL(TO_DATE(M_Cv.DOC_Expire_Date,'DD/MM/RRRR'),TO_DATE(M_Cv.QUOT_Expire_Date,'DD/MM/RRRR'))
                                 ,P_Cheque_Due_Date     => TO_DATE(M_Cv.Cheque_Due_Date,'DD/MM/RRRR')                                
                                 ,P_Si_Type             => NVL(M_Cv.TYP_NO_REF,M_Cv.Si_Type)
                                 ,P_External_Post       => M_Cv.External_Post
                                 ,P_Field1              => M_Cv.Field1
                                 ,P_Field2              => M_Cv.Field2
                                 ,P_Field3              => M_Cv.Field3
                                 ,P_Field4              => M_Cv.Field4
                                 ,P_Field5              => M_Cv.Field5
                                 ,P_Field6              => M_Cv.Field6
                                 ,P_Field7              => M_Cv.Field7
                                 ,P_Field8              => M_Cv.Field8
                                 ,P_Field9              => M_Cv.Field9
                                 ,P_Field10             => M_Cv.Field10
                                 ,P_CLC_TAX_FREE_QTY_FLG =>M_Cv.CLC_TAX_FREE_QTY_FLG
                                 ,P_Doc_Ser_Extrnl      =>M_Cv.DOC_SER_EXTRNL
                                 ,P_Brn_No              => M_Cv.Brn_No
                                 ,P_Brn_Year            => M_Cv.Brn_Year
                                 ,P_BRN_USR             => M_Cv.BRN_USR
                                 ,P_Ad_Trmnl_Nm         => M_Cv.Ad_Trmnl_Nm
                                 ,P_Ad_U_Id             => M_Cv.Ad_U_Id
                                 ,P_Ad_Date             => TO_DATE(TO_CHAR(M_CV.AD_DATE),'DD/MM/RRRR HH24:MI:SS')
                                 ,P_CLC_TAX_METHOD      =>P_CLC_TAX_METHOD
                                 ,P_DTS_ONLINE          =>P_DTS_ONLINE
                                 ,P_Lng_No              =>P_Lng_No 
                                 ,P_Msg_Txt             => P_Msg_Txt
                                 ,P_ERR_NO              => P_Err_No
                                 ,P_Pkg_NM              => P_Pkg_Nm);                                   
                If P_Msg_Txt Is Not Null Then                
                  Goto Rtn_Rslt;
                End If ;
            Exception
               When Others Then               
                  Raise_Application_Error (-20632, 'Err when insert QUOTATION DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);            
            End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  --(1)
            -------------------------------------------------------------------------------------------
            For D_Cv In (Select Extractvalue (Value (Xmldtldmy), '*/I_CODE                 ') As I_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/ITM_UNT                ') As Itm_Unt
                               ,Extractvalue (Value (Xmldtldmy), '*/I_QTY                  ') As I_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/P_QTY                  ') As P_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/P_SIZE                  ') As P_Size
                               ,Extractvalue (Value (Xmldtldmy), '*/FREE_QTY                ') As Free_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/BARCODE                 ') As Barcode
                               ,Extractvalue (Value (Xmldtldmy), '*/BATCH_NO                ') As Batch_No
                               ,Extractvalue (Value (Xmldtldmy), '*/EXPIRE_DATE             ') As Expire_Date
                               ,Extractvalue (Value (Xmldtldmy), '*/W_CODE                  ') As W_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/CC_CODE                  ') As Cc_Code
                               ,Extractvalue (Value (Xmldtldmy), '*/ACTV_NO                  ') As Actv_No
                               ,Extractvalue (Value (Xmldtldmy), '*/PJ_NO                    ') As Pj_No
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE                  ') As I_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/I_PRICE_VAT              ') As I_Price_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/MEASUR_PRICE             ') As Measur_Price
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT                 ') As Othr_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/OTHR_AMT_DISC            ') As Othr_Amt_Disc
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT                  ') As Vat_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_AFTR_DIS         ') As Vat_Amt_Aftr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_BFR_DIS          ') As Vat_Amt_Bfr_Dis
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL2_VAT     ') As Vat_Amt_Dis_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL3_VAT     ') As Vat_Amt_Dis_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_DTL_VAT      ') As Vat_Amt_Dis_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_DIS_MST_VAT      ') As Vat_Amt_Dis_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_AMT_OTHR             ') As Vat_Amt_Othr
                               ,Extractvalue (Value (Xmldtldmy), '*/VAT_PER                  ') As Vat_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT                  ') As Dis_Amt
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_AFTR_VAT         ') As Dis_Amt_Aftr_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL              ') As Dis_Amt_Dtl
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2             ') As Dis_Amt_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL2_VAT         ') As Dis_Amt_Dtl2_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3             ') As Dis_Amt_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL3_VAT         ') As Dis_Amt_Dtl3_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_VAT          ') As Dis_Amt_Dtl_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST              ') As Dis_Amt_Mst
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_MST_VAT          ') As Dis_Amt_Mst_Vat
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER                  ') As Dis_Per
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER2                 ') As Dis_Per2
                               ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER3                 ') As Dis_Per3
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_NO_REF               ') As Doc_No_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO                  ') As RCRD_NO
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE             ') As DOC_SEQUENCE
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SEQUENCE_REF          ') As Doc_Sequence_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_SER_REF               ') As Doc_Ser_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/DOC_TYPE_REF              ') As Doc_Type_Ref
                               ,Extractvalue (Value (Xmldtldmy), '*/RCRD_NO_REF               ') As RCRD_NO_REF                               
                               ,Extractvalue (Value (Xmldtldmy), '*/EXTERNAL_POST             ') As External_Post
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL1                ') As Field_Dtl1
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL2                ') As Field_Dtl2
                               ,Extractvalue (Value (Xmldtldmy), '*/FIELD_DTL3                ') As Field_Dtl3
                               ,Extractvalue (Value (Xmldtldmy), '*/F_TIME                    ') As F_Time
                               ,Extractvalue (Value (Xmldtldmy), '*/T_TIME                    ') As T_Time
                               ,Extractvalue (Value (Xmldtldmy), '*/ITEM_DESC                 ') As Item_Desc
                               ,Extractvalue (Value (Xmldtldmy), '*/I_WIDTH                   ') As I_Width
                               ,Extractvalue (Value (Xmldtldmy), '*/I_HEIGHT                  ') As I_Height
                               ,Extractvalue (Value (Xmldtldmy), '*/I_LENGTH                  ') As I_Length
                               ,Extractvalue (Value (Xmldtldmy), '*/I_NUMBER                  ') As I_Number
                               ,Extractvalue (Value (Xmldtldmy), '*/ARGMNT_NO                 ') As Argmnt_No 
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_QTY                    ') As WT_QTY 
                               ,Extractvalue (Value (Xmldtldmy), '*/WT_UNT                    ') As WT_UNT                                
                               ,Extractvalue (Value (Xmldtldmy), '*/REC_ATTCH                 ') As Rec_Attch
                               ,Extractvalue (Value (Xmldtldmy), '*/RESERVED                  ') As Reserved
                               ,Extractvalue (Value (Xmldtldmy), '*/RES_DATE                  ') As Res_Date
                               ,Extractvalue (Value (Xmldtldmy), '*/RES_QTY                   ') As Res_Qty
                               ,Extractvalue (Value (Xmldtldmy), '*/LEV_NO                    ') As Lev_No
                               ,Extractvalue (Value (Xmldtldmy), '*/PRM_GRP_NO                ') As PRM_GRP_No
                                ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_RCRD_NO           ') As QT_PRM_RCRD_NO
                                ,Extractvalue (Value (Xmldtldmy), '*/QT_PRM_SER               ') As QT_PRM_SER
                                ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_QT_PRM       ') As Dis_Amt_Dtl_Qt_Prm
                                ,Extractvalue (Value (Xmldtldmy), '*/DIS_AMT_DTL_QT_PRM_VAT   ') As Dis_Amt_Dtl_Qt_Prm_Vat
                                ,Extractvalue (Value (Xmldtldmy), '*/DIS_PER_QT_PRM          ') As Dis_Per_Qt_Prm
                           From Table (Xmlsequence (Extract (V_Xml_Type, '/QUOT/QUOTATION_DETAIL'))) Xmldtldmy)
            Loop                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 --(12)
               ---------------------
               V_DOC_SEQ:=NULL;
               V_Rcrd_No:=Null;
               V_Icode  :=Null;
               V_Itm_Unt:=Null;
               V_Barcode:=Null;
               
                Ias_Itm_Pkg.Get_I_Code (P_Barcode => D_Cv.I_Code, P_I_Code => V_Icode, P_Itm_Unt => V_Itm_Unt);
                If V_Icode Is  Null  Or nvl(V_Icode,'0')=Nvl(D_Cv.I_Code,'0') Then                                  
                  V_Icode  := D_Cv.I_Code;
                  V_Itm_Unt:=D_Cv.Itm_Unt;
                  V_Barcode:=D_Cv.Barcode;
                Else
                    V_Barcode:=D_Cv.I_Code;  
                End If;
               
               /*If D_cv.Qt_prm_ser Is Not Null And Ias_qt_prm_pkg.Ias_get_qt_prm_type ( P_qt_ser=>D_cv.Qt_prm_ser) =3 Then
                   V_dis_per_qt_prm         := D_cv.Dis_per_qt_prm;
                   V_dis_amt_dtl_qt_prm     := D_cv.Dis_amt_dtl_qt_prm;
                   V_dis_amt_dtl_qt_prm_vat := D_cv.Dis_amt_dtl_qt_prm_vat;
               End If;*/
               
               Begin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              --(2)
                  Ars_Api_Trns_Pkg.Insrt_QUOTATION_DETAIL (P_I_Code             => V_Icode
                                     ,P_Itm_Unt                => V_Itm_Unt
                                     ,P_I_Qty                  => D_Cv.I_Qty
                                     ,P_P_Qty                  => D_Cv.P_Qty
                                     ,P_P_Size                 => D_Cv.P_Size
                                     ,P_Free_Qty               => D_Cv.Free_Qty
                                     ,P_Barcode                => V_Barcode
                                     ,P_Batch_No               => D_Cv.Batch_No
                                     ,P_Expire_Date            => TO_DATE(D_Cv.Expire_Date,'DD/MM/RRRR') 
                                     ,P_W_Code                 => D_Cv.W_Code
                                     ,P_Cc_Code                => D_Cv.Cc_Code
                                     ,P_Actv_No                => D_Cv.Actv_No
                                     ,P_Pj_No                  => D_Cv.Pj_No
                                     ,P_I_Price                => D_Cv.I_Price
                                     ,P_I_Price_Vat            => D_Cv.I_Price_Vat
                                     ,P_Measur_Price           => D_Cv.Measur_Price
                                     ,P_Othr_Amt               => D_Cv.Othr_Amt
                                     ,P_Othr_Amt_Disc          => D_Cv.Othr_Amt_Disc
                                     ,P_Vat_Amt                => D_Cv.Vat_Amt
                                     ,P_Vat_Amt_Aftr_Dis       => D_Cv.Vat_Amt_Aftr_Dis
                                     ,P_Vat_Amt_Bfr_Dis        => D_Cv.Vat_Amt_Bfr_Dis
                                     ,P_Vat_Amt_Dis_Dtl2_Vat   => D_Cv.Vat_Amt_Dis_Dtl2_Vat
                                     ,P_Vat_Amt_Dis_Dtl3_Vat   => D_Cv.Vat_Amt_Dis_Dtl3_Vat
                                     ,P_Vat_Amt_Dis_Dtl_Vat    => D_Cv.Vat_Amt_Dis_Dtl_Vat
                                     ,P_Vat_Amt_Dis_Mst_Vat    => D_Cv.Vat_Amt_Dis_Mst_Vat
                                     ,P_Vat_Amt_Othr           => D_Cv.Vat_Amt_Othr
                                     ,P_Vat_Per                => D_Cv.Vat_Per
                                     ,P_Dis_Amt                => D_Cv.Dis_Amt
                                     ,P_Dis_Amt_Aftr_Vat       => D_Cv.Dis_Amt_Aftr_Vat
                                     ,P_Dis_Amt_Dtl            => D_Cv.Dis_Amt_Dtl
                                     ,P_Dis_Amt_Dtl2           => D_Cv.Dis_Amt_Dtl2
                                     ,P_Dis_Amt_Dtl2_Vat       => D_Cv.Dis_Amt_Dtl2_Vat
                                     ,P_Dis_Amt_Dtl3           => D_Cv.Dis_Amt_Dtl3
                                     ,P_Dis_Amt_Dtl3_Vat       => D_Cv.Dis_Amt_Dtl3_Vat
                                     ,P_Dis_Amt_Dtl_Vat        => D_Cv.Dis_Amt_Dtl_Vat
                                     ,P_Dis_Amt_Mst            => D_Cv.Dis_Amt_Mst
                                     ,P_Dis_Amt_Mst_Vat        => D_Cv.Dis_Amt_Mst_Vat
                                     ,P_Dis_Per                => D_Cv.Dis_Per
                                     ,P_Dis_Per2               => D_Cv.Dis_Per2
                                     ,P_Dis_Per3               => D_Cv.Dis_Per3
                                     ,P_Doc_No_Ref             => D_Cv.Doc_No_Ref
                                     ,P_Doc_Sequence           => V_DOC_SEQ
                                     ,P_Rcrd_No                => V_Rcrd_No
                                     ,P_Doc_Sequence_Ref       => D_Cv.Doc_Sequence_Ref
                                     ,P_Doc_Ser_Ref            => D_Cv.Doc_Ser_Ref
                                     ,P_Doc_Type_Ref           => D_Cv.Doc_Type_Ref
                                     ,P_Rcrd_No_Ref            => D_Cv.Rcrd_No_Ref                                     
                                     ,P_Field_Dtl1             => D_Cv.Field_Dtl1
                                     ,P_Field_Dtl2             => D_Cv.Field_Dtl2
                                     ,P_Field_Dtl3             => D_Cv.Field_Dtl3
                                     ,P_F_Time                 => D_Cv.F_Time
                                     ,P_T_Time                 => D_Cv.T_Time
                                     ,P_Item_Desc              => D_Cv.Item_Desc
                                     ,P_I_Width                => D_Cv.I_Width
                                     ,P_I_Height               => D_Cv.I_Height
                                     ,P_I_Length               => D_Cv.I_Length
                                     ,P_I_Number               => D_Cv.I_Number
                                     ,P_Argmnt_No              => D_Cv.Argmnt_No   
                                     ,P_Wt_Qty                 => D_Cv.Wt_Qty   
                                     ,P_Wt_Unt                 => D_Cv.Wt_Unt                                   
                                     ,P_Rec_Attch              => D_Cv.Rec_Attch
                                     ,P_Reserved               => D_Cv.Reserved
                                     ,P_Res_Date               => D_Cv.Res_Date
                                     ,P_Res_Qty                => D_Cv.Res_Qty
                                     ,P_Lev_No                  =>D_cv.Lev_No
                                     ,P_PRM_GRP_NO              => D_Cv.PRM_GRP_NO
                                      ,P_QT_PRM_RCRD_NO           => D_Cv.QT_PRM_RCRD_NO
                                      ,P_QT_PRM_SER               => D_Cv.QT_PRM_SER
                                      ,P_Dis_Amt_Dtl_Qt_Prm       => V_Dis_Amt_Dtl_Qt_Prm
                                      ,P_Dis_Amt_Dtl_Qt_Prm_Vat   => V_Dis_Amt_Dtl_Qt_Prm_Vat
                                      ,P_Dis_Per_Qt_Prm            => V_Dis_Per_Qt_Prm
                                     ,P_Msg_Txt                => P_Msg_Txt
                                     ,P_ERR_NO               => P_Err_No
                                     ,P_Pkg_NM                 => P_Pkg_Nm);
                    If P_Msg_Txt Is Not Null Then                  
                      Goto Rtn_Rslt;
                    End If ;              
               Exception
                  When Others Then                   
                     Raise_Application_Error (-20633, 'Err. When Insert QUOTATION_DETAIL DOC_NO= ' || V_Doc_No || ' ' || Chr (10) || Sqlerrm);
               End;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               --(2)
            --##------------------------------------------------------------------------------------------------------------------------------##--
             For Tax_Mvmnt_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As Bill_Doc_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As Doc_Jv_Type
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As Tax_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As Clc_Typ_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As Agncy_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                      ') As I_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                     ') As Itm_Unt
                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                      ') As P_Size
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_PRICE                     ') As I_Price
                                      ,Extractvalue( Value( Xmldtldmy), '*/DISC_AMT                    ') As Disc_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                    ') As A_Cy
                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As Ac_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As Tax_Prcnt
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As Tax_Amt
                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                      ') As W_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As Cc_Code
                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As Pj_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As Actv_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As Rcrd_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As Doc_Sequence
                                      ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As Tax_Amt_L
                                      ,Extractvalue( Value( Xmldtldmy), '*/I_QTY                       ') As I_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/FREE_QTY                    ') As Free_Qty
                                      ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As Ref_No
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_COST                    ') As Stk_Cost
                                      ,Extractvalue( Value( Xmldtldmy), '*/STK_RATE                    ') As Stk_Rate
                                      ,Extractvalue( Value( Xmldtldmy), '*/CLC_TAX_FREE_QTY_FLG        ') As Clc_Tax_Free_Qty_Flg
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/QUOT/GNR_TAX_ITM_MOVMNT'))) Xmldtldmy                                                                      
                                   )                              
               Loop
                   IF NVL(Tax_Mvmnt_Cv.I_CODE,'0')=NVL(D_CV.I_CODE,'0')  AND NVL(Tax_Mvmnt_Cv.ITM_UNT,'0')=NVL(D_CV.ITM_UNT,'0')
                     AND NVL(Tax_Mvmnt_Cv.RCRD_NO,0)=NVL(D_CV.RCRD_NO,0) THEN    
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Gnr_Tax_Itm_Movmnt(P_Doc_Typ                => 52
                                                     ,P_Bill_Doc_Type          => Ars_Api_Trns_Pkg.G_Bill_Doc_Type
                                                     ,P_Doc_Jv_Type            => Ars_Api_Trns_Pkg.G_QT_TYPE--Tax_Mvmnt_Cv.Doc_Jv_Type
                                                     ,P_Tax_No                 => Tax_Mvmnt_Cv.Tax_No
                                                     ,P_Clc_Typ_No             => Tax_Mvmnt_Cv.Clc_Typ_No
                                                     ,P_Agncy_No               => Tax_Mvmnt_Cv.Agncy_No
                                                     ,P_I_Code                 => V_Icode
                                                     ,P_Itm_Unt                => V_Itm_Unt
                                                     ,P_P_Size                 => Tax_Mvmnt_Cv.P_Size
                                                     ,P_I_Price                => Tax_Mvmnt_Cv.I_Price
                                                     ,P_Disc_Amt               => Tax_Mvmnt_Cv.Disc_Amt
                                                     ,P_A_Code                 => Tax_Mvmnt_Cv.A_Code
                                                     ,P_Cur_Code               => Tax_Mvmnt_Cv.A_Cy
                                                     ,P_Ac_Rate                => Tax_Mvmnt_Cv.Ac_Rate
                                                     ,P_Tax_Prcnt              => Tax_Mvmnt_Cv.Tax_Prcnt
                                                     ,P_Tax_Amt                => Tax_Mvmnt_Cv.Tax_Amt
                                                     ,P_W_Code                 => Ars_Api_Trns_Pkg.G_W_Code
                                                     ,P_Cc_Code                => Ars_Api_Trns_Pkg.G_Cc_Code
                                                     ,P_Pj_No                  => Ars_Api_Trns_Pkg.G_Pj_No
                                                     ,P_Actv_No                => Ars_Api_Trns_Pkg.G_Actv_No
                                                     ,P_Rcrd_No                => V_Rcrd_No
                                                     ,P_Doc_Sequence           => V_Doc_Seq
                                                     ,P_Tax_Amt_L              => Tax_Mvmnt_Cv.Tax_Amt_L
                                                     ,P_I_Qty                  => Tax_Mvmnt_Cv.I_Qty
                                                     ,P_Free_Qty               => Tax_Mvmnt_Cv.Free_Qty
                                                     ,P_Ref_No                 => Tax_Mvmnt_Cv.Ref_No
                                                     ,P_Stk_Cost               => Tax_Mvmnt_Cv.Stk_Cost
                                                     ,P_Stk_Rate               => Tax_Mvmnt_Cv.Stk_Rate
                                                     ,P_Clc_Tax_Free_Qty_Flg   => Tax_Mvmnt_Cv.Clc_Tax_Free_Qty_Flg
                                                     ,P_Msg_Txt                => P_Msg_Txt
                                                     ,P_ERR_NO               => P_Err_No
                                                     ,P_Pkg_Nm                 => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then
                       -- ---Rollback;
                        Raise_Application_Error( -20634, 'ERR WHEN INSERT INSRT_GNR_TAX_ITM_MOVMNT DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                    End;
                 END IF; 
               End Loop;            
            --##---------------------------------------------------------------------------------------------------------------------------##--             
            End Loop;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            --(12)          
            --##---------------------------------------------------------------------------------------------------------------------------##--
            --##INSERT OTHER CHARGE
               For Othr_Chrg_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As Doc_Typ
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                        ') As Sc_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                       ') As A_Code
                                          ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                     ') As A_Cy
                                          ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                      ') As Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/PER                          ') As Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/AMT                          ') As Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/INV_ITEM                     ') As Inv_Item
                                          ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                      ') As Rcrd_No
                                          ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                      ') As Bill_Py
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_AMT                      ') As Vat_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/VAT_PER                      ') As Vat_Per
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AMT                       ') As Sc_Amt
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_AC_RATE                   ') As Sc_Ac_Rate
                                          ,Extractvalue( Value( Xmldtldmy), '*/SC_A_CY                      ') As Sc_A_Cy
                                      From Table( Xmlsequence( Extract( V_Xml_Type, '/QUOT/OTHER_CHARGES'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Other_Charges(P_Doc_Typ      => 52
                                        ,P_Bill_Doc_Type   => Ars_Api_Trns_Pkg.G_Bill_Doc_Type
                                         ,P_BILL_TYPE   =>52
                                        ,P_Sc_No        => Othr_Chrg_Cv.Sc_No
                                        ,P_A_Code       => Othr_Chrg_Cv.A_Code
                                        ,P_Cur_Code     => Othr_Chrg_Cv.A_Cy
                                        ,P_Ac_Rate      => Othr_Chrg_Cv.Ac_Rate
                                        ,P_Per          => Othr_Chrg_Cv.Per
                                        ,P_Amt          => Othr_Chrg_Cv.Amt
                                        ,P_Inv_Item     => Othr_Chrg_Cv.Inv_Item
                                        ,P_Rcrd_No      => Othr_Chrg_Cv.Rcrd_No
                                        ,P_Bill_Py      => Othr_Chrg_Cv.Bill_Py
                                        ,P_Vat_Amt      => Othr_Chrg_Cv.Vat_Amt
                                        ,P_Vat_Per      => Othr_Chrg_Cv.Vat_Per
                                        ,P_Sc_Amt       => Othr_Chrg_Cv.Sc_Amt
                                        ,P_Sc_Ac_Rate   => Othr_Chrg_Cv.Sc_Ac_Rate
                                        ,P_Sc_A_Cy      => Othr_Chrg_Cv.Sc_A_Cy
                                        ,P_Msg_Txt      => P_Msg_Txt
                                        ,P_ERR_NO     => P_Err_No
                                        ,P_Pkg_Nm       => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                      ---  ---Rollback;
                        Raise_Application_Error( -20635, 'ERR WHEN INSERT OTHER_CHARGES DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
         --##INSERT OTHER CHARGE ITEMS
               For Othr_Chrg_Itm_Cv In (Select Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                    ') As Doc_Typ
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SC_NO                      ') As Sc_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                     ') As A_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                   ') As A_Cy
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                    ') As Ac_Rate
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PER                        ') As Per
                                                      ,Extractvalue( Value( Xmldtldmy), '*/AMT                        ') As Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/W_CODE                     ') As W_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                    ') As Cc_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                      ') As Pj_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                    ') As Actv_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                    ') As Rcrd_No
                                                      ,Extractvalue( Value( Xmldtldmy), '*/SI_TYPE                    ') As Si_Type
                                                      ,Extractvalue( Value( Xmldtldmy), '*/I_CODE                     ') As I_Code
                                                      ,Extractvalue( Value( Xmldtldmy), '*/ITM_UNT                    ') As Itm_Unt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/P_SIZE                     ') As P_Size
                                                      ,Extractvalue( Value( Xmldtldmy), '*/BILL_PY                    ') As Bill_Py
                                                      ,Extractvalue( Value( Xmldtldmy), '*/UNIT_AMT                   ') As Unit_Amt
                                                      ,Extractvalue( Value( Xmldtldmy), '*/POST_CODE                  ') As Post_Code
                                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/QUOT/OTHER_CHARGES_ITEMS'))) Xmldtldmy)
                       Loop
                          Begin
                             Ars_Api_Trns_Pkg.Insrt_Other_Charges_Items(P_Doc_Typ     => 52
                                                      ,P_Sc_No       => Othr_Chrg_Itm_Cv.Sc_No
                                                      ,P_A_Code      => Othr_Chrg_Itm_Cv.A_Code
                                                      ,P_Cur_Code    => Othr_Chrg_Itm_Cv.A_Cy
                                                      ,P_Ac_Rate     => Othr_Chrg_Itm_Cv.Ac_Rate
                                                      ,P_Per         => Othr_Chrg_Itm_Cv.Per
                                                      ,P_Amt         => Othr_Chrg_Itm_Cv.Amt
                                                      ,P_W_Code      => Othr_Chrg_Itm_Cv.W_Code
                                                      ,P_Cc_Code     => Othr_Chrg_Itm_Cv.Cc_Code
                                                      ,P_Pj_No       => Othr_Chrg_Itm_Cv.Pj_No
                                                      ,P_Actv_No     => Othr_Chrg_Itm_Cv.Actv_No
                                                      ,P_Rcrd_No     => Othr_Chrg_Itm_Cv.Rcrd_No
                                                      ,P_Si_Type     => Othr_Chrg_Itm_Cv.Si_Type
                                                      ,P_I_Code      => Othr_Chrg_Itm_Cv.I_Code
                                                      ,P_Itm_Unt     => Othr_Chrg_Itm_Cv.Itm_Unt
                                                      ,P_P_Size      => Othr_Chrg_Itm_Cv.P_Size
                                                      ,P_Bill_Py     => Othr_Chrg_Itm_Cv.Bill_Py
                                                      ,P_Unit_Amt    => Othr_Chrg_Itm_Cv.Unit_Amt
                                                      ,P_Post_Code   => Othr_Chrg_Itm_Cv.Post_Code
                                                      ,P_Msg_Txt     => P_Msg_Txt
                                                      ,P_ERR_NO    => P_Err_No
                                                      ,P_Pkg_Nm      => P_Pkg_Nm);

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                          Exception
                             When Others Then
                               -- ---Rollback;
                                Raise_Application_Error( -20636, 'ERR WHEN INSERT OTHER_CHARGES_ITEMS DOC_NO= ' || V_Doc_No || ' ' || Chr( 10) || Sqlerrm);
                          End;
                       End Loop; 
         --##---------------------------------------------------------------------------------------------------------------------------##--
         For Tax_INPT_Mvmnt_Cv In (SELECT    Extractvalue( Value( Xmldtldmy), '*/DOC_TYP                     ') As DOC_TYP              
                                            ,Extractvalue( Value( Xmldtldmy), '*/BILL_DOC_TYPE               ') As BILL_DOC_TYPE         
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_JV_TYPE                 ') As DOC_JV_TYPE                                                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_NO                      ') As TAX_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CLC_TYP_NO                  ') As CLC_TYP_NO           
                                            ,Extractvalue( Value( Xmldtldmy), '*/AGNCY_NO                    ') As AGNCY_NO                                        
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_CODE                   ') As INPT_CODE            
                                            ,Extractvalue( Value( Xmldtldmy), '*/A_CODE                      ') As A_CODE               
                                            ,Extractvalue( Value( Xmldtldmy), '*/CUR_CODE                     ') As CUR_CODE                 
                                            ,Extractvalue( Value( Xmldtldmy), '*/AC_RATE                     ') As AC_RATE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/INPT_AMT                    ') As INPT_AMT             
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_PRCNT                   ') As TAX_PRCNT            
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT                     ') As TAX_AMT              
                                            ,Extractvalue( Value( Xmldtldmy), '*/TAX_AMT_L                   ') As TAX_AMT_L            
                                            ,Extractvalue( Value( Xmldtldmy), '*/CC_CODE                     ') As CC_CODE              
                                            ,Extractvalue( Value( Xmldtldmy), '*/PJ_NO                       ') As PJ_NO                
                                            ,Extractvalue( Value( Xmldtldmy), '*/ACTV_NO                     ') As ACTV_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/REF_NO                      ') As REF_NO               
                                            ,Extractvalue( Value( Xmldtldmy), '*/RCRD_NO                     ') As RCRD_NO              
                                            ,Extractvalue( Value( Xmldtldmy), '*/DOC_SEQUENCE                ') As DOC_SEQUENCE
                                  From Table( Xmlsequence( Extract( V_Xml_Type, '/QUOT/GNR_TAX_INPT_MOVMNT'))) Xmldtldmy                                  
                                   )                              
               Loop                    
                    Begin
                          Ars_Api_Trns_Pkg.INSRT_GNR_TAX_INPT_MOVMNT(
                                            P_DOC_TYP                    =>52
                                           ,P_BILL_DOC_TYPE              =>Ars_Api_Trns_Pkg.G_BILL_DOC_TYPE
                                           ,P_DOC_JV_TYPE                =>Ars_Api_Trns_Pkg.G_QT_TYPE                                       
                                           ,P_TAX_NO                     =>Tax_INPT_Mvmnt_Cv.TAX_NO
                                          , P_CLC_TYP_NO                 =>Tax_INPT_Mvmnt_Cv.CLC_TYP_NO 
                                          , P_AGNCY_NO                   =>Tax_INPT_Mvmnt_Cv.AGNCY_NO                            
                                          , P_INPT_CODE                  =>Tax_INPT_Mvmnt_Cv.INPT_CODE 
                                           ,P_A_CODE                     =>Tax_INPT_Mvmnt_Cv.A_CODE 
                                          , P_A_CY                       =>Tax_INPT_Mvmnt_Cv.CUR_CODE
                                          , P_AC_RATE                    =>Tax_INPT_Mvmnt_Cv.AC_RATE 
                                          , P_INPT_AMT                   =>Tax_INPT_Mvmnt_Cv.INPT_AMT 
                                          , P_TAX_PRCNT                  =>Tax_INPT_Mvmnt_Cv.TAX_PRCNT 
                                          , P_TAX_AMT                    =>Tax_INPT_Mvmnt_Cv.TAX_AMT
                                          , P_TAX_AMT_L                  =>Tax_INPT_Mvmnt_Cv.TAX_AMT_L 
                                           ,P_CC_CODE                    =>Ars_Api_Trns_Pkg.G_CC_CODE 
                                          , P_PJ_NO                      =>Ars_Api_Trns_Pkg.G_PJ_NO 
                                          , P_ACTV_NO                    =>Ars_Api_Trns_Pkg.G_ACTV_NO 
                                          , P_REF_NO                     =>Tax_INPT_Mvmnt_Cv.REF_NO 
                                          , P_RCRD_NO                    =>Tax_INPT_Mvmnt_Cv.RCRD_NO 
                                          , P_DOC_SEQUENCE               =>Tax_INPT_Mvmnt_Cv.DOC_SEQUENCE
                                          ,P_Msg_Txt                     =>P_Msg_Txt
                                          ,P_ERR_NO                     =>P_ERR_NO
                                          ,P_Pkg_NM                     =>P_Pkg_NM); 

                             If P_Msg_Txt Is Not Null Then
                                Goto Rtn_Rslt;
                             End If;
                            
                    Exception
                     When Others Then
                       -- ---Rollback;
                        Raise_Application_Error( -20637, 'ERR WHEN INSERT INSRT_GNR_TAX_INPT_MOVMNT DOC_NO= ' || V_DOC_NO || ' ' || Chr( 10) || Sqlerrm);
                    End;                 
               End Loop;
       --##---------------------------------------------------------------------------------------------------------------------------##--
            For Attach_Cv
                  In (Select Extractvalue (Value (Xmldtldmy), '*/FILE_NAME         ') As File_Name
                        From Table (Xmlsequence (Extract (V_Xml_Type, '/QUOT/ATTACH'))) Xmldtldmy)
               Loop
                  Begin
                     Ars_Api_Trns_Pkg.Insrt_Archives (P_Doc_Typ     => Ars_Api_Trns_Pkg.G_Doc_Typ
                                                     ,P_Doc_Ser     => Ars_Api_Trns_Pkg.G_Doc_Ser
                                                     ,P_File_Name   => Attach_Cv.File_Name
                                                     ,P_Msg_Txt     => P_Msg_Txt
                                                     ,P_Err_No      => P_Err_No
                                                     ,P_Pkg_Nm      => P_Pkg_Nm);

                     If P_Msg_Txt Is Not Null Then
                        Goto Rtn_Rslt;
                     End If;
                  Exception
                     When Others Then
                        Raise_Application_Error (-20719,'Err.in Ars_Api_Trns_Pkg.INSRT_ARCHIVES= '|| V_Doc_No|| ' '|| Chr (10)|| Sqlerrm);
                  End;
               End Loop;
         --##---------------------------------------------------------------------------------------------------------------------------##--
          
            --## CHK INSERT DATA
            Ars_Api_Trns_Pkg.Chk_Insrt_Data (P_Doc_Typ    => 52
                           ,P_Doc_Ser    => Ars_Api_Trns_Pkg.G_Doc_Ser
                           ,P_Msg_Txt    => P_Msg_Txt
                           ,P_ERR_NO   => P_Err_No
                           ,P_Pkg_NM   => P_Pkg_Nm);
              If P_Msg_Txt Is Not Null Then                 
                  Goto Rtn_Rslt;
              End If ;                                    
         ----------------------------------------------------------------------------------------------------------
         End Loop;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        --(11)
      End If;
      --------------------------------------------------------------                         
     --####################--
     <<RTN_RSLT>>
      If P_Msg_Txt Is Not Null OR P_Err_No IS NOT NULL Then
         Rollback;
         P_Msg_Txt := NVL(P_Msg_Txt,'Message Number Is Missing') ;
         P_ERR_NO := P_Err_No;
         P_Pkg_NM := NVL(P_Pkg_Nm,'Ars_Api_Trns_Pkg.INSRT_DOC_BY_XML');
         P_XML    :=NULL;
         RETURN;
      ELSE
         P_Msg_Txt  := NULL ;
         P_ERR_NO   := NULL;
         P_Pkg_NM   := NULL;
         P_XML      :=NULL;
         ------------------------------------------        
         
         IF NVL(P_COMMIT_FLG,0)=1 THEN
            P_XML    :=NULL;
            COMMIT;
             Ars_Api_Trns_Pkg.SYNC_E_INVC_PRC(  P_DOC_TYPE      =>Ars_Api_Trns_Pkg.G_DOC_TYP,
                                                P_BILL_TYPE      =>Ars_Api_Trns_Pkg.G_BILL_DOC_TYPE,
                                                P_BRN_NO         =>Ars_Api_Trns_Pkg.G_BRN_NO,
                                                P_Use_Vat        =>Ars_Api_Trns_Pkg.G_Use_Vat,
                                                P_SYS_NO         =>Ars_Api_Trns_Pkg.G_SYS_NO,
                                                P_DOC_SER        =>Ars_Api_Trns_Pkg.G_DOC_SER,
                                                P_C_CODE         =>Ars_Api_Trns_Pkg.G_C_CODE,                           
                                                P_TAX_BILL_TYP   =>Ars_Api_Trns_Pkg.G_TAX_BILL_TYP,    
                                                P_OFFLINE_VLDT   =>0,
                                                P_DO_COMMIT      =>0, 
                                                P_Tbl_Mst_Nm     =>Ars_Api_Trns_Pkg.G_Tbl_Mst_Nm,
                                                P_Fld_Doc_Ser    =>Ars_Api_Trns_Pkg.G_Fld_Doc_Ser,                                        
                                                P_DTS_ONLINE     =>Ars_Api_Trns_Pkg.G_DTS_ONLINE,
                                                P_COMMIT_FLG     =>Ars_Api_Trns_Pkg.G_COMMIT_FLG, 
                                                P_Pst_Typ        =>Ars_Api_Trns_Pkg.G_Pst_Typ,
                                                P_WEB_SRVC_UUID  =>Ars_Api_Trns_Pkg.G_DOC_UUID,                             
                                                P_WRNNG_TXT      =>Ars_Api_Trns_Pkg.G_WRNNG_TXT,
                                                P_Msg_Txt        =>P_Msg_Txt,
                                                P_ERR_NO         =>P_ERR_NO,
                                                P_Pkg_NM         =>P_Pkg_NM);
              Ars_Api_Trns_Pkg.G_WRNNG_TXT:=NVL(P_Msg_Txt||Ars_Api_Trns_Pkg.G_WRNNG_TXT,Ars_Api_Trns_Pkg.G_ALRT_MSG_TXT);
              Ars_Api_Trns_Pkg.G_WRNNG_TXT:=Replace( Ars_Api_Trns_Pkg.G_WRNNG_TXT,'"',' ');
                Ars_Api_Trns_Pkg.G_WRNNG_TXT:=Replace( Ars_Api_Trns_Pkg.G_WRNNG_TXT,':',' ');
                Ars_Api_Trns_Pkg.G_WRNNG_TXT:=Replace( Ars_Api_Trns_Pkg.G_WRNNG_TXT,',',' ');
                Ars_Api_Trns_Pkg.G_WRNNG_TXT:=Replace( Ars_Api_Trns_Pkg.G_WRNNG_TXT,'''',' ');
              P_Msg_Txt:=NULL;
              P_ERR_NO :=NULL;
              P_Pkg_NM:=NULL;
              --##----------------------------------------------------------------------------------------##--
                  --# SEND SMS MESSEGE
                  SND_ALRT_SAVE_DOC_PRC   (  P_SYS_NO      =>Ars_Api_Trns_Pkg.G_SYS_NO ,
                                             P_DOC_TYP     =>Ars_Api_Trns_Pkg.G_Doc_Typ,  
                                             P_DOC_SER     =>Ars_Api_Trns_Pkg.G_Doc_Ser ,                                                                
                                             P_SCHMA_NM    =>Ars_Api_Trns_Pkg.G_SCHMA_NM,                                   
                                             P_U_ID        =>Ars_Api_Trns_Pkg.G_Ad_U_Id,                                    
                                             P_DTS_ONLINE  =>Ars_Api_Trns_Pkg.G_DTS_ONLINE,
                                             P_COMMIT_FLG  =>Ars_Api_Trns_Pkg.G_COMMIT_FLG,
                                             P_Pst_Typ    =>Ars_Api_Trns_Pkg.G_Pst_Typ,                        
                                             P_LNG_NO      =>Ars_Api_Trns_Pkg.G_Lng_No
                                           );
                   
             
          ELSE
          ----------------------------------------------------------
            Rollback;
            IF NVL(P_CLC_TAX_METHOD,0)=1 THEN                                               
              P_XML:=Ars_Api_Trns_Pkg.G_DOC_AMT_XML;
             ELSE
                P_XML    :=NULL;
             END IF;             
            ----------------------------------------------------------                          
          END IF;
         
       END IF;      
      --####################--
      Null;
   Exception
      When Others Then
      ROLLBACK;
      P_Msg_Txt := 'Error in INSRT_DOC_BY_XML ' || Chr(10) || Sqlerrm;
      P_Err_No := 20317;
      P_Pkg_Nm := Nvl (P_Pkg_Nm, 'Ars_Api_Trns_Pkg.INSRT_DOC_BY_XML');
      -- Raise_Application_Error (-20317, 'Err IN INSRT_DOC_BY_XML' || Chr (10) || Sqlerrm);  
   End INSRT_DOC_BY_XML;

   --##----------------------------------------------------------------------------------------------------------------------##--
   

 Procedure Check_Duplicate (  P_Sys_No        IN   NUMBER, 
                              P_DOC_TYP       IN   NUMBER,
                              P_Pst_Typ       IN   NUMBER DEFAULT NULL,
                              P_Doc_Ser       IN   NUMBER DEFAULT NULL,  
                              P_Bill_Doc_Type  IN   NUMBER DEFAULT NULL,      
                              P_BRN_YEAR      IN   NUMBER,
                              P_BRN_NO        IN   S_BRN.BRN_NO%TYPE ,
                              P_CC_CODE       IN   COST_CENTERS.CC_CODE%TYPE DEFAULT NULL,
                              P_W_CODE        IN   WAREHOUSE_DETAILS.W_CODE%TYPE DEFAULT NULL,
                              P_TYP_NO        IN   NUMBER ,
                              P_DOC_NO        IN   NUMBER  ,                           
                              P_Usr_No        In User_R.U_Id%Type  Default Null,
                              P_Trmnl_No      In Number            Default Null,
                              P_Lng_No       In User_R.U_Id%Type  Default Null,                       
                              P_Msg_Txt      Out Varchar2,
                              P_Err_No       Out Varchar2,
                              P_Pkg_Nm       Out Varchar2)
Is
   V_Cnt             Number;
   V_Msg_No          Number;
   V_Doc_Type        Number;
   V_Bill_Doc_Type   Number;
   V_Typ_No          Number;
Begin
   If P_Doc_Typ Is Null Then
      P_Err_No    := 20149;
      P_Msg_Txt   := 'DOC_TYP IS NULL';
      Goto Rtn_Rslt;
   End If;

   If P_Doc_No Is Null Then
      P_Err_No    := 20150;
      P_Msg_Txt   := 'DOC_NO IS NULL';
      Goto Rtn_Rslt;
   End If;
 

   -----------------------------------------------------
   If p_Doc_Ser Is Null Then
      P_Err_No    := 20096;
      P_Msg_Txt   := ' DOC_SER IS NULL ';
      Goto Rtn_Rslt;
   End If;

   -------------------------------------------------
   If P_Sys_No = 70 Then
      If P_Doc_Typ = 53 Then
         Begin
            Select 1
              Into V_Cnt
              From Sales_Order
             Where Order_Ser = P_Doc_Ser And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If V_Cnt > 0 Then
            P_Err_No    := 20392;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169);
            Goto Rtn_Rslt;
         End If;
      ELSIf P_Doc_Typ = 52 Then
         Begin
            Select 1
              Into V_Cnt
              From QUOTATION
             Where QUOT_Ser = P_Doc_Ser And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If V_Cnt > 0 Then
            P_Err_No    := 20599;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169);
            Goto Rtn_Rslt;
         End If;   
      ELSIf P_Doc_Typ = 136 Then
         Begin
            Select 1
              Into V_Cnt
              From Ias_Rt_Bill_MST_RQ
             Where RT_BILL_SER = P_Doc_Ser And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If V_Cnt > 0 Then
            P_Err_No    := 20554;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169);
            Goto Rtn_Rslt;
         End If;   
      Elsif P_Doc_Typ = 4 Then
           If Nvl(P_Pst_Typ,0) = 1 Then
                 Begin
                    Select 1
                      Into V_Cnt
                      From (Select Bill_Ser
                              From Ias_Bill_Mst
                             Where Bill_Ser = P_Doc_Ser
                            Union All
                            Select Bill_Ser
                              From Ias_Bill_Mst_Br
                             Where Bill_Ser = P_Doc_Ser)
                     Where Bill_Ser = P_Doc_Ser And Rownum <= 1;
                 Exception
                    When Others Then
                       V_Cnt   := 0;
                 End;
           Else
                 Begin
                   Select 1 Into V_Cnt
                              From Ias_Bill_Mst
                             Where Bill_Ser = P_Doc_Ser
                             And Rownum <= 1;                           
                 Exception
                    When Others Then
                       V_Cnt   := 0;
                 End;
           End If; 
         

         If V_Cnt > 0 Then
            P_Err_No    := 20393;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169);
            Goto Rtn_Rslt;
         End If;
      Elsif P_Doc_Typ = 5 Then
           If Nvl(P_Pst_Typ,0) = 1 Then
                 Begin
                    Select 1
                      Into V_Cnt
                      From (Select RT_Bill_Ser
                              From Ias_RT_Bill_Mst
                             Where RT_Bill_Ser = P_Doc_Ser
                            Union All
                            Select RT_Bill_Ser
                              From Ias_RT_Bill_Mst_Br
                             Where RT_Bill_Ser = P_Doc_Ser)
                     Where RT_Bill_Ser = P_Doc_Ser And Rownum <= 1;
                 Exception
                    When Others Then
                       V_Cnt   := 0;
                 End;
           Else
                 Begin
                   Select 1 Into V_Cnt
                              From Ias_RT_Bill_Mst
                             Where RT_Bill_Ser = P_Doc_Ser
                             And Rownum <= 1;                           
                 Exception
                    When Others Then
                       V_Cnt   := 0;
                 End;
           End If; 

         If V_Cnt > 0 Then
            P_Err_No    := 20394;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169);
            Goto Rtn_Rslt;
         End If;
      End If;      
      
   Else
      V_Msg_No      :=
         Ar_Doc_Sq_Pkg.Chk_Doc_No (P_Doc_Typ    => p_Doc_Typ
                                  ,P_Pay_Typ    => P_Bill_Doc_Type
                                  ,P_Brn_Year   => P_Brn_Year
                                  ,P_Brn_No     => P_Brn_No
                                  ,P_Cc_Code    => P_Cc_Code
                                  ,P_W_Code     => P_W_Code
                                  ,P_Typ_No     => P_Typ_No
                                  ,P_Doc_No     => P_Doc_No
                                  ,P_Sys_No      =>P_Sys_No
                                  ,P_Usr_No     =>P_Usr_No
                                 , P_Trmnl_No   =>Null);

      If V_Msg_No Is Not Null Then
        If Nvl(P_Pst_Typ,0) = 1 And Nvl(P_Sys_No,0)=185 then
            Null;
        Else      
         P_Err_No    := 20151;
         P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => V_Msg_No);
         Goto Rtn_Rslt;
        End If;   
      End If;

      -------------------------------------------------------
      If P_Doc_Typ = 53 Then
         Begin
            Select 1
              Into V_Cnt
              From Sales_Order
             Where Order_Ser = P_Doc_Ser And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If V_Cnt > 0 Then
            P_Err_No    := 20395;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169) || ' , DOC_SER ';
            Goto Rtn_Rslt;
         End If;
      ELSIf P_Doc_Typ = 52 Then
         Begin
            Select 1
              Into V_Cnt
              From QUOTATION
             Where QUOT_Ser = P_Doc_Ser And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If V_Cnt > 0 Then
            P_Err_No    := 20600;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169) || ' , DOC_SER ';
            Goto Rtn_Rslt;
         End If;
      ELSIf P_Doc_Typ = 136 Then
         Begin
            Select 1
              Into V_Cnt
              From IAS_RT_BILL_MST_RQ
             Where RT_BILL_Ser = P_Doc_Ser And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If V_Cnt > 0 Then
            P_Err_No    := 20601;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169) || ' , DOC_SER ';
            Goto Rtn_Rslt;
         End If;      
      Elsif P_Doc_Typ = 4 Then
         Begin
            Select 1
              Into V_Cnt
              From Ias_Bill_Mst
             Where Bill_Ser = P_Doc_Ser And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If V_Cnt > 0 Then
            P_Err_No    := 20396;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169);
            Goto Rtn_Rslt;
         End If;
      Elsif P_Doc_Typ = 5 Then
         Begin
            Select 1
              Into V_Cnt
              From Ias_Rt_Bill_Mst
             Where Rt_Bill_Ser = P_Doc_Ser And Rownum <= 1;
         Exception
            When Others Then
               V_Cnt   := 0;
         End;

         If V_Cnt > 0 Then
            P_Err_No    := 20397;
            P_Msg_Txt   := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 169);
            Goto Rtn_Rslt;
         End If;
      End If;
   -------------------------------------------------------
   End If;

  -----------------------------------------------------

  --####################--
  <<RTN_RSLT>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_CHK_Pkg.Check_Duplicate');
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;
   End If; 
   --####################--
Exception
   When Others Then
       P_Msg_Txt   := 'Error IN Check_Duplicate' || Chr(10) || Sqlerrm;
       P_Err_No    := 20352;
       P_Pkg_Nm    := 'Ars_Api_CHK_Pkg.Check_Duplicate';      
End Check_Duplicate;                                                    
   --##----------------------------------------------------------------------------------------------------------------------##--
   Procedure Calc_Other_Charges (P_Doc_Typ          In     Number
                             ,P_Bill_Doc_Type    In     Number
                             ,P_Doc_Ser          In     Number
                             ,P_Doc_Date         In     DATE
                             ,P_Brn_No           In     Number
                             ,P_Use_Vat          In     Number
                             ,P_Cur_Code         In     Ex_Rate.Cur_Code%Type
                             ,P_Cur_Rate         In     Number
                             ,P_Clc_Typ_No_Tax   In     Number
                             ,P_Fld_Doc_Ser      In     Varchar2
                             ,P_Fld_Mst_Amt      In     Varchar2                            
                             ,P_Tbl_Mst_Nm       In     Varchar2                             
                             ,P_No_Of_Decimal    In     Number
                             ,P_Lng_No           In     Number Default 1
                             ,P_Msg_Txt             Out Varchar2
                             ,P_Err_No              Out Varchar2
                             ,P_Pkg_Nm              Out Varchar2)
Is
   A            Number := 0;
   C            Number := 0;
   D            Number := 0;
   Cur_Rec      Number;
   V_Amt        Number;
   V_Per        Number;
   V_Vat_Amt    Number;
   V_Rcrd_No    Number := 0;
   V_Doc_Amt    Number;
   V_Disc_Amt   Number;
   V_Vat_Per    Number;
   V_Sc_Amt     Number;
   V_Sc_Ac_Rate   Number;
   V_Sc_A_Cy      varchar2(100);
Begin

IF P_Doc_Typ in(4,52,54) THEN
   Begin
      Execute Immediate 'Select ' || P_Fld_Mst_Amt || ', Disc_Amt        
                     From ' || P_Tbl_Mst_Nm || ' 
                    Where  ' || P_Fld_Doc_Ser || ' =' || P_Doc_Ser || ' ' Into V_Doc_Amt, V_Disc_Amt;
   Exception
      When Others Then
         P_Err_No    := 20440;
         P_Msg_Txt   := 'Error when  Calc_Other_Charges ' || Chr(10) || Sqlerrm;
         Goto Rtn_Rslt;
   End;

   Declare
      Cursor C1
      Is
           Select Sc_No
                 ,Sc_Name
                 ,A_Code
                 ,Calc_Type
                 ,nvl(Amt_Type, 0) Amt_Type
                 ,Nvl (Sc_Type, 1) Sc_Type
                 ,Decode (Amt_Type, 1, Decode (A_Cy, P_Cur_Code, Amt, Amt * Ac_Rate * 1 / P_Cur_Rate), Null) Amt
                 ,Decode (Amt_Type, 0, Amt, Null) Amt_Per
                 ,Vat_Per
                 ,Decode (Nvl (A_Cy, P_Cur_Code), P_Cur_Code, P_Cur_Rate, Ac_Rate) Sc_Ac_Rate
                 ,Nvl (A_Cy, P_Cur_Code) Sc_A_Cy
             From Sales_Charges
            Where Nvl (Fill_Auto, 0) = 1 
            And Nvl (Inv_Item, 0) = 0 
            And Nvl (Sc_Add_Frc_Invoice, 0) = 0 
            and nvl(INACTIVE,0)=0            
            And Nvl (Sc_Type, 0) <> 3 
            And Nvl (Diff_Cmpns_Qty_Sr, 0) = 0
            And Nvl (Bill_Doc_Type, 0) = Decode (Nvl (Bill_Doc_Type, 0), 0, 0, Nvl (P_Bill_Doc_Type, 0))
         Order By Sc_No;
   Begin
      For I In C1
      Loop
         ----------------------------------------
         If Nvl (I.Amt_Type, 0) = 1 Then --amt
            V_Amt   := I.Amt;
            V_Per   := I.Amt_Per;

            If Nvl (I.Sc_Type, 0) <> 1 Then
               If Nvl (V_Amt, 0) > 0 Then
                  V_Amt   := I.Amt * -1;
               End If;

               If Nvl (V_Per, 0) > 0 Then
                  V_Per   := I.Amt_Per * -1;
               End If;
            End If;
            
            V_Sc_Ac_Rate:=I.Sc_Ac_Rate;
            V_Sc_A_Cy   :=I.Sc_A_Cy;
            If I.Sc_A_Cy = P_Cur_Code Then
               V_Sc_Amt   := V_Amt;
            Else
               V_Sc_Amt   := (Nvl (V_Amt, 0) / Nvl (I.Sc_Ac_Rate, 1)) * Nvl (P_Cur_Rate, 1);
            End If;
         Else ---precent
            V_Amt   := Null;
            V_Sc_Amt:= Null;
            If I.A_Code Is Not Null And I.Amt_Per Is Not Null Then
               If i.Calc_Type = 0 Then -- Net Inv. amt
                  A   := Nvl (V_Doc_Amt, 0) - Nvl (V_Disc_Amt, 0);
               -- Elsif J.Calc_Type = 1 Then -- bill_amt+others
               -- A   := (Nvl (V_Bill_Amt, 0) - Nvl (V_Disc_Amt, 0)) + (Nvl ( :Other_Charges.Tot_Oc, 0) - Nvl ( :Other_Charges.Amt, 0));
               Else
                  A   := Nvl (V_Doc_Amt, 0) - Nvl (V_Disc_Amt, 0);
               End If;
               
               If nvl(i.sc_type,0)=1  Then
                 V_Amt   := ( (A * Nvl (I.Amt_Per, 0)) / 100);
                  v_per:=I.Amt_Per ;
               Else
                 V_Amt   := ( (A * Nvl (I.Amt_Per, 0)*-1) / 100);
                  v_per:=I.Amt_Per*-1; 
               End If;
                
               V_Sc_Ac_Rate:=NULL;
               V_Sc_A_Cy   :=NULL;                            
               V_Sc_Amt   := Nvl (V_Amt, 0);                                    
            End If;
         End If;

         ----------------------------------------
         If Nvl (Ys_Tax_Pkg.Get_Clc_Tax_Typ (P_Clc_Typ_No_Tax), 0) = 0 Then
            If Nvl (P_Use_Vat, 0) = 1 And To_Date (P_Doc_Date, 'DD/MM/YYYY') >= To_Date (Ys_Tax_Pkg.Get_Clc_Typ_No_Actv_Date (P_Clc_Typ_No => P_Clc_Typ_No_Tax, P_Brn_No => P_Brn_No), 'DD/MM/YYYY') Then
               If I.Sc_No Is Not Null Then
                  Begin
                     V_Vat_Per   := Ys_Tax_Pkg.Get_Inpt_Prcnt (P_Clc_Typ_No => P_Clc_Typ_No_Tax, P_Inpt_Typ => 1, P_Inpt_Code => I.Sc_No);
                  Exception
                     When Others Then
                        Null;
                  End;

                  If V_Amt Is Not Null And V_Vat_Per Is Not Null Then
                     V_Vat_Amt   := V_Amt * V_Vat_Per / 100;
                  End If;
               End If;
            End If;
         Else
            V_Vat_Per   := 0;
            V_Vat_Amt   := 0;
         End If;

         ----------------------------------------
         V_Rcrd_No   := V_Rcrd_No + 1;
         Ars_Api_Trns_Pkg.Insrt_Other_Charges (P_Doc_Typ  => P_Doc_Typ
                             ,P_Bill_Doc_Type   => P_Bill_Doc_Type
                             ,p_bill_type       => case when P_Doc_Typ=4 then 1 when P_Doc_Typ=5 then 3 else P_Doc_Typ end
                             ,P_Sc_No           => I.Sc_No
                             ,P_A_Code          => I.A_Code
                             ,P_Cur_Code        => P_Cur_Code
                             ,P_Ac_Rate         => P_Cur_Rate
                             ,P_Per             => V_Per
                             ,P_Amt             => V_Amt
                             ,P_Inv_Item        => 0
                             ,P_Rcrd_No         => V_Rcrd_No
                             ,P_Bill_Py         => 0
                             ,P_Vat_Amt         => V_Vat_Amt
                             ,P_Vat_Per         => V_Vat_Per
                             ,P_Sc_Amt          => V_Sc_Amt
                             ,P_Sc_Ac_Rate      => V_Sc_Ac_Rate
                             ,P_Sc_A_Cy         => V_Sc_A_Cy
                             ,P_Msg_Txt         => P_Msg_Txt
                             ,P_Err_No          => P_Err_No
                             ,P_Pkg_Nm          => P_Pkg_Nm);

         If P_Msg_Txt Is Not Null Then
            Goto Rtn_Rslt;
         End If;
      End Loop;
   End;
 END IF;
  --####################--
  <<RTN_RSLT>>
   If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then
      ---Rollback;
      P_Msg_Txt   := NVL(P_Msg_Txt,'Message Number Is Missing');
      P_Err_No    := P_Err_No;
      P_Pkg_Nm    := Nvl (P_Pkg_Nm, 'Ars_Api_CHK_Pkg.Insrt_Other_Charges');
      Return;
   Else
      P_Msg_Txt   := Null;
      P_Err_No    := Null;
      P_Pkg_Nm    := Null;
   End If;
--####################--
Exception
   When Others Then
      P_Msg_Txt   := 'ERROR WHEN Calc_Other_Charges' || Sqlerrm;
      P_Err_No    := 20441;
      P_Pkg_Nm    := 'Ars_Api_CHK_Pkg.Calc_Other_Charges';
End Calc_Other_Charges;
--##-----------------------------------------------------------------------------------------------------##--
Procedure Chk_Prmtr (          P_Sys_No          In       Number
                            ,  P_Doc_Typ          In      Number                            
                              ,P_COMMIT_FLG       In       NUMBER  --## 0 ROLLBACK ,1 COMMIT ,2 ,MANUAL COMMIT
                              ,P_CLC_TAX_METHOD   In       NUMBER  --## 0 CALC TAX IN EXTRNAL ,1-AOUTO CALC TAX                                                        
                              ,P_Pst_Typ          In       Number --## 1 to br tables ,2 to onyx tables
                              ,P_Pst_FROM_BR      In       Number  --## 1- POSTING FORM BR TABLE  0- NOT FROM BR
                              ,P_DTS_ONLINE       In     NUMBER DEFAULT 0 --## 0 OFFLINE ,1-ONLINE
                              ,P_Lng_No           In       Number Default 1                          
                              ,P_Msg_Txt          Out   Varchar2
                              ,P_ERR_NO           Out   Varchar2
                              ,P_Pkg_Nm           Out   Varchar2)
Is
Begin
 
If Nvl(P_Sys_No,0)=70 Then
      If NVL(P_CLC_TAX_METHOD,0)=1 and nvl(P_DTS_ONLINE,0)=0 Then
           P_Err_No    := 20684;
           P_Msg_Txt   := 'P_CLC_TAX_METHOD Must be equal 0 When App Is Offline  ';
           Goto Rtn_Rslt;    
      End If;
      
      If NVL(P_COMMIT_FLG,0)<>1 and nvl(P_DTS_ONLINE,0)=0 Then
           P_Err_No    := 20685;
           P_Msg_Txt   := 'P_COMMIT_FLG Must be equal 1 When App Is Offline  ';
           Goto Rtn_Rslt;    
      End If;      
 
End If;
 
  --##----------------------------------------------------------------------------------------------------------##--
     --####################--
     <<Rtn_Rslt>>
      If P_Msg_Txt Is Not Null OR P_Err_No Is Not Null Then         
         P_Msg_Txt := NVL(P_Msg_Txt,'Message Number Is Missing');
         P_ERR_NO := P_Err_No;
         P_Pkg_NM   :=NVL(P_Pkg_Nm,'Ars_Api_Chk_Pkg.Chk_Prmtr');
         Return;
      ELSE
       P_Msg_Txt := NULL;
       P_Err_No :=NULL;
       P_Pkg_NM   :=NULL; 
      End If;
   --####################--  
   Exception When Others then
         P_Msg_Txt := 'Error in Chk_Prmtr '||sqlerrm;
         P_ERR_NO  := 20686;
         P_Pkg_NM  :='Ars_Api_Chk_Pkg.Chk_Prmtr';    
End Chk_Prmtr; 
--##-----------------------------------------------------------------------------------------------------##--
PROCEDURE SND_ALRT_SAVE_DOC_PRC   (  P_SYS_NO      IN NUMBER ,
                                     P_DOC_TYP     IN NUMBER ,  
                                     P_DOC_SER     IN NUMBER ,                                                                
                                     P_SCHMA_NM    IN VARCHAR2 DEFAULT NULL,                                   
                                     P_U_ID        IN NUMBER,                                    
                                     P_DTS_ONLINE  IN NUMBER,
                                     P_COMMIT_FLG  IN NUMBER,
                                     P_Pst_Typ     IN NUMBER DEFAULT 1,                        
                                     P_LNG_NO      IN NUMBER     DEFAULT 1
                                   ) Is
 V_FORM_NO NUMBER;
 V_DTS_SND_ALRT_OFFLINE NUMBER(1):=0;                                   
BEGIN 

    IF Nvl(P_SYS_NO,0)=70 THEN
         BEGIN
           EXECUTE IMMEDIATE 'SELECT NVL(DTS_SND_ALRT_OFFLINE,0)  FROM DTS_PARA ' INTO V_DTS_SND_ALRT_OFFLINE;
         Exception When Others Then
             V_DTS_SND_ALRT_OFFLINE:=0;
         END; 
    END IF;        
   -----------------------------------------------
   IF NVL(P_Pst_Typ,0)<>2 AND P_DOC_TYP IN(4,5) THEN
      RETURN;
    END IF;
  ------------------------------------------                                 
  IF (Nvl(P_SYS_NO,0)=70  And nvl(P_DTS_ONLINE,0)=0 AND NVL(V_DTS_SND_ALRT_OFFLINE,0)=0 ) --- DTS Offline
                     Or Nvl(P_SYS_NO,0)=185           ---STN
                     or nvl(P_COMMIT_FLG,0)=0  Then -- Offline
    RETURN;
  END IF;
   ------------------------------------------                                         
    V_FORM_NO:= CASE WHEN P_Doc_Typ=4 THEN 158
                     WHEN P_Doc_Typ=5 THEN 160
                     WHEN P_Doc_Typ=52 THEN 155
                     WHEN P_Doc_Typ=53 THEN 156
                     WHEN P_Doc_Typ=136 THEN 821
                     ELSE
                      NULL
                     END;
   ------------------------------------------                      
    EXECUTE IMMEDIATE '
        BEGIN                  
           IAS_SMS_MAIL_PKG.SND_ALRT_IN_SAVE_DOC_PRC ( P_DOC_TYP     =>'||P_Doc_Typ||'  
                                                    , P_DOC_SRL      =>'||P_Doc_Ser||'                            
                                                    , P_FRM_ST       =>''I'' 
                                                    , P_SCHMA_NM     => '''||P_SCHMA_NM||'''
                                                    , P_SCHMA_PS     => NULL
                                                    , P_U_ID         =>'||P_U_ID||'
                                                    , P_FORM_NO      => '|| V_FORM_NO||'                       
                                                    , P_LNG_NO       =>'||P_Lng_No|| ');
        END;' ;                                                   
                       
                     
  ------------------------------------------  
Exception When Others Then
     Null;                  
End   SND_ALRT_SAVE_DOC_PRC;                
--##-----------------------------------------------------------------------------------------------------##-- 
Procedure Chk_Sale_Outlet ( P_Sys_No                      In  Number     Default Null  
                           ,P_Cc_Code                     In  Ias_Bill_Mst.C_Code%Type Default Null  
                           ,P_Lang                        In  Number Default 1
                           ,P_Msg_Txt                     Out Varchar2
                           ,P_Err_No                      Out Varchar2
                           ,P_Pkg_Nm                      Out Varchar2  ) Is
V_Use_Sale_Outlet    Ias_Para_Gen.Use_Sale_Outlet%Type;
V_Outlet_Sale_Typ    Ias_Para_Ar.Outlet_Sale_Typ%Type;                            
Begin
  --##-------------------------------------------------##--	
   Begin 
     Select Nvl(Use_Sale_Outlet,0), Nvl(Outlet_Sale_Typ ,0)
     Into   V_Use_Sale_Outlet,V_Outlet_Sale_Typ 
          From Ias_Para_Gen,Ias_Para_Ar 
       Where Rownum <=1; 
    
   Exception  When Others  Then Null ;
   End ; 
  --##-------------------------------------------------##--	
   If  V_Use_Sale_Outlet =0 Then 
   Return ;  
   End If; 
  --##-------------------------------------------------##--  
   If  Nvl(V_Outlet_Sale_Typ,0) <> 2 Then 
   Return ;  
   End If; 
  --##-------------------------------------------------##--	
	If Nvl(V_Outlet_Sale_Typ,0) = 2  And P_Cc_Code Is Null Then 
            P_Msg_Txt  :=  Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lang, P_Msg_No => 87);
            P_Err_No := 20753 ;   
            Goto Rtn_Rslt;
    End If ; 
 ---------------------------------------------------
  If Nvl(Ys_Json_Pkg.Get_Sale_Outlet_Fnc( P_Sys_No          => P_Sys_No    
  						                 ,P_Sale_Outlet_Typ => V_Outlet_Sale_Typ  
  						                 ,P_Inpt_Code       => P_Cc_Code ),0) = 0 Then
         P_Msg_Txt  := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lang, P_Msg_No => 7112)||' '||Ias_Gen_Pkg.Get_Prompt (P_Lng_No => P_Lang, P_Lb_No => 728)||': '||P_Cc_Code ;
         P_Err_No := 20754 ;   
         Goto Rtn_Rslt;
  End If ;	   
--------------------------------------------------- 
   <<Rtn_Rslt>>
      If P_Msg_Txt Is Not Null Or P_Err_No Is Not Null Then        
            P_Msg_Txt  := Nvl(P_Msg_Txt,'Message Number Is Missing');
            P_Err_No := P_Err_No ;
            P_Pkg_Nm   :=Nvl(P_Pkg_Nm,'Ars_Api_Chk_Pkg.Chk_Sale_Outlet');
            Return;
      Else
         P_Msg_Txt   := Null;
         P_Err_No    := Null ;
         P_Pkg_Nm    := Null;     
      End If;
   --####################--
   Exception
      When Others Then Null; 
End Chk_Sale_Outlet;		
--##-----------------------------------------------------------------------------------------------------##--                             
END Ars_Api_CHK_Pkg;      