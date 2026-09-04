--- SPEC ---
PACKAGE Ias_Insrt_Out_Bills_Pkg AS
  FUNCTION  Get_Out_No      ( P_Invs    In Number, P_Si_Type  In Number, P_Cc_Code In Varchar2,P_w_code  In Number,  P_bill_doc_type In Number,P_Brn_No In Number) Return Number;    
  FUNCTION  Get_Out_Ser     ( P_Out_No  In Number, P_Si_Type  In Number, P_Invs    In Number,  P_Cc_Code In Varchar2,P_w_code        In Number,P_bill_doc_type In Number,P_Brn_No In Number,P_Brn_Year In Number) Return Number;
  PROCEDURE Insrt_Out_Bills ( P_Invs    In Number, P_Out_Avlqty In Number Default 0 , P_Doc_Ser  In Number, P_Out_No  In Number,  P_Out_Ser In Number,P_Extrnl_Post Number,P_Lang_No Number,P_Brn_No In Number);
  FUNCTION  Get_Ret_No      ( P_Invs_Sr In Number, P_Sr_Type  In Number, P_Cc_Code In Varchar2,P_w_code  In Number,  P_bill_doc_type In Number,P_Brn_No In Number) Return Number;    
  FUNCTION  Get_Ret_Ser     ( P_Ret_No  In Number, P_Sr_Type  In Number, P_Invs_Sr In Number,  P_Cc_Code In Varchar2,P_w_code        In Number,P_bill_doc_type In Number,P_Brn_No In Number,P_Brn_Year In Number) Return Number;
  PROCEDURE Insrt_Ret_Bills ( P_Invs_Sr In Number, P_Pyear    In Number, P_Doc_Ser In Number,  P_Ret_No  In Number,  P_Ret_Ser In Number, P_Out_No  In Number, P_Out_Ser In Number, P_Extrnl_Post Number, P_Lang_No Number,P_Brn_No In Number);  
END Ias_Insrt_Out_Bills_Pkg;

--- BODY ---
PACKAGE BODY Ias_Insrt_Out_Bills_Pkg AS
--=====================================================================================--
FUNCTION Get_Out_No (P_Invs In Number,P_Si_Type  In Number,P_Cc_Code In Varchar2,P_w_code In Number,P_bill_doc_type In Number,P_Brn_No In Number) Return Number Is 
  V_Out_No Number;
  V_BRN_YEAR NUMBER;
BEGIN 

      Begin
         Select Max(Yr_No)
           Into V_BRN_YEAR
           From S_Prd_Dtl
          Where To_Date(SYSDATE, 'DD/MM/RRRR') Between F_Date And T_Date;
      Exception
         When Others Then
            Null;
      End;
    V_Out_No:=AR_DOC_SQ_PKG.GET_DOC_NO ( P_DOC_TYP        =>13,
                                          P_PAY_TYP       =>P_bill_doc_type,    
                                          P_BRN_YEAR      =>V_BRN_YEAR,
                                          P_BRN_NO        =>P_Brn_No,
                                          P_CC_CODE       =>P_Cc_Code,
                                          P_W_CODE        =>P_w_code,
                                          P_TYP_NO        =>P_Si_Type     );    
   
   Return(V_Out_No);
   
   Exception when others Then
      Return(0);
 END;
--=====================================================================================--
 FUNCTION Get_Out_Ser (P_Out_No In Number, P_Si_Type  In Number,P_Invs In Number, P_Cc_Code In Varchar2,P_w_code In Number,P_bill_doc_type In Number,P_Brn_No In Number,P_Brn_Year In Number) Return Number Is 
  V_Out_Ser Number;
  V_c_sr    Number;
  V_cc_no   Number;
  V_w_sr    Number;
BEGIN   
  -------------------------------------------------------------------------------------       
 /* If P_Invs In (3,6) Then      
       V_c_sr:=ias_cc_code_pkg.Get_Cc_ser(P_Cc_Code);
       V_cc_no:=ias_cc_code_pkg.Get_Cc_no(P_Cc_Code);                               
  ElsIf P_Invs = 4 Then          
     V_W_Sr := IAS_Wcode_Pkg.Get_Wc_Ser(P_W_Code);        
  End If;  */             
  -------------------------------------------------------------------------------------   
   V_Out_Ser:=AR_DOC_SQ_PKG.GET_DOC_SRL ( P_DOC_TYP     =>13,
                                          P_PAY_TYP       =>P_bill_doc_type,    
                                          P_BRN_YEAR      =>P_Brn_Year,
                                          P_BRN_NO        =>P_Brn_No,
                                          P_CC_CODE       =>P_Cc_Code,
                                          P_W_CODE        =>P_w_code,
                                          P_TYP_NO        =>P_Si_Type,
                                          P_DOC_NO        =>P_Out_No  );            
  -------------------------------------------------------------------------------------  
  Return(V_Out_Ser);
   Exception when others Then
     Return(0);     
 END;
--=====================================================================================-- 
 PROCEDURE Insrt_Out_Bills (P_Invs In Number , P_Out_Avlqty In Number Default 0 , P_Doc_Ser In Number, P_Out_No  In Number,  P_Out_Ser In Number, P_Extrnl_Post Number,P_Lang_No Number,P_Brn_No In Number) Is
   V_Use_Audit_Doc Number;
   V_Iqty          Number:=0;   
   V_Fqty          Number:=0;
   V_Iqty_Doc      Number:=0;   
   V_Avlqty        Number:=0;
   V_Cnt           Number;
   V_Stk_Cst       Number;
   V_costing_type  Number;
   V_wtavg_type    Number;
   V_Use_Itm_Attach Number;
   V_Use_Attch     Ias_Itm_Mst.Use_Attch%Type  ;
   V_Attch         Ias_Itm_Attach%RowType       ;
   V_Rec_Attch     Ias_Itm_Attach_Movement.Rec_Attch%Type ;  
   V_DOC_PST_SQ    Master_Out_Bills.DOC_PST_SQ%TYPE; 
 BEGIN
   ------------------------------------------------------------------------------------
        Begin
          Select  Nvl(Use_Audit_Doc,0)
            Into  V_Use_Audit_Doc 
          From Ias_Para_Gen  ;
        Exception
            When Others Then
             V_Use_Audit_Doc  := 0 ;
        End ;
        Begin
          Select  costing_type,
                  wtavg_type,
                  Use_Itm_Attach
            Into  V_costing_type,
                  V_wtavg_type,
                  V_Use_Itm_Attach
          From Ias_Para_Inv  ;
        Exception
            When Others Then
             null;
        End ;
        
   ------------------------------------------------------------------------------------
   Begin
     Select 1 InTo V_Cnt From Master_Out_Bills 
      Where Bill_Ser=P_Doc_Ser         
        And RowNum<=1;  
   Exception when others Then
     V_Cnt := 0;     
   END;
   If Nvl(V_Cnt,0)=1 Then
     Raise_application_error(-20801,Ias_Gen_Pkg.Get_Msg(P_Lang_No,1332)||' '||SqlErrm) ;
    End If; 
   ------------------------------------------------------------------------------------
   Begin
     Select 1 InTo V_Cnt From Master_Out_Bills 
      Where Out_Ser=P_Out_Ser         
        And RowNum<=1;  
   Exception when others Then
     V_Cnt := 0;     
   END;
   If Nvl(V_Cnt,0)=1 Then
     Raise_application_error(-20802,Ias_Gen_Pkg.Get_Msg(P_Lang_No,17)||' '||SqlErrm) ;
    End If;
   ------------------------------------------------------------------------------------
   Begin
     If P_Out_Avlqty=1 Then
        Select 1 InTo V_Cnt From Ias_Bill_Dtl D,Ias_Itm_Mst I
         Where D.Bill_Ser = P_Doc_Ser
           And D.I_Code   = I.I_Code
           And Nvl(D.Service_Item,0)=0 
           And (Case When Nvl(I.Use_qty_fraction,0)=0 And Get_icode_avlqty ( P_icode   => D.I_code,
                                                                             P_psize   => Nvl(D.P_size,1),
                                                                             P_wcode   => D.W_code,
                                                                             P_expdate => Nvl(D.Expire_date,'01/01/1900'),
                                                                             P_batchno => Nvl(D.Batch_no,'0'))>=1 Then 1
                     When Nvl(I.Use_qty_fraction,0)=1 And Get_icode_avlqty ( P_icode   => D.I_code,
                                                                             P_psize   => Nvl(D.P_size,1),
                                                                             P_wcode   => D.W_code,
                                                                             P_expdate => Nvl(D.Expire_date,'01/01/1900'),
                                                                             P_batchno => Nvl(D.Batch_no,'0'))>0 Then 1 End)=1                                                         
           And RowNum<=1;
     Else
         Select 1 InTo V_Cnt From Ias_Bill_Dtl 
         Where Bill_Ser=P_Doc_Ser
           And Nvl(Service_Item,0)=0 
           And RowNum<=1;
     End If;
        
                                                      
   Exception when others Then
     V_Cnt := 0;
   END; 
   ------------------------------------------------------------------------------------
   If Nvl(V_Cnt,0)=1 Then
       ------------------------------------------------------------------------------------ 
       V_DOC_PST_SQ:=IAS_POSTING_PKG.GET_DOC_PST_SQ;
       
                                      
       INSERT INTO master_out_bills ( out_no, 
                                      out_ser, 
                                      bill_doc_type,                                
                                      out_date,
                                      bill_currency, 
                                      bill_rate, 
                                      stock_rate,
                                      bill_no, 
                                      bill_ser,
                                      w_code,
                                      cc_code, 
                                      cash_no, 
                                      c_code, 
                                      c_name,
                                      a_code,
                                      pj_no,
                                      Actv_No, 
                                      driver_no, 
                                      r_code, 
                                      out_post,                                
                                      ref_no,                                
                                      a_desc, 
                                      External_Post,
                                      si_type,
                                      ad_u_id, 
                                      ad_date,
                                      UP_CNT,  
                                      brn_no, 
                                      brn_year,
                                      cmp_no, 
                                      brn_usr,
                                      Audit_Ref       ,
                                      Audit_Ref_Desc  ,
                                      Audit_Ref_U_Id  ,
                                      Audit_Ref_Date  ,
                                      Doc_Brn_No  ,
                                      DOC_PST_SQ    )                               
                              SELECT  P_Out_No,
                                      P_Out_Ser,                                    
                                      bill_doc_type,                                
                                      Bill_date,
                                      bill_currency, 
                                      bill_rate, 
                                      stock_rate,
                                      bill_no, 
                                      bill_ser,
                                      w_code,
                                      cc_code, 
                                      cash_no, 
                                      c_code, 
                                      c_name,
                                      a_code,
                                      pj_no, 
                                      Actv_No,
                                      driver_no, 
                                      r_code, 
                                      Bill_post,                                
                                      ref_no,                                
                                      a_desc, 
                                      P_Extrnl_Post,
                                      si_type,
                                      ad_u_id, 
                                      ad_date, 
                                      0,                                    
                                      brn_no, 
                                      brn_year,
                                      cmp_no, 
                                      brn_usr,
                                      Decode(V_Use_Audit_Doc,1,1,0),
                                      Null                         ,
                                      ad_u_id                      ,
                                     Ias_Gen_Pkg.Get_Curdate       ,
                                     Doc_Brn_No  ,
                                     V_DOC_PST_SQ    
                                From  Ias_bill_Mst
                               WHERE  Bill_Ser=P_Doc_Ser;
       ------------------------------------------------------------------------------------  
        For J In ( SELECT  d.bill_no, 
                           d.bill_ser, 
                           d.i_code, 
                           d.i_qty, 
                           d.free_qty, 
                           d.Itm_Unt, 
                           d.p_size, 
                           d.p_qty, 
                           d.i_price, 
                           d.stk_cost, 
                           d.w_code, 
                           d.cc_code,
                           d.Pj_No,
                           d.Actv_No, 
                           d.expire_date, 
                           d.batch_no, 
                           d.use_serialno, 
                           d.dis_amt, 
                           d.vat_amt, 
                           d.vat_per, 
                           d.rcrd_no, 
                           d.doc_sequence,                             
                           d.use_attch, 
                           d.rec_attch,
                           d.si_type, 
                           d.brn_no, 
                           d.brn_year, 
                           d.cmp_no, 
                           d.brn_usr,
                           d.Barcode,
                           m.bill_date,
                           m.bill_currency,
                           m.bill_rate,
                           m.stock_rate,
                           m.bill_doc_type,
                           m.a_desc,
                           m.ref_no,
                           m.ad_u_id,
                           d.Dis_amt_mst,
                           d.Dis_amt_mst_vat,
                           d.Dis_per,
                           d.Dis_amt_dtl,
                           d.Dis_amt_dtl_vat,
                           d.Dis_per2,
                           d.Dis_amt_dtl2,
                           d.Dis_amt_dtl2_vat,
                           d.Dis_per3,
                           d.Dis_amt_dtl3,
                           d.Dis_amt_dtl3_vat,
                           d.Emp_no,
                           d.I_price_vat,
                           d.Lev_no,
                           Nvl(I.Use_qty_fraction,0) Use_qty_fraction
                      From Ias_bill_mst m,Ias_bill_dtl d,Ias_Itm_Mst I
                    WHERE  m.bill_ser=d.bill_ser 
                      And  m.Bill_Ser=P_Doc_Ser
                      And  D.I_code  = I.I_Code
                      AND  Nvl(d.Service_Item,0)=0) Loop
          ---------------------------------------------------------------------------      
          If P_Out_Avlqty=1 Then          
             ---------------------------------------------------------------------------
             V_Avlqty := Get_Icode_Avlqty ( P_Icode   => J.I_Code,
                                            P_Psize   => Nvl(J.P_Size,1),
                                            P_Wcode   => J.W_Code,
                                            P_Expdate => Nvl(J.Expire_date,'01/01/1900'),
                                            P_Batchno => Nvl(J.Batch_no,'0'));
             ---------------------------------------------------------------------------
             --## Get Qty Previous Record When Dulicate Record In Document
             /*If Nvl(V_Avlqty,0)>0 And J.Rcrd_No>1 Then
                Begin
                     Select Sum(Nvl(D.P_Qty,0)+(Nvl(D.Free_Qty,0)*Nvl(D.P_Size,0))) 
                       Into  V_Iqty_Doc
                       From Detail_Out_Bills D
                      Where Bill_Ser=P_Doc_Ser
                        And D.I_Code=J.I_Code
                        And D.W_Code=J.W_Code
                        And Nvl(D.Expire_Date,'01/01/1900')=Nvl(D.Expire_Date,'01/01/1900')
                        And Nvl(D.Batch_No,'0')=Nvl(D.Batch_No,'0')
                        And D.Rcrd_No < J.Rcrd_No;                           
                Exception When Others Then
                    V_Iqty_Doc := 0;
                End;
             End if;
             */
              V_Avlqty := Trunc(Nvl(V_Avlqty,0)-(Nvl(V_Iqty_Doc,0)/nvl(J.p_size,0)),6);
             ---------------------------------------------------------------------------
             If Nvl(V_Avlqty,0)>=Nvl(J.I_Qty,0) Then
                V_iqty := J.I_Qty;
             Else
                V_iqty := Nvl(V_Avlqty,0);   
             End If;
             ---------------------------------------------------------------------------    
             If Nvl(V_Avlqty,0)>=(Nvl(J.I_Qty,0)+Nvl(J.Free_Qty,0)) Then
                V_Fqty := J.Free_Qty;
             Else
                If Nvl(V_Avlqty,0)-Nvl(J.I_Qty,0)>0 Then
                   V_Fqty := (Nvl(V_Avlqty,0)-Nvl(J.I_Qty,0));   
                Else
                   V_Fqty := 0;
                End If;                   
             End If;                             
             ---------------------------------------------------------------------------
          Else
             V_iqty := J.I_Qty;
             V_Fqty := J.Free_Qty;
          End If;                       
          ---------------------------------------------------------------------------
          If J.Use_qty_fraction=0 Then
             V_iqty := Trunc(V_iqty);
             V_Fqty := Trunc(V_Fqty);
          End If;
          ---------------------------------------------------------------------------
          If Nvl(V_iqty,0)+Nvl(V_Fqty,0) > 0 Then
                Insert Into Detail_out_bills ( Out_no, 
                                               out_ser, 
                                               bill_no, 
                                               bill_ser, 
                                               i_code, 
                                               i_qty, 
                                               free_qty, 
                                               Itm_Unt, 
                                               p_size, 
                                               p_qty, 
                                               i_price, 
                                               stk_cost, 
                                               w_code, 
                                               cc_code,
                                               Pj_No,
                                               Actv_No, 
                                               expire_date, 
                                               batch_no, 
                                               use_serialno, 
                                               dis_amt, 
                                               vat_amt, 
                                               vat_per, 
                                               rcrd_no, 
                                               doc_sequence, 
                                               barcode, 
                                               use_attch, 
                                               rec_attch,
                                               si_type, 
                                               brn_no, 
                                               brn_year, 
                                               cmp_no, 
                                               brn_usr)
                                      Values ( P_out_no, 
                                               P_out_ser, 
                                               J.bill_no, 
                                               J.bill_ser, 
                                               J.i_code, 
                                               V_Iqty, 
                                               V_Fqty, 
                                               J.Itm_Unt, 
                                               J.p_size, 
                                               V_Iqty*J.p_size, 
                                               J.i_price, 
                                               J.stk_cost, 
                                               J.w_code, 
                                               J.cc_code,
                                               J.Pj_No,
                                               J.Actv_No, 
                                               J.expire_date, 
                                               J.batch_no, 
                                               J.use_serialno, 
                                               J.dis_amt, 
                                               J.vat_amt, 
                                               J.vat_per, 
                                               J.rcrd_no, 
                                               J.doc_sequence, 
                                               J.barcode, 
                                               J.use_attch, 
                                               J.rec_attch,
                                               J.si_type, 
                                               J.brn_no, 
                                               J.brn_year, 
                                               J.cmp_no, 
                                               J.brn_usr);
            --##-------------------------------------------------------------------------------##--
            --## insert sale cost item mov                                               
            If P_Out_Avlqty=1  Then
                  Begin 
                  V_Stk_Cst := Nvl(j.Stk_Cost,0)/Nvl(j.P_Size,1)  ; 
                  ias_itm_inv_pkg.insrt_sale_cost(p_cst         => V_Stk_Cst                           ,
                                                p_icode       => j.i_code                        ,
                                                p_iqty        => v_iqty                          ,
                                                p_freeqty     => Nvl(v_Fqty,0)                   ,
                                                p_Itm_Unt     => j.Itm_Unt                       ,
                                                p_psize       => j.p_size                        ,
                                                P_Barcode     => j.Barcode                       ,
                                                p_cost_type   => V_costing_type            ,
                                                P_wtavg_type  => V_wtavg_type             ,
                                                p_wcode       => j.w_code                        ,
                                                p_doctype     => 1                               ,
                                                p_docno       => j.bill_no,
                                                p_billdoctype => j.bill_doc_type                      ,
                                                p_cc_code     => j.cc_code                       ,
                                                p_rcrdno      => j.rcrd_no                             ,
                                                p_expdate     => Nvl(j.expire_date,'01/01/1900') , 
                                                p_batchno     => Nvl(j.batch_no,'0')             ,
                                                p_docser      => j.bill_ser                      ,
                                                p_docseq      => j.doc_sequence                             ,
                                                p_idate       => j.bill_date                     ,
                                                p_vatamt      => Nvl(j.vat_amt,0)                ,
                                                p_disamt      => Nvl(j.dis_amt,0)                , 
                                                p_acy         => j.bill_currency                          ,
                                                p_ac_rate     => j.bill_rate                     ,
                                                p_stk_rate    => j.stock_rate                         ,
                                                p_c_code      => Null                            ,
                                                p_adesc       => j.a_desc,
                                                p_refno       => j.ref_no,
                                                p_outno       => P_Out_No                        ,
                                                p_outgrser    => P_Out_No                      ,
                                                p_inout       => -1                              ,
                                                p_iprice      => Nvl(j.i_price,0)                ,
                                                p_ad_date     => Sysdate                         ,
                                                p_up_date     => Null                            ,                                         
                                                p_brn_no      => j.brn_no                        ,
                                                p_brn_year    => j.brn_year                      ,
                                                p_Cmp_No      => j.Cmp_No                        ,                                                                                                
                                                p_Brn_Usr     => j.Brn_Usr                       ,
                                                P_Free_Typ         => 1                   ,
                                                P_Dis_Amt_Mst      => j.Dis_Amt_Mst        ,
                                                P_Dis_Amt_Mst_Vat  => j.Dis_Amt_Mst_Vat  ,
                                                P_Dis_Per          => j.Dis_Per          ,
                                                P_Dis_Amt_Dtl      => j.Dis_Amt_Dtl      ,
                                                P_Dis_Amt_Dtl_Vat  => j.Dis_Amt_Dtl_Vat  ,
                                                P_Dis_Per2         => j.Dis_Per2         ,
                                                P_Dis_Amt_Dtl2     => j.Dis_Amt_Dtl2     ,
                                                P_Dis_Amt_Dtl2_Vat => j.Dis_Amt_Dtl2_Vat ,
                                                P_Dis_Per3         => j.Dis_Per3       ,
                                                P_Dis_Amt_Dtl3     => j.Dis_Amt_Dtl3   ,
                                                P_Dis_Amt_Dtl3_Vat => j.Dis_Amt_Dtl3_Vat,
                                                P_Vat_Per          => j.Vat_Per         ,
                                                P_Emp_No           => j.Emp_No,
                                                P_I_Price_Vat      => j.I_Price_Vat  ,
                                                P_Lev_No           => j.Lev_No) ;
                  Exception When Others Then                            
                            Raise_application_error(-20802,'Error When Insert Sale cost  , '||SqlErrm||'i_code='||j.i_code||' bill_ser='||j.bill_ser) ;                                   
                  End;    
                  --##-------------------------------------------------------------------------------##--
                  --##Insert attach  
                  If Nvl(V_Use_Itm_Attach,0)=1 And  J.Barcode Is Not Null Then 
                       Begin                
                        Select 1 Into V_Use_Attch From Ias_Itm_Mst 
                                           Where I_Code =j.i_Code
                                            And Nvl(Use_Attch,0)=1
                                            And rownum<=1;              
                       Exception
                           When Others Then
                            V_Use_Attch:= 0;
                       End ;                        
                    If Nvl(V_Use_Attch,0) = 1  Then                   
                          Begin
                              Select Flex_No
                               Into V_Attch.Flex_No
                                From Ias_Itm_Unt_Barcode 
                                 Where Barcode = J.Barcode ;
                          Exception
                               When Others Then
                                 V_Attch.Flex_No  := Null ;
                          End ;
                          If V_Attch.Flex_No Is Not Null Then
                             Begin
                               Select Attch_No1, Attch_Desc_No1, 
                                      Attch_No2, Attch_Desc_No2, 
                                      Attch_No3, Attch_Desc_No3, 
                                      Attch_No4, Attch_Desc_No4, 
                                      Attch_No5, Attch_Desc_No5,
                                      Flex_Field
                                    Into V_Attch.Attch_No1,V_Attch.Attch_Desc_No1,
                                         V_Attch.Attch_No2,V_Attch.Attch_Desc_No2,
                                         V_Attch.Attch_No3,V_Attch.Attch_Desc_No3,
                                         V_Attch.Attch_No4,V_Attch.Attch_Desc_No4,
                                         V_Attch.Attch_No5,V_Attch.Attch_Desc_No5,
                                         V_Attch.Flex_Field 
                                   From Ias_Itm_Attach
                                    Where Flex_No = V_Attch.Flex_No;
                             Exception
                                 When Others Then
                                   V_Attch.Flex_Field  := Null ;
                             End ;                          
                          End If ;
                     If V_Attch.Flex_Field Is Not Null Then
                             Begin
                                Select Nvl(Max(Rec_Attch),0)+1
                                 Into V_Rec_Attch
                                  From Ias_Itm_Attach_Movement;
                             Exception
                                  When Others Then
                                     null;
                             End ;
                                                       
                          Begin
                          Insert Into Ias_Itm_Attach_Movement(I_Code, 
                                                             Itm_Unt, 
                                                             P_Size, 
                                                             Attch_No1, 
                                                             Attch_Desc_No1, 
                                                             Attch_No2, 
                                                             Attch_Desc_No2, 
                                                             Attch_No3, 
                                                             Attch_Desc_No3, 
                                                             Attch_No4, 
                                                             Attch_Desc_No4, 
                                                             Attch_No5, 
                                                             Attch_Desc_No5, 
                                                             Flex_Field, 
                                                             Flex_No, 
                                                             Rec_Attch, 
                                                             Attch_Note, 
                                                           Doc_Type, 
                                                           Bill_Doc_Type, 
                                                           Doc_No, 
                                                           Doc_Ser, 
                                                           W_Code, 
                                                           Bill_Cost, 
                                                           Rcrd_No_Doc, 
                                                           In_Out, 
                                                           Cc_Code, 
                                                           Pj_No  ,
                                                           Actv_No,
                                                           C_Code, 
                                                           Expire_Date, 
                                                           Batch_No, 
                                                           I_Qty, 
                                                           P_Qty, 
                                                           Free_Qty, 
                                                           Pf_Qty, 
                                                           Rcrd_No, 
                                                           External_Post, 
                                                           Doc_Type_Ref, 
                                                           Doc_No_Ref, 
                                                           Doc_Ser_Ref, 
                                                           Out_No, 
                                                           Out_Gr_Ser, 
                                                           Ad_U_Id, 
                                                           Ad_Date, 
                                                           Up_U_Id, 
                                                           Up_Date, 
                                                           Brn_No, 
                                                           Brn_Year,
                                                           Cmp_No,                                                                       
                                                           Brn_Usr,
                                                           A_Cy   ,
                                                           Ac_Rate,
                                                           Stk_Rate)
                                                  Values(J.I_Code, 
                                                       J.Itm_Unt, 
                                                       J.P_Size, 
                                                       V_Attch.Attch_No1,
                                                       V_Attch.Attch_Desc_No1,
                                                       V_Attch.Attch_No2,
                                                       V_Attch.Attch_Desc_No2,
                                                       V_Attch.Attch_No3,
                                                       V_Attch.Attch_Desc_No3,
                                                       V_Attch.Attch_No4,
                                                       V_Attch.Attch_Desc_No4,
                                                       V_Attch.Attch_No5,
                                                       V_Attch.Attch_Desc_No5,
                                                       V_Attch.Flex_Field    ,
                                                       V_Attch.Flex_No       ,
                                                       V_Rec_Attch, 
                                                       J.REF_NO, 
                                                           1, 
                                                           j.bill_doc_type, 
                                                           J.Bill_no, 
                                                           j.bill_ser, 
                                                           j.W_Code, 
                                                           1, 
                                                           j.rcrd_no, 
                                                           -1, 
                                                           j.cc_code, 
                                                           j.Pj_No  ,
                                                           j.Actv_No,
                                                           Null, 
                                                           Nvl(j.expire_date,'01/01/1900') , 
                                                           Nvl(j.batch_no,'0') , 
                                                           V_IQty, 
                                                           Nvl(V_IQty,0)*J.P_Size, 
                                                           Nvl(J.Free_Qty,0), 
                                                           Nvl(J.Free_Qty,0)*J.P_Size,  
                                                           j.rcrd_no, 
                                                           1, 
                                                           Null, 
                                                           Null, 
                                                           Null, 
                                                           Null, 
                                                           Null, 
                                                           J.Ad_U_Id, 
                                                           ias_gen_pkg.get_curdate, 
                                                           Null, 
                                                           Null, 
                                                           J.brn_no , 
                                                           J.brn_year,
                                                           J.Cmp_No,                                           
                                                           J.Brn_Usr ,
                                                           j.bill_currency, 
                                                           j.bill_rate, 
                                                           J.stock_rate   ) ;
                              Exception  When Others Then                                 
                                 Null;
                              End;
                          End If ;
                    End If ;
                  End If ;
                   --##End  Insert Attach
                  --##-------------------------------------------------------------------------------##--
            End If;                                                                  
          End If;                                  
       End Loop;                            
       ------------------------------------------------------------------------------------
    End If;    
   ------------------------------------------------------------------------------------                                
 Exception when others Then
     Raise_application_error(-20804,'Error When Insert Out Bills , '||SqlErrm) ;
 END;
--=====================================================================================--
FUNCTION Get_Ret_No (P_Invs_Sr In Number,P_Sr_Type  In Number,P_Cc_Code In Varchar2,P_w_code In Number,P_bill_doc_type In Number,P_Brn_No In Number) Return Number Is 
  V_Ret_No Number;
  V_BRN_YEAR NUMBER;
BEGIN   
      Begin
         Select Max(Yr_No)
           Into V_BRN_YEAR
           From S_Prd_Dtl
          Where To_Date(SYSDATE, 'DD/MM/RRRR') Between F_Date And T_Date;
      Exception
         When Others Then
            Null;
      End;
      
      V_Ret_No  := Ar_Doc_Sq_Pkg.Get_Doc_No(P_Doc_Typ    => 14
                                            ,P_Pay_Typ    => P_bill_doc_type
                                            ,P_Brn_Year   =>V_BRN_YEAR
                                            ,P_Brn_No     => P_Brn_No
                                            ,P_Cc_Code    => P_Cc_Code
                                            ,P_W_Code     => P_w_code
                                            ,P_Typ_No     => P_Sr_Type);
  
  Return(V_Ret_No);
   Exception when others Then
      Return(0);
 END;
--=====================================================================================--
 FUNCTION Get_Ret_Ser (P_Ret_No In Number,P_Sr_Type  In Number,P_Invs_Sr In Number,P_Cc_Code In Varchar2,P_w_code In Number,P_bill_doc_type In Number,P_Brn_No In Number,P_Brn_Year In Number) Return Number Is 
  V_Ret_Ser Number;
  V_c_sr    Number;
  V_cc_no   Number;
  V_w_sr    Number;
BEGIN   
  -------------------------------------------------------------------------------------       
  If P_Invs_Sr In (3,6) Then      
       V_c_sr:=ias_cc_code_pkg.Get_Cc_ser(P_Cc_Code);
       V_cc_no:=ias_cc_code_pkg.Get_Cc_no(P_Cc_Code);                               
  ElsIf P_Invs_Sr = 4 Then          
     V_W_Sr := IAS_Wcode_Pkg.Get_Wc_Ser(P_W_Code);        
  End If;               
  -------------------------------------------------------------------------------------          
  V_Ret_Ser:= Ar_Doc_Sq_Pkg.Get_Doc_Srl( P_Doc_Typ    => 14
                                         ,P_Pay_Typ    => P_bill_doc_type
                                         ,P_Brn_Year   => P_Brn_Year
                                         ,P_Brn_No     => P_Brn_No
                                         ,P_Cc_Code    => P_Cc_Code
                                         ,P_W_Code     => P_w_code
                                         ,P_Typ_No     => P_Sr_Type
                                         ,P_Doc_No     => P_Ret_No);  
  -------------------------------------------------------------------------------------  
  Return(V_Ret_Ser);
   Exception when others Then
     Return(0);     
 END;
--=====================================================================================-- 
 PROCEDURE Insrt_Ret_Bills ( P_Invs_Sr In Number, P_Pyear   In Number, P_Doc_Ser In Number,  P_Ret_No  In Number,  P_Ret_Ser In Number, P_Out_No  In Number,  P_Out_Ser In Number, P_Extrnl_Post Number, P_Lang_No Number,P_Brn_No In Number) Is
   V_Cc_Code       Ias_Ret_Bill_Mst.cc_code%TYPE;
   V_w_code        Ias_Ret_Bill_Mst.w_code%TYPE;
   V_bill_doc_type Ias_Ret_Bill_Mst.Rt_bill_doc_type%TYPE;   
   V_Cnt           Number;
   V_Use_Audit_Doc Ias_Para_Gen.Use_Audit_Doc%Type ;
   V_DOC_PST_SQ    Ias_Ret_Bill_Mst.DOC_PST_SQ%TYPE;
 BEGIN
   ------------------------------------------------------------------------------------
        Begin
          Select  Nvl(Use_Audit_Doc,0)
            Into  V_Use_Audit_Doc 
          From Ias_Para_Gen  ;
        Exception
            When Others Then
             V_Use_Audit_Doc  := 0 ;
        End ;
   ------------------------------------------------------------------------------------
   Begin
     Select 1 InTo V_Cnt From Ias_Ret_Bill_Mst 
      Where Rt_Bill_Ser=P_Doc_Ser         
        And RowNum<=1;  
   Exception when others Then
     V_Cnt := 0;     
   END;
   If Nvl(V_Cnt,0)=1 Then
     Raise_application_error(-20805,Ias_Gen_Pkg.Get_Msg(P_Lang_No,1333)||' '||SqlErrm) ;
   End If;
   ------------------------------------------------------------------------------------
   Begin
     Select 1 InTo V_Cnt From Ias_Ret_Bill_Mst 
      Where Ret_Ser=P_Ret_Ser         
        And RowNum<=1;  
   Exception when others Then
     V_Cnt := 0;     
   END;
   If Nvl(V_Cnt,0)=1 Then
     Raise_application_error(-20806,Ias_Gen_Pkg.Get_Msg(P_Lang_No,17)||' '||SqlErrm) ;
   End If;
   ------------------------------------------------------------------------------------
   Begin
     Select 1 
       InTo V_Cnt
     From Ias_Rt_Bill_Dtl
     Where Rt_Bill_Ser=P_Doc_Ser
       And Nvl(Service_Item,0)=0 
       And RowNum<=1;  
   Exception when others Then
     V_Cnt := 0;
   END; 
   ------------------------------------------------------------------------------------
   If Nvl(V_Cnt,0)=1 Then   
       ------------------------------------------------------------------------------------
       Begin
         Select Cc_Code,w_code,rt_bill_doc_type 
           InTo V_Cc_Code,V_w_code,V_bill_doc_type
         From Ias_Rt_Bill_Mst
         Where Rt_Bill_Ser=P_Doc_Ser
           And RowNum<=1;  
       Exception when others Then
         Raise_application_error(-20807,SqlErrm) ;
       END;                       
       ------------------------------------------------------------------------------------
       If P_Pyear=0 Then
          Begin
              SELECT 1 InTo V_Cnt
                From  ias_rt_bill_dtl a,detail_out_bills b           
               Where a.bill_Ser=b.bill_Ser(+)
                 and a.I_code=b.I_code(+)
                 and a.w_code=b.w_code(+)
                 and a.si_rcrd_no=b.rcrd_no(+)
                 and a.rt_bill_ser=P_Doc_Ser
                 and nvl(a.service_item,0)=0
                Group By  a.bill_Ser,a.I_code,a.w_code,a.si_rcrd_no
                Having Sum(Nvl(NVL(a.p_qty,0) +(NVL(a.free_qty,0)*NVL(a.p_size,0)),0))> 
                      Sum(Nvl(NVL(b.p_qty,0) +(NVL(b.free_qty,0)*NVL(b.p_size,0)),0));
          Exception when others Then
              V_Cnt:=0;
          END;        
          ------------------------------------------------------------------------------------     
          If Nvl(V_Cnt,0)>0 Then
            Raise_application_error(-20808,Ias_Gen_Pkg.Get_Msg(P_Lang_No,1329)||' '||SqlErrm) ;               
          End If;
          ------------------------------------------------------------------------------------
       End If;       
       ------------------------------------------------------------------------------------
       V_DOC_PST_SQ:=IAS_POSTING_PKG.GET_DOC_PST_SQ; 
       
             
       INSERT INTO  ias_ret_bill_mst ( ret_no, 
                                       ret_ser, 
                                       rt_bill_doc_type, 
                                       rt_bill_no, 
                                       rt_bill_ser, 
                                       ret_date, 
                                       a_cy, 
                                       ac_rate, 
                                       stk_rate, 
                                       c_code, 
                                       c_name, 
                                       a_code,
                                       pj_no,
                                       Actv_No, 
                                       r_code, 
                                       ret_post, 
                                       w_code, 
                                       ref_no, 
                                       cc_code, 
                                       cash_no, 
                                       doc_desc, 
                                       External_Post,
                                       rt_type,                                
                                       ad_u_id, 
                                       ad_date, 
                                       UP_CNT,
                                       sr_type,                                   
                                       brn_no, 
                                       brn_year, 
                                       cmp_no, 
                                       brn_usr,
                                       Audit_Ref       ,
                                       Audit_Ref_Desc  ,
                                       Audit_Ref_U_Id  ,
                                       Audit_Ref_Date  ,
                                       Doc_Brn_No    ,
                                       DOC_PST_SQ  )                               
                               SELECT  P_ret_no, 
                                       P_ret_ser,                               
                                       rt_bill_doc_type, 
                                       rt_bill_no, 
                                       rt_bill_ser,
                                       rt_bill_date, 
                                       rt_bill_currency, 
                                       rt_bill_rate, 
                                       stock_rate,
                                       c_code, 
                                       c_name, 
                                       a_code,
                                       pj_no, 
                                       Actv_No,
                                       r_code, 
                                       rt_bill_post, 
                                       w_code, 
                                       ref_no, 
                                       cc_code, 
                                       cash_no, 
                                       a_desc, 
                                       P_Extrnl_Post,                               
                                       p_year,                                
                                       ad_u_id, 
                                       ad_date,
                                       0, 
                                       sr_type,
                                       brn_no, 
                                       brn_year, 
                                       cmp_no, 
                                       brn_usr,
                                         Decode(V_Use_Audit_Doc,1,1,0),
                                         Null                         ,
                                         ad_u_id                      ,
                                         Ias_Gen_Pkg.Get_Curdate      ,
                                         Doc_Brn_No,
                                         V_DOC_PST_SQ      
                                 From  ias_rt_bill_mst
                                WHERE  Rt_Bill_Ser=P_Doc_Ser;                         
        ------------------------------------------------------------------------------------
        If P_Pyear=0 Then
            INSERT INTO ias_ret_bill_dtl ( ret_no, 
                                           ret_ser, 
                                           rt_bill_no, 
                                           rt_bill_ser, 
                                           i_code, 
                                           i_qty, 
                                           free_qty, 
                                           Itm_Unt, 
                                           p_size, 
                                           p_qty, 
                                           i_price, 
                                           stk_cost, 
                                           w_code, 
                                           cc_code,
                                           Pj_No,
                                           Actv_No, 
                                           expire_date, 
                                           batch_no, 
                                           use_serialno, 
                                           dis_amt, 
                                           dis_per, 
                                           rcrd_no, 
                                           vat_amt, 
                                           vat_per, 
                                           rt_rcrd_no, 
                                           barcode, 
                                           bill_no, 
                                           bill_ser, 
                                           out_no, 
                                           out_ser, 
                                           si_rcrd_no, 
                                           doc_sequence, 
                                           doc_sequence_si, 
                                           use_attch,
                                           rec_attch,
                                           sr_type, 
                                           cmp_no, 
                                           brn_no, 
                                           brn_year, 
                                           brn_usr)
                                   SELECT  P_ret_no, 
                                           P_ret_ser, 
                                           a.rt_bill_no, 
                                           a.rt_bill_ser, 
                                           a.i_code, 
                                           a.i_qty, 
                                           a.free_qty, 
                                           a.Itm_Unt, 
                                           a.p_size, 
                                           a.p_qty, 
                                           a.i_price, 
                                           b.stk_cost, 
                                           a.w_code, 
                                           a.cc_code,
                                           a.Pj_No,
                                           a.Actv_No, 
                                           a.expire_date, 
                                           a.batch_no, 
                                           a.use_serialno, 
                                           a.dis_amt, 
                                           a.dis_per, 
                                           a.rcrd_no, 
                                           a.vat_amt, 
                                           a.vat_per, 
                                           a.rcrd_no, 
                                           a.barcode, 
                                           a.bill_no, 
                                           a.bill_ser, 
                                           b.out_no, 
                                           b.out_ser, 
                                           si_rcrd_no, 
                                           a.doc_sequence,  
                                           b.doc_sequence, 
                                           a.use_attch,
                                           a.rec_attch,
                                           a.sr_type, 
                                           a.cmp_no, 
                                           a.brn_no, 
                                           a.brn_year, 
                                           a.brn_usr       
                                     From  ias_rt_bill_dtl a,Detail_Out_Bills b                             
                                    WHERE  a.rt_bill_ser         = P_Doc_Ser
                                      AND  a.Bill_Ser            = b.Bill_Ser
                                      AND  a.I_Code              = b.I_Code
                                      AND  a.W_Code              = b.W_Code
                                      AND  a.Si_Rcrd_No          = b.Rcrd_No                                  
                                      AND  Nvl(a.Service_Item,0) = 0;
        Else
             INSERT INTO ias_ret_bill_dtl ( ret_no, 
                                           ret_ser, 
                                           rt_bill_no, 
                                           rt_bill_ser, 
                                           i_code, 
                                           i_qty, 
                                           free_qty, 
                                           Itm_Unt, 
                                           p_size, 
                                           p_qty, 
                                           i_price, 
                                           stk_cost, 
                                           w_code, 
                                           cc_code,
                                           Pj_No,
                                           Actv_No, 
                                           expire_date, 
                                           batch_no, 
                                           use_serialno, 
                                           dis_amt, 
                                           dis_per, 
                                           rcrd_no, 
                                           vat_amt, 
                                           vat_per, 
                                           rt_rcrd_no, 
                                           barcode, 
                                           bill_no, 
                                           bill_ser, 
                                           out_no, 
                                           out_ser, 
                                           doc_sequence,                                            
                                           use_attch,
                                           rec_attch,
                                           sr_type, 
                                           cmp_no, 
                                           brn_no, 
                                           brn_year, 
                                           brn_usr)
                                   SELECT  P_ret_no, 
                                           P_ret_ser, 
                                           rt_bill_no, 
                                           rt_bill_ser, 
                                           i_code, 
                                           i_qty, 
                                           free_qty, 
                                           Itm_Unt, 
                                           p_size, 
                                           p_qty, 
                                           i_price, 
                                           stk_cost, 
                                           w_code, 
                                           cc_code,
                                           Pj_No,
                                           Actv_No, 
                                           expire_date, 
                                           batch_no, 
                                           use_serialno, 
                                           dis_amt, 
                                           dis_per, 
                                           rcrd_no, 
                                           vat_amt, 
                                           vat_per, 
                                           rcrd_no, 
                                           barcode, 
                                           bill_no, 
                                           bill_ser, 
                                           P_out_no, 
                                           P_out_ser,                                            
                                           doc_sequence,                                           
                                           use_attch,
                                           rec_attch,
                                           sr_type, 
                                           cmp_no, 
                                           brn_no, 
                                           brn_year, 
                                           brn_usr       
                                     From  ias_rt_bill_dtl                              
                                    WHERE  rt_bill_ser         = P_Doc_Ser                                  
                                      AND  Nvl(Service_Item,0) = 0;
        End If;                                                                                                    
        ------------------------------------------------------------------------------------
    End If;                                  
   ------------------------------------------------------------------------------------                                
 Exception when others Then
   Raise_application_error(-20809,SqlErrm) ;
 END;
--=====================================================================================--  
END Ias_Insrt_Out_Bills_Pkg;