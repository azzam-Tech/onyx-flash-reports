TEXT
Package Body Ars_Api_Fetch_Data_Pkg is

--================================================================================---
 Function Get_Cstmr_Blnc_Fnc(P_Sys_No            In Number,
                                                  P_F_C_Code          In Varchar2 Default Null,
                                                  P_T_C_Code          In Varchar2 Default Null,
                                                  P_F_Rep_Code        In Varchar2 Default Null,
                                                  P_T_Rep_Code        In Varchar2 Default Null,
                                                  P_Rep_Code_Parent   In Varchar2 Default Null, --## MAIN REP_CODE
                                                  P_Cur_Code          In Varchar2 Default Null,
                                                  P_F_Date            In Date Default Null,
                                                  P_T_Date            In Date Default Null,
                                                  P_Pst_Type          In Number Default 0, --## 0 all balnc 1- unposted 2- posted 3- not posted from br                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          --# 1-UNPOSTING 2- POSTING 3-ALL
                                                  P_Blnc_Type         In Number Default 2,--# 1 DETAIL -2 SUM
                                                  P_Hide_Zero_Blnc    In Number Default 0,--# 0 show -1 hide
                                                  P_User_No           In Number,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   --## 1-DETAIL 2- SUM
                                                  P_Lng_No            In Number Default 1,
                                                  P_Out_Data_typ      In Number Default 0,--## 0- xml # 1-query
                                                  P_F_CC_CODE         IN     IAS_POST_DTL.CC_CODE%TYPE  Default Null,
                                                  P_T_CC_CODE         IN     IAS_POST_DTL.CC_CODE%TYPE  Default Null,
                                                  P_F_PJ_NO           IN     IAS_POST_DTL.PJ_NO%TYPE  Default Null,
                                                  P_T_PJ_NO           IN     IAS_POST_DTL.PJ_NO%TYPE  Default Null,
                                                  P_F_ACTV_NO         IN     IAS_POST_DTL.ACTV_NO%TYPE  Default Null,
                                                  P_T_ACTV_NO         IN     IAS_POST_DTL.ACTV_NO%TYPE  Default Null
                                                   )
   Return Clob
Is
   Pragma Autonomous_Transaction;
   V_Cnt                   Number;
   V_Sql_Qry               Clob;
   V_sql_vw                Clob;
   V_Whr                   Clob :=' ';
   V_Whr_Acy               Varchar2(500):=' ';
   V_Whr_Sman              Varchar2(8000):=' ';
  -- V_Whr_DATE             Varchar2(8000):=' ';
   V_Xml_Typ               Xmltype;
   V_Json_Rslt             Varchar2(4000);
   Qry_Ctx                 Dbms_Xmlgen.Ctxhandle;
   Qry_Rslt                Clob;
   V_C_Code                Varchar2(500);
   V_Msg_Txt               Varchar2(4000) := Null;
   V_Pkg_Line              Varchar2(4000) := Null;
   V_Err_Line              Int := 0;
   V_F_Date                Date;
   V_T_Date                Date;
   V_F_C_Code              Varchar2(500):=P_F_C_Code;
   V_T_C_Code              Varchar2(500):=P_T_C_Code;
   V_F_Rep_Code            Varchar2(500):=P_F_Rep_Code;
   V_T_Rep_Code            Varchar2(500):=P_T_Rep_Code;
   V_F_CC_CODE              IAS_POST_DTL.CC_CODE%TYPE:=P_F_CC_CODE;
   V_T_CC_CODE              IAS_POST_DTL.CC_CODE%TYPE :=P_T_CC_CODE;
   V_F_PJ_NO                IAS_POST_DTL.PJ_NO%TYPE  :=P_F_PJ_NO;
   V_T_PJ_NO                IAS_POST_DTL.PJ_NO%TYPE  :=P_T_PJ_NO ;
   V_F_ACTV_NO              IAS_POST_DTL.ACTV_NO%TYPE  :=P_F_ACTV_NO;
   V_T_ACTV_NO              IAS_POST_DTL.ACTV_NO%TYPE  :=P_T_ACTV_NO;
   V_Fld_Sman              Varchar2(500);
   V_Aralt                 Number(1) := 0;
   V_Conn_Cst_Multi_Sman   Number(1);
   V_Cstmr_Blnc_Type       Number := 0;
   V_Tmp_Date              Date;
   V_Tmp_Code              Varchar2(500);
   v_whr_hide_zero_blnc    Varchar2(100);
   V_POST_TBL              varchar2(500):='IAS_POST_DTL';
   V_DSPLY_PRV_AC          Number(1) := 0;
   V_CC_AVAIL       NUMBER;
   V_USE_PROJECTS   NUMBER;
   V_USE_ACTVTY     NUMBER;
   V_CHK_PRIV_CCS_ASTMNT  Number(1) := 0;
   V_CHK_PRIV_PJS_ASTMNT   Number(1) := 0;
   V_CHK_PRIV_ACTV_ASTMNT   Number(1) := 0;


Begin
   --V_Lng_No :=    Nvl(P_Lng_No, 1);
   V_Json_Rslt :=  '{"_Result": { "_ErrMsg": "@ERRMSG","_ErrNo": @ERRNO } }';

   Begin
      Execute Immediate 'ALTER SESSION SET NLS_DATE_FORMAT=''DD/MM/RRRR''';
   End;

   If P_Sys_No Is Null Then
      V_Err_Line := $$plsql_Line;
      V_Msg_Txt :=  'ENTER P_SYS_NO   ';
      Goto Rtn_Rslt;
   End If;

   If P_User_No Is Null Then
      V_Err_Line := $$plsql_Line;
      V_Msg_Txt :=  Ias_Gen_Pkg.Get_Msg(P_Lng_No => P_Lng_No, P_Msg_No => 450);
      Goto Rtn_Rslt;
   End If;
    ----------------------------------------------------------------
     BEGIN
           Select Fld_Val INTO V_DSPLY_PRV_AC
              From S_Fld_Prv_Fxd_Usr
             Where Upper (Fld_Nm) = Upper ('DSPLY_PRV_AC_STMNT')
             And U_Id = P_User_No
             AND ROWNUM<=1;
    EXCEPTION WHEN OTHERS THEN
         V_DSPLY_PRV_AC:=0;
    END;
   ----------------------------------------------------------------
   V_F_Date :=     Nvl(P_F_Date, Ias_Gen_Pkg.Get_Frst_Day);
   V_T_Date :=     Nvl(P_T_Date, Ias_Gen_Pkg.Get_Curdate);

   If V_F_Date > V_T_Date Then
      V_Tmp_Date := V_F_Date;
      V_F_Date :=   V_T_Date;
      V_T_Date :=   V_Tmp_Date;
   End If;

   If  V_F_Date<Ias_Gen_Pkg.Get_Frst_Day  AND NVL(V_DSPLY_PRV_AC,0)=1 Then
     V_POST_TBL:='IAS_V_POST_DTL_YR';
   End If;

   -----------------------------------------------------------------------------
    BEGIN
      SELECT NVL(CC_AVAIL, 0),
             NVL(USE_PROJECTS, 0),
             NVL(USE_ACTVTY, 0)
        INTO V_CC_AVAIL,
             V_USE_PROJECTS,
             V_USE_ACTVTY
        FROM IAS_PARA_GEN;
   EXCEPTION
      WHEN OTHERS THEN
         V_CC_AVAIL :=     0;
         V_USE_PROJECTS := 0;
         V_USE_ACTVTY :=   0;
   END;

   -----------------------------------------------------------------------------
   BEGIN
           Select NVL(Fld_Val,0) INTO V_CHK_PRIV_CCS_ASTMNT
              From S_Fld_Prv_Fxd_Usr
             Where Upper (Fld_Nm) = Upper ('CHK_PRIV_CCS_ASTMNT')
             And U_Id = P_User_No
             AND ROWNUM<=1;
    EXCEPTION WHEN OTHERS THEN
         V_CHK_PRIV_CCS_ASTMNT:=0;
    END;

    BEGIN
           Select NVL(Fld_Val,0) INTO V_CHK_PRIV_PJS_ASTMNT
              From S_Fld_Prv_Fxd_Usr
             Where Upper (Fld_Nm) = Upper ('CHK_PRIV_PJS_ASTMNT')
             And U_Id = P_User_No
             AND ROWNUM<=1;
    EXCEPTION WHEN OTHERS THEN
         V_CHK_PRIV_PJS_ASTMNT:=0;
    END;

    BEGIN
           Select NVL(Fld_Val,0) INTO V_CHK_PRIV_ACTV_ASTMNT
              From S_Fld_Prv_Fxd_Usr
             Where Upper (Fld_Nm) = Upper ('CHK_PRIV_ACTV_ASTMNT')
             And U_Id = P_User_No
             AND ROWNUM<=1;
    EXCEPTION WHEN OTHERS THEN
         V_CHK_PRIV_ACTV_ASTMNT:=0;
    END;

    --------------------------------------------
   V_sql_vw:='create or replace force view  dts_v_all_cstmr_balnc as
                Select C_Code ,
                       Ac_Code_Dtl,
                       ac_dtl_typ,
                       a_code,
                       Rep_Code,
                       Doc_Date,
                       Doc_Type,
                       Jv_Type,
                       Doc_No,
                       Doc_ser,
                       Ref_No,
                       Doc_Desc,
                       A_Cy,
                       Dr_Amt,
                       Dr_Amt_f,
                       Amt_f,
                       Amt,
                       Cr_Amt,
                       Cr_Amt_f,
                       Doc_Post,
                       brn_no,
                       CC_CODE,
                       PJ_NO,
                       ACTV_NO
                  From '||V_POST_TBL||'
                  where ac_dtl_typ=3
                  union all
                Select C_Code ,
                       C_Code Ac_Code_Dtl,
                       3 ac_dtl_typ,
                       a_code,
                       Rep_Code,
                       Bill_Date Doc_Date,
                       4 Doc_Type,
                       Bill_Doc_Type Jv_Type,
                       Bill_No Doc_No,
                       Bill_ser Doc_ser,
                       Ref_No,
                       A_Desc Doc_Desc,
                       Bill_Currency A_Cy,
                       (Nvl((Nvl(Bill_Amt, 0) - Nvl(Disc_Amt, 0) + Nvl(Vat_Amt, 0) + Nvl(Othr_Amt, 0)-(nvl(CR_CARD_AMT,0)+nvl(CR_CARD_AMT_SCND,0)+nvl(CR_CARD_AMT_THRD,0))), 0))* Nvl(Bill_Rate, 1) Dr_Amt,
                       Decode(Bill_Currency, Ys_Gen_Pkg.Get_Local_Cur,0, (Nvl(Nvl(Bill_Amt, 0) - Nvl(Disc_Amt, 0) + Nvl(Vat_Amt, 0) + Nvl(Othr_Amt, 0)-(nvl(CR_CARD_AMT,0)+nvl(CR_CARD_AMT_SCND,0)+nvl(CR_CARD_AMT_THRD,0)), 0) )) Dr_Amt_f,
                       Decode(Bill_Currency, Ys_Gen_Pkg.Get_Local_Cur,0, (Nvl(Nvl(Bill_Amt, 0) - Nvl(Disc_Amt, 0) + Nvl(Vat_Amt, 0) + Nvl(Othr_Amt, 0)-(nvl(CR_CARD_AMT,0)+nvl(CR_CARD_AMT_SCND,0)+nvl(CR_CARD_AMT_THRD,0)), 0) )) Amt_f,
                       (Nvl((Nvl(Bill_Amt, 0) - Nvl(Disc_Amt, 0) + Nvl(Vat_Amt, 0) + Nvl(Othr_Amt, 0)-(nvl(CR_CARD_AMT,0)+nvl(CR_CARD_AMT_SCND,0)+nvl(CR_CARD_AMT_THRD,0))), 0))* Nvl(Bill_Rate, 1) Amt,
                       0 Cr_Amt,
                       0 Cr_Amt_f,
                       3 Doc_Post,
                       brn_no,
                       M.CC_CODE,
                       M.PJ_NO,
                       M.ACTV_NO
                  From Ias_Bill_Mst_Br M
                 Where Nvl(External_Post, 0) = 70
                       And Nvl(Cncl_Flg, 0) = 0
                       And Bill_Doc_Type = 4
                       And Nvl(Bill_Post, 0) = 0
                       And  Not exists (Select 1
                                             From Ias_Bill_Mst I
                                            Where Nvl(External_Post, 0) = 70
                                            and Bill_Ser=m.Bill_Ser
                                            and rownum<=1 )
                Union All
                Select C_Code ,
                       C_Code Ac_Code_Dtl,
                       3 ac_dtl_typ,
                       a_code,
                       Rep_Code,
                       Rt_Bill_Date Doc_Date,
                       5 Doc_Type,
                       rt_Bill_Doc_Type Jv_Type,
                       Rt_Bill_No Doc_No,
                       rt_Bill_ser Doc_ser,
                       Ref_No,
                       A_Desc Doc_Desc,
                       Rt_Bill_Currency A_Cy,
                       0 Dr_Amt,
                       0 Dr_Amt_f,
                      Decode(rt_Bill_Currency, Ys_Gen_Pkg.Get_Local_Cur,0, (Nvl(Nvl(Bill_Amt, 0) - Nvl(Disc_Amt, 0) + Nvl(Vat_Amt, 0) + Nvl(Othr_Amt, 0)-(nvl(CR_CARD_AMT,0)+nvl(CR_CARD_AMT_SCND,0)+nvl(CR_CARD_AMT_THRD,0)), 0) ))*-1 Amt_f,
                       (Nvl((Nvl(Bill_Amt, 0) - Nvl(Disc_Amt, 0) + Nvl(Vat_Amt, 0) + Nvl(Othr_Amt, 0)-(nvl(CR_CARD_AMT,0)+nvl(CR_CARD_AMT_SCND,0)+nvl(CR_CARD_AMT_THRD,0))), 0))* Nvl(rt_Bill_Rate, 1)*-1 Amt,
                       (Nvl((Nvl(Bill_Amt, 0) - Nvl(Disc_Amt, 0) + Nvl(Vat_Amt, 0) + Nvl(Othr_Amt, 0)-(nvl(CR_CARD_AMT,0)+nvl(CR_CARD_AMT_SCND,0)+nvl(CR_CARD_AMT_THRD,0))), 0))* Nvl(rt_Bill_Rate, 1) cr_Amt,
                       Decode(rt_Bill_Currency, Ys_Gen_Pkg.Get_Local_Cur,0, (Nvl(Nvl(Bill_Amt, 0) - Nvl(Disc_Amt, 0) + Nvl(Vat_Amt, 0) + Nvl(Othr_Amt, 0)-(nvl(CR_CARD_AMT,0)+nvl(CR_CARD_AMT_SCND,0)+nvl(CR_CARD_AMT_THRD,0)), 0) )) cr_Amt_f,
                       3 Doc_Post,
                       brn_no,
                       M.CC_CODE,
                       M.PJ_NO,
                       M.ACTV_NO
                  From Ias_Rt_Bill_Mst_Br M
                 Where Nvl(External_Post, 0) = 70
                       And Nvl(Cncl_Flg, 0) = 0
                       And Rt_Bill_Doc_Type = 4
                       And Nvl(Rt_Bill_Post, 0) = 0
                       And  Not exists (Select 1
                                             From Ias_Rt_Bill_Mst I
                                            Where Nvl(External_Post, 0) = 70
                                            and Rt_Bill_Ser=m.Rt_Bill_Ser
                                            and rownum<=1 )';

   Begin
     Execute Immediate (V_sql_vw);
   Exception
      When Others Then
         Null;
   End;
   -----------------------------------------------------------------------------
   Begin
      Select Nvl(Ar_Ac_Link_Type, 0), Nvl(Conn_Cst_Multi_Sman, 0)
        Into V_Aralt, V_Conn_Cst_Multi_Sman
        From Ias_Para_Ar;
   Exception
      When Others Then
         Null;
   End;

   If Nvl(P_Sys_No, 0) = 70 Then
      Begin
         V_Cstmr_Blnc_Type := Ias_Gen_Pkg.Get_Cnt('Select NVL (CSTMR_BLNC_TYPE, 0) From DTS_PARA');
      Exception
         When Others Then
            V_Cstmr_Blnc_Type := 0;
      End;
   End If;

   ---------------------------------------------------------------
   --## C_CODE
   If V_F_C_Code Is Null And V_T_C_Code Is Not Null Then
      V_F_C_Code := V_T_C_Code;
   Elsif V_F_C_Code Is Not Null  And V_T_C_Code Is Null Then
      V_T_C_Code := V_F_C_Code;
   End If;


   If V_F_C_Code Is Not Null Then
     Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   =>V_F_C_Code,
                                       P_TN   =>V_T_C_Code,
                                       P_Type => 'C') ;

      V_Whr := V_Whr || ' And A.Ac_Code_Dtl Between ''' || V_F_C_Code || '''  And  ''' || V_T_C_Code || '''  ';
   End If;

   -----------------------------------------------------------------
   --## Rep_Code
   If V_F_Rep_Code Is Null And V_T_Rep_Code Is Not Null Then
      V_F_Rep_Code := V_T_Rep_Code;
   Elsif V_F_Rep_Code Is Not Null And V_T_Rep_Code Is Null Then
      V_T_Rep_Code := V_F_Rep_Code;
   End If;
   If V_F_Rep_Code Is Not Null Then
     Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   =>V_F_Rep_Code,
                                       P_TN   =>V_T_Rep_Code,
                                       P_Type => 'C') ;

   End If;
   --------------------------------------------------------
   --## CC_Code
   If V_F_CC_Code Is Null And V_T_CC_Code Is Not Null Then
      V_F_CC_Code := V_T_CC_Code;
   Elsif V_F_CC_Code Is Not Null  And V_T_CC_Code Is Null Then
      V_T_CC_Code := V_F_CC_Code;
   End If;


   If V_F_CC_Code Is Not Null Then
     Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   =>V_F_CC_Code,
                                       P_TN   =>V_T_CC_Code,
                                       P_Type => 'C') ;

      V_Whr := V_Whr || ' And A.CC_Code Between ''' || V_F_CC_Code || '''  And  ''' || V_T_CC_Code || '''  ';
   End If;
   ------------------------------------------------------------------
   --## PJ_NO
   If V_F_PJ_NO Is Null And V_T_PJ_NO Is Not Null Then
      V_F_PJ_NO := V_T_PJ_NO;
   Elsif V_F_PJ_NO Is Not Null  And V_T_PJ_NO Is Null Then
      V_T_PJ_NO := V_F_PJ_NO;
   End If;


   If V_F_PJ_NO Is Not Null Then
     Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   =>V_F_PJ_NO,
                                       P_TN   =>V_T_PJ_NO,
                                       P_Type => 'C') ;

      V_Whr := V_Whr || ' And A.PJ_NO Between ''' || V_F_PJ_NO || '''  And  ''' || V_T_PJ_NO || '''  ';
   End If;
   ------------------------------------------------------------------
   --## ACTV_NO
   If V_F_ACTV_NO Is Null And V_T_ACTV_NO Is Not Null Then
      V_F_ACTV_NO := V_T_ACTV_NO;
   Elsif V_F_ACTV_NO Is Not Null  And V_T_ACTV_NO Is Null Then
      V_T_ACTV_NO := V_F_ACTV_NO;
   End If;


   If V_F_ACTV_NO Is Not Null Then
     Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   =>V_F_ACTV_NO,
                                       P_TN   =>V_T_ACTV_NO,
                                       P_Type => 'C') ;

      V_Whr := V_Whr || ' And A.ACTV_NO Between ''' || V_F_ACTV_NO || '''  And  ''' || V_T_ACTV_NO || '''  ';
   End If;
   ------------------------------------------------------------------
   If P_Rep_Code_Parent Is Null And P_sys_no=70  Then
      If V_F_Rep_Code Is Null Then
         V_Err_Line := $$plsql_Line;
         V_Msg_Txt := Ias_Gen_Pkg.Get_Msg(P_Lng_No => P_Lng_No, P_Msg_No => 811);
         Goto Rtn_Rslt;
      End If;
   End If;
   -----------------------------------------------------------------
   --V_Whr :=        V_Whr || ' And a.doc_date between ''' || V_F_Date || ''' and  ''' || V_T_Date || '''';

   -----------------------------------------------------------------
   If P_Cur_Code Is Not Null Then
      V_Whr :=     V_Whr || ' And  a.a_cy=''' || P_Cur_Code || ''' ';
      V_Whr_Acy := V_Whr_Acy || ' And  a.a_cy=''' || P_Cur_Code || ''' ';
   End If;

   If Nvl(P_Pst_Type, 0) = 1 Then
      V_Whr := V_Whr || ' And  nvl(a.DOC_POST,0)=0';
   Elsif Nvl(P_Pst_Type, 0) = 2 Then
      V_Whr := V_Whr || ' And  nvl(a.DOC_POST,0)=1';
   Elsif Nvl(P_Pst_Type, 0) = 3 Then
      V_Whr := V_Whr || ' And  nvl(a.DOC_POST,0)=3'  ;
   Else
      Null;
   End If;

   -------------------------------------------
   V_Whr :=        V_Whr || ' And (   (' || P_User_No || '= 1)
                Or (   (    (' || V_Aralt || ' = 1)
                        And Exists(
                               Select 1
                                 From Priv_Acc
                                Where U_Id = ' || P_User_No || '
                                  And A_Code = b.C_A_Code
                                  And A_Cy = A.A_Cy
                                  And Nvl(View_Flag, 0) = 1
                                  And Rownum <= 1))
                    Or (    (' || V_Aralt || ' = 2)
                        And Exists(
                               Select 1
                                 From Ias_Priv_Customer
                                Where U_Id =' || P_User_No || '
                                  And C_Code = B.C_Code
                                  And A_Cy = A.A_Cy
                                  And Nvl(View_Flag, 0) = 1
                                  And Rownum <= 1)))) ';

   V_Whr :=V_Whr||' And      (('||P_User_No||' = 1)
                                 Or Exists(Select 1
                                             From   S_brn_usr_priv
                                             Where  U_id = '||P_User_No ||'
                                             And S_brn_usr_priv.Brn_no = A.Brn_no
                                              And Nvl(View_Flag, 1) = 1
                                               And Rownum <= 1)) ';

  If Nvl(V_CHK_PRIV_CCS_ASTMNT,0)=1 Then
    V_Whr :=V_Whr||' And 1= CASE WHEN A.CC_CODE IS NOT NULL THEN NVL((Select 1
                                             From   PRIVILEGE_CC
                                             Where  U_id = '||P_User_No ||'
                                             And PRIVILEGE_CC.CC_CODE = A.CC_CODE
                                              And Nvl(View_Flag, 1) = 1
                                               And Rownum <= 1),0)
                                               ELSE 1 END  ';

  End If;

  If Nvl(V_CHK_PRIV_PJS_ASTMNT,0)=1 Then
    V_Whr :=V_Whr||' And 1= CASE WHEN A.PJ_NO IS NOT NULL THEN NVL((Select 1
                                             From   IAS_PRIV_PROJECTS
                                             Where  U_id = '||P_User_No ||'
                                             And IAS_PRIV_PROJECTS.PJ_NO = A.PJ_NO
                                              And Nvl(View_Flag, 1) = 1
                                               And Rownum <= 1),0)
                                               ELSE 1 END ';

  End If;

  If Nvl(V_CHK_PRIV_ACTV_ASTMNT,0)=1 Then
    V_Whr :=V_Whr||' And 1= CASE WHEN A.ACTV_NO IS NOT NULL THEN NVL((Select 1
                                             From   IAS_PRIV_ACTVTY
                                             Where  U_id = '||P_User_No ||'
                                             And IAS_PRIV_ACTVTY.ACTV_NO = A.ACTV_NO
                                              And Nvl(View_Flag, 1) = 1
                                               And Rownum <= 1),0)
                                                ELSE 1 END ';

  End If;


   -------------------------------------------
   --##  DISTRBUTED SYSTEM
   If P_Sys_No = 70 Then
      If Nvl(V_Cstmr_Blnc_Type, 0) = 1 Then
         V_Fld_Sman := ' A.REP_CODE ';

         If V_F_Rep_Code Is Not Null Then
            V_Whr_Sman := V_Whr_Sman || ' AND A.REP_CODE BETWEEN  ''' || V_F_Rep_Code || ''' and  ''' || V_T_Rep_Code || '''  ';
         End If;
      Else
         --V_Fld_Sman := ' NULL  ';
          V_Fld_Sman := ' A.REP_CODE ';
      End If;

      V_Whr_Sman := V_Whr_Sman || ' AND B.C_CODE IN( SELECT C_CODE FROM Dts_V_Sman_Cst WHERE nvl(SMAN_TYP,0) in(1,3) AND  REP_CODE BETWEEN  ''' || V_F_Rep_Code || ''' and  ''' || V_T_Rep_Code || ''' ) ';
   Else
      V_Fld_Sman := ' A.REP_CODE ';

      If P_Rep_Code_Parent Is Not Null Then
         V_Whr_Sman := V_Whr_Sman || ' AND A.REP_CODE In(  Select Reprs_Code REP_CODE
                                                                  From Sales_Man
                                                            Connect By Prior Reprs_Code = Rep_Code_Parent
                                                            Start With Reprs_Code =''' || P_Rep_Code_Parent || ''' ) ';
      End If;

      If V_F_Rep_Code Is Not Null Then
         V_Whr_Sman := V_Whr_Sman || ' AND A.REP_CODE BETWEEN  ''' || V_F_Rep_Code || ''' and  ''' || V_T_Rep_Code || '''  ';
      End If;
   End If;

   -------------------------------------------
   If nvl(P_Hide_Zero_Blnc,0)=1 Then
      v_whr_hide_zero_blnc:= 'where (Nvl(Dr_Amt, 0) - Nvl(Cr_Amt, 0) + Nvl(Opening_Balance, 0))<>0 ';
   End If;
   -----------------------------------
   If Nvl(P_Blnc_Type, 1) = 1 Then
      V_Sql_Qry      := 'SELECT   C_CODE,
                                  C_Name,
                                  Rep_Code,
                                  Doc_Date,
                                  Doc_Type,
                                  Doc_No,
                                  Doc_ser,
                                  Ref_No,
                                  Doc_Desc,
                                  A_Cy,
                                  Doc_Typ_Nm,
                                 SUM( (CASE Doc_Type WHEN 0 THEN (CASE WHEN NVL(Opening_Balance,0)>=0 THEN Opening_Balance ELSE 0 END    )  ELSE Dr_Amt END)) Dr_Amt,
                                  SUM((CASE Doc_Type WHEN 0 THEN (CASE WHEN NVL(Opening_Balance,0)<0  THEN ABS(Opening_Balance) ELSE 0 END )ELSE Cr_Amt END)) Cr_Amt,
                                  (Select Decode(' || P_Lng_No || ', 1, Nvl(Reprs_A_Name, Reprs_A_Name), Nvl(Reprs_A_Name, Reprs_A_Name))
                                          From Sales_Man
                                        WHERE Reprs_Code=T.rep_code
                                        and rownum<=1)rep_Name
                         from
                          (
                          Select B.C_Code,
                                 Decode(' || P_Lng_No || ', 1, Nvl(C_A_Name, C_E_Name), Nvl(C_E_Name, C_A_Name)) C_Name,
                                 ' || V_Fld_Sman || ' REP_CODE,
                                 Null Doc_Date,
                                 0 Doc_Type,
                                 0 Doc_No,
                                 0 Doc_ser,
                                 NULL Ref_No,
                                 Null Doc_Desc,
                                 A_Cy,
                                 Doc_Type_Name(' || P_Lng_No || ', 0, 0) Doc_Typ_Nm,
                                 0 Dr_Amt,
                                 0 Cr_Amt,
                                 Round(Sum(Decode(A_Cy, Ys_Gen_Pkg.Get_Local_Cur, Nvl(Amt, 0), Nvl(Amt_F, 0))), 2) Opening_Balance
                            From dts_v_all_cstmr_balnc A, Customer B
                           Where A.Ac_Code_Dtl = B.C_Code
                                 And B.C_A_CODE=a.A_code
                                 And Ac_Dtl_Typ = 3 '|| V_Whr || ' ' || V_Whr_Sman || '
                                 And (Doc_Date < ''' || V_F_Date || '''
                                      Or Doc_Type = 0)
                        Group By B.C_Code,
                                 Decode(' || P_Lng_No || ', 1, Nvl(C_A_Name, C_E_Name), Nvl(C_E_Name, C_A_Name)),
                                 ' || V_Fld_Sman || ',
                                 A_Cy,
                                 Doc_Type_Name(' || P_Lng_No || ', 0, 0)
                        UNION ALL
                        Select   B.C_Code,
                                 Decode(' || P_Lng_No || ', 1, Nvl(C_A_Name, C_E_Name), Nvl(C_E_Name, C_A_Name)) C_Name,
                                 ' || V_Fld_Sman || ' REP_CODE,
                                 Doc_Date,
                                 Doc_Type,
                                 Doc_No,
                                 Doc_ser,
                                 Ref_No,
                                 Doc_Desc,
                                 A_Cy,
                                 Doc_Type_Name( ' || P_Lng_No ||', Doc_Type, Jv_Type) Doc_Typ_Nm,
                                 Decode(Ias_Gen_Pkg.Get_Local_Cur,a_cy, Round(Dr_Amt, 2),Round(Dr_Amt_F, 2)) Dr_Amt,
                                 Decode(Ias_Gen_Pkg.Get_Local_Cur,a_cy, Round(Cr_Amt, 2),Round(Cr_Amt_F, 2)) Cr_Amt ,
                                 0 Opening_Balance
                        From dts_v_all_cstmr_balnc A, Customer B
                        Where A.Ac_Code_Dtl = B.C_Code
                             And B.C_A_CODE=a.A_code
                             and  Ac_Dtl_Typ=3
                             AND  DOC_TYPE<>0 '||V_Whr||' '||V_Whr_Sman|| '
                             And  A.doc_date between '''||V_F_Date||''' and  '''|| V_T_Date ||'''
                             ) T
                             GROUP BY
                             C_CODE,
                                  C_Name,
                                  Rep_Code,
                                  Doc_Date,
                                  Doc_Type,
                                  Doc_No,
                                  Doc_ser,
                                  Ref_No,
                                  Doc_Desc,
                                  A_Cy,
                                  Doc_Typ_Nm
                       Order By A_Cy ,Doc_Date, Doc_Type, Doc_No  ';
   Else
      V_Sql_Qry      := 'Select C_Code,
                                C_Name,
                                REP_CODE,
                                (Select Decode(' || P_Lng_No || ', 1, Nvl(Reprs_A_Name, Reprs_A_Name), Nvl(Reprs_A_Name, Reprs_A_Name))
                                   From Sales_Man
                                   WHERE Reprs_Code=T.rep_code
                                   and rownum<=1 )rep_Name,
                               A_Cy,
                               Dr_Amt,
                               Cr_Amt,
                               Opening_Balance,
                               (Nvl(Dr_Amt, 0) - Nvl(Cr_Amt, 0) + Nvl(Opening_Balance, 0)) Blnc_Amt
                          From (  Select C_Code,
                                         C_Name,
                                         REP_CODE,
                                         A_Cy,
                                         Sum(Dr_Amt) Dr_Amt,
                                         Sum(Cr_Amt) Cr_Amt,
                                         Sum(Opening_Balance) Opening_Balance
                                    From (  Select B.C_Code,
                                                   Decode(' || P_Lng_No || ', 1, Nvl(C_A_Name, C_E_Name), Nvl(C_E_Name, C_A_Name)) C_Name,
                                                   null REP_CODE,
                                                   A_Cy,
                                                   0 Dr_Amt,
                                                   0 Cr_Amt,
                                                   Round(Sum(Decode(A_Cy, Ys_Gen_Pkg.Get_Local_Cur, Nvl(Amt, 0), Nvl(Amt_F, 0))), 2) Opening_Balance
                                              From dts_v_all_cstmr_balnc A, Customer B
                                             Where A.Ac_Code_Dtl = B.C_Code
                                                   And B.C_A_CODE=a.A_code
                                                   And Ac_Dtl_Typ = 3 '||V_Whr||' '||V_Whr_Sman|| '
                                                   And (Doc_Date < '''||V_F_Date||'''
                                                        Or Doc_Type = 0)
                                          Group By B.C_Code, Decode('||P_Lng_No|| ', 1, Nvl(C_A_Name, C_E_Name), Nvl(C_E_Name, C_A_Name)), A_Cy
                                          Union All
                                            Select B.C_Code,
                                                   Decode(' || P_Lng_No || ', 1, Nvl(C_A_Name, C_E_Name), Nvl(C_E_Name, C_A_Name)) C_Name,
                                                   null REP_CODE,
                                                   A_Cy,
                                                   Round(Sum(Decode(A_Cy, Ys_Gen_Pkg.Get_Local_Cur, Nvl(Dr_Amt, 0), Nvl(Dr_Amt_F, 0))), 2) Dr_Amt,
                                                   Round(Sum(Decode(A_Cy, Ys_Gen_Pkg.Get_Local_Cur, Nvl(Cr_Amt, 0), Nvl(Cr_Amt_F, 0))), 2) Cr_Amt,
                                                   0 Opening_Balance
                                              From dts_v_all_cstmr_balnc A, Customer B
                                             Where A.Ac_Code_Dtl = B.C_Code
                                                   And B.C_A_CODE=a.A_code
                                                   And Ac_Dtl_Typ = 3
                                                   And Doc_Type <> 0 ' || V_Whr || ' ' || V_Whr_Sman || '
                                                   And a.doc_date between ''' || V_F_Date || ''' and  ''' || V_T_Date || '''
                                          Group By B.C_Code, Decode(' || P_Lng_No || ', 1, Nvl(C_A_Name, C_E_Name), Nvl(C_E_Name, C_A_Name)) , A_Cy)
                                Group By C_Code, C_Name,REP_CODE, A_Cy) T '||v_whr_hide_zero_blnc || ' ';
   End If;

   --------------------------------------------
       Qry_Rslt:=Genrat_Data_File (P_Doc_Type          => Null
                                  ,P_Mst_Qry           =>V_Sql_Qry
                                  ,P_Dtl_Qry           =>Null
                                  ,P_Mst_Dtl_Flg       => 0
                                  ,P_Out_Data_Typ      =>P_Out_Data_Typ) ;
       commit;
       Return Qry_Rslt;
   --------------------------------------------
  --####################--
  <<Rtn_rslt>>
   If V_Msg_Txt Is Not Null Then
      -- V_Json_Rslt := Replace(V_Json_Rslt, '@DOC_NO', Null);
      V_Json_Rslt := Replace(V_Json_Rslt, '@ERRNO', Nvl(V_Err_Line, '-1'));
      V_Json_Rslt := Replace(V_Json_Rslt, '@ERRMSG', V_Msg_Txt);
      Return V_Json_Rslt;
   End If;
--####################--
Exception
   When Others Then
   rollback;
      Raise_Application_Error(-20104, 'Error In Get_Cstmr_Blnc_Fnc.' || Chr(10) || Sqlerrm);
End Get_Cstmr_Blnc_Fnc;
--================================================================================---
--================================================================================---06-06-2023
FUNCTION Get_Cst_Aging_Fnc ( P_Sys_No          In     Number,
                                P_F_C_Code        In     Varchar2                   Default Null,
                                P_T_C_Code        In     Varchar2                   Default Null,
                                P_Rep_Code        In     Varchar2                   Default Null,
                                P_T_Date          In     Date                       Default Null,
                                P_Curr_Code       In     Varchar2                   Default Null,  --## CURRENCEY
                                P_Due_Amt_Type    In     Number                     Default 1,--1 Total Due Amount By Credit Period 2-Total Due Amount By Due Date
                                P_Conn_Prv_Year   In     Number                     Default 0,  --## 1- Conn.With Previous Year
                                P_Brn_Year        In     Number,
                                P_Brn_Usr         In     Number,
                                P_User_No         In     Number,
                                P_F_C_GROUP_CODE  IN     CUSTOMER.C_GROUP_CODE%TYPE Default Null,
                                P_T_C_GROUP_CODE  IN     CUSTOMER.C_GROUP_CODE%TYPE Default Null,
                                P_F_C_CLASS       IN     CUSTOMER.C_CLASS%TYPE      Default Null,
                                P_T_C_CLASS       IN     CUSTOMER.C_CLASS%TYPE      Default Null,
                                P_F_ACTV_NO       IN     IAS_POST_DTL.ACTV_NO%TYPE  Default Null,
                                P_T_ACTV_NO       IN     IAS_POST_DTL.ACTV_NO%TYPE  Default Null,
                                P_Whr             In     Varchar2                   Default Null,
                                P_Lng_No          In     Number                     Default 1,
                                P_Out_Data_typ    In     Number                     Default 0,--## 0- xml # 1-query,
                                P_Rprt_Type       In     Number                     Default 1,
                                P_Paid_Inst_Mnl   In     Number                     Default 1
                                ) Return Clob
Is
Pragma Autonomous_Transaction;
   V_F_C_Code              Varchar2 (500);
   V_T_C_Code              Varchar2 (500);
   V_F_Date                Date;
   V_T_Date                Date;
   V_Whr_Data              Varchar2 (8000);
   V_Whr_Inst_Mnl          Varchar2 (8000);
   V_Aralt                 Number (1) := 0;
   V_Cst_Grp               Varchar2 (500);
   V_Rprt_Sort             Number (1) := 0;
   V_Rprt_Type             Number (1) := 1;
   V_Sman_Grp              Varchar2 (500);
   V_Fill_Cst_Rep_Type     Number (1) := 1;
   V_Conn_Cst_Multi_Sman   Number (1);
   V_Paid_Inst_Mnl         Number:=0;
   V_cstmr_blnc_type       Number:=0;
   V_Cnt                   Number;
   V_Sql_Qry               Clob;
   V_Prd1                  Varchar2 (4000);
   V_Prd2                  Varchar2 (4000);
   V_Prd3                  Varchar2 (4000);
   V_Prd4                  Varchar2 (4000);
   V_Prd5                  Varchar2 (4000);
   V_Lng_No                Number (1):=Nvl (P_Lng_No, 1);
   V_Due_Amt_Type          Number (1) := Nvl (P_Due_Amt_Type, 1);
   V_Due_Amt_Fld           Varchar2 (8000);
   V_Local_Cur             Varchar2 (500);
   Qry_Ctx                 Dbms_Xmlgen.Ctxhandle;
   Qry_Rslt                Clob;
   V_Json_Rslt             Varchar2 (4000);
   V_Msg_Txt               Varchar2 (4000);
   V_UNPSTED_FLD           Varchar2 (4000);
   V_prd_Whr               VarchAR2(500);
   V_F_C_GROUP_CODE        CUSTOMER.C_GROUP_CODE%TYPE:=P_F_C_GROUP_CODE;
   V_T_C_GROUP_CODE        CUSTOMER.C_GROUP_CODE%TYPE:=P_T_C_GROUP_CODE;
   V_F_C_CLASS              CUSTOMER.C_CLASS%TYPE:=P_F_C_CLASS;
   V_T_C_CLASS              CUSTOMER.C_CLASS%TYPE:=P_T_C_CLASS;
   V_F_ACTV_NO              IAS_POST_DTL.ACTV_NO%TYPE:=P_F_ACTV_NO;
   V_T_ACTV_NO              IAS_POST_DTL.ACTV_NO%TYPE:=P_T_ACTV_NO;
Begin
   V_Json_Rslt :=    '{"_Result": { "_Doc_No":"@DOC_NO","_ErrMsg": "@errmsg","_ErrNo": @errno } }';

   If P_Sys_No Is Null Then
      V_Msg_Txt := 'ENTER P_SYS_NO   ';
      Goto Rtn_Rslt;
   End If;

   If P_Sys_No = 70
      And P_Rep_Code Is Null Then
      V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => V_Lng_No, P_Msg_No => 811);
      Goto Rtn_Rslt;
   End If;

   If P_Brn_Year Is Null Then
      V_Msg_Txt := 'BRN_YEAR Is Null , Must Be Entered , ';
      Goto Rtn_Rslt;
   End If;

   If P_Brn_Usr Is Null Then
      V_Msg_Txt := 'P_Brn_Usr Is Null , Must Be Entered , ';
      Goto Rtn_Rslt;
   End If;

   If P_User_No Is Null Then
      V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => V_Lng_No, P_Msg_No => 450);
      Goto Rtn_Rslt;
   End If;

   Begin
      Select Nvl (Ar_Ac_Link_Type, 0), Nvl (Conn_Cst_Multi_Sman, 0),NVL(PAID_INSTLLMNT_MAN,0)
        Into V_Aralt, V_Conn_Cst_Multi_Sman,V_Paid_Inst_Mnl
        From Ias_Para_Ar;
   Exception
      When Others Then
         Null;
   End;
   If Nvl(P_sys_no,0)=70 Then
     Begin
       V_cstmr_blnc_type:=Ias_gen_pkg.Get_cnt('Select NVL (CSTMR_BLNC_TYPE, 0) From DTS_PARA');
     Exception When Others Then
      V_cstmr_blnc_type:=0;
     End;
   End If;

   Begin
      Execute Immediate 'ALTER SESSION SET NLS_DATE_FORMAT=''DD/MM/RRRR''';
   End;

   V_F_C_Code :=     P_F_C_Code;
   V_T_C_Code :=     P_T_C_Code;
   V_Local_Cur :=    Ias_Gen_Pkg.Get_Local_Cur;
   ------------------------------------------
   --## C_CODE
   If V_F_C_Code Is Null And V_T_C_Code Is Not Null Then
      V_F_C_Code := V_T_C_Code;
   Elsif V_F_C_Code Is Not Null And V_T_C_Code Is Null Then
      V_T_C_Code := V_F_C_Code;
   End If;

   If V_F_C_Code Is Not Null Then
    Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   => V_F_C_Code,
                                      P_TN   => V_T_C_Code,
                                      P_Type => 'C') ;
   End If;
   ------------------------------------------
   --## C_GROUP_CODE
   If V_F_C_GROUP_CODE Is Null And V_T_C_GROUP_CODE Is Not Null Then
      V_F_C_GROUP_CODE := V_T_C_GROUP_CODE;
   Elsif V_F_C_GROUP_CODE Is Not Null And V_T_C_GROUP_CODE Is Null Then
      V_T_C_GROUP_CODE := V_F_C_GROUP_CODE;
   End If;

   If V_F_C_GROUP_CODE Is Not Null Then
    Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   => V_F_C_GROUP_CODE,
                                      P_TN   => V_T_C_GROUP_CODE,
                                      P_Type => 'N') ;
   End If;
   ------------------------------------------
   --## C_CLASS
   If V_F_C_CLASS Is Null And V_T_C_CLASS Is Not Null Then
      V_F_C_CLASS := V_T_C_CLASS;
   Elsif V_F_C_CLASS Is Not Null And V_T_C_CLASS Is Null Then
      V_T_C_CLASS := V_F_C_CLASS;
   End If;

   If V_F_C_CLASS Is Not Null Then
    Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   => V_F_C_CLASS,
                                      P_TN   => V_T_C_CLASS,
                                      P_Type => 'N') ;
   End If;
   ------------------------------------------
   --## ACTV_NO
   If V_F_ACTV_NO Is Null And V_T_ACTV_NO Is Not Null Then
      V_F_ACTV_NO := V_T_ACTV_NO;
   Elsif V_F_ACTV_NO Is Not Null And V_T_ACTV_NO Is Null Then
      V_T_ACTV_NO := V_F_ACTV_NO;
   End If;

   If V_F_ACTV_NO Is Not Null Then
    Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   => V_F_ACTV_NO,
                                      P_TN   => V_T_ACTV_NO,
                                      P_Type => 'C') ;
   End If;
   ------------------------------------------

   V_Whr_Data :=     V_Whr_Data || ' AND A.C_Code =B.C_Code ';
   V_Whr_Data :=     V_Whr_Data || ' AND A.C_A_Code=B.A_Code ';
   V_Whr_Data :=     V_Whr_Data || ' AND B.C_Code IS NOT NULL ';

   ------------------------------------------
   If V_F_C_Code Is Not Null Then
      V_Whr_Data :=     V_Whr_Data || ' And LPAD(a.C_Code,30,''0'') Between LPAD(''' || V_F_C_Code || ''',30,''0'') And  LPAD(''' || V_T_C_Code || ''',30,''0'') ';
      V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' and b.c_code between nvl(''' || V_F_C_Code || ''',b.c_code) and nvl(''' || V_T_C_Code || ''',b.c_code) ';
   End If;
   -----------------------------------------------------------------
   If V_F_C_GROUP_CODE Is Not Null Then
       V_Whr_Data :=V_Whr_Data || ' And Nvl(a.C_GROUP_CODE,0) Between '|| V_F_C_GROUP_CODE ||' And '||V_T_C_GROUP_CODE||' ';
       V_Whr_Inst_Mnl :=V_Whr_Inst_Mnl ||' And Nvl(a.C_GROUP_CODE,0) Between '|| V_F_C_GROUP_CODE ||' And '||V_T_C_GROUP_CODE||' ';
   End If;
   -----------------------------------------------------------------
   If V_F_C_CLASS Is Not Null Then
       V_Whr_Data :=V_Whr_Data || ' And Nvl(a.C_CLASS,0) Between '|| V_F_C_CLASS ||' And '||V_T_C_CLASS||' ';
       V_Whr_Inst_Mnl :=V_Whr_Inst_Mnl ||' And Nvl(a.C_CLASS,0) Between '|| V_F_C_CLASS ||' And '||V_T_C_CLASS||' ';
   End If;
   -----------------------------------------------------------------
   If V_F_ACTV_NO Is Not Null Then
     V_Whr_Data :=     V_Whr_Data || ' And LPAD(b.ACTV_NO,30,''0'') Between LPAD(''' || V_F_ACTV_NO || ''',30,''0'') And  LPAD(''' || V_T_ACTV_NO || ''',30,''0'') ';
     V_Whr_Inst_Mnl :=V_Whr_Inst_Mnl || ' And LPAD(b.ACTV_NO,30,''0'') Between LPAD(''' || V_F_ACTV_NO || ''',30,''0'') And  LPAD(''' || V_T_ACTV_NO || ''',30,''0'') ';
   End If;
   -----------------------------------------------------------------
   V_Whr_Data :=     V_Whr_Data || ' And Exists(Select C_Code
                        From Ias_V_List_Ccode
                       Where C_Code = A.C_Code
                         And Rownum <= 1) ';
   V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' And Exists(Select C_Code
                        From Ias_V_List_Ccode
                       Where C_Code = A.C_Code
                         And Rownum <= 1) ';
   -----------------------------------------------------------------
   V_T_Date :=       P_T_Date;

   If P_T_Date Is Null Then
      V_F_Date := Ias_Gen_Pkg.Get_Frst_Day;
      V_T_Date := Ias_Gen_Pkg.Get_Curdate;
   Else
      V_F_Date := Ias_Gen_Pkg.Get_Frst_Day;
      V_T_Date := P_T_Date;
   End If;

   V_Whr_Data :=     V_Whr_Data || ' And Doc_Date <= to_date(''' || V_T_Date || ''',''dd/mm/yyyy'') ';
   V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' And Doc_Date <= ''' || V_T_Date || ''' ';

   -----------------------------------------------------------------
   --## REP_CODE
   If P_Rep_Code Is Not Null Then
     IF  NVL(P_SYS_NO,0)=70 THEN
           IF NVL(V_cstmr_blnc_type,0)=1 THEN
                If V_Fill_Cst_Rep_Type = 1 Then
                     V_Whr_Data := V_Whr_Data || ' AND Nvl(B.Rep_Code, ''0'')  Between ''' || P_Rep_Code || ''' AND  ''' || P_Rep_Code || ''' ';
                Else
                     V_Whr_Data := V_Whr_Data || ' AND Nvl(A.Rep_Code, ''0'')  Between ''' || P_Rep_Code || ''' AND  ''' || P_Rep_Code || ''' ';
                End If;
           END IF;
     ELSE
          If V_Fill_Cst_Rep_Type = 1 Then
             V_Whr_Data := V_Whr_Data || ' AND Nvl(B.Rep_Code, ''0'')  Between ''' || P_Rep_Code || ''' AND  ''' || P_Rep_Code || ''' ';
          Else
             V_Whr_Data := V_Whr_Data || ' AND Nvl(A.Rep_Code, ''0'')  Between ''' || P_Rep_Code || ''' AND  ''' || P_Rep_Code || ''' ';
          End If;

      V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' AND Nvl(A.Rep_Code, ''0'')  Between ''' || P_Rep_Code || ''' AND  ''' || P_Rep_Code || ''' ';
     END IF;
   End If;
   ----------------------------------------------------------------
   If Nvl (V_Rprt_Type, 0) = 3 Then
      If Nvl (V_Fill_Cst_Rep_Type, 1) = 1 Then
         V_Sman_Grp := '  Nvl(B.Rep_Code, ''0'') ';
         V_Whr_Data := V_Whr_Data || ' AND  B.Rep_Code IS NOT NULL ';
      Else
         V_Sman_Grp := ' Nvl(A.Rep_Code, ''0'') ';
         V_Whr_Data := V_Whr_Data || ' AND  A.Rep_Code IS NOT NULL ';
      End If;
   Else
      V_Sman_Grp := '''0''';
   End If;

   ----------------------------------------------------------------
   If P_Curr_Code Is Not Null Then
      V_Whr_Data :=     V_Whr_Data || ' And B.A_Cy =''' || P_Curr_Code || ''' ';
      V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' And B.A_Cy =''' || P_Curr_Code || ''' ';
   End If;

   ----------------------------------------------------------------
   V_Whr_Data :=V_Whr_Data || ' And (   (' || P_User_No || '= 1)
                Or (   (    (' || V_Aralt || ' = 1)
                        And Exists(
                               Select 1
                                 From Priv_Acc
                                Where U_Id = ' || P_User_No || '
                                  And A_Code = A.C_A_Code
                                  And A_Cy = B.A_Cy
                                  And Nvl(View_Flag, 0) = 1
                                  And Rownum <= 1))
                    Or (    (' || V_Aralt || ' = 2)
                        And Exists(
                               Select 1
                                 From Ias_Priv_Customer
                                Where U_Id =' || P_User_No || '
                                  And C_Code = A.C_Code
                                  And A_Cy = B.A_Cy
                                  And Nvl(View_Flag, 0) = 1
                                  And Rownum <= 1)))) ';
   ------------------------------
   V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' And (   (' || P_User_No || '= 1)
                Or (   (    (' || V_Aralt || ' = 1)
                        And Exists(
                               Select 1
                                 From Priv_Acc
                                Where U_Id = ' || P_User_No || '
                                  And A_Code = A.C_A_Code
                                  And A_Cy = B.A_Cy
                                  And Nvl(View_Flag, 0) = 1
                                  And Rownum <= 1))
                    Or (    (' || V_Aralt || ' = 2)
                        And Exists(
                               Select 1
                                 From Ias_Priv_Customer
                                Where U_Id =' || P_User_No || '
                                  And C_Code = A.C_Code
                                  And A_Cy = B.A_Cy
                                  And Nvl(View_Flag, 0) = 1
                                  And Rownum <= 1)))) ';

    V_Whr_Data := V_Whr_Data || ' and Exists(Select 1
                 From   S_brn_usr_priv
                 Where  U_id = '||P_User_No ||'
                 And S_brn_usr_priv.Brn_no = b.Brn_no
                  And Nvl(View_Flag, 1) = 1
                   And Rownum <= 1)  ';
  V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' and Exists(Select 1
                 From   S_brn_usr_priv
                 Where  U_id = '||P_User_No ||'
                 And S_brn_usr_priv.Brn_no = b.Brn_no
                  And Nvl(View_Flag, 1) = 1
                   And Rownum <= 1)  ';
-------------------------------------------------------
   If Nvl (V_Rprt_Sort, 0) = 1 Then
      V_Cst_Grp := ' B.Cc_Code ';
   Elsif Nvl (V_Rprt_Sort, 0) = 2 Then
      V_Cst_Grp := ' B.Pj_No ';
   Elsif Nvl (V_Rprt_Sort, 0) = 3 Then
      V_Cst_Grp := '  B.Actv_No ';
   Else
      V_Cst_Grp := '''0''';
   End If;
   ----------------------------------------------------------------
   If Nvl(V_Paid_Inst_Mnl,0)=1 And Nvl(P_PAID_INST_MNL,0)=1  Then
           V_Paid_Inst_Mnl:=1;
   else
        V_Paid_Inst_Mnl:=0;
   End If;

   If Nvl (V_Paid_Inst_Mnl, 0) = 1
      And Nvl (P_Conn_Prv_Year, 0) = 0 Then
      V_Whr_Data := V_Whr_Inst_Mnl;
   End If;

   --####################################################################--
   --EXECUTE IMMEDIATE('DELETE IAS_CrLimit_Tmp');
   Execute Immediate ('DELETE IAS_CST_CR_TMP');

   Declare
      V_Whr_Sman   Varchar2 (5000) := ' ';
      V_Whr_CST    Varchar2 (5000) := ' ';
   Begin
      If P_Rep_Code Is Not Null Then
         V_Whr_Sman := ' And Rep_Code Between ''' || P_Rep_Code || ''' And ''' || P_Rep_Code || '''';
      End If;
      If V_F_C_Code Is Not Null Then
       V_Whr_CST :=   ' And LPAD(C_Code,30,''0'') Between LPAD(''' || V_F_C_Code || ''',30,''0'') And  LPAD(''' || V_T_C_Code || ''',30,''0'') ';
      End If;

      If V_Conn_Cst_Multi_Sman = 1 And P_Rep_Code Is Not Null Then
         V_Whr_Sman := ' And C_Code In (Select C_Code From Ias_Cst_Sman Where 1=1  ' || V_Whr_Sman || ')  ';
      End If;

      Execute Immediate ('CREATE OR REPLACE VIEW Ias_V_List_Ccode As Select C_Code From Customer Where 1=1 '||V_Whr_CST||' ' || V_Whr_Sman);
   End;

   ----------------------------------------------------------------
   --####################################################################--

   Begin
      Ias_Dstr_Cst_Dr_Pkg.Cst_Aging_Prc (P_Local_Cur       => V_Local_Cur,
                                         P_Paid_Inst_Mnl   => V_Paid_Inst_Mnl,
                                         P_Cst_Grp         => V_Cst_Grp,
                                         P_Sman_Grp        => V_Sman_Grp,
                                         P_Rep_Year        => P_Conn_Prv_Year,
                                         P_Per_No          => Null,
                                         P_F_Day           => Null,
                                         P_T_Day           => Null,
                                         P_T_Date          => V_T_Date,
                                         P_Terminal        => Null,
                                         P_Whr             => V_Whr_Data);
   Exception
      When Others Then
         Raise_Application_Error (-20002, 'Error2  ' || Sqlcode || ' : ' || Sqlerrm);
   End;

   --####################################################################--
   If Nvl(P_Rprt_Type,1)=2 Then
     V_prd_whr:=' and nvl(doc_ser,0)=nvl(A.doc_ser,0)
                 and nvl(rcrd_no,0)=nvl(A.rcrd_no,0) ';
   Else
      V_prd_whr:= ' ';
   End if;
   V_Prd1 :=' (select round(decode (A.a_cy,Ias_Gen_Pkg.Get_Local_Cur,sum(dr_amt),sum(dr_amtf)),2)
                 from IAS_CST_CR_TMP
                        where c_code=A.c_code
                          and a_cy=A.a_cy
                          and per_no between 0 and 30 '||V_prd_whr||'
                           )PRD_0_30 ,';

   ---------------------------
   V_Prd2 :=' (select round(decode (A.a_cy,Ias_Gen_Pkg.Get_Local_Cur,sum(dr_amt),sum(dr_amtf)),2)
                 from IAS_CST_CR_TMP
                        where c_code=A.c_code
                          and a_cy=A.a_cy
                          and per_no between 31 and 60   '||V_prd_whr||'
                           )PRD_31_60 ,';
   ---------------------------
   V_Prd3 :=' ( select round(decode (A.a_cy,Ias_Gen_Pkg.Get_Local_Cur,sum(dr_amt),sum(dr_amtf)),2)
                 from IAS_CST_CR_TMP
                        where c_code=A.c_code
                          and a_cy=A.a_cy
                          and per_no between 61 and 90   '||V_prd_whr||'
                           )PRD_61_90 ,';
   ---------------------------
   V_Prd4 :=         ' ( select round(decode (A.a_cy,Ias_Gen_Pkg.Get_Local_Cur,sum(dr_amt),sum(dr_amtf)),2)
                 from IAS_CST_CR_TMP
                        where c_code=A.c_code
                          and a_cy=A.a_cy
                          and per_no between 91 and 120  '||V_prd_whr||'  ) PRD_91_120 ,';
   ---------------------------
   V_Prd5 :=' ( select round(decode (A.a_cy,Ias_Gen_Pkg.Get_Local_Cur,sum(dr_amt),sum(dr_amtf)),2)
                 from IAS_CST_CR_TMP
                        where c_code=A.c_code
                          and a_cy=A.a_cy
                          and per_no >120  '||V_prd_whr||'
                           )PRD_MORE_120 ';
   ---------------------------
   V_Due_Amt_Fld :=' NVL((CASE WHEN ' || V_Due_Amt_Type || ' = 1 AND Nvl(B.Credit_Period,0)>0 THEN
                             (Select  round(Sum(Decode(A.A_Cy,Ias_Gen_Pkg.Get_Local_Cur,(Dr_Amt),(Dr_Amtf))),2) From IAS_CST_CR_TMP
                              Where C_Code =   A.C_Code
                                And A_Cy   =   A.A_Cy
                                And Per_No >  B.Credit_Period
                                 '||V_prd_whr||'  )
                            WHEN ' || V_Due_Amt_Type || ' = 2 THEN
                             (Select  round(Sum(Decode(A.A_Cy,Ias_Gen_Pkg.Get_Local_Cur,(Dr_Amt),(Dr_Amtf))),2) From IAS_CST_CR_TMP
                              Where C_Code =   A.C_Code
                                And A_Cy   =   A.A_Cy   '||V_prd_whr||'
                                And Doc_Due_Date<= '''||V_T_Date||''')
                    ELSE 0
                   END)  ,0) DUE_AMT ';

  IF NVL(P_SYS_NO,0)=70 THEN
    V_UNPSTED_FLD:=' ,DTS_GEN_PKG.Get_Cst_Trns_bal(  P_Bal_Typ=>2,
                                                      P_C_Code=>C_CODE ,
                                                      P_Acy =>A_CY,
                                                      P_Rep_Code=>'''||P_Rep_Code||''',
                                                      P_Due_Amt_Typ=>0
                                                   ) Unpsted_TRANS ';
  END IF;
   ---------------------------
  If Nvl(P_Rprt_Type,1)=1 Then
   IF NVL(P_SYS_NO,0)=70 THEN
        V_Sql_Qry :='SELECT C_CODE,c_name,A_CY,SUM(Bal)BAL ,SUM(PRD_0_30)PRD_0_30,SUM(PRD_31_60)PRD_31_60,SUM(PRD_61_90)PRD_61_90,SUM(PRD_91_120)PRD_91_120,SUM(PRD_MORE_120) PRD_MORE_120,SUM(DUE_AMT) DUE_AMT,SUM(Unpsted_TRANS)Unpsted_TRANS
           FROM (select  a.c_code,
                      decode(' || V_Lng_No || ',1, nvl(c_a_name,c_e_name) , nvl(c_a_name,c_e_name))c_name,
                       a.a_cy ,
                       round(Decode(A.A_Cy,''' || V_Local_Cur || ''',Sum(Nvl(Dr_Amt,0)),Sum(Nvl(Dr_Amtf,0))),2) Bal,
                       ' || V_Prd1 || V_Prd2 || V_Prd3 || V_Prd4 || V_Prd5 || ',' || V_Due_Amt_Fld || ', 0 Unpsted_TRANS
              from  IAS_CST_CR_TMP a,customer b
            where a.c_code=b.c_code
            group by a.c_code,
            decode(' || V_Lng_No || ',1, nvl(c_a_name,c_e_name) , nvl(c_a_name,c_e_name)),
            a_cy,B.Credit_Period
            UNION ALL
            SELECT a.c_code,decode(1,1, nvl(c_a_name,c_e_name) , nvl(c_a_name,c_e_name))c_name, a.a_cy ,
             NULL Bal,NULL PRD_0_30,NULL PRD_31_60,NULL PRD_61_90,NULL PRD_91_120,NULL PRD_MORE_120,NULL DUE_AMT,A.Net_Amt Unpsted_TRANS
            FROM DTS_V_CST_UNPSTED_SALES A ,customer b
                where a.c_code=b.c_code
                And Exists(Select C_Code
                        From Ias_V_List_Ccode
                       Where C_Code = A.C_Code
                         And Rownum <= 1)
   AND DECODE('||V_cstmr_blnc_type||',1,A.REP_CODE,''0'')=DECODE('||V_cstmr_blnc_type||',1,'''||P_REP_CODE||''',''0'')
   AND DECODE('''||NVL(P_CURR_CODE,'0')||''',''0'',''0'',A.A_CY)=DECODE('''||NVL(P_CURR_CODE,'0')||''',''0'',''0'','''||P_CURR_CODE||''')
    )
   WHERE 1=1 ' || P_Whr || '
GROUP BY C_CODE,c_name,A_CY ';
  ELSE
      V_Sql_Qry :=' SELECT *
               FROM (select  a.c_code,
                          decode(' || V_Lng_No || ',1, nvl(c_a_name,c_e_name) , nvl(c_a_name,c_e_name))c_name,
                           a.a_cy ,
                           round(Decode(A_Cy,''' || V_Local_Cur || ''',Sum(Nvl(Dr_Amt,0)),Sum(Nvl(Dr_Amtf,0))),2) Bal,
                           Credit_Period,' || V_Prd1 || V_Prd2 || V_Prd3 || V_Prd4 || V_Prd5 || ',' || V_Due_Amt_Fld || '
                  from  IAS_CST_CR_TMP a,customer b
                where a.c_code=b.c_code
                group by a.c_code,
                decode(' || V_Lng_No || ',1, nvl(c_a_name,c_e_name) , nvl(c_a_name,c_e_name)),
                a_cy,
                Credit_Period
                ) TBL WHERE 1=1 ' || P_Whr || ' ';
  NULL;
  END IF;
 Else
   V_Sql_Qry := 'select * from (
                Select
                A.C_Code,
                Decode(' || V_Lng_No || ',1,Nvl (C_A_Name, C_E_Name) ,Nvl (C_E_Name, C_A_Name))C_Name,
                A_Cy,
                Doc_No,
                Doc_Type_Name (' || V_Lng_No || ', Doc_Type, Doc_Jv_Type) Doc_Type_Name,
                Doc_Ser,
                Doc_Date,
                Doc_Desc,
                 round(Decode(A_Cy,''' || V_Local_Cur || ''',(Nvl(Dr_Amt,0)),(Nvl(Dr_Amtf,0))),2) Bal,
                           Credit_Period,' || V_Prd1 || V_Prd2 || V_Prd3 || V_Prd4 || V_Prd5 || ',' || V_Due_Amt_Fld || '
         From  IAS_CST_CR_TMP A, Customer B
           Where A.C_Code = B.C_Code
        Order By A.C_Code, A.A_Cy, A.Doc_Date Desc )
        WHERE 1=1 ' || P_Whr || ' ';

 End if;

   --####################################################################--
       Qry_Rslt:=Genrat_Data_File (P_Doc_Type          => Null
                                  ,P_Mst_Qry           =>V_Sql_Qry
                                  ,P_Dtl_Qry           =>Null
                                  ,P_Mst_Dtl_Flg       => 0
                                  ,P_Out_Data_Typ      =>P_Out_Data_Typ) ;
       commit;
       Return Qry_Rslt;

  --####################--
  <<Rtn_rslt>>
   If V_Msg_Txt Is Not Null Then
      V_Json_Rslt := Replace (V_Json_Rslt, '@DOC_NO', Null);
      V_Json_Rslt := Replace (V_Json_Rslt, '@errno', 20201);
      V_Json_Rslt := Replace (V_Json_Rslt, '@errmsg', V_Msg_Txt);
      commit;
      return V_Json_Rslt;

   End If;
--####################--

Exception
   When Others Then
      rollback;
      Raise_Application_Error (-20003, 'Error IN Get_Cst_Aging_Fnc ' || Sqlerrm);
End Get_Cst_Aging_Fnc;
--================================================================================---
--================================================================================---
Function Get_Doc_Data_Fnc(P_Doc_Type           In Ias_Post_Mst.Doc_Type%Type
                          ,P_Doc_Ser           In Ias_Post_Mst.Doc_Ser%Type
                          ,P_User_No           In Number
                          ,P_Lng_No            In Number Default 1
                          ,P_Out_Data_typ      In Number Default 0 --## 0- xml # 1-query
                          )Return Clob
Is
   V_Cnt        Number;
   V_Xml_Txt    Clob;
   V_Xml_Typ    Xmltype;
   V_Lng_No     Number;
   V_Doc_Ser    Varchar2 (500);
   V_Json_Rslt  Varchar2 (500):=  '{"_Result": { "_ErrMsg": "@ERRMSG","_ErrNo": @ERRNO } }';
   V_Tag_Mst    Varchar2 (500) := 'DOC_MST';
   V_Tag_Dtl    Varchar2 (500) := 'DOC_DTL';
   V_Tag        Varchar2 (500) := 'DOC';
   V_Msg_Txt    Varchar2 (4000);
   V_Pkg_Line   Varchar2 (4000);
   Qry_Ctx      Dbms_Xmlgen.Ctxhandle;
   V_Qry_Mst    Clob;
   V_Qry_Dtl    Clob;
   V_Xml        Clob;
   V_Tbl_Mst    Varchar2 (500);
   V_Tbl_Dtl    Varchar2 (500);
   V_ALLOW_CALL_REP_BTN NUMBER(2):=0;
   Qry_Rslt                Clob;
    V_WEB_SRVC_UUID       ias_bill_mst.WEB_SRVC_UUID%type;
    V_brn_no       ias_bill_mst.brn_no%type;
    V_USE_E_INVOICE         number(2);
    V_QR_CODE            Varchar2 (32000) ;

Begin
   ----------------------------------------------------------------------------------
   BEGIN
     SELECT ALLOW_CALL_REP_BTN INTO V_ALLOW_CALL_REP_BTN FROM PRIVILEGE_FIXED
       WHERE U_ID=P_User_No
       AND ROWNUM<=1;
   EXCEPTION WHEN OTHERS THEN
     V_ALLOW_CALL_REP_BTN:=0;
   END;
    IF NVL(V_ALLOW_CALL_REP_BTN,0)=0 THEN
     V_Msg_Txt:=Ias_Gen_Pkg.Get_MSG(P_Lng_No,592);
      V_Json_Rslt := Replace(V_Json_Rslt, '@ERRNO', '-1');
      V_Json_Rslt := Replace(V_Json_Rslt, '@ERRMSG', V_Msg_Txt);
      Return V_Json_Rslt;
    END IF;
   ----------------------------------------------------------------------------------
   If P_Doc_Type = 4 Then
      Begin
         Select 1
           Into V_Cnt
           From Ias_Bill_Mst
          Where Bill_Ser = P_Doc_Ser And Rownum <= 1;

         V_Tbl_Mst   := ' IAS_BILL_MST  ';
         V_Tbl_Dtl   := ' IAS_BILL_DTL ';
      Exception
         When No_Data_Found Then
            Begin
               Select 1
                 Into V_Cnt
                 From Ias_Bill_Mst_Br
                Where Bill_Ser = P_Doc_Ser And Rownum <= 1;

               V_Tbl_Mst   := ' IAS_BILL_MST_BR  ';
               V_Tbl_Dtl   := ' IAS_BILL_DTL_BR ';
            Exception
               When No_Data_Found Then
                  Begin
                    EXECUTE IMMEDIATE '  Select 1
                       From Ias_V_Bill_Mst_Yr
                      Where Bill_Ser ='|| P_Doc_Ser ||' And Rownum <= 1 ' INTO V_CNT;

                     V_Tbl_Mst   := ' IAS_V_BILL_MST_YR   ';
                     V_Tbl_Dtl   := ' IAS_V_BILL_DTL_YR ';
                  Exception
                     When Others Then
                        Raise_Application_Error (-20104, ' ERROR WHEN GET TABLE MST' || Chr (10) || Sqlerrm);
                  End;
            End;
      When Others Then
            Raise_Application_Error (-20104, ' ERROR WHEN GET TABLE MST' || Chr (10) || Sqlerrm);
      End;
      ----------------------------------------------------------------------------
      If P_Doc_Ser Is Not Null Then
            Begin
            execute immediate ' SELECT BRN_NO,WEB_SRVC_UUID
             FROM '||V_Tbl_Mst||'
                WHERE  BILL_SER='||P_DOC_SER||'
                       AND ROWNUM<=1 '
                   INTO V_BRN_NO,V_WEB_SRVC_UUID;
           Exception when Others Then
               V_BRN_NO:=null;
               V_WEB_SRVC_UUID:=null;
           End ;

            If Nvl(Ias_Brn_Pkg.Is_Brn_Use_E_Invc (P_Brn_No => V_BRN_NO ),0) =1
                And  Nvl(YS_TAX_PKG.GET_ETS_SRVC_FLG_FNC(P_BRN_NO => V_BRN_NO),0) = 1 And  V_WEB_SRVC_UUID Is Not Null Then
                    Begin
                      GNR_TECH_SOLUTION_PKG.INITIALIZE(YS_JSON_PKG.GET_E_INVC_SRVC_NO_FNC ( P_BRN_NO  =>V_BRN_NO ));
                    Exception when Others Then
                          Raise_Application_Error (-20107, ' Err.  In GNR_TECH_SOLUTION_PKG.INITIALIZE  ' || Chr (10) || Sqlerrm);
                    End ;

                    Begin
                      V_QR_CODE:=''''||GNR_TECH_SOLUTION_PKG.GETQRCODE(V_WEB_SRVC_UUID)||'''';
                    Exception when Others Then
                        Raise_Application_Error (-20108, ' Err When Get GETQRCODE  ' || Chr (10) || Sqlerrm);
                    End ;
           End If;
      End If;
   ----------------------------------------------------------
    If V_Qr_Code Is Null Then
      V_Qr_Code:=' Null ';
    End if;
      -----------------------------------------------------------------------------
      V_Qry_Mst   := 'SELECT 4 DOC_TYPE
                              ,DOC_TYPE_NAME('||P_LNG_NO||',4) Doc_Typ_Nm
                              ,M.BILL_DOC_TYPE
                              , (SELECT FLG_DESC
                                   FROM S_FLAGS
                                  WHERE FLG_CODE = ''TYPE_NAME_SI''
                                  AND FLG_VALUE=M.BILL_DOC_TYPE
                                  AND LANG_NO= '||P_LNG_NO||'
                                   AND ROWNUM <= 1)BILL_DOC_TYPE_NM
                              ,M.BILL_NO DOC_NO
                              ,M.BILL_SER DOC_SER
                              ,M.BILL_DATE DOC_DATE
                              ,M.BILL_CURRENCY CUR_CODE
                              , (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (CUR_NAME, CUR_E_NAME), NVL (CUR_E_NAME, CUR_NAME)) CUR_NAME
                                   FROM EX_RATE
                                  WHERE CUR_CODE = M.BILL_CURRENCY AND ROWNUM <= 1)CUR_NAME
                              ,M.BILL_RATE CUR_RATE
                              ,M.STOCK_RATE
                              ,M.C_CODE
                              , (CASE
                                    WHEN M.C_CODE IS NOT NULL THEN
                                       (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (C_A_NAME, C_E_NAME), NVL (C_E_NAME, C_A_NAME)) C_NAME
                                          FROM CUSTOMER
                                         WHERE C_CODE = M.C_CODE AND ROWNUM <= 1)
                                    ELSE
                                       M.C_NAME
                                 END) C_NAME
                              ,M.A_CODE
                              ,M.CHEQUE_NO
                              ,M.NOTE_NO
                              ,M.CHEQUE_DUE_DATE
                              ,M.BILL_DUE_DATE
                              ,M.W_CODE
                              , (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (W_NAME, W_E_NAME), NVL (W_E_NAME, W_NAME)) W_NAME
                                   FROM WAREHOUSE_DETAILS
                                  WHERE W_CODE = M.W_CODE AND ROWNUM <= 1) W_NAME
                              ,M.R_CODE
                              ,M.REP_CODE
                              , (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (REPRS_A_NAME, REPRS_E_NAME), NVL (REPRS_E_NAME, REPRS_A_NAME)) REP_NAME
                                   FROM SALES_MAN
                                  WHERE REPRS_CODE = M.REP_CODE AND ROWNUM <= 1)  REP_NAME
                              ,M.EMP_NO
                              ,M.REF_NO
                              ,M.CASH_NO
                              , (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (CASH_NAME, CASH_E_NAME), NVL (CASH_E_NAME, CASH_NAME)) CASH_NAME
                                   FROM CASH_IN_HAND
                                  WHERE CASH_NO = M.CASH_NO AND ROWNUM <= 1) CASH_NAME
                              ,M.CC_CODE
                              ,M.PJ_NO
                              ,M.ACTV_NO
                              ,M.SI_TYPE
                              ,M.STAND_BY
                              ,M.COL_NO
                              ,M.CASH_AC_FCC
                              ,M.CASH_NO_FCC BANK_NO
                              ,M.A_DESC
                              ,M.EXTERNAL_POST
                              ,M.C_TEL
                              ,M.C_ADDRESS
                              ,M.DRIVER_NO
                              ,M.PRM_CODE
                              ,M.DOC_BRN_NO
                              ,M.MOBILE_NO
                              ,M.C_CODE_CSH
                              ,M.C_TAX_CODE
                              ,M.AC_CODE
                              ,M.AC_CODE_DTL
                              ,M.AC_DTL_TYP
                              ,M.PYMNT_AC
                              ,M.CLC_TYP_NO_TAX
                              ,M.DOC_SER_EXTRNL
                              ,M.CNCL_FLG
                              ,M.CLC_VAT_PRICE_TYP
                              ,M.BILL_AMT
                              ,M.VAT_AMT
                              ,M.DISC_AMT_AFTR_VAT
                              ,M.DISC_AMT_MST_VAT
                              ,M.VAT_AMT_DISC_MST
                              ,M.VAT_AMT_OTHR
                              ,M.OTHR_AMT
                              ,M.DISC_AMT
                              ,M.DISC_AMT_MST
                              ,M.DISC_AMT_DTL
                              ,M.ADD_DISC_AMT_MST
                              ,M.ADD_DISC_AMT_DTL
                              ,M.OTHR_AMT_DISC
                              ,M.CRD_DISC_PER
                              ,M.CRD_NO_DISC
                              ,M.CREDIT_CARD
                              ,M.CR_CARD_AMT
                              ,M.CR_CARD_AMT_SCND
                              ,M.CR_CARD_AMT_THRD
                              ,M.CR_CARD_COMM_PER
                              ,M.CR_CARD_COMM_PER_SCND
                              ,M.CR_CARD_COMM_PER_THRD
                              ,M.CR_CARD_CST_NO
                              ,M.CR_CARD_CST_NO_SCND
                              ,M.CR_CARD_CST_NO_THRD
                              ,M.CR_CARD_DOC_NO_REF
                              ,M.CR_CARD_DOC_NO_REF_SCND
                              ,M.CR_CARD_DOC_NO_REF_THRD
                              ,M.CR_CARD_DSC
                              ,M.CR_CARD_DSC_SCND
                              ,M.CR_CARD_DSC_THRD
                              ,M.CR_CARD_MAX_COMM_AMT
                              ,M.CR_CARD_MAX_COMM_AMT_SCND
                              ,M.CR_CARD_MAX_COMM_AMT_THRD
                              ,M.CR_CARD_NO
                             ,(Select Decode( '||P_LNG_NO||' ,1,nvl(CR_CARD_NAME,CR_CARD_E_NAME),CR_CARD_E_NAME) CR_CARD_NAME
                                        from Credit_Card_Types
                                      Where Cr_Card_No=M.Cr_Card_No AND ROWNUM<=1)CR_CARD_NAME
                              ,M.CR_CARD_NO_SCND
                              ,M.CR_CARD_NO_THRD
                              ,M.CPN_AMT
                              ,M.CHEQUE_AMT
                              ,M.PRCNT_AMT
                              ,M.AC_AMT
                              ,M.WEB_SRVC_UUID
                              ,'||V_Qr_Code||'  QR_CODE
                              ,M.CMP_NO
                              ,M.BRN_NO
                              ,M.BRN_YEAR
                              ,M.BRN_USR
                              ,M.AD_U_ID
                              ,M.AD_DATE
                              ,M.AD_TRMNL_NM
                              ,DECODE('||P_LNG_NO||' ,1,NVL(BRN_LNAME,BRN_FNAME),NVL(BRN_FNAME,BRN_LNAME))BRN_NM
                              ,DECODE('||P_LNG_NO||',1,NVL(CMP_LNAME,CMP_FNAME),NVL(CMP_FNAME,CMP_LNAME))Cmp_Nm
                              ,TAX_BILL_TYP
                              ,(SELECT Ys_Gen_Pkg.Get_Flg_Nm(''TAX_BILL_TYP'',M.Tax_Bill_Typ ,'||P_LNG_NO||')FROM DUAL )Tax_Bill_Typ_Nm
                              ,ROUND(Nvl(M.Bill_Amt,0)-Nvl(M.Disc_Amt,0)+Nvl(M.Othr_Amt,0),2) Total
                              ,ROUND(Nvl(M.Bill_Amt,0)-Nvl(M.Disc_Amt,0)+Nvl(M.Othr_Amt,0)+Nvl(M.Vat_Amt,0),2) Total_With_Vat
                              ,C.Street         C_Street
                              ,C.Shrt_Add       C_Shrt_Add
                              ,C.Dstrct_Nm      C_Dstrct_Nm
                              ,C.Cstmr_Idntfr   C_Cstmr_Idntfr
                              ,C.Cr_No          C_Cr_No
                              ,C.Cntry_No       C_Cntry_No
                              ,C.City_No        C_City_No
                              ,C.C_Since        C_C_Since
                              ,C.C_Phone        C_C_Phone
                              ,C.C_Mobile       C_C_Mobile
                              ,C.C_Group_Code   C_C_Group_Code
                              ,C.C_Class        C_C_Class
                              ,C.C_Box_Code     C_C_Box_Code
                              ,C.C_A_Code       C_C_A_Code
                              ,C.Building_No    C_Building_No
                              ,C.Add_No         C_Add_No
                              ,B.Street         B_Street
                              ,B.Shrt_Add       B_Shrt_Add
                              ,B.Dstrct_Nm      B_Dstrct_Nm
                              ,B.Brn_Idntfr     B_Brn_Idntfr
                              ,B.Rc_Code        B_Rc_Code
                              ,B.Cntry_No       B_Cntry_No
                              ,B.City_No        B_City_No
                              ,B.Prov_No        B_Prov_No
                              ,B.Brn_Tel_No     B_Brn_Tel_No
                              ,B.Postal_Code    B_Postal_Code
                              ,B.Building_No    B_Building_No
                              ,B.Add_No         B_Add_No
                              ,B.Brn_Tax_Code   B_Brn_Tax_Code
                              ,B.Pos_Ref_Code   B_Pos_Ref_Code
                              ,B.Tax_Auth_Code  B_Tax_Auth_Code
                           FROM '||V_Tbl_Mst|| ' M  ,Customer C ,S_Brn  B
                            Where M.Brn_No=B.Brn_No
                             And  M.C_Code= C.C_Code(+)
                             And  M.Bill_Ser = ' || P_Doc_Ser || '';

      V_Qry_Dtl   := 'SELECT  D.BILL_NO DOC_NO
                              ,D.BILL_SER DOC_SER
                              ,D.I_CODE
                              ,DECODE (  '||P_LNG_NO||' , 1, NVL (I_NAME, I_E_NAME), NVL (I_E_NAME, I_NAME)) I_NAME
                              ,D.ITM_UNT
                              ,D.I_QTY
                              ,D.P_SIZE
                              ,D.P_QTY
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.I_PRICE_VAT,D.I_PRICE) I_PRICE
                              ,D.STK_COST
                              ,D.DOC_SEQUENCE
                              ,D.W_CODE
                              ,D.CC_CODE
                              ,D.PJ_NO
                              ,D.ACTV_NO
                              ,D.EXPIRE_DATE
                              ,D.BATCH_NO
                              ,D.FREE_QTY
                              ,D.VAT_PER
                              ,D.VAT_AMT
                              ,D.OTHR_AMT
                              ,D.ITEM_DESC
                              ,D.BARCODE
                              ,D.DIS_AMT
                              ,D.DIS_PER
                              ,D.DIS_PER2
                              ,D.DIS_PER3
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.DIS_AMT_MST_VAT,D.DIS_AMT_MST) DIS_AMT_MST
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.DIS_AMT_DTL_VAT,D.DIS_AMT_DTL) DIS_AMT_DTL
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.DIS_AMT_DTL2_VAT,D.DIS_AMT_DTL2) DIS_AMT_DTL2
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.DIS_AMT_DTL3_VAT,D.DIS_AMT_DTL3) DIS_AMT_DTL3
                              ,D.ADD_DIS_AMT_MST
                              ,D.ADD_DIS_AMT_DTL
                              ,D.VAT_AMT_OTHR
                              ,D.OTHR_AMT_DISC
                              ,D.DIS_AFTR_VAT_MST
                              ,D.VAT_AMT_DIS_DTL_VAT
                              ,D.VAT_AMT_DIS_DTL3_VAT
                              ,D.VAT_AMT_DIS_DTL2_VAT
                              ,D.VAT_AMT_DIS_MST_VAT
                              ,D.VAT_AMT_BFR_DIS
                              ,D.VAT_AMT_AFTR_DIS
                              ,D.DIS_AMT_AFTR_VAT
                              ,D.DIS_AMT_DTL_QT_PRM
                              ,D.DIS_AMT_DTL_QT_PRM_VAT
                              ,D.DIS_PER_QT_PRM
                              ,D.LEV_NO
                              ,D.PRM_GRP_NO
                              ,D.QT_PRM_RCRD_NO
                              ,D.QT_PRM_SER
                              ,D.I_LENGTH
                              ,D.I_WIDTH
                              ,D.I_HEIGHT
                              ,D.I_NUMBER
                              ,D.WT_QTY
                              ,D.WT_UNT
                              ,D.EMP_NO
                              ,D.MEASUR_PRICE
                              ,D.ARGMNT_NO
                          FROM '||V_Tbl_Mst|| ' M ,'||V_Tbl_DTL|| ' D ,IAS_ITM_MST I
                         WHERE M.BILL_SER=D.BILL_SER
                         AND D.I_CODE=I.I_CODE
                         AND M.BILL_SER = ' || P_Doc_Ser || ' ';
   --##--------------------------------------------------------------------------------------------------------##--
   Elsif P_Doc_Type = 5 Then
      Begin
         Select 1
           Into V_Cnt
           From Ias_RT_Bill_Mst
          Where RT_Bill_Ser = P_Doc_Ser And Rownum <= 1;

         V_Tbl_Mst   := ' IAS_RT_BILL_MST  ';
         V_Tbl_Dtl   := ' IAS_RT_BILL_DTL ';
      Exception
         When No_Data_Found Then
            Begin
               Select 1
                 Into V_Cnt
                 From Ias_RT_Bill_Mst_Br
                Where RT_Bill_Ser = P_Doc_Ser And Rownum <= 1;

               V_Tbl_Mst   := ' IAS_RT_BILL_MST_BR  ';
               V_Tbl_Dtl   := ' IAS_RT_BILL_DTL_BR ';
            Exception
               When No_Data_Found Then
                  Begin
                    EXECUTE IMMEDIATE '  Select 1
                       From Ias_V_RT_Bill_Mst_Yr
                      Where RT_Bill_Ser ='|| P_Doc_Ser ||' And Rownum <= 1 ' INTO V_CNT;

                     V_Tbl_Mst   := ' IAS_V_RT_BILL_MST_YR   ';
                     V_Tbl_Dtl   := ' IAS_V_RT_BILL_DTL_YR ';
                  Exception
                     When Others Then
                        Raise_Application_Error (-20104, ' ERROR WHEN GET TABLE MST' || Chr (10) || Sqlerrm);
                  End;
            End;
      When Others Then
            Raise_Application_Error (-20104, ' ERROR WHEN GET TABLE MST' || Chr (10) || Sqlerrm);
      End;

       ----------------------------------------------------------------------------
          If P_Doc_Ser Is Not Null Then
                Begin
                execute immediate ' SELECT BRN_NO,WEB_SRVC_UUID
                 FROM '||V_Tbl_Mst||'
                    WHERE  RT_BILL_SER='||P_DOC_SER||'
                           AND ROWNUM<=1 '
                       INTO V_BRN_NO,V_WEB_SRVC_UUID;
               Exception when Others Then
                   V_BRN_NO:=null;
                   V_WEB_SRVC_UUID:=null;
               End ;

                If Nvl(Ias_Brn_Pkg.Is_Brn_Use_E_Invc (P_Brn_No => V_BRN_NO ),0) =1
                    And  Nvl(YS_TAX_PKG.GET_ETS_SRVC_FLG_FNC(P_BRN_NO => V_BRN_NO),0) = 1 And  V_WEB_SRVC_UUID Is Not Null Then
                        Begin
                          GNR_TECH_SOLUTION_PKG.INITIALIZE(YS_JSON_PKG.GET_E_INVC_SRVC_NO_FNC ( P_BRN_NO  =>V_BRN_NO ));
                        Exception when Others Then
                              Raise_Application_Error (-20107, ' Err.  In GNR_TECH_SOLUTION_PKG.INITIALIZE  ' || Chr (10) || Sqlerrm);
                        End ;

                        Begin
                          V_QR_CODE:=''''||GNR_TECH_SOLUTION_PKG.GETQRCODE(V_WEB_SRVC_UUID)||'''';
                        Exception when Others Then
                            Raise_Application_Error (-20108, ' Err When Get GETQRCODE  ' || Chr (10) || Sqlerrm);
                        End ;
               End If;
          End If;
       ----------------------------------------------------------
        If V_Qr_Code Is Null Then
          V_Qr_Code:=' Null ';
        End if;
          -----------------------------------------------------------------------------
       V_Qry_Mst   := 'SELECT   5 DOC_TYPE
                              ,DOC_TYPE_NAME('||P_LNG_NO||',5) Doc_Typ_Nm
                              ,M.RT_BILL_NO DOC_NO
                              ,M.RT_BILL_SER DOC_SER
                              ,M.RT_BILL_DOC_TYPE BILL_DOC_TYPE
                              , (SELECT FLG_DESC
                                       FROM S_FLAGS
                                      WHERE FLG_CODE = ''TYPE_NAME_SI''
                                      AND FLG_VALUE=M.RT_BILL_DOC_TYPE
                                      AND LANG_NO= '||P_LNG_NO||'
                                       AND ROWNUM <= 1)BILL_DOC_TYPE_NM
                              ,M.RT_BILL_DATE DOC_DATE
                              ,M.RT_BILL_CURRENCY CUR_CODE
                               , (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (CUR_NAME, CUR_E_NAME), NVL (CUR_E_NAME, CUR_NAME)) CUR_NAME
                                           FROM EX_RATE
                                          WHERE CUR_CODE = M.RT_BILL_CURRENCY AND ROWNUM <= 1)CUR_NAME
                              ,M.RT_BILL_RATE CUR_RATE
                              ,M.STOCK_RATE
                              ,M.P_YEAR
                              ,M.C_CODE
                              , (CASE
                                    WHEN M.C_CODE IS NOT NULL THEN
                                       (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (C_A_NAME, C_E_NAME), NVL (C_E_NAME, C_A_NAME)) C_NAME
                                          FROM CUSTOMER
                                         WHERE C_CODE = M.C_CODE AND ROWNUM <= 1)
                                    ELSE
                                       M.C_NAME
                                 END) C_NAME
                              ,M.A_CODE
                              ,M.CHEQUE_NO
                              ,M.CHEQUE_AMT
                              ,M.CHEQUE_DUE_DATE
                              ,M.RT_BILL_DUE_DATE
                              ,M.W_CODE
                              , (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (W_NAME, W_E_NAME), NVL (W_E_NAME, W_NAME)) W_NAME
                                       FROM WAREHOUSE_DETAILS
                                      WHERE W_CODE = M.W_CODE AND ROWNUM <= 1) W_NAME
                              ,M.R_CODE
                              ,M.CASH_NO
                              , (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (CASH_NAME, CASH_E_NAME), NVL (CASH_E_NAME, CASH_NAME)) CASH_NAME
                                           FROM CASH_IN_HAND
                                          WHERE CASH_NO = M.CASH_NO AND ROWNUM <= 1) CASH_NAME
                              ,M.CC_CODE
                              ,M.PJ_NO
                              ,M.ACTV_NO
                              ,M.CASH_AC_FCC
                              ,M.CASH_NO_FCC BANK_NO
                              ,M.CLC_TYP_NO_TAX
                              ,M.C_TAX_CODE
                              ,M.AC_CODE
                              ,M.AC_CODE_DTL
                              ,M.AC_DTL_TYP
                              ,M.REP_CODE
                              , (SELECT DECODE (  '||P_LNG_NO||' , 1, NVL (REPRS_A_NAME, REPRS_E_NAME), NVL (REPRS_E_NAME, REPRS_A_NAME)) REP_NAME
                                               FROM SALES_MAN
                                              WHERE REPRS_CODE = M.REP_CODE AND ROWNUM <= 1)  REP_NAME
                              ,M.EMP_NO
                              ,M.SR_TYPE
                              ,M.REF_NO
                              ,M.A_DESC
                              ,M.RETURN_RES
                              ,M.PREV_YEAR
                              ,M.STAND_BY
                              ,M.NOTE_NO
                              ,M.DRIVER_NO
                              ,M.DOC_BRN_NO
                              ,M.RES_TYP
                              ,M.PYMNT_AC
                              ,M.AC_AMT
                              ,M.DOC_SER_EXTRNL
                              ,M.CNCL_FLG
                              ,M.CLC_VAT_PRICE_TYP
                              ,M.COL_NO
                              ,M.PRM_CODE
                              ,M.BILL_AMT
                              ,M.DISC_AMT
                              ,M.DISC_AMT_MST
                              ,M.DISC_AMT_DTL
                              ,M.VAT_AMT
                              ,M.OTHR_AMT
                              ,M.OTHR_AMT_DISC
                              ,M.VAT_AMT_OTHR
                              ,M.DISC_AMT_AFTR_VAT
                              ,M.DISC_AMT_MST_VAT
                              ,M.VAT_AMT_DISC_MST
                              ,M.WEB_SRVC_UUID
                              ,'||V_Qr_Code||'  QR_CODE
                              ,M.CMP_NO
                              ,M.BRN_NO
                              ,M.BRN_YEAR
                              ,M.BRN_USR
                              ,M.AD_U_ID
                              ,M.AD_DATE
                              ,M.AD_TRMNL_NM
                              ,DECODE('||P_LNG_NO||' ,1,NVL(BRN_LNAME,BRN_FNAME),NVL(BRN_FNAME,BRN_LNAME))BRN_NM
                              ,DECODE('||P_LNG_NO||',1,NVL(CMP_LNAME,CMP_FNAME),NVL(CMP_FNAME,CMP_LNAME))Cmp_Nm
                              ,TAX_BILL_TYP
                              ,(SELECT Ys_Gen_Pkg.Get_Flg_Nm(''TAX_BILL_TYP'',M.Tax_Bill_Typ ,'||P_LNG_NO||')FROM DUAL )Tax_Bill_Typ_Nm
                              ,ROUND(Nvl(M.Bill_Amt,0)-Nvl(M.Disc_Amt,0)+Nvl(M.Othr_Amt,0),2) Total
                              ,ROUND(Nvl(M.Bill_Amt,0)-Nvl(M.Disc_Amt,0)+Nvl(M.Othr_Amt,0)+Nvl(M.Vat_Amt,0),2) Total_With_Vat
                              ,C.Street         C_Street
                              ,C.Shrt_Add       C_Shrt_Add
                              ,C.Dstrct_Nm      C_Dstrct_Nm
                              ,C.Cstmr_Idntfr   C_Cstmr_Idntfr
                              ,C.Cr_No          C_Cr_No
                              ,C.Cntry_No       C_Cntry_No
                              ,C.City_No        C_City_No
                              ,C.C_Since        C_C_Since
                              ,C.C_Phone        C_C_Phone
                              ,C.C_Mobile       C_C_Mobile
                              ,C.C_Group_Code   C_C_Group_Code
                              ,C.C_Class        C_C_Class
                              ,C.C_Box_Code     C_C_Box_Code
                              ,C.C_A_Code       C_C_A_Code
                              ,C.Building_No    C_Building_No
                              ,C.Add_No         C_Add_No
                              ,B.Street         B_Street
                              ,B.Shrt_Add       B_Shrt_Add
                              ,B.Dstrct_Nm      B_Dstrct_Nm
                              ,B.Brn_Idntfr     B_Brn_Idntfr
                              ,B.Rc_Code        B_Rc_Code
                              ,B.Cntry_No       B_Cntry_No
                              ,B.City_No        B_City_No
                              ,B.Prov_No        B_Prov_No
                              ,B.Brn_Tel_No     B_Brn_Tel_No
                              ,B.Postal_Code    B_Postal_Code
                              ,B.Building_No    B_Building_No
                              ,B.Add_No         B_Add_No
                              ,B.Brn_Tax_Code   B_Brn_Tax_Code
                              ,B.Pos_Ref_Code   B_Pos_Ref_Code
                              ,B.Tax_Auth_Code  B_Tax_Auth_Code
                           FROM '||V_Tbl_Mst|| ' M  ,Customer C ,S_Brn  B
                            Where M.Brn_No=B.Brn_No
                             And  M.C_Code= C.C_Code(+)
                             And  M.Rt_Bill_Ser = ' || P_Doc_Ser || '';

      V_Qry_Dtl   := 'SELECT  M.RT_BILL_NO DOC_NO
                              ,M.RT_BILL_SER DOC_SER
                              ,D.I_CODE
                              ,DECODE (  '||P_LNG_NO||' , 1, NVL (I_NAME, I_E_NAME), NVL (I_E_NAME, I_NAME)) I_NAME
                              ,D.ITM_UNT
                              ,D.I_QTY
                              ,D.P_SIZE
                              ,D.P_QTY
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.I_PRICE_VAT,D.I_PRICE) I_PRICE
                              ,D.STK_COST
                              ,D.DOC_SEQUENCE
                              ,D.W_CODE
                              ,D.CC_CODE
                              ,D.PJ_NO
                              ,D.ACTV_NO
                              ,D.EXPIRE_DATE
                              ,D.BATCH_NO
                              ,D.FREE_QTY
                              ,D.VAT_PER
                              ,D.VAT_AMT
                              ,D.OTHR_AMT
                              ,D.ITEM_DESC
                              ,D.BARCODE
                              ,D.DIS_AMT
                              ,D.DIS_PER
                              ,D.DIS_PER2
                              ,D.DIS_PER3
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.DIS_AMT_MST_VAT,D.DIS_AMT_MST) DIS_AMT_MST
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.DIS_AMT_DTL_VAT,D.DIS_AMT_DTL) DIS_AMT_DTL
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.DIS_AMT_DTL2_VAT,D.DIS_AMT_DTL2) DIS_AMT_DTL2
                              ,DECODE(NVL(M.CLC_VAT_PRICE_TYP,1),2,D.DIS_AMT_DTL3_VAT,D.DIS_AMT_DTL3) DIS_AMT_DTL3
                              ,D.VAT_AMT_OTHR
                              ,D.OTHR_AMT_DISC
                              ,D.DIS_AFTR_VAT_MST
                              ,D.VAT_AMT_DIS_DTL_VAT
                              ,D.VAT_AMT_DIS_DTL3_VAT
                              ,D.VAT_AMT_DIS_DTL2_VAT
                              ,D.VAT_AMT_DIS_MST_VAT
                              ,D.VAT_AMT_BFR_DIS
                              ,D.VAT_AMT_AFTR_DIS
                              ,D.DIS_AMT_AFTR_VAT
                              ,D.I_LENGTH
                              ,D.I_WIDTH
                              ,D.I_HEIGHT
                              ,D.I_NUMBER
                              ,D.WT_QTY
                              ,D.WT_UNT
                              ,D.EMP_NO
                              ,D.ARGMNT_NO
                          FROM '||V_Tbl_Mst|| ' M ,'||V_Tbl_DTL|| ' D ,IAS_ITM_MST I
                         WHERE M.RT_BILL_SER=D.RT_BILL_SER
                         AND D.I_CODE=I.I_CODE
                         AND M.RT_BILL_SER = ' || P_Doc_Ser || ' ';
   --##----------------------------------------------------------------------------##--
   Elsif P_Doc_Type In (11, 12) Then
      V_Qry_Mst   := ' SELECT ' || P_Doc_Type || '           AS  DOC_TYPE
                                 ,DOC_TYPE_NAME('||P_LNG_NO||','|| P_Doc_Type|| ') Doc_Typ_Nm
                                ,TR_TYPE                    AS  TYP_NO
                                ,TR_NO                      AS  DOC_NO
                                ,TR_SER                     AS  DOC_SER
                                ,TR_DATE                    AS  DOC_DATE
                                ,REF_NO                     AS  REF_NO
                                ,T_W_CODE                   AS  T_W_CODE
                                ,F_W_CODE                   AS  F_W_CODE
                                ,CC_CODE                    AS  CC_CODE
                                ,PJ_NO                      AS  PJ_NO
                                ,ACTV_NO                    AS  ACTV_NO
                                ,TR_DESC                    AS  DOC_DESC
                                ,STK_RATE                   AS  STK_RATE
                                ,TR_AMT                     AS  DOC_AMT
                                ,TR_RES                     AS  TR_RES
                                ,PROCESSED_SI               AS  PROCESSED_SI
                                ,HUNG                       AS  HUNG
                                ,T_TR_TYPE                  AS  T_TR_TYPE
                                ,TR_A_CODE                  AS  TR_A_CODE
                                ,EXP_AMT                    AS  EXP_AMT
                                ,C_CODE                     AS  C_CODE
                                ,DOC_BRN_NO                 AS  DOC_BRN_NO
                                ,F_TR_NO                    AS  F_TR_NO
                                ,F_TR_SER                   AS  F_TR_SER
                                ,TR_COST_TYPE               AS  TR_COST_TYPE
                                ,DIFF_A_CODE                AS  DIFF_A_CODE
                                ,DIFF_A_CY                  AS  DIFF_A_CY
                                ,DIFF_AMT                   AS  DIFF_AMT
                                ,RTN_TR                     AS  RTN_TR
                                ,FIELD1                     AS  FIELD1
                                ,FIELD2                     AS  FIELD2
                                ,FIELD3                     AS  FIELD3
                                ,DRIVER_NO                  AS  DRIVER_NO
                                ,LGHT_MOV_DATE              AS  LGHT_MOV_DATE
                                ,BOE_NO                     AS  BOE_NO
                                ,AUDIT_REF_DATE             AS  AUDIT_REF_DATE
                                ,AUDIT_REF                  AS  AUDIT_REF
                                ,AUDIT_REF_DESC             AS  AUDIT_REF_DESC
                                ,AUDIT_REF_U_ID             AS  AUDIT_REF_U_ID
                                ,STK_PROCESSED              AS  STK_PROCESSED
                                ,PROCESSED                  AS  PROCESSED
                                ,LOAD_NO                    AS  LOAD_NO
                                ,ATTACH_CNT                 AS  ATTACH_CNT
                                ,CMP_NO                     AS  CMP_NO
                                ,BRN_NO                     AS  BRN_NO
                                ,BRN_YEAR                   AS  BRN_YEAR
                                ,BRN_USR                    AS  BRN_USR
                                ,AD_TRMNL_NM                AS  AD_TRMNL_NM
                                ,AD_U_ID                    AS  AD_U_ID
                                ,AD_DATE                    AS  AD_DATE
                                FROM IAS_WHTRNS_MST
                                 WHERE TR_SER=' || P_Doc_Ser || ' ';
      V_Qry_Dtl   := '  SELECT I_CODE                     AS  I_CODE
                                ,ITM_UNT                    AS  ITM_UNT
                                ,I_QTY                      AS  I_QTY
                                ,P_SIZE                     AS  P_SIZE
                                ,P_QTY                      AS  P_QTY
                                ,TR_QTY                     AS  TR_QTY
                                ,CC_CODE                    AS  CC_CODE
                                ,PJ_NO                      AS  PJ_NO
                                ,ACTV_NO                    AS  ACTV_NO
                                ,STK_COST                   AS  STK_COST
                                ,EXPIRE_DATE                AS  EXPIRE_DATE
                                ,BATCH_NO                   AS  BATCH_NO
                                ,EXP_AMT                    AS  EXP_AMT
                                ,RCRD_NO                    AS  RCRD_NO
                                ,DOC_SEQUENCE               AS  DOC_SEQUENCE
                                ,DOC_SEQUENCE_TR            AS  DOC_SEQUENCE_TR
                                ,BOE_NO                     AS  BOE_NO
                                ,USE_ATTCH                  AS  USE_ATTCH
                                ,REC_ATTCH                  AS  REC_ATTCH
                                ,I_PRICE                    AS  I_PRICE
                                ,ITEM_DESC                  AS  ITEM_DESC
                                ,BARCODE                    AS  BARCODE
                                ,DOC_TYPE_REF               AS  DOC_TYPE_REF
                                ,DOC_JV_TYPE_REF            AS  DOC_JV_TYPE_REF
                                ,DOC_NO_REF                 AS  DOC_NO_REF
                                ,DOC_SER_REF                AS  DOC_SER_REF
                                ,V_CODE                     AS  V_CODE
                                ,I_LENGTH                   AS  I_LENGTH
                                ,I_WIDTH                    AS  I_WIDTH
                                ,I_HEIGHT                   AS  I_HEIGHT
                                ,I_NUMBER                   AS  I_NUMBER
                                ,WT_QTY                     AS  WT_QTY
                                ,WT_UNT                     AS  WT_UNT
                                ,ARGMNT_NO                  AS  ARGMNT_NO
                                ,WEB_SRVC_TRNSFR_DATA_FLG   AS  WEB_SRVC_TRNSFR_DATA_FLG
                                ,WEB_SRVC_TRNSFR_DATA_DSC   AS  WEB_SRVC_TRNSFR_DATA_DSC
                                ,DOC_SEQUENCE_REF           AS  DOC_SEQUENCE_REF
                                ,TR_QTY_NOT_RECE            AS  TR_QTY_NOT_RECE
                                ,DOC_TYPE_REF_DTL           AS  DOC_TYPE_REF_DTL
                                ,DOC_NO_REF_DTL             AS  DOC_NO_REF_DTL
                                ,DOC_SER_REF_DTL            AS  DOC_SER_REF_DTL
                                ,DOC_SEQUENCE_REF_DTL       AS  DOC_SEQUENCE_REF_DTL
                                FROM IAS_WHTRNS_DTL
                                WHERE TR_SER=' || P_Doc_Ser || '  ';
   --##----------------------------------------------------------------------------##--
   Elsif P_Doc_Type IN(2,3) Then
      V_Qry_Mst   := 'Select  M.V_Ser Doc_Ser
                              ,M.Voucher_No Doc_No
                              ,M.Voucher_Type
                              ,Decode (M.Voucher_Type, 2, Ias_Gen_Pkg.Get_Prompt ( '||P_LNG_NO||', 2687), Ias_Gen_Pkg.Get_Prompt ( '||P_LNG_NO||', 2688)) Doc_Typ_Nm
                              ,M.Brn_No Brn_No
                              ,Ias_Brn_Pkg.Get_Br_Nm (M.Brn_No, '||P_LNG_NO||') Brn_Name
                              ,M.Voucher_Pay_Type
                              ,Decode (M.Voucher_Pay_Type, 1, Ias_Gen_Pkg.Get_Prompt ( '||P_LNG_NO||', 153), Ias_Gen_Pkg.Get_Prompt ( '||P_LNG_NO||', 11792) || '' - '' || Ys_Gen_Pkg.Get_Flg_Nm (''VCHR_BNK_TYP'', M.Transfer, '||P_LNG_NO||')) Pay_Type_Nm
                              ,M.Voucher_Date Doc_Date
                              ,M.A_Cy Cur_Code
                              , (Select Decode ( '||P_LNG_NO||', 1, Nvl (Cur_Name, Cur_E_Name), Nvl (Cur_E_Name, Cur_Name)) Cur_Name
                                   From Ex_Rate
                                  Where Cur_Code = M.A_Cy And Rownum <= 1) Cur_Name
                              ,M.Ref_No
                              ,M.Ref_Name
                              ,M.Ad_U_Id
                              ,M.Rep_Code
                              , (Select Decode ( '||P_LNG_NO||', 1, Nvl (Reprs_A_Name, Reprs_E_Name), Nvl (Reprs_E_Name, Reprs_A_Name)) Rep_Name
                                   From Sales_Man
                                  Where Reprs_Code = M.Rep_Code And Rownum <= 1)
                                  Rep_Name
                              ,M.Cash_No
                              ,(CASE WHEN M.voucher_pay_type=1 then
                                                    IAS_CSHBNK_PKG.Get_CB_Name(1,cash_no,'||P_LNG_NO||')
                                                   Else
                                               IAS_CSHBNK_PKG.Get_CB_Name(2,cash_no,'||P_LNG_NO||')
                                               END )Cash_BNK_Name
                              ,M.Ex_Rate Cur_Rate
                              ,M.A_Desc
                              ,M.Rec_Name
                              ,Decode (Nvl (Cash_Amtf, 0), 0, Cash_Amt, Cash_Amtf) Cashamt
                              ,Tafkeet(Decode (Nvl (Cash_Amtf, 0), 0, Cash_Amt, Cash_Amtf),M.A_Cy,'||P_LNG_NO||') READ_AMT
                          From Vouchers M  WHERE M.V_Ser=' || P_Doc_Ser || ' ';
      V_Qry_Dtl   := ' SELECT
                         D.V_Ser Doc_Ser
                        ,D.Voucher_No Doc_No
                        ,D.Ac_Code_Dtl
                        ,D.Ac_Dtl_Typ
                        ,Ys_Ac_Dtl_Pkg.Get_Ac_Dtl_Nm (D.Ac_Code_Dtl,D.A_Code,D.Ac_Dtl_Typ, '||P_LNG_NO||') Ac_Code_Dtl_Nm
                        ,D.A_Code
                        ,D.A_Cy CUR_CODE
                        ,Decode (Nvl (Ac_Amtf, 0), 0, Abs (Ac_Amt), Abs (Ac_Amtf)) Acamt
                        ,D.Ex_Rate CUR_Rate
                        ,Cheque_No
                        ,Value_Date
                        ,D.Ac_Desc
                        ,D.Cc_Code
                    From  Voucher_Detail D  WHERE D.V_Ser=' || P_Doc_Ser || ' ';
   End If;

  --##----------------------------------------------------------------------------##--
       Qry_Rslt:=Genrat_Data_File (P_Doc_Type          => P_Doc_Type
                                  ,P_Mst_Qry           =>V_Qry_Mst
                                  ,P_Dtl_Qry           =>V_Qry_Dtl
                                  ,P_Mst_Dtl_Flg       => 1
                                  ,P_Out_Data_Typ     =>P_Out_Data_Typ) ;

  --##----------------------------------------------------------------------------##--
   Return Qry_Rslt;
End Get_Doc_Data_Fnc;

--================================================================================-
Function Get_Doc_Mst_Rq (P_Sys_No          In Number Default Null
                        ,P_Doc_Type        In Number Default Null
                        ,P_Rep_Code        In Varchar2 Default Null
                        ,P_C_Code          In Varchar2 Default Null
                        ,P_Doc_Ser         In Ias_Bill_Mst.Bill_Ser%Type Default Null
                        ,P_Bill_Doc_Type   In Ias_Rt_Bill_Mst.Rt_Bill_Doc_Type%Type Default Null
                        ,P_Cur_Code        In Ias_Bill_Mst.Bill_Currency%Type Default Null
                        ,P_W_Code          In Ias_Rt_Bill_Mst.W_Code%Type Default Null
                        ,P_Doc_Date        In Ias_Rt_Bill_Mst.Rt_Bill_Date%Type Default Null
                        ,P_Brn_No          In S_brn.Brn_no%TYPE Default Null
                        ,P_RQ_STS          In Number Default 0 --## 0- all 1- approved 2- not approved 3- used 4- notused
                        ,P_EXP_STS         In Number Default 0 --## 0- All 1- Expire 2- Not Expire
                        ,P_F_Doc_No        In Quotation.Quot_No%Type       Default Null
                        ,P_T_Doc_No        In Quotation.Quot_No%Type       Default Null
                        ,P_F_Doc_Date      In Quotation.QUOT_DATE%Type     Default Null
                        ,P_T_Doc_Date      In Quotation.QUOT_DATE%Type     Default Null
                        ,P_F_C_Code        In Quotation.C_Code%Type        Default Null
                        ,P_T_C_Code        In Quotation.C_Code%Type        Default Null
                        ,P_Usr_No          In Number
                        ,P_Lng_No          In Number Default 1
                        ,P_Row_Cnt         In Number Default Null
                        ,P_Whr             In Varchar2 Default Null
                        ,P_Srch_Val        In Varchar2 Default Null
                        ,P_Out_Data_Typ    In Number Default 0  --## 0- xml # 1-query
                                                              )
   Return Clob
Is
   V_Yr                   Varchar2 (500);
   V_Cnt                  Number := 0;
   V_Lng_No               Number:=NVL(P_LNG_NO,1);
   V_Sql                  Varchar2 (8000);
   V_Whr                  Varchar2 (8000);
   V_Whr_Row              Varchar2 (8000);
   V_Price_Include_Vat    Number (1);
   V_Prv_Use_Vat          Number;
   V_Use_Vat              Number;
   V_Clc_Vat_Price_Typ    Number;
   V_Clc_Typ_No_Tax       Number;
   V_User_View_Doc_Entr   Number;
   Aralt                  Number (1);
   v_cc_avail             number(2);
   V_Ar_Cs_Type           number(2);
   V_P_Rate_Type          Number (5);
   V_Ar_Wc_Type           Number;
   V_Bill_Rate_Fld        Varchar2 (4000);
   V_Vat_Prd_Typ          Number (2);
   V_Curr_Yr              Number (5);
   V_Vat_Prd_Fld          Varchar2 (8000);
   V_Rt_Bill_Date         Date;
   V_Err_Line             Int := 0;
   V_Qry                  Clob;
   Qry_Rslt                  Clob;
   V_Doc_Date             Date;
   V_Msg_Txt              Varchar2 (1000);
   V_W_CODE_WHTRNS        Sales_order.W_code%Type;
   V_Rep_Code             Varchar2(200):=' M.Rep_Code ';
   V_Err_No               Number;
   -----------------------------------------------
   V_Json_Rslt            Varchar2 (4000) := '{"_Result": { "_ErrMsg": "@ERRMSG","_ErrNo": @ERRNO } }';
   FLD_DOC_NO                VARCHAR2(30);
   FLD_DOC_DATE              VARCHAR2(30);
   -----------------------------------------------
   V_F_Doc_No          Quotation.Quot_No%Type            :=P_F_Doc_No          ;
   V_T_Doc_No          Quotation.Quot_No%Type            :=P_T_Doc_No          ;
   V_F_Doc_Date        Quotation.QUOT_DATE%Type          :=P_F_Doc_Date        ;
   V_T_Doc_Date        Quotation.QUOT_DATE%Type          :=P_T_Doc_Date        ;
   V_F_C_Code          Quotation.C_Code%Type             :=P_F_C_Code          ;
   V_T_C_Code          Quotation.C_Code%Type             :=P_T_C_Code          ;
   -----------------------------------------------
Begin
   ---------------------------------------------------------------------
   V_Doc_Date := Nvl (P_Doc_Date, To_Date (To_Char (Sysdate, 'DD/MM/RRRR'), 'DD/MM/RRRR'));

   If P_Usr_No Is Null Then
      V_Err_No := 20001;
      V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => V_Lng_No, P_Msg_No => 450);
      Goto Rtn_Rslt;
   End If;

   If P_Doc_Type Is Null Then
      V_Err_No := $$plsql_Line;
      V_Msg_Txt := 'ENTER DOC_TYPE  ';
      Goto Rtn_Rslt;
   End If;

   If nvl(P_Doc_Type,0) Not In (53, 136, 52) Then
      V_Err_No := $$plsql_Line;
      V_Msg_Txt := ' Doc_Type =' || P_Doc_Type || ' Is Invalid  ';
      Goto Rtn_Rslt;
   End If;
    ---------------------------------------------------------------------
  IF P_DOC_TYPE =52 THEN
     FLD_DOC_NO            :='M.QUOT_NO';
     FLD_DOC_DATE          :='M.QUOT_DATE';
     ELSIF P_DOC_TYPE =53 THEN
     FLD_DOC_NO            :='M.ORDER_NO';
     FLD_DOC_DATE          :='M.ORDER_DATE';
   END IF;
   ---------------------------------------------------------------------
    If P_Sys_No = 70 And P_Rep_Code Is Null Then
       V_Err_No := $$plsql_Line;
      V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => V_Lng_No, P_Msg_No => 811);
      Goto Rtn_Rslt;
   End If;
   -----------------------------------------------
   Begin
      Select Nvl (User_View_Doc_Entr, 0)
        Into V_User_View_Doc_Entr
        From Privilege_Fixed
       Where U_Id = P_Usr_No;
   Exception
      When Others Then
         V_User_View_Doc_Entr := 0;
   End;

   Begin
      Select Nvl (Ar_Wc_Type, 1)
            ,Nvl (P_Rate_Type, 0)
            ,Nvl (Vat_Prd_Typ, 0)
            ,Nvl (Use_Vat, 0)
            ,nvl(AR_AC_LINK_TYPE,0)
            ,nvl(cc_avail,0)
            ,nvl(Ar_Cs_Type,0)
        Into V_Ar_Wc_Type
            ,V_P_Rate_Type
            ,V_Vat_Prd_Typ
            ,V_Use_Vat
            ,Aralt
            ,V_cc_avail
            ,V_Ar_Cs_Type
        From Ias_Para_Ar, Ias_Para_Gl, Ias_Para_Gen;
   Exception
      When Others Then
         V_Ar_Wc_Type := 1;
   End;
   ---------------------------------------------------------------------
   If P_Rep_Code Is Not Null Then
      V_Whr := V_Whr || '  and 1= (CASE WHEN M.Rep_code Is Not Null Then Nvl((Select 1
                                                                             From Sales_Man S
                                                                          where  Reprs_Code=M.Rep_code
                                                                                and rownum<=1
                                                                          Connect By Prior Reprs_Code = Rep_Code_Parent
                                                                           Start With Reprs_Code = ''' || P_Rep_Code || ''' ),0)
                                   Else 1 end)  ';

   End If;
  ---------------------------------------------------------------------
   If P_C_Code Is Not Null Then
      V_Whr := V_Whr || ' and M.c_code=''' || P_C_Code || ''' ';
   End If;
  ---------------------------------------------------------------------
   If P_W_Code Is Not Null And V_Ar_Wc_Type = 1 Then
      V_Whr := V_Whr || ' and M.w_code=' || P_W_Code || ' ';
   End If;
  ----------------------------------------------------
   If P_Brn_No Is Not Null Then
      V_Whr := V_Whr || ' and M.Brn_No=' || P_Brn_No || ' ';
   End If;
  ----------------------------------------------------
   If V_User_View_Doc_Entr = 1 Then
      V_Whr := V_Whr || 'And Exists (Select 1
                                    From Ias_Shw_Doc_Priv
                                   Where U_Id = ' || P_Usr_No || '
                                     And T_U_Id = M.Ad_U_Id
                                     And Nvl (Priv_Flag, 0) = 1
                                     And Rownum <= 1) ';
   End If;
  -----------------------------------------------------------------
   V_Whr := V_Whr || ' and Exists ( Select 1 From S_Brn_Usr_Priv
                        Where U_Id = ' || P_Usr_No || '
                          And S_Brn_Usr_Priv.Brn_No = M.Brn_No
                          And Nvl(Add_Flag,1)= 1
                          And RowNum <=1 )  ';


  ---------------------------------------------
  If Nvl(Aralt,0)=1 Then
    V_Whr := V_Whr || '  and 1= (CASE WHEN M.C_Code Is Not Null Then Nvl((Select 1
                                                                       From Priv_Acc P,Customer C
                                                                      Where P.A_Code = C.C_A_Code
                                                                        And C.C_Code = m.C_Code
                                                                        And P.U_Id   = '|| P_Usr_No ||'
                                                                        And P.A_Code = C.C_A_Code
                                                                        And Nvl(P.Add_Flag, 0) = 1
                                                                        And Rownum <= 1),0)
                                   Else 1 end)  ';
  Else
  V_Whr := V_Whr || '  and 1= (CASE WHEN M.C_Code Is Not Null Then (Select 1 From Ias_Priv_Customer
                                                                             Where U_Id='|| P_Usr_No || '
                                                                             And C_Code=M.C_Code
                                                                             And NVL(Add_Flag,0)=1
                                                                             And Rownum<=1)
                                   Else 1 end)  ';
  End If;
  ----------------------------------------------------
   If nvl(v_cc_avail,0)=3 And Nvl(V_Ar_Cs_Type,0)=1 Then
                                          V_Whr := V_Whr ||' AND EXISTS ( SELECT 1
                                                                                          FROM PRIVILEGE_CC
                                                                                         WHERE U_ID = '||P_Usr_No||'
                                                                                           AND PRIVILEGE_CC.Cc_CODE = M.CC_CODE
                                                                                           AND NVL (ADD_FLAG, 1) = 1
                                                                                           AND ROWNUM <= 1)';
   End If;
  ----------------------------------------------------
  If V_Ar_Wc_Type = 1 And P_Sys_No <> 70  Then
    V_Whr := V_Whr || 'AND EXISTS (SELECT 1
                                    FROM PRIVILEGE_WH
                                      WHERE U_ID = ' || P_Usr_No || '
                                          AND W_CODE = M.W_CODE
                                          And Nvl(Add_Flag,1)= 1
                                          AND ROWNUM <= 1 ) ';
  End If;

   ---------------------------------------------------------------------
   If Nvl (P_Row_Cnt, 0) > 0 Then
      V_Whr_Row := V_Whr_Row || ' AND ROW_NUM <=' || P_Row_Cnt || ' ';
   End If;

   ------------------------------------------------------------------
   If P_Srch_Val Is Not Null Then
      V_Whr_Row := V_Whr_Row || ' AND 1=(CASE WHEN TO_CHAR(DOC_SER) =  ''' || P_Srch_Val || '''   THEN 1
                                             WHEN CUR_CODE =  ''' || P_Srch_Val || '''   THEN 1
                                             WHEN TO_CHAR(DOC_NO) like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN C_Name  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN R_NAME  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN DOC_DESC  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN Typ_Nm  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN C_CODE  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN BILL_DOC_TYPE_NM  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN CASH_NAME  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN W_NAME  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN REP_NAME  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN BRN_NAME  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN PROCESED_NM  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN RSRVD  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN APPROVED_NM  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             WHEN STAND_BY_NM  like  ''' || '%' || P_Srch_Val || '%' || '''   THEN 1
                                             ELSE 0 END) ';
   End If;
      ---------------------------------------------------------------------
   ---------------------------------------------------------------------
      If  P_F_Doc_No Is Not  Null And P_T_Doc_No Is   Null Then
      V_T_Doc_No:=P_F_Doc_No;
      Elsif  P_F_Doc_No Is Null And P_T_Doc_No Is Not  Null Then
      V_F_Doc_No:=P_T_Doc_No;
      End If;

      If  V_F_Doc_No Is Not  Null And V_T_Doc_No Is Not   Null Then
      V_Whr:= V_Whr|| ' And '||Fld_Doc_No||' Between '||V_F_Doc_No || ' And  '||  V_T_Doc_No ;
      End  If;
-----------------------------------------------------------------------------------------
      If  P_F_C_Code Is Not  Null And P_T_C_Code Is   Null Then
      V_T_C_Code:=P_F_C_Code;
      Elsif  P_F_Doc_No Is Null And P_T_C_Code Is Not  Null Then
      V_F_C_Code:=P_T_C_Code;
      End If;

      If  V_F_C_Code Is Not  Null And V_T_C_Code Is Not   Null Then
      V_Whr:= V_Whr|| ' And M.C_CODE Between ''' ||V_F_C_Code ||''' And  '''||  V_T_C_Code ||''' ' ;
      End  If;
-----------------------------------------------------------------------------------------
      If  P_F_Doc_Date Is Not  Null And P_T_Doc_Date  Is Null Then
      V_T_Doc_Date:=P_F_Doc_Date;
      Elsif  P_F_Doc_Date Is Null And P_T_Doc_Date Is Not  Null Then
      V_F_Doc_Date:=P_T_Doc_Date;
      End If;

      If  V_F_Doc_Date Is Not  Null And V_T_Doc_Date Is Not   Null Then
      V_Whr:= V_Whr|| ' And '||Fld_Doc_Date||' Between ''' ||To_Char(V_F_Doc_Date,'DD/MM/YYYY') ||''' And  '''|| To_Char(V_T_Doc_Date,'DD/MM/YYYY') ||''' ' ;
      End  If;
   ---------------------------------------------------------------------
   ---------------------------------------------------------------------
   If P_Doc_Type = 136 Then
      If P_Doc_Ser Is Not Null Then
         V_Whr := V_Whr || ' AND Rt_Bill_SER =' || P_Doc_Ser || ' ';
      End If;

      If P_Cur_Code Is Not Null Then
         V_Whr := V_Whr || ' and rt_Bill_Currency=''' || P_Cur_Code || ''' ';
      End If;

      If P_Bill_Doc_Type Is Not Null Then
         V_Whr := V_Whr || ' and rt_BILL_DOC_TYPE=' || P_Bill_Doc_Type || ' ';
      End If;

      --##################################################################--
      V_Qry := '  ' || V_Whr_Row || ' ';
      --##################################################################--
   Elsif P_Doc_Type = 53 Then
      If P_Doc_Ser Is Not Null Then
         V_Whr := V_Whr || ' And M.Order_Ser =' || P_Doc_Ser || ' ';
      End If;

      If P_Cur_Code Is Not Null Then
         V_Whr := V_Whr || ' And M.Order_Cur=''' || P_Cur_Code || ''' ';
      End If;

      If P_Bill_Doc_Type Is Not Null Then
         V_Whr := V_Whr || ' And M.Bill_Doc_Type=' || P_Bill_Doc_Type || ' ';
      End If;

      If P_Doc_Date Is Not Null Then
         V_Whr := V_Whr || ' And To_Date(M.Order_Date,''DD/MM/RRRR'') =to_date('''|| P_Doc_Date ||''' ,''DD/MM/RRRR'')';
      End If;

      If nvl(P_RQ_STS,0)=0 Then
         null;
      elsIf nvl(P_RQ_STS,0)=1 Then
         V_Whr := V_Whr || ' and Nvl (m.Approved, 0)=1 ';
     elsIf nvl(P_RQ_STS,0)=2 Then
         V_Whr := V_Whr || ' and Nvl (m.Approved, 0)=0 ';
     elsIf nvl(P_RQ_STS,0)=3 Then
         V_Whr := V_Whr || ' and Nvl (m.PROCESED, 0)=1 ';
     elsIf nvl(P_RQ_STS,0)=4 Then
         V_Whr := V_Whr || ' and Nvl (m.PROCESED, 0)=0 ';
    end if;

    If Nvl(P_Exp_Sts,0)=0 Then
         Null;
    Elsif Nvl(P_Exp_Sts,0)=1 Then
         V_Whr := V_Whr || 'And M.Order_Expire_Date  <=To_Date(To_Char(Ias_Gen_Pkg.Get_Curdate ,''DD/MM/YYYY''),''DD/MM/YYYY'')';
    Elsif Nvl(P_Exp_Sts,0)=2 Then
         V_Whr := V_Whr || 'And (M.Order_Expire_Date >To_Date(To_Char(Ias_Gen_Pkg.Get_Curdate ,''DD/MM/YYYY''),''DD/MM/YYYY'') OR M.ORDER_EXPIRE_DATE IS NULL) ';
    End If;

    /*
    V_Whr := V_Whr || ' And 1 = (Case When M.Order_Expire_Date Is Null Then 1
                                 When M.Order_Expire_Date >= ''' || V_Doc_Date || '''  Then 1
                                 Else 0 End) ';
    */

    V_Whr := V_Whr || ' and  EXISTS (SELECT S_TYPE
                                               FROM IAS_PRIV_AR
                                              WHERE U_ID = '||p_usr_no||'
                                                AND NVL (VIEW_FLAG, 0) = 1
                                                AND IAS_PRIV_AR.S_TYPE = m.SO_TYPE
                                                AND IAS_PRIV_AR.AR_TYPE = 2
                                                AND ROWNUM <= 1) ';

      --------------------------------------------------
      V_Qry := 'Select *
                  From (Select Rownum Row_Num
                              ,M.Order_No Doc_No
                              ,M.Order_ser Doc_Ser
                              ,M.Order_date Doc_Date
                              ,M.Order_cur Cur_Code
                              ,(SELECT DECODE (  :P_LNG_NO , 1, NVL (CUR_NAME, CUR_E_NAME), NVL (CUR_E_NAME, CUR_NAME)) CUR_NAME
                                   FROM EX_RATE
                                  WHERE CUR_CODE = M.Order_cur AND ROWNUM <= 1)CUR_NAME
                              ,Null Cur_Rate
                              ,ROUND((NVL(ORDER_AMT,0)-NVL(DISC_AMT_MST,0)-NVL(DISC_AMT_DTL,0)+NVL(OTHR_AMT,0)+NVL(VAT_AMT,0)+NVL(VAT_AMT_OTHR,0)),2)  Doc_Amt
                              ,M.So_Type Typ_no
                              ,(SELECT DECODE (  :P_LNG_NO , 1, NVL (SO_A_NAME, SO_E_NAME), NVL (SO_E_NAME, SO_A_NAME)) CUR_NAME
                                   FROM IAS_SORDER_TYPES
                                  WHERE SO_TYPE = M.SO_TYPE AND ROWNUM <= 1)Typ_Nm
                              ,M.A_Desc Doc_Desc
                              ,M.C_Code
                              , (CASE
                                    WHEN M.C_CODE IS NOT NULL THEN
                                       (SELECT DECODE (  :P_LNG_NO , 1, NVL (C_A_NAME, C_E_NAME), NVL (C_E_NAME, C_A_NAME)) C_NAME
                                          FROM CUSTOMER
                                         WHERE C_CODE = M.C_CODE AND ROWNUM <= 1)
                                    ELSE
                                       M.C_NAME
                                 END) C_NAME
                              ,M.C_Tax_Code
                              ,M.C_ADDRESS
                              ,M.Bill_Doc_Type Bill_Doc_Type
                               , (SELECT FLG_DESC
                                   FROM S_FLAGS
                                  WHERE FLG_CODE = ''TYPE_NAME_SI''
                                  AND FLG_VALUE=M.BILL_DOC_TYPE
                                  AND LANG_NO= :P_LNG_NO
                                   AND ROWNUM <= 1)BILL_DOC_TYPE_NM
                              ,m.Cash_No
                              , (SELECT DECODE (  :P_LNG_NO , 1, NVL (CASH_NAME, CASH_E_NAME), NVL (CASH_E_NAME, CASH_NAME)) CASH_NAME
                                   FROM CASH_IN_HAND
                                  WHERE CASH_NO = M.CASH_NO AND ROWNUM <= 1) CASH_NAME
                              ,M.Cc_Code
                              ,(Select Decode (  :P_Lng_No , 1, Nvl (Cc_A_Name, Cc_E_Name), Nvl (Cc_E_Name, Cc_A_Name))Cc_Name
                                   From Cost_Centers
                                  Where Cc_Code = M.Cc_Code And Rownum <= 1) Cc_Name
                              ,M.Pj_No
                              ,(Select Decode (  :P_Lng_No , 1, Nvl (Pj_A_Name, Pj_E_Name), Nvl (Pj_E_Name, Pj_A_Name))Pj_Name
                                   From Ias_Projects
                                  Where Pj_No = M.Pj_No And Rownum <= 1) Pj_Name
                              ,M.Actv_No
                              ,(Select Decode (  :P_Lng_No , 1, Nvl (Actv_A_Name, Actv_E_Name), Nvl (Actv_E_Name, Actv_A_Name))Act_Name
                                   From IAS_ACTVTY
                                  Where Actv_No = M.Actv_No And Rownum <= 1) Actv_Name
                              ,M.W_Code
                              , (SELECT DECODE (  :P_LNG_NO , 1, NVL (W_NAME, W_E_NAME), NVL (W_E_NAME, W_NAME)) W_NAME
                                   FROM WAREHOUSE_DETAILS
                                  WHERE W_CODE = M.W_CODE AND ROWNUM <= 1) W_NAME
                              ,M.Rep_Code
                               , (SELECT DECODE (  :P_LNG_NO , 1, NVL (REPRS_A_NAME, REPRS_E_NAME), NVL (REPRS_E_NAME, REPRS_A_NAME)) REP_NAME
                                   FROM SALES_MAN
                                  WHERE REPRS_CODE = M.REP_CODE AND ROWNUM <= 1)  REP_NAME
                              ,M.R_Code
                               , (SELECT DECODE (  :P_LNG_NO , 1, NVL (R_A_NAME, R_E_NAME), NVL (R_E_NAME, R_A_NAME)) R_NAME
                                   FROM REGIONS
                                  WHERE r_code = M.R_CODE AND ROWNUM <= 1)  R_NAME
                              ,M.CR_CARD_NO
                             ,(Select Decode( :P_LNG_NO ,1,nvl(CR_CARD_NAME,CR_CARD_E_NAME),CR_CARD_E_NAME) CR_CARD_NAME
                                        from Credit_Card_Types
                                      Where Cr_Card_No=M.Cr_Card_No AND ROWNUM<=1)CR_CARD_NAME
                              ,M.Disc_Amt_Mst
                              ,M.Disc_Amt_Dtl
                              ,M.Disc_Amt_Mst_Vat
                              ,0 Add_Disc_Amt_Mst
                              ,M.Othr_Amt
                              ,M.VAT_AMT_OTHR
                              ,M.VAT_AMT
                              ,M.DISC_AMT
                              ,M.REF_DOC_NO REF_NO
                              ,M.Brn_No
                              ,(Select Decode( :P_LNG_NO ,1,nvl(BRN_LNAME,BRN_FNAME),NVL (BRN_FNAME, BRN_LNAME))
                                        from S_BRN
                                      Where BRN_NO=M.BRN_NO AND ROWNUM<=1)BRN_NAME
                              ,M.Clc_Typ_No_Tax
                              ,M.Clc_Vat_Price_Typ
                              ,m.SO_TYPE
                              ,NVL(M.PROCESED,0)PROCESED
                              ,DECODE (NVL(M.PROCESED,0),1, IAS_GEN_PKG.GET_PROMPT (:P_LNG_NO, 897), IAS_GEN_PKG.GET_PROMPT (:P_LNG_NO, 2313)) PROCESED_Nm
                              , DECODE (NVL ((SELECT 1
                                                 FROM ORDER_DETAIL
                                                WHERE ORDER_SER = M.ORDER_SER
                                                  AND NVL (RESERVED, 0) = 1
                                                  AND ROWNUM <= 1),
                                              0
                                             ),
                                         1, IAS_GEN_PKG.GET_PROMPT (:P_LNG_NO, 6778),
                                         IAS_GEN_PKG.GET_PROMPT (:P_LNG_NO, 724)
                                        ) RSRVD
                              ,Nvl (m.Approved, 0) Approved
                           , ( SELECT  FLG_DESC FROM  S_FLAGS
                                   WHERE S_FLAGS.FLG_CODE=''APPROVED''
                                         AND S_FLAGS.FLG_VALUE=M.APPROVED
                                         AND S_FLAGS.LANG_NO=:P_LNG_NO
                                          AND ROWNUM<=1 )  Approved_Nm
                              ,nvl(m.Stand_By,0) Stand_By
                           ,DECODE (NVL(M.Stand_By,0),1, IAS_GEN_PKG.GET_PROMPT (:P_LNG_NO, 1948), IAS_GEN_PKG.GET_PROMPT (:P_LNG_NO, 986)) Stand_By_Nm
                           ,To_Date(M.Order_Expire_Date,''DD/MM/YYYY'') Doc_Expire_Date
                           ,M.C_Mobile
                           ,M.Ad_U_Id
                           ,(Select Decode (  :P_Lng_No , 1, Nvl (U_A_Name, U_E_Name), Nvl (U_A_Name, U_E_Name))Ad_Name
                                   From User_R
                                  Where Ad_U_Id = M.Ad_U_Id And Rownum <= 1) Ad_Name
                           ,M.COL_NO
                           ,M.EMP_NO
                           ,M.PRM_CODE
                           ,M.DRIVER_NO
                          From sales_Order M
                         Where  1=1
                         ' || V_Whr || '
                    Order By m.order_Date Desc
                             ,m.order_No Desc
                            ,m.bill_Doc_Type
                            ,m.so_type )
                            WHERE 1=1
                            '||P_Whr||' ' || V_Whr_Row || ' ';
 Elsif P_Doc_Type = 52 Then
      If P_Doc_Ser Is Not Null Then
         V_Whr := V_Whr || ' And M.Quot_Ser =' || P_Doc_Ser || ' ';
      End If;

      If P_Cur_Code Is Not Null Then
         V_Whr := V_Whr || ' And M.Quot_Cur=''' || P_Cur_Code || ''' ';
      End If;

      If P_Bill_Doc_Type Is Not Null Then
         V_Whr := V_Whr || ' And M.Quot_Doc_Type=' || P_Bill_Doc_Type || ' ';
      End If;

      If P_Doc_Date Is Not Null Then
         V_Whr := V_Whr || ' and to_date(m.Quot_DATE,''DD/MM/RRRR'') =to_date('''|| P_Doc_Date ||''' ,''DD/MM/RRRR'')';
      End If;

      If nvl(P_RQ_STS,0)=0 Then
         null;
      elsIf nvl(P_RQ_STS,0)=1 Then
         V_Whr := V_Whr || ' and Nvl (M.Approved, 0)=1 ';
     elsIf nvl(P_RQ_STS,0)=2 Then
         V_Whr := V_Whr || ' And Nvl (M.Approved, 0)=0 ';
     elsIf nvl(P_RQ_STS,0)=3 Then
         V_Whr := V_Whr || ' and Nvl (M.PROCESSED, 0)=1 ';
     elsIf nvl(P_RQ_STS,0)=4 Then
         V_Whr := V_Whr || ' and Nvl (M.PROCESSED, 0)=0 ';
    end if;

    If Nvl(P_Exp_Sts,0)=0 Then
         Null;
    Elsif Nvl(P_Exp_Sts,0)=1 Then
         V_Whr := V_Whr || 'And M.Quot_Expire_Date  <=To_Date(To_Char(Ias_Gen_Pkg.Get_Curdate ,''DD/MM/YYYY''),''DD/MM/YYYY'')';
    Elsif Nvl(P_Exp_Sts,0)=2 Then
         V_Whr := V_Whr || 'And (M.Quot_Expire_Date >To_Date(To_Char(Ias_Gen_Pkg.Get_Curdate ,''DD/MM/YYYY''),''DD/MM/YYYY'') OR M.Quot_Expire_Date IS NULL) ';
    End If;

    /*
    V_Whr := V_Whr || ' And 1 = (Case When M.Quot_Expire_Date Is Null Then 1
                                 When M.Quot_Expire_Date >= ''' || V_Doc_Date || '''  Then 1
                                 Else 0 End) ';
     */
    V_Whr := V_Whr || ' and  EXISTS (SELECT S_TYPE
                                               FROM IAS_PRIV_AR
                                              WHERE U_ID = '||p_usr_no||'
                                                AND NVL (VIEW_FLAG, 0) = 1
                                                AND IAS_PRIV_AR.S_TYPE = M.Qt_Type
                                                AND IAS_PRIV_AR.AR_TYPE = 1
                                                AND ROWNUM <= 1) ';

      --------------------------------------------------
      V_Qry := 'Select *
                  From (Select Rownum Row_Num
                              ,M.Quot_No Doc_No
                              ,M.Quot_ser Doc_Ser
                              ,M.Quot_date Doc_Date
                              ,M.Quot_cur Cur_Code
                              ,(SELECT DECODE (  :P_LNG_NO , 1, NVL (CUR_NAME, CUR_E_NAME), NVL (CUR_E_NAME, CUR_NAME)) CUR_NAME
                                   FROM EX_RATE
                                  WHERE CUR_CODE = M.Quot_cur AND ROWNUM <= 1)CUR_NAME
                              ,Null Cur_Rate
                              ,ROUND((NVL(Quot_AMT,0)-NVL(DISC_AMT_MST,0)-NVL(DISC_AMT_DTL,0)+NVL(OTHR_AMT,0)+NVL(VAT_AMT,0)+NVL(VAT_AMT_OTHR,0)),2)  Doc_Amt
                              ,M.Si_type Typ_no
                              ,(SELECT DECODE (  :P_LNG_NO , 1, NVL (QT_A_Name, QT_E_Name), NVL (QT_A_Name, QT_E_Name)) CUR_NAME
                                   FROM Ias_Quot_Types
                                  WHERE QT_TYPE = M.SI_TYPE AND ROWNUM <= 1)Typ_Nm
                              ,M.A_Desc Doc_Desc
                              ,M.C_Code
                              , (CASE
                                    WHEN M.C_CODE IS NOT NULL THEN
                                       (SELECT DECODE (  :P_LNG_NO , 1, NVL (C_A_NAME, C_E_NAME), NVL (C_E_NAME, C_A_NAME)) C_NAME
                                          FROM CUSTOMER
                                         WHERE C_CODE = M.C_CODE AND ROWNUM <= 1)
                                    ELSE
                                       M.C_NAME
                                 END) C_NAME
                              ,C.C_Tax_Code
                              ,C.C_ADDRESS
                              ,M.Quot_Doc_Type Bill_Doc_Type
                               , (SELECT FLG_DESC
                                   FROM S_FLAGS
                                  WHERE FLG_CODE = ''TYPE_NAME_SI''
                                  AND FLG_VALUE=M.Quot_Doc_Type
                                  AND LANG_NO= :P_LNG_NO
                                   AND ROWNUM <= 1)BILL_DOC_TYPE_NM
                              ,null Cash_No
                              , Null  CASH_NAME
                              ,M.Cc_Code
                              ,(Select Decode (  :P_Lng_No , 1, Nvl (Cc_A_Name, Cc_E_Name), Nvl (Cc_E_Name, Cc_A_Name))Cc_Name
                                   From Cost_Centers
                                  Where Cc_Code = M.Cc_Code And Rownum <= 1) Cc_Name
                              ,M.Pj_No
                              ,(Select Decode (  :P_Lng_No , 1, Nvl (Pj_A_Name, Pj_E_Name), Nvl (Pj_E_Name, Pj_A_Name))Pj_Name
                                   From Ias_Projects
                                  Where Pj_No = M.Pj_No And Rownum <= 1) Pj_Name
                              ,M.Actv_No
                              ,(Select Decode (  :P_Lng_No , 1, Nvl (Actv_A_Name, Actv_E_Name), Nvl (Actv_E_Name, Actv_A_Name))Act_Name
                                   From IAS_ACTVTY
                                  Where Actv_No = M.Actv_No And Rownum <= 1) Actv_Name
                              ,M.W_Code
                              , (SELECT DECODE (  :P_LNG_NO , 1, NVL (W_NAME, W_E_NAME), NVL (W_E_NAME, W_NAME)) W_NAME
                                   FROM WAREHOUSE_DETAILS
                                  WHERE W_CODE = M.W_CODE AND ROWNUM <= 1) W_NAME
                              ,M.Rep_Code
                               , (SELECT DECODE (  :P_LNG_NO , 1, NVL (REPRS_A_NAME, REPRS_E_NAME), NVL (REPRS_E_NAME, REPRS_A_NAME)) REP_NAME
                                   FROM SALES_MAN
                                  WHERE REPRS_CODE = M.REP_CODE AND ROWNUM <= 1)  REP_NAME
                              , NULL R_Code
                               , Null  R_NAME
                              ,Null CR_CARD_NO
                             ,Null CR_CARD_NAME
                              ,M.Disc_Amt_Mst
                              ,M.Disc_Amt_Dtl
                              ,M.Disc_Amt_Mst_Vat
                              ,0 Add_Disc_Amt_Mst
                              ,M.Othr_Amt
                              ,M.VAT_AMT_OTHR
                              ,M.VAT_AMT
                              ,M.DISC_AMT
                              ,M.REF_NO REF_NO
                              ,M.Brn_No
                              ,(Select Decode( :P_LNG_NO ,1,nvl(BRN_LNAME,BRN_FNAME),NVL (BRN_FNAME, BRN_LNAME))
                                        from S_BRN
                                      Where BRN_NO=M.BRN_NO AND ROWNUM<=1)BRN_NAME
                              ,M.Clc_Typ_No_Tax
                              ,M.Clc_Vat_Price_Typ
                              ,m.Si_type
                              ,m.Qt_type
                              ,NVL(M.PROCESSED,0)PROCESSED
                              ,DECODE (NVL(M.PROCESSED,0),1, IAS_GEN_PKG.GET_PROMPT (:P_LNG_NO, 897), IAS_GEN_PKG.GET_PROMPT (:P_LNG_NO, 2313)) PROCESED_NM
                              , 0  RSRVD
                              ,Nvl (m.Approved, 0) Approved
                           , ( SELECT  FLG_DESC FROM  S_FLAGS
                                   WHERE S_FLAGS.FLG_CODE=''APPROVED''
                                         AND S_FLAGS.FLG_VALUE=M.APPROVED
                                         AND S_FLAGS.LANG_NO=:P_LNG_NO
                                          AND ROWNUM<=1 )  Approved_Nm
                              ,0  Stand_By
                           ,Null Stand_By_Nm
                           ,To_Date(M.Quot_Expire_Date,''DD/MM/YYYY'') Doc_Expire_Date
                           ,C.C_Mobile
                           ,M.Ad_U_Id
                           ,(Select Decode (  :P_Lng_No , 1, Nvl (U_A_Name, U_E_Name), Nvl (U_A_Name, U_E_Name))Ad_Name
                                   From User_R
                                  Where Ad_U_Id = M.Ad_U_Id And Rownum <= 1) Ad_Name
                           ,NULL COL_NO
                           ,NULL EMP_NO
                           ,NULL PRM_CODE
                           ,M.DRIVER_NO
                          From QUOTATION M ,CUSTOMER C
                         Where
                          M.C_CODE=C.C_CODE(+)
                         ' || V_Whr || '
                    Order  By m.Quot_Date Desc
                             ,m.Quot_No Desc
                             ,m.Quot_Doc_Type
                             ,m.Qt_type )
                            WHERE 1=1
                           '||P_Whr||' ' || V_Whr_Row || ' ';

   End If;

   V_Qry:=Replace(upper(V_Qry),':P_LNG_NO',P_LNG_NO);
   Begin
       Qry_Rslt:=Genrat_Data_File (P_Doc_Type          => Null
                                  ,P_Mst_Qry           =>V_Qry
                                  ,P_Dtl_Qry           =>Null
                                  ,P_Mst_Dtl_Flg       => 0
                                  ,P_Out_Data_Typ      =>P_Out_Data_Typ) ;
     -- Genrat_Data_File (P_Qry => V_Qry, P_Out_Data_Typ => P_Out_Data_Typ);
   Exception
      When Others Then
         V_Err_No := 20006;
         V_Msg_Txt := ' Error In Ars_Api_Fetch_Data_Pkg.Get_Doc_Mst_Rq '|| Sqlerrm;
         Goto Rtn_Rslt;
   End;

   Return Qry_Rslt;

  --####################--
  <<RTN_RSLT>>
   If V_Msg_Txt Is Not Null Then
      V_Json_Rslt := Replace (V_Json_Rslt, '@ERRNO', V_Err_No);
      V_Json_Rslt := Replace( V_Json_Rslt, '@ERRMSG',Replace( V_Msg_Txt,'"',' '));
      Return V_Json_Rslt;
   End If;
--####################--
Exception
   When Others Then
      Raise_Application_Error (-20003, ' Error In Get_Doc_Mst_Rq ' || Sqlerrm);
End Get_Doc_Mst_Rq;
 ---___________________________________________________________________________________________________________________________________-----
 Function Get_Doc_Dtl_Rq (P_Doc_Type       In Number Default Null
                        ,P_Doc_Ser        In Ias_Rt_Bill_Mst.Rt_Bill_Ser%Type Default Null
                        ,P_Usr_No         In Number
                        ,P_Lng_No         In Number Default 1
                        ,P_Out_Data_Typ   In Number Default 0   --## 0- xml # 1-query
                                                             )
   Return Clob
Is
   V_Yr          Varchar2 (500);
   V_Cnt         Number := 0;
   V_Lng_No      Number;
   V_Qry         Clob;
   Qry_Rslt         Clob;
   V_Msg_Txt     Varchar2 (1000);
   V_Err_No      Number;
   V_Json_Rslt   Varchar2 (4000) := '{"_Result": { "_ErrMsg": "@ERRMSG","_ErrNo": @ERRNO } }';
Begin
   V_Lng_No := Nvl (P_Lng_No, 1);

   If P_Usr_No Is Null Then
      V_Err_No := 20005;
      V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => V_Lng_No, P_Msg_No => 450);
      Goto Rtn_Rslt;
   End If;

   If P_Doc_Ser Is Null Then
      V_Err_No := $$plsql_Line;
      V_Msg_Txt := 'ENTER DOC_SER  ';
      Goto Rtn_Rslt;
   End If;

   If P_Doc_Type Is Null Then
      V_Err_No := $$plsql_Line;
      V_Msg_Txt := 'ENTER DOC_TYPE  ';
      Goto Rtn_Rslt;
   End If;

   If P_Doc_Type Not In (53, 136, 52) Then
      V_Err_No := $$plsql_Line;
      V_Msg_Txt := ' Doc_Type =' || P_Doc_Type || ' Is Invalid  ';
      Goto Rtn_Rslt;
   End If;

   If P_Doc_Type = 136 Then
      V_Qry := ' ';
   Elsif P_Doc_Type = 53 Then
      V_Qry := ' Select M.* From (
                    Select D.order_no Doc_No
                          ,D.order_ser Doc_Ser
                          ,D.I_Code
                          ,DECODE ( '||P_LNG_NO||' , 1, NVL (i.I_NAME, i.I_E_NAME), NVL (i.I_E_NAME, i.I_NAME)) I_NAME
                          ,D.Itm_Unt
                          ,Nvl(D.P_Size,1) P_Size
                          ,D.W_Code
                          ,D.Cc_Code
                          ,D.Pj_No
                          ,D.ACTV_NO
                          ,D.I_QTY
                          ,d.Free_Qty
                          ,D.I_Price_Vat
                          ,D.I_Price
                          ,Decode (D.Expire_Date, ''01/01/1900'', Null, D.Expire_Date) Expire_Date
                          ,Decode (D.Batch_No, ''0'', Null, D.Batch_No) Batch_No
                          ,D.Rcrd_No
                          ,Nvl (D.Vat_Per, 0) Vat_Per
                          ,Nvl (D.Vat_Amt, 0) Vat_Amt
                          ,Nvl (D.Dis_Per, 0) Dis_Per
                          ,Nvl (D.Dis_Amt, 0) Dis_Amt
                          ,Nvl (D.Dis_Amt_Mst, 0) Dis_Amt_Mst
                          ,Nvl (i.SERVICE_ITM, 0) Service_Item
                          ,D.Barcode
                          ,D.Dis_Amt_Dtl
                          ,D.Dis_Amt_Dtl2
                          ,D.Dis_Amt_Dtl3
                          ,0 Add_Dis_Amt_Mst
                          ,0 Add_Dis_Amt_Dtl
                          ,Nvl (M.Clc_Vat_Price_Typ, 1) Clc_Vat_Price_Typ
                          ,d.doc_seq Doc_Sequence
                          ,nvl(D.Othr_Amt_Disc,0) Othr_Amt_Disc
                          ,nvl(D.Othr_Amt,0) Othr_Amt
                          ,0  Has_Qt_Prm
                          ,Nvl (I.Use_Serialno, 0) Use_Serialno
                          ,D.Dis_Amt_Mst_Vat
                          ,D.Dis_Amt_Dtl_Vat
                          ,D.Dis_Amt_Dtl2_Vat
                          ,D.Dis_Amt_Dtl3_Vat
                          ,null Add_Disc_Amt_Dtl_Yr
                          ,53 Doc_Type_Ref
                          ,D.order_no      Doc_No_Ref
                          ,D.order_ser     Doc_Ser_Ref
                          ,D.Rcrd_No         Rcrd_No_Ref
                          ,M.So_Type Si_Type
                          ,m.BILL_DOC_TYPE Bill_Doc_Type
                          ,nvl(I.USE_BATCH_NO,0) USE_BATCH_NO
                          ,nvl(I.USE_EXP_DATE,0) USE_EXP_DATE
                          ,I.RETURN_PERIOD
                          ,D.lev_no
                          ,D.QT_PRM_SER
                          ,D.QT_PRM_RCRD_NO
                          ,D.QT_PRM_NO
                          ,TO_CHAR(Q.T_DATE,''MM/DD/YYYY'')  PRM_EXPIRE_DATE
                          ,Nvl(I.Use_Weight,0)Use_Weight
                          ,D.WT_UNT
                          ,D.ARGMNT_NO
                          ,I.Wt_Sys_Rnd_Typ
                          ,D.WT_QTY
                          ,D.I_NUMBER
                          ,D.I_LENGTH
                          ,D.I_HEIGHT
                          ,D.I_WIDTH
                          ,D.MEASUR_PRICE
                       From sales_order m ,order_detail D, Ias_Itm_Mst I ,IAS_QUT_PRM_MST  Q
                               Where M.order_ser=D.order_ser
                               And D.I_Code = I.I_Code
                                AND D.QT_PRM_SER=Q.QUOT_SER(+)
                                And m.order_ser ='|| P_Doc_Ser ||'
                                ) M
                             Order By Rcrd_No';
    Elsif P_Doc_Type = 52 Then
     V_Qry := 'Select M.* From (
                    Select D.Quot_no Doc_No
                          ,D.Quot_ser Doc_Ser
                          ,D.I_Code
                          ,DECODE ( '||P_LNG_NO||' , 1, NVL (i.I_NAME, i.I_E_NAME), NVL (i.I_E_NAME, i.I_NAME)) I_NAME
                          ,D.Itm_Unt
                          ,Nvl(D.P_Size,1) P_Size
                          ,D.W_Code
                          ,D.Cc_Code
                          ,D.Pj_No
                          ,D.ACTV_NO
                          ,D.I_QTY
                          ,d.Free_Qty
                          ,D.I_Price_Vat
                          ,D.I_Price
                          ,Decode (D.Expire_Date, ''01/01/1900'', Null, D.Expire_Date) Expire_Date
                          ,Decode (D.Batch_No, ''0'', Null, D.Batch_No) Batch_No
                          ,D.Rcrd_No
                          ,Nvl (D.Vat_Per, 0) Vat_Per
                          ,Nvl (D.Vat_Amt, 0) Vat_Amt
                          ,Nvl (D.Dis_Per, 0) Dis_Per
                          ,Nvl (D.Dis_Amt, 0) Dis_Amt
                          ,Nvl (D.Dis_Amt_Mst, 0) Dis_Amt_Mst
                          ,Nvl (i.SERVICE_ITM, 0) Service_Item
                          ,D.Barcode
                          ,D.Dis_Amt_Dtl
                          ,D.Dis_Amt_Dtl2
                          ,D.Dis_Amt_Dtl3
                          ,0 Add_Dis_Amt_Mst
                          ,0 Add_Dis_Amt_Dtl
                          ,Nvl (M.Clc_Vat_Price_Typ, 1) Clc_Vat_Price_Typ
                          ,d.doc_seq Doc_Sequence
                          ,nvl(D.Othr_Amt_Disc,0) Othr_Amt_Disc
                          ,nvl(D.Othr_Amt,0) Othr_Amt
                          ,0  Has_Qt_Prm
                          ,Nvl (I.Use_Serialno, 0) Use_Serialno
                          ,D.Dis_Amt_Mst_Vat
                          ,D.Dis_Amt_Dtl_Vat
                          ,D.Dis_Amt_Dtl2_Vat
                          ,D.Dis_Amt_Dtl3_Vat
                          ,null Add_Disc_Amt_Dtl_Yr
                          ,52 Doc_Type_Ref
                          ,D.Quot_no      Doc_No_Ref
                          ,D.Quot_ser     Doc_Ser_Ref
                          ,D.Rcrd_No         Rcrd_No_Ref
                          ,M.Si_Type Si_Type
                          ,m.Quot_DOC_TYPE Bill_Doc_Type
                          ,nvl(I.USE_BATCH_NO,0) USE_BATCH_NO
                          ,nvl(I.USE_EXP_DATE,0) USE_EXP_DATE
                          ,I.RETURN_PERIOD
                          ,D.lev_no
                          ,D.QT_PRM_SER
                          ,D.QT_PRM_RCRD_NO
                          ,D.QT_PRM_NO
                          ,TO_CHAR(Q.T_DATE,''MM/DD/YYYY'')  PRM_EXPIRE_DATE
                          ,Nvl(I.Use_Weight,0)Use_Weight
                          ,D.WT_UNT
                          ,D.ARGMNT_NO
                          ,I.Wt_Sys_Rnd_Typ
                          ,D.WT_QTY
                          ,D.I_NUMBER
                          ,D.I_LENGTH
                          ,D.I_HEIGHT
                          ,D.I_WIDTH
                          ,D.MEASUR_PRICE
                       From Quotation m,Quotation_Detail D, Ias_Itm_Mst I ,Ias_Qut_Prm_Mst  Q
                               Where M.Quot_ser=D.Quot_ser
                               And D.I_Code = I.I_Code
                                AND D.QT_PRM_SER=Q.QUOT_SER(+)
                               And m.Quot_ser =' || P_Doc_Ser || '
                                ) M
                             Order By Rcrd_No ';
   End If;

   Begin
       Qry_Rslt:=Genrat_Data_File (P_Doc_Type          => Null
                                  ,P_Mst_Qry           =>V_Qry
                                  ,P_Dtl_Qry           =>Null
                                  ,P_Mst_Dtl_Flg       => 0
                                  ,P_Out_Data_Typ      =>P_Out_Data_Typ) ;
     -- Genrat_Data_File (P_Qry => V_Qry, P_Out_Data_Typ => P_Out_Data_Typ);
   Exception
      When Others Then
         V_Err_No := 20006;
         V_Msg_Txt := ' Error In Ars_Api_Fetch_Data_Pkg.Get_Doc_Mst_Rq '|| Sqlerrm;
         Goto Rtn_Rslt;
   End;

   Begin
      Qry_Rslt:=Genrat_Data_File (P_Doc_Type          => Null
                                  ,P_Mst_Qry           =>V_Qry
                                  ,P_Dtl_Qry           =>Null
                                  ,P_Mst_Dtl_Flg       => 0
                                  ,P_Out_Data_Typ      =>P_Out_Data_Typ) ;
   Exception
      When Others Then
         V_Err_No := 20006;
         V_Msg_Txt := ' Error In Ars_Api_Fetch_Data_Pkg.Get_Doc_Dtl_Rq '|| Sqlerrm;
         Goto Rtn_Rslt;
   End;

   Return Qry_Rslt;

  --####################--
  <<RTN_RSLT>>
   If V_Msg_Txt Is Not Null Then
      V_Json_Rslt := Replace (V_Json_Rslt, '@ERRNO', V_Err_No);
       V_Json_Rslt := Replace( V_Json_Rslt, '@ERRMSG',Replace( V_Msg_Txt,'"',' '));
      Return V_Json_Rslt;
   End If;
--####################--
Exception
   When Others Then
      Raise_Application_Error (-20003, ' Error In Ars_Api_Fetch_Data_Pkg.Get_Doc_Dtl_Rq ' || Sqlerrm);
End Get_Doc_Dtl_Rq;
---##--------------------------------------------------------------------------------------------------##---
Function Genrat_Data_File (P_Doc_Type           In Ias_Post_Mst.Doc_Type%Type Default Null
                          ,P_Mst_Qry            In clob Default Null
                          ,P_Dtl_Qry            In clob Default Null
                          ,P_Mst_Dtl_Flg        In Number Default 0
                          ,P_Out_Data_Typ       In Number Default 0--## 0- xml # 1-query
                           ) Return Clob Is
   V_Cnt        Number;
   V_Xml_Txt    Clob;
   V_Xml_Typ    Xmltype;
   V_Lng_No     Number;
   V_Doc_Ser    Varchar2 (500);
   V_Json_Rslt  Varchar2 (500):=  '{"_Result": { "_ErrMsg": "@ERRMSG","_ErrNo": @ERRNO } }';
   V_Tag_Mst    Varchar2 (500) := 'DOC_MST';
   V_Tag_Dtl    Varchar2 (500) := 'DOC_DTL';
   V_Tag        Varchar2 (500) := 'DOC';
   V_Msg_Txt    Varchar2 (4000);
   V_Pkg_Line   Varchar2 (4000);
   Qry_Ctx      Dbms_Xmlgen.Ctxhandle;
   V_Xml_Mst    Clob;
   V_Xml_Dtl    Clob;
   V_Xml        Clob;
   Qry_Rslt                Clob;
Begin
   If Nvl (P_Out_Data_Typ, 0) = 0 Then
      --##----------------------------------------------------------------------------##--
      If Nvl (P_Mst_Dtl_Flg, 0) = 0 Then
         Begin
            Qry_Ctx    := Dbms_Xmlgen.Newcontext (P_Mst_Qry);
            Dbms_Xmlgen.Setnullhandling (Qry_Ctx, Dbms_Xmlgen.Empty_Tag);
            Qry_Rslt   := Dbms_Xmlgen.Getxml (Qry_Ctx);
         Exception
            When No_Data_Found Then
               Null;
            When Others Then
               Raise_Application_Error (-20002, 'Error  When Genert Xml File ' || Sqlerrm);
         End;
      Else
         ----------------------------------------------------------------
         Begin
            Qry_Ctx     := Dbms_Xmlgen.Newcontext (P_Mst_Qry);
            Dbms_Xmlgen.Setrowtag (Qry_Ctx, V_Tag_Mst);
            Dbms_Xmlgen.Setnullhandling (Qry_Ctx, Dbms_Xmlgen.Empty_Tag);
            V_Xml_Mst   := Dbms_Xmlgen.Getxml (Qry_Ctx);
         Exception
            When Others Then
               Raise_Application_Error (-20904, ' ERROR WHEN GENERAT ' || V_Tag_Mst || ' ' || Chr (10) || Sqlerrm);
         End;

         Begin
            Qry_Ctx     := Dbms_Xmlgen.Newcontext (P_Dtl_Qry);
            Dbms_Xmlgen.Setrowtag (Qry_Ctx, V_Tag_Dtl);
            Dbms_Xmlgen.Setnullhandling (Qry_Ctx, Dbms_Xmlgen.Empty_Tag);
            V_Xml_Dtl   := Dbms_Xmlgen.Getxml (Qry_Ctx);
         Exception
            When Others Then
               Raise_Application_Error (-20904, ' ERROR WHEN GENERAT ' || V_Tag_Dtl || ' ' || Chr (10) || Sqlerrm);
         End;

         V_Xml_Mst   := Substr (V_Xml_Mst, Instr (V_Xml_Mst, '<' || V_Tag_Mst || '>'));
         V_Xml_Mst   := Substr (V_Xml_Mst, 1, Instr (V_Xml_Mst, '</ROWSET>') - 1);
         V_Xml_Dtl   := Substr (V_Xml_Dtl, Instr (V_Xml_Dtl, '<' || V_Tag_Dtl || '>'));
         V_Xml_Dtl   := Substr (V_Xml_Dtl, 1, Instr (V_Xml_Dtl, '</ROWSET>') - 1);
         Qry_Rslt    := '<' || V_Tag || '>' || V_Xml_Mst || V_Xml_Dtl || '</' || V_Tag || '>';
      ----------------------------------------------------------------
      End If;
   --##----------------------------------------------------------------------------##--
   Elsif Nvl (P_Out_Data_Typ, 0) = 1 Then
      Qry_Rslt   := P_Mst_Qry||chr(13)||chr(13)||P_Dtl_Qry;
   End If;

   Return Qry_Rslt;
End Genrat_Data_File;
--=======================================================================================================
 Function GET_Cst_Plan_TRGT(P_Typ       In Number   Default 1 ,   -- 1-  Summary , 2-Details     P_F_C_Code    In Varchar2 Default Null,
                            P_F_C_Code    In Varchar2 Default Null,
                            P_T_C_Code    In Varchar2 Default Null,
                            P_F_C_CLASS       IN     CUSTOMER.C_CLASS%TYPE      Default Null,
                            P_T_C_CLASS       IN     CUSTOMER.C_CLASS%TYPE      Default Null,
                            P_F_Date    In Date     Default Null,
                            P_T_Date    In Date     Default Null,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      --## 1-DETAIL 2- SUM
                            P_Lng_No    In Number   Default 1)
   Return Clob
Is
   Pragma Autonomous_Transaction;
   V_Sql_Qry               Clob;
   V_Whr                   Varchar2(2000):=' ';
   V_Whr_Itm               Varchar2(2000):=' ';
   V_Xml_Typ               Xmltype;
   V_Json_Rslt             Varchar2(4000);
   Qry_Ctx                 Dbms_Xmlgen.Ctxhandle;
   Qry_Rslt                Clob;
   V_F_Date                Date:=P_F_Date;
   V_T_Date                Date:=P_T_Date;
   V_CNT                   NUMBER;
   V_F_C_Code              Varchar2 (500);
   V_T_C_Code              Varchar2 (500);
   V_F_C_CLASS              CUSTOMER.C_CLASS%TYPE:=P_F_C_CLASS;
   V_T_C_CLASS              CUSTOMER.C_CLASS%TYPE:=P_T_C_CLASS;
Begin

   Begin
      Execute Immediate 'ALTER SESSION SET NLS_DATE_FORMAT=''DD/MM/YYYY''';
   End;
   --##-----------------------------------------------------------------------------##--
   V_F_C_Code :=     P_F_C_Code;
   V_T_C_Code :=     P_T_C_Code;
   ------------------------------------------
   --## C_CODE
   If V_F_C_Code Is Null And V_T_C_Code Is Not Null Then
      V_F_C_Code := V_T_C_Code;
   Elsif V_F_C_Code Is Not Null And V_T_C_Code Is Null Then
      V_T_C_Code := V_F_C_Code;
   End If;

   IF V_F_C_Code IS NOT NULL AND V_T_C_Code IS NOT NULL  THEN
      V_Whr:=V_Whr|| ' AND S.C_CODE BETWEEN '''||V_F_C_Code||''' AND '''|| V_F_C_Code||'''';
   END IF;

   --##-----------------------------------------------------------------------------##--
   --## date
   If V_F_Date Is Null And V_T_Date Is Not Null Then
      V_F_Date := V_T_Date;
   End if;
   if V_F_Date Is Not Null And V_T_Date Is Null Then
      V_T_Date := V_F_Date;
   End If;

   IF V_F_Date IS NOT NULL And V_T_Date IS NOT NULL THEN
      V_Whr:=V_Whr||' And  Pd.F_Date >= to_date('''||V_F_Date||''',''dd/mm/yyyy'')  ';
      V_Whr:=V_Whr||' And Pd.T_Date  <= to_date('''||V_T_Date||''',''dd/mm/yyyy'') ';
   END IF;

  --##-----------------------------------------------------------------------------##--
   --## C_CLASS
   If V_F_C_CLASS Is Null And V_T_C_CLASS Is Not Null Then
      V_F_C_CLASS := V_T_C_CLASS;
   Elsif V_F_C_CLASS Is Not Null And V_T_C_CLASS Is Null Then
      V_T_C_CLASS := V_F_C_CLASS;
   End If;

   If V_F_C_CLASS Is Not Null Then
    Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   => V_F_C_CLASS,
                                      P_TN   => V_T_C_CLASS,
                                      P_Type => 'N') ;
   End If;

   If V_F_C_CLASS Is Not Null Then
       V_Whr :=V_Whr || ' And Nvl(S.C_CLASS,0) Between '|| V_F_C_CLASS ||' And '||V_T_C_CLASS||' ';
   End If;

   --##-----------------------------------------------------------------------------##--
   IF P_Typ = 2 THEN -- Details
        V_Whr:=V_Whr||' And PD.PLAN_NO = S.SALE_PLAN_NO_DET
                        And PD.PLAN_ser= S.SALE_PLAN_SRL_DET  ';
        V_Whr_Itm:=V_Whr_Itm||' AND D.i_code||D.ITM_UNT=(CASE WHEN PD.i_code IS NOT NULL THEN PD.i_code||NVL(PD.ITM_UNT,D.ITM_UNT) ELSE D.i_code||D.ITM_UNT END )';
   ELSE -- Summary
        V_Whr:=V_Whr||' And PD.PLAN_NO = S.SALE_PLAN_NO_SUM
                        And PD.PLAN_ser= S.SALE_PLAN_SRL_SUM ';
   END IF;


   --##-----------------------------------------------------------------------------##--
   V_Sql_Qry:=' SELECT  C_code
    ,C_NAME
    ,Plan_Ser
    ,Plan_No
    ,Plan_Type
    ,(SELECT FLG_DESC
        FROM S_FLAGS
       WHERE FLG_VALUE = M.PLAN_TYPE
         AND FLG_CODE = ''SALES_PLAN_TYPE''
         AND LANG_NO = '||p_lng_no||') PLAN_TYPE_NAME
    ,Plan_Dstr_Type
    ,(SELECT FLG_DESC
        FROM S_FLAGS
       WHERE FLG_VALUE = M.PLAN_DSTR_TYPE
         AND FLG_CODE = ''DSTR_PLAN_TYPE''
         AND LANG_NO = '||p_lng_no||') PLAN_DSTR_TYPE_NAME
    ,Plan_Prd_Type
    ,(SELECT FLG_DESC
        FROM S_FLAGS
       WHERE FLG_VALUE = M.PLAN_PRD_TYPE
         AND FLG_CODE = ''PLAN_PRD_TYPE''
         AND LANG_NO = '||p_lng_no||') PLAN_PRD_TYPE_NAME
    ,(SELECT Decode ('||p_lng_no||', 1, Nvl (I_NAME, I_E_NAME), Nvl (I_E_NAME, I_NAME) )
          FROM IAS_ITM_MST  WHERE I_CODE=M.I_CODE AND ROWNUM<=1) I_NAME
    ,Mnth
    ,F_Date
    ,T_Date
    ,I_CODE
    ,itm_unt
    ,DECODE ( PLAN_DSTR_TYPE,1,SUM(I_Qty),SUM(Local_Amt) ) Trgt
    ,ROUND(SUM(Actual),4) /DECODE( PLAN_DSTR_TYPE,1,NVL(IAS_Itm_Pkg.Get_Icode_Size_Unit(P_I_Code=>I_CODE,P_Itm_Unt=>itm_unt),1),1) Actual
 FROM (
Select S.C_Code
    ,Decode ('||p_lng_no||', 1, Nvl (C_A_Name, C_E_Name), Nvl (C_E_Name, C_A_Name) ) C_NAME
    ,PD.PLAN_NO
    ,PD.Plan_Ser
    ,PD.PLAN_TYPE
    ,PLAN_DSTR_TYPE
    ,PD.PLAN_PRD_TYPE
    ,nvl(Mnth,to_number(to_char(F_Date,''MM'')) )Mnth
    ,F_Date
    ,T_Date
    ,PD.I_CODE
    ,PD.itm_unt
    ,(I_Qty) I_Qty
    ,(Local_Amt) Local_Amt
    ,(NVL(( Select Decode (PD.Plan_Dstr_Type, 2,
                             Sum ((((Nvl(D.I_Price, 0) - Nvl (D.Dis_Amt, 0)) + (Nvl (D.Othr_Amt, 0) + Nvl (D.Vat_Amt, 0))) * Nvl (D.I_Qty, 0)) * Nvl (Bill_Rate, 1))
                            ,Sum (Nvl (D.I_Qty, 0)))  net
                From Ias_Bill_Mst M, Ias_Bill_Dtl D
                Where   M.Bill_Ser = D.Bill_Ser
                And M.C_Code = PD.C_Code
                And Bill_Date Between Pd.F_Date And Pd.T_Date '||V_Whr_Itm||' ),0)
        -NVL((Select Decode (PD.Plan_Dstr_Type, 2,
                             Sum ((((Nvl(D.I_Price, 0) - Nvl (D.Dis_Amt, 0)) + (Nvl (D.Othr_Amt, 0) + Nvl (D.Vat_Amt, 0))) * Nvl (D.I_Qty, 0)) * Nvl (rt_Bill_Rate, 1))
                            ,Sum (Nvl (D.I_Qty, 0)))  net
                From Ias_rt_Bill_Mst M, Ias_rt_Bill_Dtl D
                Where   M.rt_Bill_Ser = D.rt_Bill_Ser
                And     M.C_Code = PD.C_Code
                And     rt_Bill_Date Between Pd.F_Date And Pd.T_Date '||V_Whr_Itm||' ),0)
        +NVL((Select Decode (PD.Plan_Dstr_Type, 2,
                             Sum ((((Nvl(D.I_Price, 0) - Nvl (D.Dis_Amt, 0)) + (Nvl (D.Othr_Amt, 0) + Nvl (D.Vat_Amt, 0))) * Nvl (D.I_Qty, 0)) * Nvl (Bill_Rate, 1))
                            ,Sum (Nvl (D.I_Qty, 0)))  net
                From Ias_Bill_Mst_BR M, Ias_Bill_Dtl_BR D
                Where     M.Bill_Ser = D.Bill_Ser
                And M.C_Code = PD.C_Code
                AND Nvl (Bill_Post, 0) = 0
                AND  Nvl (Cncl_Flg, 0) = 0
                And Bill_Date Between Pd.F_Date And Pd.T_Date  '||V_Whr_Itm||' ),0)
        -NVL((Select Decode (PD.Plan_Dstr_Type, 2,
                             Sum ((((Nvl(D.I_Price, 0) - Nvl (D.Dis_Amt, 0)) + (Nvl (D.Othr_Amt, 0) + Nvl (D.Vat_Amt, 0))) * Nvl (D.I_Qty, 0)) * Nvl (rt_Bill_Rate, 1))
                            ,Sum (Nvl (D.I_Qty, 0)))  net
                From Ias_rt_Bill_Mst_BR M, Ias_rt_Bill_Dtl_BR D
                Where     M.rt_Bill_Ser = D.rt_Bill_Ser
                And M.C_Code = PD.C_Code
                AND Nvl (rt_Bill_Post, 0) = 0
                AND  Nvl (Cncl_Flg, 0) = 0
                And rt_Bill_Date Between Pd.F_Date And Pd.T_Date '||V_Whr_Itm||' ),0) ) Actual
From Ias_Sales_Plan_Dtl PD,CUSTOMER S
WHERE PD.C_Code=S.C_Code '||v_whr||'
 ) M
GROUP BY C_Code
    ,C_NAME
    ,Plan_Ser
    ,Plan_No
    ,Plan_Type
    ,Plan_Dstr_Type
    ,Plan_Prd_Type
    ,Mnth
    ,F_Date
    ,T_Date
    ,I_CODE
    ,itm_unt
ORDER BY Mnth , F_Date  ';
  --##-----------------------------------------------------------------------------##--
   Qry_Ctx :=      Dbms_Xmlgen.Newcontext(V_Sql_Qry);
   Dbms_Xmlgen.Setnullhandling(Qry_Ctx, Dbms_Xmlgen.Empty_Tag);
   Qry_Rslt :=     Dbms_Xmlgen.Getxml(Qry_Ctx);

   Return Qry_Rslt;

Exception
   When Others Then
      Raise_Application_Error(-20104, 'Error In GET_CST_Plan_TRGT.' || Chr(10) || Sqlerrm);
End GET_Cst_Plan_TRGT;
---=======================================================================================================
Function GET_Cst_Plan_TRGT_DVTN(P_Typ       In Number   Default 1 ,   -- 1-  Summary , 2-Details     P_F_C_Code    In Varchar2 Default Null,
                                    P_F_C_Code    In Varchar2 Default Null,
                                    P_T_C_Code    In Varchar2 Default Null,
                                    P_F_C_CLASS       IN     CUSTOMER.C_CLASS%TYPE      Default Null,
                                    P_T_C_CLASS       IN     CUSTOMER.C_CLASS%TYPE      Default Null,
                                    P_F_ACTVTY      IN IAS_ITM_MST.ACTIVITY_NO%TYPE     Default Null,
                                    P_T_ACTVTY      IN IAS_ITM_MST.ACTIVITY_NO%TYPE     Default Null,
                                    P_F_Date    In Date     Default Null,
                                    P_T_Date    In Date     Default Null,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      --## 1-DETAIL 2- SUM
                                    P_Lng_No    In Number   Default 1   ,
                                    P_Usr_No    In User_R.U_Id%Type )
   Return Clob
Is
   Pragma Autonomous_Transaction;
   V_Sql_Qry               Clob;
   V_Whr                   Varchar2(2000):=' ';
   V_Whr_Itm               Varchar2(2000):=' ';
   V_Whr_Itm1               Varchar2(2000):=' AND 1=1 ';
   V_Xml_Typ               Xmltype;
   V_Json_Rslt             Varchar2(4000);
   Qry_Ctx                 Dbms_Xmlgen.Ctxhandle;
   Qry_Rslt                Clob;
   V_F_Date                Date:=P_F_Date;
   V_T_Date                Date:=P_T_Date;
   V_CNT                   NUMBER;
   V_F_C_Code              Varchar2 (500);
   V_T_C_Code              Varchar2 (500);
   V_F_C_CLASS             CUSTOMER.C_CLASS%TYPE:=P_F_C_CLASS;
   V_T_C_CLASS             CUSTOMER.C_CLASS%TYPE:=P_T_C_CLASS;
   V_F_ACTVTY              IAS_ITM_MST.ACTIVITY_NO%TYPE:=P_F_ACTVTY;
   V_T_ACTVTY              IAS_ITM_MST.ACTIVITY_NO%TYPE:=P_T_ACTVTY;
Begin

   Begin
      Execute Immediate 'ALTER SESSION SET NLS_DATE_FORMAT=''DD/MM/YYYY''';
   End;
   --##-----------------------------------------------------------------------------##--
   V_F_C_Code :=     P_F_C_Code;
   V_T_C_Code :=     P_T_C_Code;
   ------------------------------------------
   --## C_CODE
   If V_F_C_Code Is Null And V_T_C_Code Is Not Null Then
      V_F_C_Code := V_T_C_Code;
   Elsif V_F_C_Code Is Not Null And V_T_C_Code Is Null Then
      V_T_C_Code := V_F_C_Code;
   End If;

   IF V_F_C_Code IS NOT NULL AND V_T_C_Code IS NOT NULL  THEN
      V_Whr:=V_Whr|| ' AND S.C_CODE BETWEEN '''||V_F_C_Code||''' AND '''|| V_F_C_Code||'''';
   END IF;

   --##-----------------------------------------------------------------------------##--
   --## date
   If V_F_Date Is Null And V_T_Date Is Not Null Then
      V_F_Date := V_T_Date;
   End if;
   if V_F_Date Is Not Null And V_T_Date Is Null Then
      V_T_Date := V_F_Date;
   End If;

   IF V_F_Date IS NOT NULL And V_T_Date IS NOT NULL THEN

      V_Whr:=V_Whr||' And Pd.F_Date >= to_date('''||V_F_Date||''',''dd/mm/yyyy'')  ';
      V_Whr:=V_Whr||' And Pd.T_Date  <= decode(PLAN_PRD_TYPE,2,last_day(to_date('''||V_T_Date||''',''dd/mm/yyyy'')),4,to_date(ias_gen_pkg.Get_Final_Day,''dd/mm/yyyy''),to_date('''||V_T_Date||''',''dd/mm/yyyy'')) ';
   END IF;

  --##-----------------------------------------------------------------------------##--
   --## C_CLASS
   If V_F_C_CLASS Is Null And V_T_C_CLASS Is Not Null Then
      V_F_C_CLASS := V_T_C_CLASS;
   Elsif V_F_C_CLASS Is Not Null And V_T_C_CLASS Is Null Then
      V_T_C_CLASS := V_F_C_CLASS;
   End If;

   If V_F_C_CLASS Is Not Null Then
    Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   => V_F_C_CLASS,
                                      P_TN   => V_T_C_CLASS,
                                      P_Type => 'N') ;
   End If;

   If V_F_C_CLASS Is Not Null Then
       V_Whr :=V_Whr || ' And Nvl(S.C_CLASS,0) Between '|| V_F_C_CLASS ||' And '||V_T_C_CLASS||' ';
   End If;

   --##-----------------------------------------------------------------------------##--
   IF P_Typ = 2 THEN -- Details
        V_Whr:=V_Whr||' And PD.PLAN_NO = S.SALE_PLAN_NO_DET
                        And PD.PLAN_ser= S.SALE_PLAN_SRL_DET  ';
        V_Whr_Itm:=V_Whr_Itm||' AND D.i_code||D.ITM_UNT=(CASE WHEN PD.i_code IS NOT NULL THEN PD.i_code||NVL(PD.ITM_UNT,D.ITM_UNT) ELSE D.i_code||D.ITM_UNT END )';
   ELSE -- Summary
        V_Whr:=V_Whr||' And PD.PLAN_NO = S.SALE_PLAN_NO_SUM
                        And PD.PLAN_ser= S.SALE_PLAN_SRL_SUM ';
   END IF;


    If V_F_ACTVTY Is Not Null and P_Typ = 2 Then
       V_WHR_ITM :=V_WHR_ITM ||' AND EXISTS (Select 1 From Ias_Items_Activity
       Where
       Activity_No Between '||V_F_Actvty||'  And '|| V_T_Actvty||'
        And Ias_Itm_Pkg.Get_Itm_Activity(D.I_Code)=Activity_No)';

      V_WHR_ITM1 :=V_WHR_ITM1 ||' AND EXISTS (Select 1 From Ias_Items_Activity
       Where
       Activity_No Between '||V_F_Actvty||'  And '|| V_T_Actvty||'
        And Ias_Itm_Pkg.Get_Itm_Activity(PD.I_Code)=Activity_No)';
   End If;

   --##-----------------------------------------------------------------------------##--
   V_Sql_Qry:=' SELECT  C_code
    ,C_NAME
    ,Plan_Ser
    ,Plan_No
    ,Plan_Type
    ,(SELECT FLG_DESC
        FROM S_FLAGS
       WHERE FLG_VALUE = M.PLAN_TYPE
         AND FLG_CODE = ''SALES_PLAN_TYPE''
         AND LANG_NO = '||p_lng_no||') PLAN_TYPE_NAME
    ,Plan_Dstr_Type
    ,(SELECT FLG_DESC
        FROM S_FLAGS
       WHERE FLG_VALUE = M.PLAN_DSTR_TYPE
         AND FLG_CODE = ''DSTR_PLAN_TYPE''
         AND LANG_NO = '||p_lng_no||') PLAN_DSTR_TYPE_NAME
    ,Plan_Prd_Type
    ,(SELECT FLG_DESC
        FROM S_FLAGS
       WHERE FLG_VALUE = M.PLAN_PRD_TYPE
         AND FLG_CODE = ''PLAN_PRD_TYPE''
         AND LANG_NO = '||p_lng_no||') PLAN_PRD_TYPE_NAME
    ,(SELECT Decode ('||p_lng_no||', 1, Nvl (I_NAME, I_E_NAME), Nvl (I_E_NAME, I_NAME) )
          FROM IAS_ITM_MST  WHERE I_CODE=M.I_CODE AND ROWNUM<=1) I_NAME
    ,Mnth
    ,F_Date
    ,T_Date
    ,I_CODE
    ,itm_unt
         --------------ACTVTY_NAME----------------
    ,(select decode('||p_lng_no||',1,ACTIVITY_A_NAME,ACTIVITY_E_NAME) from Ias_Items_Activity
     where  ACTIVITY_NO=Ias_Itm_Pkg.Get_Itm_Activity(I_Code) ) ACTVTY_NAME
        --------------Trgt----------------
    ,DECODE ( PLAN_DSTR_TYPE,1,SUM(I_Qty),SUM(Local_Amt) ) Trgt
        --------------Actual----------------
    ,ROUND(SUM(Actual),4) /DECODE( PLAN_DSTR_TYPE,1,NVL(IAS_Itm_Pkg.Get_Icode_Size_Unit(P_I_Code=>I_CODE,P_Itm_Unt=>itm_unt),1),1) Actual
         --------------dvtn----------------
    ,ROUND(SUM(Actual),4) /DECODE( PLAN_DSTR_TYPE,1,NVL(IAS_Itm_Pkg.Get_Icode_Size_Unit(P_I_Code=>I_CODE,P_Itm_Unt=>itm_unt),1),1)-
     DECODE ( PLAN_DSTR_TYPE,1,SUM(I_Qty),SUM(Local_Amt) ) dvtn ,
         --------------cmltv_dvtn----------------
    SUM(ROUND(SUM(Actual),4) /DECODE( PLAN_DSTR_TYPE,1,NVL(IAS_Itm_Pkg.Get_Icode_Size_Unit(P_I_Code=>I_CODE,P_Itm_Unt=>itm_unt),1),1)
    -DECODE ( PLAN_DSTR_TYPE,1,SUM(I_Qty),SUM(Local_Amt) ))
    OVER(ORDER BY  mnth )cmltv_dvtn
 FROM (
Select S.C_Code
    ,Decode ('||p_lng_no||', 1, Nvl (C_A_Name, C_E_Name), Nvl (C_E_Name, C_A_Name) ) C_NAME
    ,PD.PLAN_NO
    ,PD.Plan_Ser
    ,PD.PLAN_TYPE
    ,PLAN_DSTR_TYPE
    ,PD.PLAN_PRD_TYPE
    ,nvl(Mnth,to_number(to_char(F_Date,''MM'')) )Mnth
    ,F_Date
    ,T_Date
    ,PD.I_CODE
    ,PD.itm_unt
    ,(I_Qty) I_Qty
    ,(Local_Amt) Local_Amt
    ,(NVL(( Select Decode (PD.Plan_Dstr_Type, 2,
                             Sum ((((Nvl(D.I_Price, 0) - Nvl (D.Dis_Amt, 0)) + (Nvl (D.Othr_Amt, 0) + Nvl (D.Vat_Amt, 0))) * Nvl (D.I_Qty, 0)) * Nvl (Bill_Rate, 1))
                            ,Sum (Nvl (D.I_Qty, 0)))  net
                From Ias_Bill_Mst M, Ias_Bill_Dtl D
                Where   M.Bill_Ser = D.Bill_Ser
                And M.C_Code = PD.C_Code
                And Bill_Date Between Pd.F_Date And Pd.T_Date '||V_Whr_Itm||' ),0)
        -NVL((Select Decode (PD.Plan_Dstr_Type, 2,
                             Sum ((((Nvl(D.I_Price, 0) - Nvl (D.Dis_Amt, 0)) + (Nvl (D.Othr_Amt, 0) + Nvl (D.Vat_Amt, 0))) * Nvl (D.I_Qty, 0)) * Nvl (rt_Bill_Rate, 1))
                            ,Sum (Nvl (D.I_Qty, 0)))  net
                From Ias_rt_Bill_Mst M, Ias_rt_Bill_Dtl D
                Where   M.rt_Bill_Ser = D.rt_Bill_Ser
                And     M.C_Code = PD.C_Code
                And     rt_Bill_Date Between Pd.F_Date And Pd.T_Date '||V_Whr_Itm||' ),0)
        +NVL((Select Decode (PD.Plan_Dstr_Type, 2,
                             Sum ((((Nvl(D.I_Price, 0) - Nvl (D.Dis_Amt, 0)) + (Nvl (D.Othr_Amt, 0) + Nvl (D.Vat_Amt, 0))) * Nvl (D.I_Qty, 0)) * Nvl (Bill_Rate, 1))
                            ,Sum (Nvl (D.I_Qty, 0)))  net
                From Ias_Bill_Mst_BR M, Ias_Bill_Dtl_BR D
                Where     M.Bill_Ser = D.Bill_Ser
                And M.C_Code = PD.C_Code
                AND Nvl (Bill_Post, 0) = 0
                AND  Nvl (Cncl_Flg, 0) = 0
                And Bill_Date Between Pd.F_Date And Pd.T_Date  '||V_Whr_Itm||' ),0)
        -NVL((Select Decode (PD.Plan_Dstr_Type, 2,
                             Sum ((((Nvl(D.I_Price, 0) - Nvl (D.Dis_Amt, 0)) + (Nvl (D.Othr_Amt, 0) + Nvl (D.Vat_Amt, 0))) * Nvl (D.I_Qty, 0)) * Nvl (rt_Bill_Rate, 1))
                            ,Sum (Nvl (D.I_Qty, 0)))  net
                From Ias_rt_Bill_Mst_BR M, Ias_rt_Bill_Dtl_BR D
                Where     M.rt_Bill_Ser = D.rt_Bill_Ser
                And M.C_Code = PD.C_Code
                AND Nvl (rt_Bill_Post, 0) = 0
                AND  Nvl (Cncl_Flg, 0) = 0
                And rt_Bill_Date Between Pd.F_Date And Pd.T_Date '||V_Whr_Itm||' ),0) ) Actual
From Ias_Sales_Plan_Dtl PD,CUSTOMER S , IAS_PRIV_CUSTOMER D
WHERE PD.C_CODE         = S.C_CODE
AND   S.C_CODE          = D.C_CODE
AND   PD.C_CODE         = D.C_CODE
AND   D.U_ID            = '||P_USR_NO||'
AND   NVL(D.VIEW_FLAG,0) = 1
 '||V_WHR||V_WHR_ITM1||'
 ) M
GROUP BY C_Code
    ,C_NAME
    ,Plan_Ser
    ,Plan_No
    ,Plan_Type
    ,Plan_Dstr_Type
    ,Plan_Prd_Type
    ,Mnth
    ,F_Date
    ,T_Date
    ,I_CODE
    ,itm_unt
ORDER BY Mnth , F_Date  ';

/*
 DELETE from YS.PARA;
INSERT INTO YS.PARA VALUES ('v_whr',v_whr);
INSERT INTO YS.PARA VALUES ('V_Whr_Itm',V_Whr_Itm);
INSERT INTO YS.PARA VALUES ('p_lng_no',p_lng_no);
INSERT INTO YS.PARA VALUES ('V_Sql_Qry',V_Sql_Qry);

COMMIT;
*/
  --##-----------------------------------------------------------------------------##--
   Qry_Ctx :=      Dbms_Xmlgen.Newcontext(V_Sql_Qry);
   Dbms_Xmlgen.Setnullhandling(Qry_Ctx, Dbms_Xmlgen.Empty_Tag);
   Qry_Rslt :=     Dbms_Xmlgen.Getxml(Qry_Ctx);

   Return Qry_Rslt;

Exception
   When Others Then
      Raise_Application_Error(-20104, 'Error In GET_CST_Plan_TRGT.' || Chr(10) || Sqlerrm);
End GET_Cst_Plan_TRGT_DVTN;

--================================================================================---
Function Get_Cst_Instlmnt_Dr( P_C_Code      In Varchar2 Default Null
                             ,P_Cur_Code      In Varchar2 Default Null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   --## 1-DETAIL 2- SUM
                            ,P_Usr_No        In User_R.U_Id%Type
                            ,P_Lng_No        In Number   Default 1
                           ) Return Clob Is
V_Json_Rslt             Varchar2 (4000):='{"_Result": { "_Doc_No":"@DOC_NO","_ErrMsg": "@errmsg","_ErrNo": @errno } }';
V_Msg_Txt               Varchar2 (4000);
V_Lng_No                Number:=nvl(P_Lng_No,1);
V_Sql_Qry               Clob;
V_Err_No                Varchar2(200);
Qry_Rslt                 clob;
v_whr                     Varchar2(2000);
V_Aralt                 Number(2) := 0;
Begin

     If P_C_Code Is Null Then
          V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => V_Lng_No, P_Msg_No => 817);
          V_Err_No:=$$plsql_Line;
          Goto Rtn_Rslt;
     End If;

      If P_Usr_No Is Null Then
          V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => V_Lng_No, P_Msg_No => 450);
           V_Err_No:=$$plsql_Line;
          Goto Rtn_Rslt;
     End If;

     Begin
      Select Nvl(Ar_Ac_Link_Type, 0)
        Into V_Aralt
        From Ias_Para_Ar;
     Exception
      When Others Then
         Null;
     End;

 If P_C_code is Not Null Then
  v_whr:=V_whr||' and M.C_code='''||P_C_Code||''' ';
 End If;


 If P_Cur_code is Not Null Then
  v_whr:=V_whr||' and M.A_Cy='''||P_Cur_code||''' ';
 End If;


 If nvl(V_Aralt,0)=1 Then
    V_Whr :=V_Whr||' And Exists(
                               Select 1
                                 From Priv_Acc
                                Where U_Id = ' || P_Usr_No || '
                                  And A_Code = C.C_A_Code
                                  And A_Cy = M.A_Cy
                                  And Nvl(View_Flag, 0) = 1
                                  And Rownum <= 1) ';
 Else
  V_Whr :=V_Whr||' And Exists(
                           Select 1
                             From Ias_Priv_Customer
                            Where U_Id =' || P_Usr_No || '
                              And C_Code = M.C_Code
                              And A_Cy = M.A_Cy
                              And Nvl(View_Flag, 0) = 1
                              And Rownum <= 1) ';
 End If;

 V_Whr:=V_Whr||' And  Exists(Select 1
                         From   S_brn_usr_priv
                         Where  U_id = '||P_Usr_No ||'
                         And S_brn_usr_priv.Brn_no = M.Brn_no
                          And Nvl(View_Flag, 1) = 1
                           And Rownum <= 1) ';

 V_Sql_Qry:=' Select M.Doc_Type
                   ,M.Bill_No
                   ,M.Bill_Ser
                   ,M.Doc_Date
                   ,M.C_Code
                   ,Sum (Nvl (M.I_Amt, 0)) I_Amt
                   ,Sum (Nvl (M.Paid_Amt, 0)) Paid_Amt
                   ,Sum (Nvl (M.Adj_Amt, 0)) Adj_Amt
                   ,M.A_Cy
                   ,M.I_Py
                   ,M.I_No
                   ,Nvl ( (Sum (Nvl (M.I_Amt, 0)) - (Sum (Nvl (M.Paid_Amt, 0)) + Sum (Nvl (M.Adj_Amt, 0)))), 0) Rem_Amt
               From Installment M ,customer c
              Where  M.c_code=C.c_code
              And M.Doc_Type = 4
              And M.C_Code Is Not Null '||V_whr||'
              And Nvl (M.I_Amt, 0) - (Nvl (M.Paid_Amt, 0) + Nvl (M.Adj_Amt, 0)) > 0
           Group By M.Doc_Type
                   ,M.Bill_No
                   ,M.Bill_Ser
                   ,M.Doc_Date
                   ,M.C_Code
                   ,M.A_Cy
                   ,M.I_Py
                   ,M.I_No ';

 --####################################################################--
  Begin
       Qry_Rslt:=Genrat_Data_File (P_Doc_Type          => Null
                                  ,P_Mst_Qry           =>V_Sql_Qry
                                  ,P_Dtl_Qry           =>Null
                                  ,P_Mst_Dtl_Flg       => 0
                                  ,P_Out_Data_Typ      =>0) ;
   Exception When no_data_Found Then
     Null;
   When Others Then
       V_Msg_Txt := 'Err.'||sqlerrm;
       V_Err_No:=$$plsql_Line;
   End;
   Return Qry_Rslt;

  --####################--
  <<Rtn_rslt>>
   If V_Msg_Txt Is Not Null Then
      V_Json_Rslt := Replace (V_Json_Rslt, '@DOC_NO', Null);
      V_Json_Rslt := Replace (V_Json_Rslt, '@errno', V_Err_No);
      V_Json_Rslt := Replace (V_Json_Rslt, '@errmsg', V_Msg_Txt);
      return V_Json_Rslt;

   End If;
--####################--

Exception
   When Others Then
      Raise_Application_Error(-20104, 'Error In Get_Cst_Instlmnt_Dr.' || Chr(10) || Sqlerrm);
End  Get_Cst_Instlmnt_Dr;
--================================================================================---
function  CLC_CST_AGING (  P_Sys_No          In Number
                          ,P_F_C_Code        In Varchar2 Default Null
                          ,P_T_C_Code        In Varchar2 Default Null
                          ,P_F_Rep_Code      In Varchar2 Default Null
                          ,P_T_Rep_Code      In Varchar2 Default Null
                          ,P_Curr_Code       In     Varchar2 Default Null
                          ,P_Chk_C_V_Code    In     Varchar2 Default 0
                          ,P_Paid_Inst_Mnl   In Number Default 0
                          ,P_By_Local_Cur    In Number Default 0
                          ,P_By_Sman         In Varchar2 Default 0
                          ,P_By_Sub_Ldgr     In Varchar2 Default 0--## 1 cc_code-2 prj_no 3- activ_no
                          ,P_Rep_Year        In Number Default 0
                          ,P_Fill_Cst_Rep_Type In Number Default 0
                          ,P_Per_No          In Number Default Null
                          ,P_F_Day           In Number Default Null
                          ,P_T_Day           In Number Default Null
                          ,P_T_Date          In Date
                          ,P_User_No         In     Number
                          ,P_Conn_Prv_Year   In     Number Default 0  --## 1- Conn.With Previous Year
                          ,P_Lng_No          In     Number Default 1
                          ,P_Whr             In Varchar2 Default Null) RETURN  TP_CST_CR_TBL PIPELINED
Is
Pragma Autonomous_Transaction;
 --V_CST_CR_RFC      TP_CST_CR_RFC;
   V_F_C_Code              Varchar2 (500);
   V_T_C_Code              Varchar2 (500);
   V_F_Rep_Code              Varchar2 (500);
   V_T_Rep_Code              Varchar2 (500);
   V_F_Date                Date;
   V_T_Date                Date;
   V_Whr_Data              Varchar2 (8000);
   V_Whr_Inst_Mnl          Varchar2 (8000);
   V_Aralt                 Number (1) := 0;
   V_Cst_Grp               Varchar2 (500);
   V_Sman_Grp              Varchar2 (500);
   V_Conn_Cst_Multi_Sman   Number (1);
   V_Paid_Inst_Mnl         Number:=0;
   V_cstmr_blnc_type       Number:=0;
   V_Cnt                   Number;
     V_AR_CS_TYPE    Number        := 0;
   V_AR_PJ_TYPE    Number        := 0;
   V_AR_ACTV_TYPE  Number        := 0;
   V_CC_PJ_ACTV    Number        := 0;
   V_Sql_Qry               Clob;
   V_Lng_No                Number (1):=Nvl (P_Lng_No, 1);
  -- V_Due_Amt_Type          Number (1) := Nvl (P_Due_Amt_Type, 1);
  -- V_Due_Amt_Fld           Varchar2 (8000);
   V_Local_Cur             Varchar2 (500);
   V_Msg_Txt               Varchar2 (4000);
    V_FLD_CC_CODE Varchar2(100):='''0''' ; --NULL
   V_FLD_Pj_No   Varchar2(100):='''0''' ;
   V_FLD_Actv_No Varchar2(100):='''0''' ;
   v_rt_qry  CLOB;
   V_PRD_LBL   varchar2(500);
    V_tbl_rt_mst           VARCHAR2(500);
  V_tbl_rt_dtl           VARCHAR2(500);
  V_tbl_add_mst          VARCHAR2(500);
  V_tbl_add_dtl          VARCHAR2(500);
   v_post_dtl          VARCHAR2(500);
Begin
   V_PRD_LBL   :=IAS_GEN_PKG.GET_PROMPT (V_Lng_No ,438);

   If P_Sys_No Is Null Then
      V_Msg_Txt := 'ENTER P_SYS_NO   ';
      Goto Rtn_Rslt;
   End If;


   If P_User_No Is Null Then
      V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => V_Lng_No, P_Msg_No => 450);
      Goto Rtn_Rslt;
   End If;

   Begin
      Select Nvl (Ar_Ac_Link_Type, 0), Nvl (Conn_Cst_Multi_Sman, 0), Nvl (Paid_Instllmnt_Man, 0)
        Into V_Aralt, V_Conn_Cst_Multi_Sman, V_Paid_Inst_Mnl
        From Ias_Para_Ar;
   Exception
      When Others Then
         Null;
   End;
   -------------------------------------------------------
  Begin
    select  nvl(AR_CS_TYPE,0) ,nvl(AR_PJ_TYPE,0),nvl(AR_ACTV_TYPE,0)
      into V_AR_CS_TYPE ,V_AR_PJ_TYPE,V_AR_ACTV_TYPE
    from ias_para_ar;
  Exception when Others Then
  Null;
  End ;
  -------------------------------------------------------     ;
  If Nvl(V_AR_CS_TYPE,0)=2 or Nvl(V_AR_PJ_TYPE,0)=2 or Nvl(V_AR_ACTV_TYPE,0)=2 Then
    V_CC_PJ_ACTV:=0;
  Else
    V_CC_PJ_ACTV:=1;
  End If;
  -------------------------------------------------------

   If Nvl (P_Sys_No, 0) = 70 Then
      Begin
         V_Cstmr_Blnc_Type := Ias_Gen_Pkg.Get_Cnt ('Select NVL (CSTMR_BLNC_TYPE, 0) From DTS_PARA');
      Exception
         When Others Then
            V_Cstmr_Blnc_Type := 0;
      End;
   End If;

   Begin
      Execute Immediate 'ALTER SESSION SET NLS_DATE_FORMAT=''DD/MM/RRRR''';
   End;

   V_F_C_Code := P_F_C_Code;
   V_T_C_Code := P_T_C_Code;
   V_F_Rep_Code := P_F_Rep_Code;
   V_T_Rep_Code := P_T_Rep_Code;
   V_Local_Cur := Ias_Gen_Pkg.Get_Local_Cur;
   ------------------------------------------
   IF Nvl(P_Chk_C_V_Code, 0)=1 THEN
     V_Whr_Data:=V_Whr_Data||' AND A.C_Code =B.C_V_Code ';
     V_Whr_Data:=V_Whr_Data||' AND A.C_A_Code=A.C_A_Code ';
     V_Whr_Data:=V_Whr_Data||' AND B.C_V_Code IS NOT NULL ';
   ELSE
     V_Whr_Data:=V_Whr_Data||' and A.C_Code =B.AC_CODE_DTL AND AC_DTL_TYP=3 ';
     V_Whr_Data:=V_Whr_Data||' AND A.C_A_Code=B.A_Code ';
     V_Whr_Data:=V_Whr_Data||' AND B.AC_CODE_DTL IS NOT NULL ';
   END IF;


   --## C_CODE
   If V_F_C_Code Is Null And V_T_C_Code Is Not Null Then
      V_F_C_Code := V_T_C_Code;
   Elsif V_F_C_Code Is Not Null And V_T_C_Code Is Null Then
      V_T_C_Code := V_F_C_Code;
   End If;

   If V_F_C_Code Is Not Null Then
      V_Whr_Data := V_Whr_Data || ' And LPAD(a.C_Code,30,''0'') Between LPAD(''' || V_F_C_Code || ''',30,''0'') And  LPAD(''' || V_T_C_Code || ''',30,''0'') ';
      V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' and b.c_code between nvl(''' || V_F_C_Code || ''',b.c_code) and nvl(''' || V_T_C_Code || ''',b.c_code) ';
   End If;
   ------------------------------------------
   --## Rep_CODE
   If V_F_Rep_Code Is Null And V_T_Rep_Code Is Not Null Then
      V_F_Rep_Code := V_T_Rep_Code;
   Elsif V_F_Rep_Code Is Not Null And V_T_Rep_Code Is Null Then
      V_T_Rep_Code := V_F_Rep_Code;
   End If;

   -----------------------------------------------------------------
   V_T_Date := P_T_Date;

   If P_T_Date Is Null Then
      V_F_Date := Ias_Gen_Pkg.Get_Frst_Day;
      V_T_Date := to_date(sysdate,'DD/MM/RRRR');--Ias_Gen_Pkg.Get_final_day;
   Else
      V_F_Date := Ias_Gen_Pkg.Get_Frst_Day;
      V_T_Date := P_T_Date;
   End If;

   V_Whr_Data := V_Whr_Data || ' And Doc_Date <= to_date(''' || V_T_Date || ''',''dd/mm/yyyy'') ';
   V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' And Doc_Date <= ''' || V_T_Date || ''' ';

   -----------------------------------------------------------------
   If P_Curr_Code Is Not Null Then
      V_Whr_Data := V_Whr_Data || ' And B.A_Cy =''' || P_Curr_Code || ''' ';
      V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' And B.A_Cy =''' || P_Curr_Code || ''' ';
   End If;

   ----------------------------------------------------------------
     If nvl(P_Conn_Prv_Year,0)=0 Then

        V_tbl_rt_mst    := 'IAS_RT_BILL_MST';
        V_tbl_rt_dtl    := 'IAS_RT_BILL_Dtl';
        V_tbl_add_mst   := 'IAS_BILL_MST_ADD_DISC';
        V_tbl_add_dtl   := 'IAS_BILL_DTL_ADD_DISC';
        v_post_dtl:='IAS_POST_DTL';
    ELSE
        V_tbl_rt_mst    := 'IAS_V_RT_BILL_MST_YR';
        V_tbl_rt_dtl    := 'IAS_V_RT_BILL_Dtl_YR';
        V_tbl_add_mst   := 'IAS_V_BILL_MST_ADD_DISC_YR';
        V_tbl_add_dtl   := 'IAS_V_BILL_DTL_ADD_DISC_YR';
        v_post_dtl:='IAS_V_POST_DTL_YR';
    END IF;
  ------------------------------------------------
   If P_User_No<>1 Then
    If Nvl(V_Aralt,0)=1 Then
      V_Whr_Data := V_Whr_Data || '  And Exists(
                                       Select 1
                                         From Priv_Acc
                                        Where U_Id = ' || P_User_No || '
                                          And A_Code = A.C_A_Code
                                          And A_Cy = B.A_Cy
                                          And Nvl(View_Flag, 0) = 1
                                          And Rownum <= 1) ';
      V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || '  And Exists(
                                       Select 1
                                         From Priv_Acc
                                        Where U_Id = ' || P_User_No || '
                                          And A_Code = A.C_A_Code
                                          And A_Cy = B.A_Cy
                                          And Nvl(View_Flag, 0) = 1
                                          And Rownum <= 1) ';
    ElsIf Nvl(V_Aralt,0)=2 Then
     V_Whr_Data := V_Whr_Data || ' And Exists(
                               Select 1
                                 From Ias_Priv_Customer
                                Where U_Id =' || P_User_No || '
                                  And C_Code = A.C_Code
                                  And A_Cy = B.A_Cy
                                  And Nvl(View_Flag, 0) = 1
                                  And Rownum <= 1) ';
    V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' And Exists(
                                   Select 1
                                     From Ias_Priv_Customer
                                    Where U_Id =' || P_User_No || '
                                      And C_Code = A.C_Code
                                      And A_Cy = B.A_Cy
                                      And Nvl(View_Flag, 0) = 1
                                      And Rownum <= 1) ';

   End If;

   V_Whr_Data := V_Whr_Data || ' and Exists(Select 1
                 From   S_brn_usr_priv
                 Where  U_id = '||P_User_No ||'
                 And S_brn_usr_priv.Brn_no = b.Brn_no
                  And Nvl(View_Flag, 1) = 1
                   And Rownum <= 1)  ';

  V_Whr_Inst_Mnl := V_Whr_Inst_Mnl || ' and Exists(Select 1
                 From   S_brn_usr_priv
                 Where  U_id = '||P_User_No ||'
                 And S_brn_usr_priv.Brn_no = b.Brn_no
                  And Nvl(View_Flag, 1) = 1
                   And Rownum <= 1)  ';
 End If;

   ----------------------------------------------------------------
   If nvl(V_CC_PJ_ACTV,0)=1 Then
       If Nvl (P_By_Sub_Ldgr, 0) = 1 Then
          V_FLD_CC_CODE := ' B.Cc_Code ';
          V_Cst_Grp  :=' B.Cc_Code ';
          V_Whr_Data := V_Whr_Data || ' AND  B.Cc_Code IS NOT NULL ';
       Elsif Nvl (P_By_Sub_Ldgr, 0) = 2 Then
          V_FLD_Pj_No := ' B.Pj_No ';
          V_Cst_Grp  :=' B.Pj_No ';
          V_Whr_Data := V_Whr_Data || ' AND  B.Pj_No IS NOT NULL ';
       Elsif Nvl (P_By_Sub_Ldgr, 0) = 3 Then
          V_FLD_Actv_No := '  B.Actv_No ';
           V_Cst_Grp  :=' B.Actv_No ';
          V_Whr_Data := V_Whr_Data || ' AND  B.Actv_No IS NOT NULL ';
       Else
          V_Cst_Grp := '''0''';
       End If;
   End If;

   ----------------------------------------------------------------
   If Nvl (V_Paid_Inst_Mnl, 0) = 1 And Nvl (P_Conn_Prv_Year, 0) = 0 Then
     -- V_Whr_Data := V_Whr_Inst_Mnl;
     null;
   End If;

   --####################################################################--

   Declare
      V_Whr_Sman   Varchar2 (5000) := ' ';
      V_Whr_Cst    Varchar2 (5000) := ' ';
   Begin
         If V_F_Rep_Code Is Not Null Then
                     V_Whr_Sman := ' And Rep_Code Between ''' || V_F_Rep_Code || ''' And ''' || P_T_Rep_Code || '''';
         End If;

        If p_sys_no=70 Then
          V_Sman_Grp := '  Nvl(B.Rep_Code, ''0'') ';
          V_Whr_Data := V_Whr_Data || ' AND  B.Rep_Code IS NOT NULL ';

          If V_F_Rep_Code Is Not Null Then
             V_Whr_Data := V_Whr_Data || ' AND Nvl(B.Rep_Code, ''0'')  Between ''' || P_F_Rep_Code || ''' AND  ''' || P_T_Rep_Code || ''' ';
          End If;
        Else
            If  Nvl (P_By_Sman, 0)=1 Then

              If  Nvl(P_Fill_Cst_Rep_Type,0) = 0 Then
                 V_Sman_Grp := '  Nvl(B.Rep_Code, ''0'') ';
                 V_Whr_Data := V_Whr_Data || ' AND  B.Rep_Code IS NOT NULL ';
                 If V_F_Rep_Code Is Not Null Then
                   V_Whr_Data := V_Whr_Data || ' AND Nvl(B.Rep_Code, ''0'')  Between ''' || P_F_Rep_Code || ''' AND  ''' || P_T_Rep_Code || ''' ';
                 End If;

              Else
                 V_Sman_Grp := ' Nvl(A.Rep_Code, ''0'') ';
                  If V_Conn_Cst_Multi_Sman = 1  Then
                     V_Whr_Data :=V_Whr_Data|| ' And A.C_Code In (Select C_Code From Ias_Cst_Sman Where 1=1  ' || V_Whr_Sman || ')  ';
                  Else
                      V_Whr_Data := V_Whr_Data||' And A.C_Code In (Select C_Code From Customer Where Rep_Code Is Not Null   ' || V_Whr_Sman || ')  ';
                  End If;

              End If;

            Else
              V_Sman_Grp := '''0''';
               If V_F_Rep_Code Is Not Null Then
                  If V_Conn_Cst_Multi_Sman = 1  Then
                     V_Whr_Data := V_Whr_Data||' And A.C_Code In (Select C_Code From Ias_Cst_Sman Where 1=1  ' || V_Whr_Sman || ')  ';
                  Else
                      V_Whr_Data :=V_Whr_Data|| ' And A.C_Code In (Select C_Code From Customer Where Rep_Code Is Not Null   ' || V_Whr_Sman || ')  ';
                  End If;
               End if;
            End If;
          End If;
   End;
   -------------------------------------------------------------------------------------
   /* v_rt_qry:='NVL(( Select nvl(Sum(Dtl_Amt * Per_Amt),0)
                                                      From (
                                                      Select       rt_Bill_no,
                                                                   rt_Bill_Ser,
                                                                   Bill_Ser,
                                                                   bill_no,
                                                                   Cc_Code,
                                                                   Pj_No,
                                                                   Actv_No,
                                                                   Rt_Bill_Date,
                                                                   Rt_Bill_Rate,
                                                                   (Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser )   )bill_amt,
                                                                   Ac_Amt,
                                                                   Dtl_Amt,
                                                                    case when Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)>0 then ((Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)- Ac_Amt)/Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser) )else 0 end Per_Amt
                                                              From (Select m.rt_Bill_no,
                                                                           m.rt_Bill_Ser,
                                                                           Bill_Ser,
                                                                           bill_no,
                                                                           D.Cc_Code,
                                                                           D.Pj_No,
                                                                           D.Actv_No,
                                                                           M.Rt_Bill_Date,
                                                                           M.Rt_Bill_Rate,
                                                                           Nvl((Nvl(D.I_Qty, 0) * (Nvl(D.I_Price, 0) - Nvl(D.Dis_Amt, 0) + Nvl(D.Vat_Amt, 0) + Nvl(D.Othr_Amt, 0))), 0) Dtl_Amt,
                                                                           ((Nvl(M.Cr_Card_Amt, 0) + Nvl(M.Cr_Card_Amt_Scnd, 0) + Nvl(M.Cr_Card_Amt_Thrd, 0)) + Nvl(M.Ac_Amt, 0)) Ac_Amt
                                                                      From IAS_RT_BILL_MST M, IAS_RT_BILL_dtl D
                                                                     Where M.Rt_Bill_Ser = D.Rt_Bill_Ser
                                                                           And M.Rt_Bill_Doc_Type = 4
                                                                           And M.P_Year In (0, 3)
                                                                           and rt_bill_date      <='''||V_T_Date||'''
                                                                           And D.bill_ser=B.DOC_SER
                                                                           and b.doc_type=4))),0)';*/


  -------------------------------------------------------------------------------------
  V_Sql_Qry:= '
  with  Rt_Qry as( Select nvl(Sum(Dtl_Amt * Per_Amt),0) Rt_Amt,Bill_Ser,rt_Bill_Ser
                                      From (
                                      Select       rt_Bill_no,
                                                   rt_Bill_Ser,
                                                   Bill_Ser,
                                                   bill_no,
                                                   Cc_Code,
                                                   Pj_No,
                                                   Actv_No,
                                                   Rt_Bill_Date,
                                                   Rt_Bill_Rate,
                                                   (Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser )  )bill_amt,
                                                   Ac_Amt,
                                                   Dtl_Amt,
                                                    case when Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)>0 then ((Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)- Ac_Amt)/Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser) )else 0 end Per_Amt
                                              From (Select m.rt_Bill_no,
                                                           m.rt_Bill_Ser,
                                                           M.RT_BILL_CURRENCY,
                                                           Bill_Ser,
                                                           bill_no,
                                                           D.Cc_Code,
                                                           D.Pj_No,
                                                           D.Actv_No,
                                                           M.Rt_Bill_Date,
                                                           M.Rt_Bill_Rate,
                                                           Nvl((Nvl(D.I_Qty, 0) * (Nvl(D.I_Price, 0) - Nvl(D.Dis_Amt, 0) + Nvl(D.Vat_Amt, 0) + Nvl(D.Othr_Amt, 0))), 0) Dtl_Amt,
                                                           ((Nvl(M.Cr_Card_Amt, 0) + Nvl(M.Cr_Card_Amt_Scnd, 0) + Nvl(M.Cr_Card_Amt_Thrd, 0)) + Nvl(M.Ac_Amt, 0)) Ac_Amt
                                                      From '||V_tbl_rt_mst||' M, '||V_tbl_rt_Dtl||' D
                                                     Where M.Rt_Bill_Ser = D.Rt_Bill_Ser
                                                           And M.Rt_Bill_Doc_Type = 4
                                                           And M.P_Year In (0, 3)
                                                           and rt_bill_date      <='''||V_T_Date||'''
                                                           And D.bill_ser Is Not Null
                                                           Union ALL
                                            Select m.DOC_NO  rt_Bill_no,
                                                   m.DOC_SER rt_Bill_Ser,
                                                   M.A_CY RT_BILL_CURRENCY,
                                                   D.Bill_Ser,
                                                   D.bill_no,
                                                   M.Cc_Code,
                                                   M.Pj_No,
                                                   M.Actv_No,
                                                   M.DOC_DATE Rt_Bill_Date,
                                                   M.DOC_RATE Rt_Bill_Rate,
                                                   Nvl(D.ADD_DIS_QTY, 0) * Nvl(D.ADD_DIS_AMT_DTL, 0)+(Nvl(D.Add_Dis_Qty,0)*Nvl(D.ADD_VAT_AMT,0)) Dtl_Amt,
                                                   0 Ac_Amt
                                              From ' || V_tbl_add_mst || ' M, '|| V_tbl_add_dtl || ' D
                                             Where M.DOC_SER = D.DOC_SER AND NVL(NOTE_TYP,0)=1
                                                   And M.BILL_DOC_TYPE = 4
                                                   and M.DOC_DATE      <='''||V_T_Date||'''
                                                           ))
                                                           group by Bill_Ser,rt_Bill_Ser
                                )
  ,cst_tbl as(Select A.C_Code
                  ,decode('||P_By_Local_Cur||',1,'''||V_Local_Cur||''',B.A_Cy) A_Cy
                  ,Doc_No
                  ,Doc_Type
                  ,Jv_Type
                  ,Doc_Ser
                  ,Doc_Date
                  ,Doc_Due_Date
                 , avg(Decode(nvl(dr_Amt_F,0),0,1,(nvl(dr_Amt,0)/nvl(dr_Amt_F,0)) )) Ac_Rate
                  ,Sum (decode('||P_By_Local_Cur||',1,Nvl(Dr_Amt,0),decode(B.A_Cy,'''||V_Local_Cur||''',Nvl(Dr_Amt,0) ,Nvl(Dr_Amt_f,0)))) Doc_Dr_Amt
                  ,case when doc_type =4   and '||P_By_Local_Cur||'=0
                                                         Then nvl((select sum(rt_amt) from  Rt_Qry
                                                                        where bill_ser=b.doc_ser),0)
                        when doc_type =4   and '||P_By_Local_Cur||'=1
                                                         Then nvl((select sum(rt_amt) from  Rt_Qry
                                                                        where bill_ser=b.doc_ser),0)  * avg(Decode(nvl(dr_Amt_F,0),0,1,(nvl(dr_Amt,0)/nvl(dr_Amt_F,0)) ))
                                               else 0 end Rt_Amt
                   ,Sum (decode('||P_By_Local_Cur||',1,Nvl(cr_Amt,0),decode(B.A_Cy,'''||V_Local_Cur||''',Nvl(cr_Amt,0) ,Nvl(cr_Amt_f,0)))) cr_Amt
                  ,Doc_Desc
                  ,Ref_No
                  ,B.Rcrd_No
                  ,B.Cheque_Valued
                  ,To_Date ( '''||V_T_Date||''' , ''DD/MM/YYYY'') - Doc_Date Per_No
                  ,B.Brn_No
                  ,B.Brn_Year
                  ,B.Cmp_No
                  ,B.Brn_Usr
                  ,Nvl(A.Credit_Period,0) Credit_Period
                  ,'''||V_Local_Cur||''' Local_Cur
                  ,'||V_FLD_CC_CODE||'  Cc_Code
                  ,'||V_FLD_Pj_No||'  Pj_No
                  ,'||V_FLD_Actv_No||' Actv_No
                  ,'||V_Sman_Grp||'  Rep_Code
                  ,'||V_Cst_Grp||' Cst_Grp
              From Customer A, '||v_post_dtl||'  B
             Where 1=1 '||V_Whr_Data||'
             And b.Doc_Ser Not In( Select Rt_Bill_Ser
                      From Rt_Qry
                     )
               group by
                  A.C_Code
                  ,decode('||P_By_Local_Cur||',1,'''||V_Local_Cur||''',B.A_Cy)
                  ,Doc_No
                  ,Doc_Type
                  ,Jv_Type
                  ,Doc_Ser
                  ,Doc_Date
                  ,Doc_Due_Date
                  ,Doc_Desc
                  ,Ref_No
                  ,B.Rcrd_No
                  ,B.Cheque_Valued
                  ,To_Date ( '''||V_T_Date||''' , ''DD/MM/YYYY'') - Doc_Date
                  ,B.Brn_No
                  ,B.Brn_Year
                  ,B.Cmp_No
                   ,B.Brn_Usr
                   ,Nvl(A.Credit_Period,0)
                    ,'''||V_Local_Cur||'''
                  ,'||V_FLD_CC_CODE||'
                  ,'||V_FLD_Pj_No||'
                  ,'||V_FLD_Actv_No||'
                  ,'||V_Sman_Grp||'
                  ,'||V_Cst_Grp||'  )
  select rn
      ,C_Code
      ,A_Cy
      ,Doc_No
      ,Doc_Type
      ,Jv_Type
      ,Doc_Ser
      ,Doc_Date
      ,Doc_Due_Date
      ,Cr_Amt
      ,Doc_Desc
      ,Ref_No
      ,Rcrd_No
      ,Cheque_Valued
      ,Per_No
      ,Brn_No
      ,Brn_Year
      ,Cmp_No
      ,Brn_Usr
      ,Local_Cur
      ,Cc_Code
      ,Pj_No
      ,Actv_No
      ,decode(Rep_Code,0,null,Rep_Code) Rep_Code
      ,Cst_Grp
      ,Doc_Dr_Amt
      ,Rt_Amt
      ,AC_Rate
      ,Bal
      ,Sum_Dr_Amt
      ,Sum_Cr_Amt
      ,Dr_Amt
      ,Blnc_Amt
      ,Sum (nvl(Dr_Amt,0)) Over (Partition By C_Code,A_Cy,Rep_Code,Cst_Grp  )SUM_DR_BY_CUR
      ,Prd
      ,'''||V_PRD_LBL||''' PRD_LBL
      ,CASE WHEN PER_NO BETWEEN 0 AND 30 THEN ROUND(DR_AMT,4) ELSE NULL END PRD_0_30
        ,CASE WHEN PER_NO BETWEEN 31 AND 60 THEN ROUND(DR_AMT,4) ELSE NULL END PRD_31_60
        ,CASE WHEN PER_NO BETWEEN 61 AND 90 THEN ROUND(DR_AMT,4) ELSE NULL END PRD_61_90
        ,CASE WHEN PER_NO BETWEEN 91 AND 120 THEN ROUND(DR_AMT,4) ELSE NULL END PRD_91_120
        ,CASE WHEN PER_NO >120 THEN ROUND(DR_AMT,4) ELSE NULL END PRD_MORE_120
      ,case when Credit_Period>0 and  Per_No >  Credit_Period then ROUND(DR_AMT,4)
            when    Credit_Period=0   then ROUND(DR_AMT,4)
            else 0 end Credit_Period_Amt
       ,case when Doc_Due_Date Is Not null  and  Doc_Due_Date<= '''||V_T_Date||''' then ROUND(DR_AMT,4)
             when    Doc_Due_Date Is null   then ROUND(DR_AMT,4)
             else 0 end Due_Date_Amt
from (
select m.*
,Greatest (Least (DOC_DR_AMT-nvl(Rt_Amt,0), Bal - sum_cr_amt), 0) DR_AMT
,(sum_dr_amt-sum_cr_amt) blnc_amt
,(case  when per_no between 0 and 30 then  ''0_30''
        when per_no between 31 and 60 then  ''31_60''
        when per_no between 61 and 90 then  ''61_90''
        when per_no between 91 and 120 then  ''91_120''
        else ''>120'' end) prd
from (
select m.*
,Sum (nvl(Doc_Dr_Amt,0)-Nvl(Rt_Amt,0)) Over (Partition By C_Code,A_Cy,Rep_Code,Cst_Grp order by rn )Bal
,Sum (nvl(Doc_Dr_Amt,0)-nvl(Rt_Amt,0)) Over (Partition By C_Code,A_Cy,Rep_Code,Cst_Grp  )sum_dr_amt
,Sum (Nvl(cr_Amt,0)) Over (Partition By C_Code,A_Cy,Rep_Code,Cst_Grp  )sum_cr_amt
 from (select  ROW_NUMBER() Over ( order by C_Code,A_Cy,Rep_Code,Cst_Grp, doc_date ,doc_ser)rn
          ,m.*
          from cst_tbl m
          ----- where ( Nvl (doc_Dr_Amt, 0)-Nvl (Rt_Amt, 0))>0
           )m
          )m
         where    (Nvl(sum_dr_amt,0)-nvl(sum_cr_amt,0))>0
Order By rn--C_Code, A_Cy, Doc_Date
)m
where   nvl(dr_amt,0)>0 '||P_WHR||'
Order By rn--C_Code, A_Cy, Doc_Date ' ;
--return V_Sql_Qry;


  ------------------------------------------------------------------------------------------
   EXECUTE IMMEDIATE V_Sql_Qry BULK COLLECT INTO Tp_Cst_Cr_Rcrd ;

    BEGIN
         -- FETCH V_Dstr_Cst_Dr_RFC BULK COLLECT INTO Tp_Blc_Rcrd;
         -- EXIT WHEN Tp_Blc_Rcrd.count=0;
          for idx in 1..Tp_Cst_Cr_Rcrd.count  loop
           PIPE ROW(Tp_Cst_Cr_Rcrd(idx));
           end loop;
     Exception  WHEN NO_DATA_FOUND THEN
           NULL;
      When NO_DATA_NEEDED Then
         RETURN;
     When Others Then
        Raise_Application_Error(-20006, 'Err When FETCH Tp_Cst_Cr_Rcrd DATA  '||Sqlerrm) ;
      End;
--------------------------------------------------------------------------
  --####################--

   <<Rtn_rslt>>
   If V_Msg_Txt Is Not Null Then
     Raise_Application_Error(-20105, 'Error ' ||V_Msg_Txt|| Chr(10) || Sqlerrm);
      -- V_Json_Rslt := Replace(V_Json_Rslt, '@DOC_NO', Null);
      --V_Json_Rslt := Replace(V_Json_Rslt, '@ERRNO', Nvl(V_Err_Line, '-1'));
      --V_Json_Rslt := Replace(V_Json_Rslt, '@ERRMSG', V_Msg_Txt);
      --Return V_Json_Rslt;
   End If;
--####################--
Exception
   When Others Then
   rollback;
      Raise_Application_Error(-20104, 'Error In CLC_CST_AGING.' || Chr(10) || Sqlerrm);
End CLC_CST_AGING;
--================================================================================---
Function Get_Dstr_Cst_Dr (    P_Sys_No            In Number default Null,
                               P_c_code            In Customer.C_Code%TYPE,
                               P_Doc_Date          In Date,
                               P_User_No           In Number,
                               P_Dr_Tbl_Nm         In varchar2  default Null,
                               P_Cr_Tbl_Nm         In varchar2  default Null,
                               P_Cur_Code          In varchar2 default Null,
                               P_Paid_By_local_cur In number default 0,
                               P_PREV_YEAR_FLG     In Number  default 0,
                               P_By_Sman           In Number  default 0,
                               P_Rep_Code          In Varchar2 Default Null,
                               P_F_CC_CODE         IN     IAS_POST_DTL.CC_CODE%TYPE  Default Null,
                               P_T_CC_CODE         IN     IAS_POST_DTL.CC_CODE%TYPE  Default Null,
                               P_F_PJ_NO           IN     IAS_POST_DTL.PJ_NO%TYPE  Default Null,
                               P_T_PJ_NO           IN     IAS_POST_DTL.PJ_NO%TYPE  Default Null,
                               P_F_ACTV_NO         IN     IAS_POST_DTL.ACTV_NO%TYPE  Default Null,
                               P_T_ACTV_NO         IN     IAS_POST_DTL.ACTV_NO%TYPE  Default Null ,
                               P_whr               In varchar2 default Null ,
                               P_whr_Dr            In varchar2 default Null ,
                               P_whr_Cr            In varchar2 default Null ,
                               P_Lng_No            In Number  default 1
                              ) RETURN TP_Dstr_Cst_Dr_TBL PIPELINED
Is
Pragma Autonomous_Transaction;
 V_Sql_Qry clob;
 V_Dstr_Cst_Dr_RFC      TP_Dstr_Cst_Dr_RFC;
 V_Local_Cur Varchar2(50);
 V_Aralt  Number;
 V_No_Of_Decimal  Number;
 V_Cstmr_Blnc_Type  Number(1);
-- V_Dstr_Cst_Dr_RFC      TP_Dstr_Cst_Dr_RFC;
 V_whr   Varchar2(4000):=P_whr ;
 V_Whr_Sman Varchar2(4000):=' ';
 V_whr_dr clob;
 V_whr_Cr   clob ;
 V_Dr_Qry   clob ;
 V_DOC_DATE  date;
 V_By_Sman   Number(1):=nvl(P_By_Sman,0);
-- V_rt_qry   varchar2(4000);
 v_fld_ser varchar2(500);
 V_Bill_Tbl varchar2(500);
 V_FLD_SMAN  varchar2(500):=' NULL  ';
 V_FLD_SMAN_INSTL varchar2(500);
 V_Paid_Instllmnt_Man  Number;
 V_Conn_Cst_Multi_Sman Number(1);
 V_frst_date   DATE := Ias_gen_pkg.Get_frst_day;
  V_tbl_rt_mst           VARCHAR2(500);
  V_tbl_rt_dtl           VARCHAR2(500);
  V_tbl_add_mst          VARCHAR2(500);
  V_tbl_add_dtl          VARCHAR2(500);

  V_Lng_No        Number:=NVL(P_LNG_NO,1);

  V_Dr_Tbl_Nm VARCHAR2(500):=nvl(P_Dr_Tbl_Nm,'INSTALLMENT');
  V_Cr_Tbl_Nm VARCHAR2(500):=nvl(P_Cr_Tbl_Nm,'IAS_POST_DTL');

   V_F_CC_CODE              IAS_POST_DTL.CC_CODE%TYPE:=P_F_CC_CODE;
   V_T_CC_CODE              IAS_POST_DTL.CC_CODE%TYPE :=P_T_CC_CODE;
   V_F_PJ_NO                IAS_POST_DTL.PJ_NO%TYPE  :=P_F_PJ_NO;
   V_T_PJ_NO                IAS_POST_DTL.PJ_NO%TYPE  :=P_T_PJ_NO ;
   V_F_ACTV_NO              IAS_POST_DTL.ACTV_NO%TYPE  :=P_F_ACTV_NO;
   V_T_ACTV_NO              IAS_POST_DTL.ACTV_NO%TYPE  :=P_T_ACTV_NO;
Begin


 Begin
   select Nvl(AR_AC_LINK_TYPE,2) ,Nvl(NO_OF_DECIMAL_AR,2),nvl(Paid_Instllmnt_Man,0), Nvl(Conn_Cst_Multi_Sman, 0)
    Into V_Aralt,V_No_Of_Decimal,V_Paid_Instllmnt_Man,V_Conn_Cst_Multi_Sman
   from ias_para_ar;
 End;



 V_Local_Cur:=IAS_GEN_PKG.GET_LOCAL_CUR;

------------------------------------------------------------------------
    If nvl( P_sys_no,0)=70 Or P_Rep_Code Is Not Null or Nvl(V_By_Sman,0)=1 Then
      V_Dr_Tbl_Nm :='IAS_POST_DTL';
      V_Cr_Tbl_Nm :='IAS_POST_DTL';

      If Nvl (P_Sys_No, 0) = 70 Then
          Begin
             V_Cstmr_Blnc_Type := Ias_Gen_Pkg.Get_Cnt ('Select NVL (CSTMR_BLNC_TYPE, 0) From DTS_PARA');
          Exception
             When Others Then
                V_Cstmr_Blnc_Type := 0;
          End;


          If Nvl(V_Cstmr_Blnc_Type,0)=0 Then

              If P_Rep_Code Is Not Null Then
                 V_Whr_Sman:=V_Whr_Sman||' and  rep_code='''||p_rep_code||''' ';
              End If;

              If V_Conn_Cst_Multi_Sman = 1  Then
                 V_whr :=V_whr|| ' And A.C_Code In (Select C_Code From Ias_Cst_Sman Where 1=1  ' || V_Whr_Sman || ')  ';
              Else
                  V_whr := V_whr||' And A.C_Code In (Select C_Code From Customer Where Rep_Code Is Not Null   ' || V_Whr_Sman || ')  ';
              End If;
              V_By_Sman:=0;
          Else
            V_By_Sman:=1;
          End if;
       End If;

        If Nvl(V_By_Sman,0)=1 Then
           V_FLD_SMAN :=' B.REP_CODE ';
           V_whr:=V_whr||' AND B.REP_CODE IS NOT NULL ' ;

           If P_Rep_Code Is Not Null Then
               V_whr   :=V_whr||'  AND B.REP_CODE='''||P_Rep_Code||''' ';
           End If;
        Else
          V_FLD_SMAN:=' NULL  ';
        End If;




    End if;
------------------------------------------------------------------------

 If P_C_code Is Not Null Then
    V_whr:=V_whr||' And A.C_Code='''||P_C_code||''' ';
 End if;
 ------------------------------------------------------------------------

 ------------------------------------------------------------------------
  If P_Cur_Code Is Not Null Then
    V_whr:=V_whr||' And B.A_CY  ='''||P_Cur_Code||''' ';
 End if;
 ------------------------------------------------------------------------
 If nvl(P_User_No,0)<>1 Then
    If Nvl(V_Aralt ,0)=1 Then
      V_Whr:=V_whr ||'  And Exists (Select 1
                                        From Priv_Acc
                                       Where U_Id ='|| P_USER_NO||'
                                             And A_Code = A.C_A_Code
                                             And A_Cy = B.A_Cy
                                             And Nvl(Add_Flag, 0) = 1
                                             And Rownum <= 1)  ';
    ElsIf Nvl(V_Aralt ,0)=2 Then
      V_Whr:=V_whr ||'   And Exists
                            (Select 1
                               From Ias_Priv_Customer
                              Where U_Id = '|| P_USER_NO||'
                                    And C_Code = A.C_Code
                                    And A_Cy = B.A_Cy
                                    And Nvl(Add_Flag, 0) = 1
                                    And Rownum <= 1) ';
    End if;

     V_Whr := V_Whr || ' and Exists(Select 1
                 From   S_brn_usr_priv
                 Where  U_id = '||P_User_No ||'
                 And S_brn_usr_priv.Brn_no = b.Brn_no
                  And Nvl(View_Flag, 1) = 1
                   And Rownum <= 1)  ';
 End If;
 ------------------------------------------------------------------------
  If P_Doc_Date Is Not Null Then
      V_Doc_date:=P_Doc_Date;
   Else
      V_Doc_date:=To_Date(sysdate ,'DD/MM/RRRR');
   End if;
 ------------------------------------------------------------------------
 --------------------------------------------------------
   --## CC_Code
   If V_F_CC_Code Is Null And V_T_CC_Code Is Not Null Then
      V_F_CC_Code := V_T_CC_Code;
   Elsif V_F_CC_Code Is Not Null  And V_T_CC_Code Is Null Then
      V_T_CC_Code := V_F_CC_Code;
   End If;


   If V_F_CC_Code Is Not Null Then
     Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   =>V_F_CC_Code,
                                       P_TN   =>V_T_CC_Code,
                                       P_Type => 'C') ;

      V_whr := V_whr || ' And B.CC_Code Between ''' || V_F_CC_Code || '''  And  ''' || V_T_CC_Code || '''  ';
   End If;
   ------------------------------------------------------------------
   --## PJ_NO
   If V_F_PJ_NO Is Null And V_T_PJ_NO Is Not Null Then
      V_F_PJ_NO := V_T_PJ_NO;
   Elsif V_F_PJ_NO Is Not Null  And V_T_PJ_NO Is Null Then
      V_T_PJ_NO := V_F_PJ_NO;
   End If;


   If V_F_PJ_NO Is Not Null Then
     Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   =>V_F_PJ_NO,
                                       P_TN   =>V_T_PJ_NO,
                                       P_Type => 'C') ;

      V_whr := V_whr || ' And B.PJ_NO Between ''' || V_F_PJ_NO || '''  And  ''' || V_T_PJ_NO || '''  ';
   End If;
   ------------------------------------------------------------------
   --## ACTV_NO
   If V_F_ACTV_NO Is Null And V_T_ACTV_NO Is Not Null Then
      V_F_ACTV_NO := V_T_ACTV_NO;
   Elsif V_F_ACTV_NO Is Not Null  And V_T_ACTV_NO Is Null Then
      V_T_ACTV_NO := V_F_ACTV_NO;
   End If;


   If V_F_ACTV_NO Is Not Null Then
     Ias_Check_Sys_Pkg.Check_Bt_Value (P_FN   =>V_F_ACTV_NO,
                                       P_TN   =>V_T_ACTV_NO,
                                       P_Type => 'C') ;

      V_whr := V_whr || ' And B.ACTV_NO Between ''' || V_F_ACTV_NO || '''  And  ''' || V_T_ACTV_NO || '''  ';
   End If;
   ------------------------------------------------------------------
  V_whr_dr:=V_whr||p_whr_dr ;
  V_whr_Cr:=V_whr||p_whr_Cr ;
   ------------------------------------------------------------------------
    If Upper(trim(V_Dr_Tbl_Nm)) In('IAS_V_POST_DTL_YR','INSTALLMENT_YR') Then
        V_tbl_rt_mst    := 'IAS_RT_BILL_MST';
        V_tbl_rt_dtl    := 'IAS_RT_BILL_Dtl';
        V_tbl_add_mst   := 'IAS_BILL_MST_ADD_DISC';
        V_tbl_add_dtl   := 'IAS_BILL_DTL_ADD_DISC';
    ELSE
        V_tbl_rt_mst    := 'IAS_V_RT_BILL_MST_YR';
        V_tbl_rt_dtl    := 'IAS_V_RT_BILL_Dtl_YR';
        V_tbl_add_mst   := 'IAS_V_BILL_MST_ADD_DISC_YR';
        V_tbl_add_dtl   := 'IAS_V_BILL_DTL_ADD_DISC_YR';
    END IF;
------------------------------------------------------------------------
 If Nvl(V_Paid_Instllmnt_Man,0)=0 Or Nvl(V_By_Sman,0)=1 Then
         If Upper(trim(V_Dr_Tbl_Nm)) In('INSTALLMENT','INSTALLMENT_YR')Then
           v_fld_ser:='b.bill_ser';
         Else
          v_fld_ser:='b.doc_ser';
         End if;

         If Upper(trim(V_Dr_Tbl_Nm)) In('INSTALLMENT','INSTALLMENT_YR')Then
                 V_whr_Cr:=V_whr_Cr||' and (doc_type<>0 or Not Exists ( Select 1
                                                From Installment
                                                            Where c_code   = b.ac_code_dtl
                                                              and doc_date< TO_DATE('''||V_frst_date||''',''DD/MM/RRRR'')
                                                              And RowNum  <= 1 )) ';




              V_FLD_SMAN_INSTL:=' NULL REP_CODE ';


          V_Dr_Qry:=' Select B.C_Code,
                                        B.A_Cy,
                                        B.Bill_No DOC_NO,
                                        B.Doc_Type,
                                        B.Bill_Doc_Type,
                                        B.Bill_Ser Doc_Ser,
                                        B.I_No,
                                        B.Doc_Date,
                                        Case When nvl(:P_PAID_BY_LOCAL_CUR,0)=0 Then B.A_Cy Else :V_LOCAL_CUR End Cur_code,
                                        Decode(P.Chk_crdt_prd_typ,1,Decode(A.Credit_period, Null, B.I_date, Decode(B.Doc_date, Null, B.I_date, B.Doc_date + A.Credit_period)),B.I_date) I_date,
                                        Nvl(B.I_Amt, 0) I_Amt2,
                                         ( SUM(Nvl(B.I_Amt, 0))Over(Partition By B.Brn_Year,b.C_Code,B.A_Cy,B.Bill_Ser order by B.Brn_Year, b.C_Code,B.A_Cy,b.I_Date,B.I_No   Rows Unbounded Preceding )
                                                         - (nvl(rt.Rt_Amt,0)) )sum_Amt,
                                        (nvl(rt.Rt_Amt,0))  Rt_Amt,
                                        B.Ac_Rate,
                                        B.Pj_No,
                                        B.Actv_No,
                                        NVL(B.Rcrd_No,0)Rcrd_No,
                                       '|| V_FLD_SMAN_INSTL ||',
                                        B.Brn_No,
                                        B.Brn_Year,
                                        B.Cmp_No,
                                        B.Brn_Usr
                                   From Customer A, '||V_Dr_Tbl_Nm||'  B ,IAS_PARA_AR P,(select bill_ser, sum(Rt_Amt) Rt_Amt
                                                                                                            from Rt_Qry
                                                                                                            group by bill_ser ) Rt
                                  Where A.C_Code = B.C_Code
                                         And A.C_A_Code = B.A_Code
                                         and B.Bill_Ser=Rt.bill_ser(+)
                                         And B.Dr_No Is Null  '||V_whr_dr||' ';
         Else
            If Nvl(V_By_Sman,0)=1 Then
                V_whr_dr:=V_whr_dr|| 'AND B.REP_CODE IS NOT NULL ' ;
            End If;

            If P_Rep_Code Is Not Null Then
                   V_whr_dr   :=V_whr_dr||'  AND B.REP_CODE='''||P_Rep_Code||''' ';
                    V_whr_Cr   :=V_whr_Cr||'  AND B.REP_CODE='''||P_Rep_Code||''' ';
            End If;

          V_Dr_Qry:=' select M.*
                ,Decode(nvl(dr_Amt_F,0),0,1,(nvl(dr_Amt,0)/nvl(dr_Amt_F,0))) Ac_Rate
                ,decode(:V_Local_Cur,a_cy,dr_Amt-rt_amt,nvl(dr_Amt_F,0)-rt_amt) I_Amt2
                ,decode(:V_Local_Cur,a_cy,dr_Amt-rt_amt,nvl(dr_Amt_F,0)-rt_amt) sum_Amt
           from (
              Select a.C_Code,
                    B.A_Cy,
                    B.DOC_NO ,
                    B.Doc_Type,
                    B.jv_type Bill_Doc_Type,
                    B.Doc_Ser,
                    1 I_No,
                    B.Doc_Date,
                    Case When nvl(:P_PAID_BY_LOCAL_CUR,0)=0 Then B.A_Cy Else :V_LOCAL_CUR End Cur_code,
                    Decode(P.Chk_crdt_prd_typ,1,Decode(A.Credit_period, Null, nvl(B.DOC_DUE_DATE,b.doc_date), Decode(B.Doc_date, Null, B.DOC_DUE_DATE, B.Doc_date + A.Credit_period)),nvl(B.DOC_DUE_DATE,b.doc_date)) I_date,
                    sum(Nvl(b.dr_Amt,0) ) dr_Amt,
                    sum(Nvl(b.dr_Amt_f,0) ) dr_Amt_f,
                    sum(nvl(Rt.Rt_Amt,0)) rt_amt  ,
                    null Pj_No,
                    null Actv_No,
                    NVL(B.Rcrd_No,0)Rcrd_No,
                    '||V_FLD_SMAN||' REP_CODE,
                    B.Brn_No,
                    B.Brn_Year,
                    B.Cmp_No,
                    B.Brn_Usr
               From Customer A, '||V_Dr_Tbl_Nm||'   B,IAS_PARA_AR P,(select bill_ser, sum(Rt_Amt) Rt_Amt
                                                                            from Rt_Qry
                                                                            group by bill_ser ) Rt
               Where  A.C_Code   = B.Ac_Code_Dtl
                      And A.C_A_Code = B.A_Code
                      And B.Ac_Dtl_Typ=3
                      and b.doc_ser=rt.bill_ser(+)
                      And B.Ac_Code_Dtl Is Not Null
                      And b.doc_date  <=:V_DOC_DATE
                      and decode(:V_LOCAL_CUR,b.a_cy,b.Dr_Amt,nvl(b.Dr_Amt_F,0))>0  '||V_whr_dr|| '
              group by
                   a.C_Code,
                    B.A_Cy,
                    B.DOC_NO ,
                    B.Doc_Type,
                    B.jv_type ,
                    B.Doc_Ser,
                    B.Doc_Date,
                    Decode(P.Chk_crdt_prd_typ,1,Decode(A.Credit_period, Null, nvl(B.DOC_DUE_DATE,b.doc_date), Decode(B.Doc_date, Null, B.DOC_DUE_DATE, B.Doc_date + A.Credit_period)),nvl(B.DOC_DUE_DATE,b.doc_date)),
                    NVL(B.Rcrd_No,0),
                    '||V_FLD_SMAN||',
                    B.Brn_No,
                    B.Brn_Year,
                    B.Cmp_No,
                    B.Brn_Usr )M
                     Order By C_Code ,REP_CODE,Cur_code,I_Date,Doc_Type,doc_ser,Doc_no,I_No,Rcrd_No ';
         End if;

         V_Sql_Qry:=' with
                      Rt_Qry as( Select nvl(Sum(Dtl_Amt * Per_Amt),0) Rt_Amt,Bill_Ser,rt_Bill_Ser
                                      From (
                                      Select       rt_Bill_no,
                                                   rt_Bill_Ser,
                                                   Bill_Ser,
                                                   bill_no,
                                                   Cc_Code,
                                                   Pj_No,
                                                   Actv_No,
                                                   Rt_Bill_Date,
                                                   Rt_Bill_Rate,
                                                   (Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser ) * Decode(decode(RT_BILL_CURRENCY,:V_LOCAL_CUR,1,0),1,Nvl(Rt_Bill_Rate,1),1)  )bill_amt,
                                                   Ac_Amt,
                                                   Dtl_Amt,
                                                    case when Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)>0 then ((Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)- Ac_Amt)/Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser) )else 0 end Per_Amt
                                              From (Select m.rt_Bill_no,
                                                           m.rt_Bill_Ser,
                                                           M.RT_BILL_CURRENCY,
                                                           Bill_Ser,
                                                           bill_no,
                                                           D.Cc_Code,
                                                           D.Pj_No,
                                                           D.Actv_No,
                                                           M.Rt_Bill_Date,
                                                           M.Rt_Bill_Rate,
                                                           Nvl((Nvl(D.I_Qty, 0) * (Nvl(D.I_Price, 0) - Nvl(D.Dis_Amt, 0) + Nvl(D.Vat_Amt, 0) + Nvl(D.Othr_Amt, 0))), 0) Dtl_Amt,
                                                           ((Nvl(M.Cr_Card_Amt, 0) + Nvl(M.Cr_Card_Amt_Scnd, 0) + Nvl(M.Cr_Card_Amt_Thrd, 0)) + Nvl(M.Ac_Amt, 0)) Ac_Amt
                                                      From '||V_tbl_rt_mst||' M, '||V_tbl_rt_Dtl||' D
                                                     Where M.Rt_Bill_Ser = D.Rt_Bill_Ser
                                                           And M.Rt_Bill_Doc_Type = 4
                                                           And M.P_Year In (0, 3)
                                                           and rt_bill_date      <=:V_DOC_DATE
                                                           And D.bill_ser Is Not Null
                                                           Union ALL
                                            Select m.DOC_NO  rt_Bill_no,
                                                   m.DOC_SER rt_Bill_Ser,
                                                   M.A_CY RT_BILL_CURRENCY,
                                                   D.Bill_Ser,
                                                   D.bill_no,
                                                   M.Cc_Code,
                                                   M.Pj_No,
                                                   M.Actv_No,
                                                   M.DOC_DATE Rt_Bill_Date,
                                                   M.DOC_RATE Rt_Bill_Rate,
                                                   Nvl(D.ADD_DIS_QTY, 0) * Nvl(D.ADD_DIS_AMT_DTL, 0)+(Nvl(D.Add_Dis_Qty,0)*Nvl(D.ADD_VAT_AMT,0)) Dtl_Amt,
                                                   0 Ac_Amt
                                              From ' || V_tbl_add_mst || ' M, '|| V_tbl_add_dtl || ' D
                                             Where M.DOC_SER = D.DOC_SER AND NVL(NOTE_TYP,0)=1
                                                   And M.BILL_DOC_TYPE = 4
                                                   and M.DOC_DATE      <=:V_DOC_DATE
                                                           ))
                                                           group by Bill_Ser,rt_Bill_Ser
                                )
                     , Cst_Dr as( Select M.*
                                       , Sum(I_Amt_Clc )over(partition by Brn_Year,C_Code,REP_CODE,Cur_code order by Rn_Dr) sum_dr_amt
                                       , Nvl(Sum(I_Amt_Clc )over(partition by Brn_Year,C_Code,Cur_code order by Rn_Dr  Rows Between Unbounded Preceding And 1 Preceding ),0) sum_dr_amt_prv
                                       From(  Select
                                                       Row_Number()over( order by Brn_Year,C_Code,Cur_code,I_Date,Doc_Type,DOC_ser,DOC_no,I_No,RCRD_NO ) Rn_Dr
                                                     , M.*
                                                     , least(I_Amt2,sum_Amt)  I_Amt
                                                     , (least(I_Amt2,sum_Amt)* Nvl(Ac_Rate, 1))  I_Amt_Loc
                                                     , Case When nvl(:P_PAID_BY_LOCAL_CUR,0)=0 Then least(I_Amt2,sum_Amt) Else least(I_Amt2,sum_Amt)* Nvl(Ac_Rate, 1) End I_Amt_Clc
                                                 From (' ||V_DR_QRY ||')M
                                                    where least(I_Amt2,sum_Amt)>0
                                                     Order By Brn_Year,C_Code,REP_CODE,Cur_code,I_Date,Doc_Type,DOC_ser,DOC_no,I_No,RCRD_NO
                                                     ) M
                                                 order by Rn_Dr )
                   , Cst_Cr as( Select  M.*
                                       ,Sum(Cr_Amt_Clc)over(partition by Brn_Year,C_Code,REP_CODE,Cur_code order by Rn_Cr) sum_cr_amt
                                       ,Sum(Cr_Amt_Clc)over(partition by Brn_Year,C_Code,REP_CODE,Cur_code ) SMCR
                                         from (  Select M.*
                                                       ,Row_Number()over( order By Brn_Year, C_Code,REP_CODE,Cur_code,Paid_Date,PAID_SER,RCRD_NO) Rn_Cr
                                                       , Case When nvl(:P_PAID_BY_LOCAL_CUR,0)=0 Then Cr_Amt Else Cr_Amt* Nvl(Paid_Ac_Rate,1) End Cr_Amt_Clc
                                                  From  ( Select b.doc_ser paid_ser
                                                                ,b.doc_no paid_no
                                                                ,A.C_Code
                                                                ,Case When nvl(:P_PAID_BY_LOCAL_CUR,0)=0 Then B.A_Cy Else :V_LOCAL_CUR End Cur_code
                                                               ,b.a_cy Paid_A_Cy
                                                               ,b.Doc_Date paid_date
                                                               ,B.Doc_type Paid_Doc_Type
                                                               ,NVL(B.RCRD_NO,0)RCRD_NO
                                                               ,'||V_FLD_SMAN||  ' REP_CODE
                                                               ,b.Brn_Year
                                                               , B.BRN_USR
                                                              , B.BRN_NO
                                                              ,B.CMP_NO
                                                               ,SUM(decode(:V_LOCAL_CUR,b.a_cy,b.Cr_Amt,nvl(b.Cr_Amt_F,0))) Cr_Amt
                                                               ,AVG(Decode(nvl(b.Cr_Amt_F,0),0,1,(nvl(b.Cr_Amt,0)/nvl(b.Cr_Amt_F,0)))) Paid_Ac_Rate
                                                          From customer a,'||V_Cr_Tbl_Nm||'  b
                                                               Where A.C_Code   = B.Ac_Code_Dtl
                                                                  And A.C_A_Code = B.A_Code
                                                                  And B.Ac_Dtl_Typ=3
                                                                  And B.Ac_Code_Dtl Is Not Null
                                                                  And b.doc_date  <=:V_DOC_DATE
                                                                  and b.doc_ser not in(select rt_bill_ser from Rt_Qry)
                                                                  and decode(:V_LOCAL_CUR,b.a_cy,b.Cr_Amt,nvl(b.Cr_Amt_F,0))>0 '||V_whr_Cr||'
                                                            Group By
                                                                b.doc_ser
                                                                ,b.doc_no
                                                                ,A.C_Code
                                                               ,b.a_cy
                                                               ,b.Doc_Date
                                                               ,B.Doc_type
                                                               ,NVL(B.RCRD_NO,0)
                                                               ,'||V_FLD_SMAN||  '
                                                               ,b.Brn_Year
                                                               , B.BRN_USR
                                                              , B.BRN_NO
                                                              ,B.CMP_NO
                                                          Order By A.C_Code,'||V_FLD_SMAN||',b.a_cy,b.Doc_Date, B.Doc_Ser
                                                          ) M
                     ORDER BY C_Code,REP_CODE,CUR_CODE,paid_date,PAID_SER
                         )M
                     order BY Rn_Cr
             )
         ,Rcrsv as(
         select M.*
            ,Case When A_CY=CUR_CODE Then Nvl(PAID_AMT2,0) ELSE round(Nvl(PAID_AMT2,0)/Nvl(Ac_Rate,1),:V_NO_OF_DECIMAL) End PAID_AMT
            ,Case When  A_CY=CUR_CODE Then Nvl(Ac_Rate,1)*Nvl(PAID_AMT2,0)  ELSE Nvl(PAID_AMT2,0)   End PAID_AMT_LOC
           From (
           Select M.*
               , greatest(least(I_Amt_Clc- nvl(sum(greatest(least(I_Amt_Clc,least((sum_cr_amt-sum_dr_amt_prv),CR_AMT_clc)),0))
                                    over(partition by  Rn_Dr
                                         order by Rn_Dr ,Rn_cr rows between unbounded preceding and 1 preceding),0)
                                 ,least((sum_cr_amt-sum_dr_amt_prv),CR_AMT_clc)),0) paid_amt2
                from (
                 select       R.Rn_Dr  ,
                              r.C_Code,
                              r.REP_CODE,
                              r.Brn_Year,
                              r.A_Cy,
                              R.Cur_code,
                              r.I_Amt,
                              r.I_Amt_Loc,
                              r.I_Amt_Clc,
                              c.paid_ser ,
                              c.paid_no,
                              c.paid_date,
                              C.Paid_A_Cy,
                              c.Paid_Doc_Type,
                              c.Paid_Ac_Rate,
                              r.Ac_Rate,
                              c.cr_amt,
                              c.CR_AMT_clc,
                              r.sum_dr_amt,
                              r.sum_dr_amt_prv,
                              c.sum_cr_amt ,
                              SMCR,
                              C.Rn_cr ,
                              R.Rt_Amt
        from   Cst_Dr r,cst_cr c
        where r.c_code=c.c_code
         AND NVL(R.REP_CODE,''0'')=NVL(C.REP_CODE,''0'')
        and r.Cur_code=c.Cur_code
        -----and r.Brn_Year=c.Brn_Year
        and nvl(c.sum_cr_amt,0)-nvl(r.sum_dr_amt_prv,0) >0
        ORDER BY Rn_Dr,Rn_Cr)M
        order By  Rn_Dr,Rn_Cr
         ) M
         where Nvl(paid_amt2,0)>0
          )
         SELECT RN_DR RN,
                M.C_CODE             ,
                M.A_CY   ,
                M.CUR_CODE,
                M.REP_CODE  ,
                M.DOC_NO            ,
                M.DOC_TYPE          ,
                M.BILL_DOC_TYPE        ,
                M.DOC_SER             ,
                M.I_NO               ,
                M.DOC_DATE         ,
                M.BILL_DATE       ,
                M.Rt_Amt  ,
                M.I_AMT               ,
                M.BILL_RATE         ,
                M.PAID_AMT,
                M.SUM_PAID_DOC      ,
                CASE WHEN (NVL(I_AMT,0)-NVL(SUM_PAID_DOC,0))<> NVL(LAG(NVL(I_AMT,0)-NVL(SUM_PAID_DOC,0))OVER( PARTITION BY M.C_CODE,M.REP_CODE,M.CUR_CODE,M.RN_DR ORDER BY M.RN_DR),0)
                           THEN  (NVL(I_AMT,0)-NVL(SUM_PAID_DOC,0)) ELSE 0 END REM_AMT ,
                M.MAX_PAID_DATE,
                M.PAID_DATE         ,
                M.PAID_SER           ,
                M.PAID_NO           ,
                M.PAID_A_CY,
                M.PAID_DOC_TYPE,
                M.PAID_AC_RATE,
                M.TRMNL_NAME        ,
                M.PJ_NO           ,
                M.ACTV_NO          ,
                M.RCRD_NO          ,
                M.BRN_NO           ,
                M.BRN_YEAR          ,
                M.CMP_NO            ,
                M.BRN_USR   ,
               CASE WHEN  NVL(SUM_PAID_DOC,0)=0 THEN 2
                     WHEN NVL(SUM_PAID_DOC,0)=NVL(I_AMT,0)THEN 1
                     WHEN NVL(SUM_PAID_DOC,0)<NVL(I_AMT,0)THEN 3
                      ELSE 4 END PAID ,
               (Select Doc_Type_Name
              From Ias_Sys.Ias_Docjv_Type_Systems_Mst
             Where Lang_No = '||V_Lng_No||'  And Doc_Type = M.Doc_Type And Rownum <= 1) DOC_TYPE_NM    ,
               (Select Flg_Desc
                From S_Flags
               Where     Flg_Code = ''TYPE_NAME''
                     And Lang_No = '||V_Lng_No||'
                     And Flg_Value = M.Bill_Doc_Type
                     And Rownum <= 1) BILL_DOC_TYPE_NM    ,
               (Select Doc_Type_Name
              From Ias_Sys.Ias_Docjv_Type_Systems_Mst
             Where Lang_No = '||V_Lng_No||'  And Doc_Type = M.PAID_DOC_TYPE And Rownum <= 1) Paid_Doc_Type_NM,
             (Select Decode ('||V_Lng_No||',1, Nvl (C_A_Name, C_E_Name),Nvl (C_E_Name, C_A_Name))
                From Customer
               Where C_Code = M.C_Code And Rownum <= 1)
             C_NAME
          FROM (SELECT
                A.C_CODE             ,
                A.A_CY   ,
                A.CUR_CODE,
                A.REP_CODE,
                A.DOC_NO            ,
                A.DOC_TYPE          ,
                A.BILL_DOC_TYPE BILL_DOC_TYPE       ,
                A.DOC_SER             ,
                A.I_NO               ,
                A.DOC_DATE         ,
                A.I_DATE BILL_DATE       ,
                A.I_AMT               ,
                A.I_AMT_LOC          ,
                A.AC_RATE BILL_RATE         ,
                B.PAID_AMT,
                B.PAID_AMT_LOC                  ,
                SUM(PAID_AMT)OVER (PARTITION BY B.C_CODE,B.REP_CODE,B.CUR_CODE,B.RN_DR) SUM_PAID_DOC,
                SUM(PAID_AMT_LOC)OVER (PARTITION BY B.C_CODE,B.REP_CODE,B.CUR_CODE,B.RN_DR) SUM_PAID_DOC_LOC,
                MAX(PAID_DATE)OVER (PARTITION BY B.C_CODE,B.REP_CODE,B.CUR_CODE,B.RN_DR) MAX_PAID_DATE,
                B.PAID_DATE         ,
                B.PAID_SER           ,
                B.PAID_NO           ,
                B.PAID_A_CY,
                B.PAID_DOC_TYPE,
                B.PAID_AC_RATE,
                NULL TRMNL_NAME        ,
                A.PJ_NO           ,
                A.ACTV_NO          ,
                A.RCRD_NO          ,
                A.BRN_NO           ,
                A.BRN_YEAR          ,
                A.CMP_NO            ,
                A.BRN_USR   ,
                B.CR_AMT         ,
                A.SUM_DR_AMT    ,
                A.SUM_DR_AMT_PRV  ,
                B.SUM_CR_AMT,
                B.SMCR,
                B.SUM_PAID ,
                A.Rt_Amt,
                A.RN_DR,
                NULL RN_CR
         FROM CST_DR A ,(SELECT RCRSV.*
            ,SUM( NVL(PAID_AMT,0)   )
                  OVER (PARTITION BY BRN_YEAR,C_CODE,REP_CODE,CUR_CODE)  SUM_PAID
                  FROM RCRSV) B
        WHERE A.RN_DR=B.RN_DR(+)
        union all
        SELECT
                A.C_CODE             ,
                A.PAID_A_CY A_CY   ,
                A.CUR_CODE,
                A.REP_CODE,
                null DOC_NO            ,
                null DOC_TYPE          ,
                null  BILL_DOC_TYPE       ,
                null DOC_SER             ,
                null I_NO               ,
                null DOC_DATE         ,
                null  BILL_DATE       ,
                0 I_AMT               ,
                0 I_AMT_LOC          ,
                null BILL_RATE         ,
                nvl(a.CR_AMT_CLC,0) -nvl(B.PAID_AMT,0)PAID_AMT ,
                nvl(a.CR_AMT_CLC,0) -nvl(B.PAID_AMT_LOC,0)PAID_AMT_LOC                    ,
                nvl(a.CR_AMT_CLC,0) -nvl(B.PAID_AMT,0) SUM_PAID_DOC,
                nvl(a.CR_AMT_CLC,0) -nvl(B.PAID_AMT_LOC,0)  SUM_PAID_DOC_LOC,
                A.PAID_DATE MAX_PAID_DATE,
                A.PAID_DATE         ,
                A.PAID_SER           ,
                A.PAID_NO           ,
                A.PAID_A_CY,
                A.PAID_DOC_TYPE,
                A.PAID_AC_RATE,
                NULL TRMNL_NAME        ,
                NULL PJ_NO           ,
                NULL ACTV_NO          ,
                A.RCRD_NO          ,
                A.BRN_NO           ,
                A.BRN_YEAR          ,
                A.CMP_NO            ,
                A.BRN_USR   ,
                A.CR_AMT         ,
                NULL SUM_DR_AMT    ,
                NULL SUM_DR_AMT_PRV  ,
                A.SUM_CR_AMT,
                A.SMCR,
                0 SUM_PAID,
                0 Rt_Amt,
                 TO_NUMBER(RPAD(A.RN_CR ,10,1)) RN_DR,
                 A.RN_CR
         FROM CST_CR A ,(SELECT RN_CR,BRN_YEAR,C_CODE,REP_CODE,CUR_CODE,PAID_SER
            ,SUM( NVL(PAID_AMT,0)   ) PAID_AMT
            ,SUM( NVL(PAID_AMT_LOC,0)   ) PAID_AMT_LOC
                  FROM RCRSV
                  WHERE PAID_SER IS NOT NULL
                  GROUP BY
                  RN_CR,BRN_YEAR,C_CODE,REP_CODE,CUR_CODE,PAID_SER ) B
        WHERE A.RN_CR=B.RN_CR(+)
        AND nvl(a.CR_AMT_CLC,0) -nvl(B.PAID_AMT,0)>0
         ) M
         ORDER BY BRN_YEAR,CUR_CODE,REP_CODE,C_CODE, RN_DR';


Else
      V_FLD_SMAN_INSTL:=' NULL REP_CODE ';
  V_Sql_Qry:=' Select B.RCRD_NO,
                        B.C_CODE             ,
                        B.A_CY   ,
                        B.A_CY  CUR_CODE ,
                        '||V_FLD_SMAN_INSTL||' ,
                        B.BILL_NO DOC_NO            ,
                        B.DOC_TYPE          ,
                        B.Bill_doc_type        ,
                        B.BILL_SER DOC_SER             ,
                        B.I_NO               ,
                        B.DOC_DATE         ,
                        B.I_DATE BILL_DATE       ,
                        0 RT_AMT,
                        B.I_AMT ,
                        NULL BILL_RATE         ,
                        B.PAID_AMT,
                        B.PAID_AMT SUM_PAID_DOC      ,
                        nvl(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0) REM_AMT ,
                        NULL MAX_PAID_DATE,
                        B.PAID_DATE         ,
                        NULL PAID_SER           ,
                        NULL PAID_NO           ,
                        NULL Paid_A_Cy,
                        NULL Paid_Doc_Type,
                        NULL Paid_Ac_Rate,
                        NULL TRMNL_NAME        ,
                        B.PJ_NO           ,
                        B.ACTV_NO          ,
                        B.RCRD_NO          ,
                        B.BRN_NO           ,
                        B.BRN_YEAR          ,
                        B.CMP_NO            ,
                        B.BRN_USR   ,
                       case when  nvl(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0)=0 then 2
                             when nvl(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0)=nvl(B.I_AMT,0)then 1
                             when nvl(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0)<nvl(B.I_AMT,0)then 3
                              else 0 end PAID,
                                 (Select Doc_Type_Name
              From Ias_Sys.Ias_Docjv_Type_Systems_Mst
             Where Lang_No = '||V_Lng_No||'  And Doc_Type = B.Doc_Type And Rownum <= 1) DOC_TYPE_NM    ,
               (Select Flg_Desc
                From S_Flags
               Where     Flg_Code = ''TYPE_NAME''
                     And Lang_No = '||V_Lng_No||'
                     And Flg_Value = B.Bill_Doc_Type
                     And Rownum <= 1) BILL_DOC_TYPE_NM    ,
                     NULL Paid_Doc_Type_NM ,
                     Decode ('||V_Lng_No||',1, Nvl (C_A_Name, C_E_Name),Nvl (C_E_Name, C_A_Name)) C_NAME
                    FROM INSTALLMENT  B,Customer A
                       Where A.C_Code = B.C_Code
                       And A.C_A_Code = B.A_Code '||V_whr_dr;
End If;
V_Sql_Qry:=UPPER(V_Sql_Qry);
V_Sql_Qry:=Replace (V_Sql_Qry,':P_PAID_BY_LOCAL_CUR',nvl(P_PAID_BY_LOCAL_CUR,0));
V_Sql_Qry:=Replace (V_Sql_Qry,':V_DOC_DATE',''''||V_DOC_DATE||'''');
V_Sql_Qry:=Replace (V_Sql_Qry,':V_LOCAL_CUR',''''||V_LOCAL_CUR||'''');
V_Sql_Qry:=Replace (V_Sql_Qry,':V_NO_OF_DECIMAL',nvl(V_NO_OF_DECIMAL,2));
V_Sql_Qry:=Replace (V_Sql_Qry,':P_PREV_YEAR_FLG',nvl(P_PREV_YEAR_FLG,0));




 OPEN V_Dstr_Cst_Dr_RFC FOR(V_Sql_Qry);

  --OPEN V_Dstr_Cst_Dr_RFC FOR(V_Sql_Qry)  ;


 -- EXECUTE IMMEDIATE V_Sql_Qry BULK COLLECT INTO Tp_Blc_Rcrd ;


 OPEN V_Dstr_Cst_Dr_RFC FOR(V_Sql_Qry);
              LOOP
                 BEGIN
                      FETCH V_Dstr_Cst_Dr_RFC INTO G_Dstr_Cst_Dr_REC;
                      EXIT WHEN V_Dstr_Cst_Dr_RFC%NOTFOUND;
                       PIPE ROW(G_Dstr_Cst_Dr_REC);
                 Exception  WHEN NO_DATA_FOUND THEN
                       RETURN;
                  WHEN NO_DATA_NEEDED THEN
                      RETURN;
                 When Others Then
                   Raise_Application_Error(-20007, 'Err When FETCH Dstr_Cst_Dr_RFC DATA  '||Sqlerrm) ;
                 End;
               END LOOP;
               CLOSE V_Dstr_Cst_Dr_RFC;
               RETURN;


    /*BEGIN
         FETCH V_Dstr_Cst_Dr_RFC BULK COLLECT INTO Tp_Blc_Rcrd;
         -- EXIT WHEN Tp_Blc_Rcrd.count=0;
          for idx in 1..Tp_Blc_Rcrd.count  loop
           PIPE ROW(Tp_Blc_Rcrd(idx));
           end loop;
     Exception  WHEN NO_DATA_FOUND THEN
           NULL;
      When NO_DATA_NEEDED Then
         RETURN;
     When Others Then
   --  close V_Dstr_Cst_Dr_RFC;
        Raise_Application_Error(-20006, 'Err When FETCH Dstr_Cst_Dr_RFC DATA  '||Sqlerrm) ;
      End;
     --  close Tp_Blc_Rcrd;*/

End Get_Dstr_Cst_Dr;
--================================================================================---
FUNCTION GET_SMAN_DATA ( P_REP_CODE     IN VARCHAR2
                         ,P_Lng_No       In     Number Default 1 ) RETURN clob
Is
V_Err_No               Number;
V_Msg_Txt              Varchar2 (1000);
 V_Json_Rslt            Varchar2 (4000) := '{"_Result": { "_ErrMsg": "@ERRMSG","_ErrNo": @ERRNO } }';
 V_Qry  clob;
 Qry_Rslt clob;
begin

   If P_Rep_Code Is Null Then
      V_Err_No := $$plsql_Line;
      V_Msg_Txt := Ias_Gen_Pkg.Get_Msg (P_Lng_No => P_Lng_No, P_Msg_No => 811);
      Goto Rtn_Rslt;
   End If;
   -----------------------------------
   V_Qry:='Select S.Reprs_Code Rep_code
          ,DECODE (  '||P_LNG_NO||' , 1, NVL (S.Reprs_A_Name, S.Reprs_E_Name), NVL (S.Reprs_E_Name, S.Reprs_A_Name)) REP_NM
          ,S.Rep_Code_Parent
          ,S.W_Code
          ,Nvl (S.No_Sal, 0) No_Sal
      From Sales_Man S, Dts_Para
      where Nvl (S.No_Sal, 0)=0
      and S.W_Code Is Not null
Connect By Prior Reprs_Code = Rep_Code_Parent
Start With Reprs_Code = '''||P_Rep_Code||''' ';
-----------------------------------
   Begin
       Qry_Rslt:=Genrat_Data_File (P_Doc_Type          => Null
                                  ,P_Mst_Qry           =>V_Qry
                                  ,P_Dtl_Qry           =>Null
                                  ,P_Mst_Dtl_Flg       => 0
                                  ,P_Out_Data_Typ      =>0) ;
   Exception
      When Others Then
         V_Err_No := 20006;
         V_Msg_Txt := ' Error In Ars_Api_Fetch_Data_Pkg.GET_SMAN_DATA '|| Sqlerrm;
         Goto Rtn_Rslt;
   End;
-----------------------------------
   Return Qry_Rslt;

  --####################--
  <<RTN_RSLT>>
   If V_Msg_Txt Is Not Null Then
      V_Json_Rslt := Replace (V_Json_Rslt, '@ERRNO', V_Err_No);
      V_Json_Rslt := Replace( V_Json_Rslt, '@ERRMSG',Replace( V_Msg_Txt,'"',' '));
      Return V_Json_Rslt;
   End If;
--####################--
Exception
   When Others Then
      Raise_Application_Error (-20003, ' Error In GET_SMAN_DATA ' || Sqlerrm);
End GET_SMAN_DATA;
--================================================================================---
Begin
   Execute Immediate 'ALTER SESSION SET NLS_DATE_FORMAT=''DD/MM/RRRR''';
End Ars_Api_Fetch_Data_Pkg;