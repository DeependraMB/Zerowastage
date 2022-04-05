using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class Payment_Default : System.Web.UI.Page
{
   
    protected void Page_Load(object sender, EventArgs e)
    {
        if (!IsPostBack)
        {
           
            lblCardNumber.Text  = Session["accno"].ToString();

            
            lbl_Amount.Text = Session["amount"].ToString();
        }
    }

    protected void lblCopyIt_Click(object sender, EventArgs e)
    {
        //Code to copy address from table

        DataSet dt = new DataSet();
        dt = CRUD.selDSet("select_user_detailss", Session["uid"].ToString());
        if (dt.Tables[0].Rows.Count > 0)
        {
            txtName.Text = dt.Tables[0].Rows[0]["name"] .ToString();
            txtEmail.Text = dt.Tables[0].Rows[0]["email"].ToString();
            txtPhone.Text = dt.Tables[0].Rows[0]["phone_no"].ToString();
            Session["name"] = txtName.Text;
        }
    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        CRUD.insUpDel("make_payment", lbl_Amount.Text, DateTime.Now.Date, Session["uid"].ToString());
        Response.Redirect("~/Payment/Third.aspx");
    }

}