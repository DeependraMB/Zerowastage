<%@ Page Title="" Language="C#" MasterPageFile="~/Payment/Payment.master" AutoEventWireup="true" CodeFile="Fifth.aspx.cs" Inherits="Payment_Default" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
    <style type="text/css">
        .auto-style18 {
            height: 35px;
        }
        .auto-style21 {
            height: 39px;
        }
        .auto-style24 {
            width: 50px;
            height: 30px;
        }
        .auto-style28 {
            width: 34px;
            height: 27px;
        }
        .auto-style29 {
            height: 55px;
        }
        .auto-style30 {
            text-align: right;
            font-weight: 700;
            width: 545px;
            height: 29px;
        }
        .auto-style31 {
            width: 15px;
            height: 29px;
        }
        .auto-style32 {
            height: 29px;
        }
        .auto-style33 {
            text-align: right;
            font-weight: 700;
            width: 545px;
            height: 30px;
        }
        .auto-style34 {
            width: 15px;
            height: 30px;
        }
        .auto-style35 {
            height: 30px;
        }
        .auto-style36 {
            text-align: right;
            font-weight: 700;
            width: 545px;
            height: 32px;
        }
        .auto-style37 {
            width: 15px;
            height: 32px;
        }
        .auto-style38 {
            height: 32px;
        }
        .auto-style39 {
            height: 108px;
        }
    </style>
   <script type="text/javascript">
 <!--
    function printPartOfPage(elementId) {
        var printContent = document.getElementById(elementId);
        var windowUrl = 'about:blank';
        var uniqueName = new Date();
        var windowName = 'Print' + uniqueName.getTime();
        var printWindow = window.open(windowUrl, windowName, 'left=50000,top=50000,width=0,height=0');

        printWindow.document.write(printContent.innerHTML);
        printWindow.document.close();
        printWindow.focus();
        printWindow.print();
        printWindow.close();
    }
    // -->
    </script>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
     <div id="printablediv"><fieldset><legend style="text-align: center; font-weight: 700">Payment Details</legend>
       
        <table class="auto-style1">
            <tr>
                <td class="auto-style29"></td>
                <td style="text-align: right" class="auto-style29">
                    <asp:LinkButton ID="LinkButton1" runat="server" OnClientClick="JavaScript: printPartOfPage('printablediv');" Font-Underline="False" ForeColor="White"> <img alt="" class="auto-style28" src="Icons/1391813769_printer.png" /></asp:LinkButton>
                   </td>
                <td class="auto-style29"></td>
            </tr>
            <tr>
                <td class="auto-style18"></td>
                <td class="auto-style18" style="text-align: center; color: #3399FF">Payment Success...</td>
                <td class="auto-style18"></td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>
                    <table class="auto-style1">
                        <tr>
                            <td class="auto-style30">Merchant</td>
                            <td class="auto-style31"></td>
                            <td class="auto-style32">
                                &nbsp;<asp:Label ID="lblMurchant" runat="server"></asp:Label>
                            </td>
                        </tr>
                        <tr>
                            <td class="auto-style33">Date</td>
                            <td class="auto-style34"></td>
                            <td class="auto-style35">
                                &nbsp;<asp:Label ID="lblDate" runat="server"></asp:Label>
                            </td>
                        </tr>
                        <tr>
                            <td class="auto-style36">Amount</td>
                            <td class="auto-style37"></td>
                            <td class="auto-style38">
                                Rs.<asp:Label ID="lblAmoubnt" runat="server"></asp:Label>
                                <strong>/-</strong></td>
                        </tr>
                        <tr>
                            <td class="auto-style36">Transaction ID</td>
                            <td class="auto-style37"></td>
                            <td class="auto-style38">&nbsp; <asp:Label ID="lblTID" runat="server"></asp:Label>
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3" class="auto-style21" style="text-align: center">
                                <asp:Button ID="Button1" runat="server" Text="Continue" Width="108px" OnClick="Button1_Click" style="font-weight: 700" />
                            </td>
                        </tr>
                    </table>
                </td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td class="auto-style39"></td>
                <td style="text-align: center" class="auto-style39">&nbsp;&nbsp;&nbsp;
                    <img alt="" class="auto-style24" src="Icons/1391813453_mastercard1.gif" />
                    <img alt="" class="auto-style24" src="Icons/1391813456_visa2.gif" />
                    <img alt="" class="auto-style24" src="Icons/1391813466_westernunion.gif" />
                    <img alt="" class="auto-style24" src="Icons/1391813469_cirrus1.gif" />
                    <img alt="" class="auto-style24" src="Icons/1391813513_visa1.gif" /></td>
                <td class="auto-style39"></td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
        </table>
        
    </fieldset></div>
</asp:Content>

