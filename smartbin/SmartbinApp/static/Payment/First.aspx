<%@ Page Title="" Language="C#" MasterPageFile="~/Payment/Payment.master" AutoEventWireup="true" CodeFile="First.aspx.cs" Inherits="Payment_Default" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
    <style type="text/css">
        .auto-style15 {
            height: 134px;
        }
        .auto-style18 {
            text-align: right;
            width: 492px;
        }
        .style5 {}
        .auto-style19 {
            width: 58px;
            height: 31px;
        }
        .auto-style20 {
            height: 52px;
        }
        .auto-style21 {
            height: 23px;
        }
        .auto-style22 {
            height: 52px;
            width: 492px;
        }
        .auto-style23 {
            width: 492px;
        }
        .auto-style24 {
            height: 23px;
            width: 492px;
        }
        .auto-style25 {
            color: #3366FF;
        }
        .auto-style26 {
            text-align: right;
            width: 492px;
            color: #3366FF;
        }
    </style>
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
    <fieldset><legend style="font-weight: 700; text-align: center; font-size: large;">Enter Your Card Details</legend>
    <table class="auto-style1">
        <tr>
            <td class="auto-style20"></td>
            <td class="auto-style22"></td>
            <td class="auto-style20"></td>
            <td class="auto-style20"></td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style18">Choose your card type</td>
            <td style="vertical-align:middle;"> <asp:RadioButton ID="RadioButton1" runat="server" Text="Visa" Checked="True" 
                    GroupName="1" ValidationGroup="1" Width="57px" CssClass="style5" />
                <img alt="" class="auto-style19" src="Images/1391796960_payment_method_card_visa.png" />&nbsp;&nbsp; <asp:RadioButton ID="RadioButton2" runat="server" Text="Master Card" 
                    GroupName="1" ValidationGroup="1" Width="108px" CssClass="style5" 
                   /><img alt="" class="auto-style19" src="Images/1391796956_payment_method_master_card.png" /></td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style18">Enter your card number</td>
            <td>
                <asp:TextBox ID="TextBox1" runat="server" ontextchanged="TextBox1_TextChanged" Width="240px"></asp:TextBox>
                 
                <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ControlToValidate="TextBox1" ErrorMessage="*" ForeColor="#FF3300"></asp:RequiredFieldValidator>
                 <asp:RegularExpressionValidator ID="RegularExpressionValidator1" runat="server" 
                    ControlToValidate="TextBox1" ErrorMessage="Card not valid (16 Digits required)" 
                    ValidationExpression="^[0-9]{16}$" ForeColor="Red"></asp:RegularExpressionValidator>
            </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style18">Enter 4 digit Confirmation PIN</td>
            <td>
                <asp:TextBox ID="TextBox2" runat="server" CssClass="style4" OnTextChanged="TextBox2_TextChanged"></asp:TextBox>
                 
                <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ControlToValidate="TextBox2" ErrorMessage="*" ForeColor="#FF3300"></asp:RequiredFieldValidator>
                 <asp:RegularExpressionValidator ID="RegularExpressionValidator2" runat="server" 
                    ControlToValidate="TextBox2" ErrorMessage="PIN not valid (4 Digits required)" 
                    ValidationExpression="^[0-9]{4}$" ForeColor="Red"></asp:RegularExpressionValidator>
            </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style26">&nbsp;</td>
            <td>
                <asp:CheckBox ID="CheckBox1" runat="server" CssClass="auto-style25" />
                <span class="auto-style25">&nbsp;I Accept the Terms &amp; Conditions</span></td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>
                <asp:Label ID="Label1" runat="server" ForeColor="Red"></asp:Label>
            </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>
                <asp:Button ID="Button1" runat="server" Font-Bold="True" onclick="Button1_Click" Text="Continue " Width="180px" />
            </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td class="auto-style21"></td>
            <td class="auto-style24"></td>
            <td class="auto-style21"></td>
            <td class="auto-style21"></td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td class="auto-style23">&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </table>
        </fieldset>
</asp:Content>

