--- SPEC ---
Package YS_POST_INV_TRNS_PKG As
    PROCEDURE Update_Post_tr ;
    Procedure Check_Duplicate_Tr(  P_Tr_Inout_Type Ias_Whtrns_Mst.Tr_Inout_Type%Type ,
                                   P_Tr_No         Ias_Whtrns_Mst.Tr_No%Type         ,
                                   P_Tr_Type       Ias_Whtrns_Mst.Tr_Type%Type       ,
                                   P_Tr_Ser        Ias_Whtrns_Mst.Tr_Ser%Type        ,
                                   P_Wcode         Ias_Whtrns_Mst.W_Code%Type        ); 

    PROCEDURE Check_Duplicate_SI(P_Bill_No In Number,P_Bill_Doc_Type In NUmber,P_Bill_Ser In NUmber )  ;                             
    PROCEDURE Check_Duplicate_Sr(P_Rt_Bill_No In Number,P_Rt_Bill_Doc_Type In NUmber,P_Rt_Bill_Ser In NUmber )  ;

    PROCEDURE Insert_Installemnt (P_Doc_Type    Number,
                                  P_BillNo      Number,
                                  P_billdoctype Number,
                                  P_BillSer     Number,
                                  P_Billdate    Date,
                                  P_User_Id     Number,
                                  P_billcur     Varchar2,
                                  P_CashNo      Number,
                                  P_ccode       Varchar2,
                                  P_Typ         Varchar2 Default 'D') ;

    Procedure Insert_Other_Charges (P_Billno      Number,
                                    P_Billdoctype Number,
                                    P_Billser     Number,
                                    P_Billdate    Date,
                                    P_User_Id     Number,
                                    P_Billcur     Varchar2,
                                    P_Cashno      Number,
                                    P_Ccode       Varchar2,
                                    P_Typ         Varchar2 Default 'D') ;
    Procedure Insert_Other_Charges_Sr ( P_Rt_Billno      Number,
                                        P_Rt_Billdoctype Number,
                                        P_Rt_Billser     Number,
                                        P_Rt_Billdate    Date,
                                        P_User_Id        Number,
                                        P_Rt_Billcur     Varchar2,
                                        P_Cashno         Number,
                                        P_Ccode          Varchar2,
                                        P_Typ            Varchar2 Default 'D') ;  
    PROCEDURE Check_Avl_Qty (  P_Doc_Type Number);                                                            
                                                             
    Function Get_Bill_No (  P_Invoicing_Serials In Number   ,
                            P_Si_Type           In Number   ,
                            P_Cc_Code           In Varchar2 ,                        
                            P_Bill_Doc_Type     In Number   ,
                            P_W_Code            In Number   ,
                            P_Brn_No            In Number   ) Return Number ;
   
   Function Get_Bill_No_Br (  P_Invs In Number   ,
                                  P_Si_Type           In Number   ,
                                  P_Cc_Code           In Varchar2 ,                        
                                  P_Bill_Doc_Type     In Number   ,
                                  P_W_Code            In Number   ,
                                  P_Brn_No            In Number   ) Return Number ;
                            
    Function Get_Bill_Ser ( P_Invs              In Number ,
                            P_Si_Type           In Number,
                            P_Cc_Code           In Varchar2,
                            P_Bill_No           In Number, 
                            P_Bill_Doc_Type     In Number,
                            P_W_Code            In Number,
                            P_Brn_No            In Number,
                            P_Brn_Year          IN Number) Return Number  ;   
                            
    FUNCTION Get_Rt_Bill_No ( P_Invs_Sr          In Number,
                              P_sr_Type          In Number,
                              P_Cc_Code          In Varchar2,                        
                              P_Bill_doc_type    In Number,
                              P_W_Code           In Number,
                              P_brn_no           In number) Return Number ;
   FUNCTION Get_Rt_Bill_No_Br ( P_Invs_Sr          In Number,
                                  P_sr_Type          In Number,
                                  P_Cc_Code          In Varchar2,                        
                                  P_Bill_doc_type    In Number,
                                  P_W_Code           In Number,
                                  P_brn_no           In number) Return Number ;
   FUNCTION Get_Rt_Bill_Ser (   P_Invs_Sr       IN Number,
                                P_sr_Type       IN Number,
                                P_Cc_Code       IN Varchar2,
                                P_Rt_Bill_No    IN Number, 
                                P_Bill_doc_type IN Number,
                                P_W_Code        IN Number,
                                P_brn_no        IN number,
                                P_Brn_Year      IN Number) Return Number ;
   Function Get_Gr_No_Br ( P_Brn_No    In  S_Brn.Brn_No%Type                 ,
                           P_Ser_Type  In  Ias_Para_Inv.Incoming_Serial%Type ,
                           P_Inc_Type  In  Gr_Note.Incom_Type%Type           ,
                           P_W_Code    In  Gr_Note.W_Code%Type               ) Return Number ;

   FUNCTION Get_Out_No_Br ( P_Brn_No    In  S_Brn.Brn_No%Type                 ,
                            P_Ser_Type  In  Ias_Para_Inv.Outgoing_Serial%Type ,
                            P_Out_Type  In  Ias_Outgoing_Mst.Out_Type%Type    ,
                            P_W_Code    In  Ias_Outgoing_Mst.W_Code%Type      ) Return Number ;
   Function Get_Out_Br_Ser ( P_Outgoing_Serial In Number ,
                             P_Out_Type        In Number,
                             P_Out_No          In Number, 
                             P_W_Code          In Number,
                             P_Brn_No          In Number,
                             P_Brn_Year        In Number) Return Number ;
 
        Function Get_Gr_Br_Ser (   P_Incoming_Serial In Number ,
                                   P_Inc_Type        In Number,
                                   P_Inc_No          In Number, 
                                   P_W_Code          In Number,
                                   P_Brn_No          In Number,
                                   P_Brn_Year        In Number) Return Number;
--##--------------------------------------------------------------------------------##--                                             
   
   Procedure Post_Incmng ( P_Doc_Ser  In Gr_Note.G_Ser%Type   Default Null , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  ;
   Procedure Post_OutGoing ( P_Doc_Ser  In Ias_Outgoing_Mst.Out_Ser%Type   Default Null , P_Use_Adjstmnt In Number Default 0 ,P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  ;
   Procedure Post_Transfer_Out  ( P_Doc_Ser  In Ias_Whtrns_Mst.Tr_Ser%Type   Default Null , P_Use_Adjstmnt In Number Default 0 , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  ;
   Procedure Post_Transfer_In ( P_Doc_Ser  In Ias_Whtrns_Mst.Tr_Ser%Type   Default Null , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  ;
   Procedure Post_Transfer_Out_In ( P_Doc_Ser  In Ias_Whtrns_Mst.Tr_Ser%Type   Default Null , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  ;
   
   PROCEDURE Post_Sales_Detail ( P_Doc_Ser  In Ias_Bill_Mst.Bill_Ser%Type   Default Null , P_Use_Adjstmnt In Number Default 0 ,P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  ;
   PROCEDURE Post_Rt_Sales_Detail ( P_Doc_Ser  In Ias_Rt_Bill_Mst.Rt_Bill_Ser%Type   Default Null , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  ;   
   PROCEDURE Post_Sales_Sum ;
   PROCEDURE Post_Rt_Sales_Sum ( P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  ;   
   PROCEDURE Post_Stk_Adjstmnt ;  
   PROCEDURE Post_Jv;
   PROCEDURE Post_Vchr;
   PROCEDURE Insrt_Tax (P_Doc_Type In Number , P_Doc_Ser In Number) ;
   PROCEDURE Insrt_Point_Trns (P_Doc_Type In Number , P_Doc_Ser In Number);
   PROCEDURE Post_Serial (P_Doc_Ser In Number , P_Doc_Type In Number);
   FUNCTION Get_Card_Comm_Prcnt (P_Cr_Card_No In Number) RETURN Number;
   PROCEDURE Post_Trns_Data_Auto ;
 
End YS_POST_INV_TRNS_PKG ;

--- BODY ---
Package Body YS_POST_INV_TRNS_PKG As
--##-------------------------------------------------------------------------------------##--
PROCEDURE Update_Post_tr IS
BEGIN
  Begin
   Update Ias_Whtrns_Mst_Br a
         Set Tr_Post=1
       Where  Nvl(Tr_Post,0)=0 
         And Exists(Select 1 From Ias_Whtrns_Mst 
                    Where Tr_Ser=A.Tr_Ser 
                    --And Nvl(Tr_Amt,0)=Nvl(a.Tr_Amt,0) 
                      And RowNum <=1)             
         And Exists(select Doc_Ser From Item_Movement Where Doc_Ser=A.Tr_Ser And RowNum<=1);
    Exception
        When Others Then
          Raise_Application_Error(-20001,'Error In Update Ias_Whtrns_Mst_Br');
    End ;          
    
    Begin
       Update Ias_Whtrns_Mst_Br a
          Set Tr_Post=0
       Where  Nvl(Tr_Post,0)=1 
         And Not Exists(Select 1 From Ias_Whtrns_Mst 
                    Where Tr_Ser=A.Tr_Ser                           
                      And RowNum<=1);
    Exception
        When Others Then
          Raise_Application_Error(-20002,'Error In Update Ias_Whtrns_Mst_Br');
    End ;     
    
END Update_Post_tr ;
--##-------------------------------------------------------------------------------------##--
Procedure Check_Duplicate_Tr( P_Tr_Inout_Type Ias_Whtrns_Mst.Tr_Inout_Type%Type ,
                              P_Tr_No         Ias_Whtrns_Mst.Tr_No%Type         ,
                              P_Tr_Type       Ias_Whtrns_Mst.Tr_Type%Type       ,
                              P_Tr_Ser        Ias_Whtrns_Mst.Tr_Ser%Type        ,
                              P_Wcode         Ias_Whtrns_Mst.W_Code%Type        ) Is
  V_Cnt Number := 0 ;
 Begin
    Begin
     V_Cnt := Ias_Gen_Pkg.Get_Cnt(' Select 1 
                                     From Ias_Whtrns_Mst 
                                      Where Tr_Inout_Type = '|| P_Tr_Inout_Type||' 
                                       And Tr_Ser         = '|| P_Tr_Ser||'
                                       And Rownum        <=1 ');
    Exception  
      When No_Data_Found Then
       V_Cnt := 0 ;
      When Others Then
          Null;
    End;
    If Nvl(V_Cnt,0) > 0 Then      
       RollBack ;
       Raise_Application_Error(-20001,Ias_Gen_Pkg.Get_Prompt(1,234) ||' = '||P_Tr_No  ||Chr(13)||
                                      Ias_Gen_Pkg.Get_Prompt(1,1466)||' = '||P_Tr_Type||Chr(13)||
                                      Ias_Gen_Pkg.Get_Prompt(1,193) ||' = '||P_Wcode  ||Chr(13)||
                                      Ias_Gen_Pkg.Get_Msg(1,505));       
    End If;    
 End Check_Duplicate_Tr ;
--##-------------------------------------------------------------------------------------##--
PROCEDURE Check_Duplicate_SI(P_Bill_No In Number,P_Bill_Doc_Type In NUmber,P_Bill_Ser In NUmber ) Is
  V_Cnt Number:=0;
  V_Doc_Type_Nm S_Flags.Flg_Desc%Type ;
BEGIN
---------------------------------------------------------------------------------------------    
    Begin
        Select Flg_Desc Into V_Doc_Type_Nm From S_Flags
            Where Flg_Code='TYPE_NAME_SI'
              And Flg_Value=P_Bill_Doc_Type
                And Lang_No= 1
                And Rownum<=1;
    Exception  
         When Others Then
          Null;
    End;      
---------------------------------------------------------------------------------------------    
    Begin
        V_Cnt := Ias_Gen_Pkg.Get_Cnt('Select 1 From Ias_Bill_Mst 
                                      Where Bill_Ser ='|| P_Bill_Ser||'
                                      And Rownum<=1');
    Exception  
         When Others Then
          Null;
    End;
---------------------------------------------------------------------------------------------    
  If Nvl(V_Cnt,0) > 0 Then      
    RollBack ;   
    Raise_Application_Error (-20001,Ias_Gen_Pkg.Get_Prompt(1,349)||' '||V_Doc_Type_Nm||' '||P_Bill_No||' '||Ias_Gen_Pkg.Get_Msg(1,505));       
     
  End If;    
---------------------------------------------------------------------------------------------
END Check_Duplicate_SI;
--##-------------------------------------------------------------------------------------##--
PROCEDURE Check_Duplicate_Sr(P_Rt_Bill_No In Number,P_Rt_Bill_Doc_Type In NUmber,P_Rt_Bill_Ser In NUmber ) Is
  V_Cnt Number:=0;
  V_Doc_Type_Nm S_Flags.Flg_Desc%Type ;
BEGIN
---------------------------------------------------------------------------------------------    
    Begin
        Select Flg_Desc Into V_Doc_Type_Nm From S_Flags
            Where Flg_Code='TYPE_NAME_SI'
              And Flg_Value=P_Rt_Bill_Doc_Type
                And Lang_No= 1
                And Rownum<=1;
    Exception  
         When Others Then
          Null;
    End;      
---------------------------------------------------------------------------------------------    
    Begin
        V_Cnt := Ias_Gen_Pkg.Get_Cnt('Select 1 From Ias_Rt_Bill_Mst 
                                      Where Rt_Bill_Ser ='|| P_Rt_Bill_Ser||'
                                      And Rownum<=1');
    Exception  
         When Others Then
          Null;
    End;
---------------------------------------------------------------------------------------------    
  If Nvl(V_Cnt,0) > 0 Then      
       RollBack ;
       Raise_Application_Error (-20001,Ias_Gen_Pkg.Get_Prompt(1,349)||' '||V_Doc_Type_Nm||' '||P_Rt_Bill_No||' '||Ias_Gen_Pkg.Get_Msg(1,505));
  End If;    
---------------------------------------------------------------------------------------------
END Check_Duplicate_Sr;
--##-------------------------------------------------------------------------------------##-- 
PROCEDURE Insert_Installemnt (P_Doc_Type    Number,
                              P_BillNo      Number,
                              P_billdoctype Number,
                              P_BillSer     Number,
                              P_Billdate    Date,
                              P_User_Id     Number,
                              P_billcur     Varchar2,
                              P_CashNo      Number,
                              P_ccode       Varchar2,
                              P_Typ         Varchar2 Default 'D') Is
BEGIN
----------------------------------------------------------------------------------------------    
        If P_Typ='D' Then
            Declare                
                Cursor c1 Is
               Select   I_No, 
                        I_Date, 
                        I_Amt, 
                        Installment_Br.Cheque_No, 
                        Installment_Br.Cheque_Due_Date, 
                        Installment_Br.C_Code, 
                        A_Cy, 
                        Installment_Br.Paid_Amt, 
                        Adj_Amt, 
                        Dr_No, 
                        I_Py,
                        Installment_Br.Cc_Code, 
                        Installment_Br.Pj_No, 
                        Installment_Br.Actv_No,
                        Installment_Br.Brn_No, 
                        Installment_Br.Brn_Year,
                        Installment_Br.Cmp_No,
                        Installment_Br.Brn_Usr
                   From Ias_Bill_Mst_Br , Installment_Br
                        where Ias_Bill_Mst_Br.bill_ser= Installment_Br.bill_ser 
                          and Installment_Br.Doc_type=P_Doc_Type
                          and nvl(Ias_Bill_Mst_Br.bill_post,0)=0
                          and nvl(Ias_Bill_Mst_Br.Stand_By,0)=0
                          and Ias_Bill_Mst_Br.Bill_Ser = P_BillSer;                  
                Begin    
                     For J in c1 Loop                                    
                       Begin         
                              Insert Into Installment (  Doc_Type, 
                                                          Bill_Doc_Type, 
                                                          Bill_No, 
                                                          Bill_Ser, 
                                                          I_No, 
                                                          I_Date, 
                                                          I_Amt, 
                                                          Cheque_No, 
                                                          Cheque_Due_Date, 
                                                          C_Code, 
                                                          A_Cy, 
                                                          Paid_Amt, 
                                                          Adj_Amt, 
                                                          Dr_No, 
                                                          I_Py,
                                                          Cc_Code,
                                                          Pj_No,
                                                          Actv_No, 
                                                          Rcrd_No,
                                                          Brn_No, 
                                                          Brn_Year,
                                                          Cmp_No,
                                                          Brn_Usr) 
                                         Values ( P_Doc_Type, 
                                                  P_BillDocType, 
                                                  P_BillNo, 
                                                  P_BillSer, 
                                                  J.I_No, 
                                                  J.I_Date, 
                                                  J.I_Amt, 
                                                  J.Cheque_No, 
                                                  J.Cheque_Due_Date, 
                                                  J.C_Code, 
                                                  J.A_Cy, 
                                                  J.Paid_Amt, 
                                                  J.Adj_Amt, 
                                                  J.Dr_No, 
                                                  J.I_Py, 
                                                  J.Cc_Code,
                                                  J.Pj_No,
                                                  J.Actv_No,
                                                  1,
                                                  J.Brn_No, 
                                                  J.Brn_Year,
                                                  J.Cmp_No,
                                                  J.Brn_Usr);
                       Exception
                           When No_Data_Found Then   
                               Null;         
                           When Others Then        
                             --Raise_Application_Error(-20001,'Error In Insert Installment');                             
                             --RollBack;
                               Null;
                       End;     
                     End Loop;    
                End;
        Else --------------------------------------------------------------------------------------    
             Declare                         
                  Cursor c1 Is
                   Select   I_No, 
                            I_Date, 
                            Sum(I_Amt) I_Amt, 
                            Installment_Br.Cheque_No, 
                            Installment_Br.Cheque_Due_Date, 
                            Installment_Br.C_Code, 
                            A_Cy, 
                            Sum(Installment_Br.Paid_Amt) Paid_Amt, 
                            Sum(Adj_Amt) Adj_Amt, 
                            Dr_No,                 
                            I_Py, 
                            Installment_Br.Cc_Code, 
                            Installment_Br.Pj_No, 
                            Installment_Br.Actv_No,
                            Installment_Br.Brn_No, 
                            Installment_Br.Brn_Year,
                            Installment_Br.Cmp_No,
                            Installment_Br.Brn_Usr,
                            Ias_Bill_Mst_Br.EXTERNAL_POST
                     From Ias_Bill_Mst_Br , Installment_Br
                        Where Ias_Bill_Mst_Br.bill_ser= Installment_Br.bill_ser 
                          and Installment_Br.Doc_type=P_Doc_Type
                          and nvl(Ias_Bill_Mst_Br.bill_post,0)=0
                          and nvl(Ias_Bill_Mst_Br.Stand_By,0)=0                  
                          and Ias_Bill_Mst_Br.Bill_date=P_Billdate
                          and Ias_Bill_Mst_Br.ad_u_id=P_User_id 
                          and Ias_Bill_Mst_Br.bill_currency=P_BillCur
                          and Nvl(Ias_Bill_Mst_Br.cash_no,0)=Nvl(P_CashNo,0)
                          and Nvl(Ias_Bill_Mst_Br.c_code,0)=Nvl(P_Ccode,0)
                          Group By I_No,I_Date,Installment_Br.Cheque_No,Installment_Br.Cheque_Due_Date,Installment_Br.C_Code,A_Cy, 
                                   Dr_No,I_Py,Installment_Br.Brn_No,Installment_Br.Brn_Year;
                Begin    
                    For J in c1 Loop                                                             
                      Begin         
                              Insert Into Installment ( Doc_Type, 
                                                       Bill_Doc_Type, 
                                                       Bill_No, 
                                                       Bill_Ser, 
                                                       I_No, 
                                                       I_Date, 
                                                       I_Amt, 
                                                       Cheque_No, 
                                                       Cheque_Due_Date, 
                                                       C_Code, 
                                                       A_Cy, 
                                                       Paid_Amt, 
                                                       Adj_Amt, 
                                                       Dr_No, 
                                                       Rcrd_No,
                                                       I_Py, 
                                                       Cc_Code,
                                                       Pj_No,
                                                       Actv_No, 
                                                       Brn_No, 
                                                       Brn_Year,
                                                       Cmp_No,
                                                       Brn_Usr,
                                                       EXTERNAL_POST) 
                                         Values ( P_Doc_Type, 
                                                  P_BillDocType, 
                                                  P_BillNo, 
                                                  P_BillSer, 
                                                  J.I_No, 
                                                  J.I_Date, 
                                                  J.I_Amt, 
                                                  J.Cheque_No, 
                                                  J.Cheque_Due_Date, 
                                                  J.C_Code, 
                                                  J.A_Cy, 
                                                  J.Paid_Amt, 
                                                  J.Adj_Amt, 
                                                  J.Dr_No, 
                                                  J.I_Py, 
                                                  J.Cc_Code,
                                                  J.Pj_No,
                                                  J.Actv_No, 
                                                  1,
                                                  J.Brn_No, 
                                                  J.Brn_Year,
                                                  J.Cmp_No,
                                                  J.Brn_Usr,
                                                  J.EXTERNAL_POST); 
                                                          
                                                          
                      Exception
                          When No_Data_Found Then   
                                 Null;         
                          When Others Then        
                             --Raise_Application_Error(-20001,'Error In Insert Installment');                             
                             --RollBack;
                               Null;
                      End;     
                    End Loop;    
                End;
End If;
END Insert_Installemnt ;
--##-------------------------------------------------------------------------------------##--
PROCEDURE Insert_Other_Charges (P_BillNo      Number,
                                P_billdoctype Number,
                                P_BillSer     Number,
                                P_Billdate    Date,
                                P_User_Id     Number,
                                P_billcur     Varchar2,
                                P_CashNo      Number,
                                P_ccode       Varchar2,
                                P_Typ         Varchar2 Default 'D') Is
  --V_F_Wcode  Number:=:Post_Sales.F_W_Code;
  -- V_T_Wcode  Number:=:Post_Sales.T_W_Code;     
BEGIN
----------------------------------------------------------------------------------------------    
        If P_Typ='D' Then
            Declare                
                Cursor c1 Is
               Select amt,per,sc_no,Other_Charges_Br.a_code,a_cy,ac_rate,inv_item,rcrd_no,Other_Charges_Br.brn_no,Other_Charges_Br.brn_year,
                      Other_Charges_Br.Cmp_No,Other_Charges_Br.brn_usr,Other_Charges_Br.doc_date,Other_Charges_Br.Vat_Amt, Other_Charges_Br.Vat_Per, 
                      Other_Charges_Br.Sc_Amt, Other_Charges_Br.Sc_Ac_Rate, Other_Charges_Br.Sc_A_Cy
                 From Ias_Bill_Mst_Br , Other_Charges_Br
                where Ias_Bill_Mst_Br.bill_ser= Other_Charges_Br.bill_ser                   
                  and Other_Charges_Br.bill_type=1
                  and nvl(Ias_Bill_Mst_Br.bill_post,0)=0                              
                  and nvl(Ias_Bill_Mst_Br.Stand_By,0)=0
                  and Ias_Bill_Mst_Br.Bill_Ser = P_BillSer;
                  /*and Ias_Bill_Mst_Br.Bill_date=Billdate
                  and Ias_Bill_Mst_Br.ad_u_id=User_id 
                  and Ias_Bill_Mst_Br.bill_currency=BillCur
                  and Nvl(Ias_Bill_Mst_Br.cash_no,0)=Nvl(CashNo,0)
                  and Nvl(Ias_Bill_Mst_Br.c_code,0)=Nvl(Ccode,0);*/
                Begin    
                     For i in c1 Loop                                    
                       Begin         
                              Insert Into Other_Charges ( Bill_Type, 
                                                   Bill_Doc_Type, 
                                                   Bill_No, 
                                                   Bill_Ser, 
                                                   Sc_No, 
                                                   A_Code, 
                                                   A_Cy, 
                                                   Ac_Rate, 
                                                   Per, 
                                                   Amt, 
                                                   Inv_Item, 
                                                   Rcrd_No,
                                                   doc_date,
                                                   Vat_Amt, 
                                                   Vat_Per, 
                                                   Sc_Amt, 
                                                   Sc_Ac_Rate, 
                                                   Sc_A_Cy,
                                                   Brn_No,
                                                   Brn_Year,
                                                   Cmp_No,
                                                   brn_usr)
                                          Values ( 1,
                                                 p_Billdoctype,
                                                 p_Billno,
                                                 P_BillSer,
                                                 I.Sc_No,
                                                 I.A_Code,
                                                 I.A_Cy,
                                                 I.Ac_Rate,
                                                 I.Per,
                                                 I.Amt,
                                                 I.Inv_Item,
                                                 I.Rcrd_No,
                                                 I.doc_date,
                                                 I.Vat_Amt, 
                                                   I.Vat_Per, 
                                                   I.Sc_Amt, 
                                                   I.Sc_Ac_Rate, 
                                                   I.Sc_A_Cy,
                                                 I.Brn_No,
                                                 I.Brn_Year,
                                                 I.Cmp_No,
                                                 I.Brn_usr);
                       Exception
                               When No_Data_Found Then   
                                 Null;         
                          When Others Then
                           RollBack;
                           Raise_Application_Error(-20001,Ias_Gen_Pkg.Get_Msg(1,1161)||Chr(13)||SqlErrm);                                                            
                      End;     
                 End Loop;    
                End;
------------------------------------------ Other Charges Items -------------------------------    
                Declare                              
                    Cursor c1 Is
                       Select nvl(amt,0) amt,nvl(per,0) per,sc_no,Other_Charges_Items_Br.a_code,a_cy,ac_rate,i_code,
                              Itm_Unt,p_size,rcrd_no,Other_Charges_Items_Br.brn_no,Other_Charges_Items_Br.brn_year,Other_Charges_Items_Br.w_code,
                              Other_Charges_Items_Br.Cc_Code,Other_Charges_Items_Br.Pj_No,Other_Charges_Items_Br.Actv_No,
                              Other_Charges_Items_Br.Cmp_No,Other_Charges_Items_Br.brn_usr
                         From Ias_Bill_Mst_Br , Other_Charges_Items_Br
                        where Ias_Bill_Mst_Br.bill_ser= Other_Charges_Items_Br.bill_ser 
                          and Other_Charges_Items_Br.bill_type=1
                          --And Nvl(Ias_Bill_Mst_Br.W_Code,0) Between Nvl(V_F_Wcode,Nvl(Ias_Bill_Mst_Br.W_Code,0)) And Nvl(V_T_Wcode,Nvl(Ias_Bill_Mst_Br.W_Code,0))
                          and nvl(Ias_Bill_Mst_Br.bill_post,0)=0                                          
                          and nvl(Ias_Bill_Mst_Br.Stand_By,0)=0
                          and Ias_Bill_Mst_Br.Bill_Ser = P_BillSer;                          
                Begin                          
                        For j in c1 Loop
                        Begin                            
                              Insert Into Other_Charges_Items 
                                                        ( BILL_TYPE, 
                                                          BILL_DOC_TYPE, 
                                                          BILL_NO, 
                                                          BILL_SER, 
                                                          SC_NO, 
                                                          A_CODE, 
                                                          A_Cy, 
                                                          AC_RATE, 
                                                          PER, 
                                                          AMT, 
                                                          I_CODE, 
                                                          Itm_Unt, 
                                                          P_SIZE,
                                                     RCRD_NO,
                                                     Cc_Code,
                                                   Pj_No,
                                                   Actv_No,
                                                     brn_no,
                                                     brn_year,
                                                     w_code,
                                                     Cmp_No,
                                                   Brn_usr)
                                                 Values ( 1, 
                                                          p_BILLDOCTYPE, 
                                                          P_BILLNO, 
                                                          P_BILLSER, 
                                                          j.SC_NO, 
                                                          j.A_CODE, 
                                                          j.A_Cy, 
                                                          j.AC_RATE, 
                                                          j.PER, 
                                                          j.AMT, 
                                                          j.I_CODE, 
                                                          j.Itm_Unt, 
                                                          j.P_SIZE,
                                                     j.RCRD_NO,
                                                     j.Cc_Code,
                                                   j.Pj_No,
                                                   j.Actv_No,
                                                     j.brn_no,
                                                     j.brn_year,
                                                     j.w_code,
                                                     J.Cmp_No,
                                                   J.Brn_usr);
                         Exception
                             When No_Data_Found Then   
                                 Null;         
                          When Others Then
                          Rollback;
                          Raise_Application_Error(-20002,Ias_Gen_Pkg.Get_Msg(1,1161)||Chr(13)||SqlErrm);                                         
                          End;               
                 End Loop;    
            End;
  Else --------------------------------------------------------------------------------------    
        Declare
                rcd Number:=0;    
                Cursor c1 Is
               Select nvl(Sum(amt),0) amt,nvl(per,0) per,sc_no,Other_Charges_Br.a_code,a_cy,ac_rate,inv_item,Other_Charges_Br.brn_no,Other_Charges_Br.brn_year,
                      Other_Charges_Br.Cmp_No,Other_Charges_Br.brn_usr,
                      sum(nvl(Other_Charges_Br.Vat_Amt,0)) Vat_Amt, avg(Other_Charges_Br.Vat_Per) Vat_Per, sum(nvl(Other_Charges_Br.Sc_Amt,0)) Sc_Amt, 
                      avg(Other_Charges_Br.Sc_Ac_Rate) Sc_Ac_Rate, Other_Charges_Br.Sc_A_Cy
                 From Ias_Bill_Mst_Br , Other_Charges_Br
                where Ias_Bill_Mst_Br.bill_ser= Other_Charges_Br.bill_ser 
                  and Other_Charges_Br.bill_type=1
                  and Ias_Bill_Mst_Br.Bill_Doc_Type<>4
                  and nvl(Ias_Bill_Mst_Br.bill_post,0)=0
                  and nvl(Ias_Bill_Mst_Br.Stand_By,0)=0
                  and Ias_Bill_Mst_Br.Bill_date=P_Billdate
                  and Ias_Bill_Mst_Br.ad_u_id=P_User_Id 
                  and Ias_Bill_Mst_Br.bill_currency=P_BillCur
                  and Nvl(Ias_Bill_Mst_Br.cash_no,0)=Nvl(P_CashNo,0)
                  and Nvl(Ias_Bill_Mst_Br.c_code,0)=Nvl(P_Ccode,0)
                  Group by nvl(per,0),sc_no,Other_Charges_Br.a_code,a_cy,ac_rate,inv_item,Other_Charges_Br.brn_no,Other_Charges_Br.brn_year,
                           Other_Charges_Br.Cmp_No,Other_Charges_Br.brn_usr,Other_Charges_Br.Sc_A_Cy;
                Begin    
                     For i in c1 Loop          
                          rcd:=rcd+1;     
                       Begin         
                              Insert Into Other_Charges ( Bill_Type, 
                                                   Bill_Doc_Type, 
                                                   Bill_No, 
                                                   Bill_Ser, 
                                                   Sc_No, 
                                                   A_Code, 
                                                   A_Cy, 
                                                   Ac_Rate, 
                                                   Per, 
                                                   Amt, 
                                                   Inv_Item, 
                                                   Rcrd_No,
                                                   Vat_Amt, 
                                                   Vat_Per, 
                                                   Sc_Amt, 
                                                   Sc_Ac_Rate, 
                                                   Sc_A_Cy,
                                                   Brn_No,
                                                   Brn_Year,
                                                   Cmp_No,
                                                   Brn_usr)
                                          Values ( 1,
                                                    P_Billdoctype,
                                                    P_Billno,
                                                    P_Billser,
                                                    I.Sc_No,
                                                    I.A_Code,
                                                    I.A_Cy,
                                                    I.Ac_Rate,
                                                    I.Per,
                                                    I.Amt,
                                                    I.Inv_Item,
                                                    rcd,
                                                    I.Vat_Amt, 
                                                      I.Vat_Per, 
                                                      I.Sc_Amt, 
                                                      I.Sc_Ac_Rate, 
                                                      I.Sc_A_Cy,
                                                    I.Brn_No,
                                                    I.Brn_Year,
                                                    I.Cmp_No,
                                                    I.Brn_usr);
                     Exception
                          When No_Data_Found Then   
                                 Null;         
                          When Others Then 
                          rollback;
                          Raise_Application_Error(-20003,Ias_Gen_Pkg.Get_Msg(1,1161)||Chr(13)||SqlErrm);                                
                      End;     
                 End Loop;    
                End;
------------------------------------------ Other Charges Items -------------------------------    
                Declare            
                  rcd Number:=0;
                    Cursor c1 Is
                       Select nvl(Sum(amt),0) amt,nvl(per,0) per,sc_no,Other_Charges_Items_Br.a_code,a_cy,ac_rate,i_code,
                              Itm_Unt,p_size,rcrd_no,Other_Charges_Items_Br.brn_no,Other_Charges_Items_Br.brn_year,Other_Charges_Items_Br.w_code,
                              Other_Charges_Items_Br.Cc_Code,Other_Charges_Items_Br.Pj_No,Other_Charges_Items_Br.Actv_No,
                              Other_Charges_Items_Br.Cmp_No,Other_Charges_Items_Br.brn_usr
                         From Ias_Bill_Mst_Br , Other_Charges_Items_Br
                        where Ias_Bill_Mst_Br.bill_ser= Other_Charges_Items_Br.bill_ser 
                          and Ias_Bill_Mst_Br.Bill_Doc_Type<>4
                          and Other_Charges_Items_Br.bill_type=1
                          and nvl(Ias_Bill_Mst_Br.bill_post,0)=0
                          and nvl(Ias_Bill_Mst_Br.Stand_By,0)=0
                          and Ias_Bill_Mst_Br.Bill_date=P_Billdate
                          and Ias_Bill_Mst_Br.ad_u_id=P_User_id 
                          and Ias_Bill_Mst_Br.bill_currency=P_BillCur
                          and Nvl(Ias_Bill_Mst_Br.cash_no,0)=Nvl(P_CashNo,0)
                          and Nvl(Ias_Bill_Mst_Br.c_code,0)=Nvl(P_Ccode,0)
                          Group by nvl(per,0),sc_no,Other_Charges_Items_Br.a_code,a_cy,ac_rate,i_code,Itm_Unt,p_size ,rcrd_no,Other_Charges_Items_Br.brn_no,
                          Other_Charges_Items_Br.brn_year,Other_Charges_Items_Br.w_code,
                          Other_Charges_Items_Br.Cc_Code,Other_Charges_Items_Br.Pj_No,Other_Charges_Items_Br.Actv_No,
                                   Other_Charges_Items_Br.Cmp_No,Other_Charges_Items_Br.brn_usr;
                    Begin                        
                        For j in c1 Loop
                          Begin            
                             rcd:=rcd+1;     
                              Insert Into Other_Charges_Items ( BILL_TYPE, 
                                                                      BILL_DOC_TYPE, 
                                                                      BILL_NO, 
                                                                      BILL_SER, 
                                                                      SC_NO, 
                                                                      A_CODE, 
                                                                      A_Cy, 
                                                                      AC_RATE, 
                                                                      PER, 
                                                                      AMT, 
                                                                      I_CODE, 
                                                                      Itm_Unt, 
                                                                      P_SIZE,
                                                                 RCRD_NO,
                                                                 brn_no,
                                                                 brn_year,
                                                                 w_code,
                                                                 cc_code,
                                                                 pj_no,
                                                                 actv_no,
                                                                 Cmp_No,
                                                               Brn_usr )
                                                             Values ( 1,
                                                                      P_billdoctype,
                                                                      P_BillNo,
                                                                      P_BillSer,
                                                                      j.sc_no,
                                                                      j.a_code,
                                                                      j.a_cy,
                                                                      j.ac_rate,
                                                                      j.per,
                                                                      j.amt,
                                                                      j.i_code,
                                                                      j.Itm_Unt,
                                                                      j.p_size,
                                                                         rcd,
                                                                 j.brn_no,
                                                                 j.brn_year,
                                                                 j.w_code,
                                                                 j.cc_code,
                                                                 j.pj_no,
                                                                 j.actv_no,
                                                                 J.Cmp_No,
                                                               J.Brn_usr);
                         Exception
                              When No_Data_Found Then   
                                 Null;         
                          When Others Then
                          rollback;
                          Raise_Application_Error(-20003,Ias_Gen_Pkg.Get_Msg(1,1161)||Chr(13)||SqlErrm);                                         
                          End;               
                 End Loop;    
                End;
End If;
END Insert_Other_Charges ;


Procedure Insert_Other_Charges_Sr ( P_Rt_Billno      Number,
                                    P_Rt_Billdoctype Number,
                                    P_Rt_Billser     Number,
                                    P_Rt_Billdate    Date,
                                    P_User_Id        Number,
                                    P_Rt_Billcur     Varchar2,
                                    P_Cashno         Number,
                                    P_Ccode          Varchar2,
                                    P_Typ            Varchar2 Default 'D') Is
BEGIN

----------------------------------------------------------------------------------------------    
        If P_Typ='D' Then
            Declare                
                Cursor c1 Is
               Select amt,per,sc_no,Other_Charges_Br.a_code,a_cy,ac_rate,inv_item,rcrd_no,Other_Charges_Br.brn_no,Other_Charges_Br.brn_year,
                      Other_Charges_Br.Cmp_No,Other_Charges_Br.brn_usr,Other_Charges_Br.doc_date,Other_Charges_Br.Vat_Amt, Other_Charges_Br.Vat_Per, 
                      Other_Charges_Br.Sc_Amt, Other_Charges_Br.Sc_Ac_Rate, Other_Charges_Br.Sc_A_Cy
                 From Ias_Rt_Bill_Mst_Br , Other_Charges_Br
                where Ias_Rt_Bill_Mst_Br.Rt_Bill_ser= Other_Charges_Br.Bill_ser                   
                  and Other_Charges_Br.Bill_type=3
                  and nvl(Ias_Rt_Bill_Mst_Br.Rt_Bill_post,0)=0                              
                  and nvl(Ias_Rt_Bill_Mst_Br.Stand_By,0)=0
                  and Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser = P_Rt_Billser;                  
                Begin    
                     For i in c1 Loop                                    
                       Begin         
                              Insert Into Other_Charges ( Bill_Type, 
                                                   Bill_Doc_Type, 
                                                   Bill_No, 
                                                   Bill_Ser, 
                                                   Sc_No, 
                                                   A_Code, 
                                                   A_Cy, 
                                                   Ac_Rate, 
                                                   Per, 
                                                   Amt, 
                                                   Inv_Item, 
                                                   Rcrd_No,
                                                   doc_date,
                                                   Vat_Amt, 
                                                   Vat_Per, 
                                                   Sc_Amt, 
                                                   Sc_Ac_Rate, 
                                                   Sc_A_Cy,
                                                   Brn_No,
                                                   Brn_Year,
                                                   Cmp_No,
                                                   brn_usr)
                                          Values ( 3,
                                                 P_Rt_Billdoctype,
                                                 P_Rt_Billno,
                                                 P_Rt_Billser,
                                                 I.Sc_No,
                                                 I.A_Code,
                                                 I.A_Cy,
                                                 I.Ac_Rate,
                                                 I.Per,
                                                 I.Amt,
                                                 I.Inv_Item,
                                                 I.Rcrd_No,
                                                 i.doc_date,
                                                 I.Vat_Amt, 
                                                   I.Vat_Per, 
                                                   I.Sc_Amt, 
                                                   I.Sc_Ac_Rate, 
                                                   I.Sc_A_Cy,
                                                 I.Brn_No,
                                                 I.Brn_Year,
                                                 I.Cmp_No,
                                                 I.Brn_usr);
                       Exception
                               When No_Data_Found Then   
                                 Null;         
                          When Others Then        
                          rollback;
                          Raise_Application_Error (-20001,'Error When Post Others Charges , (Rt Sales) ,'||SqlErrm);                          
                      End;     
                 End Loop;    
                End;
------------------------------------------ Other Charges Items -------------------------------    
                Declare                              
                    Cursor c1 Is
                       Select nvl(amt,0) amt,nvl(per,0) per,sc_no,Other_Charges_Items_Br.a_code,a_cy,ac_rate,i_code,
                              Itm_Unt,p_size,rcrd_no,Other_Charges_Items_Br.brn_no,Other_Charges_Items_Br.brn_year,Other_Charges_Items_Br.w_code,
                              Other_Charges_Items_Br.cc_code,Other_Charges_Items_Br.Pj_No,Other_Charges_Items_Br.Actv_No,
                              Other_Charges_Items_Br.Cmp_No,Other_Charges_Items_Br.brn_usr
                         From Ias_Rt_Bill_Mst_Br , Other_Charges_Items_Br
                        where Ias_Rt_Bill_Mst_Br.Rt_Bill_ser= Other_Charges_Items_Br.Bill_ser 
                          and Other_Charges_Items_Br.Bill_type=3
                          and nvl(Ias_Rt_Bill_Mst_Br.Rt_Bill_post,0)=0                                          
                          and nvl(Ias_Rt_Bill_Mst_Br.Stand_By,0)=0
                          and Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser = P_Rt_Billser;                          
                Begin                          
                        For j in c1 Loop
                        Begin                            
                              Insert Into Other_Charges_Items ( Bill_TYPE, 
                                                                      Bill_DOC_TYPE, 
                                                                      Bill_NO, 
                                                                      Bill_SER, 
                                                                      SC_NO, 
                                                                      A_CODE, 
                                                                      A_Cy, 
                                                                      AC_RATE, 
                                                                      PER, 
                                                                      AMT, 
                                                                      I_CODE, 
                                                                      Itm_Unt, 
                                                                      P_SIZE,
                                                                 RCRD_NO,
                                                                 brn_no,
                                                                 brn_year,
                                                                 w_code,
                                                                 cc_code,
                                                                 pj_no,
                                                                 actv_no,
                                                                 Cmp_No,
                                                               Brn_usr)
                                                             Values ( 3, 
                                                                      P_Rt_Billdoctype, 
                                                                      P_Rt_Billno, 
                                                                      P_Rt_Billser, 
                                                                      j.SC_NO, 
                                                                      j.A_CODE, 
                                                                      j.A_Cy, 
                                                                      j.AC_RATE, 
                                                                      j.PER, 
                                                                      j.AMT, 
                                                                      j.I_CODE, 
                                                                      j.Itm_Unt, 
                                                                      j.P_SIZE,
                                                                 j.RCRD_NO,
                                                                 j.brn_no,
                                                                 j.brn_year,
                                                                 j.w_code,
                                                                 j.cc_code,
                                                                 j.pj_no,
                                                                 j.actv_no,
                                                                 J.Cmp_No,
                                                               J.Brn_usr);
                         Exception
                             When No_Data_Found Then   
                                 Null;         
                          When Others Then        
                          rollback;
                          Raise_Application_Error (-20002,'Error When Post Others Charges , (Rt Sales) ,'||SqlErrm);
                          End;               
                 End Loop;    
            End;
  Else --------------------------------------------------------------------------------------    
        Declare
                rcd Number:=0;    
                Cursor c1 Is
               Select nvl(Sum(amt),0) amt,nvl(per,0) per,sc_no,Other_Charges_Br.a_code,a_cy,ac_rate,inv_item,Other_Charges_Br.brn_no,Other_Charges_Br.brn_year,
                      Other_Charges_Br.Cmp_No,Other_Charges_Br.brn_usr,sum(nvl(Other_Charges_Br.Vat_Amt,0)) Vat_Amt, avg(Other_Charges_Br.Vat_Per) Vat_Per, sum(nvl(Other_Charges_Br.Sc_Amt,0)) Sc_Amt, 
                      avg(Other_Charges_Br.Sc_Ac_Rate) Sc_Ac_Rate, Other_Charges_Br.Sc_A_Cy
                 From Ias_Rt_Bill_Mst_Br , Other_Charges_Br
                where Ias_Rt_Bill_Mst_Br.Rt_Bill_ser= Other_Charges_Br.Bill_ser 
                  and Other_Charges_Br.Bill_type=3
                  and Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_Type<>4
                 -- And Nvl(Ias_Rt_Bill_Mst_Br.W_Code,0) Between Nvl(V_F_Wcode,Nvl(Ias_Rt_Bill_Mst_Br.W_Code,0)) And Nvl(V_T_Wcode,Nvl(Ias_Rt_Bill_Mst_Br.W_Code,0))
                  and nvl(Ias_Rt_Bill_Mst_Br.Rt_Bill_post,0)=0
                  and nvl(Ias_Rt_Bill_Mst_Br.Stand_By,0)=0
                  and Ias_Rt_Bill_Mst_Br.Rt_Bill_date=P_Rt_Billdate
                  and Ias_Rt_Bill_Mst_Br.ad_u_id=P_User_Id 
                  and Ias_Rt_Bill_Mst_Br.Rt_Bill_currency=P_Rt_Billcur
                  and Nvl(Ias_Rt_Bill_Mst_Br.cash_no,0)=Nvl(P_Cashno,0)
                  and Nvl(Ias_Rt_Bill_Mst_Br.c_code,0)=Nvl(P_Ccode,0)
                  Group by per,sc_no,Other_Charges_Br.a_code,a_cy,ac_rate,inv_item,Other_Charges_Br.brn_no,Other_Charges_Br.brn_year,
                           Other_Charges_Br.Cmp_No,Other_Charges_Br.brn_usr,Other_Charges_Br.Sc_A_Cy;
                Begin    
                     For i in c1 Loop          
                          rcd:=rcd+1;     
                       Begin         
                              Insert Into Other_Charges ( Bill_Type, 
                                                   Bill_Doc_Type, 
                                                   Bill_No, 
                                                   Bill_Ser, 
                                                   Sc_No, 
                                                   A_Code, 
                                                   A_Cy, 
                                                   Ac_Rate, 
                                                   Per, 
                                                   Amt, 
                                                   Inv_Item, 
                                                   Rcrd_No,
                                                   doc_date,
                                                   Vat_Amt, 
                                                   Vat_Per, 
                                                   Sc_Amt, 
                                                   Sc_Ac_Rate, 
                                                   Sc_A_Cy,
                                                   Brn_No,
                                                   Brn_Year,
                                                   Cmp_No,
                                                   Brn_usr)
                                          Values ( 3,
                                                    P_Rt_Billdoctype,
                                                    P_Rt_Billno,
                                                    P_Rt_Billser,
                                                    I.Sc_No,
                                                    I.A_Code,
                                                    I.A_Cy,
                                                    I.Ac_Rate,
                                                    I.Per,
                                                    I.Amt,
                                                    I.Inv_Item,
                                                    rcd,
                                                    P_Rt_Billdate,
                                                    I.Vat_Amt, 
                                                      I.Vat_Per, 
                                                      I.Sc_Amt, 
                                                      I.Sc_Ac_Rate, 
                                                      I.Sc_A_Cy,
                                                    I.Brn_No,
                                                    I.Brn_Year,
                                                    I.Cmp_No,
                                                    I.Brn_usr);
                     Exception
                          When No_Data_Found Then   
                                 Null;         
                          When Others Then        
                          rollback;
                          Raise_Application_Error (-20003,'Error When Post Others Charges , (Rt Sales) ,'||SqlErrm);
                      End;     
                 End Loop;    
                End;
------------------------------------------ Other Charges Items -------------------------------    
                Declare            
                  rcd Number:=0;
                    Cursor c1 Is
                       Select nvl(Sum(amt),0) amt,nvl(per,0) per,sc_no,Other_Charges_Items_Br.a_code,a_cy,ac_rate,i_code,
                              Itm_Unt,p_size,rcrd_no,Other_Charges_Items_Br.brn_no,Other_Charges_Items_Br.brn_year,Other_Charges_Items_Br.w_code,
                              Other_Charges_Items_Br.cc_code,Other_Charges_Items_Br.Pj_No,Other_Charges_Items_Br.Actv_No,
                              Other_Charges_Items_Br.Cmp_No,Other_Charges_Items_Br.brn_usr
                         From Ias_Rt_Bill_Mst_Br,Other_Charges_Items_Br
                        where Ias_Rt_Bill_Mst_Br.Rt_Bill_ser= Other_Charges_Items_Br.Bill_ser 
                          and Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_Type<>4
                          and Other_Charges_Items_Br.Bill_type=3
                          and nvl(Ias_Rt_Bill_Mst_Br.Rt_Bill_post,0)=0
                          and nvl(Ias_Rt_Bill_Mst_Br.Stand_By,0)=0
                          and Ias_Rt_Bill_Mst_Br.Rt_Bill_date=P_Rt_Billdate
                        --  And Nvl(Ias_Rt_Bill_Mst_Br.W_Code,0) Between Nvl(V_F_Wcode,Nvl(Ias_Rt_Bill_Mst_Br.W_Code,0)) And Nvl(V_T_Wcode,Nvl(Ias_Rt_Bill_Mst_Br.W_Code,0))
                          and Ias_Rt_Bill_Mst_Br.ad_u_id=P_User_Id 
                          and Ias_Rt_Bill_Mst_Br.Rt_Bill_currency=P_Rt_Billcur
                          and Nvl(Ias_Rt_Bill_Mst_Br.cash_no,0)=Nvl(P_Cashno,0)
                          and Nvl(Ias_Rt_Bill_Mst_Br.c_code,0)=Nvl(P_Ccode,0)
                          Group by per,sc_no,Other_Charges_Items_Br.a_code,a_cy,ac_rate,i_code,Itm_Unt,p_size ,rcrd_no,Other_Charges_Items_Br.brn_no,
                          Other_Charges_Items_Br.brn_year,Other_Charges_Items_Br.w_code,Other_Charges_Items_Br.cc_code,
                          Other_Charges_Items_Br.Pj_No,Other_Charges_Items_Br.Actv_No,
                                   Other_Charges_Items_Br.Cmp_No,Other_Charges_Items_Br.brn_usr;
                    Begin                        
                        For j in c1 Loop
                          Begin            
                             rcd:=rcd+1;     
                              Insert Into Other_Charges_Items ( Bill_TYPE, 
                                                                      Bill_DOC_TYPE, 
                                                                      Bill_NO, 
                                                                      Bill_SER, 
                                                                      SC_NO, 
                                                                      A_CODE, 
                                                                      A_Cy, 
                                                                      AC_RATE, 
                                                                      PER, 
                                                                      AMT, 
                                                                      I_CODE, 
                                                                      Itm_Unt, 
                                                                      P_SIZE,
                                                                 RCRD_NO,
                                                                 brn_no,
                                                                 brn_year,
                                                                 w_code,
                                                                 cc_code,
                                                                 pj_no,
                                                                 actv_no,
                                                                 Cmp_No,
                                                               Brn_usr )
                                                             Values ( 3,
                                                                      P_Rt_Billdoctype,
                                                                      P_Rt_Billno,
                                                                      P_Rt_Billser,
                                                                      j.sc_no,
                                                                      j.a_code,
                                                                      j.a_cy,
                                                                      j.ac_rate,
                                                                      j.per,
                                                                      j.amt,
                                                                      j.i_code,
                                                                      j.Itm_Unt,
                                                                      j.p_size,
                                                                         rcd,
                                                                 j.brn_no,
                                                                 j.brn_year,
                                                                 j.w_code,
                                                                 j.cc_code,
                                                                 j.pj_no,
                                                                 j.actv_no,
                                                                 J.Cmp_No,
                                                               J.Brn_usr);
                         Exception
                              When No_Data_Found Then   
                                 Null;         
                          When Others Then        
                         rollback;
                          Raise_Application_Error (-20004,'Error When Post Others Charges , (Rt Sales) ,'||SqlErrm);
                          End;               
                 End Loop;    
                End;
     End If;
END Insert_Other_Charges_Sr;                                      
--##-------------------------------------------------------------------------------------##--
PROCEDURE Check_Avl_Qty ( P_Doc_Type Number) IS
BEGIN
--##-------------------------------------------------------------------------------------##--       
  Execute Immediate 'Delete Table Ias_Pos_Minus_Qty_Tmp' ;
  ----------------------------------------------------------------------------------------
  If P_Doc_Type=1 Then            
             Insert Into Ias_pos_minus_qty_Tmp(I_Code ,Itm_Unt,w_code ,expire_date,batch_no,p_qty,avl_qty,Brn_No)
                Select I_code ,Itm_Unt,w_code,expire_date,batch_no,p_qty,avl_qty,Brn_No From(
                            Select Ias_Bill_Dtl_Br.I_code ,
                                   Ias_Itm_Pkg.Get_Icode_Min_Unit(Ias_Bill_Dtl_Br.I_code ) Itm_Unt,
                                   Ias_Bill_Dtl_Br.w_code,
                                   To_Date(Ias_Bill_Dtl_Br.Expire_Date,'DD/MM/YYYY') Expire_Date,
                                   Ias_Bill_Dtl_Br.Batch_No,
                                   Sum(Nvl(Ias_Bill_Dtl_Br.p_qty,0)+(Nvl(Ias_Bill_Dtl_Br.Free_Qty,0)*Nvl(Ias_Bill_Dtl_Br.P_Size,1))) p_qty,           
                                     Nvl(Get_Icode_Avlqty ( Ias_Bill_Dtl_Br.I_Code,
                                                            1,
                                                            Ias_Bill_Dtl_Br.W_Code,
                                                            To_Date(Ias_Bill_Dtl_Br.Expire_Date,'DD/MM/YYYY'),
                                                            Ias_Bill_Dtl_Br.Batch_No),0) Avl_Qty,Ias_Bill_Mst_Br.Brn_No
                                 From Ias_Bill_Mst_Br ,Ias_Bill_Dtl_Br
                                Where Ias_Bill_Mst_Br.Bill_Ser=Ias_Bill_Dtl_Br.Bill_Ser                          
                                  And Exists (Select 1 From Ias_Bill_Mst_Br_Tmp Where Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser And RowNum <=1 )
                                  And nvl(Ias_Bill_Dtl_Br.Service_Item,0)=0
                            Group by Ias_Bill_Dtl_Br.I_code,Ias_Bill_Dtl_Br.W_code, To_Date(Ias_Bill_Dtl_Br.Expire_Date,'DD/MM/YYYY'), Ias_Bill_Dtl_Br.Batch_No,Ias_Bill_Mst_Br.Brn_No)
                            Where nvl(Avl_Qty,0)-nvl(p_qty,0)< 0 ;
  ElsIf P_Doc_Type = 6 Then            
             Insert Into Ias_pos_minus_qty_Tmp(I_code ,Itm_Unt,w_code ,expire_date,batch_no,p_qty,avl_qty,Brn_No)
                Select I_code ,Itm_Unt,w_code,expire_date,batch_no,p_qty,avl_qty,Brn_No From(
                            Select Ias_Outgoing_Dtl_Br.I_code ,
                                   Ias_Itm_Pkg.Get_Icode_Min_Unit(Ias_Outgoing_Dtl_Br.I_code ) Itm_Unt ,
                                   Ias_Outgoing_Dtl_Br.w_code,
                                   To_Date(Ias_Outgoing_Dtl_Br.Expire_Date,'DD/MM/YYYY') Expire_Date,
                                   Ias_Outgoing_Dtl_Br.batch_no,
                                   Sum(Nvl(Ias_Outgoing_Dtl_Br.p_qty,0)) p_qty,           
                                     Nvl(Get_Icode_Avlqty ( Ias_Outgoing_Dtl_Br.I_Code,
                                                            1,
                                                            Ias_Outgoing_Dtl_Br.W_Code,
                                                            To_Date(Ias_Outgoing_Dtl_Br.Expire_Date,'DD/MM/YYYY'),
                                                            Ias_Outgoing_Dtl_Br.Batch_No),0) Avl_Qty,Ias_Outgoing_Dtl_Br.Brn_No
                                 From Ias_Outgoing_Mst_Br ,Ias_Outgoing_Dtl_Br
                                Where Ias_Outgoing_Mst_Br.Out_Ser=Ias_Outgoing_Dtl_Br.Out_Ser
                                  And Exists (Select 1 From Ias_Outgoing_Mst_Br_Tmp Where Out_Ser = Ias_Outgoing_Mst_Br.Out_Ser And RowNum <=1  )                          
                                  And nvl(Ias_Outgoing_Mst_Br.Out_post,0)=0                                                       
                                    And nvl(Ias_Outgoing_Mst_Br.Hung,0)=0 
                            Group by Ias_Outgoing_Dtl_Br.I_code,Ias_Outgoing_Dtl_Br.W_code, To_Date(Ias_Outgoing_Dtl_Br.Expire_Date,'DD/MM/YYYY'), Ias_Outgoing_Dtl_Br.Batch_No,Ias_Outgoing_Dtl_Br.Brn_No)
                            Where nvl(Avl_Qty,0)-nvl(p_qty,0)< 0 ;                            
  ElsIf P_Doc_Type=7 Then                                      
      Insert Into Ias_pos_minus_qty_Tmp(I_code ,Itm_Unt,w_code ,expire_date,batch_no,p_qty,avl_qty,Brn_No)
                Select I_code ,Itm_Unt,w_code,expire_date,batch_no,p_qty,avl_qty,Brn_No From(
                            Select Ias_Whtrns_Dtl_Br.I_code ,
                                   Ias_Itm_Pkg.Get_Icode_Min_Unit(Ias_Whtrns_Dtl_Br.I_code ) Itm_Unt ,
                                   Ias_Whtrns_Dtl_Br.w_code,
                                   To_Date(Ias_Whtrns_Dtl_Br.Expire_Date,'DD/MM/YYYY') Expire_Date,
                                   batch_no,
                                   Sum(Nvl(Ias_Whtrns_Dtl_Br.p_qty,0)) p_qty,           
                                     Nvl(Get_Icode_Avlqty ( Ias_Whtrns_Dtl_Br.I_Code,
                                                            1,
                                                            Ias_Whtrns_Dtl_Br.W_Code,
                                                            To_Date(Ias_Whtrns_Dtl_Br.Expire_Date,'DD/MM/YYYY'),
                                                            Ias_Whtrns_Dtl_Br.Batch_No),0) Avl_Qty,Ias_Whtrns_Dtl_Br.Brn_No
                                 From Ias_Whtrns_Mst_Br ,Ias_Whtrns_Dtl_Br
                                Where Ias_Whtrns_Mst_Br.Tr_Ser=Ias_Whtrns_Dtl_Br.Tr_Ser                          
                                  And Exists (Select 1 From Ias_Whtrns_Mst_Br_Tmp Where Tr_Ser = Ias_Whtrns_Mst_Br.Tr_Ser And RowNum <=1  )
                                  And Ias_Whtrns_Mst_Br.Tr_Inout_Type=1                                   
                                  And nvl(Ias_Whtrns_Mst_Br.Tr_post,0)=0                                  
                                  And nvl(Ias_Whtrns_Mst_Br.Hung,0)=0 
                            Group by Ias_Whtrns_Dtl_Br.I_code,Ias_Whtrns_Dtl_Br.W_code, To_Date(Ias_Whtrns_Dtl_Br.Expire_Date,'DD/MM/YYYY'), Ias_Whtrns_Dtl_Br.Batch_No,Ias_Whtrns_Dtl_Br.Brn_No)
                            Where nvl(Avl_Qty,0)-nvl(p_qty,0)< 0 ; 
  End If;   
  
  Exception When Others Then Null;
--##-------------------------------------------------------------------------------------##--           
END Check_Avl_Qty ;
--##-------------------------------------------------------------------------------------##--
Function Get_Bill_No (  P_Invoicing_Serials In Number   ,
                        P_Si_Type           In Number   ,
                        P_Cc_Code           In Varchar2 ,                        
                        P_Bill_Doc_Type     In Number   ,
                        P_W_Code            In Number   ,
                        P_Brn_No            In Number   ) Return Number Is  
  V_Bill_No  Number;
Begin    
--##-------------------------------------------------------------------------------------##--  

       
       If Nvl(P_Invoicing_Serials,0) = 1 Then -- Accumulated
           Select Nvl(Max(To_Number(Bill_No)),0) +1 
             Into V_Bill_No
           From Ias_Bill_Mst 
        Where Brn_No =P_Brn_No;
     -------------------------------------------------------------------------------------           
       Elsif Nvl(P_Invoicing_Serials,0) = 2 Then -- Bill_Doc_Type             
              Select Nvl(Max(To_Number(Bill_No)),0) +1 Into V_Bill_No From Ias_Bill_Mst 
               Where Bill_Doc_Type = P_Bill_Doc_Type
                 And Brn_No =P_Brn_No;
         -------------------------------------------------------------------------------------             
       Elsif Nvl(P_Invoicing_Serials,0) = 3 Then -- By Cost_Center        
              Select Nvl(Max(To_Number(Bill_No)),0)+1 Into V_Bill_No From Ias_Bill_Mst 
               Where Cc_Code In 
                    (Select Cc_Code From Cost_Centers
                      Where Nvl(C_Sr,0)=(Select Nvl(C_Sr,0) From Cost_Centers 
                                          Where Cc_Code=P_Cc_Code))
                  And Brn_No =P_Brn_No;                        
         -------------------------------------------------------------------------------------    
        Elsif Nvl(P_Invoicing_Serials,0) = 6 Then -- Bty Cost_Center  + Bill_Doc_Type          
            Select Nvl(Max(To_Number(Bill_No)),0) +1 
              Into V_Bill_No
            From Ias_Bill_Mst 
             Where Bill_Doc_Type = P_Bill_Doc_Type
               And Cc_Code=P_Cc_Code
               And Brn_No =P_Brn_No;
         ------------------------------------------------------------------------------------- 
         Elsif Nvl(P_Invoicing_Serials,0) = 4 Then --Warehouse              
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 Into V_Bill_No From Ias_Bill_Mst 
                   --Where W_Code=V_W_Code;              
                   Where W_Code In 
                    (Select W_Code From Warehouse_Details
                      Where Nvl(W_Ser,0)=(Select Nvl(W_Ser,0) From Warehouse_Details 
                                          Where W_Code= P_W_Code))
                 And Brn_No =P_Brn_No;                         
          -------------------------------------------------------------------------------------    
            Elsif Nvl(P_Invoicing_Serials,0) = 5 Then --Warehouse + Bill_Doc_Type                
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Bill_Mst
                   Where Bill_Doc_Type=P_Bill_Doc_Type 
                     And W_Code =P_W_Code
                     And Brn_No =P_Brn_No;  
              -------------------------------------------------------------------------------------           
           Elsif Nvl(P_Invoicing_Serials,0) = 7 Then -- Si_Type             
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 Into V_Bill_No From Ias_Bill_Mst 
                   Where Si_Type=P_Si_Type
                     And Brn_No =P_Brn_No;       
         -------------------------------------------------------------------------------------    
            Elsif Nvl(P_Invoicing_Serials,0) = 8 Then --Si_Type + Warehouse 
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Bill_Mst
                   Where Si_Type=P_Si_Type
                     And W_Code=P_W_Code 
                     And Brn_No = P_Brn_No;                 
             -------------------------------------------------------------------------------------    
            Elsif Nvl(P_Invoicing_Serials,0) = 9 Then   --Si_Type + Warehouse + Pay Type                
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Bill_Mst
                   Where Si_Type       = P_Si_Type
                     And W_Code        = P_W_Code 
                     And Bill_Doc_Type = P_Bill_Doc_Type
                     And Brn_No = P_Brn_No;            
                
           End If;
    
    
    Return(V_Bill_No);
 Exception When Others Then
      RollBack;
      Raise_Application_Error (-20001,' Err. In Get Bill No ');          
End Get_Bill_No ;
--##--------------------------------------------------------------------------------##--
Function Get_Bill_No_Br (  P_Invs In Number   ,
                           P_Si_Type           In Number   ,
                           P_Cc_Code           In Varchar2 ,                        
                           P_Bill_Doc_Type     In Number   ,
                           P_W_Code            In Number   ,
                           P_Brn_No            In Number   ) Return Number Is  
  V_Bill_No  Number;
Begin    
--##-------------------------------------------------------------------------------------##--        
       If Nvl(P_Invs,0) = 1 Then -- Accumulated
           Select Nvl(Max(To_Number(Bill_No)),0) +1 
             Into V_Bill_No
           From Ias_Bill_Mst_Br 
        Where Brn_No =P_Brn_No;
     -------------------------------------------------------------------------------------           
       Elsif Nvl(P_Invs,0) = 2 Then -- Bill_Doc_Type             
              Select Nvl(Max(To_Number(Bill_No)),0) +1 
               Into V_Bill_No From Ias_Bill_Mst_Br 
               Where Bill_Doc_Type = P_Bill_Doc_Type
                 And Brn_No =P_Brn_No;
         -------------------------------------------------------------------------------------             
       Elsif Nvl(P_Invs,0) = 3 Then -- By Cost_Center        
              Select Nvl(Max(To_Number(Bill_No)),0)+1 
              Into V_Bill_No 
              From Ias_Bill_Mst_Br 
               Where Cc_Code In 
                    (Select Cc_Code From Cost_Centers
                      Where Nvl(C_Sr,0)=(Select Nvl(C_Sr,0) From Cost_Centers 
                                          Where Cc_Code=P_Cc_Code))
                  And Brn_No =P_Brn_No;                        
         -------------------------------------------------------------------------------------    
        Elsif Nvl(P_Invs,0) = 6 Then -- Bty Cost_Center  + Bill_Doc_Type          
            Select Nvl(Max(To_Number(Bill_No)),0) +1 
              Into V_Bill_No
            From Ias_Bill_Mst_Br 
             Where Bill_Doc_Type = P_Bill_Doc_Type
               And Cc_Code=P_Cc_Code
               And Brn_No =P_Brn_No;
         ------------------------------------------------------------------------------------- 
         Elsif Nvl(P_Invs,0) = 4 Then --Warehouse              
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 
                    Into V_Bill_No 
                   From Ias_Bill_Mst_Br 
                   --Where W_Code=V_W_Code;              
                   Where W_Code In 
                    (Select W_Code From Warehouse_Details
                      Where Nvl(W_Ser,0)=(Select Nvl(W_Ser,0) From Warehouse_Details 
                                          Where W_Code= P_W_Code))
                 And Brn_No =P_Brn_No;                         
          -------------------------------------------------------------------------------------    
            Elsif Nvl(P_Invs,0) = 5 Then --Warehouse + Bill_Doc_Type                
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Bill_Mst_Br
                   Where Bill_Doc_Type=P_Bill_Doc_Type 
                     And W_Code =P_W_Code
                     And Brn_No =P_Brn_No;  
              -------------------------------------------------------------------------------------           
           Elsif Nvl(P_Invs,0) = 7 Then -- Si_Type             
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 
                  Into V_Bill_No
                   From Ias_Bill_Mst_Br 
                   Where Si_Type=P_Si_Type
                     And Brn_No =P_Brn_No;       
         -------------------------------------------------------------------------------------    
            Elsif Nvl(P_Invs,0) = 8 Then --Si_Type + Warehouse 
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Bill_Mst_Br
                   Where Si_Type=P_Si_Type
                     And W_Code=P_W_Code 
                     And Brn_No = P_Brn_No;                 
             -------------------------------------------------------------------------------------    
            Elsif Nvl(P_Invs,0) = 9 Then   --Si_Type + Warehouse + Pay Type                
                  Select Nvl(Max(To_Number(Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Bill_Mst_Br
                   Where Si_Type       = P_Si_Type
                     And W_Code        = P_W_Code 
                     And Bill_Doc_Type = P_Bill_Doc_Type
                     And Brn_No = P_Brn_No;            
                
           End If;
    
    
    Return(V_Bill_No);
 Exception When Others Then
      RollBack;
      Raise_Application_Error (-20001,' Err. In Get Bill No ');          
End Get_Bill_No_Br ;
--##--------------------------------------------------------------------------------##--
Function Get_Bill_Ser ( P_Invs In Number ,
                        P_Si_Type           In Number,
                        P_Cc_Code           In Varchar2,
                        P_Bill_No           In Number, 
                        P_Bill_Doc_Type     In Number,
                        P_W_Code            In Number,
                        P_Brn_No            In Number,
                        P_Brn_Year          IN Number) Return Number Is
  V_Csr   Number;
  V_Ccno  Number;
  V_Bser  Number;
  V_Wser   Number;
Begin
--##--------------------------------------------------------------------------------##--       
  If Nvl(P_Invs,0) =3 Then      
         V_Csr:=Ias_Cc_Code_Pkg.Get_Cc_Ser(P_Cc_Code);
         V_Ccno:=Ias_Cc_Code_Pkg.Get_Cc_No(P_Cc_Code);                  
  Elsif Nvl(P_Invs,0) = 4 Then     
           V_Wser := Ias_Wcode_Pkg.Get_Wc_Ser(P_W_Code);              
    End If;               
--##--------------------------------------------------------------------------------##--            
    If Nvl(P_Invs,0) = 1 Then
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||104||P_Bill_No;
    Elsif Nvl(P_Invs,0) = 2 Then
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||Ltrim(Lpad(P_Bill_Doc_Type,2,'0'))||P_Bill_No;
    Elsif Nvl(P_Invs,0) = 4 Then       
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||104||Ltrim(P_Bill_No)||Ltrim(Lpad(V_Wser,5,'0'));
    Elsif Nvl(P_Invs,0) =5 Then
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||104||Ltrim(Lpad(P_Bill_Doc_Type,2,'0'))||P_Bill_No||Ltrim(Lpad(P_W_Code,10,'0'));
    Elsif Nvl(P_Invs,0) = 3 Then
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||104||P_Bill_No||Ltrim(Lpad(V_Csr,5,'0'));
    Elsif Nvl(P_Invs,0) = 6 Then        
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||104||Ltrim(Lpad(P_Bill_Doc_Type,2,'0'))||P_Bill_No||Ltrim(Lpad(V_Ccno,5,'0'));
    Elsif Nvl(P_Invs,0) = 7 Then        
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||Ltrim(Lpad(P_Si_Type,5,'0'))||P_Bill_No;
    Elsif Nvl(P_Invs,0) = 8 Then        
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||104||Ltrim(Lpad(P_Si_Type,5,'0'))||P_Bill_No||Ltrim(Lpad(P_W_Code,10,'0'));
    Elsif Nvl(P_Invs,0) = 9 Then        
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||104||Ltrim(Lpad(P_Bill_Doc_Type,2,'0'))||Ltrim(Lpad(P_Si_Type,5,'0'))||P_Bill_No||Ltrim(Lpad(P_W_Code,10,'0'));          
    ElsIf P_Invs =10 Then        
       V_Bser:=P_Brn_Year||Lpad(P_brn_no,6,'0')||104||ltrim(Lpad(P_Bill_doc_type,2,'0'))||ltrim(Lpad(P_Si_Type,5,'0'))||P_Bill_No;   
    Else
       V_Bser:=P_Brn_Year||Lpad(P_Brn_No,6,'0')||104||Ltrim(Lpad(P_Bill_Doc_Type,2,'0'))||P_Bill_No||Ltrim(Lpad(P_W_Code,10,'0'))||Ltrim(To_Char(To_Number(V_Ccno),'00000'));
    End If;
Return(V_Bser);    
 Exception When Others Then
      RollBack;
      Raise_Application_Error (-20001,' Err. In Get Bill serial ');          
End Get_Bill_Ser ;

 FUNCTION Get_Rt_Bill_No ( P_Invs_Sr          In Number,
                           P_sr_Type          In Number,
                           P_Cc_Code          In Varchar2,                        
                           P_Bill_doc_type    In Number,
                           P_W_Code           In Number,
                           P_brn_no           In number) Return Number  Is  
  V_Bill_No  Number;
Begin    
--##-------------------------------------------------------------------------------------##--        
       If P_Invs_Sr=1 Then -- Accumulated
           Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
             Into V_Bill_No
           From Ias_Rt_Bill_Mst
          Where Brn_No =P_brn_no;
     -------------------------------------------------------------------------------------           
       Elsif P_Invs_Sr=2 Then -- Rt_Bill_Doc_Type             
              Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 Into V_Bill_No From Ias_Rt_Bill_Mst 
               Where Rt_Bill_Doc_Type=P_Bill_Doc_Type
                 And Brn_No =P_brn_no;
         -------------------------------------------------------------------------------------             
       Elsif P_Invs_Sr=3 Then -- By Cost_Center        
              Select Nvl(Max(To_Number(Rt_Bill_No)),0)+1 Into V_Bill_No From Ias_Rt_Bill_Mst 
               Where Cc_Code In 
                    (Select Cc_Code From Cost_Centers
                      Where Nvl(C_Sr,0)=(Select Nvl(C_Sr,0) From Cost_Centers 
                                          Where Cc_Code=P_Cc_Code))
                And Brn_No =P_brn_no;                           
         -------------------------------------------------------------------------------------    
        Elsif P_Invs_Sr=6 Then -- Bty Cost_Center  + Rt_Bill_Doc_Type          
            Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
              Into V_Bill_No
            From Ias_Rt_Bill_Mst 
             Where Rt_Bill_Doc_Type=P_Bill_Doc_Type
               And Cc_Code=P_Cc_Code
               And Brn_No =P_brn_no;
         ------------------------------------------------------------------------------------- 
         Elsif P_Invs_Sr=4 Then --Warehouse              
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 Into V_Bill_No From Ias_Rt_Bill_Mst 
                   --Where W_Code=P_W_Code;              
                   Where W_Code In 
                    (Select W_Code From Warehouse_Details
                      Where Nvl(W_Ser,0)=(Select Nvl(W_Ser,0) From Warehouse_Details 
                                          Where W_Code=P_W_Code))
                And Brn_No =P_brn_no;                          
          -------------------------------------------------------------------------------------    
            Elsif P_Invs_Sr=5 Then --Warehouse + Rt_Bill_Doc_Type                
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Rt_Bill_Mst
                   Where Rt_Bill_Doc_Type=P_Bill_Doc_Type 
                     And W_Code=P_W_Code
                     And Brn_No =P_brn_no;            
              -------------------------------------------------------------------------------------           
          Elsif P_Invs_Sr=7 Then -- Sr_Type             
              Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 Into V_Bill_No From Ias_Rt_Bill_Mst 
               Where Sr_Type=P_Sr_Type
                 And Brn_No =P_brn_no;       
            -------------------------------------------------------------------------------------    
            Elsif P_Invs_Sr=8 Then --Si_Type + Warehouse 
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Rt_Bill_Mst
                   Where Sr_Type=P_Sr_Type
                     And W_Code=P_W_Code 
                     And Brn_No = P_brn_no;                 
             -------------------------------------------------------------------------------------    
            Elsif P_Invs_Sr=9 Then   --Si_Type + Warehouse + Pay Type                
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Rt_Bill_Mst
                   Where Sr_Type=P_Sr_Type
                     And W_Code=P_W_Code 
                     And Rt_Bill_Doc_Type=P_Bill_Doc_Type
                     And Brn_No = P_brn_no;
               -------------------------------------------------------------------------------------    
             Elsif P_Invs_Sr=10 Then   --Si_Type +  Pay Type                
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Rt_Bill_Mst
                   Where Sr_Type=P_Sr_Type
                     And Rt_Bill_Doc_Type=P_Bill_Doc_Type
                     And Brn_No = P_brn_no;                                              
            End If;
    
    
    Return(V_Bill_No);
 Exception When Others Then
    RollBack;
    Raise_Application_Error (-20001,' Err. In Rt Bill No.');                  

End;

FUNCTION Get_Rt_Bill_No_Br ( P_Invs_Sr          In Number,
                               P_sr_Type          In Number,
                               P_Cc_Code          In Varchar2,                        
                               P_Bill_doc_type    In Number,
                               P_W_Code           In Number,
                               P_brn_no           In number) Return Number  Is  
  V_Bill_No  Number;
Begin    
--##-------------------------------------------------------------------------------------##--        
       If P_Invs_Sr=1 Then -- Accumulated
           Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
             Into V_Bill_No
           From Ias_Rt_Bill_Mst_Br
          Where Brn_No =P_brn_no;
     -------------------------------------------------------------------------------------           
       Elsif P_Invs_Sr=2 Then -- Rt_Bill_Doc_Type             
              Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 Into V_Bill_No From Ias_Rt_Bill_Mst_Br 
               Where Rt_Bill_Doc_Type=P_Bill_Doc_Type
                 And Brn_No =P_brn_no;
         -------------------------------------------------------------------------------------             
       Elsif P_Invs_Sr=3 Then -- By Cost_Center        
              Select Nvl(Max(To_Number(Rt_Bill_No)),0)+1 Into V_Bill_No From Ias_Rt_Bill_Mst_Br 
               Where Cc_Code In 
                    (Select Cc_Code From Cost_Centers
                      Where Nvl(C_Sr,0)=(Select Nvl(C_Sr,0) From Cost_Centers 
                                          Where Cc_Code=P_Cc_Code))
                And Brn_No =P_brn_no;                           
         -------------------------------------------------------------------------------------    
        Elsif P_Invs_Sr=6 Then -- Bty Cost_Center  + Rt_Bill_Doc_Type          
            Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
              Into V_Bill_No
            From Ias_Rt_Bill_Mst_Br 
             Where Rt_Bill_Doc_Type=P_Bill_Doc_Type
               And Cc_Code=P_Cc_Code
               And Brn_No =P_brn_no;
         ------------------------------------------------------------------------------------- 
         Elsif P_Invs_Sr=4 Then --Warehouse              
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 Into V_Bill_No From Ias_Rt_Bill_Mst_Br 
                   --Where W_Code=P_W_Code;              
                   Where W_Code In 
                    (Select W_Code From Warehouse_Details
                      Where Nvl(W_Ser,0)=(Select Nvl(W_Ser,0) From Warehouse_Details 
                                          Where W_Code=P_W_Code))
                And Brn_No =P_brn_no;                          
          -------------------------------------------------------------------------------------    
            Elsif P_Invs_Sr=5 Then --Warehouse + Rt_Bill_Doc_Type                
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Rt_Bill_Mst_Br
                   Where Rt_Bill_Doc_Type=P_Bill_Doc_Type 
                     And W_Code=P_W_Code
                     And Brn_No =P_brn_no;            
              -------------------------------------------------------------------------------------           
          Elsif P_Invs_Sr=7 Then -- Sr_Type             
              Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 Into V_Bill_No From Ias_Rt_Bill_Mst_Br 
               Where Sr_Type=P_Sr_Type
                 And Brn_No =P_brn_no;       
            -------------------------------------------------------------------------------------    
            Elsif P_Invs_Sr=8 Then --Si_Type + Warehouse 
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Rt_Bill_Mst_Br
                   Where Sr_Type=P_Sr_Type
                     And W_Code=P_W_Code 
                     And Brn_No = P_brn_no;                 
             -------------------------------------------------------------------------------------    
            Elsif P_Invs_Sr=9 Then   --Si_Type + Warehouse + Pay Type                
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Rt_Bill_Mst_Br
                   Where Sr_Type=P_Sr_Type
                     And W_Code=P_W_Code 
                     And Rt_Bill_Doc_Type=P_Bill_Doc_Type
                     And Brn_No = P_brn_no;
               -------------------------------------------------------------------------------------    
             Elsif P_Invs_Sr=10 Then   --Si_Type +  Pay Type                
                  Select Nvl(Max(To_Number(Rt_Bill_No)),0) +1 
                   Into V_Bill_No
                   From Ias_Rt_Bill_Mst_Br
                   Where Sr_Type=P_Sr_Type
                     And Rt_Bill_Doc_Type=P_Bill_Doc_Type
                     And Brn_No = P_brn_no;                                              
            End If;
    
    
    Return(V_Bill_No);
 Exception When Others Then
    RollBack;
    Raise_Application_Error (-20002,' Err. In Rt Bill No.');                  

End;

FUNCTION Get_Rt_Bill_Ser (  P_Invs_Sr       IN Number,
                            P_sr_Type       IN Number,
                            P_Cc_Code       IN Varchar2,
                            P_Rt_Bill_No    IN Number, 
                            P_Bill_doc_type IN Number,
                            P_W_Code        IN Number,
                            P_brn_no        IN number,
                            P_Brn_Year      IN Number) Return Number Is
  V_Csr   Number;
  V_CcNo  Number;
  V_Bill_Ser  Number;
  V_Wser   Number;
BEGIN
--##--------------------------------------------------------------------------------##--      
  If P_Invs_Sr In (3,6) Then      
         V_Csr:=ias_cc_code_pkg.Get_Cc_ser(P_Cc_Code);
         V_CcNo:=ias_cc_code_pkg.Get_Cc_no(P_Cc_Code);                  
    ElsIf P_Invs_Sr In (4,5) Then     
     V_Wser := IAS_Wcode_Pkg.Get_Wc_Ser(P_W_Code);              
    End If;               
--##--------------------------------------------------------------------------------##--            
    If P_Invs_Sr=1 Then
       V_Bill_Ser:=P_Brn_Year||lpad(P_brn_no,6,'0')||105||P_Rt_Bill_No;
    ElsIf P_Invs_Sr=2 Then
       V_Bill_Ser:=P_Brn_Year||lpad(P_brn_no,6,'0')||105||ltrim(Lpad(P_Bill_doc_type,2,'0'))||P_Rt_Bill_No;
    ElsIf P_Invs_Sr =4 Then
       V_Bill_Ser:=P_Brn_Year||lpad(P_brn_no,6,'0')||105||ltrim(P_Rt_Bill_No)||ltrim(lpad(V_Wser,5,'0'));
    ElsIf P_Invs_Sr =5 Then
       V_Bill_Ser:=P_Brn_Year||lpad(P_brn_no,6,'0')||105||ltrim(Lpad(P_Bill_doc_type,2,'0'))||P_Rt_Bill_No||ltrim(Lpad(P_W_Code,10,'0'));
    ElsIf P_Invs_Sr =3 Then
       V_Bill_Ser:=P_Brn_Year||lpad(P_brn_no,6,'0')||105||P_Rt_Bill_No||ltrim(lpad(V_Csr,5,'0'));
    ElsIf P_Invs_Sr =6 Then        
       V_Bill_Ser:=P_Brn_Year||lpad(P_brn_no,6,'0')||105||ltrim(Lpad(P_Bill_doc_type,2,'0'))||P_Rt_Bill_No||ltrim(lpad(V_CcNo,5,'0'));
    ElsIf P_Invs_Sr=7 Then
       V_Bill_Ser:=P_Brn_Year||lpad(P_brn_no,6,'0')||105||ltrim(Lpad(P_sr_Type,5,'0'))||P_Rt_Bill_No;       
    ElsIf P_Invs_Sr =8 Then        
    V_Bill_Ser:=P_Brn_Year||Lpad(P_brn_no,6,'0')||105||ltrim(Lpad(P_sr_Type,5,'0'))||P_Rt_Bill_No||ltrim(Lpad(P_W_Code,10,'0'));
  ElsIf P_Invs_Sr =9 Then        
    V_Bill_Ser:=P_Brn_Year||Lpad(P_brn_no,6,'0')||105||ltrim(Lpad(P_Bill_doc_type,2,'0'))||ltrim(Lpad(P_sr_Type,5,'0'))||P_Rt_Bill_No||ltrim(Lpad(P_W_Code,10,'0'));
  ElsIf P_Invs_Sr =10 Then        
    V_Bill_Ser:=P_Brn_Year||Lpad(P_brn_no,6,'0')||105||ltrim(Lpad(P_Bill_doc_type,2,'0'))||ltrim(Lpad(P_sr_Type,5,'0'))||P_Rt_Bill_No;
    Else
      V_Bill_Ser:=P_Brn_Year||lpad(P_brn_no,6,'0')||105||ltrim(Lpad(P_Bill_doc_type,2,'0'))||P_Rt_Bill_No||ltrim(Lpad(P_W_Code,10,'0'))||ltrim(to_char(to_Number(V_CcNo),'00000'));
    End If;
Return(V_Bill_Ser);    
 Exception When Others Then
      Raise_Application_Error (-20001,' Err. In Rt Bill Ser.');

--##--------------------------------------------------------------------------------##--          
END;
--##--------------------------------------------------------------------------------##--
Function Get_Gr_No_Br ( P_Brn_No    In  S_Brn.Brn_No%Type                 ,
                        P_Ser_Type  In  Ias_Para_Inv.Incoming_Serial%Type ,
                        P_Inc_Type  In  Gr_Note.Incom_Type%Type           ,
                        P_W_Code    In  Gr_Note.W_Code%Type               ) Return Number Is 
   V_Inc_No Gr_Note.Gr_No%Type ;
  Begin
     If P_Ser_Type = 1 Then  -- Accumulated
        Begin
         Select Nvl(Max(Gr_No),0)+1  
           Into V_Inc_No
            From Gr_Note_Br
             Where Brn_No = P_Brn_No
              And Pi_Type = 5 ;
        Exception
          When Others Then
           V_Inc_No := Null ;
        End ;
     ElsIf P_Ser_Type = 2 Then  -- By Warehouse 
        Begin
         Select Nvl(Max(Gr_No),0)+1  
           Into V_Inc_No
            From Gr_Note_Br
             Where Brn_No = P_Brn_No
             And Pi_Type  = 5
             And W_Code In 
                    (Select W_Code From Warehouse_Details
                      Where Nvl(W_Ser,0)=( Select Nvl(W_Ser,0) 
                                            From Warehouse_Details 
                                             Where W_Code = P_W_Code) ) ;
        Exception
          When Others Then
           V_Inc_No := Null ;
        End ;
     ElsIf P_Ser_Type = 3 Then  -- By Type
        Begin
         Select Nvl(Max(Gr_No),0)+1  
           Into V_Inc_No
            From Gr_Note_Br
             Where Brn_No     = P_Brn_No
              And  Pi_Type    = 5
              And  Incom_Type = P_Inc_Type ;
        Exception
          When Others Then
           V_Inc_No := Null ;
        End ;
     ElsIf P_Ser_Type = 4 Then  -- By Warehouse & Type
        Begin
         Select Nvl(Max(Gr_No),0)+1  
           Into V_Inc_No
            From Gr_Note_Br
             Where Brn_No     = P_Brn_No
              And  Pi_Type    = 5
              And  W_Code     = P_W_Code
              And  Incom_Type = P_Inc_Type ;
        Exception
          When Others Then
           V_Inc_No := Null ;
        End ;    
     End If ;
     Return(V_Inc_No);
 Exception
      When Others Then
      Raise_Application_Error (-20001,' Err. In Get Gr. No.');   
  End Get_Gr_No_Br ;
--##--------------------------------------------------------------------------------##--  
FUNCTION Get_Out_No_Br ( P_Brn_No    In  S_Brn.Brn_No%Type                 ,
                         P_Ser_Type  In  Ias_Para_Inv.Outgoing_Serial%Type ,
                         P_Out_Type  In  Ias_Outgoing_Mst.Out_Type%Type    ,
                         P_W_Code    In  Ias_Outgoing_Mst.W_Code%Type      ) Return Number Is 
   V_Out_No Ias_Outgoing_Mst.Out_No%Type ;
  Begin
     If P_Ser_Type = 1 Then -- Accumulated
        Begin
         Select Nvl(Max(Out_No),0)+1  
           Into V_Out_No
            From Ias_Outgoing_Mst_Br
             Where Brn_No     = P_Brn_No ;
        Exception
          When Others Then
           V_Out_No := Null ;
        End ;
     ElsIf P_Ser_Type = 2 Then -- By Warehouse 
        Begin
         Select Nvl(Max(Out_No),0)+1  
           Into V_Out_No
            From Ias_Outgoing_Mst_Br
             Where Brn_No     = P_Brn_No
              And  W_Code In 
                      (Select W_Code From Warehouse_Details
                         Where Nvl(W_Ser,0)=( Select Nvl(W_Ser,0) 
                                                From Warehouse_Details 
                                                 Where W_Code = P_W_Code) ) ;
        Exception
          When Others Then
           V_Out_No := Null ;
        End ;
     ElsIf P_Ser_Type = 3 Then  -- By Type
        Begin
         Select Nvl(Max(Out_No),0)+1  
           Into V_Out_No
            From Ias_Outgoing_Mst_Br
             Where Brn_No   = P_Brn_No
              And  Out_Type = P_Out_Type ;
        Exception
          When Others Then
           V_Out_No := Null ;
        End ;
     ElsIf P_Ser_Type = 4 Then  -- By Warehouse & Type
        Begin
         Select Nvl(Max(Out_No),0)+1  
           Into V_Out_No
            From Ias_Outgoing_Mst_Br
             Where Brn_No    = P_Brn_No
              And  W_Code    = P_W_Code
              And  Out_Type  = P_Out_Type ;
        Exception
          When Others Then
           V_Out_No := Null ;
        End ;    
     End If ;
     Return(V_Out_No);
 Exception
      When Others Then
      Raise_Application_Error (-20001,' Err. In Get Out. No. '); 
  End Get_Out_No_Br ;
--##-------------------------------------------------------------------------------------------------##--
Function Get_Out_Br_Ser (   P_Outgoing_Serial In Number ,
                            P_Out_Type        In Number,
                            P_Out_No          In Number, 
                            P_W_Code          In Number,
                            P_Brn_No          In Number,
                            P_Brn_Year        In Number) Return Number Is

  V_Out_Ser  Number;
  V_Out_No   Number;
Begin              
--##-------------------------------------------------------------------------------------------------##--            
    V_Out_No  := Get_Out_No_Br(P_Brn_No,P_Outgoing_Serial ,P_Out_Type,P_W_Code);                            
    
        If P_Outgoing_Serial = 1 Then
             V_Out_Ser  := P_Brn_Year||Lpad(P_Brn_No,6,'0')||109||P_out_no;
          ElsIf P_Outgoing_Serial = 2  Then
             V_Out_Ser  := P_Brn_Year||Lpad(P_Brn_No,6,'0')||109||Lpad(P_w_code  ,6,'0')||P_out_no;
        ElsIf P_Outgoing_Serial = 3 Then
              V_Out_Ser := P_Brn_Year||Lpad(P_Brn_No,6,'0')||109||Lpad(P_out_type,5,'0')||P_out_no;
          ElsIf P_Outgoing_Serial = 4 Then
              V_Out_Ser := P_Brn_Year||Lpad(P_Brn_No,6,'0')||109||Lpad(P_w_code  ,6,'0')||Lpad(P_out_type,5,'0')||P_out_no;    
          End If ;
Return(V_Out_Ser);    
 Exception When Others Then
      Raise_Application_Error (-20001,' Err. In Get Out serial ');          
End Get_Out_Br_Ser ;

Function Get_Gr_Br_Ser (   P_Incoming_Serial In Number ,
                           P_Inc_Type        In Number,
                           P_Inc_No          In Number, 
                           P_W_Code          In Number,
                           P_Brn_No          In Number,
                           P_Brn_Year        In Number) Return Number Is

  V_Inc_Ser  Number;
  V_Inc_No    Number;
Begin              
--##-------------------------------------------------------------------------------------------------##--            
    V_Inc_No  := Get_Gr_No_Br(P_Brn_No,P_Incoming_Serial ,P_Inc_Type,P_W_Code);                            
    If   P_Incoming_Serial       = 1 Then
         V_Inc_Ser  := P_Brn_Year||Lpad(P_Brn_No,6,'0')||108||V_Inc_No;
    Elsif P_Incoming_Serial    = 2  Then
         V_Inc_Ser  := P_Brn_Year||Lpad(P_Brn_No,6,'0')||108||Lpad(P_W_Code  ,6,'0')||P_Inc_No;
    Elsif P_Incoming_Serial    = 3 Then
         V_Inc_Ser := P_Brn_Year||Lpad(P_Brn_No,6,'0')||108||Lpad(P_Inc_Type,5,'0')||P_Inc_No;
    Elsif P_Incoming_Serial    = 4 Then
         V_Inc_Ser := P_Brn_Year||Lpad(P_Brn_No,6,'0')||108||Lpad(P_W_Code  ,6,'0')||Lpad(P_Inc_Type,5,'0')||V_Inc_No;    
    End If ;
Return(V_Inc_Ser);    
 Exception When Others Then
      Raise_Application_Error (-20001,' Err. In Get Gr Serial ');          
End Get_Gr_Br_Ser ;
--##-------------------------------------------------------------------------------------------------##--  
--##--------------------------------------------------------------------------------##--  
Procedure Post_Transfer_In  ( P_Doc_Ser  In Ias_Whtrns_Mst.Tr_Ser%Type   Default Null , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  Is    
     V_Cnt                       Number                       ;
     V_Sqlstr                    Varchar2(3000)               ;
     V_Sqlstr2                   Varchar2(3000)               ;
     V_Use_Price_Whtrns_Rec_Cost Ias_Para_Inv.Use_Price_Whtrns_Rec_Cost%Type ;
     V_Use_Itm_Attach            Ias_Para_Inv.Use_Itm_Attach%Type ;
     V_Costing_Type              Ias_Para_Inv.Costing_Type%Type ;
     V_Wtavg_Type                Ias_Para_Inv.Wtavg_Type%Type ;
     V_Stkcost                   Number                       ;
     V_Seq                       Number                       ;
     V_Cst                       Number                       ; 
     V_Wt_After                  Number                       ;
     V_Wt_Before                 Number                       ;
     V_Use_Attch                 Ias_Itm_Mst.Use_Attch%Type  ;
     V_Attch                     Ias_Itm_Attach%RowType       ;
     V_Rec_Attch                 Ias_Itm_Attach_Movement.Rec_Attch%Type ; 
     V_Tr_Type                   Number ;
     V_Wcode                     Number;  
     V_Stk_Cst_Frc               Number ;
     V_Lang_No                   Number:= P_Lang_No;
     V_Allow_Enter_Zero_Cost     Number;    
Begin  
--##------------------------------------------------------------------------------------##--
  If P_Lang_No Is Null Then    
    Begin
      Select Lang_No InTo V_Lang_No From Ias_Sys.Lang_Def Where Nvl(Flg_St,1)= 1 And Lang_Dflt=1 And Rownum<=1;
    Exception WHen Others Then
        V_Lang_No := 1;
    End;  
  ENd If;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      Select Nvl(Use_Price_Whtrns_Rec_Cost,0) ,
             Nvl(Costing_Type,0) ,
             Nvl(Wtavg_Type,0)   ,
             Nvl(Stkcost_Fraction ,6)  ,
             Nvl(Use_Itm_Attach ,0)   
        Into V_Use_Price_Whtrns_Rec_Cost ,
             V_Costing_Type              ,
             V_Wtavg_Type                ,
             V_Stk_Cst_Frc               ,
             V_Use_Itm_Attach          
       From Ias_Para_Inv ;
  Exception WHen Others Then
    RollBack;
    Raise_Application_Error(-20001,'Error When Select From Para In Post_Transfer_In (8) '||Chr(13)||SqlErrm);
  End;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      If P_User_No<>1 Then
        Select Allow_Enter_Zero_Cost InTo V_Allow_Enter_Zero_Cost From Privilege_Fixed Where U_Id=P_User_No And RowNum<=1;
      End If;          
  Exception WHen Others Then
      RollBack;
      Raise_Application_Error(-20002,'Error When Select From Privilege_Fixed In Post_Transfer_In , '||Chr(13)||SqlErrm);
  End; 
--##------------------------------------------------------------------------------------##--  
    Insert Into Ias_Whtrns_Mst_Br_Tmp (Tr_No,Tr_Ser) Select Tr_No,Tr_Ser 
                                                       From Ias_Whtrns_Mst_Br 
                                                      Where Tr_InOut_Type=2 
                                                        And Tr_Ser=Nvl(P_Doc_Ser,Tr_Ser) 
                                                        And Nvl(Hung,0)=0 
                                                        And Nvl(Tr_Post,0) = 0
                                                        And Exists ( Select 1 From Ias_Whtrns_Mst
                                                                      Where Tr_Inout_Type = 1 
                                                                        And Tr_Ser = Ias_Whtrns_Mst_Br.F_Tr_Ser
                                                                        And RowNum   <= 1 )
                                                        And Exists(Select 1 From Ias_Whtrns_Dtl_Br Where Tr_Ser=Ias_Whtrns_Mst_Br.Tr_Ser And Rownum<=1)
                                                        And Not Exists(Select 1 From Ias_Whtrns_Mst Where Tr_Ser=Ias_Whtrns_Mst_Br.Tr_Ser And Rownum<=1);
--##------------------------------------------------------------------------------------##--    
    Declare
     Cursor C_Tr_Mst Is Select Tr_Inout_Type, Tr_Type, Tr_No, 
                               Tr_Ser, Tr_Date, Ref_No, 
                               W_Code, T_W_Code, F_W_Code, 
                               Cc_Code,pj_no,actv_no, Tr_Desc, Stk_Rate, 
                               0 Tr_Post, Tr_Amt, Tr_Res, 
                               Load_No, Pr_Rep, Processed, 
                               Exp_Amt,  
                               Audit_Ref, Audit_Ref_Desc, Audit_Ref_U_Id, 
                               Audit_Ref_Date, External_Post, F_Tr_No, 
                               F_Tr_Ser, Boe_No, Ad_U_Id, 
                               Ad_Date, Up_U_Id, Up_Date, 
                               Post_U_Id, Post_Date, 
                               Unpost_U_Id, Unpost_Date, Brn_No, 
                               Brn_Year, Cmp_No,  
                               Brn_Usr, Stk_Processed, Tr_Cost_Type, 
                               Diff_A_Code, Diff_A_Cy, Diff_Amt, 
                               Rtn_Tr, Tr_A_Code,C_Code,
                               Doc_Brn_No,Driver_No
                        From  Ias_Whtrns_Mst_Br
                         Where Tr_InOut_Type  = 2                           
                         And Exists (Select 1 From Ias_Whtrns_Mst_Br_Tmp Where Tr_Ser = Ias_Whtrns_Mst_Br.Tr_Ser  And RowNum <=1  )              
                         Order By Ad_Date ; 
      Begin  
----------------------------------------------------------------##--    
      For J In C_Tr_Mst Loop    
--##-----------------------------------------------------------------------------------##--    
              --## Check Duplicate Transfer In Number 
              Check_Duplicate_Tr ( J.Tr_Inout_Type ,
                                   J.Tr_No         ,
                                   J.Tr_Type       ,
                                   J.Tr_Ser        ,
                                   J.W_Code        );
--##-----------------------------------------------------------------------------------##--
                            
              Begin    
                   Insert Into Ias_Whtrns_Mst(  Tr_Inout_Type, Tr_Type, Tr_No, 
                                                Tr_Ser, Tr_Date, Ref_No, 
                                                W_Code, T_W_Code, F_W_Code, 
                                                Cc_Code,pj_no,actv_no, Tr_Desc, Stk_Rate, 
                                                Tr_Post, Tr_Amt, Tr_Res, 
                                                Load_No, Pr_Rep, Processed, 
                                                Exp_Amt,  
                                                Audit_Ref, Audit_Ref_Desc, Audit_Ref_U_Id, 
                                                Audit_Ref_Date, External_Post, F_Tr_No, 
                                                F_Tr_Ser, Boe_No, Ad_U_Id, 
                                                Ad_Date, Up_U_Id, Up_Date, 
                                                Post_U_Id, Post_Date, 
                                                Unpost_U_Id, Unpost_Date, Brn_No, 
                                                Brn_Year, Cmp_No,  
                                                Brn_Usr, Stk_Processed, Tr_Cost_Type, 
                                                Diff_A_Code, Diff_A_Cy, Diff_Amt, 
                                                Rtn_Tr, Tr_A_Code,C_Code,Doc_Brn_No,Driver_No)
                    Values(J.Tr_Inout_Type, J.Tr_Type, J.Tr_No, 
                           J.Tr_Ser, J.Tr_Date, J.Ref_No, 
                           J.W_Code, J.T_W_Code, J.F_W_Code, 
                           J.Cc_Code,J.pj_no,J.Actv_no, J.Tr_Desc, J.Stk_Rate, 
                           0, J.Tr_Amt, J.Tr_Res, 
                           J.Load_No, J.Pr_Rep, 0 , 
                           J.Exp_Amt,  
                           J.Audit_Ref, J.Audit_Ref_Desc, J.Audit_Ref_U_Id, 
                           J.Audit_Ref_Date, J.External_Post , J.F_Tr_No, 
                           J.F_Tr_Ser, J.Boe_No, J.Ad_U_Id, 
                           J.Ad_Date, J.Up_U_Id, J.Up_Date, 
                          J.Post_U_Id, J.Post_Date, 
                           J.Unpost_U_Id, J.Unpost_Date, J.Brn_No, 
                           J.Brn_Year, J.Cmp_No, 
                           J.Brn_Usr, J.Stk_Processed, J.Tr_Cost_Type, 
                           J.Diff_A_Code, J.Diff_A_Cy, J.Diff_Amt, 
                           J.Rtn_Tr,J.Tr_A_Code,J.C_Code,J.Doc_Brn_No,J.Driver_No) ;
              Exception
               When Others Then
                 Raise_Application_Error(-20005,'Error When Insert Into Ias_Whtrns_Mst '||Chr(13)||SqlErrm);  
              End;        
--##-----------------------------------------------------------------------------------##--              
               Begin
                  Ias_Itm_Inv_Pkg.Insrt_Gr_Mst ( P_Doctype  => 8                           ,
                                                 P_Gr_No    => J.Tr_No                     ,
                                                 P_G_Ser    => J.Tr_Ser                    ,                                                                              
                                                 P_Doc_Ser  => J.Tr_Ser                    ,
                                                 P_Doc_Date => J.Tr_Date                   ,
                                                 P_A_Code   => Null                        ,
                                                 P_Acy      => Ias_Gen_Pkg.Get_Stk_Cur     ,
                                                 P_C_Code   => Null                        ,
                                                 P_AcRate   => J.Stk_Rate                  ,
                                                 P_StkRate  => J.Stk_Rate                  ,
                                                 P_GrAmt    => J.Tr_Amt                    ,
                                                 P_Pi_No    => J.Tr_No                     ,
                                                 P_Cc_Code  => J.Cc_Code                   ,
                                                 P_Pj_No    => J.Pj_No                     ,
                                                 P_Actv_No  => J.Actv_No                   ,
                                                 P_W_Code   => J.W_Code                    ,
                                                 P_RefNo    => J.Ref_No                    ,
                                                 P_Desc     => J.Tr_Desc                   ,
                                                 P_Cflag    => 1                           ,
                                                 P_Pur_Type => J.Tr_Cost_Type              ,
                                                 P_User_No  => J.Ad_U_Id                   ,
                                                 P_Brn_No     => J.Brn_No                  ,
                                                 P_Brn_Year => J.Brn_Year                  ,
                                                 P_Cmp_No     => J.Cmp_No                  ,
                                                 P_Brn_Usr  => J.Brn_Usr                   );
               Exception 
                   When Others Then
                   Raise_Application_Error(-20006,'Error When Insert Into Gr_Note  '||Chr(13)||SqlErrm);   
              End;                                                     
--##-----------------------------------------------------------------------------------##--    
          Declare
                Cursor C_Tr_Dtl Is Select   Tr_Inout_Type, Tr_Type, Tr_No, 
                                            Tr_Ser, I_Code, I_Qty, 
                                            Itm_Unt, P_Size, P_Qty, 
                                            W_Code, T_W_Code, F_W_Code, 
                                            Tr_Qty, Cc_Code,pj_no,actv_no, Stk_Cost, 
                                            Nvl(Expire_Date,'01/01/1900') Expire_Date ,
                                            Nvl(Batch_No,'0') Batch_No ,
                                            Use_Serialno, 
                                            Exp_Amt, Rcrd_No, 
                                            Doc_Sequence, Boe_No, F_Tr_No, 
                                            F_Tr_Ser, Use_Attch, Rec_Attch, 
                                            Brn_No, Brn_Year, Doc_Sequence_Tr, 
                                            Cmp_No,  Brn_Usr, 
                                            I_Price, Item_Desc, Doc_Type_Ref, 
                                            Doc_No_Ref, Doc_Ser_Ref, V_Code,
                                            External_Post,Barcode,Post_Code  
                              From Ias_Whtrns_Dtl_Br
                                Where Ias_Whtrns_Dtl_Br.Tr_Ser  = J.Tr_Ser
                                 And  Ias_Whtrns_Dtl_Br.Tr_Inout_Type  = 2;                
--##-----------------------------------------------------------------------------------##--                          
             Begin
                  For I In C_Tr_Dtl  Loop                      
                      Begin
                         Select Decode(V_Use_Price_Whtrns_Rec_Cost,1,Nvl(I.I_Price,0),Nvl(Stk_Cost,0))
                           Into V_Stkcost
                          From Ias_Whtrns_Dtl
                           Where Tr_Inout_Type  = 1
                            And  Tr_Ser         = I.F_Tr_Ser
                            And  I_Code         = I.I_Code 
                            And  Itm_Unt        = I.Itm_Unt 
                            And  T_W_Code       = I.W_Code
                            And  To_Date(Expire_Date,'DD/MM/YYYY') = To_Date(I.Expire_Date,'DD/MM/YYYY')
                            And  Batch_No       = I.Batch_No                            
                            And  RowNum<=1; 
                      Exception
                           When Others Then
                             Raise_Application_Error(-20006,'Error When Get Cost From Ias_Whtrns_Dtl Transfer '||Chr(13)
                                                         ||'F_Tr_Ser ='||I.F_Tr_Ser||Chr(13)
                                                         ||'I_Code ='  ||I.I_Code||Chr(13)||SqlErrm);
                      End ;    
                        
--##-----------------------------------------------------------------------------------##--                                        
                      Begin
                          Select Ias_Doc_Seq.NextVal Into V_Seq From Dual;                                          
                      Exception
                       When Others Then
                         Raise_Application_Error(-20007,'Error In Ias_Doc_Seq '||Chr(13)||SqlErrm );
                      End ;
--##-----------------------------------------------------------------------------------##--
                      Begin 
                            Insert Into Ias_Whtrns_Dtl( Tr_Inout_Type, Tr_Type, Tr_No, 
                                                        Tr_Ser, I_Code, I_Qty, 
                                                        Itm_Unt, P_Size, P_Qty, 
                                                        W_Code, T_W_Code, F_W_Code, 
                                                        Tr_Qty, Cc_Code,pj_no,actv_no, Stk_Cost, 
                                                        Expire_Date, Batch_No, Use_Serialno, 
                                                        Exp_Amt, Rcrd_No,
                                                        Doc_Sequence, Boe_No, F_Tr_No, 
                                                        F_Tr_Ser, Use_Attch, Rec_Attch, 
                                                        Brn_No, Brn_Year, Doc_Sequence_Tr, 
                                                        Cmp_No,  Brn_Usr, 
                                                        I_Price, Item_Desc, Doc_Type_Ref, 
                                                        Doc_No_Ref, Doc_Ser_Ref, V_Code,
                                                      External_Post,Barcode,Post_Code)
                             Values(I.Tr_Inout_Type, 
                                    I.Tr_Type, 
                                    I.Tr_No, 
                                    I.Tr_Ser, 
                                    I.I_Code, 
                                    I.I_Qty, 
                                    I.Itm_Unt, 
                                    I.P_Size, 
                                    I.P_Qty, 
                                    I.W_Code, 
                                    I.T_W_Code, 
                                    I.F_W_Code, 
                                    I.Tr_Qty, 
                                    I.Cc_Code, 
                                    I.Pj_No,
                                    I.Actv_No,
                                    Nvl(V_StkCost,0), 
                                    To_Date(Nvl(I.Expire_Date,'01/01/1900'),'DD/MM/YYYY'), 
                                    Nvl(I.Batch_No,'0'), 
                                    I.Use_Serialno, 
                                    I.Exp_Amt, I.Rcrd_No, 
                                    V_Seq, I.Boe_No, I.F_Tr_No, 
                                    I.F_Tr_Ser, I.Use_Attch, I.Rec_Attch, 
                                    I.Brn_No, I.Brn_Year, V_Seq , 
                                    I.Cmp_No, I.Brn_Usr, 
                                    I.I_Price, I.Item_Desc, I.Doc_Type_Ref, 
                                    I.Doc_No_Ref, I.Doc_Ser_Ref, I.V_Code,
                                    J.External_Post,
                                    I.Barcode,
                                    I.Post_Code);
                      Exception
                        When Others Then
                        RollBack;
                        Raise_Application_Error(-20008,'Error When Insert Into Ias_Whtrns_Dtl '||Chr(13)||SqlErrm);      
                        
                      End; 
--##-----------------------------------------------------------------------------------##--
                      --## Calc_WatAvg                 
                      Begin    
                        V_Wt_After := Calc_Wtavg_Cost(P_Cost_Type  => V_Costing_Type          ,
                                                      P_Wtavg_Type => V_Wtavg_Type            ,
                                                      P_Icode      => I.I_Code                ,
                                                      P_Iqty       => I.I_Qty                 ,
                                                      P_Icost      => Nvl(V_Stkcost,0)        ,
                                                      P_Psize      => I.P_Size                ,
                                                      P_Wcode      => I.W_Code                ,
                                                      P_Frc_No     => V_Stk_Cst_Frc           ,
                                                      P_Brn_No     => I.Brn_No                ,
                                                      P_Brn_Year   => I.Brn_Year              ,
                                                      P_Cmp_No     => I.Cmp_No                ,
                                                      P_Brn_Usr    => I.Brn_Usr               );
                      Exception 
                       When Others Then
                         RollBack;
                         Raise_Application_Error(-20009,' Calc WtAvg Error = '||SqlErrm);
                      End;
--##-----------------------------------------------------------------------------------##--                                        
                      If Nvl(V_Use_Itm_Attach,0) = 1 And Nvl(I.Use_Attch,0)=1 Then
                         Declare
                            V_Cnt Number;
                          Begin
                              Select 1 InTo V_Cnt
                               From Ias_Itm_Attach_Movement_Br
                               Where Doc_Ser   = J.Tr_Ser
                                 And Rec_Attch = I.Rec_Attch 
                                 And Doc_Type  = 8
                                 And RowNum<=1;
                          Exception When Others Then                                                                          
                             RollBack;
                             Raise_Application_Error(-20010,'Error In  Ias_Itm_Attach_Movement_Br');                                               
                          End;               
                          Begin
                              Insert InTo Ias_Itm_Attach_Movement(  I_Code, Itm_Unt, P_Size, 
                                                                    Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                                    Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                                    Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                                    Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                                    W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                                    R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                                    Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Type_Ref, 
                                                                    Doc_No_Ref, Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                                    Ac_Rate, Stk_Rate, I_Price, Dis_Amt, I_Cost, Stk_Cost, Vat_Amt, 
                                                                    V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                                    Cmp_No, Brn_No, Brn_Year,  Brn_Usr, Othr_Amt)
                               Select   I_Code, Itm_Unt, P_Size, 
                                        Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                        Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                        Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                        Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                        W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                        R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                        Free_Qty, Pf_Qty, Rcrd_No, J.External_Post, Doc_Type_Ref, Doc_No_Ref, 
                                        Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                        Ac_Rate, J.Stk_Rate, I.I_Price, Dis_Amt, Nvl(V_Stkcost,0), Nvl(V_Stkcost,0), Vat_Amt, 
                                        V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                        Cmp_No, Brn_No, Brn_Year,  Brn_Usr, Othr_Amt
                                   From Ias_Itm_Attach_Movement_Br
                                   Where Doc_Ser   = J.Tr_Ser
                                     And Rec_Attch = I.Rec_Attch 
                                     And Doc_Type  = 8;
                          Exception When Others Then                                                    
                            RollBack;
                            Raise_Application_Error(-20010,'Error In Ias_Itm_Attach_Movement');                                                     
                          End;       
                      End If;                     
--##-----------------------------------------------------------------------------------##--                                
                        --## Get WatAvg Before                 
                      If  V_Costing_Type  = 2 Then  -- Wtavg
                           Begin
                               V_Wt_Before:= Nvl(Ias_Itm_Pkg.Get_Grand_WtAvg(V_Wtavg_Type  ,
                                                              I.I_Code               ,
                                                              I.W_Code ),0           ) ;                                              
                           Exception
                             When Others Then
                              RollBack;
                              Raise_Application_Error(-20011,'Error When Get WatAvg Before Cost '||Chr(13)||SqlErrm);
                           End ;
                      Else -- fifo
                           V_Wt_Before:= 0 ;
                      End If; 
--##-----------------------------------------------------------------------------------##--                
                      --## Insrt_Ias_Itm_Wcode        
                      Begin             
                          Ias_Itm_Inv_Pkg.Insrt_Ias_Itm_Wcode ( p_icode    => I.I_Code,
                                                                p_Itm_Unt  => IAS_Itm_Pkg.Get_Icode_Min_Unit (P_I_Code => I.i_code),
                                                                p_Psize    => 1,
                                                                p_w_code   => I.w_code,
                                                                p_doc_date => J.Tr_Date);  
                      Exception 
                        When Others Then
                          RollBack;
                          Raise_Application_Error(-20012,'Error When Insrt_Ias_Itm_Wcode = '||Chr(13)||SqlErrm);
                      End;
--##-----------------------------------------------------------------------------------##--    
                      --## Insert Into Gr_Detail 
                      Begin
                        Ias_Itm_Inv_Pkg.Insrt_Gr_Dtl (  P_DocType       => 8                                  ,
                                                        P_Gr_No         => J.Tr_No                            ,
                                                        P_G_Ser         => J.Tr_Ser                           ,
                                                        P_Doc_Ser       => J.Tr_Ser                           ,
                                                        P_DocSeq        => V_Seq                              ,
                                                        P_Doc_Date      => J.Tr_Date                          ,
                                                        P_Acy           => Ias_Gen_Pkg.Get_Stk_Cur            ,
                                                        P_Acrate        => J.Stk_Rate                         ,
                                                        P_Stkrate       => J.Stk_Rate                         ,
                                                        P_Pi_No         => Null                               ,                                                                    
                                                        P_Pur_Type      => J.Tr_Cost_type                     ,
                                                        P_W_Code        => Nvl(J.W_Code,I.W_Code)             ,
                                                        P_Cc_Code       => J.Cc_Code                          ,
                                                        P_Pj_No         => J.Pj_No                            ,
                                                        P_Actv_No       => J.Actv_No                          ,
                                                        P_Icode         => I.I_Code                           ,
                                                        P_Iqty          => I.I_Qty                            ,
                                                        P_Freeqty       => 0                                  ,
                                                        P_Itm_Unt       => I.Itm_Unt                          ,
                                                        P_Psize         => I.P_Size                           ,
                                                        P_Iprice        => I.I_Price                          ,
                                                        P_Cprice        => Nvl(V_Stkcost,0)                   ,
                                                        P_Stkcost       => Nvl(V_Stkcost,0)                   ,
                                                        P_Wtavg_Before  => Nvl(V_Wt_Before,0)                 ,
                                                        P_Wtavg_After   => Nvl(V_Wt_After,0)                  ,
                                                        P_Vatper        => Null                               ,
                                                        P_Vatamt        => Null                               ,
                                                        P_expdate       => To_Date(Nvl(I.Expire_Date,'01/01/1900'),'DD/MM/YYYY') , 
                                                        P_Batchno       => Nvl(I.Batch_No,'0')                ,
                                                        P_Rcrdno        => I.Rcrd_no                          ,
                                                        P_Use_Serial    => 0                                  ,
                                                        P_Brn_No        => I.Brn_No                           ,
                                                        P_Brn_Year      => I.Brn_Year                         ,
                                                        p_Cmp_No        => I.Cmp_No                           ,
                                                        p_Brn_Usr       => I.Brn_Usr                          );
                      Exception 
                        When Others Then
                         RollBack;
                         Raise_Application_Error(-20013,'Error In Gr_Detail = '||Chr(13)||SqlErrm);
                      End;
--##-----------------------------------------------------------------------------------##--        
              --## Insert Into Item_movement
                  Begin
                   Ias_Itm_Inv_Pkg.Insrt_Item_Move( P_DocType     => 8                              ,
                                                    P_BillDocType => J.Tr_Type                      ,
                                                    P_DocNo       => J.Tr_No                        ,
                                                    P_Icode       => I.I_Code                       ,
                                                    P_Iqty        => I.I_Qty                        ,
                                                    P_Freeqty     => 0                              ,
                                                    P_Itm_Unt     => I.Itm_Unt                      ,
                                                    P_Psize       => I.P_Size                       ,
                                                    P_Idate       => J.Tr_Date                      ,
                                                    P_Iprice      => I.I_Price                      ,
                                                    P_Wcode       => I.W_Code                       ,
                                                    P_Stkcost     => Nvl(V_Stkcost,0)               ,
                                                    P_Vatamt      => Null                           ,
                                                    P_Acy         => Ias_Gen_Pkg.Get_Stk_Cur        ,
                                                    P_Ac_Rate     => J.Stk_Rate                     ,
                                                    P_Stk_Rate    => J.Stk_Rate                     ,
                                                    P_Cc_Code     => J.Cc_Code                      ,
                                                    P_Pj_No       => J.Pj_No                        ,
                                                    P_Actv_No     => J.Actv_No                      ,
                                                    P_C_Code      => Null                           ,
                                                    P_Adesc       => J.Tr_Desc                      ,                  
                                                    P_Expdate     => To_Date(Nvl(I.Expire_Date,'01/01/1900'),'DD/MM/YYYY'),
                                                    P_Batchno     => Nvl(I.Batch_No,'0')            ,
                                                    P_Rcrdno      => I.Rcrd_No                      ,
                                                    P_Refno       => J.Ref_No                       ,
                                                    P_Docser      => J.Tr_Ser                       ,
                                                    P_Docseq      => V_Seq                          ,
                                                    P_Rt_Type     => J.Tr_Cost_Type                 , 
                                                    P_Inout       => 1                              ,
                                                    p_Extrnl_pst  => J.External_Post                ,
                                                    P_Ad_Date     => J.Ad_Date                      ,
                                                    P_Up_Date     => Null                           , 
                                                    P_Brn_No      => I.Brn_No                       ,
                                                    P_Brn_Year    => I.Brn_Year                     ,
                                                    P_Cmp_No      => I.Cmp_No                       ,
                                                    P_Brn_Usr     => I.Brn_Usr                      );
                  Exception 
                       When Others Then
                         RollBack;
                         Raise_Application_Error(-20014,'Error When Inserting Itm_Movement = '||Chr(13)||SqlErrm);
                  End; 
--##------------------------------------------------------------------------------------##--
                
--##------------------------------------------------------------------------------------##--
                End Loop ;
             End ;
--##------------------------------------------------------------------------------------##--    
             --## Update Warehouse Transfer Process = 1 
             Begin
                 Update  Ias_Whtrns_Mst
                  Set    Processed =  1  
                   Where Tr_Inout_Type  = 1
                    And  Tr_Ser         = J.F_Tr_Ser ;
             Exception
               When Others Then
                 RollBack;
                 Raise_Application_Error(-20015,'Error When Updating Warehouse_Transfer  = '||Chr(13)||'F_Tr_Ser ='||J.F_Tr_Ser ||Chr(13)||SqlErrm);                
             End ;
             
                 Begin
                       Insert Into Inv_Wrhs_Trnsfr_Expns ( Doc_No, Doc_Ser, Tr_Inout_Type, Doc_Desc, Ref_No, A_Code,
                                                                              Ac_Code_Dtl, Ac_Dtl_Typ, A_Cy, Ac_Rate, Cc_Code, Pj_No, Actv_No,
                                                                              Amt, Inv_Amt, Rcrd_No, Brn_No, Brn_Year, Brn_Usr, Cmp_No,Doc_Brn_No)
                                                                       Select Doc_No, Doc_Ser, Tr_Inout_Type, Doc_Desc, Ref_No, A_Code,
                                                                                Ac_Code_Dtl, Ac_Dtl_Typ, A_Cy, Ac_Rate, Cc_Code, Pj_No, Actv_No,
                                                                                Amt, Inv_Amt, Rcrd_No, Brn_No, Brn_Year, Brn_Usr, Cmp_No,Doc_Brn_No
                                                                           From Inv_Wrhs_Trnsfr_Expns_Br
                                                                          Where Doc_Ser = J.Tr_Ser;
                Exception When No_Data_found Then Null;
                          When Others Then                                                    
                   Raise_Application_Error(-20016,'Error When Insert Inv_Wrhs_Trnsfr_Expns  = '||Chr(13)||'Tr_Ser ='||J.Tr_Ser||Chr(13)||SqlErrm);                                                  
                End;
                              
--##-------------------------------------------------------------------------------------##--      
             Begin
                IAS_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 12           ,
                                                      G_Doc_Ser     => J.Tr_Ser     ,
                                                      P_jv_type     => J.Tr_Type    ,
                                                      P_doc_no      => J.Tr_No      ,
                                                      P_Lang_no     => 1            ,
                                                      P_User_No     => J.Ad_U_Id    ,
                                                      G_Post_Type   => 0            );
             Exception 
               When No_Data_Found Then 
                 Null;
               When Others Then
                 RollBack;
                 Raise_Application_Error(-20016,'Error When Updating Post In Warehouse_Transfer  = '||Chr(13)||'Tr_Ser ='||J.Tr_Ser ||Chr(13)||SqlErrm);                                                    
             End;  
             
             --Post_Transfer_Out ( P_Doc_Ser => I.Doc_Ser ,P_Use_Adjstmnt => 0 );                                
--##-------------------------------------------------------------------------------------##--
      End Loop; --(1)
--##------------------------------------------------------------------------------------##--
      --## Update Ias_Bill_Mst_Br        
      Begin     
          Update Ias_Whtrns_Mst_Br 
            Set  Tr_Post        = 1
           Where Tr_InOut_Type  = 2
             And Exists (Select 1 From Ias_Whtrns_Mst_Br_Tmp Where Tr_Ser = Ias_Whtrns_Mst_Br.Tr_Ser  And RowNum <=1  ) 
             And Exists (Select 1 From Ias_Whtrns_Mst Where Tr_Ser = Ias_Whtrns_Mst_Br.Tr_Ser  And RowNum <=1  ) ;
       Commit ; 
      Exception
      When Others Then
        RollBack;
        Raise_Application_Error(-20016,'Error When Update Tr_Post In  Update Ias_Whtrns_Mst_Br ');
      End ;            

--##------------------------------------------------------------------------------------##--          
    End;
--##------------------------------------------------------------------------------------##--        
End Post_Transfer_In  ;

Procedure Post_Transfer_Out_In ( P_Doc_Ser  In Ias_Whtrns_Mst.Tr_Ser%Type   Default Null , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  IS
  Cursor Wt_M Is Select M.Tr_Ser
                   From Ias_Whtrns_Mst_Br M
                  Where M.Tr_InOut_Type  = 2
                    And M.F_Tr_Ser = P_Doc_Ser
                    And Nvl(M.Hung,0)=0 
                    And Nvl(M.Tr_Post,0)=0
                    And Exists(Select 1 From Ias_Whtrns_Dtl_Br Where Tr_Ser=M.Tr_Ser And Rownum<=1)
                    And Not Exists(Select 1 From Ias_Whtrns_Mst Where Tr_Ser=M.Tr_Ser And Rownum<=1)
                  Order By  M.Ad_Date;
Begin
    For I In Wt_M Loop
      Post_Transfer_In ( P_Doc_Ser => I.Tr_Ser );
    End Loop;
      
End Post_Transfer_Out_In  ;

--##------------------------------------------------------------------------------------##--
Procedure Post_OutGoing ( P_Doc_Ser  In Ias_Outgoing_Mst.Out_Ser%Type   Default Null , P_Use_Adjstmnt In Number Default 0 ,P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null) Is     
     V_Cnt              Number;
     V_Sqlstr           Varchar2(3000);
     V_sqlstr2          Varchar2(3000);
     V_Out_no           Number;      
     V_Out_ser          Number;                 
     V_StkCost          Number;
     V_Seq              Number;
     V_StkRate          Number;
     V_Cst              Number;
     V_price            Number;
     V_Use_Itm_Attach   Ias_Para_Inv.Use_Itm_Attach%Type ;
     V_Costing_Type     Ias_Para_Inv.Costing_Type%Type   ;
     V_Wtavg_Type       Ias_Para_Inv.Wtavg_Type%Type     ;  
     V_Stk_Cst_Frc      Number ;   
     V_Lang_No          Number:=P_Lang_No;
     V_Allow_Enter_Zero_Cost Number ;
Begin
--##-------------------------------------------------------------------------------------##--
  If P_Lang_No Is Null Then    
    Begin
      Select Lang_No InTo V_Lang_No From Ias_Sys.Lang_Def Where Nvl(Flg_St,1)= 1 And Lang_Dflt=1 And Rownum<=1;
    Exception WHen Others Then
        V_Lang_No := 1;
    End;  
  ENd If;  
  --##-------------------------------------------------------------------------------------##--
   --# To Insert Into  Ias_pos_minus_qty Temporary Table 
   --------------------------------------------------------------##--
  Begin
      Select Nvl(Costing_Type,0)              ,
                  Nvl(Wtavg_Type,0)                ,
                  Nvl(Stkcost_Fraction,6)          ,
                  Nvl(V_Use_Itm_Attach ,0)
            Into  V_Costing_Type              ,
                  V_Wtavg_Type                ,
                  V_Stk_Cst_Frc               ,
                  V_Use_Itm_Attach    
           From Ias_Para_Inv ;
  Exception WHen Others Then
    RollBack;
    Raise_Application_Error(-20001,'Error When Select From Para In Post_OutGoing '||Chr(13)||SqlErrm);
  End;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      If P_User_No<>1 Then
        Select Allow_Enter_Zero_Cost InTo V_Allow_Enter_Zero_Cost From Privilege_Fixed Where U_Id=P_User_No And RowNum<=1;
      End If;          
  Exception WHen Others Then
      RollBack;
      Raise_Application_Error(-20002,'Error When Select From Privilege_Fixed In Post_OutGoing'||Chr(13)||SqlErrm);
  End;
--##------------------------------------------------------------------------------------##--
  Insert Into Ias_Outgoing_Mst_Br_Tmp (Out_No,Out_Ser) Select Out_No , Out_Ser 
                                                       From Ias_Outgoing_Mst_Br 
                                                      Where Out_Ser=Nvl(P_Doc_Ser,Out_Ser) 
                                                        And Nvl(Hung,0)=0 
                                                        And Nvl(Out_Post,0)=0
                                                        And Exists(Select 1 From Ias_Outgoing_Dtl_Br Where Out_Ser=Ias_Outgoing_Mst_Br.Out_Ser And Rownum<=1)
                                                        And Not Exists(Select 1 From Ias_Outgoing_Mst Where Out_Ser=Ias_Outgoing_Mst_Br.Out_Ser And Rownum<=1);
  --##-------------------------------------------------------------------------------------##--
  Check_Avl_Qty ( P_Doc_Type => 6);
  --##-------------------------------------------------------------------------------------##--
  Begin
      Select 1 Into V_Cnt From Ias_pos_minus_qty_Tmp Where RowNum <=1 ;
   Exception
       When Others Then
         V_cnt := 0 ;
     End ; 
   If Nvl(V_Cnt,0)>0 Then ---(2)
      If Nvl(P_Use_Adjstmnt,0)=1 Then
        Post_Stk_Adjstmnt ;
      Else
        Begin
            Delete Ias_Outgoing_Mst_Br_Tmp M Where Exists ( Select 1 From Ias_Outgoing_Dtl_Br A,Ias_Pos_Minus_Qty_Tmp B
                                                             Where A.Out_Ser    = M.Out_Ser 
                                                               And A.I_Code      = B.I_Code
                                                               And A.W_Code      = B.W_Code
                                                               And To_Date(A.Expire_Date,'DD/MM/YYYY') = To_Date(B.Expire_Date,'DD/MM/YYYY')
                                                               And A.Batch_No    = B.Batch_No                           
                                                               And Rownum<=1);   
       Exception When Others Then Null;
       End;                                                    
      End If;                
   End If; ---(2) 
--##-------------------------------------------------------------------------------------##-- 
    Declare
     Cursor Sm Is Select    Out_No, 
                            Out_Ser, 
                            Out_Type, 
                            Out_Date, 
                            A_Cy, 
                            Ac_Rate, 
                            Stock_Rate, 
                            A_Code, 
                            C_Code, 
                            V_Code, 
                            Out_Due_Date,
                            Out_Post,
                            Out_Amt,
                            W_Code,
                            Ref_No,
                            Cc_Code,
                            Pj_No,
                            Actv_No,
                            Csh_Bnk_No,
                            A_Desc,
                            Attach_Cnt,
                            Pr_Rep,
                            Ben_Name,
                            Exp_A_Code,
                            Exp_A_Cy,
                            Exp_Amt,
                            Exp_Rate,
                            Nvl(Pur_Type,1) Pur_Type,
                            Ord_Hotel_No,
                            External_Post,
                            Hung,
                            Audit_Ref,
                            Audit_Ref_Desc,
                            Audit_Ref_U_Id,
                            Audit_Ref_Date,
                            Ad_U_Id, 
                            Ad_Date,
                            Up_U_Id,
                            Up_Date,
                            Up_Cnt,
                            Post_U_Id,
                            Post_Date,
                            Unpost_U_Id,
                            Unpost_Date,
                            Mrp_Mr_Order,
                            Mrp_Mr_Sq,
                            Mrp_St,
                                                        Ac_Dtl_Typ     ,
                                                        Ac_Code_Dtl     ,
                                                        Conn_With_Si ,                            
                            Doc_Brn_No,
                            Cmp_No,
                            Brn_No,
                            Brn_Year,
                            Brn_Usr                             
     From Ias_Outgoing_Mst_Br
       Where Exists (Select 1 From Ias_Outgoing_Mst_Br_Tmp Where Out_Ser = Ias_Outgoing_Mst_Br.Out_Ser  And RowNum <=1  )
         Order By  Ad_Date;
    Begin ---(11)
--##-------------------------------------------------------------------------------------##--
    --## To Get Stock Rate           
    V_StkRate := Ias_Gen_Pkg.Get_Cur_rate(p_acy=> Ias_Gen_pkg.Get_Stk_Cur);      
--##-------------------------------------------------------------------------------------##--
    For j in SM Loop     -->> (1)   
              
        Begin
             Insert Into Ias_Outgoing_Mst ( Out_No, 
                                            Out_Ser, 
                                            Out_Type, 
                                            Out_Date, 
                                            A_Cy, 
                                            Ac_Rate, 
                                            Stock_Rate, 
                                            A_Code, 
                                            C_Code, 
                                            V_Code, 
                                            Out_Due_Date,
                                            Out_Post,
                                            Out_Amt,
                                            W_Code,
                                            Ref_No,
                                            Cc_Code,
                                            Pj_No,
                                            Actv_No,
                                            Csh_Bnk_No,
                                            A_Desc,
                                            Attach_Cnt,
                                            Pr_Rep,
                                            Ben_Name,
                                            Exp_A_Code,
                                            Exp_A_Cy,
                                            Exp_Amt,
                                            Exp_Rate,
                                            Pur_Type,
                                            Ord_Hotel_No,
                                            External_Post,
                                            Hung,
                                            Audit_Ref,
                                            Audit_Ref_Desc,
                                            Audit_Ref_U_Id,
                                            Audit_Ref_Date,
                                            Ad_U_Id, 
                                            Ad_Date,
                                            Up_U_Id,
                                            Up_Date,
                                            Up_Cnt,
                                            Post_U_Id,
                                            Post_Date,
                                            Unpost_U_Id,
                                            Unpost_Date,
                                            Mrp_Mr_Order,
                                            Mrp_Mr_Sq,
                                            Mrp_St,
                                                                                        Ac_Dtl_Typ     ,
                                                                                        Ac_Code_Dtl     ,
                                                                                        Conn_With_Si ,                                            
                                            Doc_Brn_No,
                                            Cmp_No,
                                            Brn_No,
                                            Brn_Year,
                                            Brn_Usr,
                                            DOC_PST_SQ)
                                    Values( J.Out_No, 
                                            J.Out_Ser, 
                                            J.Out_Type, 
                                            J.Out_Date, 
                                            J.A_Cy, 
                                            J.Ac_Rate, 
                                            J.Stock_Rate, 
                                            J.A_Code, 
                                            J.C_Code, 
                                            J.V_Code, 
                                            J.Out_Due_Date,
                                            J.Out_Post,
                                            J.Out_Amt,
                                            J.W_Code,
                                            J.Ref_No,
                                            J.Cc_Code,
                                            J.Pj_No,
                                            J.Actv_No,
                                            J.Csh_Bnk_No,
                                            J.A_Desc,
                                            J.Attach_Cnt,
                                            J.Pr_Rep,
                                            J.Ben_Name,
                                            J.Exp_A_Code,
                                            J.Exp_A_Cy,
                                            J.Exp_Amt,
                                            J.Exp_Rate,
                                            J.Pur_Type,
                                            J.Ord_Hotel_No,
                                            J.External_Post,
                                            J.Hung,
                                            J.Audit_Ref,
                                            J.Audit_Ref_Desc,
                                            J.Audit_Ref_U_Id,
                                            J.Audit_Ref_Date,
                                            J.Ad_U_Id, 
                                            J.Ad_Date,
                                            J.Up_U_Id,
                                            J.Up_Date,
                                            J.Up_Cnt,
                                            J.Post_U_Id,
                                            J.Post_Date,
                                            J.Unpost_U_Id,
                                            J.Unpost_Date,
                                            J.Mrp_Mr_Order,
                                            J.Mrp_Mr_Sq,
                                            J.Mrp_St,
                                                                      J.Ac_Dtl_Typ     ,
                                                                      J.Ac_Code_Dtl     ,
                                                                      J.Conn_With_Si ,                                            
                                            J.Doc_Brn_No,
                                            J.Cmp_No,
                                            J.Brn_No,
                                            J.Brn_Year,
                                            J.Brn_Usr,
                                            IAS_POSTING_PKG.GET_DOC_PST_SQ);
        Exception
         When Others Then         
            Raise_Application_Error(-20003,'Error When Insert Into Ias_Outgoing_Mst '||Chr(13)||SqlErrm);  
            RollBack;   
        End;        
--##-------------------------------------------------------------------------------------##--      
        If J.C_Code Is Not Null Then             
           Begin
               Insert_Installemnt  (  9,
                                      J.Out_No,
                                      j.Out_type,
                                      J.Out_ser,
                                      j.Out_Date,
                                      j.Ad_U_id,
                                      j.A_Cy,
                                      j.Csh_Bnk_No,
                                      j.C_Code,
                                      'D');                        
           Exception
             When Others Then         
               Raise_Application_Error(-20004,'Error When Insert Into Installment '||Chr(13)||SqlErrm);  
               RollBack;   
           End;          
      End If;                  
--##-------------------------------------------------------------------------------------##--
      Declare
         Cursor BD Is Select    Out_No,
                                Out_Ser,
                                Out_Type,
                                I_Code,
                                I_Qty,
                                Itm_Unt,
                                P_Size,
                                P_Qty,
                                I_Price,
                                Stk_Cost,
                                W_Code,
                                Cc_Code,
                                Pj_No,
                                Actv_No,
                                Expire_Date,
                                Batch_No,
                                Exp_Amt,
                                Use_Serialno,
                                Rcrd_No,
                                Doc_Sequence,
                                Doc_Type_Ref,
                                Doc_Jv_Type_Ref,
                                Doc_No_Ref,
                                Doc_Ser_Ref,
                                Doc_Sequence_Ref,
                                Gr_No,
                                G_Ser,
                                Use_Attch,
                                Rec_Attch,
                                Item_Desc,
                                Barcode,
                                I_Length,
                                I_Width,
                                I_Height,
                                I_Number,
                                Post_Code,
                                Cmp_No,
                                Brn_No,
                                Brn_Year,
                                Brn_Usr
                From Ias_Outgoing_Dtl_Br
                Where Out_ser=J.Out_ser
                 And Exists (Select 1 From Ias_Outgoing_Mst_Br_Tmp Where Ias_Outgoing_Mst_Br_Tmp.Out_Ser = Ias_Outgoing_Dtl_Br.Out_Ser  And RowNum <=1  );                
--##-------------------------------------------------------------------------------------##--
    Begin --- (12)
         For i in BD  Loop        -->> (2)

--##-------------------------------------------------------------------------------------##--
            Begin
                V_StkCost := IAS_Itm_Inv_Pkg.Get_Itm_Cost(  P_costing_type => V_Costing_Type                  ,
                                                            P_Wtavg_Type   => V_Wtavg_Type                    ,
                                                            P_icode        => i.i_code                           ,
                                                            P_wcode        => i.w_code                          ,
                                                            P_Psize        => Nvl(i.p_Size,1)                  ,
                                                            P_Iqty         => ( Nvl(i.i_qty,0)   ),
                                                            P_ExpDate      => To_Date(Nvl(i.Expire_Date,'01/01/1900'),'DD/MM/YYYY') ,
                                                            P_BatchNo      => Nvl(i.Batch_No,'0')              ,
                                                            P_brn_no       => J.brn_no                          ,
                                                            P_brn_year     => J.brn_year                      ,
                                                            P_Cmp_No       => J.Cmp_No                          ,
                                                            P_Brn_Usr      => J.Brn_Usr                          );
            Exception 
              When Others Then
                Raise_Application_Error(-20005,'Error When In Get Item Cost '||Chr(13)||SqlErrm);                                                    
            End;                     
--##-------------------------------------------------------------------------------------##--       
            If  V_Costing_Type=1  Then  --fifo
                --If J.pur_type =1 Then
                  -- V_price := Round((Nvl(V_StkCost,0)*J.Stock_Rate) /J.Ac_Rate,V_Stk_Cst_Frc);
                If J.pur_type In (1,2) Then
                      V_price :=Round(((Nvl(last_incoming_price(V_Wtavg_Type    ,
                                                                I.I_Code ,
                                                                I.p_size ,
                                                                I.w_code ,
                                                                1),0))*J.Stock_Rate) /J.ac_rate,V_Stk_Cst_Frc);
                ElsIf J.pur_type =3 Then
                   V_Price := I.I_Price;
                End If;                       
--##----------------------------------------------------------------------------------##-- 
            Else
                If J.pur_type = 1 Then
                   V_price := Round((Nvl(V_StkCost,0)*J.Stock_Rate) /J.Ac_Rate,V_Stk_Cst_Frc);
                ElsIf J.pur_type = 2 Then
                   V_price :=Round(((Nvl(last_incoming_price(V_Wtavg_Type ,
                                                             I.I_Code     ,
                                                             I.p_size     ,
                                                             I.w_code     ,
                                                             1),0))*J.Stock_Rate) /J.ac_rate,V_Stk_Cst_Frc);
                ElsIf J.pur_type =3 Then
                   V_Price := I.I_Price;
                End If;
--##----------------------------------------------------------------------------------##--     
            End If;
--##----------------------------------------------------------------------------------##-- 
            Select Ias_Doc_Seq.NextVal InTo V_Seq From Dual;
--##----------------------------------------------------------------------------------##--  
            Begin
              Insert Into Ias_Outgoing_Dtl( Out_No,
                                            Out_Ser,
                                            Out_Type,
                                            I_Code,
                                            I_Qty,
                                            Itm_Unt,
                                            P_Size,
                                            P_Qty,
                                            I_Price,
                                            Stk_Cost,
                                            W_Code,
                                            Cc_Code,
                                            Pj_No,
                                            Actv_No,
                                            Expire_Date,
                                            Batch_No,
                                            Exp_Amt,
                                            Use_Serialno,
                                            Rcrd_No,
                                            Doc_Sequence,
                                            Doc_Type_Ref,
                                            Doc_Jv_Type_Ref,
                                            Doc_No_Ref,
                                            Doc_Ser_Ref,
                                            Doc_Sequence_Ref,
                                            External_Post,
                                            Gr_No,
                                            G_Ser,
                                            Use_Attch,
                                            Rec_Attch,
                                            Item_Desc,
                                            Barcode,
                                            I_Length,
                                            I_Width,
                                            I_Height,
                                            I_Number,
                                            Post_Code,
                                            Cmp_No,
                                            Brn_No,
                                            Brn_Year,
                                            Brn_Usr)
                                    Values( J.Out_No,
                                            J.Out_Ser,
                                            J.Out_Type,
                                            I.I_Code,
                                            I.I_Qty,
                                            I.Itm_Unt,
                                            I.P_Size,
                                            I.P_Qty,
                                            V_Price,
                                            V_StkCost,
                                            I.W_Code,
                                            I.Cc_Code,
                                            I.Pj_No,
                                            I.Actv_No,
                                            I.Expire_Date,
                                            I.Batch_No,
                                            I.Exp_Amt,
                                            I.Use_Serialno,
                                            I.Rcrd_No,
                                            V_Seq,
                                            I.Doc_Type_Ref,
                                            I.Doc_Jv_Type_Ref,
                                            I.Doc_No_Ref,
                                            I.Doc_Ser_Ref,
                                            I.Doc_Sequence_Ref,
                                            J.External_Post,
                                            I.Gr_No,
                                            I.G_Ser,
                                            I.Use_Attch,
                                            I.Rec_Attch,
                                            I.Item_Desc,
                                            I.Barcode,
                                            I.I_Length,
                                            I.I_Width,
                                            I.I_Height,
                                            I.I_Number,
                                            I.Post_Code,
                                            I.Cmp_No,
                                            I.Brn_No,
                                            I.Brn_Year,
                                            I.Brn_Usr);
            Exception
                When Others Then
                  Raise_Application_Error(-20006,'Error When Inserting Into Ias_Outgoing_Dtl '||Chr(13)||SqlErrm);                  
                  RollBack;
            End;
--##----------------------------------------------------------------------------------##--              
            If Nvl(V_Use_Itm_Attach,0)=1 And Nvl(I.Use_Attch,0)=1 Then                  
                  Declare
                      V_Cnt Number;
                Begin
                      Select 1 InTo V_Cnt
                               From Ias_Itm_Attach_Movement_Br
                               Where Doc_Ser   = I.Out_Ser
                                 And Rec_Attch = I.Rec_Attch 
                                 And Doc_Type  = 6
                                 And RowNum<=1;
                Exception 
                   When Others Then                                                                          
                     Raise_Application_Error(-20007,'Error When Select From Ias_Itm_Attach_Movement_Br '||Chr(13)||SqlErrm);                                              
                End;               
                  
                Begin
                     Insert InTo Ias_Itm_Attach_Movement( I_Code, Itm_Unt, P_Size, 
                                                           Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                           Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                           Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                           Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                           W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                           R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                           Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Type_Ref, 
                                                           Doc_No_Ref, Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                           Ac_Rate, Stk_Rate, I_Price, Dis_Amt, I_Cost, Stk_Cost, Vat_Amt, 
                                                           V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                           Cmp_No, Brn_No, Brn_Year, Brn_Usr, Othr_Amt)
                                                    Select I_Code, Itm_Unt, P_Size, 
                                                           Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                           Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                           Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                           Attch_Note, Doc_Type, I.Out_Type, Doc_No, Doc_Ser, 
                                                           W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no,Rep_Code, 
                                                           R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                           Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Type_Ref, Doc_No_Ref, 
                                                           Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                           Ac_Rate, J.Stock_Rate, I.I_Price, Dis_Amt, I_Price, V_StkCost, Vat_Amt, 
                                                           V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                           Cmp_No, Brn_No, Brn_Year, Brn_Usr, Othr_Amt
                                                      From Ias_Itm_Attach_Movement_Br
                                                     Where Doc_Ser   = J.Out_Ser
                                                       And Rec_Attch = I.Rec_Attch 
                                                       And Doc_Type  = 6;
                Exception When Others Then                                                                          
                  Raise_Application_Error(-20008,'Error When Insert Into Ias_Itm_Attach_Movement '||Chr(13)||SqlErrm);                                          
                End;       
            End If;      
--##-------------------------------------------------------------------------------------##--
           If Nvl(i.i_qty,0)>0 Then
              Begin
                      V_Cst := 0;
                      Ias_Itm_Inv_Pkg.Insrt_Sale_Cost(  P_Cst          =>  V_Cst                          ,
                                                        P_Wtavg_Type   => V_Wtavg_Type                    ,
                                                        P_Icode        => I.I_Code                        ,
                                                        P_Iqty         => Nvl(I.I_Qty,0)                  ,
                                                        P_Freeqty      => 0                               ,
                                                        P_Itm_Unt      => I.Itm_Unt                       ,
                                                        P_Psize        => I.P_Size                        ,
                                                        P_Cost_Type    => V_Costing_Type                  ,
                                                        P_Wcode        => I.W_Code                        ,
                                                        P_Doctype      => 6                               ,
                                                        P_Docno        => I.Out_No                        ,
                                                        P_Billdoctype  => I.Out_Type                      ,
                                                        P_Cc_Code      => I.Cc_Code                       ,
                                                        P_Pj_No        => I.Pj_No                         ,
                                                        P_Actv_No      => I.Actv_No                       ,                                                                                                        
                                                        P_Rcrdno       => I.Rcrd_No                       ,
                                                        P_Expdate      => To_Date(Nvl(i.Expire_Date,'01/01/1900'),'DD/MM/YYYY') , 
                                                        P_Batchno      => Nvl(I.Batch_No,'0')             ,
                                                        P_Docser       => I.Out_Ser                       ,
                                                        P_Docseq       => V_Seq                           ,
                                                        P_Idate        => J.Out_Date                      ,
                                                        P_Vatamt       => 0                               , 
                                                        P_Disamt       => 0                               ,
                                                        P_Acy          => J.A_Cy                          ,
                                                        P_Ac_Rate      => J.Ac_Rate                       ,
                                                        P_Stk_Rate     => J.Stock_Rate                    ,
                                                        P_C_Code       => J.C_Code                        ,
                                                        P_Adesc        => J.A_Desc                        ,
                                                        P_Refno        => J.Ref_No                        ,
                                                        P_Outno        => V_Out_No                        ,
                                                        P_Outgrser     => V_Out_Ser                       ,
                                                        P_Inout        => -1                              ,
                                                        P_Iprice       => V_Price                         ,
                                                        P_Ad_Date      => J.Ad_Date                       ,
                                                        P_Up_Date      => J.Up_Date                       ,
                                                        P_Brn_No       => I.Brn_No                        ,
                                                        P_Brn_Year     => I.Brn_Year                      ,
                                                        P_Cmp_No       => I.Cmp_No                          ,
                                                        P_Brn_Usr      => I.Brn_Usr                          );
              Exception
               When Others Then
                 Raise_Application_Error(-20009,'Error When Insert Into Sale Cost '||Chr(13)||SqlErrm);    
                 RollBack;
              End ;    
           End If;        
         End Loop; --(2)
     End; --(12)        
--##-------------------------------------------------------------------------------------##--  
    Begin
        IAS_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 9             ,
                                              G_Doc_Ser     => J.Out_Ser     ,
                                              P_jv_type     => J.Out_Type    ,
                                              P_doc_no      => J.Out_No      ,
                                              P_Lang_no     => 1             ,
                                              P_User_No     => J.Ad_U_Id     ,
                                              G_Post_Type   => 0             );
     Exception 
       When No_Data_Found Then 
         Null;
       When Others Then
         Raise_Application_Error(-20010,'Error When Updating Post In Outgoing  = '||Chr(13)||'Out_Ser ='||J.Out_Ser ||Chr(13)||SqlErrm);                                                    
    End;                                                
--##-------------------------------------------------------------------------------------##--
    End Loop; --(1)
--##-------------------------------------------------------------------------------------##--
    --## Update Ias_Outgoing_Mst_Br        
    Begin            
          Update Ias_Outgoing_Mst_Br Set Out_Post=1
           Where nvl(Out_Post,0)=0                    
             And nvl(Hung,0)=0
             And Exists (Select 1 From Ias_Outgoing_Mst Where Out_Ser=Ias_Outgoing_Mst_Br.Out_Ser And RowNum<=1)
             And Exists (Select 1 From Ias_Outgoing_Mst_Br_Tmp Where Ias_Outgoing_Mst_Br_Tmp.Out_Ser = Ias_Outgoing_Mst_Br.Out_Ser  And RowNum <=1  ) ;
           Commit;
    Exception
      When Others Then
        Raise_Application_Error(-20011,'Error When Update Out_Post In  Update Ias_Outgoing_Mst_Br ');
    End ; 
--##-------------------------------------------------------------------------------------##--
  End ;                                                                                                     
--##-------------------------------------------------------------------------------------##--
End;    
--##-------------------------------------------------------------------------------------##--
PROCEDURE Post_Sales_Sum Is     
     V_Cnt       Number;
     V_Sqlstr    Varchar2(3000);
     V_sqlstr2   Varchar2(3000);
     V_Use_Itm_Attach            Ias_Para_Inv.Use_Itm_Attach%Type ;
     V_Costing_Type              Ias_Para_Inv.Costing_Type%Type   ;
     V_Wtavg_Type                Ias_Para_Inv.Wtavg_Type%Type     ;
     V_Invoicing_Serials         Ias_Para_Ar.Invoicing_Serials%Type  ;
     V_Use_Out_Bills             Ias_Para_Ar.Use_Out_Bills %Type     ;
      V_StkCost   Number;
      V_Seq       Number;
      V_StkRate   Number;
      V_Out_no    Number;      
     V_Out_ser   Number;      
      V_Cst       Number;
      V_BillAmt   Number;
      V_DiscAmt   Number;
      V_Othramt   Number;
      V_BillRate  Number;
      V_CardAmt   Number;
      V_CardAmt2  Number;
      V_CardAmt3  Number;
      V_ChequeAmt Number;
     V_DIsc_Mst  Number;
     V_Disc_Dtl  Number;
     V_Disc_Mst_Vat Number;
     V_VatAmt    Number;
     V_Bill_No   Number;
     V_Bill_Ser  Number;
     V_Rec       Number;
     v_comm_per_frst Number;   
     v_comm_per_scnd Number;   
     v_comm_per_thrd Number;
     V_Use_Vat       NUMBER;
     V_CALC_VAT_AMT_TYPE NUMBER ;
     V_E_INVC_MTHD_NO  NUMBER;
     V_TAX_BILL_TYP   NUMBER;
      
   
Begin
--##------------------------------------------------------------------------------------##--
   --# To Insert Into  Ias_pos_minus_qty Temporary Table 
   Begin
         If    Ias_Gen_Pkg.Get_Cnt ('Select Use_Expire_Date From Ias_Para_Inv Where RowNum <= 1 ') = 0   
           And Ias_Gen_Pkg.Get_Cnt ('Select Use_Batch_No From Ias_Para_Inv Where RowNum <= 1 ') = 0  Then
                         Insert Into IAS_POS_MINUS_QTY_TMP(I_Code ,Itm_Unt,W_Code ,Expire_Date,Batch_No,P_Qty,Avl_Qty,Brn_No)        
                            Select I_Code ,Itm_Unt,W_Code,Expire_Date,Batch_No,P_Qty,Avl_Qty,Brn_No From(
                                            Select Ias_Bill_Dtl_Br.I_Code                                        ,
                                            Ias_Itm_Pkg.Get_Icode_Min_Unit(Ias_Bill_Dtl_Br.I_Code ) Itm_Unt,
                                                       Ias_Bill_Dtl_Br.W_Code                                        ,
                                                       Nvl(Ias_Bill_Dtl_Br.Expire_Date,'01/01/1900')Expire_Date      ,
                                                       Nvl(Ias_Bill_Dtl_Br.Batch_No,'0') Batch_No                    ,
                                                       Sum(Nvl(Ias_Bill_Dtl_Br.P_Qty,0))+Sum(Nvl(Ias_Bill_Dtl_Br.Free_Qty,0)*Nvl(Ias_Bill_Dtl_Br.P_Size,1)) P_Qty  ,                                            
                                                         Nvl(Get_Icode_Avlqty(Ias_Bill_Dtl_Br.I_Code                   ,
                                                                          1                                             ,
                                                                          Ias_Bill_Dtl_Br.W_Code                       ,
                                                                          Null ,
                                                                          Null ),0) Avl_Qty                           ,
                                                                          Ias_Bill_Dtl_Br.Brn_No
                                                     From Ias_Bill_Mst_Br ,Ias_Bill_Dtl_Br
                                                    Where Ias_Bill_Mst_Br.Bill_No = Ias_Bill_Dtl_Br.Bill_No                          
                                                      And Nvl(Ias_Bill_Mst_Br.Bill_Post,0) = 0
                                                      And Nvl(Ias_Bill_Mst_Br.Stand_by,0)   = 0 
                                                      And Nvl(Ias_Bill_Dtl_Br.Service_Item,0)=0 
                                                Group By Ias_Bill_Dtl_Br.Brn_No,Ias_Bill_Dtl_Br.I_Code,Ias_Bill_Dtl_Br.W_Code,Nvl(Ias_Bill_Dtl_Br.Expire_Date,'01/01/1900'), Nvl(Ias_Bill_Dtl_Br.Batch_No,'0')
                                                Having Nvl(Get_Icode_Avlqty(Ias_Bill_Dtl_Br.I_Code,1,Ias_Bill_Dtl_Br.W_Code,Null,Null,Null),0) 
                                          -( Nvl(Sum(P_Qty),0)+Sum(Nvl(Ias_Bill_Dtl_Br.Free_Qty,0)*Nvl(Ias_Bill_Dtl_Br.P_Size,1))) < 0 )    ;
         Else
                         Insert Into IAS_POS_MINUS_QTY_TMP(I_Code ,Itm_Unt,W_Code ,Expire_Date,Batch_No,P_Qty,Avl_Qty,Brn_No)
                            Select I_Code ,Itm_Unt,W_Code,Expire_Date,Batch_No,P_Qty,Avl_Qty,Brn_No From(
                                            Select Ias_Bill_Dtl_Br.I_Code                                        ,
                                                   Ias_Itm_Pkg.Get_Icode_Min_Unit(Ias_Bill_Dtl_Br.I_Code ) Itm_Unt,
                                                       Ias_Bill_Dtl_Br.W_Code                                        ,
                                                       Nvl(Ias_Bill_Dtl_Br.Expire_Date,'01/01/1900')Expire_Date      ,
                                                       Nvl(Ias_Bill_Dtl_Br.Batch_No,'0') Batch_No                    ,
                                                       Sum(Nvl(Ias_Bill_Dtl_Br.P_Qty,0))+Sum(Nvl(Ias_Bill_Dtl_Br.Free_Qty,0)*Nvl(Ias_Bill_Dtl_Br.P_Size,1)) P_Qty  , 
                                                         Nvl(Get_Icode_Avlqty(Ias_Bill_Dtl_Br.I_Code                   ,
                                                                          1                                             ,
                                                                          Ias_Bill_Dtl_Br.W_Code                       ,
                                                                          Nvl(Ias_Bill_Dtl_Br.Expire_Date,'01/01/1900'),
                                                                          Nvl(Ias_Bill_Dtl_Br.Batch_No,'0') ),0) Avl_Qty ,
                                                                          Ias_Bill_Dtl_Br.Brn_No
                                                     From Ias_Bill_Mst_Br ,Ias_Bill_Dtl_Br
                                                    Where Ias_Bill_Mst_Br.Bill_No = Ias_Bill_Dtl_Br.Bill_No                          
                                                      And Nvl(Ias_Bill_Mst_Br.Bill_Post,0)   = 0 
                                                      And Nvl(Ias_Bill_Mst_Br.Stand_by,0)   = 0
                                                      And Nvl(Ias_Bill_Dtl_Br.Service_Item,0)=0 
                                                Group By Ias_Bill_Dtl_Br.Brn_No,Ias_Bill_Dtl_Br.I_Code,Ias_Bill_Dtl_Br.W_Code,Nvl(Ias_Bill_Dtl_Br.Expire_Date,'01/01/1900'), Nvl(Ias_Bill_Dtl_Br.Batch_No,'0')
                                                Having Nvl(Get_Icode_Avlqty(Ias_Bill_Dtl_Br.I_Code,1,Ias_Bill_Dtl_Br.W_Code,Nvl(Ias_Bill_Dtl_Br.Expire_Date,'01/01/1900'),Nvl(Ias_Bill_Dtl_Br.Batch_No,'0'),Null),0) 
                                          -( Nvl(Sum(P_Qty),0)+Sum(Nvl(Ias_Bill_Dtl_Br.Free_Qty,0)*Nvl(Ias_Bill_Dtl_Br.P_Size,1))) < 0 )    ;                     
         End If ;     
   Exception 
     When Others Then
       Raise_Application_Error ( -20001,' Err. When Insert Into Temp IAS_POS_MINUS_QTY_TMP Table ');
   End;
--##-------------------------------------------------------------------------------------##--        
    --Check_Avl_Qty(1);
--##-------------------------------------------------------------------------------------##--       
   Begin
      Select 1 Into V_Cnt
       From  IAS_POS_MINUS_QTY_TMP
        Where RowNum <=1 ;
   Exception
       When Others  Then
        V_Cnt := 0 ;
     End ; 
   If Nvl(V_Cnt,0)>0 Then ---(2)
      -- Make Adjustment 
      Post_Stk_Adjstmnt ;
    End If; 
--##-------------------------------------------------------------------------------------##-- 
    --## Read Parameters
    Begin
           Select Nvl(Costing_Type,0)   ,
                  Nvl(Wtavg_Type,0)     ,
                  Nvl(Invoicing_Serials,0), 
                  Nvl(Use_Out_Bills ,0) ,
                  Nvl(Use_Itm_Attach ,0) ,
                  NVL(Use_Vat,0) ,
                  NVL(V_CALC_VAT_AMT_TYPE,0)  
            Into  V_Costing_Type              ,
                  V_Wtavg_Type                ,
                  V_Invoicing_Serials         ,
                  V_Use_Out_Bills             ,
                  V_Use_Itm_Attach      ,
                  V_Use_Vat   ,
                  V_CALC_VAT_AMT_TYPE  
           From Ias_Para_Inv ,Ias_Para_Ar ,IAS_PARA_GEN;
    Exception
      When Others Then
        Raise_Application_Error(-20004,'Error When Get Parameter Data '||Chr(13)||SqlErrm);  
    End ;   
--##-----------------------------------------------------------------------------------##--  
    Insert Into Ias_Bill_Mst_Br_Tmp Select Bill_No , Bill_Ser From Ias_Bill_Mst_Br Where Nvl(Bill_Post,0) = 0 ;
    Declare
      Cursor SM Is Select   Distinct    Bill_Date,
                                        A_code,
                                        Cash_no,                                                   
                                        Bill_Doc_type,
                                        bill_currency ,
                                        w_code,
                                        Cc_Code,
                                        Pj_No,
                                        Actv_No,
                                        Si_Type,
                                        Rep_Code,
                                        Cr_Card_No,
                                        Cr_Card_No_Scnd, 
                                        Cr_Card_No_Thrd, 
                                        Cash_Ac_Fcc,
                                        Note_No,
                                        Credit_Card,
                                        Cheque_No,
                                        Cheque_Due_Date,
                                        Clc_Typ_No_Tax,
                                        Clc_Vat_Price_Typ,
                                        Ad_U_Id,
                                        Brn_No,
                                        Brn_Year,
                                        Cmp_No,
                                        Brn_Usr,
                                        Doc_Brn_No
         From Ias_Bill_Mst_Br
           Where bill_doc_type<>4
             and nvl(bill_post,0)=0
             and nvl(Stand_By,0)=0  
             And Exists(Select 1 From Ias_Bill_Dtl_Br Where Bill_Ser=Ias_Bill_Mst_Br.Bill_Ser And RowNum<=1)
             And Exists (Select 1 From Ias_Bill_Mst_Br_Tmp Where Ias_Bill_Mst_Br_Tmp.Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser  And RowNum <=1  )
          Order By  Bill_Date,
                    Cash_no,                                                   
                    bill_currency ,
                    Ad_U_Id ;
    Begin ---(11)        
--##-------------------------------------------------------------------------------------##--    
        --## To Get Stock Rate           
        V_StkRate := Ias_Gen_Pkg.Get_Cur_rate(p_acy=> Ias_Gen_Pkg.Get_Stk_Cur);      
--##-------------------------------------------------------------------------------------##--    
        For j in SM Loop     -->> (1)              
            Begin
                  Select Sum(Bill_Amt) ,
                         Sum(Nvl(Disc_Amt,0)) ,
                         Sum(Nvl(Othr_Amt,0)),
                         Nvl(Avg(Bill_Rate),1) Billrate  ,
                         Sum(Nvl(Cr_Card_Amt,0)) ,
                         Sum(Nvl(Cr_Card_Amt_Scnd,0)) ,
                         Sum(Nvl(Cr_Card_Amt_Thrd,0)) ,
                         Sum(Nvl(Cheque_Amt,0)),
                         Sum(Nvl(Disc_Amt_Mst,0)),
                         Sum(Nvl(Disc_Amt_Dtl,0)),
                         Sum(Nvl(Vat_Amt,0)),
                         Sum(nvl(Disc_Amt_Mst_Vat,0))
                      Into V_Billamt, 
                           V_Discamt,
                           V_Othramt,
                           V_Billrate,
                           V_Cardamt,
                           V_Cardamt2,
                           V_Cardamt3,
                           V_Chequeamt,
                           V_Disc_Mst,
                           V_Disc_Dtl,
                           V_Vatamt  ,
                           V_Disc_Mst_Vat
                   From  Ias_Bill_Mst_Br
                    Where  Bill_Doc_Type <> 4
                      And Exists (Select 1 From Ias_Bill_Mst_Br_Tmp Where Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser  And RowNum <=1  )
                      And  Nvl(Bill_Post,0)         = 0
                      And  Bill_Date                = J.Bill_Date
                      And  Bill_Currency             = J.Bill_Currency
                      And  Si_Type                     = Nvl(J.Si_Type,0)
                      And  A_Code                   = J.A_Code
                      And  Nvl(Cash_No,0)           = Nvl(J.Cash_No,0)                                                                                     
                      And  Bill_Doc_Type            = J.Bill_Doc_Type
                      And  Nvl(W_Code,0)            = Nvl(J.W_Code,0)
                      And  Nvl(Cc_Code,'0')         = Nvl(J.Cc_Code,0)
                      And  Nvl(Pj_No,'0')           = Nvl(J.Pj_No,'0')
                      And  Nvl(Actv_No,'0')         = Nvl(J.Actv_No,'0')                                                    
                      And  Nvl(Cr_Card_No,0)        = Nvl(J.Cr_Card_No,0)
                      And  Nvl(Cr_Card_No_Scnd,0)   = Nvl(J.Cr_Card_No_Scnd,0)
                      And  Nvl(Cr_Card_No_Thrd,0)   = Nvl(J.Cr_Card_No_Thrd,0)                          
                      And  Nvl(Note_No,'0')         = Nvl(J.Note_No,0)
                      And  Nvl(Credit_Card,0)       = Nvl(J.Credit_Card,0)
                      And  Nvl(Cheque_No,'0')       = Nvl(J.Cheque_No,'0')
                      And  Nvl(Cash_Ac_Fcc,'0')     = Nvl(J.Cash_Ac_Fcc,'0')                          
                      And  Nvl(Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
                      And  Clc_Typ_No_Tax           = Nvl(J.Clc_Typ_No_Tax,0)
                      And  Clc_Vat_Price_Typ        = Nvl(J.Clc_Vat_Price_Typ,0)
                      And  NVL(REP_CODE,0)          = Nvl(J.REP_CODE,0)
                      And  Ad_U_Id                  = J.Ad_U_Id
                      And  Doc_Brn_No               = Nvl(J.Doc_Brn_No,0)
                      And  Brn_No                   = J.Brn_No
                      And  Brn_Year                 = J.Brn_Year
                      And  Cmp_No                   = J.Cmp_No
                      And  Brn_Usr                  = J.Brn_Usr;
            Exception When Others Then
                 Raise_Application_Error(-20001,'Err. When Select Amt From Bills '||CHr(13)||SqlErrm);
            End;                       
      ----------------------------------------------------------------------------------
            --V_Bill_No  := Get_Bill_No  ( V_Invoicing_Serials,J.Si_Type,J.Cc_Code,J.Bill_Doc_Type,J.W_Code,J.Brn_No);
           Begin
             V_Bill_No:=AR_DOC_SQ_PKG.GET_DOC_NO ( P_DOC_TYP       =>4,
                                                  P_PAY_TYP        =>J.Bill_Doc_Type,    
                                                  P_BRN_YEAR       =>J.Brn_Year,
                                                  P_BRN_NO        =>J.Brn_No,
                                                  P_CC_CODE       =>J.Cc_Code,
                                                  P_W_CODE        =>J.W_Code,
                                                  P_TYP_NO        =>J.SI_type, 
                                                  P_Sys_No        =>85,
                                                  P_Usr_No        =>j.ad_u_id,
                                                  P_Trmnl_No      => null );     
           Exception When Others Then
                RollBack;
                Raise_Application_Error (-20001,' Err. In Get Bill No ');  
           End ;                                        
      ----------------------------------------------------------------------------------
          --  V_Bill_Ser := Get_Bill_Ser ( V_Invoicing_Serials,J.Si_Type,J.Cc_Code,V_Bill_No,J.Bill_Doc_Type,J.W_Code,J.Brn_No,J.Brn_Year);
          Begin
             V_Bill_Ser:=AR_DOC_SQ_PKG.GET_DOC_SRL (  P_DOC_TYP     =>4,
                                                      P_PAY_TYP       =>J.Bill_Doc_Type,    
                                                      P_BRN_YEAR      =>J.brn_year,
                                                      P_BRN_NO        =>J.Brn_No,
                                                      P_CC_CODE       =>J.Cc_Code,
                                                      P_W_CODE        =>J.W_Code,
                                                      P_TYP_NO        =>J.SI_type,
                                                      P_DOC_NO        =>V_Bill_No,
                                                      P_Sys_No        =>85,
                                                      P_Usr_No        =>j.ad_u_id,
                                                      P_Trmnl_No      => null  );    
           Exception When Others Then
               RollBack;
               Raise_Application_Error (-20001,' Err. In Get Bill serial ');   
           End ;  
          ----------------------------------------------------------------------------------------------------------------------------------
            Begin
              v_comm_per_frst := Get_Card_Comm_Prcnt ( P_Cr_Card_No => J.Cr_Card_No);
              v_comm_per_scnd := Get_Card_Comm_Prcnt ( P_Cr_Card_No => J.Cr_Card_No_scnd);
              v_comm_per_thrd := Get_Card_Comm_Prcnt ( P_Cr_Card_No => J.Cr_Card_No_thrd);
            Exception 
              When Others Then Null;
            End;  
      ----------------------------------------------------------------------------------           
            Begin
                 Insert Into Ias_Bill_Mst(  Bill_Doc_Type, 
                                            Bill_No, 
                                            Bill_Ser, 
                                            Si_Type,
                                            Bill_Date, 
                                            Bill_Currency, 
                                            Bill_Rate, 
                                            Stock_Rate,                                                                 
                                            A_Code, 
                                            C_Name,                                                                
                                            Cheque_No, 
                                            Note_No, 
                                            Cheque_Amt, 
                                            Cheque_Due_Date, 
                                            Bill_Due_Date, 
                                            Bill_Post, 
                                            DIsc_Amt, 
                                            DIsc_Amt_Mst,
                                            DIsc_Amt_Mst_Vat, 
                                            DIsc_Amt_Dtl, 
                                            Othr_Amt, 
                                            Vat_Amt, 
                                            Bill_Amt, 
                                            W_Code, 
                                            R_Code, 
                                            Rep_Code, 
                                            Ref_No, 
                                            Cash_No, 
                                            Cc_Code, 
                                            Pj_No,
                                            Actv_No,
                                            Cr_Card_No, 
                                            Cr_Card_Amt, 
                                            Credit_Card, 
                                            Export, 
                                            Stand_By, 
                                            Col_No, 
                                            Cash_Ac_Fcc, 
                                            A_Desc, 
                                            Comm_Per, 
                                            Pr_Rep,                                                                 
                                            Processed, 
                                            Load_No, 
                                            Ad_U_Id, 
                                            Ad_Date, 
                                            Up_U_Id, 
                                            Up_Date, 
                                            Field1, 
                                            Field2, 
                                            Field3, 
                                            Brn_No, 
                                            Brn_Year, 
                                            Load_Ser, 
                                            Audit_Ref, 
                                            Audit_Ref_Desc, 
                                            Audit_Ref_Date, 
                                            Audit_Ref_U_Id,
                                            External_Post,
                                            Cmp_No,
                                            Brn_Usr,
                                            Cr_Card_No_Scnd,
                                            Cr_Card_No_Thrd,
                                            Cr_Card_Amt_Scnd,
                                            Cr_Card_Amt_Thrd,
                                            CR_CARD_COMM_PER, 
                                            CR_CARD_COMM_PER_SCND, 
                                            CR_CARD_COMM_PER_THRD,
                                            Doc_Brn_No,
                                            Clc_Typ_No_Tax,
                                            Clc_Vat_Price_Typ,
                                            Doc_Pst_Sq,
                                            E_INVC_MTHD_NO
                                            )
                 Values(    J.Bill_Doc_Type, 
                            V_Bill_No, 
                            V_Bill_Ser, 
                            J.Si_Type,
                            J.Bill_Date, 
                            J.Bill_Currency, 
                            V_BillRate, 
                            V_StkRate,                                                                 
                            J.A_Code, 
                            Ias_Gen_Pkg.Get_Prompt(1,1924)||' '||J.Ad_U_Id, 
                            J.Cheque_No, 
                            J.Note_No, 
                            V_ChequeAmt, 
                            J.Cheque_Due_Date, 
                            Null, 
                            0, 
                            Nvl(V_DiscAmt,0), 
                            Nvl(V_Disc_Mst,0), 
                            nvl(V_Disc_Mst_Vat,0),
                            Nvl(V_Disc_Dtl,0), 
                            Nvl(V_OthrAmt,0), 
                            Nvl(V_VatAmt,0), 
                            Nvl(V_BillAmt,0), 
                            J.W_Code, 
                            Null, 
                            Null, 
                            'RES', 
                            J.Cash_No, 
                            J.Cc_Code,
                            J.Pj_No,
                            J.Actv_No, 
                            J.Cr_Card_No, 
                            Nvl(V_CardAmt,0), 
                            J.Credit_Card, 
                            Null, 
                            0, 
                            Null, 
                            J.Cash_Ac_Fcc, 
                            --'Post From Light System', 
                            Nvl(Ias_Gen_Pkg.Get_Prompt(1,1925),'OnyxLight'),                                                                 
                            Null, 
                            Null,                                                                
                            Decode(V_Use_Out_Bills,1,1,0),
                            Null,
                            J.Ad_U_Id, 
                            Ias_Gen_Pkg.Get_CurDate,
                            null,
                            null,
                            null,
                            null,
                            null,
                            J.Brn_No, 
                            J.Brn_Year, 
                            Null,
                            Null,
                            Null,
                            Null,
                            Null,
                            2 ,
                            J.Cmp_No,
                            J.Brn_Usr,
                            J.Cr_Card_No_Scnd,
                            J.Cr_Card_No_Thrd,
                            V_CardAmt2,
                            V_CardAmt3,
                            v_comm_per_frst,
                            v_comm_per_scnd,
                            v_comm_per_thrd,
                            J.Doc_Brn_No,
                            j.Clc_Typ_No_Tax,
                            j.clc_Vat_Price_Typ,
                            IAS_POSTING_PKG.GET_DOC_PST_SQ,
                            Decode(Nvl(Ias_Brn_Pkg.Is_Brn_Use_E_Invc ( P_Brn_No => J.Brn_No),0),1,Gnr_Get_E_Invc_Actv_Mthd  ( P_Doc_Typ => 4,P_Sys_No => 85),Null));
        Exception
         When Others Then            
            Raise_Application_Error(-20002,'Err. When Insert Into Ias_Bill_Mst '||CHR(13)||SqlErrm);             
            RollBack ;   
        End;        
--##-------------------------------------------------------------------------------------##--    
        --## Other_Charges
        Begin
            Insert_Other_Charges( V_Bill_No,
                                  j.bill_doc_type,
                                  V_Bill_Ser,
                                  j.Bill_date,
                                  j.Ad_U_id,
                                  j.Bill_Currency,
                                  j.Cash_No,
                                  Null,
                                  'S');
        Exception
         When Others Then
            Raise_Application_Error(-20003,'Err. When Insert Into Others Charges '||CHr(13)||SqlErrm);                           
        End;      
--##-------------------------------------------------------------------------------------##--                              
        If Nvl(V_Use_Out_Bills,0) = 1 Then
             Begin
               V_Out_No  := Ias_Insrt_Out_Bills_Pkg.Get_Out_No  ( P_Invs          => V_Invoicing_Serials, 
                                                                  P_Si_Type       => J.Si_Type          ,
                                                                  P_Cc_Code       => J.Cc_Code          ,
                                                                  P_w_code        => J.w_Code           ,
                                                                  P_bill_doc_type => J.bill_doc_type    ,
                                                                  P_Brn_No        => J.Brn_No           );   
               V_Out_Ser := Ias_Insrt_Out_Bills_Pkg.Get_Out_Ser ( P_Out_No        => V_Out_No,
                                                                  P_Si_Type       => J.Si_Type,
                                                                  P_Invs          => V_Invoicing_Serials,
                                                                  P_Cc_Code       => J.Cc_Code,
                                                                  P_w_code        => J.w_code,
                                                                  P_bill_doc_type => J.bill_doc_type,
                                                                  P_Brn_No        => J.Brn_No,
                                                                  P_Brn_Year      => J.Brn_Year);
           Exception
             When Others Then
                Raise_Application_Error(-20004,'Err. When Get Out Bills Serial '||Chr(13)||SqlErrm);                           
           End;         
        End If;   
--##-------------------------------------------------------------------------------------##--    
        Declare
             Cursor BD Is Select   Sum(Ias_Bill_Dtl_Br.I_Qty)          I_qty,
                                   Sum(Ias_Bill_Dtl_Br.P_Qty)          P_qty,
                                   Sum(Ias_Bill_Dtl_Br.Free_Qty)       Free_qty,
                                   Ias_Bill_Dtl_Br.I_Code              I_code,
                                   Ias_Bill_Dtl_Br.Post_Code           Post_Code,
                                   Ias_Bill_Dtl_Br.I_Price             I_price, 
                                   Ias_Bill_Dtl_Br.I_price_Vat         I_price_Vat,  
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt,0)      Dis_amt,                               
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt_Mst,0)  Dis_Amt_Mst,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt_Mst_Vat,0)  Dis_amt_Mst_Vat,
                                   Nvl(Ias_Bill_Dtl_Br.Vat_Amt_Dis_Mst_Vat,0)  Vat_Amt_Dis_Mst_Vat,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_Per,0)      Dis_Per,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt_Dtl,0)  Dis_Amt_Dtl,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt_Dtl_Vat,0)  Dis_Amt_Dtl_Vat,
                                   Nvl(Ias_Bill_Dtl_Br.Vat_Amt_Dis_Dtl_Vat,0)  Vat_Amt_Dis_Dtl_Vat,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_Per2,0)     Dis_Per2,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt_Dtl2,0) Dis_Amt_Dtl2,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt_Dtl2_Vat,0)  Dis_Amt_Dtl2_Vat,
                                   Nvl(Ias_Bill_Dtl_Br.Vat_Amt_Dis_Dtl2_Vat,0)  Vat_Amt_Dis_Dtl2_Vat,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_Per3,0)     Dis_Per3,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt_Dtl3,0) Dis_Amt_Dtl3,
                                   Nvl(Ias_Bill_Dtl_Br.Dis_amt_Dtl3_Vat,0)  Dis_Amt_Dtl3_Vat,
                                   Nvl(Ias_Bill_Dtl_Br.Vat_Amt_Dis_Dtl3_Vat,0)  Vat_Amt_Dis_Dtl3_Vat,
                                   Nvl(Ias_Bill_Dtl_Br.Othr_amt,0)     Othr_amt,
                                   Nvl(Ias_Bill_Dtl_Br.vat_amt,0)      Vat_amt,
                                   Nvl(Ias_Bill_Dtl_Br.vat_Per,0)      Vat_Per,
                                   Ias_Bill_Dtl_Br.Itm_Unt             Itm_Unt,
                                   Ias_Bill_Dtl_Br.P_size              P_size,
                                   Ias_Bill_Dtl_Br.Expire_Date         Expire_Date,
                                   Ias_Bill_Dtl_Br.Batch_No            Batch_No,
                                   Ias_Bill_Dtl_Br.w_code              w_code,
                                   Ias_Bill_Dtl_Br.Cc_Code             Cc_Code,
                                   Ias_Bill_Mst_Br.Pj_No               Pj_No,
                                   Ias_Bill_Mst_Br.Actv_No             Actv_No,
                                   Ias_Bill_Dtl_Br.Si_Type             Si_Type,
                                   Nvl(Ias_Bill_Dtl_Br.Use_Attch,0)    Use_Attch,
                                   Ias_Bill_Mst_Br.a_code              a_code,
                                   Ias_Bill_Mst_Br.cash_no             cash_no,                               
                                   Ias_Bill_Mst_Br.Bill_Doc_type       Bill_doc_type,
                                   Ias_Bill_Mst_Br.BILL_DATE           Bill_date,                       
                                   Ias_Bill_Mst_Br.bill_currency       Bill_currency,                               
                                   Nvl(Ias_Bill_Dtl_Br.Service_Item,0) Service_Item,
                                   Ias_Bill_Dtl_Br.Brn_No,
                                   Ias_Bill_Dtl_Br.Brn_Year,
                                   Ias_Bill_Dtl_Br.Cmp_No,
                               Ias_Bill_Dtl_Br.Brn_Usr                                
                        From Ias_Bill_Mst_Br,Ias_Bill_Dtl_Br
                            Where Ias_Bill_Mst_Br.Bill_Ser=Ias_Bill_Dtl_Br.Bill_Ser
                                And Exists (Select 1 From Ias_Bill_Mst_Br_Tmp Where Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser  And RowNum <=1  ) 
                                And  Ias_Bill_Mst_Br.Bill_Doc_Type <> 4
                                And  Ias_Bill_Mst_Br.Bill_Post          = 0
                                And  Ias_Bill_Mst_Br.Bill_Date          = J.Bill_Date
                                And  Ias_Bill_Mst_Br.Bill_Currency         = J.Bill_Currency
                                And  Ias_Bill_Mst_Br.A_Code             = J.A_Code
                                And  Nvl(Ias_Bill_Mst_Br.Cash_No,0)     = Nvl(J.Cash_No,0)
                                And  Nvl(Ias_Bill_Mst_Br.Si_Type,0)     = Nvl(J.Si_Type,0)
                                And  Ias_Bill_Mst_Br.Bill_Doc_Type      = J.Bill_Doc_Type
                                And  Nvl(Ias_Bill_Mst_Br.W_Code,0)      = Nvl(J.W_Code,0)
                                And  Nvl(Ias_Bill_Mst_Br.Cc_Code,'0')   = Nvl(J.Cc_Code,'0')
                                And  Nvl(Ias_Bill_Mst_Br.Pj_No,'0')     = Nvl(J.Pj_No,'0')
                                And  Nvl(Ias_Bill_Mst_Br.Actv_No,'0')   = Nvl(J.Actv_No,'0')                
                                And  Nvl(Ias_Bill_Mst_Br.Cr_Card_No,0)  = Nvl(J.Cr_Card_No,0)
                                And  Nvl(Ias_Bill_Mst_Br.Cr_Card_No_Scnd,0)  = Nvl(J.Cr_Card_No_Scnd,0)
                                And  Nvl(Ias_Bill_Mst_Br.Cr_Card_No_Thrd,0)  = Nvl(J.Cr_Card_No_Thrd,0)
                                And  Nvl(Ias_Bill_Mst_Br.Note_No,'0')   = Nvl(J.Note_No,'0')
                                And  Nvl(Ias_Bill_Mst_Br.Credit_Card,0) = Nvl(J.Credit_Card,0)
                                And  Nvl(Ias_Bill_Mst_Br.Cheque_No,'0') = Nvl(J.Cheque_No,'0')
                                And  Nvl(Ias_Bill_Mst_Br.Cash_Ac_Fcc,'0') = Nvl(J.Cash_Ac_Fcc,'0')                          
                                And  Nvl(Ias_Bill_Mst_Br.Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
                                and  Ias_Bill_Mst_Br.Clc_Typ_No_Tax     = Nvl(J.Clc_Typ_No_Tax,0)
                                and  Ias_Bill_Mst_Br.Clc_Vat_Price_Typ  = Nvl(J.Clc_Vat_Price_Typ,0)
                                And  NVL(Ias_Bill_Mst_Br.REP_CODE,0)           = Nvl(J.REP_CODE,0)
                                And  Ias_Bill_Mst_Br.Ad_U_Id            = J.Ad_U_Id
                                And  Ias_Bill_Mst_Br.Doc_Brn_No         = Nvl(J.Doc_Brn_No,0)
                                And  Ias_Bill_Mst_Br.Brn_No             = J.Brn_No
                                And  Ias_Bill_Mst_Br.Brn_Year           = J.Brn_Year
                                And  Ias_Bill_Dtl_Br.Cmp_No             = J.Cmp_No
                                And  Ias_Bill_Dtl_Br.Brn_Usr              = J.Brn_Usr                          
                      Group by Ias_Bill_Dtl_Br.I_Code ,
                               Ias_Bill_Dtl_Br.Post_Code,
                               Ias_Bill_Dtl_Br.I_Price, 
                               Ias_Bill_Dtl_Br.I_Price_Vat,  
                               Ias_Bill_Dtl_Br.Dis_amt,               
                               Ias_Bill_Dtl_Br.Dis_amt_Mst,
                               Ias_Bill_Dtl_Br.Dis_amt_Mst_Vat,
                               Ias_Bill_Dtl_Br.Vat_Amt_Dis_Mst_Vat,
                               Ias_Bill_Dtl_Br.Dis_Per,
                               Ias_Bill_Dtl_Br.Dis_amt_Dtl,
                               Ias_Bill_Dtl_Br.Dis_amt_Dtl_Vat,
                               Ias_Bill_Dtl_Br.Vat_Amt_Dis_Dtl_Vat,
                               Ias_Bill_Dtl_Br.Dis_Per2,
                               Ias_Bill_Dtl_Br.Dis_amt_Dtl2,
                               Ias_Bill_Dtl_Br.Dis_amt_Dtl2_Vat,
                               Ias_Bill_Dtl_Br.Vat_Amt_Dis_Dtl2_Vat,
                               Ias_Bill_Dtl_Br.Dis_Per3,
                               Ias_Bill_Dtl_Br.Dis_amt_Dtl3,
                               Ias_Bill_Dtl_Br.Dis_amt_Dtl3_Vat,
                               Ias_Bill_Dtl_Br.Vat_Amt_Dis_Dtl3_Vat,
                               Ias_Bill_Dtl_Br.Othr_amt,
                               Ias_Bill_Dtl_Br.vat_amt,
                               Ias_Bill_Dtl_Br.vat_Per,
                               Ias_Bill_Dtl_Br.Itm_Unt,
                               Ias_Bill_Dtl_Br.P_size,
                               Ias_Bill_Dtl_Br.Expire_Date,
                               Ias_Bill_Dtl_Br.Batch_No,
                               Ias_Bill_Dtl_Br.w_code,
                               Ias_Bill_Dtl_Br.Cc_Code,
                               Ias_Bill_Mst_Br.Pj_No,
                               Ias_Bill_Mst_Br.Actv_No,
                               Ias_Bill_Dtl_Br.Si_Type,
                               Nvl(Ias_Bill_Dtl_Br.Use_Attch,0),
                               Ias_Bill_Mst_Br.a_code,
                               Ias_Bill_Mst_Br.cash_no,                               
                               Ias_Bill_Mst_Br.Bill_Doc_type,
                               Ias_Bill_Mst_Br.BILL_DATE,                       
                               Ias_Bill_Mst_Br.bill_currency,                               
                               Nvl(Ias_Bill_Dtl_Br.Service_Item,0),
                               Ias_Bill_Dtl_Br.Brn_No,
                               Ias_Bill_Dtl_Br.Brn_Year,                                    
                               Ias_Bill_Dtl_Br.Cmp_No,
                               Ias_Bill_Dtl_Br.Brn_Usr
                     Order By  Ias_Bill_Mst_Br.Bill_Date,             
                               Ias_Bill_Mst_Br.Bill_Currency,
                               Ias_Bill_Mst_Br.Ad_U_Id;
--##-------------------------------------------------------------------------------------##--           
         Begin --- (12)         
               V_Rec := 0;
             For i in BD  Loop        -->> (2)                          
                 V_Rec := V_Rec+1;              
                             
         --##-------------------------------------------------------------------------------------##--                               
                 Begin    
                      V_StkCost := Ias_Itm_Inv_Pkg.Get_Itm_Cost(  P_costing_type => V_Costing_Type           ,
                                                                  P_Wtavg_Type   => V_Wtavg_Type             ,
                                                                  P_icode        => i.i_code                 ,
                                                                  P_wcode        => i.w_code                 ,
                                                                  P_Psize        => Nvl(i.p_Size,1)          ,
                                                                  P_Iqty         => ( Nvl(i.i_qty,0) + Nvl(i.free_qty,0) ),
                                                                  P_ExpDate      => To_Date(Nvl(i.Expire_Date,'01/01/1900'),'DD/MM/YYYY'),
                                                                  P_BatchNo      => Nvl(i.Batch_No,'0')      ,
                                                                  P_brn_no       => J.brn_no                 ,
                                                                  P_brn_year     => J.brn_year               ,
                                                                  P_Cmp_No       => J.Cmp_No                 ,
                                                                  P_Brn_Usr      => J.Brn_Usr                 );
                 Exception 
                   When Others Then
                       Raise_Application_Error(-20005,'Err. When Get Item Cost '||Chr(13)||SqlErrm);                                                         
                 End;                         
                    --##----------------------------------------------------------------------------------##--       
                 Select Ias_Doc_Seq.NextVal InTo V_Seq From Dual;                    
                    --##----------------------------------------------------------------------------------##--
                 Begin
                      Insert Into Ias_Bill_Dtl( Bill_Doc_Type, 
                                                Bill_No, 
                                                Bill_Ser, 
                                                Si_Type,
                                                I_Code, 
                                                I_Qty, 
                                                Itm_Unt, 
                                                P_Size, 
                                                P_Qty, 
                                                I_Price,
                                                I_Price_Vat, 
                                                Stk_Cost,                                                                         
                                                W_Code, 
                                                Cc_Code,                                                                         
                                                Pj_No,
                                                Actv_No,
                                                Expire_Date, 
                                                Batch_No, 
                                                Free_Qty,                                                                         
                                                   Dis_Amt, 
                                                Dis_Amt_Mst,
                                                Dis_Amt_Mst_Vat,                                     
                                                Vat_Amt_Dis_Mst_Vat,
                                                Dis_Per, 
                                                Dis_Amt_Dtl,
                                                Dis_Amt_Dtl_Vat,  
                                                Vat_Amt_Dis_Dtl_Vat, 
                                                Dis_Per2, 
                                                Dis_Amt_Dtl2, 
                                                Dis_Amt_Dtl2_Vat,  
                                                Vat_Amt_Dis_Dtl2_Vat, 
                                                Dis_Per3, 
                                                Dis_Amt_Dtl3,
                                                Dis_Amt_Dtl3_Vat,    
                                                Vat_Amt_Dis_Dtl3_Vat, 
                                                Vat_Per, 
                                                Vat_Amt, 
                                                Othr_Amt,  
                                                Out_Qty,
                                                Out_Free_Qty,
                                                Use_Serialno, 
                                                Service_Item, 
                                                Rcrd_No, 
                                                Item_Desc, 
                                                Use_Attch,
                                                Rec_Attch,
                                                Brn_No, 
                                                Brn_Year, 
                                                Doc_Sequence,
                                                External_Post,
                                                Cmp_No,
                                                Brn_Usr,
                                                Post_Code)
                     Values(    J.Bill_Doc_Type, 
                                V_BIll_No, 
                                V_Bill_Ser, 
                                I.Si_Type,
                                I.I_Code, 
                                I.I_Qty, 
                                I.Itm_Unt, 
                                I.P_Size, 
                                I.P_Qty, 
                                I.I_Price, 
                                I.I_Price_Vat,
                                V_StkCost,                                                                         
                                I.W_Code, 
                                I.Cc_Code,
                                I.Pj_No,                                                                         
                                I.Actv_No,                                                                                                                                                          
                                I.Expire_Date, 
                                I.Batch_No, 
                                I.Free_Qty,                                                                         
                                   I.Dis_Amt, 
                                I.Dis_Amt_Mst, 
                                I.Dis_Amt_Mst_Vat,                                     
                                I.Vat_Amt_Dis_Mst_Vat ,
                                I.Dis_Per, 
                                I.Dis_Amt_Dtl,
                                I.Dis_Amt_Dtl_Vat,  
                                I.Vat_Amt_Dis_Dtl_Vat, 
                                I.Dis_Per2, 
                                I.Dis_Amt_Dtl2, 
                                I.Dis_Amt_Dtl2_Vat,  
                                I.Vat_Amt_Dis_Dtl2_Vat, 
                                I.Dis_Per3, 
                                I.Dis_Amt_Dtl3,
                                I.Dis_Amt_Dtl3_Vat,    
                                I.Vat_Amt_Dis_Dtl3_Vat,
                                I.Vat_Per, 
                                I.Vat_Amt, 
                                I.Othr_Amt, 
                                Decode(V_Use_Out_Bills,1,I.I_Qty,0),
                                Decode(V_Use_Out_Bills,1,I.Free_Qty,0),
                                0, 
                                I.Service_Item, 
                                V_Rec, 
                                Null,
                                I.Use_Attch,
                                V_Rec,
                                I.Brn_No, 
                                I.Brn_Year, 
                                V_Seq,
                                2,
                                I.Cmp_No,
                                I.Brn_Usr,
                                I.Post_Code);
                 Exception
                  When Others Then
                  Raise_Application_Error(-20006,'Err. When Insrt Into Ias_Bill_Dtl '||Chr(13)||SqlErrm);
                   RollBack;
                 End; 
                    --##----------------------------------------------------------------------------------##--              
                 If  Nvl(V_Use_Itm_Attach,0) = 1 And I.Use_Attch=1 Then                  
                     Begin
                          Insert InTo Ias_Itm_Attach_Movement(  I_Code, Itm_Unt, P_Size, 
                                                                Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                                Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                                Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                                Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                                W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code, pj_no,actv_no,Rep_Code, 
                                                                R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                                Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Date, A_Cy, 
                                                                Ac_Rate, Stk_Rate, I_Price, Dis_Amt, I_Cost, Stk_Cost, Vat_Amt, 
                                                                V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                                Cmp_No, Brn_No, Brn_Year, Brn_Usr, Othr_Amt)
                            Select  I_Code, Itm_Unt, P_Size, 
                                    Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                    Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                    Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,V_Rec, 
                                    Attch_Note, Doc_Type, Ias_Bill_Mst_Br.Bill_Doc_Type, V_Bill_No, 
                                    V_Bill_Ser, Ias_Itm_Attach_Movement_Br.W_Code, Bill_Cost, V_Rec, 
                                    In_Out, Ias_Itm_Attach_Movement_Br.Cc_Code, Ias_Itm_Attach_Movement_Br.pj_no,
                                    Ias_Itm_Attach_Movement_Br.actv_no,Ias_Bill_Mst_Br.Rep_Code, 
                                    Ias_Itm_Attach_Movement_Br.R_Code, Ias_Bill_Mst_Br.C_Code, 
                                    Expire_Date, Batch_No, Sum(nvl(I_Qty,0)),  Sum(nvl(P_Qty,0)), 
                                    Sum(nvl(Free_Qty,0)), Sum(nvl(Pf_Qty,0)), RowNum, 2,Doc_Date, A_Cy, 
                                    V_BillRate, V_StkRate, I.I_Price, V_DiscAmt, V_StkCost, V_StkCost, 
                                    Ias_Itm_Attach_Movement_Br.Vat_Amt, V_Code, Rt_Type, 
                                    Ias_Bill_Mst_Br.Ad_U_Id, Ias_Bill_Mst_Br.Ad_Date, 
                                    Ias_Bill_Mst_Br.Up_U_Id, Ias_Bill_Mst_Br.Up_Date, 
                                    Ias_Bill_Mst_Br.Cmp_No,Ias_Bill_Mst_Br.Brn_No,Ias_Bill_Mst_Br.Brn_Year,
                                    Ias_Bill_Mst_Br.Brn_Usr, 
                                    Ias_Itm_Attach_Movement_Br.Othr_Amt
                               From Ias_Bill_Mst_Br,Ias_Itm_Attach_Movement_Br
                                   Where Ias_Bill_Mst_Br.Bill_Ser           = Ias_Itm_Attach_Movement_Br.Doc_Ser
                                    and  Ias_Itm_Attach_Movement_Br.Doc_Type=1
                                    and  Ias_Itm_Attach_Movement_Br.i_code  =i.i_code 
                                    and  Ias_Bill_Mst_Br.bill_doc_type      <> 4
                                    And Exists (Select 1 From Ias_Bill_Mst_Br_Tmp Where Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser  And RowNum <=1  )
                                    and  Ias_Bill_Mst_Br.bill_post          = 0
                                    and  Ias_Bill_Mst_Br.Bill_Date          = j.Bill_Date
                                    and  Ias_Bill_Mst_Br.bill_currency         = j.bill_currency
                                    and  Ias_Bill_Mst_Br.a_code             = j.a_code
                                    and  nvl(Ias_Bill_Mst_Br.Cash_no,0)     = nvl(J.Cash_no,0)
                                    and  nvl(Ias_Bill_Mst_Br.Si_Type,0)     = nvl(J.Si_Type,0)
                                    and  Ias_Bill_Mst_Br.Bill_Doc_type      = J.Bill_Doc_type
                                    and  Nvl(Ias_Bill_Mst_Br.w_code,0)      = Nvl(J.w_code,0)
                                    and  Nvl(Ias_Bill_Mst_Br.Cc_Code,'0')   = Nvl(J.Cc_Code,'0')
                                    and  Nvl(Ias_Bill_Mst_Br.Pj_No,'0')     = Nvl(J.Pj_No,'0')        
                                    and  Nvl(Ias_Bill_Mst_Br.Actv_No,'0')   = Nvl(J.Actv_No,'0')
                                    and  Nvl(Ias_Bill_Mst_Br.Cr_Card_No,0)  = Nvl(J.Cr_Card_No,0)
                                    and  Nvl(Ias_Bill_Mst_Br.Cr_Card_No_Scnd,0) = Nvl(J.Cr_Card_No_Scnd,0)
                                    and  Nvl(Ias_Bill_Mst_Br.Cr_Card_No_Thrd,0) = Nvl(J.Cr_Card_No_Thrd,0)
                                    and  Nvl(Ias_Bill_Mst_Br.Note_No,'0')   = Nvl(J.Note_No,'0')
                                    and  Nvl(Ias_Bill_Mst_Br.Credit_Card,0) = Nvl(J.Credit_Card,0)
                                    and  Nvl(Ias_Bill_Mst_Br.Cheque_No,'0') = Nvl(J.Cheque_No,'0')
                                    and  Nvl(Ias_Bill_Mst_Br.Cash_Ac_Fcc,'0') = Nvl(J.Cash_Ac_Fcc,'0')                          
                                    and  Nvl(Ias_Bill_Mst_Br.Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
                                    and  Ias_Bill_Mst_Br.Ad_U_Id            = J.Ad_U_Id
                                    and  Ias_Bill_Mst_Br.Doc_Brn_No         = J.Doc_Brn_No
                                    and  Ias_Bill_Mst_Br.Brn_No             = J.Brn_No
                                    and  Ias_Bill_Mst_Br.Brn_Year           = J.Brn_Year
                                    and  Ias_Bill_Mst_Br.Cmp_No             = J.Cmp_No
                                    and  Ias_Bill_Mst_Br.Brn_Usr            = J.Brn_Usr    
                           Group by  I_Code, Itm_Unt, P_Size, 
                                     Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                     Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                     Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,
                                     Attch_Note, Doc_Type, Ias_Bill_Mst_Br.Bill_Doc_Type,
                                     Ias_Itm_Attach_Movement_Br.W_Code, Bill_Cost,In_Out, 
                                     Ias_Itm_Attach_Movement_Br.Cc_Code,
                                     Ias_Itm_Attach_Movement_Br.Pj_no,
                                     Ias_Itm_Attach_Movement_Br.actv_no,Ias_Bill_Mst_Br.Rep_Code, 
                                     Ias_Itm_Attach_Movement_Br.R_Code, Ias_Bill_Mst_Br.C_Code, Expire_Date, 
                                     Batch_No,Doc_Date, A_Cy,I.I_Price, Dis_Amt, I_Price,Ias_Itm_Attach_Movement_Br.Vat_Amt, 
                                     V_Code, Rt_Type, Ias_Bill_Mst_Br.Ad_U_Id, Ias_Bill_Mst_Br.Ad_Date, Ias_Bill_Mst_Br.Up_U_Id, Ias_Bill_Mst_Br.Up_Date, 
                                     Ias_Bill_Mst_Br.Cmp_No, Ias_Bill_Mst_Br.Brn_No, Ias_Bill_Mst_Br.Brn_Year, Ias_Bill_Mst_Br.Brn_Usr, Ias_Itm_Attach_Movement_Br.Othr_Amt,
                                     Ias_Bill_Mst_Br.Pj_No,
                                     Ias_Bill_Mst_Br.Actv_No,
                                     Ias_Bill_Mst_Br.Si_Type,
                                     Ias_Bill_Mst_Br.a_code,
                                     Ias_Bill_Mst_Br.cash_no,                               
                                     Ias_Bill_Mst_Br.Bill_Doc_type,
                                     Ias_Bill_Mst_Br.BILL_DATE,                       
                                     Ias_Bill_Mst_Br.bill_currency,                                                              
                                     Ias_Bill_Mst_Br.Brn_No,
                                     Ias_Bill_Mst_Br.Doc_Brn_No,
                                     Ias_Bill_Mst_Br.Brn_Year,                                    
                                     Ias_Bill_Mst_Br.Cmp_No,
                                     Ias_Bill_Mst_Br.Brn_Usr;
                     Exception 
                       When Others Then                                                    
                        Raise_Application_Error(-20007,'Err. When Insrt Into Ias_Bill_Dtl '||Chr(13)||SqlErrm);                                                  
                     End;                     
                 End If;                        
--##-------------------------------------------------------------------------------------##--                                  
                 If  Nvl(i.Service_Item,0) = 0  And (nvl(i.i_qty,0)>0 Or nvl(i.Free_qty,0)>0) Then
                     Begin
                          V_Cst := 0;
                          Ias_Itm_Inv_Pkg.Insrt_Sale_Cost(  P_Cst         => V_Cst ,
                                                            P_Wtavg_Type  => V_Wtavg_Type , 
                                                            P_Icode       => I.I_Code ,
                                                            P_Iqty        => I.I_Qty ,
                                                            P_Freeqty     => Nvl(I.Free_Qty,0) ,
                                                            P_Itm_Unt     => I.Itm_Unt ,
                                                            P_Psize       => I.P_Size ,
                                                            P_Cost_Type   => V_Costing_Type ,
                                                            P_Wcode       => I.W_Code ,
                                                            P_Doctype     => 1,
                                                            P_Docno       => V_Bill_No,
                                                            P_Billdoctype => I.Bill_Doc_Type ,
                                                            P_Cc_Code     => I.Cc_Code,
                                                            P_Pj_No       => I.Pj_No,
                                                            P_Actv_No     => I.Actv_No,
                                                            P_Rcrdno      => V_Rec,
                                                            P_Expdate     => To_Date(Nvl(i.Expire_Date,'01/01/1900'),'DD/MM/YYYY'), 
                                                            P_Batchno     => Nvl(I.Batch_No,'0') ,
                                                            P_Docser      => V_Bill_Ser,
                                                            P_Docseq      => V_Seq,
                                                            P_Idate       => J.Bill_Date,
                                                            P_Vatamt      => Nvl(I.Vat_Amt,0),
                                                            P_Disamt      => I.Dis_Amt,
                                                            P_Acy         => J.Bill_Currency ,
                                                            P_Ac_Rate     => V_Billrate ,
                                                            P_Stk_Rate    => V_Stkrate,
                                                            P_C_Code      => Null ,
                                                            P_Adesc       => 'Post From Light System' ,
                                                            P_Refno       => Null,
                                                            P_Outno       => V_Out_No,
                                                            P_Outgrser       => V_Out_Ser,
                                                            P_Inout       => -1,
                                                            P_Iprice      => Nvl(I.I_Price,0),
                                                            P_Ad_Date     => Ias_Gen_Pkg.Get_Curdate,                                                                                     
                                                            P_Up_Date     => Null,                                                                                    
                                                            P_Brn_No      => J.Brn_No,
                                                            P_Brn_Year    => J.Brn_Year,
                                                            P_Cmp_No      => J.Cmp_No        ,
                                                            P_Brn_Usr     => J.Brn_Usr        );
                     Exception When Others Then
                        Raise_Application_Error(-20008,'Err. When Insrt Into Sale Cost '||Chr(13)||SqlErrm);
                        RollBack;
                     END;    
                 End If;        
        -----------------------------------------------------------------------------------------
             End Loop; --(2)
         End; --(12)     
--##-------------------------------------------------------------------------------------##--
         If Nvl(V_Use_Out_Bills,0)=1 Then
            Begin
                  Ias_Insrt_Out_Bills_Pkg.Insrt_Out_Bills ( P_Invs        => V_Invoicing_Serials   , 
                                                          P_Doc_Ser     => V_Bill_Ser                  ,
                                                          P_Out_No      => V_Out_No              ,
                                                          P_Out_Ser     => V_Out_Ser             ,
                                                          P_Extrnl_Post => 2                     ,    
                                                          P_Lang_No     => 1                     ,
                                                          P_Brn_No      => J.Brn_No              );
            Exception 
              When Others Then                                                    
               Raise_Application_Error(-20009,'Err. When Insrt Into Out_Bills'||Chr(13)||SqlErrm);                                              
            End;                    
         End If; 
 --##------------------------------------------------------------------------------------##--
       If V_Use_Vat=1 Then        
             Begin
                                        Insert Into Gnr_Tax_Itm_Movmnt (Doc_No, 
                                                                        Doc_Ser, 
                                                                        Doc_Date,
                                                                        Doc_Type,
                                                                        Bill_Doc_Type,
                                                                        Doc_Jv_Type,                          
                                                                        Tax_No,
                                                                        Clc_Typ_No,
                                                                        Agncy_No,
                                                                        I_Code, 
                                                                        Itm_Unt,
                                                                        P_Size,                                   
                                                                        A_Code, 
                                                                        A_Cy, 
                                                                        Ac_Rate, 
                                                                        Stk_Rate,
                                                                        I_Price,
                                                                        Disc_Amt, 
                                                                        Tax_Prcnt, 
                                                                        Tax_Amt,
                                                                        Tax_Amt_L, 
                                                                        I_Qty, 
                                                                        Free_Qty, 
                                                                        Stk_Cost,
                                                                        W_Code, 
                                                                        Cc_Code,
                                                                        Pj_No, 
                                                                        Actv_No, 
                                                                        Rcrd_No, 
                                                                        Doc_Sequence, 
                                                                        External_Post, 
                                                                        Ref_No,
                                                                        Cmp_No, Brn_No,Brn_Year, Brn_Usr)
                                                               Select    D.Bill_No, 
                                                                          D.Bill_Ser, 
                                                                          Bm.Bill_Date,
                                                                          M.Doc_Type, 
                                                                          M.Bill_Doc_Type,
                                                                          M.Doc_Jv_Type,                           
                                                                          M.Tax_No, 
                                                                          M.Clc_Typ_No, 
                                                                          M.Agncy_No, 
                                                                          M.I_Code, 
                                                                          M.Itm_Unt, 
                                                                          M.P_Size,                              
                                                                          M.A_Code, 
                                                                          M.A_Cy, 
                                                                          Bm.Bill_Rate,
                                                                          Bm.Stock_Rate,
                                                                          Nvl(D.I_Price,0) I_Price,
                                                                          Nvl(D.Dis_Amt,0) Disc_Amt, 
                                                                          M.Tax_Prcnt Tax_Prcnt, 
                                                                          --nvl(Nvl(M.Tax_Amt,0) Tax_Amt, 
                                                                          --Nvl(M.Tax_Amt_L,0) Tax_Amt_L,
                                                                          (Decode(V_CALC_VAT_AMT_TYPE,1,( Nvl(D.I_Price,0)*m.Tax_Prcnt)/100,((Nvl(D.I_Price,0)-Nvl(D.Dis_Amt,0))*m.Tax_Prcnt)/100)) Tax_Amt,
                                                                          (Decode(V_CALC_VAT_AMT_TYPE,1,( Nvl(D.I_Price,0)*m.Tax_Prcnt)/100,((Nvl(D.I_Price,0)-Nvl(D.Dis_Amt,0))*m.Tax_Prcnt)/100)*Nvl(m.Ac_Rate,1)) Tax_Amt_L,
                                                                          Sum(Nvl(M.I_Qty,0)) I_Qty,
                                                                          Sum(Nvl(M.Free_Qty,0)) Free_Qty,
                                                                          Nvl(D.Stk_Cost,0) Stk_Cost,
                                                                          M.W_Code, 
                                                                          M.Cc_Code,
                                                                          M.Pj_No, 
                                                                          M.Actv_No,
                                                                          D.Rcrd_No, 
                                                                          D.Doc_Sequence,
                                                                          M.External_Post, 
                                                                          DECODE(M.External_Post,85,'LGHT',70,'DTS',NULL),
                                                                          M.Cmp_No,
                                                                          M.Brn_No,
                                                                          M.Brn_Year, 
                                                                          M.Brn_Usr    
                                                                   From Ias_Bill_Mst_Br Bm,Ias_Bill_Dtl d,Gnr_Tax_Itm_Movmnt_Br M
                                                                           Where Bm.Bill_Ser           = M.Doc_Ser
                                                                            and  M.I_Code              = D.I_Code
                                                            and  M.Itm_Unt             = D.Itm_Unt
                                                            and  M.W_Code              = D.W_Code
                                                            And  D.Bill_Ser            = V_Bill_Ser
                                                                            and  M.Doc_Type            = 4
                                                                            and  Bm.bill_doc_type      <> 4
                                                                            --And Nvl(Bm.W_Code,0) Between Nvl(V_F_Wcode,Nvl(Bm.W_Code,0)) And Nvl(V_T_Wcode,Nvl(Bm.W_Code,0))
                                                                            and  Bm.bill_post          = 0
                                                                        and  Bm.Bill_Date          = j.Bill_Date
                                                                        and  Bm.bill_currency        = j.bill_currency
                                                                        and  Bm.a_code             = j.a_code
                                                                        and  nvl(Bm.Cash_no,0)     = nvl(J.Cash_no,0)
                                                                        and  nvl(Bm.Si_Type,0)     = nvl(J.Si_Type,0)
                                                                        and  Bm.Bill_Doc_type      = J.Bill_Doc_type
                                                                        and  Nvl(Bm.w_code,0)      = Nvl(J.w_code,0)
                                                                        and  Nvl(Bm.Cc_Code,'0')   = Nvl(J.Cc_Code,'0')
                                                                        and  Nvl(Bm.Pj_No,'0')     = Nvl(J.Pj_No,'0')        
                                                                        and  Nvl(Bm.Actv_No,'0')   = Nvl(J.Actv_No,'0')
                                                                        and  Nvl(Bm.Rep_Code,'0')  = Nvl(J.Rep_Code,'0')              
                                                                        and  Nvl(Bm.Cr_Card_No,0)  = Nvl(J.Cr_Card_No,0)
                                                                        and  Nvl(Bm.Cr_Card_No_Scnd,0) = Nvl(J.Cr_Card_No_Scnd,0)
                                                                        and  Nvl(Bm.Cr_Card_No_Thrd,0) = Nvl(J.Cr_Card_No_Thrd,0)
                                                                        and  Nvl(Bm.Note_No,'0')   = Nvl(J.Note_No,'0')
                                                                        and  Nvl(Bm.Credit_Card,0) = Nvl(J.Credit_Card,0)
                                                                        and  Nvl(Bm.Cheque_No,'0') = Nvl(J.Cheque_No,'0')
                                                                        and  Nvl(Bm.Cash_Ac_Fcc,'0') = Nvl(J.Cash_Ac_Fcc,'0')                          
                                                                        and  Nvl(Bm.Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
                                                                        and  Bm.Ad_U_Id            = J.Ad_U_Id
                                                                        and  Bm.Doc_Brn_No         = Nvl(J.Doc_Brn_No,0)
                                                                        and  Bm.Clc_Typ_No_Tax     = Nvl(J.Clc_Typ_No_Tax,0)
                                                                        and  Bm.Clc_Vat_Price_Typ  = Nvl(J.Clc_Vat_Price_Typ,0)
                                                                        and  Nvl(D.I_Price,0)      = Nvl(M.I_Price,0)
                                                                        and  Nvl(D.Dis_Amt,0)      = Nvl(M.Disc_Amt,0)
                                                                        And  Nvl(D.Vat_Amt,0)      >0
                                                                        and  Bm.Brn_No             = J.Brn_No
                                                                        and  Bm.Brn_Year           = J.Brn_Year
                                                                        and  Bm.Cmp_No             = J.Cmp_No
                                                                        and  Bm.Brn_Usr               = J.Brn_Usr 
                                                       Group By D.Bill_No, 
                                                                      D.Bill_Ser, 
                                                                      Bm.Bill_Date,
                                                                      M.Doc_Type, 
                                                                      M.Bill_Doc_Type,
                                                                      M.Doc_Jv_Type,                           
                                                                      M.Tax_No, 
                                                                      M.Clc_Typ_No, 
                                                                      M.Agncy_No, 
                                                                      M.I_Code, 
                                                                      M.Itm_Unt, 
                                                                      M.P_Size,                              
                                                                      M.A_Code, 
                                                                      M.A_Cy, 
                                                                      Bm.Bill_Rate,
                                                                      Bm.Stock_Rate,
                                                                      Nvl(D.I_Price,0),
                                                                      Nvl(D.Dis_Amt,0), 
                                                                      M.Tax_Prcnt, 
                                                                      Nvl(D.Stk_Cost,0),
                                                                      m.Ac_Rate,
                                                                      M.W_Code, 
                                                                      M.Cc_Code,
                                                                      M.Pj_No, 
                                                                      M.Actv_No,
                                                                      D.Rcrd_No, 
                                                                      D.Doc_Sequence,
                                                                      M.Cmp_No,
                                                                      M.Brn_No,
                                                                      M.Brn_Year, 
                                                                      M.Brn_Usr    ;
                                                                          
                                                                          
                 Exception When Others Then                                                    
                   ROLLBACK;
                    Raise_Application_Error(-20003,'ERROR WHEN INSERT Gnr_Tax_Itm_Movmnt '||Chr(13)||SqlErrm);                                                  
                End;
             End If;                   
--##-------------------------------------------------------------------------------------##-- 
      Begin
        Insert Into Ias_Point_Calc_Trns(Trns_Date, Cust_Code, Mobile_No, Point_Typ_No, Bill_No, Rt_Bill_No, Doc_Amt, A_Cy, Point_Cnt, Trns_Type, Machine_No, 
                                          Expire_Date, Bill_Amt, External_Post, Doc_No, Doc_Srl, Doc_Typ, Ac_Rate, Point_Amt,Ad_U_Id, Ad_Date, Up_U_Id, 
                                          Up_Date, Up_Cnt, Cmp_No, Brn_No, Brn_Year, Brn_Usr)
                                   Select T.Trns_Date, T.Cust_Code, T.Mobile_No, T.Point_Typ_No, V_BILL_NO, Null, T.Doc_Amt, T.A_Cy, T.Point_Cnt, T.Trns_Type,
                                          T.Machine_No, T.Expire_Date, T.Bill_Amt, T.External_Post, V_BILL_NO, V_BILL_SER, T.Doc_Typ, T.Ac_Rate, T.Point_Amt,T.Ad_U_Id, 
                                          T.Ad_Date, T.Up_U_Id, T.Up_Date, T.Up_Cnt, T.Cmp_No, T.Brn_No, T.Brn_Year, T.Brn_Usr
                                     From Ias_Bill_Mst_Br Bm, Ias_Point_Calc_Trns_Br T
                                    Where Bm.Bill_Ser            = T.Doc_Srl
                                      And T.Doc_Typ              = 4 
                                      And T.Trns_Type           In (1,2)
                                      And  Bm.Bill_Ser           = V_BILL_SER
                                      And  Bm.Bill_Doc_Type      <> 4
                                    --  And Nvl(Bm.W_Code,0) Between Nvl(V_F_Wcode,Nvl(Bm.W_Code,0)) And Nvl(V_T_Wcode,Nvl(Bm.W_Code,0))
                                      And  Bm.Bill_Post          = 0
                                      And  Bm.Bill_Date          = J.Bill_Date
                                      And  Bm.Bill_Currency        = J.Bill_Currency
                                      And  Bm.A_Code             = J.A_Code
                                      And  Nvl(Bm.Cash_No,0)     = Nvl(J.Cash_No,0)
                                      And  Nvl(Bm.Si_Type,0)     = Nvl(J.Si_Type,0)
                                      And  Bm.Bill_Doc_Type      = J.Bill_Doc_Type
                                      And  Nvl(Bm.W_Code,0)      = Nvl(J.W_Code,0)
                                      And  Nvl(Bm.Cc_Code,'0')   = Nvl(J.Cc_Code,'0')
                                      And  Nvl(Bm.Pj_No,'0')     = Nvl(J.Pj_No,'0')        
                                      And  Nvl(Bm.Actv_No,'0')   = Nvl(J.Actv_No,'0')
                                      And  Nvl(Bm.Rep_Code,'0')  = Nvl(J.Rep_Code,'0')              
                                      And  Nvl(Bm.Cr_Card_No,0)  = Nvl(J.Cr_Card_No,0)
                                      And  Nvl(Bm.Cr_Card_No_Scnd,0) = Nvl(J.Cr_Card_No_Scnd,0)
                                      And  Nvl(Bm.Cr_Card_No_Thrd,0) = Nvl(J.Cr_Card_No_Thrd,0)
                                      And  Nvl(Bm.Note_No,'0')   = Nvl(J.Note_No,'0')
                                      And  Nvl(Bm.Credit_Card,0) = Nvl(J.Credit_Card,0)
                                      And  Nvl(Bm.Cheque_No,'0') = Nvl(J.Cheque_No,'0')
                                      And  Nvl(Bm.Cash_Ac_Fcc,'0') = Nvl(J.Cash_Ac_Fcc,'0')                          
                                      And  Nvl(Bm.Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
                                      And  Bm.Ad_U_Id            = J.Ad_U_Id
                                      And  Bm.Doc_Brn_No         = Nvl(J.Doc_Brn_No,0)
                                      And  Bm.Clc_Typ_No_Tax     = Nvl(J.Clc_Typ_No_Tax,0)
                                      and  Bm.Clc_Vat_Price_Typ  = Nvl(J.Clc_Vat_Price_Typ,0)
                                      And  Bm.Brn_No             = J.Brn_No
                                      And  Bm.Brn_Year           = J.Brn_Year
                                      And  Bm.Cmp_No             = J.Cmp_No
                                      And  Bm.Brn_Usr            = J.Brn_Usr; 
                                                                  
      Exception When Others Then                                                    
             ROLLBACK;
              Raise_Application_Error(-20003,'ERROR WHEN INSERT INTO Ias_Point_Calc_Trns'||Chr(13)||SqlErrm);                                                  
      End;   
--##-------------------------------------------------------------------------------------##--
    Begin
          Ars_Gnr_Pkg.Insrt_Crdt_Crd_From_Br ( P_Doc_Type        =>4
                                                  ,P_Doc_No          =>V_Bill_No
                                                  ,P_Bill_Doc_Type   =>J.Bill_Doc_Type
                                                  ,P_Doc_Ser         =>V_Bill_Ser
                                                  ,P_Doc_Date        =>J.Bill_Date
                                                  ,P_User_Id         =>J.Ad_U_id
                                                  ,P_A_Cy            =>j.Bill_Currency
                                                  ,P_Cash_No         =>J.Cash_No
                                                  ,P_C_Code          =>null
                                                  ,P_External_Post   =>85
                                                  ,Typ               =>'S');                                                 
    Exception When Others Then                                                    
       RollBack;
       Raise_Application_Error(-20015,'Ars_Gnr_Pkg.Insrt_Crdt_Crd_From_Br  = '||Chr(13)||'Bill_Ser ='||V_Bill_Ser ||Chr(13)||SqlErrm);                                               
    End; 
  --##-------------------------------------------------------------------------------------##--   
--##-------------------------------------------------------------------------------------##--     
         Begin
                Ias_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 4                 ,
                                                      G_Doc_Ser     => V_Bill_Ser        ,
                                                      P_Jv_Type      => J.Bill_Doc_Type   ,
                                                      P_Doc_No      => V_Bill_No         ,
                                                      P_Lang_No     => 1                 ,
                                                      P_User_No     => J.Ad_U_Id         ,
                                                      G_Post_Type   => 0                 );
         Exception 
           When No_Data_Found Then 
                Null;
           When Others Then
                Raise_Application_Error(-20010,'Error When Updating Post In Bills  = '||Chr(13)||'Tr_Ser ='||V_Bill_Ser ||Chr(13)||SqlErrm);                                                    
         End;  
                                                                      
--##-------------------------------------------------------------------------------------##--
      If V_Use_Out_Bills=1 Then
            BEGIN
              Ias_Post_In_Sav_Pkg.Post_Doc_In_Sav (  G_Doc_Type    => 13                 ,
                                                      G_Doc_Ser     => V_Out_Ser        ,
                                                      P_Jv_Type     => J.Bill_Doc_Type   ,
                                                      P_Doc_No      => V_Out_No         ,
                                                      P_Lang_No     => 1                 ,
                                                      P_User_No     => J.Ad_U_Id         ,
                                                      G_Post_Type   => 0                 );
           Exception 
               When No_Data_Found Then 
                    Null;
               When Others Then
                    Raise_Application_Error(-20010,'Error When Updating Post In OUT_Bills  = '||Chr(13)||'BILL_SER ='||V_Bill_Ser ||Chr(13)||SqlErrm);
           END;                               
       End If;    
--##------------------------------------------------------------------------------------##--
    End Loop; --(1)
--##-------------------------------------------------------------------------------------##--
    --## Update Ias_Bill_Mst_Br        
    Begin
     Update  Ias_Bill_Mst_Br
      Set    Bill_Post           =  1  
       Where Bill_Doc_Type      <>4
          And Nvl(Bill_Post,0)  = 0
          And Nvl(Stand_By,0)   = 0    
          And Exists (Select 1 From Ias_Bill_Dtl_Br Where Bill_Ser=Ias_Bill_Mst_Br.Bill_Ser And Rownum<=1)
          And Exists (Select 1 From Ias_Bill_Mst_Br_Tmp Where Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser  And RowNum <=1  ) ;
       Commit ;
    Exception
      When Others Then
         Raise_Application_Error(-20011,'Error When Updating Bill Post  = '||Chr(13)||'Bill_Ser ='||V_Bill_Ser ||Chr(13)||Sqlerrm);
         RollBack  ;                
     End ;
--##-------------------------------------------------------------------------------------##--
  END;
--##-------------------------------------------------------------------------------------##--    
   End Post_Sales_Sum ;
--##-------------------------------------------------------------------------------------##--
PROCEDURE Post_Sales_Detail ( P_Doc_Ser  In Ias_Bill_Mst.Bill_Ser%Type   Default Null , P_Use_Adjstmnt In Number Default 0 , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null)  Is     
     V_Cnt                    Number;
     V_Sqlstr                 Varchar2(3000);
     V_sqlstr2                Varchar2(3000);
     V_Out_no                 Number;      
     V_Out_ser                Number;      
     V_StkCost                Number;
     V_Seq                    Number;
     V_StkRate                Number;
     V_Cst                    Number;
     V_Use_Itm_Attach         Ias_Para_Inv.Use_Itm_Attach%Type ;
     V_Costing_Type           Ias_Para_Inv.Costing_Type%Type   ;
     V_Wtavg_Type             Ias_Para_Inv.Wtavg_Type%Type     ;
     V_Invoicing_Serials      Ias_Para_Ar.Invoicing_Serials%Type  ;
     V_Use_Out_Bills          Ias_Para_Ar.Use_Out_Bills %Type     ;     
     V_Allow_Enter_Zero_Cost  Number;
     v_Use_SerialNo           Number;
     V_Itm_Use_SerialNo       Number:=0;
     V_Service_Item           Number:=0;   
     V_Lang_No                Number:=P_Lang_No;
     V_TAX_BILL_TYP           NUMBER(5);
Begin
--##-------------------------------------------------------------------------------------##--
  If P_Lang_No Is Null Then    
    Begin
      Select Lang_No InTo V_Lang_No From Ias_Sys.Lang_Def Where Nvl(Flg_St,1)= 1 And Lang_Dflt=1 And Rownum<=1;
    Exception WHen Others Then
        V_Lang_No := 1;
    End;  
  ENd If;  
  --##-------------------------------------------------------------------------------------##--
   --# To Insert Into  Ias_pos_minus_qty Temporary Table 
   --------------------------------------------------------------##--
  Begin
      Select Nvl(Costing_Type,0)   ,
                 Nvl(Wtavg_Type,0)     ,
                 Nvl(Invoicing_Serials,0) ,
                 Nvl(Use_Out_Bills ,0) ,
                 Nvl(Use_Itm_Attach ,0)  ,
                 Nvl(Use_SerialNo,0)  
            Into V_Costing_Type              ,
                 V_Wtavg_Type                ,
                 V_Invoicing_Serials         ,
                 V_Use_Out_Bills             ,
                 V_Use_Itm_Attach   , 
                 v_Use_SerialNo       
           From Ias_Para_Inv ,Ias_Para_Ar ;
  Exception WHen Others Then
    RollBack;
    Raise_Application_Error(-20001,'Error When Select From Para In Post_Sales_Detail '||Chr(13)||SqlErrm);
  End;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      If P_User_No<>1 Then
        Select Allow_Enter_Zero_Cost InTo V_Allow_Enter_Zero_Cost From Privilege_Fixed Where U_Id=P_User_No And RowNum<=1;
      End If;          
  Exception WHen Others Then
      RollBack;
      Raise_Application_Error(-20002,'Error When Select From Privilege_Fixed In Post_Sales_Detail'||Chr(13)||SqlErrm);
  End;
--##------------------------------------------------------------------------------------##--
  Begin
    Delete from Ias_Bill_Mst_Br_Tmp;
  Exception WHen Others Then
    Null;
  End; 
   
  Insert Into Ias_Bill_Mst_Br_Tmp (Bill_No,Bill_Ser) Select Bill_No , Bill_Ser 
                                                       From Ias_Bill_Mst_Br 
                                                      Where Bill_Ser=Nvl(P_Doc_Ser,Bill_Ser) 
                                                        And Nvl(Stand_By,0)=0 
                                                        And Nvl(Bill_Post,0)=0
                                                        And Exists(Select 1 From Ias_Bill_Dtl_Br Where Bill_Ser=Ias_Bill_Mst_Br.Bill_Ser And Rownum<=1)
                                                        And Not Exists(Select 1 From Ias_Bill_Mst Where Bill_Ser=Ias_Bill_Mst_Br.Bill_Ser And Rownum<=1);
  --##-------------------------------------------------------------------------------------##--
  Check_Avl_Qty ( P_Doc_Type => 1);
  --##-------------------------------------------------------------------------------------##--
  Begin
      Select 1 Into V_Cnt From Ias_Pos_Minus_Qty_Tmp Where RowNum <=1 ;
   Exception
       When Others Then
         V_cnt := 0 ;
     End ; 
   If Nvl(V_Cnt,0)>0 Then ---(2)
      If Nvl(P_Use_Adjstmnt,0)=1 Then
        Post_Stk_Adjstmnt ;
      Else
        Begin
            Delete Ias_Bill_Mst_Br_Tmp M Where Exists ( Select 1 From Ias_Bill_Dtl_Br A,Ias_Pos_Minus_Qty_Tmp B
                                                        Where A.Bill_Ser    = M.Bill_Ser 
                                                          And A.I_Code      = B.I_Code
                                                          And A.W_Code      = B.W_Code
                                                          And To_Date(A.Expire_Date,'DD/MM/YYYY') = To_Date(B.Expire_Date,'DD/MM/YYYY')
                                                          And A.Batch_No    = B.Batch_No                           
                                                          And Rownum<=1);   
       Exception When Others Then Null;
       End;                                                    
      End If;                
   End If; ---(2)
--##-------------------------------------------------------------------------------------##--
   Declare
     Cursor Sm Is  Select Bill_Doc_Type
                         ,Bill_No
                         ,Bill_Ser
                         ,Bill_Date
                         ,Bill_Currency
                         ,Bill_Rate
                         ,Stock_Rate
                         ,C_Code
                         ,C_Name
                         ,Decode (Bill_Doc_Type,  4, A_Code,  1, Ias_Cshbnk_Pkg.Get_A_Code (1, Cash_No),  A_Code) As "A_CODE"
                         ,Cheque_No
                         ,Note_No
                         ,Cheque_Due_Date
                         ,Bill_Due_Date
                         ,W_Code
                         ,R_Code
                         ,Rep_Code
                         ,Emp_No
                         ,Ref_No
                         ,Cash_No
                         ,Cc_Code
                         ,Pj_No
                         ,Actv_No
                         ,Si_Type
                         ,Stand_By
                         ,Col_No
                         ,Cash_Ac_Fcc
                         ,Cash_No_Fcc
                         ,A_Desc
                         ,Bill_Py
                         ,External_Post
                         ,Field1
                         ,Field2
                         ,Field3
                         ,Field4
                         ,Field5
                         ,Field6
                         ,Field7
                         ,Field8
                         ,Field9
                         ,Field10
                         ,C_Tel
                         ,C_Address
                         ,Driver_No
                         ,Bill_Valued
                         ,Value_Date
                         ,Bill_Without_Auto_Othr_Amt
                         ,Qt_Prm_No
                         ,Qt_Prm_Ser
                         ,Qt_Prm_Rcrd_No
                         ,Prm_Code
                         ,Doc_Brn_No
                         ,Cmpny_No
                         ,Mobile_No
                         ,Not_Use_Qut_Prm
                         ,Receive_Nm
                         ,Conn_Si_With_Outgong
                         ,C_Code_Csh
                         ,C_Tax_Code
                         ,Doc_No_Res
                         ,Doc_Srl_Res
                         ,Ac_Code
                         ,Ac_Code_Dtl
                         ,Ac_Dtl_Typ
                         ,Pymnt_Ac
                         ,Clc_Typ_No_Tax
                         ,Doc_Ser_Extrnl
                         ,Cncl_Flg
                         ,Clc_Vat_Price_Typ
                         ,Bill_Amt
                         ,Vat_Amt
                         ,Disc_Amt_Aftr_Vat
                         ,Disc_Amt_Mst_Vat
                         ,Vat_Amt_Disc_Mst
                         ,Vat_Amt_Othr
                         ,Othr_Amt
                         ,Disc_Amt
                         ,Disc_Amt_Mst
                         ,Disc_Amt_Dtl
                         ,Add_Disc_Amt_Mst
                         ,Add_Disc_Amt_Dtl
                         ,Othr_Amt_Disc
                         ,Out_Bill_Typ
                         ,Bill_Stat_Typ
                         ,Crd_Disc_Per
                         ,Crd_No_Disc
                         ,Credit_Card
                         ,Cr_Card_Amt
                         ,Cr_Card_Amt_Scnd
                         ,Cr_Card_Amt_Thrd
                         ,Cr_Card_Comm_Per
                         ,Cr_Card_Comm_Per_Scnd
                         ,Cr_Card_Comm_Per_Thrd
                         ,Cr_Card_Cst_No
                         ,Cr_Card_Cst_No_Scnd
                         ,Cr_Card_Cst_No_Thrd
                         ,Cr_Card_Doc_No_Ref
                         ,Cr_Card_Doc_No_Ref_Scnd
                         ,Cr_Card_Doc_No_Ref_Thrd
                         ,Cr_Card_Dsc
                         ,Cr_Card_Dsc_Scnd
                         ,Cr_Card_Dsc_Thrd
                         ,Cr_Card_Max_Comm_Amt
                         ,Cr_Card_Max_Comm_Amt_Scnd
                         ,Cr_Card_Max_Comm_Amt_Thrd
                         ,Cr_Card_No
                         ,Cr_Card_No_Scnd
                         ,Cr_Card_No_Thrd
                         ,Cr_Doc_No_Ref
                         ,Cr_Doc_No_Ref_Scnd
                         ,Cr_Doc_No_Ref_Thrd
                         ,Cr_Valued
                         ,Cr_Valued_Scnd
                         ,Cr_Valued_Thrd
                         ,Cr_Value_Date
                         ,Cr_Value_Date_Scnd
                         ,Cr_Value_Date_Thrd
                         ,Cpn_Amt
                         ,Cheque_Amt
                         ,Prcnt_Amt
                         ,Ac_Amt
                         ,Clc_Tax_Free_Qty_Flg
                         ,Cmp_No
                         ,Brn_No
                         ,Brn_Year
                         ,Brn_Usr
                         ,Ad_U_Id
                         ,Ad_Date
                         ,Ad_Trmnl_Nm 
                         ,Audit_Ref
                         ,Audit_Ref_Date
                         ,Audit_Ref_Desc
                         ,Audit_Ref_U_Id
                         ,Bill_No_Conn                       
                         ,Bill_Ser_Conn
                         ,Clc_Insrnce_Load_Amt_Mthd
                         ,Clc_Tax_Insrnc_Cmpny_Flg
                         ,Comm_Amt_Dtl
                         ,Comm_Per
                         ,Export
                         ,Insrnce_Add_Lmt_Doc
                         ,Insrnce_Add_Lmt_Dtl
                         ,Insrnce_Add_Lmt_Mst
                         ,Insrnce_Apprvd_Code
                         ,Insrnce_Bnf_No
                         ,Insrnce_Card_No
                         ,Insrnce_Card_No_Fmly
                         ,Insrnce_Clss_No
                         ,Insrnce_Cmp_No
                         ,Insrnce_Csh_Amt
                         ,Insrnce_Diagnosis
                         ,Insrnce_Load_Per
                         ,Insrnce_Mdcl_No
                         ,Insrnce_Prson_Nm
                         ,Insrnce_Rltn_Typ
                         ,Load_No
                         ,Load_Ser
                         ,Point_Calc_Typ_No
                         ,Point_Cnt
                         ,Point_Cnt_All
                         ,Point_Rplc_Amt
                         ,Point_Rplc_Cnt
                         ,Point_Typ_No
                         ,Processed
                         ,Pr_Rep
                         ,Up_Date
                         ,Up_U_Id
                         ,E_Invc_Mthd_No
                         ,TAX_BILL_TYP
                       From Ias_Bill_Mst_Br
                      Where Nvl(Bill_Post,0)=0         
                        And Nvl(Stand_By,0)=0     
                        And Exists (Select 1 From Ias_Bill_Mst_Br_Tmp Where Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser  And RowNum <=1  )
                        Order By  Ad_Date;
    Begin ---(11)
--##-------------------------------------------------------------------------------------##--
    --## To Get Stock Rate           
     V_StkRate := Ias_Gen_Pkg.Get_Cur_rate(p_acy=> Ias_Gen_Pkg.Get_Stk_Cur);      
--##-------------------------------------------------------------------------------------##--
     
--##-------------------------------------------------------------------------------------##--
     For j in SM Loop     -->> (1)    
         Begin
             --Check_Duplicate_SI(J.Bill_No,J.Bill_Doc_Type,J.Bill_Ser);
             ----------------------------------------------------
             V_TAX_BILL_TYP:=NULL;     
               Begin
                     select  DECODE( NVL(C_CLASS_VAT,1),2,2,3,2,1) into V_TAX_BILL_TYP from customer where c_code=j.c_code and rownum<=1;
               Exception when others then             
                    V_TAX_BILL_TYP:=1;
               end; 
               
               if J.C_Tax_Code is Not null Then
                 V_TAX_BILL_TYP:=2;
               end if;
               
       -----------------------------------------------
             Insert Into Ias_Bill_Mst(  Bill_Doc_Type
                                         ,Bill_No
                                         ,Bill_Ser
                                         ,Bill_Date
                                         ,Bill_Currency
                                         ,Bill_Rate
                                         ,Stock_Rate
                                         ,C_Code
                                         ,C_Name
                                         ,A_Code
                                         ,Cheque_No
                                         ,Note_No
                                         ,Cheque_Due_Date
                                         ,Bill_Due_Date
                                         ,W_Code
                                         ,R_Code
                                         ,Rep_Code
                                         ,Emp_No
                                         ,Ref_No
                                         ,Cash_No
                                         ,Cc_Code
                                         ,Pj_No
                                         ,Actv_No
                                         ,Si_Type
                                         ,Stand_By
                                         ,Col_No
                                         ,Cash_Ac_Fcc
                                         ,Cash_No_Fcc
                                         ,A_Desc
                                         ,Bill_Py
                                         ,External_Post
                                         ,Field1
                                         ,Field2
                                         ,Field3
                                         ,Field4
                                         ,Field5
                                         ,Field6
                                         ,Field7
                                         ,Field8
                                         ,Field9
                                         ,Field10
                                         ,C_Tel
                                         ,C_Address
                                         ,Driver_No
                                         ,Bill_Valued
                                         ,Value_Date
                                         ,Bill_Without_Auto_Othr_Amt
                                         ,Qt_Prm_No
                                         ,Qt_Prm_Ser
                                         ,Qt_Prm_Rcrd_No
                                         ,Prm_Code
                                         ,Doc_Brn_No
                                         ,Cmpny_No
                                         ,Mobile_No
                                         ,Not_Use_Qut_Prm
                                         ,Receive_Nm
                                         ,Conn_Si_With_Outgong
                                         ,C_Code_Csh
                                         ,C_Tax_Code
                                         ,Doc_No_Res
                                         ,Doc_Srl_Res
                                         ,Ac_Code
                                         ,Ac_Code_Dtl
                                         ,Ac_Dtl_Typ
                                         ,Pymnt_Ac
                                         ,Clc_Typ_No_Tax
                                         ,Doc_Ser_Extrnl
                                         ,Cncl_Flg
                                         ,Clc_Vat_Price_Typ
                                         ,Bill_Amt
                                         ,Vat_Amt
                                         ,Disc_Amt_Aftr_Vat
                                         ,Disc_Amt_Mst_Vat
                                         ,Vat_Amt_Disc_Mst
                                         ,Vat_Amt_Othr
                                         ,Othr_Amt
                                         ,Disc_Amt
                                         ,Disc_Amt_Mst
                                         ,Disc_Amt_Dtl
                                         ,Add_Disc_Amt_Mst
                                         ,Add_Disc_Amt_Dtl
                                         ,Othr_Amt_Disc
                                         ,Out_Bill_Typ
                                         ,Bill_Stat_Typ
                                         ,Crd_Disc_Per
                                         ,Crd_No_Disc
                                         ,Credit_Card
                                         ,Cr_Card_Amt
                                         ,Cr_Card_Amt_Scnd
                                         ,Cr_Card_Amt_Thrd
                                         ,Cr_Card_Comm_Per
                                         ,Cr_Card_Comm_Per_Scnd
                                         ,Cr_Card_Comm_Per_Thrd
                                         ,Cr_Card_Cst_No
                                         ,Cr_Card_Cst_No_Scnd
                                         ,Cr_Card_Cst_No_Thrd
                                         ,Cr_Card_Doc_No_Ref
                                         ,Cr_Card_Doc_No_Ref_Scnd
                                         ,Cr_Card_Doc_No_Ref_Thrd
                                         ,Cr_Card_Dsc
                                         ,Cr_Card_Dsc_Scnd
                                         ,Cr_Card_Dsc_Thrd
                                         ,Cr_Card_Max_Comm_Amt
                                         ,Cr_Card_Max_Comm_Amt_Scnd
                                         ,Cr_Card_Max_Comm_Amt_Thrd
                                         ,Cr_Card_No
                                         ,Cr_Card_No_Scnd
                                         ,Cr_Card_No_Thrd
                                         ,Cr_Doc_No_Ref
                                         ,Cr_Doc_No_Ref_Scnd
                                         ,Cr_Doc_No_Ref_Thrd
                                         ,Cr_Valued
                                         ,Cr_Valued_Scnd
                                         ,Cr_Valued_Thrd
                                         ,Cr_Value_Date
                                         ,Cr_Value_Date_Scnd
                                         ,Cr_Value_Date_Thrd
                                         ,Cpn_Amt
                                         ,Cheque_Amt
                                         ,Prcnt_Amt
                                         ,Ac_Amt
                                         ,Clc_Tax_Free_Qty_Flg
                                         ,Cmp_No
                                         ,Brn_No
                                         ,Brn_Year
                                         ,Brn_Usr
                                         ,Ad_U_Id
                                         ,Ad_Date
                                         ,Ad_Trmnl_Nm 
                                         ,Audit_Ref
                                         ,Audit_Ref_Date
                                         ,Audit_Ref_Desc
                                         ,Audit_Ref_U_Id
                                         ,Bill_No_Conn
                                         ,Bill_Post
                                         ,Bill_Ser_Conn
                                         ,Clc_Insrnce_Load_Amt_Mthd
                                         ,Clc_Tax_Insrnc_Cmpny_Flg
                                         ,Comm_Amt_Dtl
                                         ,Comm_Per
                                         ,Export
                                         ,Insrnce_Add_Lmt_Doc
                                         ,Insrnce_Add_Lmt_Dtl
                                         ,Insrnce_Add_Lmt_Mst
                                         ,Insrnce_Apprvd_Code
                                         ,Insrnce_Bnf_No
                                         ,Insrnce_Card_No
                                         ,Insrnce_Card_No_Fmly
                                         ,Insrnce_Clss_No
                                         ,Insrnce_Cmp_No
                                         ,Insrnce_Csh_Amt
                                         ,Insrnce_Diagnosis
                                         ,Insrnce_Load_Per
                                         ,Insrnce_Mdcl_No
                                         ,Insrnce_Prson_Nm
                                         ,Insrnce_Rltn_Typ
                                         ,Load_No
                                         ,Load_Ser
                                         ,Point_Calc_Typ_No
                                         ,Point_Cnt
                                         ,Point_Cnt_All
                                         ,Point_Rplc_Amt
                                         ,Point_Rplc_Cnt
                                         ,Point_Typ_No
                                         ,Processed
                                         ,Pr_Rep
                                         ,Up_Date
                                         ,Up_U_Id
                                         ,DOC_PST_SQ
                                         ,E_INVC_MTHD_NO
                                         ,TAX_BILL_TYP )
                              Values(  J.Bill_Doc_Type
                                         ,J.Bill_No
                                         ,J.Bill_Ser
                                         ,J.Bill_Date
                                         ,J.Bill_Currency
                                         ,J.Bill_Rate
                                         ,V_StkRate--J.Stock_Rate
                                         ,J.C_Code
                                         ,J.C_Name
                                         ,J.A_Code
                                         ,J.Cheque_No
                                         ,J.Note_No
                                         ,J.Cheque_Due_Date
                                         ,J.Bill_Due_Date
                                         ,J.W_Code
                                         ,J.R_Code
                                         ,J.Rep_Code
                                         ,J.Emp_No
                                         ,J.Ref_No
                                         ,J.Cash_No
                                         ,J.Cc_Code
                                         ,J.Pj_No
                                         ,J.Actv_No
                                         ,J.Si_Type
                                         ,J.Stand_By
                                         ,J.Col_No
                                         ,J.Cash_Ac_Fcc
                                         ,J.Cash_No_Fcc
                                         ,J.A_Desc
                                         ,J.Bill_Py
                                         ,J.External_Post
                                         ,J.Field1
                                         ,J.Field2
                                         ,J.Field3
                                         ,J.Field4
                                         ,J.Field5
                                         ,J.Field6
                                         ,J.Field7
                                         ,J.Field8
                                         ,J.Field9
                                         ,J.Field10
                                         ,J.C_Tel
                                         ,J.C_Address
                                         ,J.Driver_No
                                         ,J.Bill_Valued
                                         ,J.Value_Date
                                         ,J.Bill_Without_Auto_Othr_Amt
                                         ,J.Qt_Prm_No
                                         ,J.Qt_Prm_Ser
                                         ,J.Qt_Prm_Rcrd_No
                                         ,J.Prm_Code
                                         ,J.Doc_Brn_No
                                         ,J.Cmpny_No
                                         ,J.Mobile_No
                                         ,J.Not_Use_Qut_Prm
                                         ,J.Receive_Nm
                                         ,J.Conn_Si_With_Outgong
                                         ,J.C_Code_Csh
                                         ,J.C_Tax_Code
                                         ,J.Doc_No_Res
                                         ,J.Doc_Srl_Res
                                         ,J.Ac_Code
                                         ,J.Ac_Code_Dtl
                                         ,J.Ac_Dtl_Typ
                                         ,J.Pymnt_Ac
                                         ,J.Clc_Typ_No_Tax
                                         ,J.Doc_Ser_Extrnl
                                         ,J.Cncl_Flg
                                         ,J.Clc_Vat_Price_Typ
                                         ,J.Bill_Amt
                                         ,NVL(J.Vat_Amt,0)
                                         ,J.Disc_Amt_Aftr_Vat
                                         ,NVL(J.Disc_Amt_Mst_Vat,0)
                                         ,J.Vat_Amt_Disc_Mst
                                         ,J.Vat_Amt_Othr
                                         ,NVL(J.Othr_Amt,0)
                                         ,NVL(J.Disc_Amt,0)
                                         ,NVL(J.Disc_Amt_Mst,0)
                                         ,NVL(J.Disc_Amt_Dtl,0)
                                         ,J.Add_Disc_Amt_Mst
                                         ,J.Add_Disc_Amt_Dtl
                                         ,J.Othr_Amt_Disc
                                         ,J.Out_Bill_Typ
                                         ,J.Bill_Stat_Typ
                                         ,J.Crd_Disc_Per
                                         ,J.Crd_No_Disc
                                         ,J.Credit_Card
                                         ,J.Cr_Card_Amt
                                         ,J.Cr_Card_Amt_Scnd
                                         ,J.Cr_Card_Amt_Thrd
                                         ,J.Cr_Card_Comm_Per
                                         ,J.Cr_Card_Comm_Per_Scnd
                                         ,J.Cr_Card_Comm_Per_Thrd
                                         ,J.Cr_Card_Cst_No
                                         ,J.Cr_Card_Cst_No_Scnd
                                         ,J.Cr_Card_Cst_No_Thrd
                                         ,J.Cr_Card_Doc_No_Ref
                                         ,J.Cr_Card_Doc_No_Ref_Scnd
                                         ,J.Cr_Card_Doc_No_Ref_Thrd
                                         ,J.Cr_Card_Dsc
                                         ,J.Cr_Card_Dsc_Scnd
                                         ,J.Cr_Card_Dsc_Thrd
                                         ,J.Cr_Card_Max_Comm_Amt
                                         ,J.Cr_Card_Max_Comm_Amt_Scnd
                                         ,J.Cr_Card_Max_Comm_Amt_Thrd
                                         ,J.Cr_Card_No
                                         ,J.Cr_Card_No_Scnd
                                         ,J.Cr_Card_No_Thrd
                                         ,J.Cr_Doc_No_Ref
                                         ,J.Cr_Doc_No_Ref_Scnd
                                         ,J.Cr_Doc_No_Ref_Thrd
                                         ,J.Cr_Valued
                                         ,J.Cr_Valued_Scnd
                                         ,J.Cr_Valued_Thrd
                                         ,J.Cr_Value_Date
                                         ,J.Cr_Value_Date_Scnd
                                         ,J.Cr_Value_Date_Thrd
                                         ,J.Cpn_Amt
                                         ,J.Cheque_Amt
                                         ,J.Prcnt_Amt
                                         ,J.Ac_Amt
                                         ,J.Clc_Tax_Free_Qty_Flg
                                         ,J.Cmp_No
                                         ,J.Brn_No
                                         ,J.Brn_Year
                                         ,J.Brn_Usr
                                         ,J.Ad_U_Id
                                         ,J.Ad_Date
                                         ,J.Ad_Trmnl_Nm 
                                         ,J.Audit_Ref
                                         ,J.Audit_Ref_Date
                                         ,J.Audit_Ref_Desc
                                         ,J.Audit_Ref_U_Id
                                         ,J.Bill_No_Conn
                                         ,0
                                         ,J.Bill_Ser_Conn
                                         ,J.Clc_Insrnce_Load_Amt_Mthd
                                         ,J.Clc_Tax_Insrnc_Cmpny_Flg
                                         ,J.Comm_Amt_Dtl
                                         ,J.Comm_Per
                                         ,J.Export
                                         ,J.Insrnce_Add_Lmt_Doc
                                         ,J.Insrnce_Add_Lmt_Dtl
                                         ,J.Insrnce_Add_Lmt_Mst
                                         ,J.Insrnce_Apprvd_Code
                                         ,J.Insrnce_Bnf_No
                                         ,J.Insrnce_Card_No
                                         ,J.Insrnce_Card_No_Fmly
                                         ,J.Insrnce_Clss_No
                                         ,J.Insrnce_Cmp_No
                                         ,J.Insrnce_Csh_Amt
                                         ,J.Insrnce_Diagnosis
                                         ,J.Insrnce_Load_Per
                                         ,J.Insrnce_Mdcl_No
                                         ,J.Insrnce_Prson_Nm
                                         ,J.Insrnce_Rltn_Typ
                                         ,J.Load_No
                                         ,J.Load_Ser
                                         ,J.Point_Calc_Typ_No
                                         ,J.Point_Cnt
                                         ,J.Point_Cnt_All
                                         ,J.Point_Rplc_Amt
                                         ,J.Point_Rplc_Cnt
                                         ,J.Point_Typ_No
                                         ,Decode(V_Use_Out_Bills,1,1,J.Processed)
                                         ,J.Pr_Rep
                                         ,J.Up_Date
                                         ,J.Up_U_Id
                                         ,IAS_POSTING_PKG.GET_DOC_PST_SQ
                                         ,NVL(J.E_Invc_Mthd_No,Decode(Nvl(Ias_Brn_Pkg.Is_Brn_Use_E_Invc ( P_Brn_No => J.Brn_No),0),1,Gnr_Get_E_Invc_Actv_Mthd  ( P_Doc_Typ => 4,P_Sys_No => J.External_Post),Null)) 
                                         ,NVL(J.TAX_BILL_TYP,V_TAX_BILL_TYP) );
        Exception
         When Others Then         
            RollBack ;
            Raise_Application_Error(-20003,'Err. When Insert Into Ias_Bill_Mst '||CHr(13)||SqlErrm);              
        End;        
--##-------------------------------------------------------------------------------------##--      
        If J.Bill_Doc_Type=4 Then             
           --## Insert_Installemnt
           Begin        
                Insert_Installemnt  ( 4,
                                      J.Bill_No,
                                      j.bill_doc_type,
                                      J.Bill_ser,
                                      j.Bill_date,
                                      j.Ad_U_id,
                                      j.Bill_Currency,
                                      j.Cash_No,
                                      j.C_Code,
                                      'D');                          
          Exception
           When Others Then
             RollBack ;
             Raise_Application_Error(-20004,'Err. When Insert Into Insert Installemnt '||CHr(13)||SqlErrm);                           
          End;  
        End If;                  
--##-------------------------------------------------------------------------------------##--
        --## Other_Charges
        Begin
            Insert_Other_Charges( J.Bill_No,
                                  j.bill_doc_type,
                                  J.Bill_Ser,
                                  j.Bill_date,
                                  j.Ad_U_id,
                                  j.Bill_Currency,
                                  j.Cash_No,
                                  Null,
                                  'S');
        Exception
          When Others Then
            RollBack;
            Raise_Application_Error(-20005,'Err. When Insert Into Others Charges '||CHr(13)||SqlErrm);                           
        End;                                         
--##-------------------------------------------------------------------------------------##--                               
        If Nvl(V_Use_Out_Bills,0) = 1 Then
           Begin
               V_Out_No  := Ias_Insrt_Out_Bills_Pkg.Get_Out_No  ( P_Invs          => V_Invoicing_Serials, 
                                                                  P_Si_Type       => J.Si_Type          ,
                                                                  P_Cc_Code       => J.Cc_Code          ,
                                                                  P_w_code        => J.W_Code           ,
                                                                  P_bill_doc_type => J.bill_doc_type    ,
                                                                  P_Brn_No        => J.Brn_No           );   
               V_Out_Ser := Ias_Insrt_Out_Bills_Pkg.Get_Out_Ser ( P_Out_No        => V_Out_No,
                                                                  P_Si_Type       => J.Si_Type,
                                                                  P_Invs          => V_Invoicing_Serials,
                                                                  P_Cc_Code       => J.Cc_Code,
                                                                  P_w_code        => J.w_code,
                                                                  P_bill_doc_type => J.bill_doc_type,
                                                                  P_Brn_No        => J.Brn_No,
                                                                  P_Brn_Year      => J.Brn_Year);
           Exception
             When Others Then
               RollBack;
               Raise_Application_Error(-20006,'Err. When Get Out Bills Serial '||Chr(13)||SqlErrm);                           
           End;         
         End If;   
--##-------------------------------------------------------------------------------------##--
         Declare
             Cursor BD Is Select    Bill_Doc_Type             , 
                                    Bill_No                   , 
                                    Bill_Ser                  ,     
                                    Si_Type                   ,                                                                          
                                    I_Code                    , 
                                    I_Qty                     , 
                                    Itm_Unt                   , 
                                    P_Size                    , 
                                    P_Qty                     , 
                                    I_Price                   , 
                                    Stk_Cost                  , 
                                    Out_Qty                   , 
                                    Out_Free_Qty              , 
                                    W_Code                    , 
                                    Cc_Code                   ,
                                    Pj_No                     ,                                                     
                                    Actv_No                   ,
                                    Expire_Date               , 
                                    Batch_No                  , 
                                    Free_Qty                  , 
                                    Dis_Amt                   , 
                                    Dis_Amt_Mst               , 
                                    Dis_Per                   , 
                                    Dis_Amt_Dtl               , 
                                    Dis_Per2                  , 
                                    Dis_Amt_Dtl2              , 
                                    Dis_Per3                  , 
                                    Dis_Amt_Dtl3              , 
                                    Vat_Per                   , 
                                    Vat_Amt                   , 
                                    Othr_Amt                  , 
                                    Use_Serialno              , 
                                    Nvl(Service_Item,0) Service_Item, 
                                    Rcrd_No                   , 
                                    Item_Desc                 , 
                                    Brn_No                    , 
                                    Brn_Year                  , 
                                    Doc_Sequence              ,
                                    Cmp_No                    ,
                                    Brn_Usr                   ,
                                    Use_Attch                 ,
                                    Rec_Attch                 ,
                                    Post_Code                 ,
                                    Doc_Type_Ref              , 
                                    Doc_No_Ref                , 
                                    Doc_Ser_Ref               ,
                                    Barcode                   ,
                                    Comm_Per                  ,
                                    Comm_Amt_Dtl              , 
                                    Emp_No                    , 
                                    Measur_Price              , 
                                    I_Price_Vat               , 
                                    Up_Cnt                    , 
                                    Wt_Qty                    , 
                                    Field_Dtl1                , 
                                    Field_Dtl2                , 
                                    Field_Dtl3                , 
                                    Sub_C_Code                , 
                                    Wt_Unt                    ,
                                    Argmnt_No                 ,
                                    I_Length                  ,
                                    I_Width                   ,
                                    I_Height                  ,
                                    I_Number                  ,
                                    Insrnce_Load_Per          ,
                                    Insrnce_Load_Amt          ,
                                    Insrnce_Add_Lmt           ,
                                    Insrnce_Add_Lmt_Mst,
                                    Insrnce_Apprvd_Code      ,
                                    Doc_Sequence_Ref,
                                    I_Price_Outgong, 
                                    Cpn_Qty, 
                                    Used_Itm, 
                                    Vat_Amt_Othr, 
                                    Othr_Amt_Disc, 
                                    Prm_Grp_No, 
                                    Dis_Aftr_Vat_Mst, 
                                    Dis_Amt_Dtl_Vat, 
                                    Dis_Amt_Dtl2_Vat, 
                                    Vat_Amt_Dis_Dtl_Vat, 
                                    Vat_Amt_Dis_Dtl3_Vat, 
                                    Vat_Amt_Dis_Dtl2_Vat, 
                                    Dis_Amt_Mst_Vat, 
                                    Vat_Amt_Dis_Mst_Vat, 
                                    Vat_Amt_Bfr_Dis, 
                                    Vat_Amt_Aftr_Dis, 
                                    Pkg_Unt, 
                                    Pkg_Unt_Size, 
                                    Pkg_Qty,
                                    Pkg_Length, 
                                    Pkg_Width, 
                                    Pkg_Height, 
                                    Pkg_Size, 
                                    Pkg_Weight, 
                                    Dis_Amt_Aftr_Vat, 
                                    Dis_Amt_Dtl_Qt_Prm, 
                                    Dis_Amt_Dtl_Qt_Prm_Vat, 
                                    Dis_Per_Qt_Prm, 
                                    Dis_Amt_Dtl3_Vat,
                                    FREE_TYP,
                                    LEV_NO
                               From Ias_Bill_Dtl_Br
                              Where Ias_Bill_Dtl_Br.Bill_Ser=J.Bill_Ser ;                
--##-------------------------------------------------------------------------------------##--
           Begin --- (12)
               For i in BD  Loop        -->> (2)

--##-------------------------------------------------------------------------------------##--
                     Begin    
                          V_StkCost := Ias_Itm_Inv_Pkg.Get_Itm_Cost(  P_costing_type => V_Costing_Type           ,
                                                                      P_Wtavg_Type   => V_Wtavg_Type             ,
                                                                      P_icode        => i.i_code                 ,
                                                                      P_wcode        => i.w_code                 ,
                                                                      P_Psize        => Nvl(i.p_Size,1)          ,
                                                                      P_Iqty         => ( Nvl(i.i_qty,0) + Nvl(i.free_qty,0) ),
                                                                      P_ExpDate      => To_Date(Nvl(i.Expire_Date,'01/01/1900'),'DD/MM/YYYY'),
                                                                      P_BatchNo      => Nvl(i.Batch_No,'0')      ,
                                                                      P_brn_no       => J.brn_no                 ,
                                                                      P_brn_year     => J.brn_year               ,
                                                                      P_Cmp_No       => J.Cmp_No                 ,
                                                                      P_Brn_Usr      => J.Brn_Usr                 );
                     Exception 
                       When Others Then
                           RollBack;
                           Raise_Application_Error(-20007,'Err. When Get Item Cost '||Chr(13)||SqlErrm);                                                         
                     End;    
                                     
--##-------------------------------------------------------------------------------------##--       
                     Select Ias_Doc_Seq.NextVal InTo V_Seq From Dual; 
--##-------------------------------------------------------------------------------------##--                     
                     Begin
                       select use_serialno,nvl(Service_Itm,0)
                        Into 
                           V_Itm_Use_SerialNo,V_Service_Item
                         From ias_itm_mst
                         where i_code=i.i_code
                         and rownum<=1;
                     Exception when others then
                           V_Itm_Use_SerialNo:=0;
                           V_Service_Item:=0;
                     End;                                          
--##-------------------------------------------------------------------------------------##--
                   If  Nvl(V_Service_Item,0)=0  And (Nvl(I.I_Qty,0)>0 Or Nvl(I.Free_Qty,0)>0) Then
                       Begin
                           V_Cst := 0;                                                                                       
                           Ias_Itm_Inv_Pkg.Insrt_Sale_Cost (P_Cst                => V_Cst
                                                           ,P_Wtavg_Type         => V_Wtavg_Type
                                                           ,P_Icode              => I.I_Code
                                                           ,P_Iqty               => Nvl (I.I_Qty, 0)
                                                           ,P_Freeqty            => Nvl (I.Free_Qty, 0)
                                                           ,P_Itm_Unt            => I.Itm_Unt
                                                           ,P_Psize              => I.P_Size
                                                           ,P_Cost_Type          => V_Costing_type
                                                           ,P_Wcode              => I.W_Code
                                                           ,P_Doctype            => 1
                                                           ,P_Docno              => I.Bill_No
                                                           ,P_Billdoctype        => I.Bill_Doc_Type
                                                           ,P_Cc_Code            => I.Cc_Code
                                                           ,P_Pj_No              => I.Pj_No
                                                           ,P_Actv_No            => I.Actv_No
                                                           ,P_Rcrdno             => I.Rcrd_No
                                                           ,P_Expdate            =>To_Date(Nvl(i.Expire_Date,'01/01/1900'),'DD/MM/YYYY') 
                                                           ,P_Batchno            => Nvl (I.Batch_No, '0')
                                                           ,P_Docser             => I.Bill_Ser
                                                           ,P_Docseq             => V_Seq
                                                           ,P_Idate              => J.Bill_Date
                                                           ,P_Vatamt             => Nvl (I.Vat_Amt, 0)
                                                           ,P_Disamt             => I.Dis_Amt
                                                           ,P_Acy                => J.Bill_Currency
                                                           ,P_Ac_Rate            => J.Bill_Rate
                                                           ,P_Stk_Rate           => V_StkRate
                                                           ,P_C_Code             => J.C_Code
                                                           ,P_Adesc              => J.A_Desc
                                                           ,P_Refno              => J.Ref_No
                                                           ,P_Outno              => V_Out_No
                                                           ,P_Outgrser           => V_Out_Ser
                                                           ,P_Inout              => -1
                                                           ,P_Iprice             => Nvl (I.I_Price, 0)
                                                           ,P_Itm_Length         => I.I_Length
                                                           ,P_Itm_Width          => I.I_Width
                                                           ,P_Itm_Height         => I.I_Height
                                                           ,P_Itm_Number         => I.I_Number
                                                           ,P_Wt_Qty             => I.Wt_Qty
                                                           ,P_Wt_Unt             => I.Wt_Unt
                                                           ,P_Argmnt_No          => I.Argmnt_No
                                                           ,P_Ad_Date            => J.Ad_Date
                                                           ,P_Up_Date            => J.Up_Date
                                                           ,P_Brn_No             => I.Brn_No
                                                           ,P_Brn_Year           => I.Brn_Year
                                                           ,P_Cmp_No             => I.Cmp_No
                                                           ,P_Brn_Usr            => I.Brn_Usr
                                                           ,P_Free_Typ           => I.Free_Typ
                                                           ,P_Dis_Amt_Mst        => I.Dis_Amt_Mst
                                                           ,P_Dis_Amt_Mst_Vat    => I.Dis_Amt_Mst_Vat
                                                           ,P_Dis_Per            => I.Dis_Per
                                                           ,P_Dis_Amt_Dtl        => I.Dis_Amt_Dtl
                                                           ,P_Dis_Amt_Dtl_Vat    => I.Dis_Amt_Dtl_Vat
                                                           ,P_Dis_Per2           => I.Dis_Per2
                                                           ,P_Dis_Amt_Dtl2       => I.Dis_Amt_Dtl2
                                                           ,P_Dis_Amt_Dtl2_Vat   => I.Dis_Amt_Dtl2_Vat
                                                           ,P_Dis_Per3           => I.Dis_Per3
                                                           ,P_Dis_Amt_Dtl3       => I.Dis_Amt_Dtl3
                                                           ,P_Dis_Amt_Dtl3_Vat   => I.Dis_Amt_Dtl3_Vat
                                                           ,P_Othr_Amt           => I.Othr_Amt
                                                           ,P_Vat_Amt_Othr       => I.Vat_Amt_Othr
                                                           ,P_Vat_Per            => I.Vat_Per
                                                           ,P_Emp_No             => I.Emp_No
                                                           ,P_I_Price_Vat        => I.I_Price_Vat
                                                           ,P_Lev_No             => I.Lev_No);                                                            
                       Exception 
                         When Others Then
                           RollBack;
                           Raise_Application_Error(-20008,'Err. When Insrt Into Sale Cost '||Chr(13)||Sqlerrm);
                       End;   
                       V_Cst := Nvl(V_Cst,0)*Nvl(I.P_Size,1);        
                   Else
                      V_Cst := V_StkCost; 
                   End If;        
--##-------------------------------------------------------------------------------------##-- 
                   Begin
                         Insert Into Ias_Bill_Dtl(  Bill_Doc_Type       , 
                                                    Bill_No                , 
                                                    Bill_Ser            ,     
                                                    Si_Type             ,                                                                                                        
                                                    I_Code                , 
                                                    I_Qty                , 
                                                    Itm_Unt                , 
                                                    P_Size                , 
                                                    P_Qty                , 
                                                    I_Price                , 
                                                    Stk_Cost            , 
                                                    Out_Qty                , 
                                                    Out_Free_Qty        , 
                                                    W_Code                , 
                                                    Cc_Code                ,                                                                         
                                                    Pj_No               ,
                                                    Actv_No             ,
                                                    Expire_Date            , 
                                                    Batch_No            , 
                                                    Free_Qty            ,                                                                         
                                                    DIs_Amt                , 
                                                    DIs_Amt_Mst            , 
                                                    DIs_Per                , 
                                                    DIs_Amt_Dtl            , 
                                                    DIs_Per2            , 
                                                    DIs_Amt_Dtl2        , 
                                                    DIs_Per3            , 
                                                    DIs_Amt_Dtl3        , 
                                                    Vat_Per                , 
                                                    Vat_Amt                , 
                                                    Othr_Amt            , 
                                                    Use_Serialno        , 
                                                    Service_Item        ,     
                                                    Rcrd_No                , 
                                                    Item_Desc            , 
                                                    Brn_No                , 
                                                    Brn_Year            , 
                                                    Doc_Sequence        ,
                                                    Cmp_No                ,
                                                    Brn_Usr                ,
                                                    Use_Attch           ,
                                                    Rec_Attch           ,   
                                                    External_Post       ,
                                                    Post_Code           ,
                                                    Doc_Type_Ref        , 
                                                    Doc_No_Ref          , 
                                                    Doc_Ser_Ref         ,
                                                    Barcode             ,
                                                    Comm_Per            ,
                                                    Comm_Amt_Dtl        , 
                                                    Emp_No              , 
                                                    Measur_Price        , 
                                                    I_Price_Vat         , 
                                                    Up_Cnt              , 
                                                    Wt_Qty              , 
                                                    Field_Dtl1          , 
                                                    Field_Dtl2          , 
                                                    Field_Dtl3          , 
                                                    Sub_C_Code          , 
                                                    Wt_Unt              ,
                                                    Argmnt_No           ,
                                                    Insrnce_Load_Per    ,
                                                    Insrnce_Load_Amt    ,
                                                    Insrnce_Add_Lmt     ,
                                                    Insrnce_Add_Lmt_Mst,
                                                    Insrnce_Apprvd_Code,
                                                    Doc_Sequence_Ref,
                                                    I_Price_Outgong, 
                                                    Cpn_Qty, 
                                                    Used_Itm, 
                                                    Vat_Amt_Othr, 
                                                    Othr_Amt_Disc, 
                                                    Prm_Grp_No, 
                                                    Dis_Aftr_Vat_Mst, 
                                                    Dis_Amt_Dtl_Vat, 
                                                    Dis_Amt_Dtl2_Vat, 
                                                    Vat_Amt_Dis_Dtl_Vat, 
                                                    Vat_Amt_Dis_Dtl3_Vat, 
                                                    Vat_Amt_Dis_Dtl2_Vat, 
                                                    Dis_Amt_Mst_Vat, 
                                                    Vat_Amt_Dis_Mst_Vat, 
                                                    Vat_Amt_Bfr_Dis, 
                                                    Vat_Amt_Aftr_Dis, 
                                                    Pkg_Unt, 
                                                    Pkg_Unt_Size, 
                                                    Pkg_Qty,
                                                    Pkg_Length, 
                                                    Pkg_Width, 
                                                    Pkg_Height, 
                                                    Pkg_Size, 
                                                    Pkg_Weight, 
                                                    Dis_Amt_Aftr_Vat, 
                                                    Dis_Amt_Dtl_Qt_Prm, 
                                                    Dis_Amt_Dtl_Qt_Prm_Vat, 
                                                    Dis_Per_Qt_Prm, 
                                                    Dis_Amt_Dtl3_Vat,
                                                    FREE_TYP,
                                                    LEV_NO  ,
                                                    Doc_Sequence_Br,
                                                    RCRD_NO_BR
                                                    )
                                           Values( J.Bill_Doc_Type     , 
                                                    J.Bill_No            , 
                                                    J.Bill_Ser            , 
                                                    J.Si_Type           ,                                                                                                                                         
                                                    I.I_Code            , 
                                                    I.I_Qty                , 
                                                    I.Itm_Unt            , 
                                                    I.P_Size            , 
                                                    I.P_Qty                , 
                                                    I.I_Price            , 
                                                    V_Cst                  , 
                                                    Decode(V_Use_Out_Bills,1,I.I_Qty,0),
                                                    Decode(V_Use_Out_Bills,1,I.Free_Qty,0),
                                                    I.W_Code            , 
                                                    I.Cc_Code            ,
                                                    I.Pj_No             ,
                                                    I.Actv_No           ,                                                                         
                                                    I.Expire_Date        , 
                                                    I.Batch_No            , 
                                                    I.Free_Qty            , 
                                                    I.DIs_Amt            , 
                                                    I.DIs_Amt_Mst        , 
                                                    I.DIs_Per            , 
                                                    I.DIs_Amt_Dtl        , 
                                                    I.Dis_Per2            , 
                                                    I.DIs_Amt_Dtl2        , 
                                                    I.DIs_Per3            , 
                                                    I.DIs_Amt_Dtl3        , 
                                                    I.Vat_Per            , 
                                                    I.Vat_Amt            , 
                                                    I.Othr_Amt            , 
                                                    V_itm_Use_Serialno        , 
                                                    V_Service_Item      , 
                                                    I.Rcrd_No            , 
                                                    I.Item_Desc            , 
                                                    I.Brn_No            , 
                                                    I.Brn_Year            , 
                                                    V_Seq                ,
                                                    I.Cmp_No            ,
                                                    I.Brn_Usr            ,
                                                    I.Use_Attch         ,
                                                    I.Rec_Attch         ,   
                                                    J.External_Post     ,
                                                    I.Post_Code         ,
                                                    I.Doc_Type_Ref      , 
                                                    I.Doc_No_Ref        , 
                                                    I.Doc_Ser_Ref       ,
                                                    I.Barcode           ,
                                                    I.Comm_Per          ,
                                                    I.Comm_Amt_Dtl      , 
                                                    I.Emp_No            , 
                                                    I.Measur_Price      , 
                                                    I.I_Price_Vat       , 
                                                    I.Up_Cnt            , 
                                                    I.Wt_Qty            , 
                                                    I.Field_Dtl1        , 
                                                    I.Field_Dtl2        ,  
                                                    I.Field_Dtl3        , 
                                                    I.Sub_C_Code        , 
                                                    I.Wt_Unt            ,
                                                    I.Argmnt_No         ,
                                                    I.Insrnce_Load_Per  ,
                                                    I.Insrnce_Load_Amt  ,
                                                    I.Insrnce_Add_Lmt   ,
                                                    I.Insrnce_Add_Lmt_Mst,
                                                    I.Insrnce_Apprvd_Code,
                                                    I.Doc_Sequence_Ref,
                                                    I.I_Price_Outgong, 
                                                    I.Cpn_Qty, 
                                                    I.Used_Itm, 
                                                    I.Vat_Amt_Othr, 
                                                    I.Othr_Amt_Disc, 
                                                    I.Prm_Grp_No, 
                                                    I.Dis_Aftr_Vat_Mst, 
                                                    I.Dis_Amt_Dtl_Vat, 
                                                    I.Dis_Amt_Dtl2_Vat, 
                                                    I.Vat_Amt_Dis_Dtl_Vat, 
                                                    I.Vat_Amt_Dis_Dtl3_Vat, 
                                                    I.Vat_Amt_Dis_Dtl2_Vat, 
                                                    I.Dis_Amt_Mst_Vat, 
                                                    I.Vat_Amt_Dis_Mst_Vat, 
                                                    I.Vat_Amt_Bfr_Dis, 
                                                    I.Vat_Amt_Aftr_Dis, 
                                                    I.Pkg_Unt, 
                                                    I.Pkg_Unt_Size, 
                                                    I.Pkg_Qty,
                                                    I.Pkg_Length, 
                                                    I.Pkg_Width, 
                                                    I.Pkg_Height, 
                                                    I.Pkg_Size, 
                                                    I.Pkg_Weight, 
                                                    I.Dis_Amt_Aftr_Vat, 
                                                    I.Dis_Amt_Dtl_Qt_Prm, 
                                                    I.Dis_Amt_Dtl_Qt_Prm_Vat, 
                                                    I.Dis_Per_Qt_Prm, 
                                                    I.Dis_Amt_Dtl3_Vat,
                                                    I.FREE_TYP,
                                                    I.LEV_NO  ,
                                                    I.Doc_Sequence,
                                                    I.Rcrd_No);
                   Exception
                      When Others Then
                        RollBack;
                        Raise_Application_Error(-20009,'Err. When Insrt Into Ias_Bill_Dtl '||Chr(13)||SqlErrm);                        
                   End; 
--##-------------------------------------------------------------------------------------##--              
                   If  Nvl(V_Use_Itm_Attach,0) = 1 And I.Use_Attch=1 Then                  
                      Begin
                            Select 1 InTo V_Cnt
                           From Ias_Itm_Attach_Movement_Br
                           Where Doc_Ser   = J.bill_Ser
                             And Rec_Attch = I.Rec_Attch 
                             And Doc_Type  = 1
                             And RowNum<=1;
                      Exception 
                        When Others Then   
                          RollBack;                                                                       
                          Raise_Application_Error(-20010,'Err. When Get Data From Ias_Itm_Attach_Movement_Br '||Chr(13)||SqlErrm);                                                  
                      End;               
                  
                      Begin
                          Insert InTo Ias_Itm_Attach_Movement( I_Code, Itm_Unt, P_Size, 
                                                               Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                               Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                               Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                               Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                               W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                               R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                               Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Type_Ref, 
                                                               Doc_No_Ref, Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                               Ac_Rate, Stk_Rate, I_Price, Dis_Amt, I_Cost, Stk_Cost, Vat_Amt, 
                                                               V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                               Cmp_No, Brn_No, Brn_Year, Brn_Usr, Othr_Amt)
                                                        Select I_Code, Itm_Unt, P_Size, 
                                                               Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                               Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                               Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                               Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                               W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no,Rep_Code, 
                                                               R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                               Free_Qty, Pf_Qty, Rcrd_No, J.External_Post, Doc_Type_Ref, Doc_No_Ref, 
                                                               Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                               Ac_Rate, J.Stock_Rate, I.I_Price, Dis_Amt, I_Price, V_Cst, Vat_Amt, 
                                                               V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                               Cmp_No, Brn_No, Brn_Year, Brn_Usr, Othr_Amt
                                                          From Ias_Itm_Attach_Movement_Br
                                                          Where Doc_Ser   = J.bill_Ser
                                                            And Rec_Attch = I.Rec_Attch 
                                                            And Doc_Type  = 1;
                      Exception 
                        When Others Then  
                          RollBack;                                                                        
                          Raise_Application_Error(-20011,'Err. When Insrt Into Ias_Itm_Attach_Movement '||Chr(13)||SqlErrm);                                                  
                      End;       
                   End If;      
--##-------------------------------------------------------------------------------------##--    
               End Loop; --(2)
           End; --(12)        
--##-------------------------------------------------------------------------------------##--
           If Nvl(V_Use_Out_Bills,0)=1 Then
                Begin
                    Ias_Insrt_Out_Bills_Pkg.Insrt_Out_Bills ( P_Invs        => V_Invoicing_Serials   , 
                                                              P_Doc_Ser     => J.Bill_Ser            ,
                                                              P_Out_No      => V_Out_No              ,
                                                              P_Out_Ser     => V_Out_Ser             ,
                                                              P_Extrnl_Post => J.External_Post       ,    
                                                              P_Lang_No     => 1                     ,
                                                              P_Brn_No      => J.Brn_No              );
                Exception 
                  When Others Then  
                   RollBack;                                                  
                   Raise_Application_Error(-20012,'Err. When Insrt Into Out_Bills'||Chr(13)||SqlErrm);                                              
                End;                    
           End If;          
--##-------------------------------------------------------------------------------------##--      
           --Update_Reserve_Table (P_Bill_Ser =>    J.Bill_Ser );
--##-------------------------------------------------------------------------------------##--  
          If J.Clc_Typ_No_Tax Is Not Null Then
            Insrt_Tax (P_Doc_Type => 4 , P_Doc_Ser => J.Bill_Ser);
          End If;      
          If J.POINT_TYP_NO Is Not Null Then
             Insrt_Point_Trns (P_Doc_Type => 4 , P_Doc_Ser => J.Bill_Ser);
          END IF;
          If nvl(V_Use_Serialno,0)<>0  Then
           Post_Serial (P_Doc_Ser => J.Bill_Ser, P_Doc_Type =>1);
          End If; 
  --##-------------------------------------------------------------------------------------##--
  Begin
          Ars_Gnr_Pkg.Insrt_Crdt_Crd_From_Br ( P_Doc_Type        =>4
                                                  ,P_Doc_No          =>J.Bill_no
                                                  ,P_Bill_Doc_Type   =>J.Bill_Doc_Type
                                                  ,P_Doc_Ser         =>J.Bill_Ser
                                                  ,P_Doc_Date        =>J.Bill_Date
                                                  ,P_User_Id         =>J.Ad_U_id
                                                  ,P_A_Cy            =>j.Bill_Currency
                                                  ,P_Cash_No         =>J.Cash_No
                                                  ,P_C_Code          =>null
                                                  ,P_External_Post   =>85
                                                  ,Typ               =>'D');                                                 
    Exception When Others Then                                                    
       RollBack;
       Raise_Application_Error(-20013,'Ars_Gnr_Pkg.Insrt_Crdt_Crd_From_Br  = '||Chr(13)||'Bill_Ser ='||J.Bill_Ser ||Chr(13)||SqlErrm);                                               
    End; 
  --##-------------------------------------------------------------------------------------##--                 
           Begin
                Ias_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 4                 ,
                                                      G_Doc_Ser     => J.Bill_Ser        ,
                                                      P_Jv_Type     => J.Bill_Doc_Type   ,
                                                      P_Doc_No      => J.Bill_No         ,
                                                      P_Lang_No     => 1                 ,
                                                      P_User_No     => J.Ad_U_Id         ,
                                                      G_Post_Type   => 0                 );
           Exception 
               When No_Data_Found Then 
                    Null;
               When Others Then
                    RollBack;
                    Raise_Application_Error(-20013,'Error When Updating Post In Bills  = '||Chr(13)||'Tr_Ser ='||J.Bill_Ser ||Chr(13)||SqlErrm);                                                    
           End;
           If Nvl(V_Use_Out_Bills,0)=1 Then
              begin
                 Ias_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 13                 ,
                                                      G_Doc_Ser     => v_out_ser        ,
                                                      P_Jv_Type     => J.Bill_Doc_Type   ,
                                                      P_Doc_No      => v_out_no        ,
                                                      P_Lang_No     => 1                 ,
                                                      P_User_No     => J.Ad_U_Id         ,
                                                      G_Post_Type   => 0                 );
              Exception 
               When No_Data_Found Then 
                    Null;
               When Others Then
                    RollBack;
                    Raise_Application_Error(-20013,'Error When Updating Post In out Bills  = '||Chr(13)||'bill_ser ='||J.Bill_Ser ||Chr(13)||SqlErrm);                                                    
              End;                        
           End If;   
               
--##-------------------------------------------------------------------------------------##--
     End Loop; --(1)
--##-------------------------------------------------------------------------------------##--
    --## Update Ias_Bill_Mst_Br        
    Begin
       Update Ias_Bill_Mst_Br
          Set Bill_Post         = 1  
        Where Exists (Select 1 From Ias_Bill_Mst_Br_Tmp Where Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser  And RowNum <=1  )
          And Exists (Select 1 From Ias_Bill_Mst Where Bill_Ser = Ias_Bill_Mst_Br.Bill_Ser  And RowNum <=1  );
          ---- Commit ;
                     
    Exception
      When Others Then
         RollBack;
         Raise_Application_Error(-20014,'Error When Updating Bill Post  = ' ||Chr(13)||Sqlerrm);                         
     End ;

--##-------------------------------------------------------------------------------------##--
    END;                                                                                                     
--##-------------------------------------------------------------------------------------##--
End Post_Sales_Detail ;

PROCEDURE Post_Rt_Sales_Detail ( P_Doc_Ser  In Ias_Rt_Bill_Mst.Rt_Bill_Ser%Type Default Null , 
                                 P_User_No In User_R.U_Id%Type                  Default Null ,
                                 P_Lang_No In Number                            Default Null )  IS 
      V_StkCost               Number;
      V_Seq                   Number;
      V_Ret_No                Number;
      V_Ret_Ser               Number;      
      V_StkRate               Number;
      V_Py                    Number;
      V_Out_No                Number;
      V_Out_Ser               Number;
      V_No                    Number;
      V_Ser                   Number;
      V_Wt_after              Number;
      V_Wcode                 Number;
      V_Use_Out_Bills         Number; 
      V_Invs_Sr               Number;
      V_Costing_Type          Number;
      V_Wtavg_Type            Number;
      V_Allow_Enter_Zero_Cost Number:=1; 
      V_Use_Itm_Attach        Number;
      V_Use_SerialNo           Number;
      V_Itm_Use_SerialNo       Number:=0;
      V_Service_Item           Number:=0;   
      V_Stkcost_Fraction      Number;
      V_Lang_No               Number:=P_Lang_No;
      V_USE_VAT               NUMBER;
Begin
--##-------------------------------------------------------------------------------------##--
  If P_Lang_No Is Null Then    
    Begin
      Select Lang_No InTo V_Lang_No From Ias_Sys.Lang_Def Where Nvl(Flg_St,1)= 1 And Lang_Dflt=1 And Rownum<=1;
    Exception WHen Others Then
        V_Lang_No := 1;
    End;  
  ENd If;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      Select Use_Out_Bills,Invoicing_Serials_Sr,Costing_Type,Wtavg_Type,Use_Itm_Attach ,Stkcost_Fraction,Use_SerialNo
        InTo V_Use_Out_Bills,V_Invs_Sr,V_Costing_Type,V_Wtavg_Type,V_Use_Itm_Attach,V_Stkcost_Fraction,V_Use_SerialNo
        From Ias_Para_AR,Ias_Para_Inv  ,IAS_PARA_GEN  
       Where RowNum<=1;
  Exception WHen Others Then
    RollBack;
    Raise_Application_Error(-20001,'Error When Select From Para In Post_Rt_Sales_Detail '||Chr(13)||SqlErrm);
  End;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      If P_User_No<>1 Then
        Select Allow_Enter_Zero_Cost InTo V_Allow_Enter_Zero_Cost From Privilege_Fixed Where U_Id=P_User_No And RowNum<=1;
      End If;  
  Exception WHen Others Then
      RollBack;
      Raise_Application_Error(-20002,'Error When Select From Privilege_Fixed In Post_Rt_Sales_Detail'||Chr(13)||SqlErrm);
  End;
  ---------------------------------- ## Cursor Return Sales ## -------------------------------- 
   Begin
    Delete from Ias_Rt_Bill_Mst_Br_Tmp;
   Exception WHen Others Then
    Null;
   End;
       
  Insert Into Ias_Rt_Bill_Mst_Br_Tmp (Rt_Bill_No,Rt_Bill_Ser) Select Rt_Bill_No , Rt_Bill_Ser 
                                                               From Ias_Rt_Bill_Mst_Br 
                                                              Where Rt_Bill_Ser=Nvl(P_Doc_Ser,Rt_Bill_Ser) 
                                                                And Nvl(Stand_By,0)=0 
                                                                And Nvl(Rt_Bill_Post,0)=0
                                                                And Exists(Select 1 From Ias_Rt_Bill_Dtl_Br Where Rt_Bill_Ser=Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser And Rownum<=1)
                                                                And Not Exists(Select 1 From Ias_Rt_Bill_Mst Where Rt_Bill_Ser=Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser And Rownum<=1);
  Declare
       Cursor SRM Is Select Rt_Bill_Doc_Type  , 
                            Rt_Bill_No        , 
                            Rt_Bill_Ser       ,
                            P_Year            , 
                            Sr_Type           ,
                            Rt_Bill_Date      , 
                            Rt_Bill_Currency  ,
                            Rt_Bill_Rate      , 
                            Stock_Rate        ,     
                            C_Code            ,
                            C_Name            , 
                            DECODE(Rt_Bill_Doc_Type,4,A_Code ,1,IAS_CSHBNK_PKG.Get_A_code(1,Cash_No),A_Code) AS "A_CODE",             
                            Cheque_No         , 
                            Cheque_Amt        , 
                            Cheque_Due_Date   , 
                            Rt_Bill_Due_Date  , 
                            Rt_Bill_Post      , 
                            Disc_Amt          , 
                            Disc_Amt_Mst      , 
                            Disc_Amt_Mst_Vat  , 
                            Disc_Amt_Dtl      , 
                            Bill_Amt          , 
                            Vat_Amt           , 
                            Othr_Amt          , 
                            W_Code            , 
                            R_Code            ,
                            Rep_Code          , 
                            Cash_No           , 
                            Ref_No            ,
                            Cc_Code           ,
                            Pj_No             ,
                            Actv_No           ,    
                            Classify_No       , 
                            Cash_Ac_Fcc       ,
                            A_Desc            , 
                            Return_Res        , 
                            Processed         ,
                            Comm_Per          , 
                            Pr_Rep            ,                         
                            Ad_U_Id           , 
                            Ad_Date           , 
                            Up_U_Id           , 
                            Up_Date           ,                         
                            Brn_No            , 
                            Brn_Year          , 
                            Classify_Ser      ,                         
                            Audit_Ref         , 
                            Audit_Ref_Desc    , 
                            Audit_Ref_U_Id    , 
                            Audit_Ref_Date    , 
                            External_Post     , 
                            Rt_Bill_Py        ,
                            Cmp_No            ,
                            Brn_Usr           ,
                            Doc_Brn_No        ,
                            Insrnce_Cmp_No    ,
                            Insrnce_Bnf_No    ,
                            Insrnce_Prson_Nm  ,
                            Insrnce_Card_No   ,
                            Insrnce_Card_No_Fmly,
                            Insrnce_Rltn_Typ  ,
                            Insrnce_Clss_No   ,
                            Insrnce_Csh_Amt  ,
                            Insrnce_Add_Lmt_Mst,
                            Insrnce_Add_Lmt_Dtl,
                            Insrnce_Add_Lmt_Doc,
                            Export,
                            Clc_Typ_No_Tax,
                            Point_Rplc_Amt, 
                            Point_Typ_No, 
                            Point_Cnt, 
                            Point_Rplc_Cnt,
                            Clc_Vat_Price_Typ, 
                            Col_No,
                            AC_AMT,
                            AC_CODE,
                            AC_CODE_DTL,
                            AC_DTL_TYP,
                            CASH_NO_FCC,
                            PYMNT_AC,
                            AD_TRMNL_NM,
                            CC_CODE_BILL,
                            CLC_TAX_FREE_QTY_FLG,
                            CNCL_FLG,
                            DISC_AMT_AFTR_VAT,
                            DOC_SER_EXTRNL,
                            DRIVER_NO,
                            EMP_NO,
                            FIELD1,
                            FIELD10,
                            FIELD2,
                            FIELD3,
                            FIELD4,
                            FIELD5,
                            FIELD6,
                            FIELD7,
                            FIELD8,
                            FIELD9,
                            NOTE_NO,
                            OTHR_AMT_DISC,
                            PREV_YEAR,
                            PRM_CODE,
                            REP_CODE_BILL,
                            RES_TYP,
                            0 STAND_BY,
                            VAT_AMT_DISC_MST,
                            VAT_AMT_OTHR,
                            WITHOUT_VAT,
                            W_CODE_BILL,
                            E_Invc_Mthd_No
             From Ias_Rt_Bill_Mst_Br
              Where nvl(Rt_Bill_Post,0)=0    
                And Rt_Bill_Ser = Nvl(P_Doc_Ser,Rt_Bill_Ser)
                And Exists (Select 1 From Ias_Rt_Bill_Mst_Br_Tmp Where Rt_Bill_Ser = Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser  And RowNum <=1  )
       Order By Ad_Date;
    Begin ---(11)
--##-------------------------------------------------------------------------------------##--    
    --## To Get Stock Rate           
    V_StkRate := Ias_Gen_Pkg.Get_Cur_rate( P_Acy => Ias_Gen_Pkg.Get_Stk_Cur );      
--##-------------------------------------------------------------------------------------##--    
    For J In SRM Loop     -->> (1)    
        Begin
          Check_Duplicate_Sr(J.Rt_Bill_No,J.Rt_Bill_Doc_Type,J.Rt_Bill_Ser);
          Insert Into Ias_Rt_Bill_Mst(  Rt_Bill_Doc_Type             , 
                                        Rt_Bill_No                   , 
                                        Rt_Bill_Ser                  ,
                                        P_Year                       , 
                                        Sr_Type                      ,
                                        Rt_Bill_Date                 , 
                                        Rt_Bill_Currency             ,
                                        Rt_Bill_Rate                 , 
                                        Stock_Rate                   ,   
                                        C_Code                       ,
                                        C_Name                       , 
                                        A_Code                       , 
                                        Cheque_No                    , 
                                        Cheque_Amt                   , 
                                        Cheque_Due_Date              , 
                                        Rt_Bill_Due_Date             , 
                                        Rt_Bill_Post                 , 
                                        Disc_Amt                     , 
                                        Disc_Amt_Mst                 ,
                                        Disc_Amt_Mst_Vat             , 
                                        Disc_Amt_Dtl                 , 
                                        Bill_Amt                     , 
                                        Vat_Amt                      , 
                                        Othr_Amt                     , 
                                        W_Code                       , 
                                        R_Code                       ,
                                        Rep_Code                     , 
                                        Cash_No                      , 
                                        Ref_No                       ,
                                        Cc_Code                      , 
                                        Pj_No                        ,
                                        Actv_No                      ,
                                        Classify_No                  , 
                                        Cash_Ac_Fcc                  ,
                                        A_Desc                       , 
                                        Return_Res                   , 
                                        Processed                    ,
                                        Comm_Per                     , 
                                        Pr_Rep                       ,                                                 
                                        Ad_U_Id                      , 
                                        Ad_Date                      , 
                                        Up_U_Id                      , 
                                        Up_Date                      ,                                                 
                                        Brn_No                       , 
                                        Brn_Year                     , 
                                        Classify_Ser                 ,                                                    
                                        Audit_Ref                    , 
                                        Audit_Ref_Desc               , 
                                        Audit_Ref_U_Id               , 
                                        Audit_Ref_Date               , 
                                        External_Post                , 
                                        Rt_Bill_Py                   ,
                                        Cmp_No                       ,
                                        Brn_Usr                      ,
                                        Doc_Brn_No                   ,
                                        Insrnce_Cmp_No               ,
                                        Insrnce_Bnf_No               ,
                                        Insrnce_Prson_Nm             ,
                                        Insrnce_Card_No              ,
                                        Insrnce_Card_No_Fmly         ,
                                        Insrnce_Rltn_Typ             ,
                                        Insrnce_Clss_No              ,
                                        Insrnce_Csh_Amt              ,
                                        Insrnce_Add_Lmt_Mst,
                                                    Insrnce_Add_Lmt_Dtl,
                                                    Insrnce_Add_Lmt_Doc,
                                        Export,
                                        Clc_Typ_No_Tax,
                                        Point_Rplc_Amt, 
                                        Point_Typ_No, 
                                        Point_Cnt, 
                                        Point_Rplc_Cnt,
                                        Clc_Vat_Price_Typ, 
                                        Col_No  ,
                                        AC_AMT,
                                        AC_CODE,
                                        AC_CODE_DTL,
                                        AC_DTL_TYP,
                                        CASH_NO_FCC,
                                        PYMNT_AC,
                                         AD_TRMNL_NM,
                                        CC_CODE_BILL,
                                        CLC_TAX_FREE_QTY_FLG,
                                        CNCL_FLG,
                                        DISC_AMT_AFTR_VAT,
                                        DOC_SER_EXTRNL,
                                        DRIVER_NO,
                                        EMP_NO,
                                        FIELD1,
                                        FIELD10,
                                        FIELD2,
                                        FIELD3,
                                        FIELD4,
                                        FIELD5,
                                        FIELD6,
                                        FIELD7,
                                        FIELD8,
                                        FIELD9,
                                        NOTE_NO,
                                        OTHR_AMT_DISC,
                                        PREV_YEAR,
                                        PRM_CODE,
                                        REP_CODE_BILL,
                                        RES_TYP,
                                        STAND_BY,
                                        VAT_AMT_DISC_MST,
                                        VAT_AMT_OTHR,
                                        WITHOUT_VAT,
                                        W_CODE_BILL,
                                        DOC_PST_SQ,
                                        E_INVC_MTHD_NO )
                                Values( J.Rt_Bill_Doc_Type           , 
                                        J.Rt_Bill_No                 , 
                                        J.Rt_Bill_Ser                , 
                                       Decode(Nvl(J.External_post,0),70,J.P_year, Decode(J.P_Year,0,2,J.P_Year)),
                                        J.Sr_Type                    ,
                                        J.Rt_Bill_Date               , 
                                        J.Rt_Bill_Currency           ,
                                        J.Rt_Bill_Rate               , 
                                        V_StkRate                      , 
                                        J.C_Code                     ,
                                        J.C_Name                     , 
                                        J.A_Code                     , 
                                        J.Cheque_No                  , 
                                        J.Cheque_Amt                 , 
                                        J.Cheque_Due_Date            , 
                                        J.Rt_Bill_Due_Date           , 
                                        0                            , 
                                        J.Disc_Amt                   , 
                                        J.Disc_Amt_Mst               ,
                                        J.Disc_Amt_Mst_Vat           , 
                                        J.Disc_Amt_Dtl               , 
                                        J.Bill_Amt                   , 
                                        J.Vat_Amt                    , 
                                        J.Othr_Amt                   , 
                                        J.W_Code                     , 
                                        J.R_Code                     ,
                                        J.Rep_Code                   ,  
                                        J.Cash_No                    , 
                                        J.Ref_No                     ,
                                        J.Cc_Code                    ,
                                        J.Pj_No                      ,
                                        J.Actv_No                    ,    
                                        J.Classify_No                , 
                                        J.Cash_Ac_Fcc                ,
                                        J.A_Desc                     , 
                                        J.Return_Res                 , 
                                        Decode(V_Use_Out_Bills,1,1,J.Processed),
                                        J.Comm_Per                   , 
                                        J.Pr_Rep                     ,                                                 
                                        J.Ad_U_Id                    , 
                                        J.Ad_Date                    , 
                                        J.Up_U_Id                    , 
                                        J.Up_Date                    ,                                                 
                                        J.Brn_No                     , 
                                        J.Brn_Year                   , 
                                        J.Classify_Ser               ,                                                 
                                        J.Audit_Ref                  , 
                                        J.Audit_Ref_Desc             , 
                                        J.Audit_Ref_U_Id             , 
                                        J.Audit_Ref_Date             , 
                                        J.External_Post              , 
                                        J.Rt_Bill_Py                 ,
                                        J.Cmp_No                     ,
                                        J.Brn_Usr                    ,
                                        J.Doc_Brn_No                 ,
                                        J.Insrnce_Cmp_No             ,
                                        J.Insrnce_Bnf_No             ,
                                        J.Insrnce_Prson_Nm           ,
                                        J.Insrnce_Card_No            ,
                                        J.Insrnce_Card_No_Fmly       ,
                                        J.Insrnce_Rltn_Typ           ,
                                        J.Insrnce_Clss_No            ,
                                        J.Insrnce_Csh_Amt            ,
                                        J.Insrnce_Add_Lmt_Mst,
                                                    J.Insrnce_Add_Lmt_Dtl,
                                                    J.Insrnce_Add_Lmt_Doc,
                                        J.Export                     ,
                                        J.Clc_Typ_No_Tax             ,
                                        J.Point_Rplc_Amt, 
                                        J.Point_Typ_No, 
                                        J.Point_Cnt, 
                                        J.Point_Rplc_Cnt,
                                        J.Clc_Vat_Price_Typ, 
                                        J.Col_No ,
                                        J.AC_AMT,
                                        J.AC_CODE,
                                        J.AC_CODE_DTL,
                                        J.AC_DTL_TYP,
                                        J.CASH_NO_FCC,
                                        J.PYMNT_AC
                                       ,J.Ad_Trmnl_Nm
                                          ,J.Cc_Code_Bill
                                          ,J.Clc_Tax_Free_Qty_Flg
                                          ,J.Cncl_Flg
                                          ,J.Disc_Amt_Aftr_Vat
                                          ,J.Doc_Ser_Extrnl
                                          ,J.Driver_No
                                          ,J.Emp_No
                                          ,J.Field1
                                          ,J.Field10
                                          ,J.Field2
                                          ,J.Field3
                                          ,J.Field4
                                          ,J.Field5
                                          ,J.Field6
                                          ,J.Field7
                                          ,J.Field8
                                          ,J.Field9
                                          ,J.Note_No
                                          ,J.Othr_Amt_Disc
                                          ,J.Prev_Year
                                          ,J.Prm_Code
                                          ,J.Rep_Code_Bill
                                          ,J.Res_Typ
                                          ,J.Stand_By
                                          ,J.Vat_Amt_Disc_Mst
                                          ,J.Vat_Amt_Othr
                                          ,J.Without_Vat
                                          ,J.W_Code_Bill
                                          ,IAS_POSTING_PKG.GET_DOC_PST_SQ 
                                          ,NVL(J.E_Invc_Mthd_No,Decode(Nvl(Ias_Brn_Pkg.Is_Brn_Use_E_Invc ( P_Brn_No => J.Brn_No),0),1,Gnr_Get_E_Invc_Actv_Mthd  ( P_Doc_Typ => 5,P_Sys_No => J.External_Post),Null)  )  );
        Exception
         When Others Then
            RollBack;
            Raise_Application_Error(-20003,'Error When Insert Into Ias_Rt_Bill_Mst In Post Rt Sales , '||Chr(13)||SqlErrm);    
        End;        
--##-------------------------------------------------------------------------------------##--      
  If V_Use_Out_Bills=1 Then
        V_Ret_No  := Ias_Insrt_Out_Bills_Pkg.Get_Ret_No  ( P_Invs_sr       => V_Invs_Sr , 
                                                           P_Sr_Type       => J.Sr_Type          ,
                                                           P_Cc_Code       => J.Cc_Code          ,
                                                           P_w_code        => J.w_Code           ,
                                                           P_bill_doc_type => J.Rt_bill_doc_type ,
                                                           P_Brn_No        => J.Brn_No           );   
                                                           
         V_Ret_Ser := Ias_Insrt_Out_Bills_Pkg.Get_Ret_Ser ( P_ret_No        => V_Ret_No           ,
                                                            P_Sr_Type       => J.Sr_Type          ,
                                                            P_Invs_Sr       => V_Invs_sr ,
                                                            P_Cc_Code       => J.Cc_Code          ,
                                                            P_w_code        => J.w_code           ,
                                                            P_bill_doc_type => J.Rt_bill_doc_type ,
                                                            P_Brn_No        => J.Brn_No           ,
                                                            P_Brn_Year      => J.Brn_Year         );
  End If;      
--##-------------------------------------------------------------------------------------##--
    If V_Use_Out_Bills=0 Then
        V_No  := J.rt_bill_no;
        V_Ser := J.rt_bill_ser;
    Else
        V_No  := V_Ret_No;
        V_Ser := V_Ret_Ser;
    End If;
--##-------------------------------------------------------------------------------------##--            
    Begin
          IAS_Itm_Inv_Pkg.Insrt_Gr_Mst ( p_doctype  => 3                         ,
                                         p_gr_no    => V_No                      ,
                                         p_g_ser    => V_Ser                     ,                                                                              
                                         p_doc_ser  => J.rt_bill_ser             ,
                                         p_doc_date => J.rt_bill_date            ,
                                         p_a_code   => J.a_code                  ,
                                         p_acy      => J.rt_bill_currency        ,
                                         p_c_code   => J.c_code                  ,
                                         p_acrate   => J.rt_bill_rate            ,
                                         p_stkrate  => V_StkRate                   ,
                                         p_gramt    => J.bill_amt                ,
                                         p_pi_no    => J.rt_bill_no              ,
                                         p_cc_code  => J.Cc_Code                 ,
                                         p_pj_no    => J.Pj_No                   ,
                                         p_Actv_no  => J.Actv_No                 ,
                                         p_w_code   => J.W_Code                  ,
                                         p_refno    => J.ref_no                  ,
                                         p_desc     => J.a_desc                  ,
                                         p_cflag    => 1                         ,
                                         p_pur_type => J.P_Year                  ,
                                         p_User_No  => J.Ad_U_Id                 ,
                                         P_Brn_no   => J.Brn_no                  ,
                                         P_Brn_Year => J.Brn_Year                ,
                                         P_Cmp_No   => J.Cmp_No                  ,
                                         P_Brn_Usr  => J.Brn_Usr                 );
                                
        Exception when Others Then
             RollBack;
             Raise_Application_Error(-20004,'Error When Insert Into Gr_Note In Post Rt Sales'||Chr(13)||SqlErrm);
        End;
--##-------------------------------------------------------------------------------------##--    
--## Other_Charges
    Insert_Other_Charges_Sr(  J.Rt_Bill_No,
                              j.Rt_bill_doc_type,
                              J.Rt_Bill_ser,
                              j.Rt_Bill_date,
                              j.Ad_U_id,
                              j.Rt_Bill_Currency,
                              j.Cash_No,
                              j.C_Code,
                              'D');    
--##-------------------------------------------------------------------------------------##--    
  Declare
         Cursor SRD Is Select  Rt_Bill_Doc_Type                , 
                               Rt_Bill_No                      , 
                               Rt_Bill_Ser                     ,
                               Sr_Type                         , 
                               Bill_No                         , 
                               Bill_Doc_Type                   ,        
                               Bill_Ser                        ,                                                    
                               I_Code                          , 
                               I_Qty                           , 
                               Itm_Unt                         , 
                               P_Size                          , 
                               P_Qty                           , 
                               I_Price_Vat                     , 
                               I_Price                         , 
                               Stk_Cost                        , 
                               W_Code                          , 
                               Cc_Code                         ,
                               Pj_No                           ,
                               Actv_No                         ,    
                               Expire_Date                     , 
                               Batch_No                        , 
                               Free_Qty                        , 
                               Nvl(Service_Item,0) Service_Item,                                                   
                               Dis_Amt, 
                               Dis_Amt_Mst,
                               Dis_Amt_Mst_Vat,                                     
                               Vat_Amt_Dis_Mst_Vat,
                               Dis_Per, 
                               Dis_Amt_Dtl,
                               Dis_Amt_Dtl_Vat,  
                               Vat_Amt_Dis_Dtl_Vat, 
                               Dis_Per2, 
                               Dis_Amt_Dtl2, 
                               Dis_Amt_Dtl2_Vat,  
                               Vat_Amt_Dis_Dtl2_Vat, 
                               Dis_Per3, 
                               Dis_Amt_Dtl3,
                               Dis_Amt_Dtl3_Vat,    
                               Vat_Amt_Dis_Dtl3_Vat, 
                               Vat_Per, 
                               Vat_Amt, 
                               Othr_Amt,
                               Ret_Qty                         , 
                               Ret_Free_Qty                    , 
                               Use_Serialno                    , 
                               Si_Rcrd_No                      , 
                               Rcrd_No                         , 
                               Item_Desc                       , 
                               Brn_No                          , 
                               Brn_Year                        ,
                               Cmp_No                          ,
                               Brn_Usr                         ,
                               Use_Attch                       , 
                               Rec_Attch                       ,
                               Doc_Sequence_Si                 ,
                               Post_Code                       ,
                               Insrnce_Load_Per                ,
                               Insrnce_Load_Amt                ,                               
                               Insrnce_Add_Lmt_Mst             ,                               
                               Emp_No                          ,
                               Field_Dtl1                      ,
                               Field_Dtl2                      ,
                               Field_Dtl3                      ,
                               Sub_C_Code                      ,
                               Up_Cnt                          ,
                               Doc_No_Ref                      ,
                               Doc_Ser_Ref                     ,
                               Doc_Type_Ref                    ,
                               Rcrd_No_Ref                     ,
                               I_Length                        ,
                               I_Width                         ,
                               I_Height                        ,
                               I_Number                        ,
                               Wt_Qty                          ,
                               Wt_Unt                          ,
                               Argmnt_No                       ,
                               DIS_AFTR_VAT_MST,
                               FREE_TYP,                               
                                OTHR_AMT_DISC,
                                VAT_AMT_AFTR_DIS,
                                VAT_AMT_BFR_DIS,
                                VAT_AMT_OTHR ,                                
                                BARCODE,
                                DIS_AMT_AFTR_VAT,                              
                                QT_PRM_NO,
                                QT_PRM_RCRD_NO,
                                QT_PRM_SER                                  
                          From Ias_Rt_Bill_Dtl_Br             
                         Where Ias_Rt_Bill_Dtl_Br.Rt_bill_ser=J.Rt_bill_ser;     
--##-------------------------------------------------------------------------------------##--           
    Begin --- (12)
         For i in SRD  Loop        -->> (2)
         Begin
       --##-------------------------------------------------------------------------------------##--               
            If V_Costing_Type = 2 Then  -- WtAvrg
               V_Stkcost:=Ias_Itm_Pkg.Get_Grand_Wtavg ( P_Wtavg_Type => V_Wtavg_Type ,
                                                        P_Icode      => I.I_Code,
                                                        P_Wcode      => I.W_Code)* Nvl(I.P_Size,1);                                                      
             Else -- FIFO
                 V_StkCost:=Last_Incoming_Price ( P_Wtavg_Type => V_Wtavg_Type ,
                                                  P_Icode      => i.I_code,
                                                  P_Psize      => i.p_size,
                                                  P_Wcode      => i.w_code,
                                                  P_Type       => 1) ;
             End If;
             
             If Nvl(V_Stkcost,0)  = 0 Then
                Begin
                       V_Stkcost := Inv_Get_Lst_Itm_Wtavg_Fnc (   P_I_Code     => I.I_code ,      
                                                                  P_P_Size     => I.p_size  ,     
                                                                  P_W_Code     => I.w_code  ,   
                                                                  P_Cost_Type  =>V_Costing_Type  ,
                                                                  P_Wtavg_Type =>V_Wtavg_Type     
                                                                  )* nvl(I.p_size,1);
                Exception When Others Then
                       RollBack;
                      Raise_Application_Error(-20004,'Error When Inv_Get_Lst_Itm_Wtavg_Fnc'); 
                End;   
             End If ;                                                                    
            -------------------------------------------------------------------------------------------
             Begin
               select nvl(use_serialno,0),nvl(Service_Itm,0)
                Into 
                    V_Itm_Use_SerialNo,V_Service_Item
                 From ias_itm_mst
                 where i_code=i.i_code
                 and rownum<=1;
             Exception when others then
                   V_Itm_Use_SerialNo:=0;
                   V_Service_Item:=0;
             End; 
            -------------------------------------------------------------------------------------------
            If Nvl(V_Service_Item,0)=0 And V_Allow_Enter_Zero_Cost = 0 And Nvl(V_StkCost,0) = 0  Then
               RollBack;
               Raise_Application_Error(-20005,'Error When Not Allow Enter Zero Cost In Post Rt Sales');                   
            End If ;                    
            --##----------------------------------------------------------------------------------##--       
            Select Ias_Doc_Seq.NextVal InTo V_Seq From Dual;
            --##-------------------------------------------------------------------------------------##-- 
             Begin 
               Insert Into Ias_Rt_Bill_Dtl ( Rt_Bill_Doc_Type, 
                                             Rt_Bill_No, 
                                             Rt_Bill_Ser, 
                                             Sr_Type,   
                                             Bill_No, 
                                             Bill_Doc_Type, 
                                             Bill_Ser,                                                                            
                                             I_Code, 
                                             I_Qty, 
                                             Itm_Unt, 
                                             P_Size, 
                                             P_Qty, 
                                             I_Price_Vat,
                                             I_Price,
                                             Stk_Cost, 
                                             W_Code, 
                                             Cc_Code, 
                                             Pj_No,
                                             Actv_No,
                                             Expire_Date, 
                                             Batch_No, 
                                             Free_Qty, 
                                             Service_Item,                                                                            
                                              Dis_Amt, 
                                               Dis_Amt_Mst,
                                               Dis_Amt_Mst_Vat,                                     
                                               Vat_Amt_Dis_Mst_Vat,
                                               Dis_Per, 
                                               Dis_Amt_Dtl,
                                               Dis_Amt_Dtl_Vat,  
                                               Vat_Amt_Dis_Dtl_Vat, 
                                               Dis_Per2, 
                                               Dis_Amt_Dtl2, 
                                               Dis_Amt_Dtl2_Vat,  
                                               Vat_Amt_Dis_Dtl2_Vat, 
                                               Dis_Per3, 
                                               Dis_Amt_Dtl3,
                                               Dis_Amt_Dtl3_Vat,    
                                               Vat_Amt_Dis_Dtl3_Vat, 
                                               Vat_Per, 
                                               Vat_Amt, 
                                               Othr_Amt, 
                                             Ret_Qty, 
                                             Ret_Free_Qty, 
                                             Use_Serialno, 
                                             Si_Rcrd_No, 
                                             Rcrd_No, 
                                             Item_Desc, 
                                             Brn_No, 
                                             Brn_Year, 
                                             Doc_Sequence, 
                                             External_Post,
                                             Cmp_No,
                                             Brn_Usr,
                                             Use_Attch, 
                                             Rec_Attch,
                                             Doc_Sequence_Si,
                                             Post_Code,
                                             Insrnce_Load_Per,
                                             Insrnce_Load_Amt,
                                             Insrnce_Add_Lmt_Mst,                                                                                                                                
                                             Emp_No,
                                             Field_Dtl1,
                                             Field_Dtl2,
                                             Field_Dtl3,
                                             Sub_C_Code,
                                             Up_Cnt,
                                             Wt_Qty,
                                             Wt_Unt,
                                             Doc_No_Ref,
                                             Doc_Ser_Ref,
                                             Doc_Type_Ref,
                                             Rcrd_No_Ref,
                                             DIS_AFTR_VAT_MST,
                                            FREE_TYP,                                           
                                            OTHR_AMT_DISC,
                                            VAT_AMT_AFTR_DIS,
                                            VAT_AMT_BFR_DIS,
                                             VAT_AMT_OTHR  ,
                                             BARCODE,
                                            DIS_AMT_AFTR_VAT,                              
                                            QT_PRM_NO,
                                            QT_PRM_RCRD_NO,
                                            QT_PRM_SER)
                                     Values( J.Rt_Bill_Doc_Type, 
                                             J.Rt_Bill_No, 
                                             J.Rt_Bill_Ser, 
                                             J.Sr_Type,                                                                              
                                             Decode(Nvl(J.External_post,0),70,I.Bill_No, Decode(J.P_Year,0,null,I.Bill_No)),
                                             Decode(Nvl(J.External_post,0),70,I.Bill_Doc_Type, Decode(J.P_Year,0,null,I.Bill_Doc_Type)),
                                             Decode(Nvl(J.External_post,0),70,I.Bill_Ser,Decode(J.P_Year,0,null,I.Bill_Ser)),
                                             I.I_Code, 
                                             I.I_Qty, 
                                             I.Itm_Unt, 
                                             I.P_Size, 
                                             I.P_Qty, 
                                             I.I_Price_Vat,
                                             I.I_Price, 
                                             V_StkCost, 
                                             I.W_Code, 
                                             I.Cc_Code,
                                             I.Pj_No,  
                                             I.Actv_No, 
                                             I.Expire_Date, 
                                             I.Batch_No, 
                                             I.Free_Qty, 
                                             V_Service_Item, 
                                             I.Dis_Amt, 
                                               I.Dis_Amt_Mst,
                                               I.Dis_Amt_Mst_Vat,                                     
                                               I.Vat_Amt_Dis_Mst_Vat,
                                               I.Dis_Per, 
                                               I.Dis_Amt_Dtl,
                                               I.Dis_Amt_Dtl_Vat,  
                                               I.Vat_Amt_Dis_Dtl_Vat, 
                                               I.Dis_Per2, 
                                               I.Dis_Amt_Dtl2, 
                                               I.Dis_Amt_Dtl2_Vat,  
                                               I.Vat_Amt_Dis_Dtl2_Vat, 
                                               I.Dis_Per3, 
                                               I.Dis_Amt_Dtl3,
                                               I.Dis_Amt_Dtl3_Vat,    
                                               I.Vat_Amt_Dis_Dtl3_Vat,
                                               I.Vat_Per, 
                                               I.Vat_Amt, 
                                               I.Othr_Amt, 
                                             Decode(V_Use_Out_Bills,1,I.I_Qty,0),
                                             Decode(V_Use_Out_Bills,1,I.Free_Qty,0),
                                             V_Itm_Use_SerialNo, 
                                             I.Si_Rcrd_No, 
                                             I.Rcrd_No, 
                                             I.Item_Desc, 
                                             I.Brn_No, 
                                             I.Brn_Year, 
                                             V_Seq, 
                                             J.External_Post,
                                             I.Cmp_No,
                                             I.Brn_Usr,
                                             I.Use_Attch,
                                             I.Rec_Attch,
                                             I.Doc_Sequence_Si,
                                             I.Post_Code,
                                             I.Insrnce_Load_Per,
                                             I.Insrnce_Load_Amt,
                                             I.Insrnce_Add_Lmt_Mst,                                                                                        
                                             I.Emp_No,
                                             I.Field_Dtl1,
                                             I.Field_Dtl2,
                                             I.Field_Dtl3,
                                             I.Sub_C_Code,
                                             I.Up_Cnt,
                                             I.Wt_Qty,
                                             I.Wt_Unt,
                                             I.Doc_No_Ref,
                                             I.Doc_Ser_Ref,
                                             I.Doc_Type_Ref,
                                             I.Rcrd_No_Ref,
                                             I.DIS_AFTR_VAT_MST,
                                             I.FREE_TYP,                                            
                                             I.OTHR_AMT_DISC,
                                             I.VAT_AMT_AFTR_DIS,
                                             I.VAT_AMT_BFR_DIS,
                                             I.VAT_AMT_OTHR,
                                             I.BARCODE,
                                             I.DIS_AMT_AFTR_VAT,                              
                                             I.QT_PRM_NO,
                                             I.QT_PRM_RCRD_NO,
                                             I.QT_PRM_SER);
              Exception
                  When Others Then                  
                    RollBack;
                    Raise_Application_Error(-20006,'Error When Insert Into Ias_Rt_Bill_Dtl  '||Chr(13)||SqlErrm);
              End;
              
              If V_Use_Itm_Attach=1 And Nvl(I.Use_Attch,0)=1 Then
                  Declare
                      V_Cnt Number;
                  Begin
                      Select 1 InTo V_Cnt
                               From Ias_Itm_Attach_Movement_Br
                           Where Doc_Ser   = J.rt_bill_Ser
                             And Rec_Attch = I.Rec_Attch 
                             And Doc_Type  = 3
                             And RowNum<=1;
                 Exception When Others Then                                                                          
                      Raise_Application_Error(-20007,'Error When Select Attach From Ias_Itm_Attach_Movement_Br , Attach Not Found (Rt Sales)'||Chr(13)||SqlErrm);
                      RollBack;                                                  
                 End;               
                         
                  Begin
                      Insert InTo Ias_Itm_Attach_Movement ( I_Code, Itm_Unt, P_Size,Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                            Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4,Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                            Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser,W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                            R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Type_Ref, 
                                                            Doc_No_Ref, Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy,Ac_Rate, Stk_Rate, I_Price, Dis_Amt, I_Cost, Stk_Cost, Vat_Amt, 
                                                            V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, Cmp_No, Brn_No, Brn_Year, Brn_Usr, Othr_Amt)
                                                     Select I_Code, Itm_Unt, P_Size, 
                                                            Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2,Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                            Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch,Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                            W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code,R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                            Free_Qty, Pf_Qty, Rcrd_No, J.External_Post, Doc_Type_Ref, Doc_No_Ref,Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                            Ac_Rate, J.Stock_Rate, I.I_Price, Dis_Amt, I_Price, V_StkCost, Vat_Amt,V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                            Cmp_No, Brn_No, Brn_Year,  Brn_Usr, Othr_Amt
                                                       From Ias_Itm_Attach_Movement_Br
                                                      Where Doc_Ser   = J.rt_bill_Ser
                                                        And Rec_Attch = I.Rec_Attch 
                                                        And Doc_Type  = 3;
                  Exception When Others Then                                                    
                      RollBack;
                      Raise_Application_Error(-20008,'Error In Insert InTo Ias_Itm_Attach_Movement (Rt Sales)'||Chr(13)||SqlErrm);                                                  
                  End;       
                End If;      
--##-------------------------------------------------------------------------------------##--             
                If Nvl(V_Service_Item,0)=0 Then
                            --## Calc_WatAvg                
                            Begin    
                              V_Wt_After := Calc_Wtavg_Cost ( p_cost_type  => V_costing_type              ,
                                                              p_wtavg_type => V_wtavg_type                , 
                                                              p_icode      => i.i_code                    ,
                                                              p_iqty       => i.i_qty                     ,
                                                              P_Frqty      => Nvl(i.free_qty,0)           ,
                                                              p_icost      => Nvl(v_stkcost,0)              ,
                                                              p_psize      => i.p_size                    ,
                                                              p_wcode      => i.w_code                    ,
                                                              P_Frc_No     => V_Stkcost_Fraction ,
                                                              P_brn_no     => J.brn_no                    ,
                                                              P_brn_year   => J.brn_year                  ,
                                                              P_Cmp_No     => J.Cmp_No                    ,                                                                        
                                                              P_Brn_Usr    => J.Brn_Usr                   );
                            Exception 
                             When Others Then
                                 RollBack;
                                 Raise_Application_Error(-20009,'Error When Calc WtAvg Error , (Rt Sales) '||Chr(13)||SqlErrm);
                            End;      
                           --##-------------------------------------------------------------------------------------##--
                           Begin
                                IAS_Itm_Inv_Pkg.Insrt_Gr_Dtl (  p_doctype       => 3,
                                                                p_gr_no         => V_No,
                                                                p_g_ser         => V_Ser,
                                                                p_doc_ser       => J.rt_bill_ser,
                                                                p_DocSeq        => V_Seq,
                                                                p_doc_date      => J.rt_bill_date,
                                                                p_acy           => J.rt_bill_currency,
                                                                p_acrate        => J.rt_bill_rate,
                                                                p_stkrate       => V_StkRate,
                                                                p_pi_no         => J.rt_bill_no,                                                                    
                                                                p_pur_type      => J.p_year,
                                                                p_w_code        => nvl(J.W_Code,I.w_code),
                                                                p_cc_code       => nvl(J.Cc_Code,I.Cc_Code),
                                                                p_Pj_no         => nvl(J.Pj_no,I.Pj_no),
                                                                p_Actv_no       => nvl(J.Actv_no,I.Actv_no),
                                                                p_icode         => I.i_code,
                                                                p_iqty          => I.i_qty,
                                                                p_freeqty       => I.free_qty,
                                                                p_Itm_Unt       => I.Itm_Unt,
                                                                p_psize         => I.p_size,
                                                                p_iprice        => I.i_price,
                                                                p_cprice        => (V_stkcost*V_StkRate)/J.rt_bill_rate,
                                                                p_stkcost       => V_stkcost,
                                                                p_wtavg_before  => V_stkcost/Nvl(I.p_size,1),
                                                                p_wtavg_after   => Nvl(V_Wt_after,0),
                                                                p_vatper        => I.vat_per,
                                                                p_vatamt        => I.vat_amt,
                                                                p_disamt        => I.dis_amt ,
                                                                p_expdate       => To_Date(I.Expire_date,'DD/MM/YYYY'),
                                                                p_batchno       => I.Batch_no,
                                                                p_rcrdno        => I.rcrd_no,
                                                                p_use_serial    => V_Itm_Use_SerialNo,
                                                                p_Brn_no        => J.Brn_no,
                                                                p_Brn_Year      => J.Brn_Year,
                                                                P_Cmp_No        => J.Cmp_No,
                                                                P_Brn_Usr       => J.Brn_Usr);
                           Exception when Others Then
                              RollBack;
                              Raise_Application_Error(-20010,'Error When Insert Into Gr Detail , (Rt Sales) '||Chr(13)||SqlErrm);
                           End;
                          -------------------------------------------------------------------------------------------- 
                          --## Insert Into Item_movement        
                          Begin 
                          
                             Ias_Itm_Inv_Pkg.Insrt_Item_Move (P_Doctype            => 3
                                   ,P_Billdoctype        => J.Rt_Bill_Doc_Type
                                   ,P_Docno              => J.Rt_Bill_No
                                   ,P_Icode              => I.I_Code
                                   ,P_Iqty               => I.I_Qty
                                   ,P_Freeqty            => I.Free_Qty
                                   ,P_Itm_Unt            => I.Itm_Unt
                                   ,P_Psize              => I.P_Size
                                   ,P_Idate              => J.Rt_Bill_Date
                                   ,P_Iprice             => I.I_Price
                                   ,P_Wcode              => I.W_Code
                                   ,P_Stkcost            => V_stkcost
                                   ,P_Vatamt             => I.Vat_Amt
                                   ,P_Disamt             => I.Dis_Amt
                                   ,P_Acy                => J.Rt_Bill_Currency
                                   ,P_Ac_Rate            => J.Rt_Bill_Rate
                                   ,P_Stk_Rate           => V_StkRate
                                   ,P_Cc_Code            => Nvl (J.Cc_Code, I.Cc_Code)
                                   ,P_Pj_No              => Nvl (J.Pj_No, I.Pj_No)
                                   ,P_Actv_No            => Nvl (J.Actv_No, I.Actv_No)
                                   ,P_C_Code             => J.C_Code
                                   ,P_Adesc              => J.A_Desc
                                   ,P_Expdate            => To_Date(I.Expire_date,'DD/MM/YYYY')
                                   ,P_Batchno            => I.Batch_No
                                   ,P_Rcrdno             => I.Rcrd_No
                                   ,P_Refno              => J.Ref_No
                                   ,P_Docser             => J.Rt_Bill_Ser
                                   ,P_Docseq             => V_Seq
                                   ,P_Outno              => V_Ret_No
                                   ,P_Outgrser           => V_Ret_Ser
                                   ,P_Rt_Type            => J.P_Year
                                   ,P_Inout              => 1
                                   ,P_Ad_Date            => J.Ad_Date
                                   ,P_Up_Date            => J.Up_Date
                                   ,P_Brn_No             => J.Brn_No
                                   ,P_Brn_Year           => J.Brn_Year
                                   ,P_Cmp_No             => J.Cmp_No
                                   ,P_Brn_Usr            => J.Brn_Usr
                                   ,P_Free_Typ           => I.Free_Typ
                                   ,P_Dis_Amt_Mst        => I.Dis_Amt_Mst
                                   ,P_Dis_Amt_Mst_Vat    => I.Dis_Amt_Mst_Vat
                                   ,P_Dis_Per            => I.Dis_Per
                                   ,P_Dis_Amt_Dtl        => I.Dis_Amt_Dtl
                                   ,P_Dis_Amt_Dtl_Vat    => I.Dis_Amt_Dtl_Vat
                                   ,P_Dis_Per2           => I.Dis_Per2
                                   ,P_Dis_Amt_Dtl2       => I.Dis_Amt_Dtl2
                                   ,P_Dis_Amt_Dtl2_Vat   => I.Dis_Amt_Dtl2_Vat
                                   ,P_Dis_Per3           => I.Dis_Per3
                                   ,P_Dis_Amt_Dtl3       => I.Dis_Amt_Dtl3
                                   ,P_Dis_Amt_Dtl3_Vat   => I.Dis_Amt_Dtl3_Vat
                                   ,P_Othr_Amt           => I.Othr_Amt
                                   ,P_Vat_Amt_Othr       => I.Vat_Amt_Othr
                                   ,P_Vat_Per            => I.Vat_Per
                                   ,P_Emp_No             => I.Emp_No
                                   ,P_I_Price_Vat        => I.I_Price_Vat
                                   ,P_Lev_No             => Null);                                                                                                            
                        Exception when Others Then
                          RollBack;
                          Raise_Application_Error(-20010,'Error When Insert Into Item Movement , (Rt Sales) '||Chr(13)||SqlErrm);
                        End;
                      End If;     
                   End;                  
      End Loop; --(2)
     End; --(12)
--##-------------------------------------------------------------------------------------##--
     If V_Use_Out_Bills=1 Then
            If J.P_Year=0 And nvl(J.External_Post,0)=85 Then
                V_Py := 2;
            Else
                V_Py := J.P_Year;
            End If;    
            
            Begin
              Ias_Insrt_Out_Bills_Pkg.Insrt_Ret_Bills ( P_Invs_Sr     => V_Invs_Sr             , 
                                                        P_Pyear       => V_Py                  ,
                                                        P_Doc_Ser     => J.Rt_Bill_Ser         ,                                                        
                                                        P_Ret_No      => V_Ret_No              ,
                                                        P_Ret_Ser     => V_Ret_Ser             ,
                                                        P_Out_No      => V_Out_No              ,
                                                        P_Out_Ser     => V_Out_Ser             ,
                                                        P_Extrnl_Post => J.External_Post       ,    
                                                        P_Lang_No     => V_Lang_No             ,     
                                                        P_Brn_No      => J.Brn_No              );  
          Exception When Others Then                                                    
             RollBack;
             Raise_Application_Error(-20011,'Error When Insert Into Out Bills Tables , (Rt Sales)'||Chr(13)||SqlErrm);                                             
          End;         
     End If;
     --##-------------------------------------------------------------------------------------##--
       If J.Clc_Typ_No_Tax Is Not Null Then
         Insrt_Tax (P_Doc_Type => 5 , P_Doc_Ser => J.Rt_Bill_Ser);
        End If;      
        If J.POINT_TYP_NO Is Not Null Then
            Insrt_Point_Trns (P_Doc_Type => 5 , P_Doc_Ser => J.Rt_Bill_Ser);
        END IF; 
        If nvl(v_use_serialno,0)<>0 Then    
           Post_Serial (P_Doc_Ser => J.Rt_Bill_Ser, P_Doc_Type =>3); 
        End If;      
     --##-------------------------------------------------------------------------------------##--
     Begin
          Ars_Gnr_Pkg.Insrt_Crdt_Crd_From_Br ( P_Doc_Type        =>5
                                                  ,P_Doc_No          =>J.RT_Bill_no
                                                  ,P_Bill_Doc_Type   =>J.RT_Bill_Doc_Type
                                                  ,P_Doc_Ser         =>J.RT_Bill_Ser
                                                  ,P_Doc_Date        =>J.RT_Bill_Date
                                                  ,P_User_Id         =>J.Ad_U_id
                                                  ,P_A_Cy            =>j.Rt_Bill_Currency
                                                  ,P_Cash_No         =>J.Cash_No
                                                  ,P_C_Code          =>null
                                                  ,P_External_Post   =>85
                                                  ,Typ               =>'D');                                                 
    Exception When Others Then                                                    
       RollBack;
       Raise_Application_Error(-20015,'Ars_Gnr_Pkg.Insrt_Crdt_Crd_From_Br  = '||Chr(13)||'RT_Bill_Ser ='||J.rt_Bill_Ser ||Chr(13)||SqlErrm);                                               
    End; 
  --##-------------------------------------------------------------------------------------##--     

     Begin
        IAS_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 5                   ,
                                              G_Doc_Ser     => J.Rt_Bill_Ser       ,
                                              P_jv_type     => J.Rt_Bill_Doc_Type  ,
                                              P_doc_no      => J.Rt_Bill_No        ,
                                              P_Lang_no     => Nvl(V_Lang_no,1)    ,
                                              P_User_No     => J.Ad_U_Id           ,
                                              G_Post_Type   => 0                   );
     Exception When Others Then
         RollBack;
         Raise_Application_Error(-20012,'Error When Post Rt Bill , '||Chr(13)||SqlErrm);                                                   
     End;
     --##----------------------------------------------------------------------------------##--
      If V_Use_Out_Bills=1 Then
         BEGIN
           IAS_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 14                  ,
                                                  G_Doc_Ser     => V_Ret_Ser      ,
                                                  P_jv_type     => J.Rt_Bill_Doc_Type  ,
                                                  P_doc_no      => V_Ret_No       ,
                                                  P_Lang_no     => Nvl(V_Lang_no,1)    ,
                                                  P_User_No     => J.Ad_U_Id           ,
                                                  G_Post_Type   => 0                   );
         Exception When Others Then
             RollBack;
             Raise_Application_Error(-20013,'Error When Post REt Bill , '||Chr(13)||SqlErrm);                                                   
         End;
    End If;  
     --##----------------------------------------------------------------------------------##--                            
    End Loop; --(1)
--##-------------------------------------------------------------------------------------##--
    --## Update Ias_Rt_Bill_Mst_Br        
    Begin    
        Update Ias_Rt_Bill_Mst_Br Set Rt_Bill_post=1
         Where nvl(Rt_Bill_post,0)= 0                    
           And Exists (Select 1 From Ias_Rt_Bill_Mst_Br_Tmp Where Rt_Bill_Ser = Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser  And RowNum <=1  ) 
           And Exists (Select 1 From Ias_Rt_Bill_Mst Where Rt_Bill_Ser=Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser And RowNum<=1);
          
    Exception When Others Then
         RollBack;
         Raise_Application_Error(-20013,'Error When Update Rt_Bill_Post , '||Chr(13)||SqlErrm);                                                   
    End;                             
  End;
END Post_Rt_Sales_Detail; 


PROCEDURE Post_Rt_Sales_Sum (P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null) Is     
   V_Cnt              Number;
   V_StkCost          Number;
   V_Seq              Number;
   V_StkRate          Number;
   V_Cst              Number;
   V_Rt_BillAmt       Number;
   V_DIscAmt          Number;
   V_othramt          Number;
   V_Rt_BillRate      Number;
   V_CardAmt          Number;
   V_ChequeAmt        Number;
   V_DIsc_Mst         Number;
   V_DIsc_Dtl         Number;   
   V_VatAmt           Number;
   V_Rt_Bill_No       Number;
   V_Rt_Bill_Ser      Number;
   V_Ret_No           Number;
   V_Ret_Ser          Number;
   V_Out_No           Number;
   V_Out_Ser          Number;
   V_No               Number;
   V_Ser              Number;
   V_Py               Number;
   V_Rec              Number;   
   V_Wcode            Number;   
   V_wt_after         Number; 
   V_Lang_No          Number; 
   V_Use_Out_Bills    Number;
   V_Invs_Sr          Number; 
   V_Costing_Type     Number;
   V_Wtavg_Type       Number;
   V_Use_Itm_Attach   Number;
   V_Stkcost_Fraction Number;
   V_Allow_Enter_Zero_Cost Number;
   V_Disc_Mst_Vat       NUMBER;
   V_Use_Vat            NUMBER;
   V_CALC_VAT_AMT_TYPE  NUMBER;
   
Begin
--##-------------------------------------------------------------------------------------##--    
  If P_Lang_No Is Null Then    
    Begin
      Select Lang_No InTo V_Lang_No From Ias_Sys.Lang_Def Where Nvl(Flg_St,1)= 1 And Lang_Dflt=1 And Rownum<=1;
    Exception WHen Others Then
        V_Lang_No := 1;
    End;  
  ENd If;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      Select Use_Out_Bills,Invoicing_Serials_Sr,Costing_Type,Wtavg_Type,Use_Itm_Attach ,Stkcost_Fraction, NVL(Use_Vat,0) , NVL(V_CALC_VAT_AMT_TYPE,0)  
        InTo V_Use_Out_Bills,V_Invs_Sr,V_Costing_Type,V_Wtavg_Type,V_Use_Itm_Attach,V_Stkcost_Fraction, V_Use_Vat ,V_CALC_VAT_AMT_TYPE   
        From Ias_Para_AR,Ias_Para_Inv ,IAS_PARA_GEN   
       Where RowNum<=1;
  Exception WHen Others Then
    RollBack;
    Raise_Application_Error(-20001,'Error When Select From Para In Post_Rt_Sales_Detail '||Chr(13)||SqlErrm);
  End;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      If P_User_No<>1 Then
        Select Allow_Enter_Zero_Cost InTo V_Allow_Enter_Zero_Cost From Privilege_Fixed Where U_Id=P_User_No And RowNum<=1;
      End If;  
  Exception WHen Others Then
      RollBack;
      Raise_Application_Error(-20002,'Error When Select From Privilege_Fixed In Post_Rt_Sales_Detail'||Chr(13)||SqlErrm);
  End;
  ---------------------------------- ## Cursor Return Sales ## --------------------------------      
  Insert Into Ias_Rt_Bill_Mst_Br_Tmp (Rt_Bill_No,Rt_Bill_Ser) Select Rt_Bill_No , Rt_Bill_Ser 
                                                               From Ias_Rt_Bill_Mst_Br 
                                                              Where Rt_Bill_Doc_Type<>4 
                                                                And Nvl(Stand_By,0)=0 
                                                                And Nvl(Rt_Bill_Post,0)=0
                                                                And Exists(Select 1 From Ias_Rt_Bill_Dtl_Br Where Rt_Bill_Ser=Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser And Rownum<=1);
--##-------------------------------------------------------------------------------------##--   
    Declare
      Cursor SM Is Select   DIstinct   Decode(P_Year,0,2,P_Year) P_Year,
                                       Rt_Bill_Date,
                                       A_code,
                                       Cash_no,                
                                       Sr_Type,
                                       Rt_Bill_Doc_type,
                                       Rt_Bill_currency ,
                                       Clc_Typ_No_Tax,
                                       Clc_Vat_Price_Typ,
                                       w_code,
                                       Cc_Code,
                                       Pj_No,
                                       Actv_No,
                                       Rep_Code,
                                       Cash_Ac_Fcc,                                                   
                                       Cheque_No,
                                       Cheque_Due_Date,
                                       Ad_U_Id,
                                       Brn_No,
                                       Brn_Year,
                                       Cmp_No,                                     
                                       Brn_Usr,
                                       Doc_Brn_No
                                  From Ias_Rt_Bill_Mst_Br
                                 Where Exists(Select 1 From Ias_Rt_Bill_Mst_Br_Tmp Where Rt_Bill_Ser=Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser And RowNum<=1)
                                 Order By  Rt_Bill_Date,               
                                            Rt_Bill_currency ,               
                                            Ad_U_Id;
        Begin ---(11)
--##-------------------------------------------------------------------------------------##--    
    --## To Get Stock Rate           
     V_StkRate := Ias_Gen_Pkg.Get_Cur_rate( P_Acy => Ias_Gen_Pkg.Get_Stk_Cur );      
--##-------------------------------------------------------------------------------------##--    
  For j in SM Loop     -->> (1)    
     Begin          
       Begin
                  Select Sum(Bill_amt) ,
                         Sum(Nvl(Disc_amt,0)) ,
                         Sum(Nvl(Othr_amt,0)),
                         AVG(Rt_Bill_Rate) Rt_BillRate  ,                             
                         Sum(Nvl(Cheque_Amt,0)),
                         Sum(nvl(Disc_Amt_Mst,0)),
                         Sum(nvl(Disc_Amt_Mst_Vat,0)),
                         Sum(Nvl(Disc_Amt_Dtl,0)),
                         Sum(Nvl(Vat_Amt,0))
                    Into V_Rt_BillAmt, 
                         V_DIscAmt,
                         V_Othramt,
                         V_Rt_BillRate,                               
                         V_ChequeAmt,
                         V_Disc_Mst,
                         V_Disc_Mst_Vat,
                         V_Disc_Dtl,
                         V_VatAmt
                    From Ias_Rt_Bill_Mst_Br
            Where Exists(Select 1 From Ias_Rt_Bill_Mst_Br_Tmp Where Rt_Bill_Ser=Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser And RowNum<=1)
              and Nvl(Sr_Type,0)            = Nvl(j.Sr_Type,0)
              and Decode(P_Year,0,2,P_Year) = J.P_year
              and Rt_Bill_Date              = j.Rt_Bill_Date
              and Rt_Bill_currency          = j.Rt_Bill_currency
              and a_code                    = j.a_code
              and Nvl(Cash_no,0)            = Nvl(J.Cash_no,0)                                                                                     
              and Rt_Bill_Doc_type          = J.Rt_Bill_Doc_type
              and  Nvl(w_code,0)            = Nvl(J.w_code,0)
              and  Nvl(Cc_Code,'0')         = Nvl(J.Cc_Code,'0')
              and  Nvl(Pj_No,'0')           = Nvl(J.Pj_No,'0')
              and  Nvl(Actv_No,'0')         = Nvl(J.Actv_No,'0')
              and  Nvl(Cheque_No,'0')       = Nvl(J.Cheque_No,'0')
              and  Nvl(Cash_Ac_Fcc,'0')     = Nvl(J.Cash_Ac_Fcc,'0') 
              and  Nvl(Clc_Typ_No_Tax,0)    = Nvl(J.Clc_Typ_No_Tax,0)
              and  Nvl(Clc_Vat_Price_Typ,0)    = Nvl(J.Clc_Vat_Price_Typ,0)                           
              and  Nvl(Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
              and  Nvl(Rep_Code,'0')        = Nvl(J.Rep_Code,'0')
              and  Ad_U_Id                  = J.Ad_U_Id
              and  Doc_Brn_No               = Nvl(J.Doc_Brn_No,0)
              and  Brn_No                   = J.Brn_No
              and  Brn_Year                 = J.Brn_Year
              and  Cmp_No                   = J.Cmp_No
              and  Brn_Usr                  = J.Brn_Usr    ;                      
      Exception
         When Others Then
            RollBack;
            Raise_Application_Error(-20003,'Error When Select From Ias_Rt_Bill_Mst In Post Rt Sales Sum , '||Chr(13)||SqlErrm);    
      End;                       
      ----------------------------------------------------------------------------------
       --V_Rt_Bill_No := Get_Rt_Bill_No  ( V_Invs_Sr,J.sr_type,J.Cc_Code,J.Rt_Bill_doc_type,J.W_Code,J.Brn_NO);
       Begin
         V_Rt_Bill_No:=AR_DOC_SQ_PKG.GET_DOC_NO ( P_DOC_TYP       =>5,
                                                  P_PAY_TYP        =>J.Rt_Bill_Doc_type,    
                                                  P_BRN_YEAR       =>J.Brn_Year,
                                                  P_BRN_NO         =>J.Brn_No,
                                                  P_CC_CODE        =>J.Cc_Code,
                                                  P_W_CODE         =>J.W_Code,
                                                  P_TYP_NO        =>J.Sr_type,   
                                                  P_Sys_No        =>85,
                                                  P_Usr_No        =>j.ad_u_id,
                                                  P_Trmnl_No      => null    );     
       Exception When Others Then
            RollBack;
            Raise_Application_Error (-20001,' Err. In Get Rt Bill No ');  
       End ;
      ----------------------------------------------------------------------------------
     -- V_Rt_Bill_Ser := Get_Rt_Bill_Ser ( V_Invs_Sr,J.sr_type,J.Cc_Code,V_Rt_Bill_No,J.Rt_Bill_doc_type,J.W_Code,J.Brn_NO,J.Brn_Year);
       Begin
             V_Rt_Bill_Ser:=AR_DOC_SQ_PKG.GET_DOC_SRL (  P_DOC_TYP     =>5,
                                                          P_PAY_TYP       =>J.Rt_Bill_Doc_type,    
                                                          P_BRN_YEAR      =>J.brn_year,
                                                          P_BRN_NO        =>J.Brn_No,
                                                          P_CC_CODE       =>J.Cc_Code,
                                                          P_W_CODE        =>J.W_Code,
                                                          P_TYP_NO        =>J.Sr_type,
                                                          P_DOC_NO        =>V_Rt_Bill_No,
                                                          P_Sys_No        =>85,
                                                          P_Usr_No        =>j.ad_u_id,
                                                          P_Trmnl_No      => null  );    
       Exception When Others Then
           RollBack;
           Raise_Application_Error (-20001,' Err. In Get Rt Bill serial ');   
       End ;  
      ----------------------------------------------------------------------------------
      Insert Into Ias_Rt_Bill_Mst(  Rt_Bill_Doc_Type, 
                                    Rt_Bill_No, 
                                    Rt_Bill_Ser,
                                    P_Year, 
                                    Sr_Type,
                                    Rt_Bill_Date, 
                                    Rt_Bill_Currency,
                                    Rt_Bill_Rate, 
                                    Stock_Rate, 
                                    C_Code,
                                    C_Name, 
                                    A_Code, 
                                    Cheque_No, 
                                    Cheque_Amt, 
                                    Cheque_Due_Date, 
                                    Rt_Bill_Due_Date, 
                                    Rt_Bill_Post, 
                                    Disc_Amt, 
                                    Disc_Amt_Mst,
                                    DIsc_Amt_Mst_Vat, 
                                    Disc_Amt_Dtl, 
                                    Bill_Amt, 
                                    Vat_Amt, 
                                    Othr_Amt, 
                                    W_Code, 
                                    R_Code,
                                    Rep_Code, 
                                    Cash_No, 
                                    Ref_No,
                                    Cc_Code, 
                                    Pj_No,
                                    Actv_No,
                                    Classify_No, 
                                    Cash_Ac_Fcc,
                                    A_Desc, 
                                    Return_Res, 
                                    Processed,
                                    Comm_Per, 
                                    Pr_Rep,                                                 
                                    Ad_U_Id, 
                                    Ad_Date, 
                                    Up_U_Id, 
                                    Up_Date, 
                                    Unpost_U_Id, 
                                    Unpost_Date, 
                                    Brn_No, 
                                    Brn_Year, 
                                    Classify_Ser, 
                                    Post_U_Id, 
                                    Post_Date,                               
                                    Audit_Ref, 
                                    Audit_Ref_Desc, 
                                    Audit_Ref_U_Id, 
                                    Audit_Ref_Date, 
                                    External_Post, 
                                    Rt_Bill_Py,
                                    Cmp_No,
                                    Brn_Usr,
                                    Doc_Brn_No,                                    
                                    Clc_Typ_No_Tax,
                                    Clc_Vat_Price_Typ,
                                    DOC_PST_SQ,
                                    E_INVC_MTHD_NO)
                            Values( J.Rt_Bill_Doc_Type, 
                                    V_Rt_Bill_No, 
                                    V_Rt_Bill_Ser,                                                
                                    J.P_year, 
                                    J.Sr_Type,
                                    J.Rt_Bill_Date, 
                                    J.Rt_Bill_Currency,
                                    V_Rt_BillRate, 
                                    V_StkRate, 
                                    Null,
                                    Ias_Gen_Pkg.Get_Prompt(V_Lang_no,1924)||' '||J.Ad_U_Id, 
                                    J.A_Code, 
                                    J.Cheque_No, 
                                    V_ChequeAmt, 
                                    J.Cheque_Due_Date, 
                                    Null, 
                                    0, 
                                    Nvl(V_DIscAmt,0), 
                                    Nvl(V_DIsc_Mst,0),
                                    NVL(V_Disc_Mst_Vat,0), 
                                    Nvl(V_DIsc_Dtl,0), 
                                    Nvl(V_Rt_BillAmt,0), 
                                    Nvl(V_VatAmt,0), 
                                    Nvl(V_OthrAmt,0), 
                                    J.W_Code, 
                                    Null,
                                    Null, 
                                    J.Cash_No, 
                                    Null,
                                    J.Cc_Code, 
                                    J.Pj_No,
                                    J.Actv_No,
                                    Null, 
                                    J.Cash_Ac_Fcc,                                                
                                    Ias_Gen_Pkg.Get_Prompt(V_Lang_no,1924)||' '||J.Ad_U_Id, 
                                    Null, 
                                    Decode(V_Use_Out_Bills,1,1,0),
                                    Null, 
                                    Null,                                                 
                                    J.Ad_U_Id, 
                                    Ias_Gen_Pkg.Get_CurDate, 
                                    Null, 
                                    Null, 
                                    Null, 
                                    Null, 
                                    J.Brn_No, 
                                    J.Brn_Year, 
                                    Null, 
                                    Null, 
                                    Null,                               
                                    Null, 
                                    Null, 
                                    Null, 
                                    Null, 
                                    85, 
                                    Null,
                                    J.Cmp_No,
                                    J.Brn_Usr,
                                    J.Doc_Brn_No,
                                    J.Clc_Typ_No_Tax,
                                    J.Clc_Vat_Price_Typ,
                                    IAS_POSTING_PKG.GET_DOC_PST_SQ,
                                    Decode(Nvl(Ias_Brn_Pkg.Is_Brn_Use_E_Invc ( P_Brn_No => J.Brn_No),0),1,Gnr_Get_E_Invc_Actv_Mthd  ( P_Doc_Typ => 5,P_Sys_No => 85),Null) );
    Exception
     When Others Then
        RollBack;
        Raise_Application_Error(-20004,'Error When Insert Into Ias_Rt_Bill_Mst In Post Rt Sales Sum, '||Chr(13)||SqlErrm);    
    End; 
--##-------------------------------------------------------------------------------------##--                              
  If V_Use_Out_Bills=1 Then
        V_Ret_No  := Ias_Insrt_Out_Bills_Pkg.Get_Ret_No  ( P_Invs_sr       => V_Invs_sr , 
                                                           P_Sr_Type       => J.Sr_Type          ,
                                                           P_Cc_Code       => J.Cc_Code          ,
                                                           P_w_code        => J.w_Code           ,
                                                           P_bill_doc_type => J.Rt_bill_doc_type    ,
                                                           P_Brn_No        => J.Brn_No           );   
                                                           
        V_Ret_Ser := Ias_Insrt_Out_Bills_Pkg.Get_Ret_Ser ( P_ret_No        => V_Ret_No           ,
                                                           P_Sr_Type       => J.Sr_Type          ,
                                                           P_Invs_Sr       => V_Invs_sr ,
                                                           P_Cc_Code       => J.Cc_Code          ,
                                                           P_w_code        => J.w_code           ,
                                                           P_bill_doc_type => J.Rt_bill_doc_type ,
                                                           P_Brn_No        => J.Brn_No           ,
                                                           P_Brn_Year      => J.Brn_Year         );
  End If;  
--##-------------------------------------------------------------------------------------##--
  If V_Use_Out_Bills=0 Then
      V_No  := V_Rt_Bill_No;
      V_Ser := V_Rt_Bill_Ser;
  Else
      V_No  := V_Ret_No;
      V_Ser := V_Ret_Ser;
  End If;    
--##-------------------------------------------------------------------------------------##--        
    Begin
          IAS_Itm_Inv_Pkg.Insrt_Gr_Mst ( p_doctype  => 3,
                                         p_gr_no    => V_No,
                                         p_g_ser    => V_Ser,                                                                             
                                         p_doc_ser  => V_Rt_Bill_Ser,
                                         p_doc_date => J.rt_bill_date,
                                         p_a_code   => J.a_code,
                                         p_acy      => J.rt_bill_currency,
                                         p_c_code   => Null,
                                         p_acrate   => V_rt_billrate,
                                         p_stkrate  => V_stkrate,
                                         p_gramt    => V_Rt_billamt,
                                         p_pi_no    => V_Rt_Bill_No,
                                         p_cc_code  => J.Cc_Code,
                                         p_Pj_No    => J.Pj_No,
                                         p_Actv_No  => J.Actv_No,
                                         p_w_code   => J.W_Code,
                                         p_refno    => Null,
                                         p_desc     => Ias_Gen_Pkg.Get_Prompt(V_Lang_no,1924)||' '||J.Ad_U_Id,
                                         p_cflag    => 1,
                                         p_pur_type => Null,
                                         p_User_No  => J.Ad_U_Id,
                                         P_Brn_no   => J.Brn_no,
                                         P_Brn_Year => J.Brn_Year,
                                         P_Cmp_No   => J.Cmp_No,
                                         P_Brn_Usr  => J.Brn_Usr);
                                
             Exception
     When Others Then
        RollBack;
        Raise_Application_Error(-20005,'Error When Insert Into Gr_Note In Post Rt Sales Sum, '||Chr(13)||SqlErrm);    
    End;
--##-------------------------------------------------------------------------------------##--            
--## Other_Charges
    Insert_Other_Charges_Sr(  V_Rt_Bill_No,
                              j.Rt_Bill_doc_type,
                              V_Rt_Bill_Ser,
                              j.Rt_Bill_date,
                              j.Ad_U_id,
                              j.Rt_Bill_Currency,
                              j.Cash_No,
                              Null,
                              'S');
--##-------------------------------------------------------------------------------------##--    
  Declare
         Cursor BD Is Select   Sum(Ias_Rt_Bill_Dtl_Br.I_Qty)       I_qty,
                               Sum(Ias_Rt_Bill_Dtl_Br.P_Qty)       P_qty,
                               Sum(Ias_Rt_Bill_Dtl_Br.Free_Qty)    Free_qty,
                               Ias_Rt_Bill_Dtl_Br.I_Code           I_code,
                               Ias_Rt_Bill_Dtl_Br.Post_Code        Post_Code,
                               Ias_Rt_Bill_Dtl_Br.I_Price          I_price, 
                                Ias_Rt_Bill_Dtl_Br.I_price_Vat      I_price_Vat,  
                               Ias_Rt_Bill_Dtl_Br.Dis_amt          Dis_amt,                               
                               Ias_Rt_Bill_Dtl_Br.Dis_amt_Mst      Dis_Amt_Mst,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_amt_Mst_Vat,0)  Dis_amt_Mst_Vat,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Vat_Amt_Dis_Mst_Vat,0)  Vat_Amt_Dis_Mst_Vat,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_Per,0)      Dis_Per,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl,0)  Dis_Amt_Dtl,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl_Vat,0)  Dis_Amt_Dtl_Vat,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Vat_Amt_Dis_Dtl_Vat,0)  Vat_Amt_Dis_Dtl_Vat,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_Per2,0)     Dis_Per2,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl2,0) Dis_Amt_Dtl2,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl2_Vat,0)  Dis_Amt_Dtl2_Vat,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Vat_Amt_Dis_Dtl2_Vat,0)  Vat_Amt_Dis_Dtl2_Vat,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_Per3,0)     Dis_Per3,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl3,0) Dis_Amt_Dtl3,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl3_Vat,0)  Dis_Amt_Dtl3_Vat,
                               Nvl(Ias_Rt_Bill_Dtl_Br.Vat_Amt_Dis_Dtl3_Vat,0)  Vat_Amt_Dis_Dtl3_Vat,
                               Ias_Rt_Bill_Dtl_Br.Othr_amt         Othr_amt,
                               Ias_Rt_Bill_Dtl_Br.vat_amt          Vat_amt,
                               Ias_Rt_Bill_Dtl_Br.vat_Per          Vat_Per,
                               Ias_Rt_Bill_Dtl_Br.Itm_Unt           Itm_Unt,
                               Ias_Rt_Bill_Dtl_Br.P_size           P_size,
                               Ias_Rt_Bill_Dtl_Br.Expire_Date      Expire_Date,
                               Ias_Rt_Bill_Dtl_Br.Batch_No         Batch_No,
                               Ias_Rt_Bill_Dtl_Br.w_code           w_code,
                               Ias_Rt_Bill_Dtl_Br.Cc_Code          Cc_Code,
                               Ias_Rt_Bill_Mst_Br.Pj_No            Pj_No,
                               Ias_Rt_Bill_Mst_Br.Actv_No          Actv_No,
                               Ias_Rt_Bill_Mst_Br.Sr_Type          Sr_Type,        
                               Nvl(Ias_Rt_Bill_Dtl_Br.Use_Attch,0) Use_Attch,                         
                               Decode(P_Year,0,2,P_Year)           P_Year,
                               Ias_Rt_Bill_Mst_Br.a_code           a_code,
                               Ias_Rt_Bill_Mst_Br.cash_no          cash_no,                               
                               Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_type Rt_Bill_doc_type,
                               Ias_Rt_Bill_Mst_Br.Rt_Bill_DATE     Rt_Bill_date,                       
                               Ias_Rt_Bill_Mst_Br.Rt_Bill_currency Rt_Bill_currency,                              
                               Nvl(Ias_Rt_Bill_Dtl_Br.Service_Item,0) Service_Item,
                               Ias_Rt_Bill_Dtl_Br.Brn_No,
                               Ias_Rt_Bill_Dtl_Br.Brn_Year,
                               Ias_Rt_Bill_Dtl_Br.Cmp_No,
                           Ias_Rt_Bill_Dtl_Br.Brn_Usr
             From Ias_Rt_Bill_Mst_Br,Ias_Rt_Bill_Dtl_Br
           Where Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser         = Ias_Rt_Bill_Dtl_Br.Rt_Bill_Ser
             And Exists(Select 1 From Ias_Rt_Bill_Mst_Br_Tmp Where Rt_Bill_Ser=Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser And RowNum<=1)                 
             And Decode(P_Year,0,2,P_Year)              = J.P_year
             And Ias_Rt_Bill_Mst_Br.Rt_Bill_Date        = j.Rt_Bill_Date
             And Ias_Rt_Bill_Mst_Br.Rt_Bill_currency    = j.Rt_Bill_currency
             And Nvl(Ias_Rt_Bill_Mst_Br.Sr_Type,0)      = Nvl(j.Sr_Type,0)        
             And Ias_Rt_Bill_Mst_Br.a_code              = j.a_code
             And Ias_Rt_Bill_Mst_Br.Cash_no             = J.Cash_no                                                                                     
             And  Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_type    = J.Rt_Bill_Doc_type
             And Nvl(Ias_Rt_Bill_Mst_Br.w_code,0)       = Nvl(J.w_code,0)
             And Nvl(Ias_Rt_Bill_Mst_Br.Cc_Code,'0')    = Nvl(J.Cc_Code,'0')        
             And Nvl(Ias_Rt_Bill_Mst_Br.Pj_No,'0')      = Nvl(J.Pj_No,'0')
             And Nvl(Ias_Rt_Bill_Mst_Br.Actv_No,'0')      = Nvl(J.Actv_No,'0')
             And Nvl(Ias_Rt_Bill_Mst_Br.Cheque_No,'0')  = Nvl(J.Cheque_No,'0')
             And Nvl(Ias_Rt_Bill_Mst_Br.Cash_Ac_Fcc,'0')= Nvl(J.Cash_Ac_Fcc,'0')  
             and  Nvl(Ias_Rt_Bill_Mst_Br.Clc_Typ_No_Tax,0) = Nvl(J.Clc_Typ_No_Tax,0)
             and  Nvl(Ias_Rt_Bill_Mst_Br.Clc_Vat_Price_Typ,0) = Nvl(J.Clc_Vat_Price_Typ,0)
             and  Nvl(Ias_Rt_Bill_Mst_Br.Rep_Code,'0')   = Nvl(J.Rep_Code,'0')                          
             And Nvl(Ias_Rt_Bill_Mst_Br.Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
             And Ias_Rt_Bill_Mst_Br.Ad_U_Id             = J.Ad_U_Id
             And Ias_Rt_Bill_Mst_Br.Doc_Brn_No          = Nvl(J.Doc_Brn_No,0)
             And Ias_Rt_Bill_Mst_Br.Brn_No              = J.Brn_No
             And Ias_Rt_Bill_Mst_Br.Brn_Year            = J.Brn_Year
        Group by Ias_Rt_Bill_Dtl_Br.I_Code,
                 Ias_Rt_Bill_Dtl_Br.Post_Code,
                 Ias_Rt_Bill_Dtl_Br.I_Price, 
                 Ias_Rt_Bill_Dtl_Br.I_Price_Vat, 
                 Ias_Rt_Bill_Dtl_Br.Dis_amt,             
                 Ias_Rt_Bill_Dtl_Br.Dis_amt_Mst,
                 Ias_Rt_Bill_Dtl_Br.Dis_amt_Mst_Vat,
                 Ias_Rt_Bill_Dtl_Br.Vat_Amt_Dis_Mst_Vat,
                 Ias_Rt_Bill_Dtl_Br.Dis_Per,
                 Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl,
                 Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl_Vat,
                 Ias_Rt_Bill_Dtl_Br.Vat_Amt_Dis_Dtl_Vat,
                 Ias_Rt_Bill_Dtl_Br.Dis_Per2,
                 Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl2,
                 Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl2_Vat,
                 Ias_Rt_Bill_Dtl_Br.Vat_Amt_Dis_Dtl2_Vat,
                 Ias_Rt_Bill_Dtl_Br.Dis_Per3,
                 Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl3,
                 Ias_Rt_Bill_Dtl_Br.Dis_amt_Dtl3_Vat,
                 Ias_Rt_Bill_Dtl_Br.Vat_Amt_Dis_Dtl3_Vat,
                 Ias_Rt_Bill_Dtl_Br.Othr_amt,
                 Ias_Rt_Bill_Dtl_Br.vat_amt,
                 Ias_Rt_Bill_Dtl_Br.vat_Per,
                 Ias_Rt_Bill_Dtl_Br.Itm_Unt,
                 Ias_Rt_Bill_Dtl_Br.P_size,
                 Ias_Rt_Bill_Dtl_Br.Expire_Date,
                 Ias_Rt_Bill_Dtl_Br.Batch_No,
                 Ias_Rt_Bill_Dtl_Br.w_code,
                 Ias_Rt_Bill_Dtl_Br.Cc_Code,
                 Ias_Rt_Bill_Mst_Br.Pj_No,
                 Ias_Rt_Bill_Mst_Br.Actv_No,
                 Ias_Rt_Bill_Mst_Br.Sr_Type,
                 Nvl(Ias_Rt_Bill_Dtl_Br.Use_Attch,0),
                 Decode(P_Year,0,2,P_Year),
                 Ias_Rt_Bill_Mst_Br.a_code,
                 Ias_Rt_Bill_Mst_Br.cash_no,                               
                 Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_type,
                 Ias_Rt_Bill_Mst_Br.Rt_Bill_DATE,                       
                 Ias_Rt_Bill_Mst_Br.Rt_Bill_currency,                              
                 Nvl(Ias_Rt_Bill_Dtl_Br.Service_Item,0),
                 Ias_Rt_Bill_Dtl_Br.Brn_No,
                 Ias_Rt_Bill_Dtl_Br.Brn_Year,
                 Ias_Rt_Bill_Dtl_Br.Cmp_No,        
                 Ias_Rt_Bill_Dtl_Br.Brn_Usr                                    
       Order By  Ias_Rt_Bill_Mst_Br.Rt_Bill_Date,             
                 Ias_Rt_Bill_Mst_Br.Rt_Bill_Currency ;
  
--##-------------------------------------------------------------------------------------##--
    Begin --- (12)
         V_Rec := 0;
         For i in BD  Loop        -->> (2)
             V_Rec := V_Rec+1;
             Begin               
            --##-------------------------------------------------------------------------------------##--               
               If V_Costing_Type = 2 Then  -- WtAvrg
                   V_StkCost:=Ias_Itm_Pkg.get_grAnd_wtavg ( P_Wtavg_Type => V_Wtavg_Type ,
                                                            p_Icode      => i.i_code,
                                                            P_Wcode      => i.w_code)* nvl(i.p_size,1);
                 If  V_Costing_Type = 2 And V_Wtavg_Type In (2,3) Then
                          If  Nvl(V_Stkcost,0) = 0 Then
                                Begin 
                                  Select  W_Code
                                    Into  V_Wcode
                                   From Warehouse_Details
                                    Where Nvl(Main_Wcode,0) = 1  ;
                                Exception
                                     When Others Then
                                        V_Wcode := Null  ;
                                End ;
                                If V_Wcode Is Not Null  Then
                                            V_Stkcost := ias_itm_pkg.get_grand_wtavg( p_wtavg_type => V_Wtavg_Type ,
                                                                                      p_icode      => i.i_code     ,                                                                                      
                                                                                      p_wcode      => V_Wcode      )* Nvl(i.p_size,1);
                                                                           
                               
                                End If ;
                        End If ;

                  
                    End If ;                                     
                       Else -- FIFO
                         V_StkCost:=Last_Incoming_Price ( P_Wtavg_Type => V_Wtavg_Type ,
                                                          P_Icode      => i.I_code,
                                                          P_Psize      => i.p_size,
                                                          P_Wcode      => i.w_code,
                                                          P_Type       => 1);
               End If;                                                    
                    -------------------------------------------------------------------------------------------
             If Nvl(I.Service_Item,0)=0 And V_allow_enter_zero_cost = 0 And Nvl(V_StkCost,0) = 0  Then
                RollBack;
                Raise_Application_Error(-20005,'Error When Not Allow Enter Zero Cost In Post Rt Sales Sum'); 
             End If ;                    
            --##----------------------------------------------------------------------------------##--       
            Select Ias_Doc_Seq.NextVal InTo V_Seq From Dual;
            --##-------------------------------------------------------------------------------------##-- 
              Insert Into Ias_Rt_Bill_Dtl( Rt_Bill_Doc_Type, 
                                           Rt_Bill_No, 
                                           Rt_Bill_Ser, 
                                           Sr_Type,
                                           Bill_No, 
                                           Bill_Doc_Type, 
                                           Bill_Ser, 
                                           I_Code, 
                                           I_Qty, 
                                           Itm_Unt, 
                                           P_Size, 
                                           P_Qty, 
                                           I_Price,
                                           Stk_Cost, 
                                           W_Code, 
                                           Cc_Code, 
                                           Pj_No,
                                           Actv_No,
                                           Expire_Date, 
                                           Batch_No, 
                                           Free_Qty, 
                                           Service_Item, 
                                           Dis_Amt, 
                                           Dis_Amt_Mst,
                                           Dis_Amt_Mst_Vat,                                     
                                           Vat_Amt_Dis_Mst_Vat,
                                           Dis_Per, 
                                           Dis_Amt_Dtl,
                                           Dis_Amt_Dtl_Vat,  
                                           Vat_Amt_Dis_Dtl_Vat, 
                                           Dis_Per2, 
                                           Dis_Amt_Dtl2, 
                                           Dis_Amt_Dtl2_Vat,  
                                           Vat_Amt_Dis_Dtl2_Vat, 
                                           Dis_Per3, 
                                           Dis_Amt_Dtl3,
                                           Dis_Amt_Dtl3_Vat,    
                                           Vat_Amt_Dis_Dtl3_Vat, 
                                           Vat_Per, 
                                           Vat_Amt, 
                                           Othr_Amt, 
                                           Ret_Qty, 
                                           Ret_Free_Qty, 
                                           Use_Serialno, 
                                           Si_Rcrd_No, 
                                           Rcrd_No, 
                                           Item_Desc,
                                           Use_Attch,
                                           Rec_Attch,
                                           Brn_No, 
                                           Brn_Year, 
                                           Doc_Sequence, 
                                           External_Post,
                                           Cmp_No,
                                           Brn_Usr,
                                           Post_Code)
                                  Values(  j.Rt_Bill_Doc_Type, 
                                           V_Rt_Bill_No, 
                                           V_Rt_Bill_Ser, 
                                           J.Sr_Type,
                                           Null, 
                                           Null, 
                                           Null, 
                                           I.I_Code, 
                                           I.I_Qty, 
                                           I.Itm_Unt, 
                                           I.P_Size, 
                                           I.P_Qty, 
                                           I.I_Price,
                                           V_StkCost, 
                                           I.W_Code, 
                                           I.Cc_Code,
                                           I.Pj_No, 
                                           I.Actv_No,  
                                           I.Expire_Date, 
                                           I.Batch_No, 
                                           I.Free_Qty, 
                                           I.Service_Item, 
                                           I.Dis_Amt, 
                                           I.Dis_Amt_Mst,
                                           I.Dis_Amt_Mst_Vat,                                     
                                           I.Vat_Amt_Dis_Mst_Vat,
                                           I.Dis_Per, 
                                           I.Dis_Amt_Dtl,
                                           I.Dis_Amt_Dtl_Vat,  
                                           I.Vat_Amt_Dis_Dtl_Vat, 
                                           I.Dis_Per2, 
                                           I.Dis_Amt_Dtl2, 
                                           I.Dis_Amt_Dtl2_Vat,  
                                           I.Vat_Amt_Dis_Dtl2_Vat, 
                                           I.Dis_Per3, 
                                           I.Dis_Amt_Dtl3,
                                           I.Dis_Amt_Dtl3_Vat,    
                                           I.Vat_Amt_Dis_Dtl3_Vat,
                                           I.Vat_Per, 
                                           I.Vat_Amt, 
                                           I.Othr_Amt,  
                                           Decode(V_Use_Out_Bills,1,I.I_Qty,0),
                                           Decode(V_Use_Out_Bills,1,I.Free_Qty,0),
                                           Null, 
                                           Null, 
                                           V_Rec, 
                                           Null,
                                           I.Use_Attch, 
                                           V_Rec,
                                           I.Brn_No, 
                                           I.Brn_Year, 
                                           V_Seq, 
                                           85,
                                           I.Cmp_No,
                                           I.Brn_Usr,
                                           I.Post_Code);
              Exception
                  When Others Then                  
                    RollBack;
                    Raise_Application_Error(-20006,'Error When Insert Into Ias_Rt_Bill_Dtl Sum '||Chr(13)||SqlErrm);
              End; 
              
               If V_Use_Itm_Attach=1 And I.Use_Attch=1 Then                  
                      Begin
                          Insert InTo Ias_Itm_Attach_Movement( I_Code, Itm_Unt, P_Size, 
                                                               Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                               Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                               Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                               Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                               W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                               R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                               Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Date, A_Cy, 
                                                               Ac_Rate, Stk_Rate, I_Price, Dis_Amt, I_Cost, Stk_Cost, Vat_Amt, 
                                                               V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                               Cmp_No, Brn_No, Brn_Year,  Brn_Usr, Othr_Amt)
                                                        Select I_Code, Itm_Unt, P_Size, 
                                                               Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                               Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                               Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,V_Rec, 
                                                               Attch_Note, Doc_Type, Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_Type, V_Rt_Bill_No, 
                                                               V_Rt_Bill_Ser, Ias_Itm_Attach_Movement_Br.W_Code, Bill_Cost, V_Rec, 
                                                               In_Out, Ias_Itm_Attach_Movement_Br.Cc_Code,Ias_Itm_Attach_Movement_Br.Pj_No,
                                                               Ias_Itm_Attach_Movement_Br.Actv_No, Ias_Rt_Bill_Mst_Br.Rep_Code, 
                                                               Ias_Itm_Attach_Movement_Br.R_Code, Ias_Rt_Bill_Mst_Br.C_Code, Expire_Date, 
                                                               Batch_No, Sum(nvl(I_Qty,0)),  Sum(nvl(P_Qty,0)), 
                                                               Sum(nvl(Free_Qty,0)), Sum(nvl(Pf_Qty,0)), RowNum, 85,Doc_Date, A_Cy, 
                                                               V_Rt_BillRate, V_StkRate, I.I_Price, Dis_Amt, V_StkCost, V_StkCost, 
                                                               Ias_Itm_Attach_Movement_Br.Vat_Amt, V_Code, Rt_Type, 
                                                               Ias_Rt_Bill_Mst_Br.Ad_U_Id, Ias_Rt_Bill_Mst_Br.Ad_Date, 
                                                               Ias_Rt_Bill_Mst_Br.Up_U_Id, Ias_Rt_Bill_Mst_Br.Up_Date, 
                                                               Ias_Rt_Bill_Mst_Br.Cmp_No,Ias_Rt_Bill_Mst_Br.Brn_No,
                                                               Ias_Rt_Bill_Mst_Br.Brn_Year,--Ias_Rt_Bill_Mst_Br.Brn_Ser, 
                                                               Ias_Rt_Bill_Mst_Br.Brn_Usr, Ias_Itm_Attach_Movement_Br.Othr_Amt
                                                          From Ias_Rt_Bill_Mst_Br,Ias_Itm_Attach_Movement_Br
                                                         Where Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser        = Ias_Itm_Attach_Movement_Br.Doc_Ser
                                                          and  Ias_Itm_Attach_Movement_Br.Doc_Type   = 3
                                                          and  Ias_Itm_Attach_Movement_Br.i_code     = i.i_code 
                                                          And Exists(Select 1 From Ias_Rt_Bill_Mst_Br_Tmp Where Rt_Bill_Ser=Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser And RowNum<=1)     
                                                          and  Ias_Rt_Bill_Mst_Br.Rt_Bill_Date       = j.Rt_Bill_Date
                                                          and  Ias_Rt_Bill_Mst_Br.Rt_Bill_currency   = j.Rt_Bill_currency
                                                          and  Ias_Rt_Bill_Mst_Br.a_code             = j.a_code
                                                          and  nvl(Ias_Rt_Bill_Mst_Br.Cash_no,0)     = nvl(J.Cash_no,0)
                                                          and  nvl(Ias_Rt_Bill_Mst_Br.Sr_Type,0)     = nvl(J.Sr_Type,0)
                                                          and  Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_type   = J.Rt_Bill_Doc_type
                                                          and  Nvl(Ias_Rt_Bill_Mst_Br.w_code,0)      = Nvl(J.w_code,0)
                                                          and  Nvl(Ias_Rt_Bill_Mst_Br.Cc_Code,'0')   = Nvl(J.Cc_Code,'0')
                                                          and  Nvl(Ias_Rt_Bill_Mst_Br.Pj_No,'0')     = Nvl(J.Pj_No,'0')
                                                          and  Nvl(Ias_Rt_Bill_Mst_Br.Actv_No,'0')   = Nvl(J.Actv_No,'0')                                                                                                                                                                                                                
                                                          and  Nvl(Ias_Rt_Bill_Mst_Br.Cheque_No,'0') = Nvl(J.Cheque_No,'0')
                                                          and  Nvl(Ias_Rt_Bill_Mst_Br.Cash_Ac_Fcc,'0') = Nvl(J.Cash_Ac_Fcc,'0')  
                                                          and  Nvl(Ias_Rt_Bill_Mst_Br.Rep_Code,'0')  = Nvl(J.Rep_Code,'0')                        
                                                          and  Nvl(Ias_Rt_Bill_Mst_Br.Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
                                                          and  Ias_Rt_Bill_Mst_Br.Ad_U_Id            = J.Ad_U_Id
                                                          and  Ias_Rt_Bill_Mst_Br.Brn_No             = J.Brn_No
                                                          and  Ias_Rt_Bill_Mst_Br.Doc_Brn_No         = Nvl(J.Doc_Brn_No,0)
                                                          and  Ias_Rt_Bill_Mst_Br.Brn_Year           = J.Brn_Year
                                                          and  Ias_Rt_Bill_Mst_Br.Cmp_No             = J.Cmp_No
                                                          and  Ias_Rt_Bill_Mst_Br.Brn_Usr            = J.Brn_Usr    
                                                     Group by  I_Code, Itm_Unt, P_Size, 
                                                               Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                               Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                               Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,
                                                               Attch_Note, Doc_Type, Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_Type, 
                                                               Ias_Itm_Attach_Movement_Br.W_Code, Bill_Cost,In_Out, 
                                                               Ias_Itm_Attach_Movement_Br.Cc_Code,
                                                               Ias_Itm_Attach_Movement_Br.Pj_No,
                                                               Ias_Itm_Attach_Movement_Br.Actv_No,Ias_Rt_Bill_Mst_Br.Rep_Code, 
                                                               Ias_Itm_Attach_Movement_Br.R_Code, Ias_Rt_Bill_Mst_Br.C_Code, 
                                                               Expire_Date, Batch_No,Doc_Date, A_Cy, 
                                                               I.I_Price, Dis_Amt,Ias_Itm_Attach_Movement_Br.Vat_Amt, 
                                                               V_Code, Rt_Type, Ias_Rt_Bill_Mst_Br.Ad_U_Id, Ias_Rt_Bill_Mst_Br.Ad_Date, Ias_Rt_Bill_Mst_Br.Up_U_Id, Ias_Rt_Bill_Mst_Br.Up_Date, 
                                                               Ias_Rt_Bill_Mst_Br.Cmp_No, Ias_Rt_Bill_Mst_Br.Brn_No, Ias_Rt_Bill_Mst_Br.Brn_Year, Ias_Rt_Bill_Mst_Br.Brn_Usr, Ias_Itm_Attach_Movement_Br.Othr_Amt,
                                                               Ias_Rt_Bill_Mst_Br.Pj_No,
                                                               Ias_Rt_Bill_Mst_Br.Sr_Type,
                                                               Ias_Rt_Bill_Mst_Br.a_code,
                                                               Ias_Rt_Bill_Mst_Br.cash_no,                               
                                                               Ias_Rt_Bill_Mst_Br.Rt_Bill_Doc_type,
                                                               Ias_Rt_Bill_Mst_Br.Rt_Bill_DATE,                       
                                                               Ias_Rt_Bill_Mst_Br.Rt_Bill_currency,                                                              
                                                               Ias_Rt_Bill_Mst_Br.Brn_No,
                                                               Ias_Rt_Bill_Mst_Br.Brn_Year,                                    
                                                               Ias_Rt_Bill_Mst_Br.Cmp_No,
                                                               Ias_Rt_Bill_Mst_Br.Brn_Usr;
                        Exception When Others Then                                                    
                           RollBack;
                           Raise_Application_Error(-20008,'Error In Insert InTo Ias_Itm_Attach_Movement (Rt Sales Sum)'||Chr(13)||SqlErrm);                                                  
                        End;                     
            End If;        
--##-------------------------------------------------------------------------------------##--
            --## Calc_WatAvg                
            Begin    
              V_Wt_After := calc_wtavg_cost(p_cost_type  => V_Costing_Type     ,
                                            p_wtavg_type => V_Wtavg_Type       ,
                                            p_icode      => i.i_code                    ,
                                            p_iqty       => i.i_qty                     ,
                                            P_Frqty      => Nvl(i.free_qty,0)           ,
                                            p_icost      => Nvl(V_stkcost,0)              ,
                                            p_psize      => i.p_size                    ,
                                            p_wcode      => i.w_code                    ,
                                            P_Frc_No     => V_Stkcost_Fraction ,
                                            P_brn_no     => J.brn_no                    ,
                                            P_brn_year   => J.brn_year                  ,
                                            P_Cmp_No     => J.Cmp_No                    ,                                                                        
                                            P_Brn_Usr    => J.Brn_Usr                   );
            Exception When Others Then                                                    
               RollBack;
               Raise_Application_Error(-20009,'Error In Calc calc_wtavg_cost (Rt Sales Sum)'||Chr(13)||SqlErrm);                                                  
            End;      
--##-------------------------------------------------------------------------------------##--
           If Nvl(I.Service_Item,0)=0 Then
                   Begin
                       IAS_Itm_Inv_Pkg.Insrt_Gr_Dtl (   p_doctype       => 3,
                                                        p_gr_no         => V_No,
                                                        p_g_ser         => V_Ser,
                                                        p_doc_ser       => V_Rt_Bill_Ser,
                                                        p_DocSeq        => V_Seq,
                                                        p_doc_date      => J.rt_bill_date,
                                                        p_acy           => J.rt_bill_currency,
                                                        p_acrate        => V_rt_billrate,
                                                        p_stkrate       => V_stkrate,
                                                        p_pi_no         => V_Rt_Bill_No,                                                                    
                                                        p_pur_type      => 2,
                                                        p_w_code        => nvl(J.W_Code,I.w_code),
                                                        p_cc_code       => nvl(J.Cc_Code,I.Cc_Code),
                                                        p_Pj_No         => nvl(J.Pj_No,I.Pj_No),
                                                        p_Actv_No       => nvl(J.Actv_No,I.Actv_No),
                                                        p_icode         => I.i_code,
                                                        p_iqty          => I.i_qty,
                                                        p_freeqty       => I.free_qty,
                                                        p_Itm_Unt       => I.Itm_Unt,
                                                        p_psize         => I.p_size,
                                                        p_iprice        => I.i_price,
                                                        p_cprice        => (V_stkcost*V_stkrate)/V_rt_billrate,
                                                        p_stkcost       => V_stkcost,                                                                            
                                                        p_wtavg_before  => V_stkcost/Nvl(i.p_size,1),
                                                        p_wtavg_after   => Nvl(V_wt_after,0)                ,
                                                        p_vatper        => I.vat_per,
                                                        p_vatamt        => I.vat_amt,
                                                        p_disamt        => i.dis_amt,
                                                        p_expdate       => To_Date(I.Expire_date,'DD/MM/YYYY'),
                                                        p_batchno       => I.Batch_no,
                                                        p_rcrdno        => V_rec,
                                                        p_use_serial    => Null,
                                                        p_Brn_no        => J.Brn_no,
                                                        p_Brn_Year      => J.Brn_Year,
                                                        P_Cmp_No        => J.Cmp_No,
                                                        P_Brn_Usr       => J.Brn_Usr);                                                
        
                   Exception When Others Then                                                    
                       RollBack;
                       Raise_Application_Error(-20008,'Error In Insert InTo Gr_Detail (Rt Sales Sum)'||Chr(13)||SqlErrm);                                                  
                    End;
            
--##-------------------------------------------------------------------------------------##--
--## Insert Into Item_movement        
                 Begin
                 IAS_Itm_Inv_Pkg.Insrt_Item_Move (  p_DocType     => 3 ,
                                                    p_billDocType => J.rt_bill_doc_type ,
                                                    p_DocNo       => V_Rt_Bill_No,
                                                    p_ICode       => I.i_code ,
                                                    p_Iqty        => I.i_qty ,
                                                    p_Freeqty     => I.Free_qty ,
                                                    p_Itm_Unt     => I.Itm_Unt ,
                                                    p_PSize       => I.P_size ,
                                                    p_idate       => J.rt_bill_date,
                                                    p_iprice      => I.i_price,
                                                    p_WCode       => I.w_code ,
                                                    p_stkcost     => V_stkcost ,
                                                    p_vatamt      => I.vat_amt ,
                                                    p_disamt      => I.dis_amt ,
                                                    p_acy         => J.rt_bill_Currency ,
                                                    p_ac_rate     => V_rt_billrate ,
                                                    p_stk_rate    => V_stkrate ,
                                                    p_Cc_Code     => nvl(J.Cc_Code ,I.Cc_Code ),
                                                    p_Pj_No       => nvl(J.Pj_No ,I.Pj_No ),
                                                    p_Actv_No     => nvl(J.Actv_No ,I.Actv_No ),
                                                    p_c_code      => Null ,
                                                    p_adesc       => Ias_Gen_Pkg.Get_Prompt(V_Lang_no,1924)||' '||J.Ad_U_Id ,
                                                    p_ExpDate     => To_Date(I.Expire_date,'DD/MM/YYYY'),
                                                    p_BatchNo     => I.Batch_No,
                                                    p_RcrdNo      => V_Rec,
                                                    p_refno       => Null,
                                                    p_DocSer      => V_Rt_Bill_Ser,
                                                    p_DocSeq      => V_Seq,
                                                    p_outno       => V_Ret_no,
                                                    p_outgrser    => V_Ret_ser,
                                                    p_rt_type     => 2,
                                                    p_inout       => 1,
                                                    p_ad_date     => Ias_Gen_Pkg.Get_CurDate, 
                                                    p_up_date     => Null,
                                                    P_Brn_no      => J.Brn_no,
                                                    P_Brn_Year    => J.Brn_Year,
                                                    P_Cmp_No      => J.Cmp_No,
                                                    P_Brn_Usr     => J.Brn_Usr);
                Exception When Others Then                                                    
                   RollBack;
                   Raise_Application_Error(-20009,'Error In Insert InTo Item_Movement (Rt Sales Sum)'||Chr(13)||SqlErrm);                                                  
                End;
        End If;
        --##-------------------------------------------------------------------------------------##-----------        
      End Loop; --(2)
     End; --(12)
--##-------------------------------------------------------------------------------------##--
   If V_Use_Out_Bills=1 Then
      If J.P_Year=0 Then
         V_Py :=2;
      Else
         V_Py := J.P_Year;
         End If;    
            Begin
              Ias_Insrt_Out_Bills_Pkg.Insrt_Ret_Bills ( P_Invs_Sr     => V_Invs_Sr             , 
                                                        P_Pyear       => V_Py                  ,
                                                        P_Doc_Ser     => V_Rt_Bill_Ser         ,                                                        
                                                        P_Ret_No      => V_Ret_No              ,
                                                        P_Ret_Ser     => V_Ret_Ser             ,
                                                        P_Out_No      => V_Out_No              ,
                                                        P_Out_Ser     => V_Out_Ser             ,
                                                        P_Extrnl_Post => 85                    , 
                                                        P_Lang_No     => V_Lang_No             ,
                                                        P_Brn_No      => J.Brn_No              );
        Exception When Others Then                                                    
           RollBack;
           Raise_Application_Error(-20009,'Error In Insrt_Ret_Bills (Rt Sales Sum)'||Chr(13)||SqlErrm);                                                  
        End;         
      End If;    
--##-------------------------------------------------------------------------------------##--
 If V_Use_Vat=1 Then  
      
     Begin
        Insert Into Gnr_Tax_Itm_Movmnt (Doc_No, 
                                                              Doc_Ser, 
                                                              Doc_Date,
                                                              Doc_Type,
                                                              Bill_Doc_Type,
                                                              Doc_Jv_Type,                          
                                                            Tax_No,
                                                            Clc_Typ_No,
                                                            Agncy_No,
                                                            I_Code, 
                                                            Itm_Unt,
                                                            P_Size,                                   
                                                            A_Code, 
                                                            A_Cy, 
                                                            Ac_Rate, 
                                                            Stk_Rate,
                                                            I_Price,
                                                            Disc_Amt, 
                                                            Tax_Prcnt, 
                                                            Tax_Amt,
                                                            Tax_Amt_L, 
                                                            I_Qty, 
                                                            Free_Qty, 
                                                            Stk_Cost,
                                                            W_Code, 
                                                            Cc_Code,
                                                            Pj_No, 
                                                            Actv_No, 
                                                            Rcrd_No, 
                                                            Doc_Sequence, 
                                                            External_Post, 
                                                            Ref_No,
                                                            Cmp_No, Brn_No,Brn_Year, Brn_Usr)
                                                   Select D.Rt_Bill_No, 
                                                              D.Rt_Bill_Ser, 
                                                              Bm.Rt_Bill_Date,
                                                              M.Doc_Type, 
                                                              Bm.Rt_Bill_Doc_Type,
                                                              M.Doc_Jv_Type,                           
                                                                  M.Tax_No, 
                                                                  M.Clc_Typ_No, 
                                                                  M.Agncy_No, 
                                                                  M.I_Code, 
                                                                  M.Itm_Unt, 
                                                                  M.P_Size,                              
                                                                  M.A_Code, 
                                                                  M.A_Cy, 
                                                                  Bm.Rt_Bill_Rate,
                                                                  Bm.Stock_Rate,
                                                                  Nvl(D.I_Price,0) I_Price,
                                                                  Nvl(D.Dis_Amt,0) Disc_Amt, 
                                                                  M.Tax_Prcnt Tax_Prcnt, 
                                                                  (Decode(V_CALC_VAT_AMT_TYPE,1,( Nvl(D.I_Price,0)*m.Tax_Prcnt)/100,((Nvl(D.I_Price,0)-Nvl(D.Dis_Amt,0))*m.Tax_Prcnt)/100)) Tax_Amt,
                                                                  (Decode(V_CALC_VAT_AMT_TYPE,1,( Nvl(D.I_Price,0)*m.Tax_Prcnt)/100,((Nvl(D.I_Price,0)-Nvl(D.Dis_Amt,0))*m.Tax_Prcnt)/100)*Nvl(m.Ac_Rate,1)) Tax_Amt_L,
                                                                  Sum(Nvl(M.I_Qty,0)) I_Qty,
                                                                  Sum(Nvl(M.Free_Qty,0)) Free_Qty,
                                                                  Nvl(D.Stk_Cost,0),
                                                                  M.W_Code, 
                                                                  M.Cc_Code,
                                                                  M.Pj_No, 
                                                                  M.Actv_No,
                                                                  D.Rcrd_No, 
                                                                        D.Doc_Sequence,
                                                                  M.External_Post,
                                                                  DECODE(M.External_Post,85,'LGHT',70,'DTS',M.REF_NO) ,
                                                                  M.Cmp_No,
                                                                  M.Brn_No,
                                                                  M.Brn_Year, 
                                                                  M.Brn_Usr                              
                                                           From Ias_Rt_Bill_Mst_Br Bm,Ias_Rt_Bill_Dtl d,Gnr_Tax_Itm_Movmnt_Br M
                                                                   Where Bm.Rt_Bill_Ser        = M.Doc_Ser
                                                                    and  M.I_Code              = D.I_Code
                                                    and  M.Itm_Unt             = D.Itm_Unt
                                                    and  M.W_Code              = D.W_Code
                                                    And  D.Rt_Bill_Ser         = V_RT_BILL_SER
                                                                    and  M.Doc_Type            = 5
                                                                    and  Bm.Rt_bill_doc_type   <> 4
                                                                    and  Bm.Rt_bill_post       = 0
                                                                and  Bm.Rt_Bill_Date       = j.Rt_Bill_Date
                                                               -- And Nvl(Bm.W_Code,0) Between Nvl(V_F_Wcode,Nvl(Bm.W_Code,0)) And Nvl(V_T_Wcode,Nvl(Bm.W_Code,0))
                                                                and  Bm.Rt_bill_currency      = j.Rt_bill_currency
                                                                and  Bm.a_code             = j.a_code
                                                                and  nvl(Bm.Cash_no,0)     = nvl(J.Cash_no,0)
                                                                and  nvl(Bm.Sr_Type,0)     = nvl(J.Sr_Type,0)
                                                                and  Bm.Rt_Bill_Doc_type   = J.Rt_Bill_Doc_type
                                                                and  Nvl(Bm.w_code,0)      = Nvl(J.w_code,0)
                                                                and  Nvl(Bm.Cc_Code,'0')   = Nvl(J.Cc_Code,'0')
                                                                and  Nvl(Bm.Pj_No,'0')     = Nvl(J.Pj_No,'0')        
                                                                and  Nvl(Bm.Actv_No,'0')   = Nvl(J.Actv_No,'0')
                                                                and  Nvl(Bm.Rep_Code,'0')  = Nvl(J.Rep_Code,'0')              
                                                                and  Nvl(Bm.Cheque_No,'0')   = Nvl(J.Cheque_No,'0')
                                                                and  Nvl(Bm.Cash_Ac_Fcc,'0') = Nvl(J.Cash_Ac_Fcc,'0')                          
                                                                and  Bm.Clc_Typ_No_Tax      = Nvl(J.Clc_Typ_No_Tax,0)
                                                                and  Nvl(Bm.Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
                                                                and  Bm.Ad_U_Id            = J.Ad_U_Id
                                                                and  Bm.Doc_Brn_No         = Nvl(J.Doc_Brn_No,0)    
                                                                and  Nvl(D.I_Price,0)      = Nvl(M.I_Price,0)
                                                                and  Nvl(D.Dis_Amt,0)      = Nvl(M.Disc_Amt,0)
                                                                And  Nvl(D.Vat_Amt,0)      >0  
                                                                and  Bm.Brn_No             = J.Brn_No
                                                                and  Bm.Brn_Year           = J.Brn_Year
                                                                and  Bm.Cmp_No             = J.Cmp_No
                                                                and  Bm.Brn_Usr               = J.Brn_Usr 
                                               Group By D.Rt_Bill_No, 
                                                              D.Rt_Bill_Ser, 
                                                              Bm.Rt_Bill_Date,
                                                              M.Doc_Type, 
                                                              Bm.Rt_Bill_Doc_Type,
                                                              M.Doc_Jv_Type,                           
                                                                  M.Tax_No, 
                                                                  M.Clc_Typ_No, 
                                                                  M.Agncy_No, 
                                                                  M.I_Code, 
                                                                  M.Itm_Unt, 
                                                                  M.P_Size,                              
                                                                  M.A_Code, 
                                                                  M.A_Cy, 
                                                                  Bm.Rt_Bill_Rate,
                                                                  Bm.Stock_Rate,
                                                                  Nvl(D.I_Price,0),
                                                                  Nvl(D.Dis_Amt,0), 
                                                                  M.Tax_Prcnt, 
                                                                  Nvl(D.Stk_Cost,0),
                                                                  m.Ac_Rate,
                                                                  M.W_Code, 
                                                                  M.Cc_Code,
                                                                  M.Pj_No, 
                                                                  M.Actv_No,
                                                                  D.Rcrd_No, 
                                                                        D.Doc_Sequence,
                                                                  M.Cmp_No,
                                                                  M.Brn_No,
                                                                  M.Brn_Year, 
                                                                  M.Brn_Usr        ;
                                                                  
            Exception When Others Then                                                    
                  rollback;
                Raise_Application_Error (-20001,'Error When INSERT  Gnr_Tax_Itm_Movmnt, (Rt Sales) ,'||SqlErrm);                                              
            End;
      End If;   
--##-------------------------------------------------------------------------------------##-- 
 Begin
        Insert Into Ias_Point_Calc_Trns(Trns_Date, Cust_Code, Mobile_No, Point_Typ_No, Bill_No, Rt_Bill_No, Doc_Amt, A_Cy, Point_Cnt, Trns_Type, Machine_No, 
                                          Expire_Date, Bill_Amt, External_Post, Doc_No, Doc_Srl, Doc_Typ, Ac_Rate, Point_Amt,Ad_U_Id, Ad_Date, Up_U_Id, 
                                          Up_Date, Up_Cnt, Cmp_No, Brn_No, Brn_Year, Brn_Usr)
                                   Select T.Trns_Date, T.Cust_Code, T.Mobile_No, T.Point_Typ_No, Null, V_RT_BILL_NO, T.Doc_Amt, T.A_Cy, T.Point_Cnt, T.Trns_Type,
                                          T.Machine_No, T.Expire_Date, T.Bill_Amt, T.External_Post, V_RT_BILL_NO, V_RT_BILL_SER, T.Doc_Typ, T.Ac_Rate, T.Point_Amt,T.Ad_U_Id, 
                                          T.Ad_Date, T.Up_U_Id, T.Up_Date, T.Up_Cnt, T.Cmp_No, T.Brn_No, T.Brn_Year, T.Brn_Usr
                                     From Ias_Rt_Bill_Mst_Br Bm, Ias_Point_Calc_Trns_Br T
                                    Where Bm.Rt_Bill_Ser         = T.Doc_Srl
                                      And T.Doc_Typ              = 5 
                                      And T.Trns_Type           In (1,2)
                                     -- And Nvl(Bm.W_Code,0) Between Nvl(V_F_Wcode,Nvl(Bm.W_Code,0)) And Nvl(V_T_Wcode,Nvl(Bm.W_Code,0))
                                      And  Bm.Rt_Bill_Ser        = V_RT_BILL_SER
                                      And  Bm.Rt_Bill_Doc_Type   <> 4
                                      And  Bm.Rt_Bill_Post       = 0
                                      And  Bm.Rt_Bill_Date       = J.Rt_Bill_Date
                                      And  Bm.Rt_Bill_Currency   = J.Rt_Bill_Currency
                                      And  Bm.A_Code             = J.A_Code
                                      And  Nvl(Bm.Cash_No,0)     = Nvl(J.Cash_No,0)
                                      And  Nvl(Bm.Sr_Type,0)     = Nvl(J.Sr_Type,0)
                                      And  Bm.Rt_Bill_Doc_Type   = J.Rt_Bill_Doc_Type
                                      And  Nvl(Bm.W_Code,0)      = Nvl(J.W_Code,0)
                                      And  Nvl(Bm.Cc_Code,'0')   = Nvl(J.Cc_Code,'0')
                                      And  Nvl(Bm.Pj_No,'0')     = Nvl(J.Pj_No,'0')        
                                      And  Nvl(Bm.Actv_No,'0')   = Nvl(J.Actv_No,'0')
                                      And  Nvl(Bm.Rep_Code,'0')  = Nvl(J.Rep_Code,'0')              
                                      And  Nvl(Bm.Cheque_No,'0') = Nvl(J.Cheque_No,'0')
                                      And  Nvl(Bm.Cash_Ac_Fcc,'0') = Nvl(J.Cash_Ac_Fcc,'0')                          
                                      And  Nvl(Bm.Cheque_Due_Date,'01/01/1900') = Nvl(J.Cheque_Due_Date,'01/01/1900')
                                      And  Bm.Ad_U_Id            = J.Ad_U_Id
                                      And  Bm.Doc_Brn_No         = Nvl(J.Doc_Brn_No,0)
                                      And  Bm.Clc_Typ_No_Tax     = Nvl(J.Clc_Typ_No_Tax,0)
                                      And  Bm.Brn_No             = J.Brn_No
                                      And  Bm.Brn_Year           = J.Brn_Year
                                      And  Bm.Cmp_No             = J.Cmp_No
                                      And  Bm.Brn_Usr            = J.Brn_Usr; 
                                                                  
        Exception When Others Then                                                    
            rollback;
            Raise_Application_Error (-20001,'Error When INSERT Ias_Point_Calc_Trns, (Rt Sales) ,'||SqlErrm);                                               
        End;  
--##-------------------------------------------------------------------------------------##-- 
--##-------------------------------------------------------------------------------------##--
    Begin
          Ars_Gnr_Pkg.Insrt_Crdt_Crd_From_Br ( P_Doc_Type        =>5
                                                  ,P_Doc_No          =>V_Rt_Bill_No
                                                  ,P_Bill_Doc_Type   =>J.Rt_Bill_Doc_Type
                                                  ,P_Doc_Ser         =>V_Rt_Bill_Ser
                                                  ,P_Doc_Date        =>J.Rt_Bill_Date
                                                  ,P_User_Id         =>J.Ad_U_id
                                                  ,P_A_Cy            =>j.Rt_Bill_Currency
                                                  ,P_Cash_No         =>J.Cash_No
                                                  ,P_C_Code          =>null
                                                  ,P_External_Post   =>85
                                                  ,Typ               =>'S');                                                 
    Exception When Others Then                                                    
       RollBack;
       Raise_Application_Error(-20015,'Ars_Gnr_Pkg.Insrt_Crdt_Crd_From_Br  = '||Chr(13)||'rt_Bill_Ser ='||V_Rt_Bill_Ser ||Chr(13)||SqlErrm);                                               
    End; 
  --##-------------------------------------------------------------------------------------##--
--##-------------------------------------------------------------------------------------##--    
     Begin
        IAS_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 5                   ,
                                              G_Doc_Ser     => V_Rt_Bill_Ser       ,
                                              P_jv_type      => J.Rt_Bill_Doc_Type ,
                                              P_doc_no      => V_Rt_Bill_No        ,
                                              P_Lang_no     => Nvl(V_Lang_no,1)    ,
                                              P_User_No     => J.Ad_U_Id           ,
                                              G_Post_Type   => 0                   );
     Exception When Others Then
         RollBack;
         Raise_Application_Error(-20012,'Error When Post Rt Bill Sum, '||Chr(13)||SqlErrm);                                                   
     End;
  --##-----------------------------------------------------------------------------------##-- 
      If V_Use_Out_Bills=1 Then
           Begin
                IAS_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 14                   ,
                                                      G_Doc_Ser     => V_Ret_SER       ,
                                                      P_jv_type      => J.Rt_Bill_Doc_Type ,
                                                      P_doc_no      => V_Ret_No        ,
                                                      P_Lang_no     => Nvl(V_Lang_no,1)    ,
                                                      P_User_No     => J.Ad_U_Id           ,
                                                      G_Post_Type   => 0                   );
             Exception When Others Then
                 RollBack;
                 Raise_Application_Error(-20012,'Error When Post Rt Bill Sum, '||Chr(13)||SqlErrm);                                                   
             End;
       END IF;  
  --##-----------------------------------------------------------------------------------##--  
    End Loop; --(1)
--##-------------------------------------------------------------------------------------##--
    --## Update Ias_Rt_Bill_Mst_Br        
    Begin    
        Update Ias_Rt_Bill_Mst_Br Set Rt_Bill_post=1
         Where nvl(Rt_Bill_post,0)= 0                    
           And Exists (Select 1 From Ias_Rt_Bill_Mst_Br_Tmp Where Rt_Bill_Ser = Ias_Rt_Bill_Mst_Br.Rt_Bill_Ser  And RowNum <=1  );
          
    Exception When Others Then
         RollBack;
         Raise_Application_Error(-20013,'Error When Update Rt_Bill_Post Sum, '||Chr(13)||SqlErrm);                                                   
    End;  
--##-------------------------------------------------------------------------------------##--
  END;
--##-------------------------------------------------------------------------------------##--        
End;

Procedure Post_Transfer_Out ( P_Doc_Ser  In Ias_Whtrns_Mst.Tr_Ser%Type   Default Null , P_Use_Adjstmnt In Number Default 0 , P_User_No In User_R.U_Id%Type Default Null ,P_Lang_No In Number Default Null)  IS     
     V_Cnt                       Number                       ;
     V_Price                     Number                       ;
     V_Sqlstr2                   Varchar2(3000)               ;
     V_Use_Price_Whtrns_Rec_Cost Ias_Para_Inv.Use_Price_Whtrns_Rec_Cost%Type ;
     V_Use_Itm_Attach            Ias_Para_Inv.Use_Itm_Attach%Type ;
     V_Costing_Type              Ias_Para_Inv.Costing_Type%Type ;
     V_Wtavg_Type                Ias_Para_Inv.Wtavg_Type%Type ;
     V_Stkcost                   Number                       ;
     V_Seq                       Number                       ;
     V_Cst                       Number                       ; 
     V_Wt_After                  Number                       ;
     V_Wt_Before                 Number                       ;
     V_Use_Attch                 Ias_Itm_Mst.Use_Attch%Type  ;
     V_Attch                     Ias_Itm_Attach%RowType       ;
     V_Rec_Attch                 Ias_Itm_Attach_Movement.Rec_Attch%Type ; 
     V_Tr_Type                   Number ;
     V_Wcode                     Number;  
     V_Stk_Cst_Frc               Number ;
     V_Allow_Enter_Zero_Cost     Number:=1;
     V_Lang_No                   Number:=P_Lang_No;
Begin
  --##-------------------------------------------------------------------------------------##--
  If P_Lang_No Is Null Then    
    Begin
      Select Lang_No InTo V_Lang_No From Ias_Sys.Lang_Def Where Nvl(Flg_St,1)= 1 And Lang_Dflt=1 And Rownum<=1;
    Exception WHen Others Then
        V_Lang_No := 1;
    End;  
  ENd If;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      Select Costing_Type,Wtavg_Type,Use_Itm_Attach ,Stkcost_Fraction
        InTo V_Costing_Type,V_Wtavg_Type,V_Use_Itm_Attach,V_Stk_Cst_Frc
        From Ias_Para_AR,Ias_Para_Inv    
       Where RowNum<=1;
  Exception WHen Others Then
    RollBack;
    Raise_Application_Error(-20001,'Error When Select From Para In Post_Transfer_Out (7) '||Chr(13)||SqlErrm);
  End;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      If P_User_No<>1 Then
        Select Allow_Enter_Zero_Cost InTo V_Allow_Enter_Zero_Cost From Privilege_Fixed Where U_Id=P_User_No And RowNum<=1;
      End If;          
  Exception WHen Others Then
      RollBack;
      Raise_Application_Error(-20002,'Error When Select From Privilege_Fixed In Post_Transfer_Out , '||Chr(13)||SqlErrm);
  End;
--##------------------------------------------------------------------------------------##--
  Insert Into Ias_Whtrns_Mst_Br_Tmp (Tr_No,Tr_Ser) Select Tr_No,Tr_Ser 
                                                       From Ias_Whtrns_Mst_Br 
                                                      Where Tr_InOut_Type=1 
                                                        And Tr_Ser=Nvl(P_Doc_Ser,Tr_Ser) 
                                                        And Nvl(Hung,0)=0 
                                                        And Nvl(Tr_Post,0) = 0
                                                        And Exists(Select 1 From Ias_Whtrns_Dtl_Br Where Tr_Ser=Ias_Whtrns_Mst_Br.Tr_Ser And Rownum<=1)
                                                        And Not Exists(Select 1 From Ias_Whtrns_Mst Where Tr_Ser=Ias_Whtrns_Mst_Br.Tr_Ser And Rownum<=1);
                                                        
  Check_Avl_Qty ( P_Doc_Type => 7);  
--##-------------------------------------------------------------------------------------##--
  Begin
      Select 1 Into V_Cnt
       From  Ias_pos_minus_qty_Tmp
        Where RowNum <=1 ;
   Exception
       When Others Then
         V_cnt := 0 ;
     End ; 
   If Nvl(V_Cnt,0)>0 Then ---(2)
      If Nvl(P_Use_Adjstmnt,0)=1 Then
        Post_Stk_Adjstmnt ;
      Else
        Begin
            Delete Ias_Whtrns_Mst_Br_Tmp M Where Exists ( Select 1 From Ias_Whtrns_Dtl_Br A,Ias_Pos_Minus_Qty_Tmp B
                                                           Where A.Tr_Ser      = M.Tr_Ser 
                                                             And A.I_Code      = B.I_Code
                                                             And A.W_Code      = B.W_Code
                                                             And To_Date(A.Expire_date,'DD/MM/YYYY') = To_Date(B.Expire_date,'DD/MM/YYYY')
                                                             And A.Batch_No    = B.Batch_No                           
                                                             And Rownum<=1);   
        Exception When Others Then Null;
        End; 
      End If;                
   End If; ---(2)
--##-----------------------------------------------------------------------------------##--      
    Declare
     Cursor C_Tr_Mst Is Select Tr_Inout_Type, Tr_Type, Tr_No,Tr_Ser, Tr_Date, Ref_No,W_Code, T_W_Code, F_W_Code,Cc_Code,pj_no,actv_no, Tr_Desc, Stk_Rate, 
                               0 Tr_Post, Tr_Amt, Tr_Res, Load_No, Pr_Rep, Processed,Exp_Amt,Audit_Ref, Audit_Ref_Desc, Audit_Ref_U_Id,Audit_Ref_Date, External_Post, F_Tr_No, 
                               F_Tr_Ser, Boe_No, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date,Post_U_Id, Post_Date,Unpost_U_Id, Unpost_Date, Brn_No,Brn_Year, Cmp_No,  
                               Brn_Usr, Stk_Processed, Tr_Cost_Type, Diff_A_Code, Diff_A_Cy, Diff_Amt,Rtn_Tr,Tr_A_Code,C_Code,Doc_Brn_No
                        From   Ias_Whtrns_Mst_Br
                         Where Tr_InOut_Type  = 1
                          And Exists (Select 1 From Ias_Whtrns_Mst_Br_Tmp Where Tr_Ser = Ias_Whtrns_Mst_Br.Tr_Ser  And RowNum <=1  )                                               
                         Order By Ad_Date ;       
      Begin  
        For J In C_Tr_Mst Loop     
          --## Check Duplicate Transfer Out Number 
          /*Check_Duplicate_Tr ( J.Tr_Inout_Type ,
                               J.Tr_No         ,
                               J.Tr_Type       ,
                               J.Tr_Ser        ,
                               J.W_Code        );*/
--##-----------------------------------------------------------------------------------##--                 
           Begin    
                Insert Into Ias_Whtrns_Mst( Tr_Inout_Type, Tr_Type, Tr_No, Tr_Ser, Tr_Date, Ref_No,W_Code, T_W_Code, F_W_Code,Cc_Code,pj_no,actv_no, Tr_Desc, Stk_Rate, 
                                            Tr_Post, Tr_Amt, Tr_Res, Load_No, Pr_Rep, Processed,Exp_Amt,Audit_Ref, Audit_Ref_Desc, Audit_Ref_U_Id,Audit_Ref_Date, External_Post, F_Tr_No, 
                                            F_Tr_Ser, Boe_No, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date,Post_U_Id, Post_Date,Unpost_U_Id, Unpost_Date, Brn_No, 
                                            Brn_Year, Cmp_No,  Brn_Usr, Stk_Processed, Tr_Cost_Type,Diff_A_Code, Diff_A_Cy, Diff_Amt,Rtn_Tr, Tr_A_Code,C_Code,Doc_Brn_No,DOC_PST_SQ)
                                   Values ( J.Tr_Inout_Type, J.Tr_Type, J.Tr_No,J.Tr_Ser, J.Tr_Date, J.Ref_No, 
                                            J.W_Code, J.T_W_Code, J.F_W_Code, J.Cc_Code,J.Pj_No,J.Actv_No, J.Tr_Desc, J.Stk_Rate,0, J.Tr_Amt, J.Tr_Res,J.Load_No, J.Pr_Rep, 0 , 
                                            J.Exp_Amt, J.Audit_Ref, J.Audit_Ref_Desc, J.Audit_Ref_U_Id,J.Audit_Ref_Date, J.External_Post , J.F_Tr_No, 
                                            J.F_Tr_Ser, J.Boe_No, J.Ad_U_Id, J.Ad_Date, J.Up_U_Id, J.Up_Date,J.Post_U_Id, J.Post_Date,J.Unpost_U_Id, J.Unpost_Date, J.Brn_No, 
                                            J.Brn_Year, J.Cmp_No, J.Brn_Usr, J.Stk_Processed, J.Tr_Cost_Type,J.Diff_A_Code, J.Diff_A_Cy, J.Diff_Amt,J.Rtn_Tr,J.Tr_A_Code,J.C_Code,J.Doc_Brn_No,IAS_POSTING_PKG.GET_DOC_PST_SQ) ;
              Exception
               When Others Then
                 RollBack;
                 Raise_Application_Error ( -20004,' Err. When Insert InTo Ias_Whtrns_Mst , '||SqlErrm);    
              End;                                                                      
--##-----------------------------------------------------------------------------------##--        
              Declare
                Cursor C_Tr_Dtl Is Select Tr_Inout_Type, Tr_Type, Tr_No, Tr_Ser, I_Code, I_Qty,Itm_Unt, P_Size, P_Qty,W_Code, T_W_Code, F_W_Code,Tr_Qty,
                                          Cc_Code,pj_no,actv_no, Stk_Cost,Nvl(Expire_Date,'01/01/1900') Expire_Date ,Nvl(Batch_No,'0') Batch_No ,Use_Serialno,
                                          Exp_Amt, Out_Req_Type,Out_Req_No, Out_Req_Ser, Rcrd_No, Doc_Sequence, Boe_No, F_Tr_No,F_Tr_Ser, Use_Attch, Rec_Attch,Brn_No, Brn_Year, Doc_Sequence_Tr, 
                                          Cmp_No, Brn_Usr, I_Price, Item_Desc, Doc_Type_Ref,Doc_No_Ref, Doc_Ser_Ref, V_Code,External_Post,Barcode,Post_Code,
                                          I_Length,I_Width,I_Height,I_Number,Wt_Qty,Wt_Unt,Argmnt_No       
                                     From Ias_Whtrns_Dtl_Br
                                    Where Tr_InOut_Type=1
                                      And Ias_Whtrns_Dtl_Br.Tr_Ser = J.Tr_Ser;                
--##-----------------------------------------------------------------------------------##--           
              Begin 
                For I In C_Tr_Dtl  Loop     
                  Begin
                    V_Stkcost := Ias_Itm_Inv_Pkg.Get_Itm_Cost ( P_Costing_Type => V_Costing_Type         ,
                                                                P_Wtavg_Type   => V_Wtavg_Type           ,
                                                                P_Icode        => I.I_Code                        ,
                                                                P_Wcode        => I.W_Code                        ,
                                                                P_Psize        => Nvl(I.P_Size,1)                 ,
                                                                P_Iqty         => Nvl(I.I_Qty,0)                  ,
                                                                P_Expdate      => To_Date(Nvl(I.Expire_Date,'01/01/1900'),'DD/MM/YYYY') ,
                                                                P_Batchno      => Nvl(I.Batch_No,'0')             ,
                                                                P_Brn_No       => J.Brn_No                        ,
                                                                P_Brn_Year     => J.Brn_Year             ,
                                                                P_Cmp_No       => J.Cmp_No               ,
                                                                P_Brn_Usr      => J.Brn_Usr              );
                  Exception 
                    When Others Then
                          RollBack;
                          Raise_Application_Error ( -20005,' Err. When Get Cost In Ias_Whtrns_Mst , '||SqlErrm);                                                      
                    End;     
                  --------------------------------------------------------------------------------------------
                  If V_allow_enter_zero_cost = 0 And Nvl(V_Stkcost,0) = 0  Then
                     RollBack;
                     Raise_Application_Error ( -20006,' Err. Not Allowed Zero Cost In Ias_Whtrns_Mst , '||SqlErrm);
                  End If ;                    
                  --##----------------------------------------------------------------------------------##--       
                  Begin
                      Select Ias_Doc_Seq.NextVal Into V_Seq From Dual;                    
                  Exception
                     When Others Then
                        RollBack;
                        Raise_Application_Error ( -20007,' Err. On Get Ias_Doc_Seq , '||SqlErrm);
                  End ;
--##-----------------------------------------------------------------------------------##--
                  Begin
                      Insert Into Ias_Whtrns_Dtl (  Tr_Inout_Type, Tr_Type, Tr_No,Tr_Ser, I_Code, I_Qty,Itm_Unt, P_Size, P_Qty,W_Code, T_W_Code, F_W_Code, 
                                                    Tr_Qty, Cc_Code,pj_no,actv_no, Stk_Cost, Expire_Date, Batch_No, Use_Serialno,Exp_Amt, Rcrd_No,Doc_Sequence, Boe_No, F_Tr_No, 
                                                    F_Tr_Ser, Use_Attch, Rec_Attch, Brn_No, Brn_Year, Doc_Sequence_Tr,Cmp_No,  Brn_Usr,I_Price, Item_Desc, Doc_Type_Ref, 
                                                    Doc_No_Ref, Doc_Ser_Ref, V_Code,External_Post ,Barcode,Post_Code)
                                          Values (  I.Tr_Inout_Type, 
                                                    I.Tr_Type, 
                                                    I.Tr_No, 
                                                    I.Tr_Ser, 
                                                    I.I_Code, 
                                                    I.I_Qty, 
                                                    I.Itm_Unt, 
                                                    I.P_Size, 
                                                    I.P_Qty, 
                                                    I.W_Code, 
                                                    I.T_W_Code, 
                                                    I.F_W_Code, 
                                                    I.Tr_Qty, 
                                                    I.Cc_Code,
                                                    I.Pj_No, 
                                                    I.Actv_No,
                                                    Nvl(V_StkCost,0), 
                                                    Nvl(I.Expire_Date,'01/01/1900'), 
                                                    Nvl(I.Batch_No,'0'), 
                                                    I.Use_Serialno, 
                                                    I.Exp_Amt, I.Rcrd_No, 
                                                    V_Seq, I.Boe_No, I.F_Tr_No, 
                                                    I.F_Tr_Ser, I.Use_Attch, I.Rec_Attch, 
                                                    I.Brn_No, I.Brn_Year, V_Seq , 
                                                    I.Cmp_No, I.Brn_Usr, 
                                                    Decode(J.Tr_Cost_Type,1,Nvl(V_StkCost,0),Nvl(I.I_Price,0)),
                                                    I.Item_Desc, I.Doc_Type_Ref, 
                                                    I.Doc_No_Ref, I.Doc_Ser_Ref, I.V_Code,
                                                    I.External_Post,I.Barcode,I.Post_Code);
                  Exception
                    When Others Then
                     RollBack;
                     Raise_Application_Error ( -20008,' Err. When Insert In To Ias_Whtrns_Dtl (7), '||SqlErrm);
                  End; 
                      
                  If V_Use_Itm_Attach=1 And Nvl(I.Use_Attch,0)=1 Then
                      
                      Declare
                          V_Cnt Number;
                      Begin
                          Select 1 InTo V_Cnt
                            From Ias_Itm_Attach_Movement_Br
                           Where Doc_Ser   = J.Tr_Ser
                             And Rec_Attch = I.Rec_Attch 
                             And Doc_Type  = 7
                             And RowNum   <= 1;
                     Exception When Others Then                                                                          
                          RollBack;
                          Raise_Application_Error ( -20009,' Err. When Get Attachement To Ias_Whtrns_Mst (7) , '||SqlErrm);                                                  
                     End; 
                     ------------------------------------------------------------------------------------------------------              
                     Begin
                        Insert InTo Ias_Itm_Attach_Movement ( I_Code, Itm_Unt, P_Size,Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                              Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                              Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                              Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                              W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                              R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                              Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Type_Ref, 
                                                              Doc_No_Ref, Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                              Ac_Rate, Stk_Rate, I_Price, Dis_Amt, I_Cost, Stk_Cost, Vat_Amt, 
                                                              V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                              Cmp_No, Brn_No, Brn_Year,  Brn_Usr, Othr_Amt)
                                                       Select I_Code, Itm_Unt, P_Size, 
                                                              Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                              Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                              Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                              Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                              W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                              R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                              Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Type_Ref, Doc_No_Ref, 
                                                              Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                              Ac_Rate, J.Stk_Rate, I.I_Price, Dis_Amt, Nvl(V_Stkcost,0), Nvl(V_Stkcost,0), Vat_Amt, 
                                                              V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                              Cmp_No, Brn_No, Brn_Year,  Brn_Usr, Othr_Amt
                                                         From Ias_Itm_Attach_Movement_Br
                                                        Where Doc_Ser   = J.Tr_Ser
                                                          And Rec_Attch = I.Rec_Attch 
                                                          And Doc_Type  = 7;
                     Exception When Others Then                                                    
                        RollBack;
                        Raise_Application_Error ( -20010,' Err. When Insert InTo Ias_Itm_Attach_Movement_Br (7) , '||SqlErrm);                                              
                     End;  
                     ------------------------------------------------------------------------------------------------------     
                  End If;           
--##-----------------------------------------------------------------------------------##--                          
                  Begin
                   Select Decode(J.Tr_Cost_Type,1,Nvl(V_StkCost,0),Nvl(I.I_Price,0)) 
                     Into V_Price
                    From Dual;
                  Exception
                      When Others Then
                       V_Price :=  Nvl(I.I_Price,0) ;
                  End ;
                  
                  Begin
                    V_Cst := 0;
                    Ias_Itm_Inv_Pkg.Insrt_Sale_Cost ( P_Cst         => V_Cst                            ,
                                                      P_Icode       => I.I_Code                         ,
                                                      P_Iqty        => Nvl(I.I_Qty,0)                   ,
                                                      P_Freeqty     => 0                                ,
                                                      P_Itm_Unt     => I.Itm_Unt                        ,
                                                      P_Psize       => I.P_Size                         ,
                                                      p_Cost_Type   => V_Costing_Type                   ,
                                                      p_Wtavg_Type  => V_Wtavg_Type                     ,
                                                      P_Wcode       => I.W_Code                         ,
                                                      P_Doctype     => 7                                ,
                                                      P_Docno       => I.Tr_No                          ,
                                                      P_Billdoctype => I.Tr_Type                        ,
                                                      P_Cc_Code     => I.CC_Code                        ,
                                                      P_Pj_No       => I.Pj_No                          ,
                                                      P_Actv_No     => I.Actv_No                        ,
                                                      P_Rcrdno      => I.Rcrd_No                        ,
                                                      P_Expdate     => To_Date(Nvl(I.Expire_Date,'01/01/1900'),'DD/MM/YYYY')  , 
                                                      P_Batchno     => Nvl(I.Batch_No,'0')              ,
                                                      P_Docser      => I.Tr_Ser                         ,
                                                      P_Docseq      => V_Seq                            ,
                                                      P_Idate       => J.Tr_Date                        ,
                                                      P_Vatamt      => 0                                ,
                                                      P_Disamt      => 0                                ,
                                                      P_Acy         => Ias_Gen_Pkg.Get_Stk_Cur          ,
                                                      P_Ac_Rate     => J.Stk_Rate                       ,
                                                      P_Stk_Rate    => J.Stk_Rate                       ,
                                                      P_C_Code      => Null                             ,
                                                      P_Adesc       => J.Tr_Desc                        ,
                                                      P_Refno       => J.Ref_no                         ,
                                                      P_Inout       => -1                               ,
                                                      P_Iprice      => Nvl(V_Price,0)                   ,
                                                      p_Extrnl_pst  => J.External_post                  ,
                                                      P_Itm_Length  => I.I_Length                       ,
                                                      P_Itm_Width   => I.I_Width                        ,
                                                      P_Itm_Height  => I.I_Height                       ,
                                                      P_Itm_Number  => I.I_Number                       ,
                                                      P_Wt_Qty        => I.Wt_Qty                         ,
                                                      P_Wt_Unt        => I.Wt_Unt                         ,
                                                      P_Argmnt_No    => I.Argmnt_No                      ,
                                                      P_Ad_Date     => J.Ad_Date                        ,
                                                      P_Up_Date     => Null                             , 
                                                      P_Brn_No      => J.Brn_No                         ,
                                                      P_Brn_Year    => J.Brn_Year                       ,
                                                      p_Cmp_No      => J.Cmp_No                         ,
                                                      P_Brn_Usr     => J.Brn_Usr                        ) ;                                                                                                                                      
                  Exception When Others Then
                     RollBack;
                     Raise_Application_Error ( -20011,' Err. In Ias_Itm_Inv_Pkg.Insrt_Sale_Cost (7) , '||SqlErrm);
                  End ;                
                End Loop;
              End ;
              
              Begin
                IAS_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 11           ,
                                                      G_Doc_Ser     => J.Tr_Ser     ,
                                                      P_jv_type     => J.Tr_Type    ,
                                                      P_doc_no      => J.Tr_No      ,
                                                      P_Lang_no     => 1            ,
                                                      P_User_No     => J.Ad_U_Id    ,
                                                      G_Post_Type   => 0            );
             Exception 
               When No_Data_Found Then 
                 Null;
               When Others Then                
                 RollBack;
                 Raise_Application_Error(-20012,'Error When Post Warehouse Transfer (7) , '||Chr(13)||SqlErrm);                                                   
              End;              
                
        End Loop; 
--##-----------------------------------------------------------------------------------##--
       --## Update Ias_Rt_Bill_Mst_Br        
        Begin    
            Update Ias_Whtrns_Mst_Br Set Tr_post=1
             Where Tr_Inout_Type=1
               And Nvl(Tr_post,0)=0                    
               And Exists (Select 1 From Ias_Whtrns_Mst_Br_Tmp Where Tr_Ser = Ias_Whtrns_Mst_Br.Tr_Ser  And RowNum <=1  ) 
               And Exists (Select 1 From Ias_Whtrns_Mst Where Tr_Ser=Ias_Whtrns_Mst_Br.Tr_Ser And RowNum<=1);
        Exception When Others Then
             RollBack;             
             Raise_Application_Error(-20013,'Error When Update Ias_Whtrns_Mst_Br (7) , '||Chr(13)||SqlErrm);                                                   
        End;                
   End;
End Post_Transfer_Out;
    
Procedure Post_Incmng ( P_Doc_Ser  In Gr_Note.G_Ser%Type   Default Null , P_User_No In User_R.U_Id%Type Default Null,P_Lang_No In Number Default Null) Is     
      V_Cnt                       Number;
      V_Seq                       Number;
      V_Ret_No                    Number;
      V_Ret_Ser                   Number;      
      V_StkRate                   Number;
      V_Cst                       Number;
      V_Py                        Number;
      V_Wt_Before                 Number;    
      V_Wt_After                  Number;
      V_Rec_No                    Number;
      V_Costing_Type              Number;
      V_Wtavg_Type                Number;
      V_Stk_Cst_Frc               Number;
      V_Use_Itm_Attach            Number;
      V_Lang_No                   Number:= P_Lang_No;
      V_Allow_Enter_Zero_Cost     Number;    
Begin  
--##------------------------------------------------------------------------------------##--
  If P_Lang_No Is Null Then    
    Begin
      Select Lang_No InTo V_Lang_No From Ias_Sys.Lang_Def Where Nvl(Flg_St,1)= 1 And Lang_Dflt=1 And Rownum<=1;
    Exception WHen Others Then
        V_Lang_No := 1;
    End;  
  ENd If;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      Select Nvl(Costing_Type,0) ,
             Nvl(Wtavg_Type,0)   ,
             Nvl(Stkcost_Fraction ,6)  ,
             Nvl(Use_Itm_Attach ,0)   
        Into V_Costing_Type              ,
             V_Wtavg_Type                ,
             V_Stk_Cst_Frc               ,
             V_Use_Itm_Attach          
       From Ias_Para_Inv ;
  Exception WHen Others Then
    RollBack;
    Raise_Application_Error(-20001,'Error When Select From Para In Post_Incoming '||Chr(13)||SqlErrm);
  End;  
  --##-------------------------------------------------------------------------------------##--
  Begin
      If P_User_No<>1 Then
        Select Allow_Enter_Zero_Cost InTo V_Allow_Enter_Zero_Cost From Privilege_Fixed Where U_Id=P_User_No And RowNum<=1;
      End If;          
  Exception WHen Others Then
      RollBack;
      Raise_Application_Error(-20002,'Error When Select From Privilege_Fixed In Post_Incomingt , '||Chr(13)||SqlErrm);
  End; 
--##------------------------------------------------------------------------------------##--  
    Insert Into Gr_Note_Br_Tmp (Gr_No,G_Ser) Select Gr_No,G_Ser 
                                               From Gr_Note_Br 
                                              Where Pi_Type=5 
                                                And G_Ser=Nvl(P_Doc_Ser,G_Ser) 
                                                And Nvl(Hung,0)=0 
                                                And Nvl(Gr_Post,0) = 0
                                                And Exists(Select 1 From Gr_Detail_Br Where G_Ser=Gr_Note_Br.G_Ser And Rownum<=1)
                                                And Not Exists(Select 1 From Gr_Note Where G_Ser=Gr_Note_Br.G_Ser And Rownum<=1);
--##------------------------------------------------------------------------------------##--    
---------------------------------- ## Cursor Return Sales ## --------------------------------      
    Declare
       Cursor GRM Is Select Pi_Type, 
                            Gr_No, 
                            G_Ser, 
                            Incom_Type, 
                            Gr_Date, 
                            A_Code, 
                            A_Cy, 
                            Ac_Rate, 
                            Stk_Rate, 
                            Gr_Amt, 
                            Pi_No, 
                            V_Code, 
                            C_Code, 
                            Csh_Bnk_No,
                            C_Flag, 
                            W_Code, 
                            Gr_Post, 
                            Ref_No, 
                            A_Desc, 
                            Cc_Code, 
                            Pj_No, 
                            Actv_No, 
                            Pending, 
                            Pur_Type, 
                            Driver_Name, 
                            Car_No, 
                            Work_Shop, 
                            Doc_Ser, 
                            Doc_No, 
                            Rt_Out, 
                            Out_Diff_A_Code, 
                            Out_Diff_A_Cy, 
                            Out_Diff_Amt, 
                            Boe_No, 
                            Use_Vat, 
                            Vat_Amt, 
                            Pr_Rep, 
                            Pi_Doc_Type, 
                            External_Post, 
                            Mrp_Mt_Sq, 
                            Mrp_Mt_Order, 
                            Mrp_Mt_Type, 
                            Under_Selling, 
                            Audit_Ref, 
                            Audit_Ref_Desc,
                            Audit_Ref_U_Id, 
                            Audit_Ref_Date, 
                            Ad_U_Id,
                            Ad_Date, 
                            Up_U_Id, 
                            Up_Date, 
                            Post_U_Id, 
                            Post_Date, 
                            Unpost_U_Id, 
                            Unpost_Date, 
                            Cmp_No, 
                            Brn_No, 
                            Brn_Year, 
                            Brn_Usr, 
                            Doc_Due_Date,
                            Doc_Brn_No,
                            CONN_WITH_PI,
                            Ac_Code_Dtl    ,
                            Ac_Dtl_Typ    
                    From Gr_Note_Br
                    Where Pi_Type=5
                      And nvl(Gr_post,0)=0         
                      And Exists (Select 1 From Gr_Note_Br_Tmp Where G_Ser = Gr_Note_Br.G_Ser  And RowNum <=1  )              
                    Order By Ad_Date ;
    Begin ---(11)
--##-------------------------------------------------------------------------------------##--    
    --## To Get Stock Rate           
     V_StkRate := Ias_Gen_Pkg.Get_Cur_rate(p_acy=>Ias_Gen_Pkg.Get_Stk_Cur);      
--##-------------------------------------------------------------------------------------##--    
  For j in GRM Loop     -->> (1)    
        Begin
          --Check_Duplicate_Gr(J.Gr_No,J.Incom_Type,J.G_Ser);
          Insert Into Gr_Note ( Pi_Type, 
                                Gr_No, 
                                G_Ser, 
                                Incom_Type, 
                                Gr_Date, 
                                A_Code, 
                                A_Cy, 
                                Ac_Rate, 
                                Stk_Rate, 
                                Gr_Amt, 
                                Pi_No, 
                                V_Code, 
                                C_Code,
                                Csh_Bnk_No, 
                                C_Flag, 
                                W_Code, 
                                Gr_Post, 
                                Ref_No, 
                                A_Desc, 
                                Cc_Code, 
                                Pj_No, 
                                Actv_No,
                                Pending, 
                                Pur_Type, 
                                Driver_Name, 
                                Car_No, 
                                Work_Shop, 
                                Doc_Ser, 
                                Doc_No, 
                                Rt_Out, 
                                Out_Diff_A_Code, 
                                Out_Diff_A_Cy, 
                                Out_Diff_Amt, 
                                Boe_No, 
                                Use_Vat, 
                                Vat_Amt, 
                                Pr_Rep, 
                                Pi_Doc_Type, 
                                External_Post, 
                                Mrp_Mt_Sq, 
                                Mrp_Mt_Order, 
                                Mrp_Mt_Type, 
                                Under_Selling, 
                                Audit_Ref, 
                                Audit_Ref_Desc,
                                Audit_Ref_U_Id, 
                                Audit_Ref_Date, 
                                Ad_U_Id, 
                                Ad_Date, 
                                Up_U_Id, 
                                Up_Date, 
                                Post_U_Id, 
                                Post_Date, 
                                Unpost_U_Id, 
                                Unpost_Date, 
                                Cmp_No, 
                                Brn_No, 
                                Brn_Year, 
                                Brn_Usr, 
                                Doc_Due_Date,
                                Doc_Brn_No,
                                DOC_PST_SQ,
                                CONN_WITH_PI,
                                Ac_Code_Dtl    ,
                                Ac_Dtl_Typ    )
                        Values( J.Pi_Type, 
                                J.Gr_No, 
                                J.G_Ser, 
                                J.Incom_Type, 
                                J.Gr_Date, 
                                J.A_Code, 
                                J.A_Cy, 
                                J.Ac_Rate, 
                                V_StkRate, 
                                J.Gr_Amt, 
                                J.Pi_No, 
                                J.V_Code, 
                                J.C_Code, 
                                J.Csh_Bnk_No,
                                J.C_Flag, 
                                J.W_Code, 
                                0, 
                                J.Ref_No, 
                                J.A_Desc, 
                                J.Cc_Code, 
                                J.Pj_No, 
                                J.Actv_No, 
                                J.Pending, 
                                J.Pur_Type, 
                                J.Driver_Name, 
                                J.Car_No, 
                                J.Work_Shop, 
                                J.Doc_Ser, 
                                J.Doc_No, 
                                J.Rt_Out, 
                                J.Out_Diff_A_Code, 
                                J.Out_Diff_A_Cy, 
                                J.Out_Diff_Amt, 
                                J.Boe_No, 
                                J.Use_Vat, 
                                J.Vat_Amt, 
                                J.Pr_Rep, 
                                J.Pi_Doc_Type, 
                                J.External_Post, 
                                J.Mrp_Mt_Sq, 
                                J.Mrp_Mt_Order, 
                                J.Mrp_Mt_Type, 
                                J.Under_Selling, 
                                J.Audit_Ref, 
                                J.Audit_Ref_Desc,
                                J.Audit_Ref_U_Id, 
                                J.Audit_Ref_Date, 
                                J.Ad_U_Id, 
                                J.Ad_Date, 
                                J.Up_U_Id, 
                                J.Up_Date, 
                                J.Post_U_Id, 
                                J.Post_Date, 
                                J.Unpost_U_Id, 
                                J.Unpost_Date, 
                                J.Cmp_No, 
                                J.Brn_No, 
                                J.Brn_Year, 
                                J.Brn_Usr, 
                                J.Doc_Due_Date,
                                J.Doc_Brn_No,
                                IAS_POSTING_PKG.GET_DOC_PST_SQ,
                                J.CONN_WITH_PI,
                                J.Ac_Code_Dtl    ,
                                J.Ac_Dtl_Typ    );
        Exception
       When Others Then
         RollBack;
         Raise_Application_Error(-20005,'Error When Insert Into Gr_Note '||Chr(13)||SqlErrm);  
      End;        
--##-------------------------------------------------------------------------------------##--      
  Declare
         Cursor GRD Is Select  Pi_Type, 
                               Gr_No, 
                               G_Ser, 
                               Incom_Type, 
                               Gr_Date, 
                               I_Code, 
                               I_Qty, 
                               Free_Qty, 
                               Itm_Unt, 
                               P_Size, 
                               P_Qty, 
                               Cp_Qty, 
                               Pi_No, 
                               Pur_Type, 
                               Doc_Ser, 
                               W_Code, 
                               Whg_Code, 
                               C_Price, 
                               Stk_Cost, 
                               Stk_Rate, 
                               A_Cy, 
                               Ac_Rate, 
                               Expire_Date, 
                               Batch_No, 
                               Cc_Code,
                               Pj_No,
                               Actv_No, 
                               V_Code, 
                               I_Price, 
                               Dis_Amt, 
                               Vat_Per, 
                               Vat_Amt, 
                               Diff_Amt, 
                               Use_Serialno, 
                               Rcrd_No, 
                               Doc_Sequence, 
                               Use_Attch, 
                               Rec_Attch, 
                               Item_Desc, 
                               Under_Selling, 
                               Cmp_No, 
                               Brn_No, 
                               Brn_Year, 
                               Brn_Usr, 
                               Barcode, 
                               External_Post,
                               Doc_Type_Ref         ,
                                                             Doc_No_Ref           ,
                                                             Doc_Ser_Ref         ,
                                                            Doc_Sequence_Ref 
                          From Gr_Detail_br             
                         Where Pi_Type=5
                           And G_Ser=J.G_Ser;     
--##-------------------------------------------------------------------------------------##--           
    Begin --- (12)
         For i in GRD  Loop        -->> (2)
            Begin
               --##-------------------------------------------------------------------------------------##--
                Select Ias_Doc_Seq.NextVal InTo V_Seq From Dual;
                Select Ias_Recno_Seq.NextVal InTo V_Rec_No From Dual;                    
                --##-------------------------------------------------------------------------------------##-- 
                    --## Calc_WatAvg                 
                  Begin    
                      V_Wt_After := Calc_Wtavg_Cost(P_Cost_Type  => V_Costing_Type ,
                                                    P_Wtavg_Type => V_Wtavg_Type   ,
                                                    P_Icode      => I.I_Code                ,
                                                    P_Iqty       => I.I_Qty                 ,
                                                    P_Icost      => Nvl((J.Ac_Rate/J.Stk_Rate)*Nvl(I.C_price,0),0),
                                                    P_Psize      => I.P_Size                ,
                                                    P_Wcode      => I.W_Code                ,
                                                    P_Frc_No     => V_Stk_Cst_Frc,
                                                    P_Brn_No     => j.Brn_No                ,
                                                    P_Brn_Year   => j.Brn_Year              ,
                                                    P_Cmp_No     => j.Cmp_No                ,
                                                    P_Brn_Usr    => j.Brn_Usr               
                                                                );
                  Exception 
                   When Others Then
                     RollBack;
                     Raise_Application_Error(-20005,'Error When Calc V_Wt_After Error In Post Incoming '||Chr(13)||SqlErrm);                     
                  End;

                    --## Get WatAvg Before                 
                  If  V_Costing_Type  = 2 Then  -- Wtavg
                       Begin
                          V_Wt_Before:= Nvl(Ias_Itm_Pkg.Get_Grand_WtAvg ( V_Wtavg_Type   ,
                                                                          I.I_Code               ,
                                                                          I.W_Code ),0           ) ;                                              
                        Exception
                           When Others Then
                             RollBack;
                             Raise_Application_Error(-20005,'Error When Calc V_Wt_Before Error In Post Incoming '||Chr(13)||SqlErrm);
                         End ;
          Else -- fifo
                  V_Wt_Before:= 0 ;
          End If; 
          
          -------------------------------------------------------------------------------------------
          If V_allow_enter_zero_cost = 0 And Nvl(V_Wt_After,0) = 0  Then
               RollBack;
               Raise_Application_Error(-20005,'Error Not Allow Zero Cost In Post Incoming I_Code= '||I.I_Code||Chr(13)||SqlErrm);
          End If ;                                        
--##-------------------------------------------------------------------------------------##--                
          Insert Into Gr_Detail (  Pi_Type, 
                                   Gr_No, 
                                   G_Ser, 
                                   Incom_Type, 
                                   Gr_Date, 
                                   I_Code, 
                                   I_Qty, 
                                   Free_Qty, 
                                   Itm_Unt, 
                                   P_Size, 
                                   P_Qty, 
                                   Cp_Qty, 
                                   Pi_No, 
                                   Pur_Type, 
                                   Doc_Ser, 
                                   W_Code, 
                                   Whg_Code,
                                   C_Price, 
                                   Stk_Cost, 
                                   Stk_Rate, 
                                   A_Cy, 
                                   Ac_Rate, 
                                   Wt_Avg_Before, 
                                   Wt_Avg_After, 
                                   Expire_Date, 
                                   Batch_No, 
                                   Cc_Code,
                                   Pj_No,
                                   Actv_No, 
                                   V_Code, 
                                   I_Price, 
                                   Dis_Amt, 
                                   Vat_Per, 
                                   Vat_Amt, 
                                   Diff_Amt, 
                                   Use_Serialno, 
                                   Rcrd_No, 
                                   Rec_No, 
                                   Doc_Sequence, 
                                   Use_Attch, 
                                   Rec_Attch, 
                                   Item_Desc, 
                                   Under_Selling, 
                                   Cmp_No, 
                                   Brn_No, 
                                   Brn_Year, 
                                   Brn_Usr, 
                                   Barcode, 
                                   External_Post,
                                   Doc_Type_Ref         ,
                                                                 Doc_No_Ref           ,
                                                                 Doc_Ser_Ref         ,
                                                                 Doc_Sequence_Ref  )
                           Values( I.Pi_Type, 
                                   I.Gr_No, 
                                   I.G_Ser, 
                                   I.Incom_Type, 
                                   I.Gr_Date, 
                                   I.I_Code, 
                                   I.I_Qty, 
                                   Null, 
                                   I.Itm_Unt, 
                                   I.P_Size, 
                                   I.P_Qty, 
                                   I.Cp_Qty, 
                                   I.Pi_No, 
                                   I.Pur_Type, 
                                   I.Doc_Ser, 
                                   I.W_Code, 
                                   I.Whg_Code,
                                   I.C_Price, 
                                   (J.Ac_Rate/J.Stk_Rate)*Nvl(I.C_price,0),
                                   V_StkRate, 
                                   I.A_Cy, 
                                   I.Ac_Rate, 
                                   Nvl(V_Wt_Before,0), 
                                   Nvl(V_Wt_After,0), 
                                   I.Expire_Date, 
                                   I.Batch_No, 
                                   I.Cc_Code, 
                                   I.Pj_No,
                                   I.Actv_No,              
                                   I.V_Code, 
                                   I.I_Price, 
                                   I.Dis_Amt, 
                                   I.Vat_Per, 
                                   I.Vat_Amt, 
                                   I.Diff_Amt, 
                                   I.Use_Serialno, 
                                   I.Rcrd_No, 
                                   V_Rec_No, 
                                   V_Seq, 
                                   I.Use_Attch, 
                                   I.Rec_Attch, 
                                   I.Item_Desc, 
                                   I.Under_Selling, 
                                   I.Cmp_No, 
                                   I.Brn_No, 
                                   I.Brn_Year, 
                                   I.Brn_Usr, 
                                   I.Barcode, 
                                   J.External_Post,
                                   I.Doc_Type_Ref         ,
                                   I.Doc_No_Ref           ,
                                   I.Doc_Ser_Ref         ,
                                   I.Doc_Sequence_Ref  );
              Exception
                  When Others Then                  
                     RollBack;
                     Raise_Application_Error(-20005,'Error In Insert InTo Gr_Detail '||Chr(13)||SqlErrm);
              End;
              
              If V_Use_Itm_Attach=1 And Nvl(I.Use_Attch,0)=1 Then
                  Declare
                      V_Cnt Number;
                  Begin
                      Select 1 InTo V_Cnt
                       From Ias_Itm_Attach_Movement_Br
                      Where Doc_Ser   = J.G_Ser
                        And Rec_Attch = I.Rec_Attch 
                        And Doc_Type  = 5
                        And RowNum<=1;
                        Exception When Others Then                                                                          
                             RollBack;
                             Raise_Application_Error(-20010,'Error In  Ias_Itm_Attach_Movement_Br In Post_Incmng');                                                  
                         End;               
                                         
                  Begin
                     Insert InTo Ias_Itm_Attach_Movement(I_Code, Itm_Unt, P_Size, 
                                                           Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                           Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                           Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                           Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                           W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                           R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                           Free_Qty, Pf_Qty, Rcrd_No, External_Post, Doc_Type_Ref, 
                                                           Doc_No_Ref, Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                           Ac_Rate, Stk_Rate, I_Price, Dis_Amt, I_Cost, Stk_Cost, Vat_Amt, 
                                                           V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                           Cmp_No, Brn_No, Brn_Year, Brn_Usr, Othr_Amt)
                                                    Select I_Code, Itm_Unt, P_Size, 
                                                           Attch_No1, Attch_Desc_No1, Attch_No2, Attch_Desc_No2, 
                                                           Attch_No3, Attch_Desc_No3, Attch_No4, Attch_Desc_No4, 
                                                           Attch_No5, Attch_Desc_No5, Flex_Field, Flex_No,Rec_Attch, 
                                                           Attch_Note, Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, 
                                                           W_Code, Bill_Cost, Rcrd_No_Doc, In_Out, Cc_Code,pj_no,actv_no, Rep_Code, 
                                                           R_Code, C_Code, Expire_Date, Batch_No, I_Qty, P_Qty, 
                                                           Free_Qty, Pf_Qty, Rcrd_No, 85, Doc_Type_Ref, Doc_No_Ref, 
                                                           Doc_Ser_Ref, Out_No, Out_Gr_Ser, Doc_Date, A_Cy, 
                                                           Ac_Rate, V_StkRate, I.I_Price, Dis_Amt, I_Price, Nvl((J.Ac_Rate/J.Stk_Rate)*Nvl(I.C_price,0),0), Vat_Amt, 
                                                           V_Code, Rt_Type, Ad_U_Id, Ad_Date, Up_U_Id, Up_Date, 
                                                           Cmp_No, Brn_No, Brn_Year, Brn_Usr, Othr_Amt
                                                      From Ias_Itm_Attach_Movement_Br
                                                     Where Doc_Ser   = J.G_Ser
                                                       And Rec_Attch = I.Rec_Attch 
                                                       And Doc_Type  = 5;
                      Exception When Others Then                                                    
                          RollBack;
                          Raise_Application_Error(-20010,'Error In  In Insert InTo Ias_Itm_Attach_Movement In Post_Incmng');                                                  
                      End;       
                End If;      
--##-------------------------------------------------------------------------------------##--
                Begin
                 IAS_Itm_Inv_Pkg.Insrt_Item_Move ( p_DocType     => 5 ,
                                                   p_billDocType => J.Incom_Type ,
                                                   p_DocNo       => J.Gr_No,
                                                   p_ICode       => I.i_code ,
                                                   p_Iqty        => I.i_qty ,
                                                   p_Freeqty     => 0 ,
                                                   p_Itm_Unt     => I.Itm_Unt ,
                                                   p_PSize       => I.P_size ,
                                                   p_idate       => J.Gr_Date,
                                                   p_iprice      => I.i_price,
                                                   p_WCode       => I.w_code ,
                                                   p_stkcost     => Nvl((J.Ac_Rate/J.Stk_Rate)*Nvl(I.C_price,0),0),
                                                   p_vatamt      => I.vat_amt ,
                                                   p_disamt      => 0 ,
                                                   p_acy         => J.A_Cy ,
                                                   p_ac_rate     => J.Ac_Rate ,
                                                   p_stk_rate    => V_StkRate ,
                                                   p_Cc_Code     => nvl(J.Cc_Code ,I.Cc_Code ),
                                                   p_Pj_No       => nvl(J.Pj_No ,I.Pj_No ),
                                                   p_Actv_No     => nvl(J.Actv_No ,I.Actv_No ),
                                                   p_c_code      => J.c_code ,
                                                   p_adesc       => J.a_desc ,
                                                   p_ExpDate     => To_Char(Nvl(I.Expire_Date,'01/01/1900'),'DD/MM/YYYY'),
                                                   p_BatchNo     => I.Batch_No,
                                                   p_RcrdNo      => I.rcrd_no,
                                                   p_refno       => J.Ref_no,
                                                   p_DocSer      => J.G_Ser,
                                                   p_DocSeq      => V_Seq,
                                                   p_outno       => Null,
                                                   p_outgrser    => Null,
                                                   p_rt_type     => Null,
                                                   p_inout       => 1,
                                                   p_Extrnl_pst  => J.External_Post,
                                                   p_ad_date     => J.Ad_Date,
                                                   p_up_date     => J.Up_Date,
                                                   P_Brn_no      => j.Brn_no,
                                                   P_Brn_Year    => J.Brn_Year,
                                                   P_Cmp_No      => J.Cmp_No,
                                                   P_Brn_Usr     => J.Brn_Usr);
                    Exception when Others Then
                        RollBack;
                        Raise_Application_Error(-20010,'Error In  In Insert InTo Ias_Itm_Attach_Movement In Post_Incmng');
                    End;

              End Loop; --(2)
             End; --(12)
--##-------------------------------------------------------------------------------------##--        
       Begin
            Ias_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 8                 ,
                                                  G_Doc_Ser     => J.G_Ser        ,
                                                  P_Jv_Type     => J.Incom_Type   ,
                                                  P_Doc_No      => J.Gr_No         ,
                                                  P_Lang_No     => 1                 ,
                                                  P_User_No     => J.Ad_U_Id         ,
                                                  G_Post_Type   => 0                 );
       Exception 
           When No_Data_Found Then 
                Null;
           When Others Then
                RollBack;
                Raise_Application_Error(-20013,'Error When Post In Incoming  = '||Chr(13)||'G_Ser ='||J.G_Ser ||Chr(13)||SqlErrm);                                                    
       End;    
    
--##-------------------------------------------------------------------------------------##--             
      
    End Loop; --(1)
--##-------------------------------------------------------------------------------------##--
    --## Update Gr_Note_Br        
    Begin
       Update Gr_Note_Br
          Set Gr_Post         = 1  
        Where Exists (Select 1 From Gr_Note_Br_Tmp Where G_Ser = Gr_Note_Br.G_Ser  And RowNum <=1  )
          And Exists (Select 1 From Gr_Note Where G_Ser = Gr_Note_Br.G_Ser  And RowNum <=1  );
           Commit ;
                     
    Exception
      When Others Then
         RollBack;
         Raise_Application_Error(-20014,'Error When Updating Gr_Note Post  = ' ||Chr(13)||Sqlerrm);                         
     End ;
--------------------------------------------------------------------------------------------                
        END;
End;

--##-------------------------------------------------------------------------------------------------##--
Procedure  Post_Stk_Adjstmnt Is
   V_Cnt              Number;
   V_Seq              Number;
   V_Wt_After         Number;
   V_Wt_Before        Number;
   V_Stk_Type         Stk_Adjustment.Stk_Type%Type;
   V_Stk_Adj_A_Code   Account.A_Code%Type;
   V_Brn_Year         S_Brn.Brn_Year%Type;
   V_Brn_Usr          S_Brn.Brn_Usr%Type;
   V_Cmp_No           S_Brn.Cmp_No%Type;   
   V_Rec              Number;
   V_Doc_No           Number;
   V_Doc_Ser          Number;
   V_Doc_Date         Date;
Begin
 
--##------------------------------------------------------------------------------------##--

   Begin
      Select 1
        Into V_Cnt
        From IAS_POS_MINUS_QTY_TMP
       Where Rownum <= 1;
   Exception
      When Others Then
         V_Cnt := 0;
   End;

   If Nvl (V_Cnt, 0) > 0  Then
--##-----------------------------------------------------------------------------------##--
      Declare 
            Cursor C_Brn Is Select Distinct Brn_No From Ias_Pos_Minus_Qty_Tmp  Order By Brn_No ;
       Begin
           For  I_Brn In C_Brn Loop
                --## Get Brn_Info.
                        
                        
                 If I_Brn.Brn_No Is Null Then
                    Raise_Application_Error ( -20003,Ias_Gen_Pkg.Get_Msg (1, 449) || ' Brn No Is Null ');
                 Else
                    V_Cmp_No := Ias_Brn_Pkg.Get_Br_Cmp (I_Brn.Brn_No);
                            
                     Select Brn_Year, Brn_Usr
                       Into V_Brn_Year, V_Brn_Usr
                       From S_Brn
                      Where Brn_No = I_Brn.Brn_No;
                 End If;
--##-----------------------------------------------------------------------------------##--
                 --## Get Serial For Stk.Adjustment
                 Begin
                   -- Stopped Temporary 
                   --V_Doc_No := Ias_Doc_Serial_Pkg.Stk_Adj_Serial (P_Brn_No => I_Brn.Brn_No);
                     V_Doc_No := 1 ;
                 Exception
                  When Others Then
                      Raise_Application_Error (-20004, ' Err. In Ias_Doc_Serial_Pkg ');
                 End;
                    
                 V_Doc_Ser := V_Brn_Year||Lpad(I_Brn.Brn_No,6,'0')||110||V_Doc_No   ;

--##-----------------------------------------------------------------------------------##--
                  --## Get Stk Adjustment Interface Account
                  Begin
                     Select Stk_Adj_A_Code
                       Into V_Stk_Adj_A_Code
                       From Interface_Acc
                      Where Brn_No = I_Brn.Brn_No And Rownum <= 1;
                  Exception
                     When Others Then
                        Raise_Application_Error ( -20005, ' Enter Stk.Adj. Account In Interface Acc. ');
                  End;
--##-----------------------------------------------------------------------------------##--
                  Begin
                     Select Min (Stk_Type)
                       Into V_Stk_Type
                       From Ias_Stk_Adjst_Types
                      Where Rownum <= 1;
                  Exception
                     When Others
                     Then
                        Raise_Application_Error (-20006,' Err. When Get Min(Stk.Adj.Type) ');
                  End;

                  V_Doc_Date := To_Date (Ias_Gen_Pkg.Get_Sysdate, 'DD/MM/RRRR');
--##-----------------------------------------------------------------------------------##--      
                  Begin
                     Insert Into Stk_Adjustment (Stk_Type,
                                                 Adjust_Type,
                                                 Doc_No,
                                                 Doc_Ser,
                                                 Doc_Date,
                                                 Ref_No,
                                                 Stk_Desc,
                                                 A_Code,
                                                 A_Cy,
                                                 Stk_Acc_Rate,
                                                 Cc_Code,
                                                 Pj_No,
                                                 Actv_No,
                                                 Stk_Post,
                                                 Pr_Rep,
                                                 Hung,
                                                 Fill_Type,
                                                 Doc_Brn_No,
                                                 Audit_Ref,
                                                 Audit_Ref_Desc,
                                                 Audit_Ref_U_Id,
                                                 Audit_Ref_Date,
                                                 Ad_U_Id,
                                                 Ad_Date,
                                                 Up_U_Id,
                                                 Up_Date,
                                                 Up_Cnt,
                                                 Post_U_Id,
                                                 Post_Date,
                                                 Unpost_U_Id,
                                                 Unpost_Date,
                                                 Cmp_No,
                                                 Brn_No,
                                                 Brn_Year,
                                                 Brn_Usr)
                          Values (V_Stk_Type,
                                  1,
                                  V_Doc_No,
                                  V_Doc_Ser,
                                  V_Doc_Date,
                                  'Stk.Auto',
                                  Ias_Gen_Pkg.Get_Prompt (1, 3108),
                                  V_Stk_Adj_A_Code,
                                  Ias_Gen_Pkg.Get_Stk_Cur,
                                  Ias_Gen_Pkg.Get_Cur_Rate (Ias_Gen_Pkg.Get_Stk_Cur),
                                  Null,
                                  Null,
                                  Null,
                                  0,
                                  0,
                                  0,
                                  Null,
                                  I_Brn.Brn_No,
                                  0,
                                  Null,
                                  Null,
                                  Null,
                                  1,
                                  Ias_Gen_Pkg.Get_Sysdate,
                                  Null,
                                  Null,
                                  0,
                                  Null,
                                  Null,
                                  Null,
                                  Null,
                                  V_Cmp_No,
                                  I_Brn.Brn_No,
                                  V_Brn_Year,
                                  V_Brn_Usr);
                  Exception
                     When Others Then
                        Raise_Application_Error (-20007,'Error When Insert Into Stk_Adjustment '|| Chr (13)|| Sqlerrm);
                  End;

--##-----------------------------------------------------------------------------------##--
                  Begin
                     Ias_Itm_Inv_Pkg.Insrt_Gr_Mst ( P_Doctype    => 15,
                                                    P_Gr_No      => V_Doc_No,
                                                    P_G_Ser      => V_Doc_Ser,
                                                    P_Doc_Ser    => V_Doc_Ser,
                                                    P_Doc_Date   => V_Doc_Date,
                                                    P_A_Code     => Null,
                                                    P_Acy        => Ias_Gen_Pkg.Get_Stk_Cur,
                                                    P_C_Code     => Null,
                                                    P_Acrate     => Ias_Gen_Pkg.Get_Cur_Rate (Ias_Gen_Pkg.Get_Stk_Cur),
                                                    P_Stkrate    => Ias_Gen_Pkg.Get_Cur_Rate (Ias_Gen_Pkg.Get_Stk_Cur),
                                                    P_Gramt      => Null,
                                                    P_Pi_No      => Null,
                                                    P_Cc_Code    => Null,
                                                    P_Pj_No      => Null,
                                                    P_Actv_No    => Null,
                                                    P_W_Code     => Null,
                                                    P_Refno      => 'Stk.Auto',
                                                    P_Desc       => Ias_Gen_Pkg.Get_Prompt (1, 3108),
                                                    P_Cflag      => 1,
                                                    P_Pur_Type   => Null,
                                                    P_User_No    => 1,
                                                    P_Brn_No     => I_Brn.Brn_No,
                                                    P_Brn_Year   => V_Brn_Year,
                                                    P_Cmp_No     => V_Cmp_No,
                                                    P_Brn_Usr    => V_Brn_Usr);
                  Exception
                     When Others Then
                        Raise_Application_Error ( -20008, 'Error When Insert Into Gr_Note ' || Chr (13) || Sqlerrm);
                  End;
--##-----------------------------------------------------------------------------------##--
                  Declare
                     Cursor C_Stk_Dtl Is
                        Select I_Code,
                               W_Code,
                               Expire_Date,
                               Batch_No,
                               Nvl(P_Qty,0)-Nvl(Avl_Qty,0) P_Qty,
                               Nvl(Avl_Qty,0) Avl_Qty,
                               Ias_Itm_Pkg.Get_Icode_Min_Unit (P_I_Code => I_Code) Itm_Unt 
                          From Ias_Pos_Minus_Qty_Tmp 
                          Where Brn_No =I_Brn.Brn_No;
--##-----------------------------------------------------------------------------------##--
                      Begin
                         V_Rec := 0;
                        
                         For I In C_Stk_Dtl
                         Loop
--##-----------------------------------------------------------------------------------##--
                                Begin
                                   Select Ias_Doc_Seq.Nextval Into V_Seq From Dual;
                                Exception
                                   When Others Then
                                      Raise_Application_Error ( -20009,'Error In Ias_Doc_Seq ' || Chr (13) || Sqlerrm);
                                End;

--##-----------------------------------------------------------------------------------##--
                                --## Get WatAvg Before
                                If Ias_Gen_Pkg.Get_Cnt ('Select Costing_Type From Ias_Para_Inv Where RowNum <= 1 ') = 2 Then                                                      -- Wtavg
                                   Begin
                                      V_Wt_Before := Nvl (Ias_Itm_Pkg.Get_Grand_Wtavg ( P_Wtavg_Type   => Ias_Gen_Pkg.Get_Cnt ('Select Wtavg_Type From Ias_Para_Inv Where RowNum <= 1 '),
                                                                                        P_Icode        => I.I_Code,
                                                                                        P_Wcode        => I.W_Code),0);
                                   Exception
                                      When Others  Then
                                         Raise_Application_Error ( -20010, 'Error When Get WatAvg Before Cost ' || Chr (13)|| Sqlerrm);
                                   End;
                                Else                                                       -- fifo
                                   V_Wt_Before :=
                                      Last_Incoming_Price (P_Wtavg_Type   => Ias_Gen_Pkg.Get_Cnt ('Select Wtavg_Type From Ias_Para_Inv Where RowNum <= 1 '),
                                                           P_Icode        => I.I_Code ,
                                                           P_Psize        => 1        ,
                                                           P_Wcode        => I.W_Code ,
                                                           P_Type         => 1        );
                                End If;

--##-----------------------------------------------------------------------------------##--
                                V_Rec := V_Rec + 1;
                    
                                Begin
                                   Insert Into Stk_Adjustment_Det (Adjust_Type,
                                                                   Doc_No,
                                                                   Doc_Ser,
                                                                   I_Code,
                                                                   Itm_Unt ,
                                                                   W_Code,
                                                                   Expire_Date,
                                                                   Batch_No,
                                                                   Barcode,
                                                                   Wtavg,
                                                                   Avl_Qty,
                                                                   Pls_Mins,
                                                                   P_Size,
                                                                   P_Qty,
                                                                   Use_Serialno,
                                                                   Rcrd_No,
                                                                   Doc_Sequence,
                                                                   Item_Desc,
                                                                   Man_P_Qty,
                                                                   Man_Avl_Pqty,
                                                                   Pi_Price,
                                                                   Pi_I_Qty,
                                                                   Pr_I_Qty,
                                                                   Bill_Disc,
                                                                   Doc_Type_Ref,
                                                                   Doc_No_Ref,
                                                                   Doc_Ser_Ref,
                                                                   V_Code,
                                                                   Cc_Code,
                                                                   Pj_No,
                                                                   Actv_No,
                                                                   Inc_Qty,
                                                                   Inc_Cost,
                                                                   Bal_Qty,
                                                                   Real_Cost,
                                                                   I_Length,
                                                                   I_Width,
                                                                   I_Height,
                                                                   I_Number,
                                                                   Post_Code,
                                                                   Cmp_No,
                                                                   Brn_No,
                                                                   Brn_Year,
                                                                   Brn_Usr)
                                        Values (  V_Stk_Type ,
                                                  V_Doc_No,
                                                  V_Doc_Ser,
                                                  I.I_Code,
                                                  I.Itm_Unt,
                                                  I.W_Code,
                                                  Nvl (I.Expire_Date, To_Date('01/01/1900','DD/MM/YYYY')),
                                                  Nvl (I.Batch_No, '0'),
                                                  Null,
                                                  V_Wt_Before,
                                                  0,
                                                  I.P_Qty,
                                                  1,
                                                  I.P_Qty,
                                                  0,
                                                  V_Rec,
                                                  V_Seq,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Ias_Vndr_Pkg.Get_Vndr_For_Itm (I.I_Code   ,
                                                                                 Null     ) ,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Null,
                                                  Get_Post_Code_Inv (Ias_Gen_Pkg.Get_Cnt ('Select Item_Posting_Flag From Ias_Para_Inv Where Rownum <= 1 '),
                                                                     I.I_Code,
                                                                     I.W_Code),
                                                  V_Cmp_No,
                                                  I_Brn.Brn_No,
                                                  V_Brn_Year,
                                                  V_Brn_Usr);
                                Exception
                                   When Others Then
                                      Raise_Application_Error (-20011,'Error When Insrt Stk.Adjustment Det '|| Chr (13) || Sqlerrm);
                                      Rollback;
                                End;

--##-----------------------------------------------------------------------------------##--
                                --## Calc_WatAvg
                                Begin
                                   V_Wt_After :=
                                      Calc_Wtavg_Cost (P_Cost_Type    => Ias_Gen_Pkg.Get_Cnt ('Select Costing_Type From Ias_Para_Inv Where RowNum <= 1 '),
                                                       P_Wtavg_Type   => Ias_Gen_Pkg.Get_Cnt ('Select Wtavg_Type From Ias_Para_Inv Where RowNum <= 1 '),
                                                       P_Icode        => I.I_Code,
                                                       P_Iqty         => I.P_Qty,
                                                       P_Icost        => Nvl (V_Wt_Before, 0),
                                                       P_Psize        => 1,
                                                       P_Wcode        => I.W_Code,
                                                       P_Frc_No       => 6,
                                                       P_Brn_No       => I_Brn.Brn_No,
                                                       P_Brn_Year     => V_Brn_Year,
                                                       P_Cmp_No       => V_Cmp_No,
                                                       P_Brn_Usr      => V_Brn_Usr);
                                Exception
                                   When Others Then
                                      Raise_Application_Error (-20012, 'Err. In Calc.WtAvg Error ' || Chr (13) || Sqlerrm);
                                End;

--##-----------------------------------------------------------------------------------##--
                                --## Insert Into Storage
                                Begin
                                   Ias_Itm_Inv_Pkg.Insrt_Ias_Itm_Wcode (P_Icode      => I.I_Code,
                                                                        p_Itm_Unt    => Ias_Itm_Pkg.Get_Icode_Min_Unit (P_I_Code =>I.I_Code),
                                                                        P_Psize      => 1,
                                                                        P_W_Code     => I.W_Code);
                                Exception
                                   When Others Then
                                      Raise_Application_Error (-20012,'Error When Insert Storage ' || Chr (13) || Sqlerrm);
                                End;
--##-----------------------------------------------------------------------------------##--
                                --## Insert Into Gr_Detail
                                Begin
                                   Ias_Itm_Inv_Pkg.Insrt_Gr_Dtl ( P_Doctype        => 15,
                                                                  P_Gr_No          => V_Doc_No,
                                                                  P_G_Ser          => V_Doc_Ser,
                                                                  P_Doc_Ser        => V_Doc_Ser,
                                                                  P_Docseq         => V_Seq,
                                                                  P_Doc_Date       => V_Doc_Date,
                                                                  P_Acy            => Ias_Gen_Pkg.Get_Stk_Cur,
                                                                  P_Acrate         => Ias_Gen_Pkg.Get_Cur_Rate (Ias_Gen_Pkg.Get_Stk_Cur),
                                                                  P_Stkrate        => Ias_Gen_Pkg.Get_Cur_Rate (Ias_Gen_Pkg.Get_Stk_Cur),
                                                                  P_Pi_No          => Null,
                                                                  P_Pur_Type       => Null,
                                                                  P_W_Code         => I.W_Code, 
                                                                  P_Cc_Code        => Null,
                                                                  P_Pj_No          => Null,
                                                                  P_Actv_No        => Null,
                                                                  P_Icode          => I.I_Code,
                                                                  P_Itm_Unt          => I.Itm_Unt,
                                                                  P_Iqty           => I.P_Qty,
                                                                  P_Freeqty        => 0,
                                                                  P_Psize          => 1,
                                                                  P_Iprice         => V_Wt_Before,
                                                                  P_Cprice         => Nvl (V_Wt_Before, 0),
                                                                  P_Stkcost        => Nvl (V_Wt_Before, 0),
                                                                  P_Wtavg_Before   => Nvl (V_Wt_Before, 0),
                                                                  P_Wtavg_After    => Nvl (V_Wt_After, 0),
                                                                  P_Vatper         => Null,
                                                                  P_Vatamt         => Null,
                                                                  P_Expdate        => Nvl (I.Expire_Date, To_Date('01/01/1900','DD/MM/YYYY')),
                                                                  P_Batchno        => Nvl (I.Batch_No, '0'),
                                                                  P_Rcrdno         => V_Rec,
                                                                  P_Use_Serial     => 0,
                                                                  P_Brn_No         => I_Brn.Brn_No,
                                                                  P_Brn_Year       => V_Brn_Year,
                                                                  P_Cmp_No         => V_Cmp_No,
                                                                  P_Brn_Usr        => V_Brn_Usr);
                                Exception
                                   When Others Then
                                      Raise_Application_Error ( -20013,'Error In Gr_Detail ' || Chr (13) || Sqlerrm);
                                End;

--##-----------------------------------------------------------------------------------##--
                                --## Insert Into Item_movement
                                Begin
                                   Ias_Itm_Inv_Pkg.Insrt_Item_Move (  P_Doctype       => 15,
                                                                      P_Billdoctype   => 1,
                                                                      P_Docno         => V_Doc_No,
                                                                      P_Icode         => I.I_Code,
                                                                      P_Itm_Unt       => I.Itm_Unt,
                                                                      P_Iqty          => I.P_Qty,
                                                                      P_Freeqty       => 0,
                                                                      P_Psize         => 1,
                                                                      P_Idate         => V_Doc_Date,
                                                                      P_Iprice        => V_Wt_Before,
                                                                      P_Wcode         => I.W_Code,
                                                                      P_Stkcost       => Nvl (V_Wt_Before, 0),
                                                                      P_Vatamt        => Null,
                                                                      P_Acy           => Ias_Gen_Pkg.Get_Stk_Cur,
                                                                      P_Ac_Rate       => Ias_Gen_Pkg.Get_Cur_Rate (Ias_Gen_Pkg.Get_Stk_Cur),
                                                                      P_Stk_Rate      => Ias_Gen_Pkg.Get_Cur_Rate (Ias_Gen_Pkg.Get_Stk_Cur),
                                                                      P_Cc_Code       => Null,
                                                                      P_Pj_No         => Null,
                                                                      P_Actv_No       => Null,
                                                                      P_C_Code        => Null,
                                                                      P_Adesc         => Ias_Gen_Pkg.Get_Prompt (1, 3108),
                                                                      P_Expdate       => Nvl (I.Expire_Date, To_Date('01/01/1900','DD/MM/YYYY')),
                                                                      P_Batchno       => Nvl (I.Batch_No, '0'),
                                                                      P_Rcrdno        => V_Rec,
                                                                      P_Refno         => 'Stk.Auto',
                                                                      P_Docser        => V_Doc_Ser,
                                                                      P_Docseq        => V_Seq,
                                                                      P_Rt_Type       => Null,
                                                                      P_Inout         => 1,
                                                                      P_Extrnl_Pst    => 2,
                                                                      P_Ad_Date       => Ias_Gen_Pkg.Get_Curdate,
                                                                      P_Up_Date       => Null,
                                                                      P_Brn_No        => I_Brn.Brn_No,
                                                                      P_Brn_Year      => V_Brn_Year,
                                                                      P_Cmp_No        => V_Cmp_No,
                                                                      P_Brn_Usr       => V_Brn_Usr);
                                Exception
                                   When Others Then
                                      Raise_Application_Error (-20014,'Error When Inserting Itm_Movement '|| Chr (13) || Sqlerrm);
                                End;

--##-------------------------------------------------------------------------------------##--
                                --## Posting Doc.
                                Begin
                                   Ias_Post_In_Sav_Pkg.Post_Doc_In_Sav (G_Doc_Type   => 10        ,
                                                                        G_Doc_Ser    => V_Doc_Ser ,
                                                                        P_Jv_Type    => 1         ,
                                                                        P_Doc_No     => V_Doc_No  ,
                                                                        P_Lang_No    => 1         ,
                                                                        P_User_No    => 1         ,
                                                                        G_Post_Type  => 0         );
                                Exception
                                   When No_Data_Found Then
                                      Null;
                                   When Others  Then
                                      Raise_Application_Error (-20015, 'Error When Posting Stk_Adjustment  '|| Chr (13)|| 'Doc_Ser =' || V_Doc_Ser || Chr (13)|| Sqlerrm);
                                End;
--##-------------------------------------------------------------------------------------##--
                         End Loop;
                      End;

--##------------------------------------------------------------------------------------##--
           End Loop ;
       End ;
--##------------------------------------------------------------------------------------##--
     -- Commit;
   End If;
--##------------------------------------------------------------------------------------##--
 End Post_Stk_Adjstmnt;
 --##------------------------------------------------------------------------------------##--
Procedure Post_Jv Is
   Cursor C_Jv Is Select J_Ser,Jv_Type,J_Doc_No,Ad_U_Id From Master_Journal_V 
                      Where Nvl(Stand_By,0)=0 
                        And J_Ser In ( Select J_Ser From Master_Journal_V Where Nvl(Stand_By,0)=0
                                       Minus
                                       Select Doc_Ser From Ias_Post_Mst Where Doc_Type=1);
Begin
      For I In C_Jv Loop  
        Ias_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => 1            ,
                                              G_Doc_Ser     => I.J_Ser      ,
                                              P_Jv_Type     => I.Jv_Type    ,
                                              P_Doc_No      => I.J_Doc_No   ,
                                              P_Lang_No     => 1            ,
                                              P_User_No     => I.Ad_U_Id    ,
                                              G_Post_Type   => 0            );
      End Loop;          
Exception When Others Then
         Null;                                                    
End Post_Jv;                                 
--##------------------------------------------------------------------------------------##--
Procedure Post_Vchr Is
   Cursor C_Vchr Is Select Decode(Voucher_Type,1,2,2,3) Doc_Type,V_Ser,Voucher_Pay_Type,Voucher_No,Ad_U_Id From Vouchers 
                        Where Nvl(Stand_By,0)=0 
                          And V_Ser In ( Select V_Ser From Vouchers Where Nvl(Stand_By,0)=0
                                         Minus
                                         Select Doc_Ser From Ias_Post_Mst Where Doc_Type In (2,3));
Begin
    ------------------------------------------------------------------------------------------------------------------------------------    
      For I In C_Vchr Loop  
        Ias_Post_In_Sav_Pkg.Post_Doc_In_Sav ( G_Doc_Type    => I.Doc_Type          ,
                                              G_Doc_Ser     => I.V_Ser             ,
                                              P_Jv_Type     => I.Voucher_Pay_Type  ,
                                              P_Doc_No      => I.Voucher_No        ,
                                              P_Lang_No     => 1                   ,
                                              P_User_No     => I.Ad_U_Id           ,
                                              G_Post_Type   => 0                   );
      End Loop;
        
      
Exception When Others Then
         Null;                                                    
End Post_Vchr;  
--##------------------------------------------------------------------------------------##-
PROCEDURE Insrt_Tax (P_Doc_Type In Number , P_Doc_Ser In Number) Is
BEGIN
  Insert InTo Gnr_Tax_Itm_Movmnt ( Doc_Type, Bill_Doc_Type, Doc_Jv_Type, Doc_No, Doc_Ser, Doc_Date, Tax_No, Clc_Typ_No, Agncy_No, I_Code, Itm_Unt, P_Size, I_Price, Disc_Amt, A_Code, A_Cy, Ac_Rate, 
                                   Tax_Prcnt, Tax_Amt, W_Code, Cc_Code, Pj_No, Actv_No, Rcrd_No, Doc_Sequence, External_Post, Cmp_No, Brn_No, Brn_Year, Brn_Usr, Tax_Amt_L, I_Qty, Free_Qty, 
                                   Ref_No, Stk_Cost, Stk_Rate,CLC_TAX_FREE_QTY_FLG)
                            Select Doc_Type, Bill_Doc_Type, Doc_Jv_Type, Doc_No, Doc_Ser, Doc_Date, Tax_No, Clc_Typ_No, Agncy_No, I_Code, Itm_Unt, P_Size, I_Price, Disc_Amt, A_Code, A_Cy, Ac_Rate, 
                                   Tax_Prcnt, Tax_Amt, W_Code, Cc_Code, Pj_No, Actv_No, Rcrd_No, Doc_Sequence, External_Post, Cmp_No, Brn_No, Brn_Year, Brn_Usr, Tax_Amt_L, I_Qty, Free_Qty, 
                                   Ref_No, Stk_Cost, Stk_Rate ,CLC_TAX_FREE_QTY_FLG
                              From Gnr_Tax_Itm_Movmnt_Br
                             Where Doc_Type = P_Doc_Type 
                               And Doc_Ser  = P_Doc_Ser;
                                    
Exception 
      When No_Data_Found Then Null;                            
    When Others Then
    Rollback; 
    Raise_Application_Error (-20015, 'Error When Into Gnr_Tax_Itm_Movmnt '|| Chr (13)|| 'Doc_Ser =' ||P_Doc_Ser || Chr (13)|| Sqlerrm);        
END;
--##------------------------------------------------------------------------------------##--
PROCEDURE Insrt_Point_Trns (P_Doc_Type In Number , P_Doc_Ser In Number) Is 
BEGIN
 Insert InTo Ias_Point_Calc_Trns (Trns_Date, Cust_Code, Mobile_No, Point_Typ_No, Bill_No, Rt_Bill_No, Doc_Amt, A_Cy, Point_Cnt, Trns_Type, Machine_No, 
                                  Expire_Date, Bill_Amt, External_Post, Doc_No, Doc_Srl, Doc_Typ, Ac_Rate, Point_Amt,Ad_U_Id, Ad_Date, Up_U_Id, 
                                  Up_Date, Up_Cnt, Cmp_No, Brn_No, Brn_Year, Brn_Usr)
                           Select Trns_Date, Cust_Code, Mobile_No, Point_Typ_No, Bill_No, Rt_Bill_No, Doc_Amt, A_Cy, Point_Cnt, Trns_Type, Machine_No, 
                                  Expire_Date, Bill_Amt, External_Post, Doc_No, Doc_Srl, Doc_Typ, Ac_Rate, Point_Amt,Ad_U_Id, Ad_Date, Up_U_Id, 
                                  Up_Date, Up_Cnt, Cmp_No, Brn_No, Brn_Year, Brn_Usr
                             From Ias_Point_Calc_Trns_Br
                            Where Doc_Typ = P_Doc_Type 
                              And Doc_Srl  = P_Doc_Ser
                              And TRNS_TYPE IN (1,2);
  Exception 
      When No_Data_Found Then Null;                            
    When Others Then 
    Rollback;
    Raise_Application_Error (-20015, 'Error When Into Insrt_Point_Trns '|| Chr (13)|| 'Doc_Ser =' || P_Doc_Ser || Chr (13)|| Sqlerrm);        
END;
--##------------------------------------------------------------------------------------##--
PROCEDURE Post_Serial (P_Doc_Ser In Number , P_Doc_Type In Number)IS
BEGIN
  
         Begin
                 Insert InTo Ias_Item_Serialno(Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, Doc_Date, I_Code, Serialno, Desc_No, W_Code, Cc_Code, Pj_No, Actv_No, Expire_Date, Batch_No, Free_Flg, Bill_Cost, 
                                               Out_No, Out_Gr_Ser, In_Out, Rcrd_No, Rcrd_No_Doc, Active, Active_U_Id, Active_Date, Active_Note, External_Post, Ad_Date, Up_Date, Cmp_No, Brn_No, Brn_Year, 
                                               Brn_Usr, Itm_Unt, P_Size)
                Select Doc_Type, Bill_Doc_Type, Doc_No, Doc_Ser, Doc_Date, I_Code, Serialno, Desc_No, W_Code, Cc_Code, Pj_No, Actv_No, Expire_Date, Batch_No, Free_Flg, Bill_Cost, 
                                               Out_No, Out_Gr_Ser, In_Out, Rcrd_No, Rcrd_No_Doc, Active, Active_U_Id, Active_Date, Active_Note, External_Post, Ad_Date, Up_Date, Cmp_No, Brn_No, Brn_Year, 
                                               Brn_Usr, Itm_Unt, P_Size
               From Ias_Item_Serialno_Br
               Where Doc_Ser   = P_Doc_Ser
                 And Doc_Type  = P_Doc_Type;
          Exception When Others Then
          Rollback;                                                    
             Raise_Application_Error (-20015, 'Error IN Post_Serial '|| Chr (13)|| 'Doc_Ser =' || P_Doc_Ser || Chr (13)|| Sqlerrm);                                                  
          End;
                  
END;
--##-----------------------------------------------------------------------------------##---
FUNCTION Get_Card_Comm_Prcnt (P_Cr_Card_No In Number) RETURN Number IS
  v_comm_per Number:=0;
BEGIN
  If P_Cr_Card_No Is Not Null Then
     Begin
      Select D.comm_per Into v_comm_per
        From Credit_card_types D,Ias_Cr_Card_Types M 
       Where M.Cr_Card_Type=D.Cr_Card_Type
         And D.cr_card_no=P_Cr_Card_No
         And RowNum<=1;
    Exception 
      When Others Then v_comm_per:=0;
    End;
End If;
Return (v_comm_per);
END;
--##-----------------------------------------------------------------------------------##---
--##-----------------------------------------------------------------------------------##---
--##-----------------------------------------------------------------------------------##---
Procedure Post_Trns_Data_Auto Is 
  Cursor C_Post Is Select Doc_Type,Doc_Ser,Doc_Sequence From 
          (Select 1 Doc_Type,M.Bill_Ser Doc_Ser,Min(Doc_Sequence) Doc_Sequence
            From Ias_Bill_Mst_Br M,Ias_Bill_Dtl_Br D
           Where M.Bill_Ser = D.Bill_Ser 
            And Nvl(M.Stand_By,0)=0 
            And Nvl(M.Bill_Post,0)=0
            And Exists(Select 1 From Ias_Bill_Dtl_Br Where Bill_Ser=M.Bill_Ser And Rownum<=1)
            And Not Exists(Select 1 From Ias_Bill_Mst Where Bill_Ser=M.Bill_Ser And Rownum<=1)
          Group By M.Bill_Ser  
          Union All
          Select 3 Doc_Type,M.Rt_Bill_Ser Doc_Ser,Min(Doc_Sequence) Doc_Sequence
            From Ias_Rt_Bill_Mst_Br M,Ias_Rt_Bill_Dtl_Br D
           Where M.Rt_Bill_Ser = D.Rt_Bill_Ser 
            And Nvl(M.Stand_By,0)=0 
            And Nvl(M.Rt_Bill_Post,0)=0
            And Exists(Select 1 From Ias_Rt_Bill_Dtl_Br Where Rt_Bill_Ser=M.Rt_Bill_Ser And Rownum<=1)
            And Not Exists(Select 1 From Ias_Rt_Bill_Mst Where Rt_Bill_Ser=M.Rt_Bill_Ser And Rownum<=1)
          Group By M.Rt_Bill_Ser
          Union All
          Select 5 Doc_Type,M.G_Ser Doc_Ser,Min(Doc_Sequence) Doc_Sequence
            From Gr_Note_Br M,Gr_Detail_Br D
           Where M.G_Ser = D.G_Ser 
            And M.Pi_Type=5
            And Nvl(M.Hung,0)=0 
            And Nvl(M.Gr_Post,0)=0
            And Exists(Select 1 From Gr_Detail_Br Where G_Ser=M.G_Ser And Rownum<=1)
            And Not Exists(Select 1 From Gr_Note Where G_Ser=M.G_Ser And Rownum<=1)
          Group By M.G_Ser
          Union All
          Select 6 Doc_Type,M.Out_Ser Doc_Ser,Min(Doc_Sequence) Doc_Sequence
            From Ias_Outgoing_Mst_Br M,Ias_Outgoing_Dtl_Br D
           Where M.Out_Ser = D.Out_Ser 
            And Nvl(M.Hung,0)=0 
            And Nvl(M.Out_Post,0)=0
            And Exists(Select 1 From Ias_Outgoing_Dtl_Br Where Out_Ser=M.Out_Ser And Rownum<=1)
            And Not Exists(Select 1 From Ias_Outgoing_Mst Where Out_Ser=M.Out_Ser And Rownum<=1)
          Group By M.Out_Ser
          Union All      
          Select Decode(M.Tr_InOut_Type,1,7,2,8) Doc_Type,M.Tr_Ser Doc_Ser,Min(Doc_Sequence) Doc_Sequence
            From Ias_Whtrns_Mst_Br M,Ias_Whtrns_Dtl_Br D
           Where M.Tr_Ser = D.Tr_Ser 
             And Nvl(M.Hung,0)=0 
             And Nvl(M.Tr_Post,0)=0
             And Exists(Select 1 From Ias_Whtrns_Dtl_Br Where Tr_Ser=M.Tr_Ser And Rownum<=1)
             And Not Exists(Select 1 From Ias_Whtrns_Mst Where Tr_Ser=M.Tr_Ser And Rownum<=1)
          Group By Decode(M.Tr_InOut_Type,1,7,2,8),M.Tr_Ser)
          Order By Doc_Sequence;
 Begin
    For I In C_Post Loop
      If I.Doc_Type=1 Then
         -------------------------------------------------------------------
         Post_Sales_Detail ( P_Doc_Ser => I.Doc_Ser ,P_Use_Adjstmnt => 0 );         
         -------------------------------------------------------------------         
      ElsIf I.Doc_Type=3 Then
         -------------------------------------------------------------------
         Post_Rt_Sales_Detail ( P_Doc_Ser => I.Doc_Ser );         
         -------------------------------------------------------------------                       
      ElsIf I.Doc_Type=5 Then
         -------------------------------------------------------------------
         Post_Incmng ( P_Doc_Ser  => I.Doc_Ser );         
         -------------------------------------------------------------------
      ElsIf I.Doc_Type=7 Then
         -------------------------------------------------------------------
         Post_Transfer_Out ( P_Doc_Ser => I.Doc_Ser ,P_Use_Adjstmnt => 0 );         
         -------------------------------------------------------------------   
      ElsIf I.Doc_Type=8 Then
         -------------------------------------------------------------------
         Post_Transfer_In ( P_Doc_Ser  => I.Doc_Ser );         
         -------------------------------------------------------------------
      ELsIf I.Doc_Type=6 Then
         -------------------------------------------------------------------
         Post_OutGoing ( P_Doc_Ser => I.Doc_Ser ,P_Use_Adjstmnt => 0 );         
         -------------------------------------------------------------------
      End If;      
      Commit;         
    End Loop;       
    ------------------------------------------------------------    
    Post_Incmng;
    Post_Rt_Sales_Detail;
    Post_Transfer_In;
    Post_Sales_Detail;
    Post_Transfer_Out;
    Post_OutGoing;
    Post_Jv;
    Post_Vchr;
    Commit;                  
End Post_Trns_Data_Auto ;    
    
End YS_POST_INV_TRNS_PKG ;