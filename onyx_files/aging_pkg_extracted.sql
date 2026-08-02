TEXT
PACKAGE BODY IAS_DSTR_CST_DR_PKG AS
Procedure Ias_Dstr_Cst_Dr_Amt_Prc  (P_C_Code        In Customer.C_Code%Type,
                                    P_Doc_Date      In Date,
                                    P_Local_Cur     In Varchar2,
                                    P_Aralt         In Number,
                                    P_User_No       In Number,
                                    P_No_Of_Decimal In Number) Is
        Crrem         Number := 0;
        Cramt         Number := 0;
        V_Frst_Date   Date := Ias_Gen_Pkg.Get_Frst_Day;

        Cursor Cst_Dr Is
              Select C_Code,
                     A_Cy,
                     Bill_No,
                     Doc_Type,
                     Bill_Doc_Type,
                     Bill_Ser,
                     I_No,
                     Doc_Date,
                     I_Date,
                     Least(I_Amt, Sum_Amt)                         I_Amt,
                     (Least(I_Amt, Sum_Amt) * Nvl(Ac_Rate, 1))     I_Amt_Loc,
                     Ac_Rate,
                     Pj_No,
                     Actv_No,
                     Rcrd_No,
                     A_Code,
                     Dr_Typ,
                     Move_Cy,
                     Brn_No,
                     Brn_Year,
                     Cmp_No,
                     Brn_Usr
                From (With
                         T1  As
                          (Select C_Code, A_Cy, Bill_No, Doc_Type, Bill_Doc_Type, Bill_Ser, I_No, Doc_Date, I_Date, I_Amt  , Sum_Amt, Ac_Rate, Pj_No, Actv_No, Rcrd_No ,A_Code, Dr_Typ, Move_Cy, Brn_No, Brn_Year, Cmp_No, Brn_Usr
                             From
                              (  Select B.C_Code,
                                        B.A_Cy,
                                        B.Bill_No,
                                        B.Doc_Type,
                                        B.Bill_Doc_Type,
                                        B.Bill_Ser,
                                        B.I_No,
                                        B.Doc_Date,
                                        Decode(P.Chk_Crdt_Prd_Typ,
                                                1, Decode( A.Credit_Period,
                                                           Null, B.I_Date,
                                                           Decode(B.Doc_Date, Null, B.I_Date, B.Doc_Date + A.Credit_Period)
                                                         )
                                                ,  B.I_Date
                                              ) I_Date ,
                                        Nvl(B.I_Amt, 0) I_Amt,
                                        (Sum(Nvl(B.I_Amt, 0)) Over(Partition By B.C_Code, B.A_Cy, B.Bill_Ser Order By B.C_Code, B.A_Cy, B.I_Date, B.I_No Rows Unbounded Preceding) - 0)
                                            Sum_Amt,
                                        --(Nvl(B.I_Amt, 0) * Nvl(B.Ac_Rate, 1)) I_Amt_Loc,
                                        B.Ac_Rate,
                                        B.Pj_No,
                                        B.Actv_No,
                                        B.Rcrd_No,
                                        B.A_Code,
                                        B.Dr_Typ,
                                        B.Move_Cy,
                                        B.Brn_No,
                                        B.Brn_Year,
                                        B.Cmp_No,
                                        B.Brn_Usr
                                   From Customer A, Installment B, Ias_Para_Ar P
                                  Where B.C_Code = A.C_Code
                                        And B.C_Code = P_C_Code
                                        And B.I_Date <= Nvl(P_Doc_Date, B.I_Date)
                                        And B.Dr_No Is Null  And Nvl(B.I_Amt,0) >0
                                        And ((P_User_No = 1)
                                             Or (((P_Aralt = 1)
                                                  And Exists
                                                          (Select 1
                                                             From Priv_Acc
                                                            Where U_Id = P_User_No
                                                                  And A_Code = A.C_A_Code
                                                                  And A_Cy = B.A_Cy
                                                                  And Nvl(Add_Flag, 0) = 1
                                                                  And Rownum <= 1))
                                                 Or ((P_Aralt = 2)
                                                     And Exists
                                                             (Select 1
                                                                From Ias_Priv_Customer
                                                               Where U_Id = P_User_No
                                                                     And C_Code = A.C_Code
                                                                     And A_Cy = B.A_Cy
                                                                     And Nvl(Add_Flag, 0) = 1
                                                                     And Rownum <= 1))))
                        Union All --- Include vndr Trans
                         Select A.C_Code,     B.A_Cy,
                                B.Doc_No Bill_No,
                                B.Doc_Type,
                                B.Jv_Type Bill_Doc_Type,
                                B.Doc_Ser Bill_Ser,
                                1 I_No,
                                B.Doc_Date,
                                Decode( P.Chk_Crdt_Prd_Typ,
                                        1, Decode( A.Credit_Period,
                                                   Null, B.Doc_Due_Date,
                                                   Decode(B.Doc_Date, Null, B.Doc_Due_Date, B.Doc_Date + A.Credit_Period)
                                                  )
                                       , B.Doc_Due_Date)   I_Date,
                                Nvl(B.Amt, 0)    I_Amt,
                                (Sum(Nvl(B.Amt, 0)) Over(Partition By A.C_Code, B.A_Cy, B.Doc_Ser Order By A.C_Code, B.A_Cy, B.Doc_Due_Date  Rows Unbounded Preceding) - 0)
                                Sum_Amt,
                                Decode (Nvl(B.Amt_F,0),0,1, Nvl(B.Amt,0)/Nvl(B.Amt_F,0)) Ac_Rate,
                                B.Pj_No,
                                B.Actv_No,
                                B.Rcrd_No,
                                B.A_Code,
                                1 Dr_Typ,
                                0 Move_Cy,
                                B.Brn_No,
                                B.Brn_Year,
                                B.Cmp_No,
                                B.Brn_Usr
                         From Customer A, Ias_Post_Dtl B, Ias_Para_Ar P
                        Where A.C_Code = B.C_V_Code
                              And B.C_Code Is Null
                              And B.C_V_Code = P_C_Code And B.Doc_Due_Date <= Nvl(P_Doc_Date, B.Doc_Due_Date)
                              AND NVL( ADM_GEN_PKG.GET_PRV_FXD_FLD_NMBR_FNC( NVL(P_user_no,1), 'AR_INC_VND_MOV_CON_CST_CHKCRDT' ),0)=1
                              And Nvl(B.Amt,0) >0
                              And ((P_User_No = 1)
                                   Or (((P_Aralt = 1)
                                        And Exists
                                                (Select 1  From Priv_Acc
                                                  Where U_Id = P_User_No
                                                        And A_Code = A.C_A_Code
                                                        And A_Cy = B.A_Cy
                                                        And Nvl(Add_Flag, 0) = 1
                                                        And Rownum <= 1))
                                       Or ((P_Aralt = 2)
                                           And Exists
                                                   (Select 1 From Ias_Priv_Customer
                                                     Where U_Id = P_User_No
                                                           And C_Code = A.C_Code
                                                           And A_Cy = B.A_Cy
                                                           And Nvl(Add_Flag, 0) = 1
                                                           And Rownum <= 1))))
                             )
                      Order By I_Date, Doc_Type, Bill_No, I_No)
                      Select C_Code,
                             A_Cy,
                             Bill_No,
                             Doc_Type,
                             Bill_Doc_Type,
                             T1.Bill_Ser,
                             I_No,
                             Doc_Date,
                             I_Date,
                             I_Amt,
                             Sum_Amt - Nvl(Rt_Amt, 0)     Sum_Amt,
                             Ac_Rate,
                             Pj_No,
                             Actv_No,
                             Rcrd_No,
                             T1.A_Code,
                             T1.Dr_Typ,
                             T1.Move_Cy,
                             Brn_No,
                             Brn_Year,
                             Cmp_No,
                             Brn_Usr
                        From T1,
                             (  Select Bill_Ser, Nvl(Sum(Dtl_Amt * Per_Amt), 0) Rt_Amt
                                  From (Select Rt_Bill_No,
                                               Rt_Bill_Ser,
                                               Bill_Ser,
                                               Bill_No,
                                               Cc_Code,
                                               Pj_No,
                                               Actv_No,
                                               Rt_Bill_Date,
                                               Rt_Bill_Rate,
                                               (Sum(Nvl(Dtl_Amt, 0)) Over (Partition By Rt_Bill_Ser) * Decode(0, 1, Nvl(Rt_Bill_Rate, 1), 1)) Bill_Amt,
                                               Ac_Amt,
                                               Dtl_Amt,
                                               ((Sum(Nvl(Dtl_Amt, 0)) Over (Partition By Rt_Bill_Ser) - Ac_Amt) / Decode(Sum(Nvl(Dtl_Amt, 0)) Over(Partition By Rt_Bill_Ser), 0, 1, Sum(Nvl(Dtl_Amt, 0)) Over(Partition By Rt_Bill_Ser)))
                                                   Per_Amt
                                          From (Select M.Rt_Bill_No,
                                                       M.Rt_Bill_Ser,
                                                       D.Bill_Ser,
                                                       Bill_No,
                                                       D.Cc_Code,
                                                       D.Pj_No,
                                                       D.Actv_No,
                                                       M.Rt_Bill_Date,
                                                       M.Rt_Bill_Rate,
                                                       Nvl((Nvl(D.I_Qty, 0) * (Nvl(D.I_Price, 0) - Nvl(D.Dis_Amt, 0) + Nvl(D.Vat_Amt, 0) + Nvl(D.Othr_Amt, 0))), 0)  Dtl_Amt,
                                                       ((Nvl(M.Cr_Card_Amt, 0) + Nvl(M.Cr_Card_Amt_Scnd, 0) + Nvl(M.Cr_Card_Amt_Thrd, 0)) + Nvl(M.Ac_Amt, 0))    Ac_Amt
                                                  From Ias_Rt_Bill_Mst M, Ias_Rt_Bill_Dtl D
                                                 Where M.Rt_Bill_Ser = D.Rt_Bill_Ser
                                                       And M.Rt_Bill_Doc_Type = 4
                                                       And M.P_Year In (0, 3)
                                                       And M.Rt_Bill_Date <= Nvl(P_Doc_Date, M.Rt_Bill_Date)
                                                Union All
                                                Select M.Doc_No      Rt_Bill_No,
                                                       M.Doc_Ser     Rt_Bill_Ser,
                                                       D.Bill_Ser,
                                                       D.Bill_No,
                                                       M.Cc_Code,
                                                       M.Pj_No,
                                                       M.Actv_No,
                                                       M.Doc_Date    Rt_Bill_Date,
                                                       M.Doc_Rate    Rt_Bill_Rate,
                                                       Nvl(D.Add_Dis_Qty, 0) * Nvl(D.Add_Dis_Amt_Dtl, 0)
                                                       + (Nvl(D.Add_Dis_Qty, 0) * Nvl(D.Add_Vat_Amt, 0)
                                                       )             Dtl_Amt,
                                                       0             Ac_Amt
                                                  From Ias_Bill_Mst_Add_Disc M, Ias_Bill_Dtl_Add_Disc D
                                                 Where M.Doc_Ser = D.Doc_Ser
                                                       And Nvl(Note_Typ, 0) = 1
                                                       And M.Bill_Doc_Type = 4
                                                       And M.Doc_Date <= Nvl(P_Doc_Date, M.Doc_Date)))
                              Group By Bill_Ser) Rt
                       Where Rt.Bill_Ser(+) = T1.Bill_Ser)
               Where Least(I_Amt, Sum_Amt) > 0
            Order By I_Date, Doc_Type, Bill_No, I_No;
            ----------------------------------------------------------------------------------------------
         Cursor Cst_cr Is
          Select  C_code , Doc_date,Doc_type,Doc_ser,Doc_no,Cr_amt,Ac_rate
            From
              (
              Select Coalesce(B.C_v_code, B.C_code)                                                     C_code,
                     B.Doc_date,
                     B.Doc_type,
                     B.Doc_ser,
                     B.Doc_no,
                     B.Cr_amt                                                                      Cr_amt,
                     Decode(Nvl(B.Cr_amt_f, 0), 0, 1, (Nvl(B.Cr_amt, 0) / Nvl(B.Cr_amt_f, 0)))     Ac_rate
                From Customer A, Ias_post_dtl B
               Where A.C_code = Nvl(B.C_v_code, B.C_code)                                      --B.C_code
                     And Nvl(Cr_amt, 0) > 0
                     And Coalesce(B.C_v_code, B.C_code) = P_c_code
                     And B.Doc_date <= Nvl(P_doc_date, B.Doc_date)
                     And (Doc_type <> 0
                          Or Not Exists
                                 (Select 1 From Installment
                                   Where C_code = Coalesce(B.C_v_code, B.C_code)              ---B.Ac_code_dtl
                                         And Doc_date < V_frst_date
                                          And Nvl(I_amt,0) >0
                                         And Rownum <= 1))
                     And ((P_user_no = 1)
                          Or (((P_aralt = 1)
                               And Exists
                                       (Select 1 From Priv_acc
                                         Where U_id = P_user_no
                                               And A_code = A.C_a_code
                                               And A_cy = B.A_cy
                                               And Nvl(Add_flag, 0) = 1
                                               And Rownum <= 1))
                              Or ((P_aralt = 2)
                                  And Exists
                                          (Select 1 From Ias_priv_customer
                                            Where U_id = P_user_no
                                                  And C_code = Coalesce(B.C_v_code, B.C_code)       --A.C_code
                                                  And A_cy = B.A_cy
                                                  And Nvl(Add_flag, 0) = 1
                                                  And Rownum <= 1))))
                     And Not Exists
                             (Select 1
                                From Ias_rt_bill_mst M, Ias_rt_bill_dtl D
                               Where M.Rt_bill_ser = D.Rt_bill_ser
                                     And M.Rt_bill_doc_type = 4
                                     And B.Doc_type = 5
                                     And M.P_year In (0, 3)
                                     And M.Rt_bill_ser = B.Doc_ser
                                     And Exists
                                             (Select 1
                                                From Ias_bill_mst
                                               Where Ias_bill_mst.Bill_ser = D.Bill_ser
                                                     And Ias_bill_mst.Bill_doc_type = 4
                                                     And Rownum <= 1)
                                     And Rownum <= 1)
            Union All
              Select
                     B.C_code                           C_code,
                     B.Rt_bill_date                     Doc_date,
                     5                                  Doc_type,
                     B.Rt_bill_ser                       Doc_ser,
                     B.Rt_bill_no                       Doc_no,
                     Sum(Case When D.Bill_doc_type Not In (4,8) Then (Nvl(D.I_qty,0) * (Nvl (D.I_price, 0)
                                        + Nvl (D.Vat_amt, 0)
                                        + Nvl (D.Othr_amt, 0)
                                        - Nvl (D.Dis_amt, 0)
                                        - Nvl (D.Dis_amt_aftr_vat, 0)
                                       )
                         ) End)Cr_amt,
                     B.Rt_bill_rate Ac_rate
                From Customer A,Ias_rt_bill_mst B, Ias_rt_bill_dtl D
                Where A.C_code = B.C_code
                 And B.Rt_bill_ser=  D.Rt_bill_ser
                 And B.C_code = P_c_code
                 And B.Rt_bill_doc_type = 4
                 And B.P_year In (0, 3)
                 And B.Rt_bill_date <= Nvl(P_doc_date, B.Rt_bill_date)
                 And Exists  (Select 1
                                          From Ias_rt_bill_dtl D2, Ias_bill_mst Bill
                                        Where D2.Bill_ser = Bill.Bill_ser
                                            And D2.Rt_bill_ser = B.Rt_bill_ser
                                            And Bill.Bill_doc_type In (4)) --4,8
                 And ((P_user_no = 1)
                          Or (((P_aralt = 1)
                               And Exists
                                       (Select 1 From Priv_acc
                                         Where U_id = P_user_no
                                               And A_code = A.C_a_code
                                               And A_cy =B.Rt_bill_currency
                                               And Nvl(Add_flag, 0) = 1
                                               And Rownum <= 1))
                              Or ((P_aralt = 2)
                                  And Exists
                                          (Select 1 From Ias_priv_customer
                                            Where U_id = P_user_no
                                                  And C_code = B.C_code
                                                  And A_cy = B.Rt_bill_currency
                                                  And Nvl(Add_flag, 0) = 1
                                                  And Rownum <= 1))))
		Group By B.C_code,
		         B.Rt_bill_date ,
		         B.Rt_bill_ser   ,
		         B.Rt_bill_no   ,
		         B.Rt_bill_rate)
		            Order By C_code, Doc_date;
    Begin
        --##--------------------------------------------------------------------------------------##--
        For I In Cst_Dr Loop
            Begin
                Insert Into Ias_Si_Dr_Dtl_Tmp(C_Code, A_Cy, Doc_No, Doc_Type, Doc_Jv_Type, Doc_Ser, I_No, Doc_Date, Bill_Date, I_Amt, I_Amt_Loc,  Bill_Rate, Paid_Amt, Paid_Amt_Loc, Paid_Date, Paid, Trmnl_Name,
                                              Pj_No, Actv_No, Rcrd_No , A_Code, Dr_Typ, Move_Cy , Brn_No, Brn_Year, Cmp_No, Brn_Usr
                                             )
                 Values (I.C_Code, I.A_Cy, I.Bill_No, I.Doc_Type, I.Bill_Doc_Type, I.Bill_Ser,  I.I_No, I.I_Date, I.Doc_Date, I.I_Amt, I.I_Amt_Loc, Nvl(I.Ac_Rate, 1),Null, Null, Null, 0, Null,
                         I.Pj_No, I.Actv_No, I.Rcrd_No , I.A_Code, I.Dr_Typ, I.Move_Cy, I.Brn_No, I.Brn_Year, I.Cmp_No, I.Brn_Usr);
            Exception When Others Then
                Raise_Application_Error(-20400, ' Error When Insert Into Ias_Si_Dr_Dtl_Tmp. ' || Chr(13) || Sqlerrm);
            End;
        End Loop;

        Crrem   := 0;

        For Cr In Cst_Cr Loop
            Declare
                Cursor C_Paid Is
                      Select Doc_Ser,
                             Doc_No,
                             I_No,
                             Doc_Date,
                             I_Amt_Loc,
                             Paid_Amt_Loc,
                             Paid_Date,
                             Paid,
                             C_Code,
                             Bill_Rate     Ac_Rate
                        From Ias_Si_Dr_Dtl_Tmp
                       Where Nvl(Paid, 0) = 0 And C_Code = Cr.C_Code
                    Order By C_Code, Doc_Date, Doc_Ser;
            Begin
                Cramt   := Cr.Cr_Amt + Crrem;

                For Cp In C_Paid Loop
                    If Cramt > Cp.I_Amt_Loc Then
                        Cramt   := Cramt - Cp.I_Amt_Loc;
                        Crrem   := 0;
                        Begin
                            Update Ias_Si_Dr_Dtl_Tmp
                               Set Paid_Amt_Loc = I_Amt_Loc,
                                   Paid_Amt = Round((I_Amt_Loc / Cp.Ac_Rate), P_No_Of_Decimal), --I_amt_loc
                                                                                                Paid = 1,
                                   Paid_Date = Cr.Doc_Date
                             Where Doc_Ser = Cp.Doc_Ser And C_Code = Cr.C_Code And I_No = Cp.I_No;
                        End;
                    Elsif Cramt = Cp.I_Amt_Loc Then
                        Cramt   := 0;
                        Crrem   := 0;
                        Begin
                            Update Ias_Si_Dr_Dtl_Tmp
                               Set Paid_Amt_Loc = I_Amt_Loc,
                                   Paid_Amt = Round((I_Amt_Loc / Cp.Ac_Rate), P_No_Of_Decimal), Paid = 1,
                                   Paid_Date = Cr.Doc_Date
                             Where Doc_Ser = Cp.Doc_Ser And C_Code = Cr.C_Code And I_No = Cp.I_No;
                        End;
                        Exit;
                        Crrem   := 0;
                    Elsif Cramt < Cp.I_Amt_Loc Then
                        Crrem   := Cramt;
                        Cramt   := 0;
                        Begin
                            Update Ias_Si_Dr_Dtl_Tmp
                               Set Paid_Amt_Loc = Crrem,
                                   Paid_Amt = Round((Crrem / Cp.Ac_Rate), P_No_Of_Decimal),
                                   Paid_Date = Cr.Doc_Date
                             Where Doc_Ser = Cp.Doc_Ser And C_Code = Cr.C_Code And I_No = Cp.I_No;
                        End;
                        Exit;
                    End If;
                End Loop;                                                                        --C_Paid
            End;
        End Loop;                                                                                --Cst_Cr
    End;
    -----------------------------------------------------------------------------------------------------------------------------------------------

    Procedure Ias_Dstr_Cst_Dr_Amt_Acy_Prc
        (P_C_Code In Customer.C_Code%Type, P_Doc_Date In Date, P_Local_Cur In Varchar2, P_Aralt In Number, P_User_No In Number, P_No_Of_Decimal In Number) Is
        Crrem         Number := 0;
        Cramt         Number := 0;
        V_Frst_Date   Date := Ias_Gen_Pkg.Get_Frst_Day;

        Cursor Cst_Dr Is
            With T1 As
                  (Select C_Code, A_Cy, Bill_No, Doc_Type, Bill_Doc_Type, Bill_Ser, I_No, Doc_Date, I_Date, I_Amt , Sum_Amt,
                          Ac_Rate, Pj_No, Actv_No, Rcrd_No ,A_Code, Dr_Typ, Move_Cy, Brn_No, Brn_Year, Cmp_No, Brn_Usr
                     From
                       (Select B.C_Code,
                              B.A_Cy,
                              B.Bill_No,
                              B.Doc_Type,
                              B.Bill_Doc_Type,
                              B.Bill_Ser,
                              B.I_No,
                              B.Doc_Date,
                              Decode(
                                  P.Chk_Crdt_Prd_Typ,
                                  1, Decode(
                                         A.Credit_Period,
                                         Null, B.I_Date,
                                         Decode(B.Doc_Date, Null, B.I_Date, B.Doc_Date + A.Credit_Period)),
                                  B.I_Date)
                                  I_Date,
                              Nvl(B.I_Amt, 0)
                                  I_Amt,
                              (Sum(Nvl(B.I_Amt, 0)) Over(Partition By B.C_Code, B.A_Cy, B.Bill_Ser Order By B.C_Code, B.A_Cy, B.I_Date, B.I_No Rows Unbounded Preceding) - 0)
                                  Sum_Amt,
                              --(Nvl(B.I_Amt, 0) * Nvl(B.Ac_Rate, 1)) I_Amt_Loc,
                              B.Ac_Rate,
                              B.Pj_No,
                              B.Actv_No,
                              B.Rcrd_No,
                              B.A_Code,
                              B.Dr_Typ,
                              B.Move_Cy,
                              B.Brn_No,
                              B.Brn_Year,
                              B.Cmp_No,
                              B.Brn_Usr
                         From Customer A, Installment B, Ias_Para_Ar P
                        Where A.C_Code = B.C_Code
                              And B.C_Code = P_C_Code
                              And B.I_Date <= Nvl(P_Doc_Date, B.I_Date)
                              And B.Dr_No Is Null  And Nvl(B.I_Amt,0) >0
                              And (B.A_Cy = P_Local_Cur
                                   Or (Select Sum(Amt_F)
                                         From Ias_Post_Dtl
                                        Where A_Cy = B.A_Cy And Ac_Dtl_Typ = 3 And Ac_Code_Dtl = B.C_Code) <>0)
                              And ((P_User_No = 1)
                                   Or (((P_Aralt = 1)
                                        And Exists
                                                (Select 1  From Priv_Acc
                                                  Where U_Id = P_User_No
                                                        And A_Code = A.C_A_Code
                                                        And A_Cy = B.A_Cy
                                                        And Nvl(Add_Flag, 0) = 1
                                                        And Rownum <= 1))
                                       Or ((P_Aralt = 2)
                                           And Exists
                                                   (Select 1 From Ias_Priv_Customer
                                                     Where U_Id = P_User_No
                                                           And C_Code = A.C_Code
                                                           And A_Cy = B.A_Cy
                                                           And Nvl(Add_Flag, 0) = 1
                                                           And Rownum <= 1))))
                      Union All --- Include vndr Trans
                         Select A.C_Code,     B.A_Cy,
                                B.Doc_No Bill_No,
                                B.Doc_Type,
                                B.Jv_Type Bill_Doc_Type,
                                B.Doc_Ser Bill_Ser,
                                1 I_No,
                                B.Doc_Date,
                                Decode( P.Chk_Crdt_Prd_Typ,
                                        1, Decode( A.Credit_Period,
                                                   Null, B.Doc_Due_Date,
                                                   Decode(B.Doc_Date, Null, B.Doc_Due_Date, B.Doc_Date + A.Credit_Period)
                                                  ), B.Doc_Due_Date)   I_Date,
                                Nvl(B.Amt, 0)    I_Amt,
                                (Sum(Nvl(B.Amt, 0)) Over(Partition By A.C_Code, B.A_Cy, B.Doc_Ser Order By A.C_Code, B.A_Cy, B.Doc_Due_Date  Rows Unbounded Preceding) - 0)
                                Sum_Amt,
                                Decode (Nvl(B.Amt_F,0),0,1, Nvl(B.Amt,0)/Nvl(B.Amt_F,0)) Ac_Rate,
                                B.Pj_No,
                                B.Actv_No,
                                B.Rcrd_No,
                                B.A_Code,
                                1 Dr_Typ,
                                0 Move_Cy,
                                B.Brn_No,
                                B.Brn_Year,
                                B.Cmp_No,
                                B.Brn_Usr
                         From Customer A, Ias_Post_Dtl B, Ias_Para_Ar P
                        Where A.C_Code = B.C_V_Code
                              And B.C_Code Is Null
                              And B.C_V_Code = P_C_Code And B.Doc_Due_Date <= Nvl(P_Doc_Date, B.Doc_Due_Date)
                              AND NVL( ADM_GEN_PKG.GET_PRV_FXD_FLD_NMBR_FNC( NVL(P_user_no,1), 'AR_INC_VND_MOV_CON_CST_CHKCRDT' ),0)=1
                              And Nvl(B.Amt,0) >0
                              And (B.A_Cy = P_Local_Cur
                                   Or (Select Sum(Amt_F)
                                         From Ias_Post_Dtl
                                        Where A_Cy = B.A_Cy And C_V_Code = B.C_V_Code) <> 0)
                              And ((P_User_No = 1)
                                   Or (((P_Aralt = 1)
                                        And Exists
                                                (Select 1  From Priv_Acc
                                                  Where U_Id = P_User_No
                                                        And A_Code = A.C_A_Code
                                                        And A_Cy = B.A_Cy
                                                        And Nvl(Add_Flag, 0) = 1
                                                        And Rownum <= 1))
                                       Or ((P_Aralt = 2)
                                           And Exists
                                                   (Select 1 From Ias_Priv_Customer
                                                     Where U_Id = P_User_No
                                                           And C_Code = A.C_Code
                                                           And A_Cy = B.A_Cy
                                                           And Nvl(Add_Flag, 0) = 1
                                                           And Rownum <= 1))))
                             )  Order By I_Date, Doc_Type, Bill_No, I_No
                    )
              Select C_Code,
                     A_Cy,
                     Bill_No,
                     Doc_Type,
                     Bill_Doc_Type,
                     T1.Bill_Ser,
                     I_No,
                     Doc_Date,
                     I_Date,
                     Least(I_Amt, Sum_Amt - Nvl(Rt_Amt, 0))                         I_Amt,
                     (Least(I_Amt, Sum_Amt - Nvl(Rt_Amt, 0)) * Nvl(Ac_Rate, 1))     I_Amt_Loc,
                     Ac_Rate,
                     Pj_No,
                     Actv_No,
                     Rcrd_No,
                     T1.A_Code,
                     T1.Dr_Typ,
                     T1.Move_Cy,
                     Brn_No,
                     Brn_Year,
                     Cmp_No,
                     Brn_Usr
                From T1,
                     (  Select Bill_Ser, Nvl(Sum(Dtl_Amt * Per_Amt), 0) Rt_Amt
                          From (Select Rt_Bill_No,
                                       Rt_Bill_Ser,
                                       Bill_Ser,
                                       Bill_No,
                                       Cc_Code,
                                       Pj_No,
                                       Actv_No,
                                       Rt_Bill_Date,
                                       Rt_Bill_Rate,
                                       (Sum(Nvl(Dtl_Amt, 0)) Over (Partition By Rt_Bill_Ser) * Decode(1, 1, Nvl(Rt_Bill_Rate, 1), 1)) Bill_Amt,
                                       Ac_Amt,
                                       Dtl_Amt,
                                       ((Sum(Nvl(Dtl_Amt, 0)) Over (Partition By Rt_Bill_Ser)-Ac_Amt) / Decode(Sum(Nvl(Dtl_Amt, 0)) Over(Partition By Rt_Bill_Ser), 0, 1, Sum(Nvl(Dtl_Amt, 0)) Over(Partition By Rt_Bill_Ser)))
                                           Per_Amt
                                  From (Select M.Rt_Bill_No,
                                               M.Rt_Bill_Ser,
                                               D.Bill_Ser,
                                               Bill_No,
                                               D.Cc_Code,
                                               D.Pj_No,
                                               D.Actv_No,
                                               M.Rt_Bill_Date,
                                               M.Rt_Bill_Rate,
                                               Nvl((Nvl(D.I_Qty, 0) * (Nvl(D.I_Price, 0) - Nvl(D.Dis_Amt, 0)
                                                    + Nvl(D.Vat_Amt, 0) + Nvl(D.Othr_Amt, 0))),
                                                   0
                                                  )                                                                                                      Dtl_Amt,
                                               ((Nvl(M.Cr_Card_Amt, 0) + Nvl(M.Cr_Card_Amt_Scnd, 0) + Nvl(M.Cr_Card_Amt_Thrd, 0)) + Nvl(M.Ac_Amt, 0))    Ac_Amt
                                          From Ias_Rt_Bill_Mst M, Ias_Rt_Bill_Dtl D
                                         Where M.Rt_Bill_Ser = D.Rt_Bill_Ser
                                               And M.Rt_Bill_Doc_Type = 4
                                               And M.P_Year In (0, 3)
                                        --And NVL(D.bill_ser,0)=P_Doc_Ser
                                        Union All
                                        Select M.Doc_No      Rt_Bill_No,
                                               M.Doc_Ser     Rt_Bill_Ser,
                                               D.Bill_Ser,
                                               D.Bill_No,
                                               M.Cc_Code,
                                               M.Pj_No,
                                               M.Actv_No,
                                               M.Doc_Date    Rt_Bill_Date,
                                               M.Doc_Rate    Rt_Bill_Rate,
                                               Nvl(D.Add_Dis_Qty, 0) * Nvl(D.Add_Dis_Amt_Dtl, 0) + (Nvl(D.Add_Dis_Qty, 0) * Nvl(D.Add_Vat_Amt, 0)
                                               )             Dtl_Amt,
                                               0             Ac_Amt
                                          From Ias_Bill_Mst_Add_Disc M, Ias_Bill_Dtl_Add_Disc D
                                         Where M.Doc_Ser = D.Doc_Ser
                                               And Nvl(Note_Typ, 0) = 1
                                               And M.Bill_Doc_Type = 4--And NVL(D.bill_ser,0)='||P_Doc_Ser||'
                                          ))
                      Group By Bill_Ser) Rt
               Where Rt.Bill_Ser(+) = T1.Bill_Ser And Least(I_Amt, Sum_Amt - Nvl(Rt_Amt, 0)) > 0
            Order By I_Date, Doc_Type, Bill_No, I_No;
        ----------------------------------------------------------------------------------------------
        Cursor Cst_cr Is
           Select  C_code,Doc_date,Doc_type,Doc_ser,Doc_no , Cr_amt ,Ac_rate
            From (
              Select Coalesce(B.C_v_code, B.C_code)                                                     C_code,
                     B.Doc_date,
                     B.Doc_type,
                     B.Doc_ser,
                     B.Doc_no,
                     Decode(B.A_cy, P_local_cur, B.Cr_amt, B.Cr_amt_f)                             Cr_amt,
                     Decode(Nvl(B.Cr_amt_f, 0), 0, 1, (Nvl(B.Cr_amt, 0) / Nvl(B.Cr_amt_f, 0)))     Ac_rate
                From Customer A, Ias_post_dtl B
               Where A.C_code = Coalesce(B.C_v_code, B.C_code)
                     And Nvl(Cr_amt, 0) > 0
                     And Nvl(B.C_v_code, B.C_code) = P_c_code
                     And B.Doc_date <= Nvl(P_doc_date, B.Doc_date)
                     And (B.A_cy = P_local_cur
                          Or (Select Sum(Amt_f)
                                From Ias_post_dtl
                               Where A_cy = B.A_cy
                                     And Ac_dtl_typ = 3
                                     And Ac_code_dtl = Coalesce(B.C_v_code, B.C_code)) <>
                             0)
                     And (Doc_type <> 0
                          Or Not Exists
                                 (Select 1 From Installment
                                   Where C_code = Coalesce(B.C_v_code, B.C_code)               --B.Ac_code_dtl
                                         And Doc_date < V_frst_date
                                          And Nvl(I_amt,0) >0
                                         And Rownum <= 1))
                     And ((P_user_no = 1)
                          Or (((P_aralt = 1)
                               And Exists
                                       (Select 1 From Priv_acc
                                         Where U_id = P_user_no
                                               And A_code = A.C_a_code
                                               And A_cy = B.A_cy
                                               And Nvl(Add_flag, 0) = 1
                                               And Rownum <= 1))
                              Or ((P_aralt = 2)
                                  And Exists
                                          (Select 1 From Ias_priv_customer
                                            Where U_id = P_user_no
                                                  And C_code = Coalesce(B.C_v_code, B.C_code)
                                                  And A_cy = B.A_cy
                                                  And Nvl(Add_flag, 0) = 1
                                                  And Rownum <= 1))))
                     And Not Exists
                             (Select 1
                                From Ias_rt_bill_mst M, Ias_rt_bill_dtl D
                               Where M.Rt_bill_ser = D.Rt_bill_ser
                                     And M.Rt_bill_doc_type = 4
                                     And B.Doc_type = 5
                                     And M.P_year In (0, 3)
                                     And M.Rt_bill_ser = B.Doc_ser
                                     And Exists
                                             (Select 1 From Ias_bill_mst
                                               Where Ias_bill_mst.Bill_ser = D.Bill_ser
                                                     And Ias_bill_mst.Bill_doc_type = 4
                                                     And Rownum <= 1)
                                     And Rownum <= 1)

            Union All
              Select
                     B.C_code                           C_code,
                     B.Rt_bill_date                     Doc_date,
                     5                                  Doc_type,
                     B.Rt_bill_ser                       Doc_ser,
                     B.Rt_bill_no                       Doc_no,
                     Sum(Case When D.Bill_doc_type Not In (4,8) Then (Nvl(D.I_qty,0) * (Nvl (D.I_price, 0)
                                        + Nvl (D.Vat_amt, 0)
                                        + Nvl (D.Othr_amt, 0)
                                        - Nvl (D.Dis_amt, 0)
                                        - Nvl (D.Dis_amt_aftr_vat, 0)
                                       )
                         ) End)Cr_amt,
                     B.Rt_bill_rate Ac_rate
                From Customer A,Ias_rt_bill_mst B, Ias_rt_bill_dtl D
                Where A.C_code = B.C_code
                    And B.Rt_bill_ser=  D.Rt_bill_ser
                    And B.C_code = P_c_code
                    And B.Rt_bill_doc_type = 4
                    And B.P_year In (0, 3)
                    And B.Rt_bill_date <= Nvl(P_doc_date, B.Rt_bill_date)
                    And Exists  (Select 1
                                          From Ias_rt_bill_dtl D2, Ias_bill_mst Bill
                                        Where D2.Bill_ser = Bill.Bill_ser
                                            And D2.Rt_bill_ser = B.Rt_bill_ser
                                            And Bill.Bill_doc_type In (4) And Rownum <= 1 )  --4,8
                     And ((P_user_no = 1)
                          Or (((P_aralt = 1)
                               And Exists
                                       (Select 1 From Priv_acc
                                         Where U_id = P_user_no
                                               And A_code = A.C_a_code
                                               And A_cy =B.Rt_bill_currency
                                               And Nvl(Add_flag, 0) = 1
                                               And Rownum <= 1))
                              Or ((P_aralt = 2)
                                  And Exists
                                          (Select 1 From Ias_priv_customer
                                            Where U_id = P_user_no
                                                  And C_code = B.C_code
                                                  And A_cy = B.Rt_bill_currency
                                                  And Nvl(Add_flag, 0) = 1
                                                  And Rownum <= 1))))
		Group By B.C_code,
		         B.Rt_bill_date ,
		         B.Rt_bill_ser   ,
		         B.Rt_bill_no   ,
		         B.Rt_bill_rate
		            )
		            Order By C_code, Doc_date;
    Begin
        For I In Cst_Dr Loop
            Begin
                Insert Into Ias_Si_Dr_Dtl_Tmp(C_Code, A_Cy, Doc_No, Doc_Type, Doc_Jv_Type, Doc_Ser, I_No, Doc_Date, Bill_Date, I_Amt, I_Amt_Loc, Bill_Rate, Paid_Amt, Paid_Amt_Loc, Paid_Date, Paid ,	Trmnl_Name,
                                             Pj_No, Actv_No, Rcrd_No ,  A_Code, Dr_Typ, Move_Cy , Brn_No, Brn_Year, Cmp_No, Brn_Usr
                                             )
                     Values (I.C_Code, I.A_Cy, I.Bill_No, I.Doc_Type, I.Bill_Doc_Type, I.Bill_Ser, I.I_No, I.I_Date, I.Doc_Date, I.I_Amt, I.I_Amt_Loc, Nvl(I.Ac_Rate, 1),  Null, Null, Null, 0, Null,
                             I.Pj_No,  I.Actv_No, I.Rcrd_No ,  I.A_Code, I.Dr_Typ, I.Move_Cy , I.Brn_No, I.Brn_Year, I.Cmp_No, I.Brn_Usr);
            Exception When Others Then
                Raise_Application_Error(-20401, ' Error When Insert Into Ias_Si_Dr_Dtl_Tmp. ' || Chr(13) || Sqlerrm);
            End;
        End Loop;

        Crrem   := 0;

        For Cr In Cst_Cr Loop
            Declare
                Cursor C_Paid Is
                      Select Doc_Ser,
                             Doc_No,
                             I_No,
                             Doc_Date,
                             I_Amt,
                             I_Amt_Loc,
                             Paid_Amt,
                             Paid_Amt_Loc,
                             Paid_Date,
                             Paid,
                             C_Code,
                             Bill_Rate     Ac_Rate
                        From Ias_Si_Dr_Dtl_Tmp
                       Where Nvl(Paid, 0) = 0 And C_Code = Cr.C_Code
                    -- and i_no=Cr.i_no
                    Order By C_Code, Doc_Date, Doc_Ser;
            Begin
                Cramt   := Cr.Cr_Amt + Crrem;
                For Cp In C_Paid Loop
                    If Cramt > Cp.I_Amt Then
                        Cramt   := Cramt - Cp.I_Amt;
                        Crrem   := 0;
                        Begin
                            Update Ias_Si_Dr_Dtl_Tmp
                               Set Paid_Amt_Loc = Round((I_Amt * Cp.Ac_Rate), P_No_Of_Decimal),
                                   Paid_Amt = I_Amt, --Paid_Amt     = I_amt,
                                                     Paid = 1, Paid_Date = Cr.Doc_Date
                             Where Doc_Ser = Cp.Doc_Ser And C_Code = Cr.C_Code And I_No = Cp.I_No;
                        --COMMIT;
                        End;
                    Elsif Cramt = Cp.I_Amt Then
                        Cramt   := 0;
                        Crrem   := 0;
                        Begin
                            Update Ias_Si_Dr_Dtl_Tmp
                               Set Paid_Amt_Loc = Round((I_Amt * Cp.Ac_Rate), P_No_Of_Decimal),
                                   Paid_Amt = I_Amt, --Paid_Amt     = I_amt,
                                                     Paid = 1, Paid_Date = Cr.Doc_Date
                             Where Doc_Ser = Cp.Doc_Ser And C_Code = Cr.C_Code And I_No = Cp.I_No;
                        End;
                        Exit;
                        Crrem   := 0;
                    Elsif Cramt < Cp.I_Amt Then
                        Crrem   := Cramt;
                        Cramt   := 0;
                        Begin
                            Update Ias_Si_Dr_Dtl_Tmp
                               Set Paid_Amt_Loc = Round((Crrem * Cp.Ac_Rate), P_No_Of_Decimal),
                                   Paid_Amt = Crrem, Bill_Rate = Cr.Ac_Rate, Paid_Date = Cr.Doc_Date
                             Where Doc_Ser = Cp.Doc_Ser And C_Code = Cr.C_Code And I_No = Cp.I_No;
                        End;
                        Exit;
                    End If;
                End Loop;                                                                        --C_Paid
            End;
        End Loop;                                                                                --Cst_Cr
    End;


    --##-------------------------------------------------------------------------------##--
    PROCEDURE Cst_aging_prc(P_local_cur     IN VARCHAR2,
                            P_paid_inst_mnl IN NUMBER DEFAULT 0,
                            P_cst_grp       IN VARCHAR2 DEFAULT NULL,
                            P_sman_grp      IN VARCHAR2 DEFAULT NULL,
                            P_rep_year      IN NUMBER DEFAULT 0,
                            P_per_no        IN NUMBER DEFAULT NULL,
                            P_f_day         IN NUMBER DEFAULT NULL ,
                            P_t_day         IN NUMBER DEFAULT NULL,
                            P_t_date        IN DATE,
                            P_terminal      IN VARCHAR2 DEFAULT NULL,
                            P_whr           IN VARCHAR2 DEFAULT NULL,
                            P_dr_typ        IN NUMBER DEFAULT 1) IS
        V_sql                  VARCHAR2(32000);
        V_sql2                 CLOB;                                                --VARCHAR2 ( 32000 );
        V_dr                   NUMBER := 0;
        V_drf                  NUMBER := 0;
        V_dr_rem               NUMBER := 0;
        V_drf_rem              NUMBER := 0;
        V_ex_rate              NUMBER := 0;
        V_st                   BOOLEAN := TRUE;
        V_stat                 VARCHAR2(500);
        V_trmnlname            VARCHAR2(100) := USERENV('TERMINAL');
        V_cst_grp              VARCHAR2(1000);
        V_sman_grp             VARCHAR2(100);
        V_tb_nm                VARCHAR2(100);
        V_fld_cc_code          VARCHAR2(100) := 'NULL';
        V_fld_pj_no            VARCHAR2(100) := 'NULL';
        V_fld_actv_no          VARCHAR2(100) := 'NULL';
        V_ar_cs_type           NUMBER := 0;
        V_ar_pj_type           NUMBER := 0;
        V_ar_actv_type         NUMBER := 0;
        V_cc_pj_actv           NUMBER := 0;
        V_hav                  VARCHAR2(1000) := ' ';
        V_tbl_rt_mst           VARCHAR2(500);
        V_tbl_rt_dtl           VARCHAR2(500);
        V_rt_whr               VARCHAR2(32000);
        V_sql_rt               VARCHAR2(32000);
        V_sql_get_rt_amt       VARCHAR2(32000);
        V_sql_get_rt_amt_loc   VARCHAR2(32000);
        V_cnt                  NUMBER := 0;
        V_tbl_add_mst          VARCHAR2(500);
        V_tbl_add_dtl          VARCHAR2(500);
        V_add_whr              VARCHAR2(32000);
        V_last_yr_frst_dy      DATE;
        V_fd_whr               VARCHAR2(1000);
        V_SQL_INSTLMNT  			 VARCHAR2(32000); --3
        V_WHR_DOC_TYPE  			 VARCHAR2(32000);
    BEGIN
        EXECUTE IMMEDIATE 'Truncate Table Ias_Cst_Cr_Tmp';
        -------------------------------------------------------
        BEGIN
            SELECT NVL(Ar_cs_type, 0), NVL(Ar_pj_type, 0), NVL(Ar_actv_type, 0)  INTO V_ar_cs_type, V_ar_pj_type, V_ar_actv_type
              FROM Ias_para_ar;
        EXCEPTION WHEN OTHERS THEN
            NULL;
        END;
        -------------------------------------------------------     ;
        IF NVL(V_ar_cs_type, 0) <> 2 AND NVL(V_ar_pj_type, 0) <> 2 AND NVL(V_ar_actv_type, 0) <> 2 THEN
            V_cc_pj_actv   := 1;
        ELSE
            V_cc_pj_actv   := 0;
        END IF;
        -------------------------------------------------------
        IF UPPER(P_cst_grp) = 'B.CC_CODE' THEN
            V_fld_cc_code   := P_cst_grp;
        ELSIF UPPER(P_cst_grp) = 'B.PJ_NO' THEN
            V_fld_pj_no   := P_cst_grp;
        ELSIF UPPER(P_cst_grp) = 'B.ACTV_NO' THEN
            V_fld_actv_no   := P_cst_grp;
        END IF;
        -------------------------------------------------------
        /*
        IF NVL(P_rep_year, 0) = 1 THEN
            SELECT TO_DATE(TO_CHAR(Ys_gen_pkg.Get_frst_day, 'dd/mm') || '/' || EXTRACT(YEAR FROM Ys_gen_pkg.Get_frst_day - INTERVAL '1' YEAR), 'DD/MM/YYYY')
              INTO V_last_yr_frst_dy
              FROM DUAL;
            V_fd_whr   := ' And B.Doc_Date>=To_Date(''' || V_last_yr_frst_dy || ''',''dd/mm/yyyy'') ';
        END IF;
			 */
        --##------------------------------------------------------------------------##--
        IF NVL(P_rep_year, 0) = 0 THEN
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
        --##------------------------------------------------------------------------##--
        IF P_t_date IS NOT NULL THEN
            V_rt_whr    := V_rt_whr  || ' And M.Rt_Bill_Date <=''' || P_t_date || '''';
            V_add_whr   := V_add_whr || ' And M.Doc_Date     <=''' || P_t_date || '''';
        END IF;
        --##------------------------------------------------------------------------##--
        IF NVL(P_rep_year, 0) = 1 OR NVL(P_paid_inst_mnl, 0) = 0 THEN
            IF NVL(P_rep_year, 0) = 1 THEN
                V_tb_nm  := 'IAS_V_POST_DTL_YR';
            ELSE
                V_tb_nm  := 'Ias_Post_Dtl';
            END IF;
        		-----------------------------------------
            IF NVL(P_dr_typ, 0) = 1 THEN
                V_hav   := ' Having Decode(''' || P_local_cur || ''',  A_Cy,(Sum(Dr_Amt) - Sum(Cr_Amt)), (Sum(Dr_Amt_F) - Sum(Cr_Amt_F))) > 0';
            END IF;
        		-----------------------------------------
            BEGIN
                V_sql := 'Select  A.C_Code C_CODE, B.A_Cy A_CY,
													(Nvl(Sum(Dr_Amt), 0) - Nvl(Sum(Cr_Amt), 0)) Bal,
													(Nvl(Sum(Dr_Amt_F), 0) - Nvl(Sum(Cr_Amt_F), 0)) Fbal,
													' || P_cst_grp ||       '  Cst_Grp,
													' || P_sman_grp||       '  Sman_Grp
											 From Customer A,  ' || V_tb_nm || '  B  WHERE 1=1 ' || P_whr || '
											Group By A.C_Code,	B.A_Cy,
													' || P_cst_grp ||  '  ,
													' || P_sman_grp || ' ' || V_hav;
                EXECUTE IMMEDIATE V_sql  BULK COLLECT INTO Cstrec;
            EXCEPTION
                WHEN NO_DATA_FOUND THEN
                    NULL;
                WHEN OTHERS THEN
                    Raise_application_error(-20001, 'Error  ' || SQLCODE || ' : ' || SQLERRM);
            END;
        		-----------------------------------------
            FOR I IN 1 .. Cstrec.COUNT LOOP                                                         --(1)
                ------------------------------------------------------------
                If V_tb_nm =  'Ias_Post_Dtl' Then
						        IF  UPPER(P_WHR) LIKE UPPER('%B.C_V_Code IS NOT NULL%') THEN
						                V_WHR_DOC_TYPE :=' AND (  NVL(DOC_TYPE, 0)<>0
						                                          OR (NVL(DOC_TYPE, 0)=0 AND NVL(AC_DTL_TYP, 0)=4 )
						                                        ) '  ;
						        ELSE
						                V_WHR_DOC_TYPE := ' AND Nvl(DOC_TYPE, 0)<>0 '  ;
						        END IF;
		                V_SQL_INSTLMNT := 'SELECT B.C_Code,
                                        B.A_Cy          A_Cy    ,
                                        B.BILL_NO       Doc_No  ,
                                        B.Doc_Type      Doc_Type,
                                        B.BILL_DOC_TYPE Jv_Type ,
                                        B.BILL_SER      Doc_Ser ,
                                        B.Doc_Date      Doc_Date,
                                        NULL            Doc_Due_Date,
                                        SUM(NVL(I_Amt,0)* NVL(AC_RATE,1))  Dr_Amt  ,
                                        SUM(NVL(I_Amt,0))                  Dr_Amtf ,
                                        NULL            Doc_Desc,
                                        B.Ref_No        Ref_No  ,
                                        B.Rcrd_No       Rcrd_No ,
                                        ' || V_Fld_Cc_Code || ' Cc_Code       ,
                                        ' || V_Fld_Pj_No ||   ' Pj_No         ,
                                        ' || V_Fld_Actv_No || ' Actv_No       ,
                                        ' || P_Sman_Grp ||    ' Rep_Code      ,
                                        NULL                   Cheque_Valued  ,
                                        TO_DATE( ''' || P_T_Date || ''',''DD/MM/YYYY'') -  TO_DATE( B.Doc_Date,''DD/MM/YYYY'') Per_No,
                                        B.Brn_No,
                                        B.Brn_Year,
                                        B.Cmp_No,
                                        B.Brn_Usr
                                   FROM Customer A, INSTALLMENT B
                                  WHERE A.C_Code=B.C_Code AND  Nvl(B.I_amt,0) >0
                                    AND 1 = (CASE WHEN NVL(B.I_Py, 0) = 1 OR NVL(B.Doc_Type, 0) = 0 THEN 1 ELSE 0 END)
                                    AND A.C_Code=''' || Cstrec(I).C_Code || '''
                                    AND B.A_Cy = ''' || Cstrec(I).A_Cy   || '''
                                    AND '|| P_Cst_Grp || ' =''' || Cstrec(I).Cst_Grp ||  '''
                                    AND '|| P_Sman_Grp|| ' =''' || Cstrec(I).Sman_Grp||  '''
                                    AND Doc_Date <= To_Date(''' || P_T_Date || ''',''DD/MM/YYYY'')
                                Group by B.C_Code ,
                                         B.a_Cy,
                                         B.BILL_NO,
                                         B.Doc_Type,
                                         B.BILL_DOC_TYPE,
                                         B.BILL_SER,
                                         B.Doc_Date,
                                         B.Ref_No,
                                         B.Rcrd_No,
                                         ' || V_fld_cc_code ||  ',
                                         ' || V_fld_pj_no   || ',
                                         ' || V_fld_actv_no || ',
                                         ' || P_sman_grp    ||  ',
                                         TO_DATE( ''' || P_t_date || ''',''DD/MM/YYYY'') - TO_DATE(B.Doc_Date,''DD/MM/YYYY'') ,
                                         B.Brn_No,
                                         B.Brn_Year,
                                         B.Cmp_No,
                                         B.Brn_Usr
                        UNION  ';
                END IF;
                ------------------------------------------------------------
                -- Declare
                V_sql2   := 'select * from (With T1(  C_Code,
                                A_Cy,
                                Doc_No,
                                Doc_Type,
                                Jv_Type,
                                Doc_Ser,
                                Doc_Date,
                                Doc_Due_Date,
                                Dr_Amt,
                                Dr_Amtf,
                                Doc_Desc,
                                Ref_No,
                                Rcrd_No,
                                Cc_Code,
                                Pj_No,
                                Actv_No,
                                Rep_Code,
                                Cheque_Valued,Per_No,
                                Brn_No,
                                Brn_Year,
                                Cmp_No,
                                Brn_Usr)
                            As( ('||V_SQL_INSTLMNT||'
                          SELECT
                                A.C_Code,
                                B.A_Cy  ,
                                Doc_No  ,
                                Doc_Type,
                                Jv_Type ,
                                Doc_Ser ,
                                Doc_Date,
                                Doc_Due_Date,
                                SUM (NVL(Dr_Amt  ,0))  Dr_Amt,
                                (SUM(NVL(Dr_Amt_F,0))) Dr_Amtf,
                                Doc_Desc,
                                Ref_No,
                                B.Rcrd_No,
                                ' || V_fld_cc_code || ' Cc_Code,
                                ' || V_fld_pj_no   || ' Pj_No,
                                ' || V_fld_actv_no || ' Actv_No,
                                ' || P_sman_grp    || ' Rep_Code,
                                B.cheque_Valued,
                                TO_DATE('''|| P_t_date ||''',''DD/MM/YYYY'') - TO_DATE(Doc_Date,''DD/MM/YYYY'') Per_No,
                                B.brn_No,
                                B.brn_Year,
                                B.cmp_No,
                                B.brn_Usr
                            FROM Customer A, ' || V_tb_nm || ' B
                           WHERE A.c_Code=''' || Cstrec(I).C_code || '''
                               AND B.a_Cy = ''' || Cstrec(I).A_cy || '''
                              AND Nvl(dr_Amt, 0) > 0         '|| V_WHR_DOC_TYPE ||'
                              AND Doc_Date <= To_Date(''' || P_t_date || ''',''DD/MM/YYYY'') '
                              || P_whr ||  V_fd_whr ||  '
                                 AND ' || P_cst_grp || '  =''' || Cstrec(I).Cst_grp ||   '''
                                 AND ' || P_sman_grp || ' =''' || Cstrec(I).Sman_grp ||  '''
                              Group by A.C_Code ,
                                         B.a_Cy,
                                         Doc_No,
                                         Doc_Type,
                                         Jv_Type,
                                         Doc_Ser,
                                         Doc_Date,
                                         Doc_Due_Date,
                                         Doc_Desc,
                                         Ref_No,
                                         B.rcrd_No,
                                         ' || V_fld_cc_code ||  ',
                                         ' || V_fld_pj_no || ',
                                         ' || V_fld_actv_no || ',
                                         ' || P_sman_grp ||  ',
                                          B.cheque_Valued,
                                         TO_DATE( ''' || P_t_date || ''',''DD/MM/YYYY'') - TO_DATE(Doc_Date,''DD/MM/YYYY'') ,
                                         B.brn_No,
                                         B.brn_Year,
                                         B.cmp_No,
                                         B.brn_Usr
                                ) ORDER BY c_Code,
                                        a_Cy,
                                        doc_Date Desc
                             )
                    SELECT
                      C_Code,
                      A_Cy,
                      Doc_No,
                      Doc_Type,
                      Jv_Type,
                      Doc_Ser,
                      Doc_Date,
                      Doc_Due_Date,
                      Nvl(Dr_Amt,0)-( case when ' || V_cc_pj_actv || '=0    Then 0
                                             else Nvl(Rt_AmtL,0)  end ) Dr_Amt,
                      Nvl(Dr_AmtF,0)-( case when A_Cy =''' || P_local_cur || ''' Then 0
                                              when ' || V_cc_pj_actv || '=0    Then 0
                                             else Nvl(Rt_Amt,0)  end )  Dr_Amtf,
                      Doc_Desc,
                      Ref_No,
                      Rcrd_No,
                      Cc_Code,
                      Pj_No,
                      Actv_No,
                      Rep_Code,
                      Cheque_Valued,Per_No,
                      Brn_No,
                      Brn_Year,
                      Cmp_No,
                      Brn_Usr
                    From T1,(Select Bill_Ser,nvl(Sum(Dtl_Amt * Per_Amt),0) Rt_Amt,nvl(Sum(Dtl_Amt_L * Per_Amt),0) Rt_AmtL
                              From (Select Rt_Bill_no,
                                           Rt_Bill_Ser,
                                           Bill_Ser,
                                           bill_no,
                                           Cc_Code,
                                           Pj_No,
                                           Actv_No,
                                           Rt_Bill_Date,
                                           Rt_Bill_Rate,
                                           Nvl(Dtl_Amt,0)* Nvl(Rt_Bill_Rate,1)  Dtl_Amt_L,   ---  (Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser ) * Nvl(Rt_Bill_Rate,1)  ) Dtl_Amt_L,
                                           Ac_Amt,
                                           Dtl_Amt,
                                           ((Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)- Ac_Amt)/Decode(Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser),0,1,Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)) ) Per_Amt
                                      From (Select m.rt_Bill_no,
                                                   m.rt_Bill_Ser,
                                                   D.Bill_Ser,
                                                   bill_no,
                                                   D.Cc_Code,
                                                   D.Pj_No,
                                                   D.Actv_No,
                                                   M.Rt_Bill_Date,
                                                   M.Rt_Bill_Rate,
                                                   Nvl((Nvl(D.I_Qty, 0) * (Nvl(D.I_Price, 0) - Nvl(D.Dis_Amt, 0) + Nvl(D.Vat_Amt, 0) + Nvl(D.Othr_Amt, 0))), 0) Dtl_Amt,
                                                   ((Nvl(M.Cr_Card_Amt, 0) + Nvl(M.Cr_Card_Amt_Scnd, 0) + Nvl(M.Cr_Card_Amt_Thrd, 0)) + Nvl(M.Ac_Amt, 0)) Ac_Amt
                                              From ' || V_tbl_rt_mst || ' M, ' ||V_tbl_rt_dtl || ' D
                                             Where M.Rt_Bill_Ser = D.Rt_Bill_Ser
                                                   And M.Rt_Bill_Doc_Type = 4
                                                   And M.P_Year In (0, 3) ' || V_rt_whr ||  '
                                           Union ALL
                                             Select m.DOC_NO  rt_Bill_no ,
                                                    m.DOC_SER rt_Bill_Ser,
                                                    D.Bill_Ser	,
                                                    D.bill_no	,
                                                    M.Cc_Code	,
                                                    M.Pj_No		,
                                                    M.Actv_No	,
                                                    M.DOC_DATE Rt_Bill_Date,
                                                    M.DOC_RATE Rt_Bill_Rate,
                                                    Nvl(D.ADD_DIS_QTY, 0) * Nvl(D.ADD_DIS_AMT_DTL, 0)+(Nvl(D.Add_Dis_Qty,0)*Nvl(D.ADD_VAT_AMT,0)) Dtl_Amt,
                                                    0 Ac_Amt
                                                 From ' || V_tbl_add_mst || ' M, '|| V_tbl_add_dtl || ' D
                                                Where M.DOC_SER = D.DOC_SER AND NVL(NOTE_TYP,0)=1
                                                  And M.BILL_DOC_TYPE = 4 ' || V_add_whr || '
                                              )
                                       ) Group By Bill_Ser) Rt
                                       Where Rt.Bill_Ser(+) = T1.Doc_Ser)
                     where nvl(Dr_Amt,0)>0 or nvl(Dr_Amtf,0)>0
                        Order By C_Code,
                                 A_Cy,
                                 Doc_Date Desc ';

                -- INSERT INTO TST_BA(cb)VALUES(V_SQL2);
                -- COMMIT;

                BEGIN
                    EXECUTE IMMEDIATE V_sql2  BULK COLLECT INTO Cstrec_2;
                EXCEPTION
                    WHEN NO_DATA_FOUND THEN
                        NULL;
                    WHEN OTHERS THEN
                        Raise_application_error(-20002, 'Error2  ' || SQLCODE || ' : ' || SQLERRM);
                END;

                BEGIN
                    V_dr        := 0;
                    V_drf       := 0;
                    V_dr_rem    := 0;
                    V_drf_rem   := 0;

                    FOR J IN 1 .. Cstrec_2.COUNT LOOP                                               --(2)
                        IF Cstrec(I).A_cy = P_local_cur THEN                                  --(1) Local
                            V_dr   := V_dr + Cstrec_2(J).Dr_amt;

                            IF Cstrec(I).Bal >= V_dr THEN
                                IF ((Chk_prd_no(P_prd_no => Cstrec_2(J).Per_no, P_per_no => P_per_no, P_f_day => P_f_day, P_t_day => P_t_day) = 1 OR NVL(P_per_no, 0) = 0) AND NVL(P_rep_year, 0) = 1)
                                   OR NVL(P_rep_year, 0) = 0 THEN
                                    INSERT INTO Ias_cst_cr_tmp(C_code, A_cy, Doc_no, Doc_type, Doc_jv_type, Doc_ser, Doc_date, Doc_due_date, Dr_amt, Dr_amtf, Doc_desc, Ref_no, Rcrd_no, Cc_code,
                                                                Pj_no, Actv_no, Rep_code, Cheque_valued, Per_no, Trmnl_name, Brn_no, Brn_year, Cmp_no, Brn_usr
                                                              )
                                             VALUES (Cstrec_2(J).C_code,
                                                     Cstrec_2(J).A_cy,
                                                     Cstrec_2(J).Doc_no,
                                                     Cstrec_2(J).Doc_type,
                                                     Cstrec_2(J).Jv_type,
                                                     Cstrec_2(J).Doc_ser,
                                                     Cstrec_2(J).Doc_date,
                                                     Cstrec_2(J).Doc_due_date,
                                                     Cstrec_2(J).Dr_amt,
                                                     0,
                                                     Cstrec_2(J).Doc_desc,
                                                     Cstrec_2(J).Ref_no,
                                                     Cstrec_2(J).Rcrd_no,
                                                     Cstrec_2(J).Cc_code,
                                                     Cstrec_2(J).Pj_no,
                                                     Cstrec_2(J).Actv_no,
                                                     Cstrec_2(J).Rep_code,
                                                     Cstrec_2(J).Cheque_valued,
                                                     Cstrec_2(J).Per_no,
                                                     P_terminal,
                                                     Cstrec_2(J).Brn_no,
                                                     Cstrec_2(J).Brn_year,
                                                     Cstrec_2(J).Cmp_no,
                                                     Cstrec_2(J).Brn_usr);
                                END IF;
                            ELSE
                                IF V_dr - Cstrec_2(J).Dr_amt = Cstrec(I).Bal THEN
                                    EXIT;
                                ELSIF V_dr > Cstrec(I).Bal THEN
                                    V_dr_rem   := (Cstrec(I).Bal - (V_dr - Cstrec_2(J).Dr_amt));
                                ELSE
                                    V_dr_rem   := Cstrec(I).Bal;
                                END IF;

                                IF ((Chk_prd_no(P_prd_no => Cstrec_2(J).Per_no, P_per_no => P_per_no, P_f_day => P_f_day, P_t_day => P_t_day) = 1 OR NVL(P_per_no, 0) = 0) AND NVL(P_rep_year, 0) = 1)
                                   OR NVL(P_rep_year, 0) = 0 THEN
                                    INSERT INTO Ias_cst_cr_tmp(C_code, A_cy, Doc_no, Doc_type, Doc_jv_type, Doc_ser, Doc_date, Doc_due_date, Dr_amt, Dr_amtf, Doc_desc, Ref_no, Rcrd_no,
                                                                Cc_code, Pj_no, Actv_no, Rep_code, Cheque_valued, Per_no, Trmnl_name , Brn_no, Brn_year, Cmp_no, Brn_usr
                                                              )
                                             VALUES (Cstrec_2(J).C_code,
                                                     Cstrec_2(J).A_cy,
                                                     Cstrec_2(J).Doc_no,
                                                     Cstrec_2(J).Doc_type,
                                                     Cstrec_2(J).Jv_type,
                                                     Cstrec_2(J).Doc_ser,
                                                     Cstrec_2(J).Doc_date,
                                                     Cstrec_2(J).Doc_due_date,
                                                     V_dr_rem,
                                                     0,
                                                     Cstrec_2(J).Doc_desc,
                                                     Cstrec_2(J).Ref_no,
                                                     Cstrec_2(J).Rcrd_no,
                                                     Cstrec_2(J).Cc_code,
                                                     Cstrec_2(J).Pj_no,
                                                     Cstrec_2(J).Actv_no,
                                                     Cstrec_2(J).Rep_code,
                                                     Cstrec_2(J).Cheque_valued,
                                                     Cstrec_2(J).Per_no,
                                                     P_terminal,
                                                     Cstrec_2(J).Brn_no,
                                                     Cstrec_2(J).Brn_year,
                                                     Cstrec_2(J).Cmp_no,
                                                     Cstrec_2(J).Brn_usr);
                                END IF;

                                EXIT;
                            END IF;
                        ELSE                                                                --(1) Foreign
                            V_drf   := V_drf + Cstrec_2(J).Dr_amtf;

                            IF Cstrec(I).Fbal >= V_drf THEN
                                IF ((Chk_prd_no(P_prd_no => Cstrec_2(J).Per_no, P_per_no => P_per_no, P_f_day => P_f_day, P_t_day => P_t_day) = 1 OR NVL(P_per_no, 0) = 0) AND NVL(P_rep_year, 0) = 1)
                                   OR NVL(P_rep_year, 0) = 0 THEN
                                    INSERT INTO Ias_cst_cr_tmp(C_code, A_cy, Doc_no, Doc_type, Doc_jv_type, Doc_ser, Doc_date, Doc_due_date, Dr_amt, Dr_amtf, Doc_desc, Ref_no, Rcrd_no,
                                                                Cc_code, Pj_no, Actv_no, Rep_code, Cheque_valued, Per_no, Trmnl_name , Brn_no, Brn_year, Cmp_no, Brn_usr
                                                              )
                                             VALUES (Cstrec_2(J).C_code,
                                                     Cstrec_2(J).A_cy,
                                                     Cstrec_2(J).Doc_no,
                                                     Cstrec_2(J).Doc_type,
                                                     Cstrec_2(J).Jv_type,
                                                     Cstrec_2(J).Doc_ser,
                                                     Cstrec_2(J).Doc_date,
                                                     Cstrec_2(J).Doc_due_date,
                                                     Cstrec_2(J).Dr_amt,
                                                     Cstrec_2(J).Dr_amtf,
                                                     Cstrec_2(J).Doc_desc,
                                                     Cstrec_2(J).Ref_no,
                                                     Cstrec_2(J).Rcrd_no,
                                                     Cstrec_2(J).Cc_code,
                                                     Cstrec_2(J).Pj_no,
                                                     Cstrec_2(J).Actv_no,
                                                     Cstrec_2(J).Rep_code,
                                                     Cstrec_2(J).Cheque_valued,
                                                     Cstrec_2(J).Per_no,
                                                     P_terminal,
                                                     Cstrec_2(J).Brn_no,
                                                     Cstrec_2(J).Brn_year,
                                                     Cstrec_2(J).Cmp_no,
                                                     Cstrec_2(J).Brn_usr);
                                END IF;
                            ELSE
                                IF V_drf - Cstrec_2(J).Dr_amtf = Cstrec(I).Fbal THEN
                                    EXIT;
                                ELSIF V_drf > Cstrec(I).Fbal THEN
                                    V_drf_rem   := (Cstrec(I).Fbal - (V_drf - Cstrec_2(J).Dr_amtf));
                                ELSE
                                    V_drf_rem   := Cstrec(I).Fbal;
                                END IF;

                                IF Cstrec_2(J).Dr_amtf > 0 THEN
                                    V_ex_rate   := Cstrec_2(J).Dr_amt / Cstrec_2(J).Dr_amtf;
                                END IF;

                                IF ((Chk_prd_no(P_prd_no => Cstrec_2(J).Per_no, P_per_no => P_per_no, P_f_day => P_f_day, P_t_day => P_t_day) = 1 OR NVL(P_per_no, 0) = 0) AND NVL(P_rep_year, 0) = 1)
                                   OR NVL(P_rep_year, 0) = 0 THEN
                                    INSERT INTO Ias_cst_cr_tmp(C_code, A_cy, Doc_no, Doc_type, Doc_jv_type, Doc_ser, Doc_date, Doc_due_date, Dr_amt, Dr_amtf, Doc_desc, Ref_no, Rcrd_no, Cc_code, Pj_no, Actv_no, Rep_code, Cheque_valued, Per_no, Trmnl_name
                                                               , Brn_no, Brn_year, Cmp_no
                                                              )
                                             VALUES (Cstrec_2(J).C_code,
                                                     Cstrec_2(J).A_cy,
                                                     Cstrec_2(J).Doc_no,
                                                     Cstrec_2(J).Doc_type,
                                                     Cstrec_2(J).Jv_type,
                                                     Cstrec_2(J).Doc_ser,
                                                     Cstrec_2(J).Doc_date,
                                                     Cstrec_2(J).Doc_due_date,
                                                     (V_drf_rem * V_ex_rate),
                                                     V_drf_rem,
                                                     Cstrec_2(J).Doc_desc,
                                                     Cstrec_2(J).Ref_no,
                                                     Cstrec_2(J).Rcrd_no,
                                                     Cstrec_2(J).Cc_code,
                                                     Cstrec_2(J).Pj_no,
                                                     Cstrec_2(J).Actv_no,
                                                     Cstrec_2(J).Rep_code,
                                                     Cstrec_2(J).Cheque_valued,
                                                     Cstrec_2(J).Per_no,
                                                     P_terminal,
                                                     Cstrec_2(J).Brn_no,
                                                     Cstrec_2(J).Brn_year,
                                                     Cstrec_2(J).Cmp_no);
                                END IF;

                                EXIT;
                            END IF;
                        END IF;                                                                     --(1)
                    END LOOP;
                END;
            END LOOP;                                                                              --(1);
        --  END;

        ELSE
            V_sql   :=

                'Insert Into IAS_CST_CR_TMP( C_CODE, A_CY, DOC_NO, DOC_TYPE, DOC_JV_TYPE, DOC_SER, DOC_DATE,DOC_DUE_DATE, DR_AMT, DR_AMTF, DOC_DESC,
                                                       REF_NO, RCRD_NO, CC_CODE,PJ_NO,ACTV_NO,CHEQUE_VALUED,PER_NO,TRMNL_NAME,BRN_NO,BRN_YEAR,CMP_NO,BRN_USR)
                SELECT B.C_CODE,B.A_CY,B.BILL_NO DOC_NO,B.DOC_TYPE,B.BILL_DOC_TYPE DOC_JV_TYPE,B.BILL_SER DOC_SER,
                       B.DOC_DATE,B.I_DATE,(NVL(B.I_AMT,0)-(NVL(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0))) DR_AMT,DECODE(B.A_CY,''' || P_local_cur ||''',NULL,(NVL(B.I_AMT,0)-(NVL(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0)))) DR_AMTF,
                       NULL DOC_DESC,B.REF_NO,B.RCRD_NO,B.CC_CODE,B.PJ_NO,B.ACTV_NO, NULL CHEQUE_VALUED,(TO_DATE(''' || P_t_date || ''',''DD/MM/YYYY'')-NVL(B.DOC_DATE,IAS_GEN_PKG.GET_FRST_DAY)) PER_NO,'''|| P_terminal ||''' TRMNL_NAME,
                       B.BRN_NO,B.BRN_YEAR,B.CMP_NO,B.BRN_USR
                FROM CUSTOMER A,INSTALLMENT B
                WHERE A.C_CODE=B.C_CODE
                AND NVL(B.I_AMT,0)>(NVL(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0))
                AND B.DR_NO IS NULL ' || P_whr;

            -- INSERT INTO TST_BA(SQL_V)VALUES(V_SQL);
            -- COMMIT;

            EXECUTE IMMEDIATE V_sql;
        END IF;
    END Cst_aging_prc;

--##-------------------------------------------------------------------------------##--
PROCEDURE Cst_parnt_aging_prc ( P_local_cur IN VARCHAR2,
                                P_paid_inst_mnl IN NUMBER DEFAULT 0,
                                P_cst_grp IN VARCHAR2 DEFAULT NULL,
                                P_sman_grp IN VARCHAR2 DEFAULT NULL,
                                P_rep_year IN NUMBER DEFAULT 0,
                                P_per_no IN NUMBER DEFAULT NULL,
                                P_f_day IN NUMBER DEFAULT NULL,
                                P_t_day IN NUMBER DEFAULT NULL,
                                P_t_date IN DATE,
                                P_terminal IN VARCHAR2 DEFAULT NULL,
                                P_whr IN VARCHAR2 DEFAULT NULL,
                                P_dr_typ IN NUMBER DEFAULT 1) IS
        V_sql            VARCHAR2(32000);
        V_sql2           VARCHAR2(32000);
        V_dr             NUMBER := 0;
        V_drf            NUMBER := 0;
        V_dr_rem         NUMBER := 0;
        V_drf_rem        NUMBER := 0;
        V_ex_rate        NUMBER := 0;
        V_st             BOOLEAN := TRUE;
        V_stat           VARCHAR2(500);
        V_trmnlname      VARCHAR2(100) := USERENV('TERMINAL');
        V_cst_grp        VARCHAR2(1000);
        V_sman_grp       VARCHAR2(100);
        V_tb_nm          VARCHAR2(100);
        V_fld_cc_code    VARCHAR2(100) := 'NULL';
        V_fld_pj_no      VARCHAR2(100) := 'NULL';
        V_fld_actv_no    VARCHAR2(100) := 'NULL';
        V_ar_cs_type     NUMBER := 0;
        V_ar_pj_type     NUMBER := 0;
        V_ar_actv_type   NUMBER := 0;
        V_cc_pj_actv     NUMBER := 0;
        V_hav            VARCHAR2(1000) := ' ';
    BEGIN
        EXECUTE IMMEDIATE 'Truncate Table Ias_cst_cr_tmp';

        -------------------------------------------------------
        BEGIN
            SELECT NVL(Ar_cs_type, 0), NVL(Ar_pj_type, 0), NVL(Ar_actv_type, 0)
              INTO V_ar_cs_type, V_ar_pj_type, V_ar_actv_type
              FROM Ias_para_ar;
        EXCEPTION
            WHEN OTHERS THEN
                NULL;
        END;

        -------------------------------------------------------     ;
        IF NVL(V_ar_cs_type, 0) <> 2 AND NVL(V_ar_pj_type, 0) <> 2 AND NVL(V_ar_actv_type, 0) <> 2 THEN
            V_cc_pj_actv   := 1;
        ELSE
            V_cc_pj_actv   := 0;
        END IF;

        -------------------------------------------------------
        IF UPPER(P_cst_grp) = 'B.CC_CODE' THEN
            V_fld_cc_code   := P_cst_grp;
        ELSIF UPPER(P_cst_grp) = 'B.PJ_NO' THEN
            V_fld_pj_no   := P_cst_grp;
        ELSIF UPPER(P_cst_grp) = 'B.ACTV_NO' THEN
            V_fld_actv_no   := P_cst_grp;
        END IF;

        -------------------------------------------------------
        ----IF NVL(P_Rep_Year,0)=1 OR  NVL(P_Paid_Inst_MNL,0)=0 THEN
        IF NVL(P_paid_inst_mnl, 0) = 0 THEN
            IF NVL(P_rep_year, 0) = 1 THEN
                V_tb_nm   := 'IAS_V_POST_DTL_YR';
            ELSE
                V_tb_nm   := 'Ias_Post_Dtl';
            END IF;

            ------------------------------------------------

            IF NVL(P_dr_typ, 0) = 1 THEN
                V_hav   := ' Having Decode(''' || P_local_cur || ''',  A_Cy,(Sum(Dr_Amt) - Sum(Cr_Amt)),  (Sum(Dr_Amt_F) - Sum(Cr_Amt_F))) > 0 ';
            END IF;

            BEGIN
                V_sql   :=
                    'Select Nvl(A.C_parent,b.C_CODE)  C_CODE,
                                                   B.A_Cy A_CY,
                                                   (Nvl(Sum(Dr_Amt), 0) - Nvl(Sum(Cr_Amt), 0)) Bal,
                                                   (Nvl(Sum(Dr_Amt_F), 0) - Nvl(Sum(Cr_Amt_F), 0)) Fbal,
                                                    ' || P_cst_grp ||           '  Cst_Grp,
                                                   ' || P_sman_grp ||           '  Sman_Grp
                                              From Customer A, ' || V_tb_nm ||    '  B
                    WHERE 1=1 And Exists (select 1 from customer where C_parent=nvl(A.C_parent,b.C_CODE) And Rownum <= 1 ) '
                    || P_whr || '
                      Group By Nvl(A.C_parent,B.C_CODE) ,
                               B.A_Cy, '
                               || P_cst_grp ||' ,'
                               || P_sman_grp || ' '
                               || V_hav;

                --  COMMIT;
                EXECUTE IMMEDIATE V_sql BULK COLLECT INTO Cstrec;
            EXCEPTION
                WHEN NO_DATA_FOUND THEN
                    NULL;
                WHEN OTHERS THEN
                    NULL;
                    Raise_application_error(-20001, 'Error  ' || SQLCODE || ' : ' || SQLERRM);
            END;

            FOR I IN 1 .. Cstrec.COUNT LOOP                                                         --(1)
                -- Declare
                V_sql2   :=
                    'select *
                         from (Select        Nvl(A.C_parent,b.C_CODE)  C_Code,
                                             B.A_Cy,
                                             Doc_No,
                                             Doc_Type,
                                             Jv_Type,
                                             Doc_Ser,
                                             Doc_Date,
                                             Doc_Due_Date,
                                            ( sum(Nvl(Dr_Amt, 0)) -( case   when ' || V_cc_pj_actv || '=0    Then 0
                                                                            else  0 end ) )Dr_Amt,
                                             (sum(Nvl(Dr_Amt_F, 0))- ( case when B.A_Cy =''' || P_local_cur || ''' Then 0
                                                                            when ' || V_cc_pj_actv || '=0          Then 0
                                                                            else  0 end ) )Dr_Amtf,
                                             Doc_Desc,
                                             Ref_No,
                                             B.Rcrd_No,
                                             ' || V_fld_cc_code ||          ' Cc_Code,
                                             ' || V_fld_pj_no ||            '  Pj_No,
                                             ' || V_fld_actv_no ||          ' Actv_No,
                                             ' || P_sman_grp ||             ' Rep_Code,
                                             B.Cheque_Valued,
                                             TO_DATE(''' || P_t_date || ''',''DD/MM/YYYY'') - Doc_Date Per_No,
                                             B.Brn_No,
                                             B.Brn_Year,
                                             B.Cmp_No,
                                             B.Brn_Usr
                                        From Customer A, ' || V_tb_nm || '  B
                                       Where   A.c_code=B.AC_CODE_DTL
                                          and AC_DTL_TYP=3
                                          AND  Nvl(A.C_parent,A.C_code) =''' || Cstrec(I).C_code || '''
                                           And B.A_Cy = ''' || Cstrec(I).A_cy ||'''
                                          And ( Nvl(Dr_Amt, 0) > 0  or ' || NVL(P_dr_typ, 0) ||  '=0 )
                                          And Doc_Date <= ''' || P_t_date ||  '''
                                             And ' || P_cst_grp || '  =''' || Cstrec(I).Cst_grp || '''
                                             And ' || P_sman_grp || ' =''' || Cstrec(I).Sman_grp ||'''
                                          Group by  Nvl(A.C_parent,b.C_CODE) ,
                                                     B.A_Cy,
                                                     Doc_No,
                                                     Doc_Type,
                                                     Jv_Type,
                                                     Doc_Ser,
                                                     Doc_Date,
                                                     Doc_Due_Date,
                                                     Doc_Desc,
                                                     Ref_No,
                                                     B.Rcrd_No,
                                                     ' || V_fld_cc_code || ' ,
                                                     ' || V_fld_pj_no ||  '  ,
                                                     ' || V_fld_actv_no ||'  ,
                                                     ' || P_sman_grp ||  ' ,
                                                      B.Cheque_Valued,
                                                     TO_DATE(''' || P_t_date || ''',''DD/MM/YYYY'') - Doc_Date ,
                                                     B.Brn_No,
                                                     B.Brn_Year,
                                                     B.Cmp_No,
                                                     B.Brn_Usr
                                            Order By A.c_parent,
                                             B.A_Cy,
                                             B.Doc_Date Desc)
                                             where nvl(Dr_Amt,0)>0 or nvl(Dr_Amtf,0)>0  or ' || NVL( P_dr_typ, 0) ||'=0
                                                Order By C_code,
                                                         A_Cy,
                                                         Doc_Date Desc ';


                BEGIN
                    EXECUTE IMMEDIATE V_sql2 BULK COLLECT INTO Cstrec_2;
                EXCEPTION
                    WHEN NO_DATA_FOUND THEN
                        NULL;
                    WHEN OTHERS THEN
                        Raise_application_error(-20002, 'Error2  ' || SQLCODE || ' : ' || SQLERRM);
                END;

                BEGIN
                    V_dr        := 0;
                    V_drf       := 0;
                    V_dr_rem    := 0;
                    V_drf_rem   := 0;

                    FOR J IN 1 .. Cstrec_2.COUNT LOOP                                               --(2)
                        IF Cstrec(I).A_cy = P_local_cur THEN                                  --(1) Local
                            V_dr   := V_dr + Cstrec_2(J).Dr_amt;

                            IF Cstrec(I).Bal >= V_dr THEN
                                IF ((Chk_prd_no(P_prd_no => Cstrec_2(J).Per_no, P_per_no => P_per_no, P_f_day => P_f_day, P_t_day => P_t_day) = 1 OR NVL(P_per_no, 0) = 0) AND NVL(P_rep_year, 0) = 1)
                                   OR NVL(P_rep_year, 0) = 0 THEN
                                    INSERT INTO Ias_cst_cr_tmp(C_code, A_cy, Doc_no, Doc_type, Doc_jv_type, Doc_ser, Doc_date, Doc_due_date, Dr_amt, Dr_amtf, Doc_desc, Ref_no, Rcrd_no, Cc_code, Pj_no, Actv_no, Rep_code, Cheque_valued, Per_no, Trmnl_name
                                                               , Brn_no, Brn_year, Cmp_no, Brn_usr
                                                              )
                                             VALUES (Cstrec_2(J).C_code,
                                                     Cstrec_2(J).A_cy,
                                                     Cstrec_2(J).Doc_no,
                                                     Cstrec_2(J).Doc_type,
                                                     Cstrec_2(J).Jv_type,
                                                     Cstrec_2(J).Doc_ser,
                                                     Cstrec_2(J).Doc_date,
                                                     Cstrec_2(J).Doc_due_date,
                                                     Cstrec_2(J).Dr_amt,
                                                     0,
                                                     Cstrec_2(J).Doc_desc,
                                                     Cstrec_2(J).Ref_no,
                                                     Cstrec_2(J).Rcrd_no,
                                                     Cstrec_2(J).Cc_code,
                                                     Cstrec_2(J).Pj_no,
                                                     Cstrec_2(J).Actv_no,
                                                     Cstrec_2(J).Rep_code,
                                                     Cstrec_2(J).Cheque_valued,
                                                     Cstrec_2(J).Per_no,
                                                     P_terminal,
                                                     Cstrec_2(J).Brn_no,
                                                     Cstrec_2(J).Brn_year,
                                                     Cstrec_2(J).Cmp_no,
                                                     Cstrec_2(J).Brn_usr);
                                END IF;
                            ELSE
                                IF V_dr - Cstrec_2(J).Dr_amt = Cstrec(I).Bal THEN
                                    EXIT;
                                ELSIF V_dr > Cstrec(I).Bal THEN
                                    V_dr_rem   := (Cstrec(I).Bal - (V_dr - Cstrec_2(J).Dr_amt));
                                ELSE
                                    V_dr_rem   := Cstrec(I).Bal;
                                END IF;

                                IF ((Chk_prd_no(P_prd_no => Cstrec_2(J).Per_no, P_per_no => P_per_no, P_f_day => P_f_day, P_t_day => P_t_day) = 1 OR NVL(P_per_no, 0) = 0) AND NVL(P_rep_year, 0) = 1)
                                   OR NVL(P_rep_year, 0) = 0 THEN
                                    INSERT INTO Ias_cst_cr_tmp(C_code, A_cy, Doc_no, Doc_type, Doc_jv_type, Doc_ser, Doc_date, Doc_due_date, Dr_amt, Dr_amtf, Doc_desc, Ref_no, Rcrd_no, Cc_code, Pj_no, Actv_no, Rep_code, Cheque_valued, Per_no, Trmnl_name
                                                               , Brn_no, Brn_year, Cmp_no, Brn_usr
                                                              )
                                             VALUES (Cstrec_2(J).C_code,
                                                     Cstrec_2(J).A_cy,
                                                     Cstrec_2(J).Doc_no,
                                                     Cstrec_2(J).Doc_type,
                                                     Cstrec_2(J).Jv_type,
                                                     Cstrec_2(J).Doc_ser,
                                                     Cstrec_2(J).Doc_date,
                                                     Cstrec_2(J).Doc_due_date,
                                                     V_dr_rem,
                                                     0,
                                                     Cstrec_2(J).Doc_desc,
                                                     Cstrec_2(J).Ref_no,
                                                     Cstrec_2(J).Rcrd_no,
                                                     Cstrec_2(J).Cc_code,
                                                     Cstrec_2(J).Pj_no,
                                                     Cstrec_2(J).Actv_no,
                                                     Cstrec_2(J).Rep_code,
                                                     Cstrec_2(J).Cheque_valued,
                                                     Cstrec_2(J).Per_no,
                                                     P_terminal,
                                                     Cstrec_2(J).Brn_no,
                                                     Cstrec_2(J).Brn_year,
                                                     Cstrec_2(J).Cmp_no,
                                                     Cstrec_2(J).Brn_usr);
                                END IF;

                                EXIT;
                            END IF;
                        ELSE                                                                --(1) Foreign
                            V_drf   := V_drf + Cstrec_2(J).Dr_amtf;

                            IF Cstrec(I).Fbal >= V_drf THEN
                                IF ((Chk_prd_no(P_prd_no => Cstrec_2(J).Per_no, P_per_no => P_per_no, P_f_day => P_f_day, P_t_day => P_t_day) = 1 OR NVL(P_per_no, 0) = 0) AND NVL(P_rep_year, 0) = 1)
                                   OR NVL(P_rep_year, 0) = 0 THEN
                                    INSERT INTO Ias_cst_cr_tmp(C_code, A_cy, Doc_no, Doc_type, Doc_jv_type, Doc_ser, Doc_date, Doc_due_date, Dr_amt, Dr_amtf, Doc_desc, Ref_no, Rcrd_no, Cc_code, Pj_no, Actv_no, Rep_code, Cheque_valued, Per_no, Trmnl_name
                                                               , Brn_no, Brn_year, Cmp_no, Brn_usr
                                                              )
                                             VALUES (Cstrec_2(J).C_code,
                                                     Cstrec_2(J).A_cy,
                                                     Cstrec_2(J).Doc_no,
                                                     Cstrec_2(J).Doc_type,
                                                     Cstrec_2(J).Jv_type,
                                                     Cstrec_2(J).Doc_ser,
                                                     Cstrec_2(J).Doc_date,
                                                     Cstrec_2(J).Doc_due_date,
                                                     Cstrec_2(J).Dr_amt,
                                                     Cstrec_2(J).Dr_amtf,
                                                     Cstrec_2(J).Doc_desc,
                                                     Cstrec_2(J).Ref_no,
                                                     Cstrec_2(J).Rcrd_no,
                                                     Cstrec_2(J).Cc_code,
                                                     Cstrec_2(J).Pj_no,
                                                     Cstrec_2(J).Actv_no,
                                                     Cstrec_2(J).Rep_code,
                                                     Cstrec_2(J).Cheque_valued,
                                                     Cstrec_2(J).Per_no,
                                                     P_terminal,
                                                     Cstrec_2(J).Brn_no,
                                                     Cstrec_2(J).Brn_year,
                                                     Cstrec_2(J).Cmp_no,
                                                     Cstrec_2(J).Brn_usr);
                                END IF;
                            ELSE
                                IF V_drf - Cstrec_2(J).Dr_amtf = Cstrec(I).Fbal THEN
                                    EXIT;
                                ELSIF V_drf > Cstrec(I).Fbal THEN
                                    V_drf_rem   := (Cstrec(I).Fbal - (V_drf - Cstrec_2(J).Dr_amtf));
                                ELSE
                                    V_drf_rem   := Cstrec(I).Fbal;
                                END IF;

                                IF Cstrec_2(J).Dr_amtf > 0 THEN
                                    V_ex_rate   := Cstrec_2(J).Dr_amt / Cstrec_2(J).Dr_amtf;
                                END IF;

                                IF ((Chk_prd_no(P_prd_no => Cstrec_2(J).Per_no, P_per_no => P_per_no, P_f_day => P_f_day, P_t_day => P_t_day) = 1 OR NVL(P_per_no, 0) = 0) AND NVL(P_rep_year, 0) = 1)
                                   OR NVL(P_rep_year, 0) = 0 THEN
                                    INSERT INTO Ias_cst_cr_tmp(C_code, A_cy, Doc_no, Doc_type, Doc_jv_type, Doc_ser, Doc_date, Doc_due_date, Dr_amt, Dr_amtf, Doc_desc, Ref_no, Rcrd_no, Cc_code, Pj_no, Actv_no, Rep_code, Cheque_valued, Per_no, Trmnl_name
                                                               , Brn_no, Brn_year, Cmp_no
                                                              )
                                             VALUES (Cstrec_2(J).C_code,
                                                     Cstrec_2(J).A_cy,
                                                     Cstrec_2(J).Doc_no,
                                                     Cstrec_2(J).Doc_type,
                                                     Cstrec_2(J).Jv_type,
                                                     Cstrec_2(J).Doc_ser,
                                                     Cstrec_2(J).Doc_date,
                                                     Cstrec_2(J).Doc_due_date,
                                                     (V_drf_rem * V_ex_rate),
                                                     V_drf_rem,
                                                     Cstrec_2(J).Doc_desc,
                                                     Cstrec_2(J).Ref_no,
                                                     Cstrec_2(J).Rcrd_no,
                                                     Cstrec_2(J).Cc_code,
                                                     Cstrec_2(J).Pj_no,
                                                     Cstrec_2(J).Actv_no,
                                                     Cstrec_2(J).Rep_code,
                                                     Cstrec_2(J).Cheque_valued,
                                                     Cstrec_2(J).Per_no,
                                                     P_terminal,
                                                     Cstrec_2(J).Brn_no,
                                                     Cstrec_2(J).Brn_year,
                                                     Cstrec_2(J).Cmp_no);
                                END IF;

                                EXIT;
                            END IF;
                        END IF;                                                                     --(1)
                    END LOOP;
                END;
            END LOOP;                                                                              --(1);
        --  END;
        ELSE
            V_sql   :=

                'Insert Into IAS_CST_CR_TMP( C_CODE, A_CY, DOC_NO, DOC_TYPE, DOC_JV_TYPE, DOC_SER, DOC_DATE,DOC_DUE_DATE, DR_AMT, DR_AMTF, DOC_DESC,
                                                       REF_NO, RCRD_NO, CC_CODE,PJ_NO,ACTV_NO,CHEQUE_VALUED,PER_NO,TRMNL_NAME,BRN_NO,BRN_YEAR,CMP_NO,BRN_USR)
        SELECT  B.C_CODE,B.A_CY,B.BILL_NO DOC_NO,B.DOC_TYPE,B.BILL_DOC_TYPE DOC_JV_TYPE,B.BILL_SER DOC_SER,
                           B.DOC_DATE,B.I_DATE,(NVL(B.I_AMT,0)-(NVL(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0))) DR_AMT,DECODE(B.A_CY,'''|| P_local_cur ||  ''',NULL,(NVL(B.I_AMT,0)-(NVL(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0)))) DR_AMTF,
                           NULL DOC_DESC,B.REF_NO,B.RCRD_NO,B.CC_CODE,B.PJ_NO,B.ACTV_NO, NULL CHEQUE_VALUED,(TO_DATE('''|| P_t_date || ''',''DD/MM/YYYY'')-NVL(B.DOC_DATE,IAS_GEN_PKG.GET_FRST_DAY)) PER_NO,''' || P_terminal ||''' TRMNL_NAME,
                           B.BRN_NO,B.BRN_YEAR,B.CMP_NO,B.BRN_USR
                                        FROM CUSTOMER A,INSTALLMENT B
                                        WHERE A.C_CODE=B.C_CODE
                                        AND NVL(B.I_AMT,0)>(NVL(B.PAID_AMT,0)+NVL(B.ADJ_AMT,0))
                                        AND B.DR_NO IS NULL ' || P_whr;

            -- INSERT INTO TST_BA(SQL_V)VALUES(V_SQL);
            -- COMMIT;

            EXECUTE IMMEDIATE V_sql;
        END IF;
    END Cst_parnt_aging_prc;

    --##-------------------------------------------------------------------------------##--
    FUNCTION Get_bl_cst_fnc(P_loc_cur IN VARCHAR2,
                            P_cc_code IN Cost_centers.Cc_code%TYPE DEFAULT NULL,
                            P_c_code IN Customer.C_code%TYPE,
                            P_acy IN VARCHAR2,
                            P_fd IN DATE DEFAULT NULL,
                            P_td IN DATE DEFAULT NULL,
                            P_bal_type IN NUMBER DEFAULT 0)
        RETURN NUMBER IS
        Bl_amt   NUMBER := 0;
    BEGIN
        IF P_bal_type = 0 THEN                                                            -- Open_bal (1)
            SELECT DECODE(P_acy,
                          P_loc_cur, NVL(SUM(D.Dr_amt), 0) - NVL(SUM(D.Cr_amt), 0),
                          NVL(SUM(D.Dr_amt_f), 0) - NVL(SUM(D.Cr_amt_f), 0)
                         )
              INTO Bl_amt
              FROM Ias_post_dtl D, Customer C
             WHERE D.A_code = C.C_a_code
                   AND D.Ac_code_dtl = C.C_code
                   AND Ac_dtl_typ = 3
                   AND D.C_code = P_c_code
                   AND D.A_cy = P_acy
                   AND (D.Doc_date < P_fd OR D.Doc_type = 0)
                   AND NVL(D.Cc_code, '0') = DECODE(P_cc_code, NULL, NVL(D.Cc_code, '0'), P_cc_code);
        ELSE                                                                                   -- Balance
            IF P_fd IS NOT NULL AND P_td IS NOT NULL THEN                                           --(2)
                SELECT DECODE(P_acy,
                              P_loc_cur, NVL(SUM(D.Dr_amt), 0) - NVL(SUM(D.Cr_amt), 0),
                              NVL(SUM(D.Dr_amt_f), 0) - NVL(SUM(D.Cr_amt_f), 0)
                             )
                  INTO Bl_amt
                  FROM Ias_post_dtl D, Customer C
                 WHERE D.A_code = C.C_a_code
                       AND D.Ac_code_dtl = C.C_code
                       AND Ac_dtl_typ = 3
                       AND D.C_code = P_c_code
                       AND D.A_cy = P_acy
                       AND D.Doc_date BETWEEN P_fd AND P_td
                       AND NVL(D.Cc_code, '0') = DECODE(P_cc_code, NULL, NVL(D.Cc_code, '0'), P_cc_code);
            ELSIF P_td IS NOT NULL THEN                                                             --(2)
                SELECT DECODE(P_acy,
                              P_loc_cur, NVL(SUM(D.Dr_amt), 0) - NVL(SUM(D.Cr_amt), 0),
                              NVL(SUM(D.Dr_amt_f), 0) - NVL(SUM(D.Cr_amt_f), 0)
                             )
                  INTO Bl_amt
                  FROM Ias_post_dtl D, Customer C
                 WHERE D.A_code = C.C_a_code
                       AND D.Ac_code_dtl = C.C_code
                       AND Ac_dtl_typ = 3
                       AND D.C_code = P_c_code
                       AND D.A_cy = P_acy
                       AND D.Doc_date <= P_td
                       AND NVL(D.Cc_code, '0') = DECODE(P_cc_code, NULL, NVL(D.Cc_code, '0'), P_cc_code);
            ELSE                                                                                    --(2)
                SELECT DECODE(P_acy,
                              P_loc_cur, NVL(SUM(D.Dr_amt), 0) - NVL(SUM(D.Cr_amt), 0),
                              NVL(SUM(D.Dr_amt_f), 0) - NVL(SUM(D.Cr_amt_f), 0)
                             )
                  INTO Bl_amt
                  FROM Ias_post_dtl D, Customer C
                 WHERE D.A_code = C.C_a_code
                       AND D.Ac_code_dtl = C.C_code
                       AND Ac_dtl_typ = 3
                       AND D.C_code = P_c_code
                       AND D.A_cy = P_acy
                       AND NVL(D.Cc_code, '0') = DECODE(P_cc_code, NULL, NVL(D.Cc_code, '0'), P_cc_code);
            END IF;                                                                                 --(2)
        END IF;                                                                                     --(1)

        RETURN (NVL(Bl_amt, 0));
    EXCEPTION
        WHEN OTHERS THEN
            RETURN (0);
    END Get_bl_cst_fnc;

    --##-------------------------------------------------------------------------------##--
    FUNCTION Chk_prd_no(P_prd_no IN NUMBER DEFAULT NULL,
                        P_per_no IN NUMBER DEFAULT NULL,
                        P_f_day IN NUMBER DEFAULT NULL,
                        P_t_day IN NUMBER DEFAULT NULL)
        RETURN NUMBER IS
        V_flg   NUMBER := 0;
    BEGIN
        --##------------------------------------------------------------------------------------------------------------------------------------------------##--
        --## Check Days
        IF P_prd_no IS NOT NULL AND NVL(P_per_no, 0) <> 0 AND P_f_day IS NOT NULL THEN              --(1)
            IF P_per_no = 1 THEN
                IF P_prd_no > P_f_day THEN
                    V_flg   := 1;
                END IF;
            ELSIF P_per_no = 2 THEN
                IF P_prd_no < P_f_day THEN
                    V_flg   := 1;
                END IF;
            ELSIF P_per_no = 3 THEN
                IF P_prd_no = P_f_day THEN
                    V_flg   := 1;
                END IF;
            ELSIF P_per_no = 4 THEN
                IF P_prd_no >= P_f_day THEN
                    V_flg   := 1;
                END IF;
            ELSIF P_per_no = 5 THEN
                IF P_prd_no <= P_f_day THEN
                    V_flg   := 1;
                END IF;
            ELSIF P_per_no = 8 THEN                                                             --between
                IF P_prd_no BETWEEN P_f_day AND P_t_day THEN
                    V_flg   := 1;
                END IF;
            ELSE
                V_flg   := 1;
            END IF;
        ELSE
            V_flg   := 1;
        END IF;

        RETURN (V_flg);
    --##-------------------------------------------------------------------------------##--
    --##------------------------------------------------------------------------------------------------------------------------------------------------##--
    END;

    --##---------------------------------------------------------------------------------##--
    FUNCTION Get_rt_amt_fnc(P_doc_type IN NUMBER,
                            P_doc_ser IN NUMBER,
                            P_local_amt_flg IN NUMBER,
                            P_cc_code IN VARCHAR2 DEFAULT NULL,
                            P_pj_no IN VARCHAR2 DEFAULT NULL,
                            P_actv_no IN VARCHAR2 DEFAULT NULL,
                            P_prv_yr IN NUMBER DEFAULT 0,
                            P_t_date IN DATE DEFAULT NULL)
        RETURN NUMBER IS
        PRAGMA AUTONOMOUS_TRANSACTION;
        V_rt_bill_amt   NUMBER := 0;
        V_whr           VARCHAR2(3000);
        V_tbl_mst       VARCHAR2(500);
        V_tbl_dtl       VARCHAR2(500);
        V_tbl2_mst      VARCHAR2(500);
        V_tbl2_dtl      VARCHAR2(500);
        V_whr2          VARCHAR2(3000);
    BEGIN
        IF P_doc_type = 4 THEN
            IF NVL(P_prv_yr, 0) = 0 THEN
                V_tbl_mst    := 'IAS_RT_BILL_MST';
                V_tbl_dtl    := 'IAS_RT_BILL_Dtl';
                V_tbl2_mst   := 'IAS_BILL_MST_ADD_DISC';
                V_tbl2_dtl   := 'IAS_BILL_DTL_ADD_DISC';
            ELSE
                V_tbl_mst    := 'IAS_V_RT_BILL_MST_YR';
                V_tbl_dtl    := 'IAS_V_RT_BILL_Dtl_YR';
                V_tbl2_mst   := 'IAS_V_BILL_MST_ADD_DISC_YR';
                V_tbl2_dtl   := 'IAS_V_BILL_DTL_ADD_DISC_YR';
            END IF;

            -------------------------------------------------------------------
            /* If P_Cc_Code Is Not Null Then
               V_Whr := V_Whr ||' And Nvl(D.Cc_Code,''0'')='''||P_Cc_Code||'''';
             End If;
             -------------------------------------------------------------------
             If P_Pj_No Is Not Null Then
               V_Whr := V_Whr ||' And Nvl(D.Pj_No,''0'')='''||P_Pj_No||'''';
             End If;
             -------------------------------------------------------------------
             If P_Actv_No Is Not Null Then
               V_Whr := V_Whr ||' And Nvl(D.Actv_No,''0'')='''||P_Actv_No||'''';
             End If;*/
            IF P_t_date IS NOT NULL THEN
                V_whr    := V_whr || ' And Rt_Bill_Date <=''' || P_t_date || '''';
                V_whr2   := V_whr2 || ' And M.Doc_Date   <=''' || P_t_date || '''';
            END IF;

            -------------------------------------------------------------------
            V_rt_bill_amt   :=
                Ias_gen_pkg.Get_cnt('  Select nvl(Sum(Dtl_Amt * Per_Amt),0)
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
                                                                   (Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser ) * Decode(' || P_local_amt_flg || ',1,Nvl(Rt_Bill_Rate,1),1)  )bill_amt,
                                                                   Ac_Amt,
                                                                   Dtl_Amt,
                                                                   ((Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)- Ac_Amt)/Decode(Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser),0,1,Sum(Nvl(Dtl_Amt,0))Over(partition by rt_Bill_Ser)) ) Per_Amt
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
                                                                      From ' || V_tbl_mst || ' M, ' || V_tbl_dtl || ' D
                                                                     Where M.Rt_Bill_Ser = D.Rt_Bill_Ser
                                                                           And M.Rt_Bill_Doc_Type = 4
                                                                           And M.P_Year In (0, 3)' || V_whr || '
                                                                           And NVL(D.bill_ser,0)=' || P_doc_ser || '
                                                                                                                                     Union ALL
                                                                    Select m.DOC_NO  rt_Bill_no,
                                                                           m.DOC_SER rt_Bill_Ser,
                                                                           D.Bill_Ser,
                                                                           D.bill_no,
                                                                           M.Cc_Code,
                                                                           M.Pj_No,
                                                                           M.Actv_No,
                                                                           M.DOC_DATE Rt_Bill_Date,
                                                                           M.DOC_RATE Rt_Bill_Rate,
                                                                           Nvl(D.ADD_DIS_QTY, 0) * Nvl(D.ADD_DIS_AMT_DTL, 0)+(Nvl(D.Add_Dis_Qty,0)*Nvl(D.ADD_VAT_AMT,0)) Dtl_Amt,
                                                                           0 Ac_Amt
                                                                      From ' || V_tbl2_mst || ' M, ' || V_tbl2_dtl || ' D
                                                                     Where M.DOC_SER = D.DOC_SER AND NVL(NOTE_TYP,0)=1
                                                                           And M.BILL_DOC_TYPE = 4 ' || V_whr2 || '
                                                                           And NVL(D.bill_ser,0)=' || P_doc_ser || '
                                                                      )
                                                               )');
        END IF;

        RETURN (V_rt_bill_amt);
    EXCEPTION
        WHEN OTHERS THEN
            RETURN (0);
    -- Raise_Application_Error(-20002, 'ErrorinGet_Rt_Amt_Fnc '||Sqlerrm) ;
    END Get_rt_amt_fnc;

    --##---------------------------------------------------------------------------------##--
    PROCEDURE Insrt_adjst_instlmnt( P_brn_no IN S_brn.Brn_no%TYPE,
                                    P_c_code IN Customer.C_code%TYPE,
                                    P_doc_type_ref IN NUMBER,
                                    P_doc_no_ref IN NUMBER,
                                    P_doc_ser_ref IN NUMBER,
                                    P_doc_date_ref IN DATE,
                                    P_doc_amt_ref IN NUMBER,
                                    P_a_cy IN Ex_rate.Cur_code%TYPE,
                                    P_cc_code IN Cost_centers.Cc_code%TYPE DEFAULT NULL,
                                    P_bill_ser IN NUMBER,
                                    P_user_no IN NUMBER,
                                    P_brn_year IN NUMBER,
                                    P_cmp_no IN NUMBER,
                                    P_terminal IN VARCHAR2
                                   , P_brn_usr IN NUMBER,
                                   P_no_of_decimal IN NUMBER) IS
        V_cnt       NUMBER := 0;
        V_doc_no    NUMBER;
        V_doc_ser   NUMBER;
    BEGIN
        --## Check Exists
        BEGIN
            SELECT 1
              INTO V_cnt
              FROM Ias_adjst_installment_mst
             WHERE Doc_no_ref = P_doc_no_ref
                   AND Doc_type_ref = 5
                   AND NVL(Auto_adj_flg, 0) = 1
                   AND Doc_ser_ref = P_doc_ser_ref
                   AND ROWNUM <= 1;
        EXCEPTION
            WHEN OTHERS THEN
                V_cnt   := 0;
        END;

        IF NVL(V_cnt, 0) = 1 THEN
            BEGIN
                UPDATE Installment A
                   SET Adj_amt   =
                           NVL(Adj_amt, 0) - NVL(
                           (                     SELECT Paid_amt_doc
                                                   FROM Ias_adjst_installment_mst  M,
                           Ias_adjst_installment_dtl                               D
                                                  WHERE M.Doc_ser = D.Doc_ser
                           AND M.Doc_no_ref = P_doc_no_ref
                           AND M.Doc_type_ref = 5
                           AND NVL(M.Auto_adj_flg, 0) = 1
                           AND M.Doc_ser_ref = P_doc_ser_ref
                           AND D.Doc_ser_ref = P_bill_ser
                           AND D.I_no = A.I_no
                           AND D.A_cy = A.A_cy
                           AND NVL(D.Rcrd_no, 1) = NVL(A.Rcrd_no, 1)
                           AND NVL(D.I_py, 0) = NVL(A.I_py, 0)
                           AND D.C_code = A.C_code
                           AND NVL(D.Cc_code, '0') = NVL(A.Cc_code, '0')),
                           0)
                 WHERE Bill_ser = P_bill_ser;
            EXCEPTION
                WHEN OTHERS THEN
                    Raise_application_error(-20002,
                        'Err In Insrt_Adjst_Instlmnt  When Update Installment' || SQLERRM);
            END;
        END IF;


        BEGIN
            DELETE FROM
                Ias_adjst_installment_dtl
                  WHERE Doc_ser IN
                            (SELECT Doc_ser
                               FROM Ias_adjst_installment_mst
                              WHERE Doc_no_ref = P_doc_no_ref
                                    AND Doc_type_ref = 5
                                    AND NVL(Auto_adj_flg, 0) = 1
                                    AND Doc_ser_ref = P_doc_ser_ref);
        EXCEPTION
            WHEN OTHERS THEN
                Raise_application_error(-20002,
                    'Err When Delete From Ias_Adjst_Installment_Mst' || SQLERRM);
        END;

        BEGIN
            DELETE FROM
                Ias_adjst_installment_mst
                  WHERE Doc_no_ref = P_doc_no_ref
                        AND Doc_type_ref = 5
                        AND NVL(Auto_adj_flg, 0) = 1
                        AND Doc_ser_ref = P_doc_ser_ref;
        EXCEPTION
            WHEN OTHERS THEN
                Raise_application_error(-20002,
                    'Err When Delete From Ias_Adjst_Installment_Mst' || SQLERRM);
        END;

        BEGIN
            SELECT 1
              INTO V_cnt
              FROM Ias_adjst_installment_mst
             WHERE Doc_no_ref = P_doc_no_ref
                   AND Doc_type_ref = 5
                   AND NVL(Auto_adj_flg, 0) = 1
                   AND Doc_ser_ref = P_doc_ser_ref
                   AND ROWNUM <= 1;
        EXCEPTION
            WHEN OTHERS THEN
                V_cnt   := 0;
        END;

        IF NVL(V_cnt, 0) = 0 THEN
            BEGIN
                SELECT 1
                  INTO V_cnt
                  FROM Installment
                 WHERE Doc_type = 4
                       AND Bill_ser = P_bill_ser
                       AND NVL(I_amt, 0) > (NVL(Paid_amt, 0) + NVL(Adj_amt, 0))
                       AND DR_NO IS NULL  And Nvl(I_amt,0) >0
                       AND ROWNUM <= 1;
            EXCEPTION
                WHEN OTHERS THEN
                    V_cnt   := 0;
            END;

            BEGIN
                SELECT NVL(MAX(Doc_no), 0) + 1
                  INTO V_doc_no
                  FROM Ias_adjst_installment_mst;
            EXCEPTION
                WHEN OTHERS THEN
                    V_doc_no   := 1;
            END;

            IF V_doc_no IS NOT NULL THEN
                V_doc_ser   := P_brn_year || LPAD(P_brn_no, 6, '0') || V_doc_no;
            END IF;


            IF V_cnt > 0 AND V_doc_no IS NOT NULL THEN
                BEGIN
                    INSERT INTO Ias_adjst_installment_mst(Doc_no, Doc_ser, Doc_date, Doc_type_ref, Doc_no_ref, Doc_ser_ref, Doc_date_ref, C_code, Cc_code, A_cy
                                                          , Doc_amt_ref, Auto_adj_flg, Ad_u_id, Ad_date, Cmp_no, Brn_no, Brn_year, Brn_usr, Ad_trmnl_nm
                                                         )
                         VALUES (V_doc_no, V_doc_ser, SYSDATE, P_doc_type_ref, P_doc_no_ref, P_doc_ser_ref, P_doc_date_ref, P_c_code, P_cc_code, P_a_cy, P_doc_amt_ref, 1, P_user_no, SYSDATE, P_cmp_no, P_brn_no, P_brn_year, P_brn_usr
                                 , P_terminal);


                    INSERT INTO Ias_adjst_installment_dtl(Doc_no, Doc_ser, Doc_type_ref, C_code, Cc_code, A_cy, Doc_no_ref, Doc_ser_ref, I_no, Paid_amt_doc
                                                          , Rcrd_no, I_py, Paid_amt, I_amt, I_date, Cmp_no, Brn_no, Brn_year, Brn_usr
                                                         )
                          SELECT V_doc_no,
                                 V_doc_ser,
                                 4,
                                 P_c_code,
                                 P_cc_code,
                                 P_a_cy,
                                 Bill_no,
                                 Bill_ser,
                                 I_no,
                                 Paid_amt_doc,
                                 Rcrd_no,
                                 I_py,
                                 (NVL(Paid_amt, 0) + NVL(Adj_amt, 0))     Paid_amt,
                                 I_amt,
                                 I_date,
                                 P_cmp_no,
                                 P_brn_no,
                                 P_brn_year,
                                 P_brn_usr
                            FROM (SELECT Bill_doc_type,
                                         Bill_no,
                                         Bill_ser,
                                         Doc_date,
                                         I_no,
                                         I_date,
                                         I_amt,
                                         Ac_rate,
                                         Cheque_no,
                                         Cc_code,
                                         C_code,
                                         A_cy,
                                         Paid_amt,
                                         Paid_date,
                                         Adj_amt,
                                         Ref_no,
                                         Dr_no,
                                         I_py,
                                         Rcrd_no,
                                         Remind_amt,
                                         DECODE(
                                             SIGN(P_doc_amt_ref - Remind_amt),
                                             1, (I_amt - (NVL(Paid_amt, 0) + NVL(Adj_amt, 0))),
                                             0, (I_amt - (NVL(Paid_amt, 0) + NVL(Adj_amt, 0))),
                                             DECODE(
                                                 SIGN(I_amt - ABS(P_doc_amt_ref - Remind_amt)),
                                                 1, DECODE(
                                                        SIGN(P_doc_amt_ref - (I_amt - (NVL(Paid_amt, 0) + NVL(Adj_amt, 0)))),
                                                        1, ABS(P_doc_amt_ref - LAG(Remind_amt) OVER(ORDER BY I_no, I_date)),
                                                        P_doc_amt_ref),
                                                 0))    Paid_amt_doc
                                    FROM (SELECT Doc_type,
                                                 Bill_doc_type,
                                                 Bill_no,
                                                 Bill_ser,
                                                 Doc_date,
                                                 I_no,
                                                 I_date,
                                                 I_amt,
                                                 Ac_rate,
                                                 Cheque_no,
                                                 Cc_code,
                                                 C_code,
                                                 A_cy,
                                                 Paid_amt,
                                                 Paid_date,
                                                 Adj_amt,
                                                 Ref_no,
                                                 Dr_no,
                                                 I_py,
                                                 Rcrd_no,
                                                 (SUM(I_amt) OVER (ORDER BY I_no, I_date) - SUM(NVL(Paid_amt, 0) + NVL(Adj_amt, 0)) OVER(ORDER BY I_no, I_date))    Remind_amt
                                            FROM Installment
                                           WHERE Bill_ser = P_bill_ser
                                                 AND NVL(I_amt, 0) > (NVL(Paid_amt, 0) + NVL(Adj_amt, 0))
                                                 AND DR_NO IS NULL  And Nvl(I_amt,0) >0 ))
                           WHERE NVL(Paid_amt_doc, 0) > 0
                        ORDER BY I_no, I_date;
                EXCEPTION
                    WHEN OTHERS THEN
                        Raise_application_error(-20002,
                            'Err When Insrt  Ias_Adjst_Installment_Dtl' || SQLERRM);
                END;
            END IF;

            BEGIN
                SELECT 1
                  INTO V_cnt
                  FROM Ias_adjst_installment_mst M, Ias_adjst_installment_dtl D
                 WHERE M.Doc_ser = D.Doc_ser AND NVL(M.Auto_adj_flg, 0) = 1 AND ROWNUM <= 1;
            EXCEPTION
                WHEN OTHERS THEN
                    V_cnt   := 0;
            END;

            IF NVL(V_cnt, 0) > 0 THEN
                BEGIN
                    UPDATE Installment A
                       SET Adj_amt   =
                               NVL(Adj_amt, 0) + NVL(
                               (                     SELECT Paid_amt_doc
                                                       FROM Ias_adjst_installment_dtl
                                                      WHERE Doc_ser = V_doc_ser
                               AND Doc_ser_ref = P_bill_ser
                               AND I_no = A.I_no
                               AND A_cy = A.A_cy
                               AND NVL(Rcrd_no, 1) = NVL(A.Rcrd_no, 1)
                               AND NVL(I_py, 0) = NVL(A.I_py, 0)
                               AND C_code = A.C_code
                               AND NVL(Cc_code, '0') = NVL(A.Cc_code, '0')),
                               0)
                     WHERE Bill_ser = P_bill_ser;
                EXCEPTION
                    WHEN OTHERS THEN
                        Raise_application_error(-20002,
                            'Err In Insrt_Adjst_Instlmnt  When Update Installment' || SQLERRM);
                END;
            END IF;
        END IF;
    END Insrt_adjst_instlmnt;
--##---------------------------------------------------------------------------------##--
END Ias_dstr_cst_dr_pkg;